---
title: "Configure site mailboxes in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 9/20/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 57b7618a-2ca4-450d-aa8b-77bce21a9884
description: "Configure Exchange Server, SharePoint Server for team email by using the Site Mailboxes feature."
---

# Configure site mailboxes in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
This article describes how to configure Site Mailboxes in SharePoint Server and Exchange Server. The Site Mailboxes feature provides SharePoint Server users with team email on a site. Site Mailboxes also provides links to SharePoint document libraries in Microsoft Outlook, enabling users to share files and email messages with other members of a team that are working on a joint project. 
  
## Before you begin
<a name="begin"> </a>

Before you begin this operation, review the following information about prerequisites:
  
- Site Mailboxes requires Exchange Server 2016 or Exchange Server 2013.
    
- Any previous version of Exchange Web Services (EWS) will need to be uninstalled from the SharePoint servers.
    
    > [!NOTE]
    > You may need to determine if a previous version of EWS is installed. If so, please run the Check-SiteMailboxConfig script referenced below. 
  
- Site Mailboxes feature requires that user profile synchronization be configured in the farm. For information about configuring user profile synchronization, see [User profiles and identities](user-profiles-and-identities.md), and [Manage user profile synchronization in SharePoint Server](manage-profile-synchronization.md).
    
- Site Mailboxes feature requires that the app management service application be configured in the farm. For information about configuring the app management service application, see [New-SPAppManagementServiceApplication](/powershell/module/sharepoint-server/New-SPAppManagementServiceApplication?view=sharepoint-ps).
    
- Secure Sockets Layer (SSL) configured for the Default Zone is a requirement for web applications that are deployed in scenarios that support server-to-server authentication and app authentication. This is such a scenario. As a prerequisite for configuring Site Mailboxes, the computer that is running SharePoint Server must have SSL configured. For more information, see [Create claims-based web applications in SharePoint Server](/previous-versions/office/sharepoint-server-2010/ee806885(v=office.14)) and follow the steps for creating an SSL site collection and server certificate. 
    
Note that you may need to import the Exchange Server SSL certificate from Exchange Server to SharePoint Server, and from SharePoint Server to Exchange Server. This is only necessary if the certificate is not trusted for the API endpoints (such as a Self-SSL Certificate in a lab environment). 
To import an untrusted SSL certificate to a new server: 
- Open Internet Explorer and navigate to Outlook Web App (if the deployment is on SharePoint Server) or the SSL SharePoint site (if the deployment is on Exchange Server): https://\<ExServerName\>/owa or https://\<SP_FQDN\>. 
- Accept to trust the certificate by clicking **Continue to website**. 
- Click **Certificate Error** info in Internet Explorer next to the Address bar, and then click **View Certificates**. 
- Select **Install Certificate** and then select **Place all certificates in the following store**. 
- Select the checkbox to show physical stores. 
- Install the certificate to Trusted Root Certification Authorities > Local Computer. 
  
- In order to perform these procedures, you must be a member of the SharePoint and Exchange Server administrator groups and have an operational Exchange Server with end-user mailboxes.
    
- A SharePoint backup solution will not incorporate Exchange site mailboxes. An Exchange administrator will need to ensure timely backups of site mailboxes are taking place.
    
- Users who access files in a SharePoint document library from a Site Mailbox must have the document library configured as a trusted site in their browser or a warning will appear that asks the user if she or he wants to trust the file.
    
## Configure SharePoint for Site Mailboxes in SharePoint Server
<a name="begin"> </a>

The first step in configuring Site Mailboxes is to install the Exchange Server Web Services API on each web and application server in the SharePoint Server farm.
  
 **Install Exchange Web Services API on SharePoint Server**
  
1. Download EWSManagedAPI.msi from the [Microsoft Download Center](https://www.microsoft.com/en-us/download/details.aspx?id=42951) and save it to a folder on each web and application server. 
    
2. Open a command window as administrator and navigate to the folder where you saved EWSManagedAPI.msi.
    
3. Run the following command:
    
   ```
   msiexec /I EwsManagedApi.msi addlocal="ExchangeWebServicesApi_Feature"
   ```

4. Reset IIS from the command line by typing IISReset.
    
## Establish OAuth Trust and Service Permissions on SharePoint Server
<a name="begin"> </a>

The next step is to copy the following two scripts. The first should be saved as Set-SiteMailboxConfig.ps1 and the second should be saved as Check-SiteMailboxConfig.ps1.
  
Set-SiteMailboxConfig.ps1:
  
```
# .SYNOPSIS
#
# Set-SiteMailboxConfig helps configure Site Mailboxes for a SharePoint farm
#
# .DESCRIPTION
#
# Establishes trust with an Exchange Server, sets Site Mailbox settings and enables Site Mailboxes for a farm.
#
# .PARAMETER ExchangeSiteMailboxDomain
#
# The FQDN of the Exchange Organization where Site Mailboxes will be created
#
# .PARAMETER ExchangeAutodiscoverDomain
#
# [Optional] The FQDN of an Exchange Autodiscover Virtual Directory
#
# .PARAMETER WebApplicationUrl
#
# [Optional] The URL of a specific web application to configure. If not specified all Web Applications will be configured
#
# .PARAMETER Force
#
# [Optional] Indicate that the script should ignore any configuration issues and enable Site Mailboxes anyway
#
Param
(
   [Parameter(Mandatory=$true)]
   [ValidateNotNullOrEmpty()]   
   [string]$ExchangeSiteMailboxDomain,
   [Parameter(Mandatory=$false)]
   [ValidateNotNullOrEmpty()]   
   [string]$ExchangeAutodiscoverDomain,
   [Parameter(Mandatory=$false)]
   [ValidateNotNullOrEmpty()]   
   [string]$WebApplicationUrl,
   [Parameter(Mandatory=$false)]
   [switch]$Force
)
$script:currentDirectory = Split-Path $MyInvocation.MyCommand.Path
if($WebApplicationUrl -ne $NULL -and $WebApplicationUrl -ne "")
{
    $webapps = Get-SPWebApplication $WebApplicationUrl
}
else
{
    $webapps = Get-SPWebApplication
}
if($webapps -eq $NULL)
{
    if($WebApplicationUrl -ne $NULL)
    {
        Write-Warning "No Web Application Found at $($WebApplicationUrl). Please create a web application and re-run Set-SiteMailboxConfig"
    }
    else
    {
        Write-Warning "No Web Applications Found. Please create a web application and re-run Set-SiteMailboxConfig"
    }
    
    return
}
$rootWeb = $NULL
foreach($webapp in $webapps)
{
    if($rootWeb -eq $NULL)
    {
        $rootWeb = Get-SPWeb $webApp.Url -EA SilentlyContinue
    }
}
if($rootWeb -eq $NULL)
{
    Write-Warning "Unable to find a root site collection. Please create a root site collection on a web application and re-run Set-SiteMailboxConfig"
    return
}
$exchangeServer = $ExchangeAutodiscoverDomain
if($exchangeServer -eq $NULL -or $exchangeServer -eq "")
{
    $exchangeServer = "autodiscover.$($ExchangeSiteMailboxDomain)"
}
Write-Host "Establishing Trust with Exchange Server: $($exchangeServer)"
$metadataEndpoint = "https://$($exchangeServer)/autodiscover/metadata/json/1"
$exchange = Get-SPTrustedSecurityTokenIssuer | Where-Object { $_.MetadataEndpoint -eq $metadataEndpoint }
if($exchange -eq $NULL)  
{
    $exchange = New-SPTrustedSecurityTokenIssuer -Name $exchangeServer -MetadataEndPoint $metadataEndpoint
}
if($exchange -eq $NULL)
{
    Write-Warning "Unable to establish trust with Exchange Server $($exchangeServer). Ensure that $($metadataEndpoint) is accessible."
    if($ExchangeAutodiscoverDomain -eq $NULL -or $ExchangeAutodiscoverDomain -eq "")
    {
        Write-Warning "If $($metadataEndpoint) does not exist you may specify an alternate FQDN using ExchangeAutodiscoverDomain."
    }
    return
}
Write-Host "Granting Permissions to Exchange Server: $($exchangeServer)"
$appPrincipal = Get-SPAppPrincipal -Site $rootWeb.Url -NameIdentifier $exchange.NameId
Set-SPAppPrincipalPermission -AppPrincipal $appPrincipal -Site $rootWeb -Scope SiteSubscription -Right FullControl -EnableAppOnlyPolicy
Write-Host
Write-Host
Write-Host "Verifying Site Mailbox Configuration"
$warnings = & $script:currentDirectory\Check-SiteMailboxConfig.ps1 -ReturnWarningState
if($warnings -and -not $Force)
{
    Write-Warning "Pre-requisites not satisfied. Stopping Set-SiteMailboxConfig. Use -Force to override"
    return
}
elseif($warnings)
{
    Write-Warning "Pre-requisites not satisfied. -Force used to override"
}
foreach($webapp in $webapps)
{
    Write-Host "Configuring Web Application: $($webapp.Url)"
    Write-Host "Setting Exchange Site Mailbox Domain to $($ExchangeSiteMailboxDomain)"
    $webapp.Properties["ExchangeTeamMailboxDomain"] = $ExchangeSiteMailboxDomain
        
    if($ExchangeAutodiscoverDomain -ne $NULL -and $ExchangeAutodiscoverDomain -ne "")
    {
        Write-Host "Setting Exchange Autodiscover Domain to $($ExchangeAutodiscoverDomain)"
        $webapp.Properties["ExchangeAutodiscoverDomain"] = $ExchangeAutodiscoverDomain;
    }
    $webapp.Update()
}
$feature = Get-SPFeature CollaborationMailboxFarm -Farm -ErrorAction Ignore
if($feature -eq $NULL)
{
    Write-Host "Enabling Site Mailboxes for Farm"
    Enable-SPFeature CollaborationMailboxFarm
}
else
{
    Write-Host "Site Mailboxes already enabled for Farm"
}
```

Check-SiteMailboxConfig.ps1:
  
```
Param
(
   [Parameter(Mandatory=$false)]
   [ValidateNotNullOrEmpty()]   
   [switch]$ReturnWarningState
)
Add-PSSnapin Microsoft.SharePoint.Powershell
$anyWarnings = $false
Write-Host "Step 1: Checking for Exchange Web Services"
try
{
    $assm = [System.Reflection.Assembly]::Load("Microsoft.Exchange.WebServices, Version=15.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35")
    if($assm.GlobalAssemblyCache)
    {
        Write-Host -Foreground Green "Found Exchange Web Services in Global Assembly Cache"
        Write-Host "Exchange Web Services Version: $([System.Diagnostics.FileVersionInfo]::GetVersionInfo($assm.Location).FileVersion)"
    }
    else
    {
        Write-Warning "Unable to find Exchange Web Services in Global Assembly Cache"
        $anyWarnings = $true
    }
}
catch
{
    Write-Warning "Unable to find Exchange Web Services in Global Assembly Cache"
    $anyWarnings = $true
}
Write-Host
Write-Host
Write-Host "Step 2: Checking for https web application"
$webapps = Get-SPWebApplication -EA SilentlyContinue
$rootWeb = $NULL
if($webapps -ne $NULL)
{
    $sslWebAppExists = $false
    foreach($webapp in $webapps)
    {
        if($rootWeb -eq $NULL)
        {
            $rootWeb = Get-SPWeb $webApp.Url -EA SilentlyContinue
        }
        if(-not $webapp.Url.StartsWith("https://"))
        {
            Write-Warning "Web Application at $($webapp.Url) does not use HTTPS. Site Mailboxes will not work on this Web Application."
        }
        else
        {
            $sslWebAppExists = $true
            Write-Host -Foreground Green "Found Web Application at $($webapp.Url) that uses HTTPS"
        }
    }
    if(-not $sslWebAppExists)
    {
        Write-Warning "At least one Web Application must be configured for HTTPS in the default zone."
        $anyWarnings = $true
    }
}
else
{
    Write-Warning "No Web Applications Found. Please create a web application and re-run Check-SiteMailboxConfig"
    $anyWarnings = $true
    if($ReturnWarningState)
    {
        return $anyWarnings
    }
    return;
}
if($rootWeb -eq $NULL)
{
    Write-Warning "Unable to find any Sites. Please create a root site collection on a web application and re-run Check-SiteMailboxConfig"
    $anyWarnings = $true
    if($ReturnWarningState)
    {
        return $anyWarnings
    }
    return;
}
# Get App Permissions Management Objects
$appPrincipalManager = [Microsoft.SharePoint.SPAppPrincipalManager]::GetManager($rootWeb)
$appPrincipalPermissionsManager = New-Object -TypeName Microsoft.SharePoint.SPAppPrincipalPermissionsManager -ArgumentList $rootWeb        
Write-Host
Write-Host
Write-Host "Step 3: Checking for trusted Exchange Servers"
$trustedIssuers = Get-SPTrustedSecurityTokenIssuer
$trustedIssuerHosts = @()
if($trustedIssuers -ne $NULL)
{
    $foundTrustedIssuer = $false
    foreach($trustedIssuer in $trustedIssuers)
    {
        if($trustedIssuer.RegisteredIssuerName.StartsWith("00000002-0000-0ff1-ce00-000000000000@"))
        {
            if($trustedIssuer.IsSelfIssuer)
            {
                $foundTrustedIssuer = $true
                $uri = New-Object -TypeName System.Uri -ArgumentList $trustedIssuer.MetadataEndPoint
                
                Write-Host -Foreground Green "Found trusted Exchange Server at $($uri.Host)"
                $appPrincipalName = [Microsoft.SharePoint.SPAppPrincipalName]::CreateFromNameIdentifier($trustedIssuer.RegisteredIssuerName)
                $appPrincipal = $appPrincipalManager.LookupAppPrincipal([Microsoft.SharePoint.SPAppPrincipalIdentityProvider]::External, $appPrincipalName);
                
                if($appPrincipal -ne $NULL)
                {
                    $isValidAppPrincipal = $true;
                    if($appPrincipalPermissionsManager.GetAppPrincipalSiteSubscriptionContentPermission($appPrincipal) -eq [Microsoft.SharePoint.SPAppPrincipalPermissionKind]::FullControl)
                    {
                        Write-Host -Foreground Green "Exchange Server at $($uri.Host) has Full Control permissions"
                        
                    }
                    else
                    {
                        Write-Warning "Exchange Server at $($uri.Host) does not have Full Control permissions"
                        $isValidAppPrincipal = $false;
                        $anyWarnings = $true
                    }
                    if($appPrincipalPermissionsManager.IsAppOnlyPolicyAllowed($appPrincipal))
                    {
                        Write-Host -Foreground Green "Exchange Server at $($uri.Host) has App Only Permissions"
                    }
                    else
                    {
                        Write-Warning "Exchange Server at $($uri.Host) does not have App Only Permissions"
                        $isValidAppPrincipal = $false;
                        $anyWarnings = $true
                    }
                    
                    if($isValidAppPrincipal)
                    {
                        $trustedIssuerHosts += $uri.Host
                    }
                }
                else
                {
                    Write-Warning "Unable to get App Principal for $($uri.Host). Unable to check permissions for this Exchange Server"
                    $anyWarnings = $true
                }
            }
            else
            {
                Write-Warning "Found trusted Exchange Server at $($uri.Host) but it is not a Self Issuer"
                $anyWarnings = $true
            }
        }
    }
    if(-not $foundTrustedIssuer)
    {
        Write-Warning "Unable to find any trusted Exchange Servers"
        $anyWarnings = $true
    }
}
else
{
    Write-Warning "Unable to find any trusted Exchange Servers"
    $anyWarnings = $true
}
Write-Host
Write-Host
Write-Host "Step 4: Report current Site Mailbox Configuration"
if($webapps -ne $NULL)
{
    foreach($webapp in $webapps)
    {
        Write-Host
        Write-Host "Web Application Site Mailbox Configuration: $($webapp.Url)"
        Write-Host "Exchange Site Mailbox Domain: $($webapp.Properties["ExchangeTeamMailboxDomain"])"
        
        if($webapp.Properties["ExchangeAutodiscoverDomain"] -ne $NULL)
        {
            Write-Host "Exchange Autodiscover Domain: $($webapp.Properties["ExchangeAutodiscoverDomain"])"
        }
    }
}
Write-Host
Write-Host "Trusted Exchange Services: $([String]::Join(", ", $trustedIssuerHosts))"
$feature = Get-SPFeature CollaborationMailboxFarm -Farm -ErrorAction Ignore
if($feature -eq $NULL)
{
    Write-Host -ForegroundColor Red "Site Mailboxes are NOT enabled for Farm"
}
else
{
    Write-Host -ForegroundColor Green "Site Mailboxes are enabled for Farm"
}
if($ReturnWarningState)
{
    return $anyWarnings
}
```

Save the two .ps1 files to the same folder on a SharePoint Server Front-end or Application server, as one script calls the other during execution. In a Microsoft PowerShell window (right-click the PowerShell icon and choose **Run As Administrator** to open), navigate to the folder containing the .ps1 files and run the Set-SiteMailboxConfig.ps1 script. This allows users to do the following: 
  
- Retrieve and install the Exchange metadata, giving the Exchange service principal full control permissions to the SharePoint site subscription
    
- Enable the site mailbox feature in the SharePoint environment
    
- (optional) Set the Exchange site mailbox target domain, if DNS for the domain hasn't been configured for AutoDiscover
    
The Check-SiteMailboxConfig.ps1 is called as part of the Set-SiteMailboxConfig script, and it confirms that the configuration has been successful (it can also be run separately).
  
The format should be as follows:

```
   .\Set-SiteMailboxConfig.ps1 -ExchangeSiteMailboxDomain \<Domain\> -ExchangeAutodiscoverDomain [Exchange Server] -WebApplicationUrl [URL]
```  
Where \<Domain\> equals the FQDN of the domain your Exchange Server is in, and \<Exchange Server\> is the Exchange Server that you intend to connect to. This is a required parameter.
  
Optional parameters are [Exchange Server], which is the Exchange Server you intend to connect to (this is needed if Autodiscover is not enabled or properly configured) and [URL], which would be a specific URL that you may be configuring (typically used in an environment with SSL and non-SSL web applications).
  
Example: 
```
   .\Set-SiteMailboxConfig.ps1 -ExchangeSiteMailboxDomain tailspintoys.com -ExchangeAutodiscoverDomain exchange1.tailspintoys.com -WebApplicationUrl https://tailspintoys.com
```
If you encounter an error while running the script, refer to the "Troubleshooting" section in this article for guidance.
  
## Configure Exchange Server for Site Mailboxes
<a name="begin"> </a>

The final step is to establish OAuth trust, and service permissions, on the Exchange server.
  
 **Establish OAuth Trust and Service Permission on Exchange**
  
1. On your instance of Exchange Server open the Exchange Management PowerShell window as Administrator and change to the "C:\Program Files\Microsoft\Exchange Server\V15\Scripts" directory .
    
2. Run the following command:
    
   ```
   .\Configure-EnterprisePartnerApplication.ps1 -ApplicationType Sharepoint -AuthMetadataUrl https://<SP_FQDN>/_layouts/15/metadata/json/1
   ```

    Where \<SP_FQDN> is the URL to the SharePoint SSL root site collection that you want to configure.
    
## Troubleshooting
<a name="touble"> </a>

Please review the following table if you encounter issues.
  
**Table of error codes for reference when you run a configuration checklist script**

|**Error Code**|**Error**|**Notes**|
|:-----|:-----|:-----|
|0  <br/> |NoError  <br/> |Review Prerequisites.  <br/> |
|1  <br/> |ExchangeClientNotAvailable  <br/> |EWS client was not found on the SharePoint WFE. Run the Check script and ensure the entries are properly in the GAC; you may need to reinstall the EWS client.  <br/> |
|2  <br/> |UnsupportedVersion  <br/> |EWS client version is incompatible with SharePoint. Run the Check script to ensure the version meets minimum requirements. Alternatively, the Exchange server may be 2010 or earlier.  <br/> |
|3  <br/> |InvalidUser  <br/> |The TeamMailboxDomain parameter is not a valid FQDN or SMTP address.  <br/> |
|4  <br/> |UnauthorizedUser  <br/> |The script received a 401 from the Exchange Server, review the Exchange setup steps.  <br/> |
|5  <br/> |ServerBusy  <br/> |Exchange timed out during AutoDiscovery. It should be intermittent, please retry, but if it is persistent, follow-up with the Exchange Administrator.  <br/> |
|6  <br/> |URLNotAvailable  <br/> |AutoDiscovery failed to return a URL for ECP/OWA, which means typically that the EWS client version is incompatible with SharePoint. It may also mean Site Mailboxes are not enabled on Exchange, which would require follow-up with the Exchange Administrator.  <br/> |
|7  <br/> |OAuthNotSupported  <br/> |Unsuccessful in generating an OAuth token on behalf of SharePoint. This is typically caused by claims-based authentication being disabled on the SharePoint web application.  <br/> |
|8  <br/> |OAuthException  <br/> |An error occurred during the OAuth handshake between SharePoint and Exchange. This is typically caused by server to server configuration issues, such as a realm value mismatch on either side, certificate issues for Exchange or SharePoint, etc. Review certificates and attempt to establish or reestablish trust.  <br/> |
|9  <br/> |InvalidAutodiscoverDomain  <br/> |The AutoDiscover domain property is not set to a valid FQDN.  <br/> |
|10  <br/> |UnknownError  <br/> |An unknown error condition has occurred. Run the Check script and confirm that a valid, trusted instance of SharePoint is available, review prerequisites, confirm AutoDiscover has been set-up properly with the Exchange Administrator.  <br/> |
|101  <br/> |OAuthNotSupportedOverHttp  <br/> |If this error is thrown, your web application's default zone is not set to SSL, and AllowOauthoverHttp is also set to false. Run the Check script to ensure that any web application you intend to host site mailboxes are set with SSL in the default zone, as outlined in the prerequisites.  <br/> |
|102  <br/> |AssociatedOwnersGroupNull  <br/> |One or both of the default Owners and Members groups for the site have been deleted. Each of these two default groups are required to exist on any site where users install site mailboxes. A site administrator should be able to direct a site owner to recreated these required groups.  <br/> |
|103  <br/> |ExchangeTeamMailboxDomainNotSet  <br/> |The ExchangeTeamMailboxDomain property has not been set.  <br/> |
|104  <br/> |ExchangeAppPrincipalNotFound  <br/> |No Exchange app principals were found to be trusted. Typically, this means the New-SPTrustedSecureTokenService step was missed. Run the Check script and ensure that the app principal URL(s) outputted are the correct one(s).  <br/> |
|105  <br/> |ExchangeAppPrincipalMissingPermissions  <br/> |The Exchange app principal being connected to doesn't have the right permissions on the SharePoint farm. Run the Check script and ensure that the Exchange app principal has the required permissions on the farm.  <br/> |
   
## See also
<a name="touble"> </a>

#### Concepts

[Plan email integration for a SharePoint Server farm](email-integration-planning.md)
  
[Configure email integration for a SharePoint Server farm](configure-email-integration.md)
#### Other Resources

[Site mailboxes](/Exchange/collaboration/site-mailboxes?view=exchserver-2019)
  
[Collaboration](/Exchange/collaboration/collaboration?view=exchserver-2019)

