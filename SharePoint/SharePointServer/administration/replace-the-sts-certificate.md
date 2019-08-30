---
title: "Replace the STS certificate for SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
description: "Learn how to replace the STS certificate with a new certificate from a public authority."
---

# Replace the STS certificate for SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]

This topic provides information on replacing the SharePoint Security Token Service (STS) certificate in a SharePoint farm.

## Certificate Requirements

Purchase a certificate from a trusted Certificate Authority, create a new certificate from a self-hosted PKI infrastructure (such as Active Directory Certificate Services), or create a self-signed certificate (created through `certreq.exe` or `New-SelfSignedCertificate`). The certificate must be using 2048 bit encryption or higher.

To replace the STS certificate, you will need the public certificate (CER) and public with private key certificate (PFX) and the friendly name of the certificate.

The certificate should be replaced during a maintenance window as the SharePoint Timer Service (SPTimerV4) must be restarted.

As public certificates and by default, private certificates expire within 1 to 3 years depending on the specified validity  period, this procedure should be followed when the certificate requires renewal.

> [!NOTE]
> The default STS certificate does not need to be renewed. Renewal only applies after the STS certificate has been replaced.

## Creating a Self-Signed Certificate

To create a self-signed certificate, choose the method of creation and follow these steps.

> [!TIP]
> The Common Name and DNS Name may be set to any value.

> [!NOTE]
> Certificate private keys and passwords are sensitive. Use a strong password and securely store the PFX file.

### New-SelfSignedCertificate

```PowerShell
New-SelfSignedCertificate -DnsName 'sts.contoso.com' -KeyLength 2048 -FriendlyName 'SharePoint STS Certificate' -CertStoreLocation 'cert:\LocalMachine\My' -KeySpec KeyExchange
$password = ConvertTo-SecureString "P@ssw0rd1!" -Force -AsPlainText
$cert = Get-ChildItem "cert:\localmachine\my" | ?{$_.Subject -eq "CN=sts.contoso.com"}
Export-PfxCertificate -Cert $cert -Password $password -FilePath C:\sts.pfx
Export-Certificate -Cert $cert -Type CERT -FilePath C:\sts.cer
```

This example creates a new certificate with the DNS Name of 'sts.contoso.com' and a Common Name of 'CN=sts.contoso.com'. The Common Name is automatically set by the `New-SelfSignedCertificate` cmdlet. Using a secure password, we then export the PFX (sts.pfx) and public certificate (sts.cer).

### Certreq

Create a new file, request.inf, for the certificate. Adjust the Subject as needed from the below example.

```
[Version]
Signature="$Windows NT$

[NewRequest]
FriendlyName = "SharePoint STS Certificate"
Subject = "CN=sts.contoso.com"
KeyLength = 2048
KeyAlgorithm = RSA
KeyUsage = "CERT_KEY_ENCIPHERMENT_KEY_USAGE | CERT_DIGITAL_SIGNATURE_KEY_USAGE"
KeySpec = "AT_KEYEXCHANGE"
MachineKeySet = true
RequestType = Cert
ExportableEncrypted = true

[Strings]
szOID_ENHANCED_KEY_USAGE = "2.5.29.37"
szOID_PKIX_KP_SERVER_AUTH = "1.3.6.1.5.5.7.3.1"
szOID_PKIX_KP_CLIENT_AUTH = "1.3.6.1.5.5.7.3.2"

[Extensions]
%szOID_ENHANCED_KEY_USAGE%="{text}%szOID_PKIX_KP_SERVER_AUTH%,"
_continue_ = "%szOID_PKIX_KP_CLIENT_AUTH%"
```

From an elevated Command Prompt, run the following to create and install the certificate in the local machine store. When the certificate has been installed, a save dialog will appear. Change the Save as type to `Certificate Files` and save the file as `C:\sts.cer`.

```
certreq -net request.inf
certutil -store My "sts.contoso.com"
certutil -exportPFX -p "P@ssw0rd1!" CA 1f4758121a6ede8c4b81c8ca60a2d72a C:\sts.pfx
```

The first step creates the certificate based on the above request. The second step allows us to find the Serial Number of our new certificate. Finally, the last step exports the certificate to a PFX secured by a password.

## Replacing the STS certificate

This procedure must be performed on every server in the farm. The first step is to import the PFX to the Trusted Root Certification Authorities container in the Local Machine store.

### Import-PfxCertificate

To import a PFX using `Import-PfxCertificate`, follow the example.

```PowerShell
$password = Get-Credential -UserName "certificate" -Message "Enter password"
Import-PfxCertificate -FilePath C:\sts.pfx -CertStoreLocation Cert:\LocalMachine\Root -Password $password.Password
```

In this example, we first create a credential. The username isn't used in this example, but must be set. The password will be the value of the exported PFX password; in our example, "P@ssw0rd1!".

### Certutil

```
certutil -f -p "P@ssw0rd1!" -importpfx Root C:\sts.pfx
```

In this example, we import the PFX file using `certutil`, specifying the password we used when exporting the PFX and importing into the Trusted Root Certification Authorities container in the Local Machine store.

## Replace the STS Certificate in SharePoint

Once the PFX has been imported on all SharePoint servers in the farm, we must replace the certificate that is in use by the STS. You must be a SharePoint Shell Administrator (see [Add-SPShellAdmin](/powershell/module/sharepoint-server/add-spshelladmin?view=sharepoint-ps) for details on how to add a SharePoint Shell Administrator) to perform this operation.

Using the SharePoint Management Shell, we will specify the path to the PFX file, set the password, set the STS to use the new certificate, restart IIS, and finally restart the SharePoint Timer Service (SPTimerV4).

```PowerShell
$path = 'C:\sts.pfx'
$pass = 'P@ssw0rd1!'
$cert = New-Object System.Security.Cryptography.X509Certificates.X509Certificate2($path, $pass, 20)
Set-SPSecurityTokenServiceConfig -ImportSigningCertificate $cert
iisreset
Restart-Service SPTimerV4
```

Complete the above steps on all SharePoint server in the farm. This completes the STS certificate replacement process. If you are using a hybrid farm, see [Use an Office 365 SharePoint site to authorize provider-hosted add-ins on an on-premises SharePoint site](/sharepoint/dev/sp-add-ins/use-an-office-365-sharepoint-site-to-authorize-provider-hosted-add-ins-on-an-on) for additional steps required to upload the STS certificate to Azure.

## See Also

[Hybrid for SharePoint Server](../hybrid/hybrid.md)

[Export-PfxCertificate](/powershell/module/pkiclient/export-pfxcertificate?view=win10-ps)

[Export-Certificate](/powershell/module/pkiclient/export-certificate?view=win10-ps)

[Certreq](/windows-server/administration/windows-commands/certreq_1)

[Certutil](/windows-server/administration/windows-commands/certutil)

