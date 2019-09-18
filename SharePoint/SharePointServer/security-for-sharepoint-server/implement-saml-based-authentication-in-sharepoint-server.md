---
title: "Implement SAML based authentication in SharePoint Server"
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 6/21/2019
ms.audience: ITPro
ms.topic: concetpual
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 
description: "Implement a Security Assertion Markup Language (SAML) security token for a Microsoft SharePoint claims-based web application."
---

# Implement SAML authentication
[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]  


## Overview of SAML authentication ##

In SAML claims mode, SharePoint Server accepts SAML tokens from a trusted external Security Token Provider (STS), often known as a claims provider trust. A user who attempts to log on is directed to an external claims provider (for example, the Windows Live ID claims provider), which authenticates the user and produces a SAML token. SharePoint Server accepts and processes this token, augmenting the claim and creating a claims identity object for the user.

## Concepts and terminology ##
To understand the concepts and terminology that are used in SAML-based authentication, see [Authentication Overview](https://docs.microsoft.com/en-us/sharepoint/security-for-sharepoint-server/authentication-overview).


## SharePoint Server with Active Directory Federation Services 2.0 ##

This section describes how to configure Active Directory Federation Services (AD FS) to act as an Identity Provider Security Token Service (IP-STS) for a SharePoint Server web application. In this configuration, AD FS issues SAML-based security tokens consisting of claims so that client computers can access web applications that use claims-based authentication.

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
- See [Add-SPShellAdmin](https://docs.microsoft.com/en-us/powershell/module/sharepoint-server/add-spshelladmin?view=sharepoint-ps).
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

```
# ADFS and root certificate names 

$adfsCertName = "< Input ADFS Cert Name >"
 $MACertName = "< Input Machine Authority >" $MIACertName = "< Input Certificate Authority >" $RootCertName = "< Input Root name >" 

# The local file path, which points to the certificate used to sign token requests (exported from the AD FS server) $certFilePath = $ScriptDir + "\Certificates\" # Build the certificates. $adfsCertPath = $certFilePath + $adfsCertName + ".cer" $MACertName = $certFilePath + $MACertName + ".cer" $MIACertPath = $certFilePath + $MIACertName + ".cer" $RootCertPath = $certFilePath + $BCTRCertName + ".cer" 

# Import certificates to the SharePoint Trusted Root Authority. # $adfsCert = $null if($adfsCert -eq $null) { Write-Host "installing " $adfsCert $adfsCert = New-Object System.Security.Cryptography.X509Certificates.X509Certificate2($adfsCertPath) 

# Install the certificate that was exported from the ADFS server. New-SPTrustedRootAuthority -Name $adfsCertName -Certificate $adfsCert New-SPTrustedRootAuthority -Name $MACertName -Certificate $MACertName New-SPTrustedRootAuthority -Name $MIACertName -Certificate $MIACertPath New-SPTrustedRootAuthority -Name $BCTRCertName -Certificate $RootCertPath } 
```
**Note**: You can use a different file name, but you must save the file as an ANSI-encoded text file that has the extension .ps1.

4.	On the **Start** menu, click **All Programs** > **Microsoft SharePoint Products** > **SharePoint  Management Shell**.
5.	Change the command prompt to the directory to which you saved the file.
6.	At the Windows PowerShell command prompt, type the following command:  ./Add-ADFSCerts.ps1.

## Create the trusted provider by using a Windows PowerShell script ##

1.	Check that you meet the following minimum requirements:
- See [Add-SPShellAdmin](https://docs.microsoft.com/en-us/powershell/module/sharepoint-server/add-spshelladmin?view=sharepoint-ps).
- Read [about_Execution_Policies](https://go.microsoft.com/fwlink/p/?LinkId=193050).

2.	Copy the following variable declarations, and paste them into a text editor, such as Notepad. Set input values specific to your organization. You will use these values in Step 3. Save the file, and name it **TrustedProviderConfiguration-Regular.ps1**.

Settings you need to change for your organization before the script is run.
```
 # ADFS and root certificate names
$adfsCertName = "< Input ADFS Certificate Name >" $MACertName = "< Input Machine Authority >" $MIACertName = "< Input Certificate Authority >" $RootCertName = "< Input Root name >" 
```

3.	Copy the following code, and paste it into Audiences.ps1 underneath the variable declarations from Step 2.

This script configures SharePoint Server with ADFS certificates and claim type maps and creates a Trusted Identity Token Issuer that enables SAML claims support in SharePoint web applications.

## Variables that need to be change before you run script:

  The directory that contains this script 



$ScriptDir = Split-Path -parent $MyInvocation.MyCommand.Path 

**ADFS and root certificate names**

 - $adfsCertName = "< Input ADFS Cert Name >"
 - $MACertName = "< Input Machine Authority >"
 - $MIACertName = "< Input Certificate Authority >"
 - $RootCertName = "< Input Root name >" 

**The local file path, which points to the certificate used to sign token requests (exported from the AD FS server)**

$certFilePath = $ScriptDir + "\Certificates\" # Build the certificates. $adfsCertPath = $certFilePath + $adfsCertName + ".cer" $MACertName = $certFilePath + $MACertName + ".cer" $MIACertPath = $certFilePath + $MIACertName + ".cer" $RootCertPath = $certFilePath + $BCTRCertName + ".cer" 



```
# Import certificates to the SharePoint Trusted Root Authority**

$adfsCert = $null if($adfsCert -eq $null) { Write-Host "installing " $adfsCert $adfsCert = New-Object System.Security.Cryptography.X509Certificates.X509Certificate2($adfsCertPath)

 # Install the certificate that was exported from the ADFS server. 

New-SPTrustedRootAuthority -Name $adfsCertName -Certificate $adfsCert New-SPTrustedRootAuthority -Name $MACertName -Certificate $MACertName New-SPTrustedRootAuthority -Name $MIACertName -Certificate $MIACertPath New-SPTrustedRootAuthority -Name $BCTRCertName -Certificate $RootCertPath } 
```

**Note**: You can use a different file name, but you must save the file as an ANSI-encoded text file that has the extension .ps1.

4.	On the **Start** menu, click **All Programs** > **Microsoft SharePoint Products** > **SharePoint Management Shell**.
5.	Change the command prompt to the directory to which you saved the file.
6.	At the Windows PowerShell command prompt, type the following command, .Add-ADFSCerts.ps1.

### Create the trusted provider by using a Windows PowerShell script ###

1.	Check that you meet the following minimum requirements:
- See [Add-SPShellAdmin](https://docs.microsoft.com/en-us/powershell/module/sharepoint-server/add-spshelladmin?view=sharepoint-ps).
- Read [about_Execution_Policies](https://go.microsoft.com/fwlink/p/?LinkId=193050).

2.	Copy the following variable declarations, and paste them into a text editor, such as Notepad. Set input values specific to your organization. You will use these values in Step 3. Save the file, and name it **TrustedProviderConfiguration-Regular.ps1**.

 Settings you need to change for your organization before the script is run. 

**ADFS and root certificate names**

- $adfsCertName = "< Input ADFS Certificate Name >" 
- $MACertName = "< Input Machine Authority >"
- $MIACertName = "< Input Certificate Authority >" 
- $RootCertName = "< Input Root name >" 


This script configures SharePoint 2013 with ADFS certificates and claim type maps and creates a Trusted Identity Token Issuer that enables SAML claims support in SharePoint web applications. These providers use the UPN or EMail claim rule for the identity claim. 

```
**The production ADFS redirect URL** 

$signInUrl = https://sts.msft.net/adfs/ls/" 

**The URL and realm for the partner web application** 

$webAppUri = "https://ppedrtest.mmsxl.com/" $siteRealm = "urn:039d:spdr:emp" 

**The directory that contains this script**
$ScriptDir = Split-Path -parent $MyInvocation.MyCommand.Path

**The claim type schema used as the user identity, which uses the email address as the UPN**
 
$IdClaimType = http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress" 
$adfsCert = New-Object System.Security.Cryptography.X509Certificates.X509Certificate2($adfsCertPath) 

**The ADFS and root certificate names**

$adfsCertName = "<Insert ADFS Certification Name>

**The local file path, which points to the certificate used to sign token requests (exported from the AD FS server)**

$certFilePath = $ScriptDir + "\Certificates\" # Build the certificates. $adfsCertPath = $certFilePath + $adfsCertName + ".cer" $adfsCert = New-Object System.Security.Cryptography.X509Certificates.X509Certificate2($adfsCertPath) 

**Create or rebuild TrustedIdentityTokenIssuer**

$tokenIdentityProviderName = "RegularUsers" $TrustedIdentityTokenIssuerDescription = "SAML Provider for SharePoint" foreach($issuer in Get-SPTrustedIdentityTokenIssuer) { if($issuer.Name -eq $tokenIdentityProviderName) {

 **Remove TrustedIdentityTokenIssuer (usually, to modify the ADFS property maps) if it already exists?**
 
Read-Host "Identity Token Issuer already exists. Remove and reinstall it? Press CTRL+C to cancel." 
Remove-SPTrustedIdentityTokenIssuer -Identity $tokenIdentityProviderName } } 

Read-Host "Create a new SharePoint Trusted Identity Token Issuer?"

**Create the SharePoint Trusted Identity Token Issuer**
 
Write-Host "Creating SPTrustedIdentityTokenIssuer named " $tokenIdentityProviderName 
$ap = New-SPTrustedIdentityTokenIssuer `-Name $tokenIdentityProviderName `-Description $TrustedIdentityTokenIssuerDescription `-realm $siteRealm `-ImportTrustCertificate $adfsCert `-SignInUrl $signInUrl ` -UseDefaultConfiguration `-IdentifierClaimIs USER-PRINCIPAL-NAME `-RegisteredIssuerName $siteRealm 

**Add the partner site realm to the trusted provider**
 
$uri = new-object System.Uri($webAppUri) 
$ap = Get-SPTrustedIdentityTokenIssuer $tokenIdentityProviderName $ap.ProviderRealms.Add($uri,$siteRealm) $ap.Update() 
```

**Note**:  You can use a different file name, but you must save the file as an ANSI-encoded text file that has the extension .ps1.

4.	On the **Start** menu, click **All Programs** > **Microsoft SharePoint Products** > **SharePoint Management Shell**.
5.	Change the command prompt to the directory to which you saved the file.
6.	At the Windows PowerShell command prompt, type the following command, ./TrustedProviderConfiguration-Regular.ps1.

## Enable tracing for SharePoint Server claims ##

To enable tracing for SharePoint 2013, you can use the following ways:
 - Enable tracing in Windows Identity Foundation (WIF). For information about how to enable tracing, see [WIF Tracing](https://docs.microsoft.com/en-us/dotnet/framework/security/how-to-enable-wif-tracing).
 - Configure diagnostic logging in SharePoint Server. 

For information about how to configure diagnostic logging, see [Configure diagnostic logging in SharePoint Server](https://docs.microsoft.com/en-us/sharepoint/administration/configure-diagnostic-logging).


## Trusted identity providers and user profile synchronization ##

This section describes the steps that let user profile synchronization use claims-based authentication with a trusted identity provider.

When you configure a directory synchronization connection, you can specify the type of authentication provider that will be used to access the imported profiles. In the case of a trusted claims provider, you can also select the specific trusted provider configured in the farm.

To provide the user profile application with sufficient information to map the imported profiles to authenticated users, you have to set the imported attributed to the corresponding authenticated users identity claim. The claim is immutable. It cannot be changed after it is configured in the trusted identity provider. To map users correctly, the user profile system must be informed of which of the attributes it can import to be used as the identity claim. The key is to identify the identity claim for the user profile system so that there is enough information to match the identity claim with the corresponding profile entry. The Claim User Identifier property is used to establish the mapping.

The next profile import will result in users who are associated with the corresponding profile entries.
For additional information about user profile synchronization, see [User Profile Synchronization in SharePoint Server 2013](https://docs.microsoft.com/en-us/sharepoint/administration/overview-of-profile-synchronization-in-sharepoint-server-2013) and [User Profile Synchronization in SharePoint Server 2016](https://docs.microsoft.com/en-us/sharepoint/administration/profile-synchronization-in-sharepoint-server-2013).


## Using audiences with claims-based sites ##

This section describes how SAML claims work with the audiences feature in SharePoint Server. By default, synchronization support is available for AD DS and several Lightweight Directory Access Protocol (LDAP) sources and from a Lightweight Directory Interchange Format (LDIF) file.  A problem is that the account name for most SAML claims users is something like i:05:t|AD FS with roles|fred@contoso.com.

To take advantage of audiences, you need to create profiles for users either manually or through custom code. Create the profiles with their proper claims attributes—for example, i:05:t|AD FS with roles|fred@contoso.com as the account name—and then populate the other fields with data that you want to use in your audiences.

After the profiles are created, audiences can be created. You can't use a user-based audience, such as membership in a group, for the audience unless you implement custom code. It might be more efficient to use the property-based audience.

For more information see, [Claims-Based Identity Term Definitions](https://docs.microsoft.com/en-us/previous-versions/office/developer/sharepoint-2010/ee534975(v=office.14)).






 



