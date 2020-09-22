---
title: "Implement federated authentication in SharePoint Server"
ms.author: serdars
author: SerdarSoysal
manager: serdars
ms.date: 6/21/2019
ms.audience: ITPro
f1.keywords:
- NOCSH
ms.topic: concetpual
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 
description: "Implement federated authentication in SharePoint Server."
---

# Implement federated authentication
[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]  

## Enable remote access to SharePoint with Azure AD Application Proxy

This step-by-step guide explains how to configure federated authentication in SharePoint with Active Directory Federation Services (AD FS).

## Overview of federated authentication

In federated authentication, SharePoint processes SAML tokens from a trusted external Security Token Service (STS). A user who attempts to log on is directed to that STS, which authenticates the user and produces a SAML token. SharePoint processes this token, uses it to create its own and authorize user to access the site.

## Prerequisites

To perform the configuration, you need the following resources:
- A SharePoint 2013 farm or newer.
- An AD FS farm version 2 or newer, already created, with the public key of the ADFS signing certificate exported in a .cer file

This article uses the following values:
- SharePoint site URL: `https://spsites.contoso.local/`
- AD FS site URL: `https://adfs.contoso.local/adfs/ls/`
- Realm (relying party identifier): `urn:contoso:spsites`
- Identity claim type: `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress`
- Role claim type: `http://schemas.microsoft.com/ws/2008/06/identity/claims/role`

## Create a relying party in AD FS

In this step, you create a relying party in AD FS. The relying party will store the configuration required to work with SharePoint, and the claim rules that define what claims will be added to the SAML token upon successful authentication.

On a AD FS server, start PowerShell and run the following script:

```PowerShell
### STEP 1: Create the relying party
# Name of the Relying Party
$name = "SPSites"
# Unique identifier of the Relying Party (in SharePoint it's referred to as the realm)
$identifier = "urn:contoso:spsites"
# Authority that authenticates users
$identityProvider = "Active Directory"
# SharePoint URL where user is redirected upon successful authentication
$redirectURL = "https://spsites.contoso.local/_trust/default.aspx"
# Allow everyone to use this relying party
$allowEveryoneRule = '=> issue (Type = "http://schemas.microsoft.com/authorization/claims/permit", value = "true");'
# Create the Relying Party
Add-ADFSRelyingPartyTrust -Name $name -Identifier $identifier -ClaimsProviderName $identityProvider -Enabled $true -WSFedEndpoint $redirectURL -IssuanceAuthorizationRules $allowEveryoneRule -Confirm:$false

### STEP 2: Add claim rules to the relying party
# Rule below configured relying party to issue 2 claims in the SAML token: email and role
$LDAPClaimsRule = @"
@RuleTemplate = "LdapClaims"
@RuleName = "AD"
c:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname", Issuer == "AD AUTHORITY"]
=> issue(
store = "Active Directory", 
types = ("http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress", "http://schemas.microsoft.com/ws/2008/06/identity/claims/role"), 
query = ";mail,tokenGroups(fullDomainQualifiedName);{0}", 
param = c.Value);
"@
# Apply the rule to the Relying Party
Set-ADFSRelyingPartyTrust -TargetName $name -IssuanceTransformRules $LDAPClaimsRule
```

When the script completes, the relying party in AD FS should look like this:

    ![ADFS Relying Party](./media/SharePointTrustedAuthN_ADFSRelyingParty.png)

## Configure SharePoint to trust ADFS

In this step you create a SPTrustedLoginProvider that will store the configuration that SharePoint needs to trust AD FS.
Start the **SharePoint Management Shell** and run the following script to create it:

```PowerShell
# Define claim types
$email = New-SPClaimTypeMapping "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress" -IncomingClaimTypeDisplayName "EmailAddress" -SameAsIncoming
$role = New-SPClaimTypeMapping "http://schemas.microsoft.com/ws/2008/06/identity/claims/role" -IncomingClaimTypeDisplayName "Role" -SameAsIncoming

# Public key of the AD FS signing certificate
$signingCert = New-Object System.Security.Cryptography.X509Certificates.X509Certificate2("C:\Data\Claims\ADFS Signing.cer")
# Unique realm (corresponds to the unique identifier of the AD FS Relying Party)
$realm = "urn:contoso:spsites"
# Set the AD FS URL where users are redirected to authenticate
$signinurl = "https://adfs.contoso.local/adfs/ls/"

# Create a new SPTrustedIdentityTokenIssuer in SharePoint
New-SPTrustedIdentityTokenIssuer -Name "Contoso.local" -Description "Contoso.local" -Realm $realm -ImportTrustCertificate $signingCert -ClaimsMappings $email,$role -SignInUrl $signinurl -IdentifierClaim $email.InputClaimType
```

Then, the relevant certificate must be added to the SharePoint root authority certificate store. There are 2 possible options:

- If the ADFS signing certificate is issued by a certificate authority (best practice for security reasons)

The public key of the issuer's certificate (and all the intermediates) must be added to the store:
Start the **SharePoint Management Shell** and run the following script to add it:

```PowerShell
$rootCert = New-Object System.Security.Cryptography.X509Certificates.X509Certificate2("C:\Data\Claims\ADFS Signing issuer.cer")
New-SPTrustedRootAuthority -Name "adfs.contoso.local signing root authority" -Certificate $rootCert
```

- If the ADFS signing certificate is a self-signed certificate (not recommended for security reasons)

The public key of the ADFS signing certificate itself must be added to the store:
Start the **SharePoint Management Shell** and run the following script to add it:

```PowerShell
$rootCert = New-Object System.Security.Cryptography.X509Certificates.X509Certificate2("C:\Data\Claims\ADFS Signing.cer")
New-SPTrustedRootAuthority -Name "adfs.contoso.local signing certificate" -Certificate $rootCert
```

### Configure the SharePoint web application

In this step you will configure a web application in SharePoint to federate the authentication with the AD FS, using the SPTrustedLoginProvider that was created above.

There are some rules to re

- Default zone of the SharePoint web application must have Windows authentication enabled. This is requires
- SharePoint URL that will use AD FS federation must be be HTTPS

- If you create a new web application and use both Windows and AD FS authentication in the Default zone:

    1. Start the **SharePoint Management Shell** and run the following script:

        ```powershell
        # This script creates a new web application and sets Windows and AD FS authentication on the Default zone
        # URL of the SharePoint site federated with ADFS
        $trustedSharePointSiteUrl = "https://spsites.contoso.local/"
        $applicationPoolManagedAccount = "Contoso\spapppool"

        $winAp = New-SPAuthenticationProvider -UseWindowsIntegratedAuthentication -DisableKerberos:$true
        $sptrust = Get-SPTrustedIdentityTokenIssuer "Contoso.local"
        $trustedAp = New-SPAuthenticationProvider -TrustedIdentityTokenIssuer $sptrust

        New-SPWebApplication -Name "SharePoint - ADFS on contoso.local" -Port 443 -SecureSocketsLayer -URL $trustedSharePointSiteUrl -ApplicationPool "SharePoint - ADFS on contoso.local" -ApplicationPoolAccount (Get-SPManagedAccount $applicationPoolManagedAccount) -AuthenticationProvider $winAp, $trustedAp
        ```

    2. Open the **SharePoint Central Administration** site.
    1. Under **System Settings**, select **Configure Alternate Access Mappings**. The **Alternate Access Mapping Collection** box opens.
    1. Filter the display with the new web application and confirm that you see something like this:

       ![Alternate Access Mappings of web application](./media/application-proxy-integrate-with-sharepoint-server/new-webapp-aam.png)

- If you extend an existing web application to set AD FS authentication on a new zone:

    1. Start the SharePoint Management Shell and run the following script:

        ```powershell
        # This script extends an existing web application to set AD FS authentication on a new zone
        # URL of the default zone of the web application
        $webAppDefaultZoneUrl = "http://spsites/"
        # URL of the SharePoint site federated with ADFS
        $trustedSharePointSiteUrl = "https://spsites.contoso.local/"

        $sptrust = Get-SPTrustedIdentityTokenIssuer "Contoso.local"
        $ap = New-SPAuthenticationProvider -TrustedIdentityTokenIssuer $sptrust
        $wa = Get-SPWebApplication $webAppDefaultZoneUrl
        New-SPWebApplicationExtension -Name "SharePoint - ADFS on contoso.local" -Identity $wa -SecureSocketsLayer -Zone Intranet -Url $trustedSharePointSiteUrl -AuthenticationProvider $ap
        ```

    2. Open the **SharePoint Central Administration** site.
    1. Under **System Settings**, select **Configure Alternate Access Mappings**. The **Alternate Access Mapping Collection** box opens.
    1. Filter the display with the web application that was extended and confirm that you see something like this:

        ![Alternate Access Mappings of extended application](./media/SharePointTrustedAuthN_AAMExtendedWebapp.png)

### Make sure that an HTTPS certificate is configured for the SharePoint site federated with AD FS

Because the SharePoint URL uses HTTPS protocol (`https://spsites.contoso.local/`), a certificate must be set on the Internet Information Services (IIS) site.

1. Open the Windows PowerShell console.
1. Run the following script to generate a self-signed certificate and add it to the computer's MY store:

   ```powershell
   New-SelfSignedCertificate -DnsName "spsites.contoso.local" -CertStoreLocation "cert:\LocalMachine\My"
   ```

   > [!IMPORTANT]
   > Self-signed certificates are suitable only for test purposes. In production environments, we strongly recommend that you use certificates issued by a certificate authority instead.

1. Open the Internet Information Services Manager console.
1. Expand the server in the tree view, expand **Sites**, select the **SharePoint - ADFS on contoso.local** site, and select **Bindings**.
1. Select **https binding** and then select **Edit**.
1. In the TLS/SSL certificate field, choose **spsites.contoso.local** certificate and then select **OK**.










## Concepts and terminology ##
To understand the concepts and terminology that are used in SAML-based authentication, see [Authentication Overview](https://docs.microsoft.com/sharepoint/security-for-sharepoint-server/authentication-overview).







## SharePoint Server with Active Directory Federation Services ##

This section describes how to configure Active Directory Federation Services (AD FS) to act as an Identity Provider Security Token Service (IP-STS) for a SharePoint web application. In this configuration, AD FS issues SAML 1.1 security tokens that will be processed by SharePoint.

## Configure a SharePoint web application for SAML authentication ##

This section discusses how to set up a new or existing Windows authentication web application to support SAML.
Each authentication type has realms associated with it. For example: urn: "customercode":sp "webapptype" :"authusers"
   
For example, the value for the Contoso team web application for employee user could be similar to the following: urn:contoso:spteam:emp.

### Configure a new or existing Windows authentication web application to support SAML ###

There are four steps that are needed to configure a new or existing web application to support SAML claims:

1.	Create a realm for employee access.
2.	Add trusted certificates.
3.	Create the trusted providers.
4.	Associate them to a web application.

**Create a realm for employee access**

The following claim rules for the new realm are created:

 - Email
 - UPN
 - PrimarySID
 - GroupsSID
 	
If the AD FS STS domain is configured by using additional claims, it will be ignored.

**Add trusted certificates by using a Windows PowerShell script**

1.	Check that you meet the following minimum requirements:
- See [Add-SPShellAdmin](https://docs.microsoft.com/powershell/module/sharepoint-server/add-spshelladmin?view=sharepoint-ps).
- Read [about_Execution_Policies](https://go.microsoft.com/fwlink/p/?LinkId=193050).
2.	Copy the following variable declarations, and paste them into a text editor, like Notepad. Set input values specific to your organization. You will use these values in Step 3. Save the file, and name it **Add-ADFSCerts.ps1**.

Settings you need to change for your organization before the script is run. 

- ADFS and root certificate names $adfsCertName = "< Input ADFS Cert Name >" 
- $MACertName = "< Input Machine Authority >"
- $MIACertName = "< Input Certificate Authority >"
- $RootCertName = "< Input Root name >".

3.	Copy the following code, and paste it into Audiences.ps1 underneath the variable declarations from Step 2.


This script configures SharePoint 2013 with ADFS certificates and claim type maps and creates a Trusted Identity Token Issuer that enables SAML claims support in SharePoint web applications.

The directory that contains this script $ScriptDir = Split-Path -parent $MyInvocation.MyCommand.Path 

```PowerShell
# ADFS and root certificate names 
$adfsCertName = "<Input ADFS Cert Name>"
$MACertName = "<Input Machine Authority>" 
$MIACertName = "<Input Certificate Authority>"
$RootCertName = "<Input Root name>"

# The local file path, which points to the certificate used to sign token requests (exported from the AD FS server) $certFilePath = $ScriptDir + "\Certificates\" # Build the certificates. $adfsCertPath = $certFilePath + $adfsCertName + ".cer" $MACertName = $certFilePath + $MACertName + ".cer" $MIACertPath = $certFilePath + $MIACertName + ".cer" $RootCertPath = $certFilePath + $BCTRCertName + ".cer" 
# Import certificates to the SharePoint Trusted Root Authority. # $adfsCert = $null if($adfsCert -eq $null) { Write-Host "installing " $adfsCert $adfsCert = New-Object System.Security.Cryptography.X509Certificates.X509Certificate2($adfsCertPath) 
# Install the certificate that was exported from the ADFS server. New-SPTrustedRootAuthority -Name $adfsCertName -Certificate $adfsCert New-SPTrustedRootAuthority -Name $MACertName -Certificate $MACertName New-SPTrustedRootAuthority -Name $MIACertName -Certificate $MIACertPath New-SPTrustedRootAuthority -Name $BCTRCertName -Certificate $RootCertPath } 
```

 > [!NOTE]
 > You can use a different file name, but you must save the file as an ANSI-encoded text file that has the extension .ps1.

4.	On the **Start** menu, click **All Programs** > **Microsoft SharePoint Products** > **SharePoint  Management Shell**.
5.	Change the command prompt to the directory to which you saved the file.
6.	At the Windows PowerShell command prompt, type the following command:  ./Add-ADFSCerts.ps1.

## Create the trusted provider by using a Windows PowerShell script ##

1.	Check that you meet the following minimum requirements:
- See [Add-SPShellAdmin](https://docs.microsoft.com/powershell/module/sharepoint-server/add-spshelladmin?view=sharepoint-ps).
- Read [about_Execution_Policies](https://go.microsoft.com/fwlink/p/?LinkId=193050).

2.	Copy the following variable declarations, and paste them into a text editor, such as Notepad. Set input values specific to your organization. You will use these values in Step 3. Save the file, and name it **TrustedProviderConfiguration-Regular.ps1**.

Settings you need to change for your organization before the script is run.
```PowerShell
 #ADFS and root certificate names
 $adfsCertName = "<Input ADFS Certificate Name>"
 $MACertName = "<Input Machine Authority>"
 $MIACertName = "<Input Certificate Authority>"
 $RootCertName = "<Input Root name>"
```

3.	Copy the following code, and paste it into Audiences.ps1 underneath the variable declarations from Step 2.

This script configures SharePoint Server with ADFS certificates and claim type maps and creates a Trusted Identity Token Issuer that enables SAML claims support in SharePoint web applications.

## Variables that need to be change before you run script:

  The directory that contains this script 



$ScriptDir = Split-Path -parent $MyInvocation.MyCommand.Path 

**ADFS and root certificate names**

 - $adfsCertName = "< Input ADFS Cert Name>"
 - $MACertName = "< Input Machine Authority>"
 - $MIACertName = "< Input Certificate Authority>"
 - $RootCertName = "< Input Root name>" 

**The local file path, which points to the certificate used to sign token requests (exported from the AD FS server)**

$certFilePath = $ScriptDir + "\Certificates\" # Build the certificates. $adfsCertPath = $certFilePath + $adfsCertName + ".cer" $MACertName = $certFilePath + $MACertName + ".cer" $MIACertPath = $certFilePath + $MIACertName + ".cer" $RootCertPath = $certFilePath + $BCTRCertName + ".cer" 

```PowerShell
 # Import certificates to the SharePoint Trusted Root Authority**

 $adfsCert = $null 
 if($adfsCert -eq $null){ 
    Write-Host "installing " + $adfsCert 
    $adfsCert = New-Object System.Security.Cryptography.X509Certificates.X509Certificate2($adfsCertPath)

    #Install the certificate that was exported from the ADFS server. 

    New-SPTrustedRootAuthority -Name $adfsCertName -Certificate $adfsCert 
    New-SPTrustedRootAuthority -Name $MACertName -Certificate $MACertName 
    New-SPTrustedRootAuthority -Name $MIACertName -Certificate $MIACertPath 
    New-SPTrustedRootAuthority -Name $BCTRCertName -Certificate $RootCertPath 
 } 
```

 > [!NOTE]
 > You can use a different file name, but you must save the file as an ANSI-encoded text file that has the extension .ps1.

4.	On the **Start** menu, click **All Programs** > **Microsoft SharePoint Products** > **SharePoint Management Shell**.
5.	Change the command prompt to the directory to which you saved the file.
6.	At the Windows PowerShell command prompt, type the following command, .Add-ADFSCerts.ps1.

### Create the trusted provider by using a Windows PowerShell script ###

1.	Check that you meet the following minimum requirements:
- See [Add-SPShellAdmin](https://docs.microsoft.com/powershell/module/sharepoint-server/add-spshelladmin?view=sharepoint-ps).
- Read [about_Execution_Policies](https://go.microsoft.com/fwlink/p/?LinkId=193050).

2.	Copy the following variable declarations, and paste them into a text editor, such as Notepad. Set input values specific to your organization. You will use these values in Step 3. Save the file, and name it **TrustedProviderConfiguration-Regular.ps1**.

 Settings you need to change for your organization before the script is run. 

**ADFS and root certificate names**

- $adfsCertName = "< Input ADFS Certificate Name>" 
- $MACertName = "< Input Machine Authority>"
- $MIACertName = "< Input Certificate Authority>" 
- $RootCertName = "< Input Root name>" 


This script configures SharePoint 2013 with ADFS certificates and claim type maps and creates a Trusted Identity Token Issuer that enables SAML claims support in SharePoint web applications. These providers use the UPN or EMail claim rule for the identity claim. 

```PowerShell
**The production ADFS redirect URL** 
$signInUrl = https://sts.msft.net/adfs/ls/" 

**The URL and realm for the partner web application** 
$webAppUri = "https://ppedrtest.mmsxl.com/" 
$siteRealm = "urn:039d:spdr:emp" 

**The directory that contains this script**
$ScriptDir = Split-Path -parent $MyInvocation.MyCommand.Path

**The claim type schema used as the user identity, which uses the email address as the UPN**
 
$IdClaimType = http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress" 
$adfsCert = New-Object System.Security.Cryptography.X509Certificates.X509Certificate2($adfsCertPath) 

**The ADFS and root certificate names**
$adfsCertName = "<Insert ADFS Certification Name>"

**The local file path, which points to the certificate used to sign token requests (exported from the AD FS server)**
$certFilePath = $ScriptDir + "\\Certificates\\" 

# Build the certificates. 
$adfsCertPath = $certFilePath + $adfsCertName + ".cer" 
$adfsCert = New-Object System.Security.Cryptography.X509Certificates.X509Certificate2($adfsCertPath) 

**Create or rebuild TrustedIdentityTokenIssuer**
$tokenIdentityProviderName = "RegularUsers" 
$TrustedIdentityTokenIssuerDescription = "SAML Provider for SharePoint" 

foreach($issuer in Get-SPTrustedIdentityTokenIssuer){ 
    if($issuer.Name -eq $tokenIdentityProviderName){
        **Remove TrustedIdentityTokenIssuer (usually, to modify the ADFS property maps) if it already exists?**
        Read-Host "Identity Token Issuer already exists. Remove and reinstall it? Press CTRL+C to cancel." 
        Remove-SPTrustedIdentityTokenIssuer -Identity $tokenIdentityProviderName 
    } 
} 

Read-Host "Create a new SharePoint Trusted Identity Token Issuer?"
**Create the SharePoint Trusted Identity Token Issuer**
 
Write-Host "Creating SPTrustedIdentityTokenIssuer named: ""$tokenIdentityProviderName"" "
$ap = New-SPTrustedIdentityTokenIssuer -Name $tokenIdentityProviderName -Description $TrustedIdentityTokenIssuerDescription `
      -realm $siteRealm -ImportTrustCertificate $adfsCert -SignInUrl $signInUrl  -UseDefaultConfiguration `
      -IdentifierClaimIs "USER-PRINCIPAL-NAME" -RegisteredIssuerName $siteRealm 

**Add the partner site realm to the trusted provider**
$uri = new-object System.Uri($webAppUri) 
$ap = Get-SPTrustedIdentityTokenIssuer $tokenIdentityProviderName $ap.ProviderRealms.Add($uri,$siteRealm) 
$ap.Update() 
```

 > [!NOTE]
 > You can use a different file name, but you must save the file as an ANSI-encoded text file that has the extension .ps1.

4.	On the **Start** menu, click **All Programs** > **Microsoft SharePoint Products** > **SharePoint Management Shell**.
5.	Change the command prompt to the directory to which you saved the file.
6.	At the Windows PowerShell command prompt, type the following command, ./TrustedProviderConfiguration-Regular.ps1.

## Enable tracing for SharePoint Server claims ##

To enable tracing for SharePoint 2013, you can use the following ways:
 - Enable tracing in Windows Identity Foundation (WIF). For information about how to enable tracing, see [WIF Tracing](https://docs.microsoft.com/dotnet/framework/security/how-to-enable-wif-tracing).
 - Configure diagnostic logging in SharePoint Server. 

For information about how to configure diagnostic logging, see [Configure diagnostic logging in SharePoint Server](https://docs.microsoft.com/sharepoint/administration/configure-diagnostic-logging).

## Trusted identity providers and user profile synchronization ##

This section describes the steps that let user profile synchronization use claims-based authentication with a trusted identity provider.

When you configure a directory synchronization connection, you can specify the type of authentication provider that will be used to access the imported profiles. In the case of a trusted claims provider, you can also select the specific trusted provider configured in the farm.

To provide the user profile application with sufficient information to map the imported profiles to authenticated users, you have to set the imported attributed to the corresponding authenticated users identity claim. The claim is immutable. It cannot be changed after it is configured in the trusted identity provider. To map users correctly, the user profile system must be informed of which of the attributes it can import to be used as the identity claim. The key is to identify the identity claim for the user profile system so that there is enough information to match the identity claim with the corresponding profile entry. The Claim User Identifier property is used to establish the mapping.

The next profile import will result in users who are associated with the corresponding profile entries.
For additional information about user profile synchronization, see [User Profile Synchronization in SharePoint Server 2013](https://docs.microsoft.com/sharepoint/administration/overview-of-profile-synchronization-in-sharepoint-server-2013) and [User Profile Synchronization in SharePoint Server 2016](https://docs.microsoft.com/sharepoint/administration/profile-synchronization-in-sharepoint-server-2013).

## Using audiences with claims-based sites ##

This section describes how SAML claims work with the audiences feature in SharePoint Server. By default, synchronization support is available for AD DS and several Lightweight Directory Access Protocol (LDAP) sources and from a Lightweight Directory Interchange Format (LDIF) file.  A problem is that the account name for most SAML claims users is something like i:05:t|AD FS with roles|fred@contoso.com.

To take advantage of audiences, you need to create profiles for users either manually or through custom code. Create the profiles with their proper claims attributes—for example, i:05:t|AD FS with roles|fred@contoso.com as the account name—and then populate the other fields with data that you want to use in your audiences.

After the profiles are created, audiences can be created. You can't use a user-based audience, such as membership in a group, for the audience unless you implement custom code. It might be more efficient to use the property-based audience.

For more information see, [Claims-Based Identity Term Definitions](https://docs.microsoft.com/previous-versions/office/developer/sharepoint-2010/ee534975(v=office.14)).
