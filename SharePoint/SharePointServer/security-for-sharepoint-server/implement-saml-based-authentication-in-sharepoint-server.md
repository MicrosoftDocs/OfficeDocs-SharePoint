---
title: "Implement SAML based authentication in SharePoint Server"
ms.author: kirks
author: Techwriter40
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


## SharePoint Server 2013 with Active Directory Federation Services 2.0 ##

This section describes how to configure Active Directory Federation Services (AD FS) to act as an Identity Provider Security Token Service (IP-STS) for a SharePoint 2013 web application. In this configuration, AD FS issues SAML-based security tokens consisting of claims so that client computers can access web applications that use claims-based authentication.

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

Settings you need to change for your organization before the script is run ## # ADFS and root certificate names $adfsCertName = "< Input ADFS Cert Name >" $MACertName = "< Input Machine Authority >" $MIACertName = "< Input Certificate Authority >" $RootCertName = "< Input Root name >".

3.	Copy the following code, and paste it into Audiences.ps1 underneath the variable declarations from Step 2.


This script configures SharePoint 2013 with ADFS certificates and claim type maps and creates a Trusted Identity Token Issuer that enables SAML claims support in SharePoint web applications.

The directory that contains this script $ScriptDir = Split-Path -parent $MyInvocation.MyCommand.Path 

 ```
ADFS and root certificate names $adfsCertName = "< Input ADFS Cert Name >" $MACertName = "< Input Machine Authority >" $MIACertName = "< Input Certificate Authority >" $RootCertName = "< Input Root name >" # The local file path, which points to the certificate used to sign token requests (exported from the AD FS server) $certFilePath = $ScriptDir + "\Certificates\" # Build the certificates. $adfsCertPath = $certFilePath + $adfsCertName + ".cer" $MACertName = $certFilePath + $MACertName + ".cer" $MIACertPath = $certFilePath + $MIACertName + ".cer" $RootCertPath = $certFilePath + $BCTRCertName + ".cer" # Import certificates to the SharePoint Trusted Root Authority. # $adfsCert = $null if($adfsCert -eq $null) { Write-Host "installing " $adfsCert $adfsCert = New-Object System.Security.Cryptography.X509Certificates.X509Certificate2($adfsCertPath) # Install the certificate that was exported from the ADFS server. New-SPTrustedRootAuthority -Name $adfsCertName -Certificate $adfsCert New-SPTrustedRootAuthority -Name $MACertName -Certificate $MACertName New-SPTrustedRootAuthority -Name $MIACertName -Certificate $MIACertPath New-SPTrustedRootAuthority -Name $BCTRCertName -Certificate $RootCertPath } 
```
**Note**: You can use a different file name, but you must save the file as an ANSI-encoded text file that has the extension .ps1.

4.	On the Start menu, click All Programs > Microsoft SharePoint Products > SharePoint  Management Shell.
5.	Change the command prompt to the directory to which you saved the file.
6.	At the Windows PowerShell command prompt, type the following command:  ./Add-ADFSCerts.ps1.

## Create the trusted provider by using a Windows PowerShell script ##

1.	Check that you meet the following minimum requirements:
- See [Add-SPShellAdmin](https://docs.microsoft.com/en-us/powershell/module/sharepoint-server/add-spshelladmin?view=sharepoint-ps).
- Read [about_Execution_Policies](https://go.microsoft.com/fwlink/p/?LinkId=193050).

2.	Copy the following variable declarations, and paste them into a text editor, such as Notepad. Set input values specific to your organization. You will use these values in Step 3. Save the file, and name it **TrustedProviderConfiguration-Regular.ps1**.

Settings you need to change for your organization before the script is run.
```
 ADFS and root certificate names $adfsCertName = "< Input ADFS Certificate Name >" $MACertName = "< Input Machine Authority >" $MIACertName = "< Input Certificate Authority >" $RootCertName = "< Input Root name >" 
```

3.	Copy the following code, and paste it into Audiences.ps1 underneath the variable declarations from Step 2.
