---
title: "Introducing SSL Certificate management operations"
ms.reviewer: 
ms.author: v-nsatapathy
author: nimishasatapathy
manager: serdars
ms.date: 10/19/2021
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 354706a8-a7f0-4e83-b2b0-bfccd1753c2e
description: "To learn how to configure incoming and outgoing email for a SharePoint Server, see these articles."
---

[!INCLUDE[appliesto-2013-2016-2019-SUB-xxx-md](../includes/appliesto-2013-2016-2019-SUB-xxx-md.md)]

# Introducing SSL Certificate management operations

Secure Sockets Layer (SSL) certificate management is the process of monitoring and managing the life cycles from acquisition and deployment to tracking renewal, usage, and expiration of all SSL certificates deployed within a network.
 
This article focuses on the following SSL certificate management operations.

## Importing certificates

SharePoint supports both RSA and Elliptic Curve Cryptography (ECC) certificates. You can import certificates from PFX (PKCS #12) files, P7B (PKCS #7) files, and CER files. Only PFX files will contain private keys for certificates, which are necessary for a server certificate to be assigned to an IIS website. However, the entire certificate chain, from the end entity (leaf) certificate to the root certificate, must be imported to SharePoint for SSL connections to be successful.

Certificates are automatically deployed to the Windows certificate store on each server in the SharePoint farm when they are imported into SharePoint. Certificates are also automatically deployed to new servers in the SharePoint farm when those servers join the farm.

Disconnecting a server from a SharePoint farm will not automatically remove SharePoint-managed certificates from that server's Windows certificate store. Uninstalling SharePoint from a server will not automatically remove SharePoint-managed certificates from that server's Windows certificate store.

Use the Import-SPCertificate PowerShell cmdlet to import certificates from certificate files. 

The cmdlet parameters are:

Import-SPCertificate

**`[-Path] <string>`** 
The path to the PFX, P7B, or CER file containing certificates.

**`[-Password <securestring>]`** 
The password if the certificate file is protected by a password (for PFX files).

**`[-Store {EndEntity | Intermediate | Pending | Root}]`** 
The certificate store that certificates should be imported into. Unless there is a need to override SharePoint's automatic certificate detection, we recommend omitting this parameter, so that SharePoint will automatically select the appropriate certificate store for each certificate.


**`[-Exportable]`**
Specifies whether private keys of the certificates imported into SharePoint may be exported. If this parameter is not specified, the private keys of certificates deployed to the Windows Certificate Store on each server in the SharePoint farm will not be exportable, and SharePoint will not allow you to export the private keys from within the SharePoint administration interface.

**`[-Replace]`**
Currently unused. In future builds, this will allow automatically replacing previous certificates assignments with new certificates during the certificate renewal process.

Example cmdlet syntax:

```PowerShell
$password = ConvertTo-SecureString -AsPlainText -Force Import-SPCertificate -Path "\\server\fileshare\certificates.pfx" -Password $password -Exportable

```
## Assigning certificates to web applications

SharePoint supports assigning SharePoint-managed certificates to web applications with an SSL binding. The certificate must be in SharePoint's End Entity certificate store and the certificate's private key must also be imported. You can assign a certificate when the web application is first created or after it is created.

```PowerShell
A "-Certificate <SPServerCertificatePipeBind>" parameter has been added to the following cmdlets and commands:

· New-SPWebApplication

· New-SPWebApplicationExtension

· Set-SPWebApplication

· New-SPCentralAdministration

· Set-SPCentralAdministration

· PSConfig.exe -cmd adminvs

```
The SPServerCertificatePipeBind accepts the following values:

- GUID: ID property of the SPServerCertificate object.

- String: Thumbprint of the certificate.

- String: Friendly name of the certificate.

To assign a certificate to a web application when creating that web application or extending a web application to an additional zone through Central Administration, set "Use Server Sockets Layer (SSL)" to Yes, and then select the server certificate from the Server Certificate drop-down list.

## Replacing a certificate assignment

You can replace all usage of an existing certificate within SharePoint with a different certificate, for example, if an existing certificate is approaching its expiration and you've imported a new certificate. To replace, use the Switch-SPCertificate cmdlet to replace the assignments of the existing certificate with the new certificate. All usage of the existing certificate within SharePoint will then be replaced with the new certificate. 

The cmdlet parameters are:

Switch-SPCertificate

**`-Identity <SPServerCertificatePipeBind>`**
The certificate whose assignments you want to replace.

**`-NewCertificate <SPServerCertificatePipeBind>`**
The certificate that should replace all of the assignments of the certificate specified by the Identity parameter.

For example:

```PowerShell
Switch-SPCertificate -Identity "Contoso SharePoint (2020)" -NewCertificate "Contoso SharePoint (2021)"
```

## Removing certificates

The following are the known issues when you remove a certificate from SharePoint:

- By default, SharePoint will not allow you to remove a certificate if it's currently assigned to a SharePoint object. You must override the default behavior if you want to force the removal of a certificate. If you override the default behavior, existing assignments of the certificate are cleared.
- The certificate and any private key associated with that certificate is removed from the Windows certificate store on every server in the SharePoint farm.
- The certificate and any private key associated with it is removed from the SharePoint configuration database.
- Any previous exports from the certificate through the SharePoint administration interface will not be removed. Those exported files will still exist.

Use the Remove-SPCertificate cmdlet to remove a certificate from SharePoint. 

The cmdlet parameters are:

Remove-SPCertificate

**`[-Identity] <SPServerCertificatePipeBind>`**
The certificate to remove from SharePoint.


**`[-Force] `**
Specifies that the certificate should be removed from SharePoint, even if the certificate is currently assigned to SharePoint objects. If this parameter is specified, any existing assignments of the certificate are also cleared. If this parameter is not specified and the certificate is assigned to a SharePoint object, the operation will fail.

For example:

```PowerShell
Remove-SPCertificate -Identity "Contoso SharePoint (2020)"
```

## Finding/viewing certificates

SharePoint supports finding certificates via the Get-SPCertificate PowerShell cmdlet. Optional parameters are available to filter the results returned by this cmdlet.


```PowerShell
Get-SPCertificate [-Identity <SPServerCertificatePipeBind>] [-FriendlyName <string>] [-Store {EndEntity | Intermediate | Pending | Root}] [-InUse] [-DaysToExpiration <int>]

```

The cmdlet parameters are:

**`[-Identity] <SPServerCertificatePipeBind>`**
The certificate to find.

**`[-FriendlyName <string>]`**
The friendly name of the certificate to find. Use this parameter instead of the Identity parameter if multiple certificates might match this criteria. The Identity parameter can only return a single certificate.

**`[-Store {EndEntity | Intermediate | Pending | Root}]`**
Specifies the certificate store to search. If this parameter isn't specified, all certificate stores will be searched.

**`[-InUse]`**
Specifies to only return certificates that are directly assigned to SharePoint objects (that is, currently in use).

**`[-DaysToExpiration <int>]`**
If a positive number, only return certificates that will expire in the number of days from now specified by this parameter. Specify "-1" to only return certificates that have already expired. Specifying "0" will result in no filtering based on expiration date.


The following are the examples of cmdlet syntax:
 

```PowerShell
- Get-SPCertificate -FriendlyName "Contoso SharePoint (2020)"
- Get-SPCertificate -InUse -DaysToExpiration 30
```

## Exporting certificate

SharePoint supports exporting certificates to PFX (PKCS #12) files, P7B (PKCS #7) files, and CER files. Both PFX files and P7B files can contain multiple certificates, which is useful for exporting a chain of certificates from the end entity (leaf) certificate to the root certificate.  However, only PFX files can contain private keys for certificates, which are necessary for a server certificate to be assigned to an IIS website. CER files contain only a single certificate.

In the future builds, SharePoint will store exported certificate files in a SharePoint list in the Central Administration site for easy retrieval.  But for now, SharePoint only supports storing exported certificate files on the file system.

Use the Export-SPCertificate PowerShell cmdlet to import certificates from certificate files.  

This cmdlet supports multiple parameter sets:

```PowerShell
Export-SPCertificate [-Identity] <SPServerCertificatePipeBind> -Password <securestring> [-EncryptionType {AES256 | TripleDes}] [-IncludeAllCertificatesInCertificationPath] [-IncludeExtendedProperties] [-Path <string>] [-Force]
Export-SPCertificate [-Identity] <SPServerCertificatePipeBind> -Type {Cert | Pkcs7} [-IncludeAllCertificatesInCertificationPath] [-Path <string>] [-Force]

```
The cmdlet parameters are:


**`[-Identity] <SPServerCertificatePipeBind>`**
The certificate to export.
-Password <securestring>
The password to use to protect the exported PFX file. This parameter is only compatible with PFX files.

**`[-EncryptionType {AES256 | TripleDes}]`**
Specifies the encryption algorithm to use to protect the exported PFX file. AES256 specifies that AES-256 encryption with SHA256 hashing will be used. TripleDes specifies that 3DES encryption with SHA1 hashing will be used. AES-256 encryption is stronger than 3DES encryption, but is only supported with PFX files on Windows Server 2019 and newer operating systems. Use 3DES encryption if the PFX file needs to be compatible with older operating systems. If this parameter is not specified, AES-256 encryption is used by default. This parameter is only compatible with PFX files.

**`-Type {Cert | Pkcs7}`**
Specifies the type of file to generate. Cert will generate a CER file containing a single DER-encoded certificate. Pkcs7 will generate a P7B (PKCS #7) file containing one or more certificates. This parameter is only compatible with CER and P7B files.


**`[-IncludeAllCertificatesInCertificationPath]`**
Specifies whether to export additional certificates that are part of the certificate chain of the specified certificate. This will only add parent certificates of the specified certificate, not child certificates issued by the specified certificate. This parameter is only compatible with PFX and P7B files.

**`[-IncludeExtendedProperties]`**
Specifies whether extended properties of the certificate should be exported, such as the friendly name of the certificate. This parameter is only compatible with PFX files.

**`[-Path] <string>`**
The path to the PFX, P7B, or CER file containing certificates.

**`[-Force]`**
Specifies whether to overwrite a file if it already exists at the specified path.
Example cmdlet syntax:
$password = ConvertTo-SecureString -AsPlainText -Force
Export-SPCertificate -Identity "Contoso SharePoint (2020)" -Password $password -IncludeAllCertificatesInCertificationPath -IncludeExtendedProperties -Path "\\server\fileshare\certificates.pfx"


## Outgoing SMTP support for client certificate authentication

Some SMTP servers may require the use of client certificates for authentication before accepting email messages. SharePoint now supports client certificate authentication when sending emails to an SMTP server. The outbound SMTP settings in SharePoint must be configured to use TLS connection encryption and a certificate must be assigned to use this capability. The certificate must be in SharePoint's End Entity certificate store, the certificate's private key must be imported, and the certificate's enhanced key usage extension must specify the certificate is valid for client authentication if that extension is present.

```PowerShell
A "-Certificate <SPServerCertificatePipeBind>" parameter has been added to the following cmdlets parameter set:

Set-SPWebApplication [-Identity] <SPWebApplicationPipeBind> -SMTPServer <String> [-Certificate <SPServerCertificatePipeBind>] [-DisableSMTPEncryption] [-Force] [-NotProvisionGlobally] [-OutgoingEmailAddress <String>] [-ReplyToEmailAddress <String>] [-SMTPServerPort <Int32>] [-SMTPCredentials <PSCredential>]

```
To assign a certificate to the outbound SMTP settings through Central Administration, set "Use TLS connection encryption" and "Use client certificate authentication" to **Yes**, and then select the **client certificate** from the **Client certificate** drop-down list.

## Creating new certificates

SharePoint supports creating SSL certificate requests via the New-SPCertificateRequest PowerShell cmdlet. This is the first step in a three-step process to install a new SSL certificate.

Once an SSL certificate request is created via the operation, the SharePoint administrator must submit the certificate request to their SSL certificate authority. The SSL certificate authority will then generate a signed certificate based on the request and return it to the SharePoint administrator. The SharePoint administrator must then import the certificate provided by the SSL certificate authority into SharePoint. SharePoint will then pair the imported certificate with the private key generated by the certificate request operation. The certificate is then ready to be used by SharePoint.

```PowerShell
New-SPCertificateRequest -FriendlyName <string> -CommonName <string> [-AlternativeNames <string[]>] [-OrganizationalUnit <string>] [-Organization <string>] [-Locality <string>] [-State <string>] [-Country <string>] [-Exportable] [-KeyAlgorithm {ECC | RSA}] [-KeySize {2048 | 4096 | 8192 | 16384}] [-EllipticCurve {nistP256 | nistP384 | nistP521}] [-HashAlgorithm {SHA256 | SHA384 | SHA512}] [-Path <string>]

```

The cmdlet parameters are:

**`-FriendlyName <string>`**
The friendly name for the certificate. This name can be used to help you remember the purpose of this certificate. The friendly name will only be visible to administrators, not to end users.

**`-CommonName <string>`**
The primary DNS domain name or IP address that this certificate will be assigned to. Fully Qualified Domain Names (FQDNs) are recommended.

**`[-AlternativeNames <string[]>]`**
Additional DNS domain names or IP addresses that this certificate will be assigned to. Fully Qualified Domain Names (FQDNs) are recommended.

**`[-OrganizationalUnit <string>]`**
The name of your department within your organization or company. If this parameter is not specified, the default organizational unit of the farm will be used.

**`[-Organization <string>]`**
The legally registered name of your organization or company. If this parameter is not specified, the default organization of the farm will be used.

**`[-Locality <string>]`**
The name of the city or locality where your organization is legally located. Do not abbreviate the name. If this parameter is not specified, the default locality of the farm will be used.

**`[-State <string>]`**
The name of the state or province where your organization is legally located. Do not abbreviate the name. If this parameter is not specified, the default state of the farm will be used.

**`[-Country <string>]`**
The two letter country code where your organization is legally located. This must be an ISO 3166-1 alpha-2 country code. If this parameter is not specified, the default country of the farm will be used.

**`[-Exportable]`**
Specifies whether the private key of the certificate may be exported. If this parameter is not specified, the private key of certificate deployed to the Windows Certificate Store on each server in the SharePoint farm will not be exportable, and SharePoint will not allow you to export the private key from within the SharePoint administration interface.

**`[-KeyAlgorithm {ECC | RSA}]`**
Specifies the key algorithm for your certificate. This choice will be used for both the public key and the private key of your certificate.

RSA is the most common and widely supported key algorithm for certificates. Select the RSA algorithm if you are unsure, which type of key your certificate authority supports.

ECC uses elliptic curve cryptography based on ECDSA keys with NIST P-256, P-384, or P-521 curves. SSL/TLS connections are faster to complete with ECC certificates than RSA certificates at the equivalent security strength. Verify that your certificate authority supports ECC certificates before selecting it.

If this parameter is not specified, the default key algorithm of the farm will be used.

**`[-KeySize {2048 | 4096 | 8192 | 16384}]`**
Specifies the size of your public and private RSA keys in bits.

Larger key sizes provide more cryptographic strength than smaller key sizes, but they are also more computationally expensive and take more time to complete the SSL/TLS connection. Select 2048 if you are unsure, which key size to use. Key sizes larger than 4096 are not recommended.

Example cmdlet syntax:

```PowerShell
New-SPCertificateRequest -FriendlyName "Contoso SharePoint (2021)" -CommonName sharepoint.contoso.com -AlternativeNames extranet.contoso.com, onedrive.contoso.com -OrganizationalUnit "Contoso IT Department" -Organization "Contoso" -Locality "Redmond" -State "Washington" -Country "US" -Exportable -KeyAlgorithm RSA -KeySize 2048 -HashAlgorithm SHA256 -Path "\\server\fileshare\Contoso SharePoint 2021 Certificate Signing Request.txt"

```
## Renewing certificates

SharePoint supports renewing SSL certificates via the Renew-SPCertificate PowerShell cmdlet. This creates a new certificate signing request based on the properties of an existing certificate and is the first step in a three-step process to renew an SSL certificate.

Once an SSL certificate request is created via the operation, the SharePoint administrator must submit the certificate request to their SSL certificate authority. The SSL certificate authority will then generate a signed certificate based on the request and return it to the SharePoint administrator. The SharePoint administrator must then import the certificate provided by the SSL certificate authority into SharePoint.

SharePoint will then pair the imported certificate with the private key generated by the certificate request operation. The certificate is then ready to be used by SharePoint.

When you import a certificate as part of a certificate renewal operation, you can specify the -Replace switch parameter with the Import-SPCertificate cmdlet. This tells SharePoint to automatically replace the certificate assignments of the certificate being renewed with the new certificate.

> [!NOTE]
> The name of this PowerShell cmdlet is still under discussion and may change in future builds. 

```PowerShell
Renew-SPCertificate [-Identity] <SPServerCertificatePipeBind> -FriendlyName <string> [-CommonName <string>] [-AlternativeNames <string[]>] [-OrganizationalUnit <string>] [-Organization <string>] [-Locality <string>] [-State <string>] [-Country <string>] [-Exportable] [-KeyAlgorithm {ECC | RSA}] [-KeySize {2048 | 4096 | 8192 | 16384}] [-EllipticCurve {nistP256 | nistP384 | nistP521}] [-HashAlgorithm {SHA256 | SHA384 | SHA512}] [-Path <string>]

```
The cmdlet parameters are:


**`[-Identity] <SPServerCertificatePipeBind>`**
The certificate to be renewed.

**`-FriendlyName <string>`**
The friendly name for the certificate. This name can be used to help you remember the purpose of this certificate. The friendly name will only be visible to administrators, not to end users.

**`[-CommonName <string>]`**
The primary DNS domain name or IP address that this certificate will be assigned to. Fully Qualified Domain Names (FQDNs) are recommended.
If this parameter is not specified, the common name of the certificate to be renewed will be used.

**`[-AlternativeNames <string[]>]`**
Additional DNS domain names or IP addresses that this certificate will be assigned to. Fully Qualified Domain Names (FQDNs) are recommended.
If this parameter is not specified, the alternative names of the certificate to be renewed will be used.

**`[-OrganizationalUnit <string>]`**
The name of your department within your organization or company.
If this parameter is not specified, the organizational unit of the certificate to be renewed will be used. If an organizational unit cannot be found in the certificate to be renewed, the default organizational unit of the farm will be used.

**`[-OrganizationalUnit <string>]`**
The legally registered name of your organization or company.
If this parameter is not specified, the organization of the certificate to be renewed will be used. If an organization cannot be found in the certificate to be renewed, the default organization of the farm will be used.

**`[-Locality <string>]`**
The name of the city or locality where your organization is legally located. Do not abbreviate the name.
If this parameter is not specified, the locality of the certificate to be renewed will be used. If a locality cannot be found in the certificate to be renewed, the default locality of the farm will be used.

**`[-State <string>]`**
The name of the state or province where your organization is legally located. Do not abbreviate the name.
If this parameter is not specified, the state of the certificate to be renewed will be used. If a state cannot be found in the certificate to be renewed, the default state of the farm will be used.

**`[-Country <string>]`**
The two letter country code where your organization is legally located. This must be an ISO 3166-1 alpha-2 country code.
If this parameter is not specified, the country of the certificate to be renewed will be used. If a country cannot be found in the certificate to be renewed, the default country of the farm will be used.


**`[-Exportable]`**
Specifies whether the private key of the certificate may be exported. If this parameter is nto specified, the private key of certificate deployed to the Windows Certificate Store on each server in the SharePoint farm will not be exportable, and SharePoint will not allow you to export the private key from within the SharePoint administration interface.

**`[-KeyAlgorithm {ECC | RSA}]`**
Specifies the key algorithm for your certificate. This choice will be used for both the public key and the private key of your certificate.
RSA is the most common and widely supported key algorithm for certificates. Select the RSA algorithm if you are unsure, which type of key your certificate authority supports.
ECC uses elliptic curve cryptography based on ECDSA keys with NIST P-256, P-384, or P-521 curves. SSL/TLS connections are faster to complete with ECC certificates than RSA certificates at the equivalent security strength. Verify that your certificate authority supports ECC certificates before selecting it.
If this parameter is not specified, the key algorithm of the certificate to be renewed will be used.

**`[-KeySize {2048 | 4096 | 8192 | 16384}]`**
Specifies the size of your public and private RSA keys in bits.
Larger key sizes provide more cryptographic strength than smaller key sizes, but they are also more computationally expensive and take more time to complete the SSL/TLS connection. Select 2048 if you are unsure, which key size to use. Key sizes larger than 4096 are not recommended.
If this parameter is not specified, the key size of the certificate to be renewed will be used.

**`[-EllipticCurve {nistP256 | nistP384 | nistP521}]`**
Specifies the elliptic curve of your public and private ECC keys.
Larger elliptic curves provide more cryptographic strength than smaller elliptic curves, but they are also more computationally expensive and take more time to complete the SSL/TLS connection. Select nistP256 if you are unsure, which elliptic curve to use. Elliptic curves larger than nistP384 are not recommended.
If this parameter is not specified, the elliptic curve of the certificate to be renewed will be used.

**`[-HashAlgorithm {SHA256 | SHA384 | SHA512}]`**
Specifies the hash algorithm of your certificate signature, which your certificate authority will use to verify that your certificate request has not been tampered with.
Larger hash algorithms provide more cryptographic strength than smaller hash algorithms, but they are also more computationally expensive. Select SHA256 if you are unsure, which hash algorithm to use. Hash algorithms larger than SHA384 are not recommended.
If this parameter is not specified, the hash algorithm of the certificate to be renewed will be used.

**`[-Path <string>]`**
The path to the certificate signing request file that will be generated.

Example cmdlet syntax:

```PowerShell
Renew-SPCertificateRequest -Identity "Contoso SharePoint (2020)" -FriendlyName "Contoso SharePoint (2021)" -Exportable -Path "\\server\fileshare\Contoso SharePoint 2021 Certificate Signing Request.txt"
```
## Renaming certificate friendly names

SharePoint supports changing the friendly name of certificates using the Rename-SPCertificate PowerShell cmdlet.

```PowerShell
Rename-SPCertificate [-Identity] <SPServerCertificatePipeBind> -NewFriendlyName <string>

```
The cmdlet parameters are:

**`[-Identity] <SPServerCertificatePipeBind>`**
The certificate to be renamed.
-NewFriendlyName <string>
The new friendly name for the certificate.

Example cmdlet syntax:

```PowerShell
Rename-SPCertificate -Identity "Contoso SharePoint" -NewFriendlyName "Contoso SharePoint (2020)"

```
## Moving certificates between certificate stores

SharePoint supports moving certificates between certificate stores using the Move-SPCertificate PowerShell cmdlet.

```PowerShell
Move-SPCertificate [-Identity] <SPServerCertificatePipeBind> -NewStore {Default | EndEntity | Intermediate | Root} [-Force]

```
The cmdlet parameters are:


**`[-Identity] <SPServerCertificatePipeBind>`**
The certificate to move.
-NewStore {Default | EndEntity | Intermediate | Root}
The certificate store to move the certificate to. If Default is specified, SharePoint will automatically select the appropriate certificate store for the certificate.

**`[-Force]`**
Specifies that the certificate should be moved to a different certificate store, even if the certificate is currently assigned to SharePoint objects. If this parameter is specified, any existing assignments of the certificate are cleared. If this parameter is not specified and the certificate is assigned to a SharePoint object, the operation will fail.

```
Example cmdlet syntax:

```PowerShell
Move-SPCertificate -Identity "Contoso SharePoint (2020)" -NewStore EndEntity

```
## View certificate default settings

SharePoint supports farm-wide default settings for certificate management. These include default properties for creating and renewing certificates and certificate health rule thresholds.

Use the Get-SPCertificateDefaults PowerShell cmdlet to view the certificate management default settings.

> [!NOTE]
> Future builds of SharePoint will provide PowerShell cmdlets to set the certificate management default settings.

## Set certificate default settings

SharePoint supports farm-wide default settings for certificate management. These include default properties for creating and renewing certificates and certificate health rule thresholds.

Use the Set-SPCertificateDefaults PowerShell cmdlet to set the certificate management default settings.

```PowerShell
Set-SPCertificateDefaults [-OrganizationalUnit <string>] [-Organization <string>] [-Locality <string>] [-State <string>] [-Country <string>] [-KeyAlgorithm {ECC | RSA}] [-KeySize {2048 | 4096 | 8192 | 16384}] [-EllipticCurve {nistP256 | nistP384 | nistP521}] [-HashAlgorithm {SHA256 | SHA384 | SHA512}] [-CertificateExpirationAttentionThreshold <int>] [-CertificateExpirationWarningThreshold <int>] [-CertificateExpirationErrorThreshold <int>]

```
The cmdlet parameters are:


**`[-OrganizationalUnit <string>]`**
The name of your department within your organization or company.

**`[-Organization <string>]`**
The legally registered name of your organization or company.

**`[-Locality <string>]`**
The name of the city or locality where your organization is legally located. Do not abbreviate the name.

**`[-State <string>]`**
The name of the state or province where your organization is legally located. Do not abbreviate the name.

**`[-Country <string>]`**
The two letter country code where your organization is legally located. This must be an ISO 3166-1 alpha-2 country code.

**`[-KeyAlgorithm {ECC | RSA}]`**
Specifies the key algorithm for your certificate. This choice will be used for both the public key and the private key of your certificate.

RSA is the most common and widely supported key algorithm for certificates. Select the RSA algorithm if you're unsure which type of key your certificate authority supports.
ECC uses elliptic curve cryptography based on ECDSA keys with NIST P-256, P-384, or P-521 curves. SSL/TLS connections are faster to complete with ECC certificates than RSA certificates at the equivalent security strength. Verify that your certificate authority supports ECC certificates before selecting it.

**`[-KeySize {2048 | 4096 | 8192 | 16384}]`**
Specifies the size of your public and private RSA keys in bits.
Larger key sizes provide more cryptographic strength than smaller key sizes, but they are also more computationally expensive and take more time to complete the SSL/TLS connection. Select 2048 if you are unsure, which key size to use. Key sizes larger than 4096 are not recommended.

**`[-EllipticCurve {nistP256 | nistP384 | nistP521}]`**
Specifies the elliptic curve of your public and private ECC keys.
Larger elliptic curves provide more cryptographic strength than smaller elliptic curves, but they're also more computationally expensive and take more time to complete the SSL/TLS connection. Select nistP256 if you are unsure, which elliptic curve to use. Elliptic curves larger than nistP384 are not recommended.

**`[-HashAlgorithm {SHA256 | SHA384 | SHA512}]`**
Specifies the hash algorithm of your certificate signature, which your certificate authority will use to verify that your certificate request has not been tampered with.
Larger hash algorithms provide more cryptographic strength than smaller hash algorithms, but they are also more computationally expensive. Select SHA256 if you are unsure, which hash algorithm to use. Hash algorithms larger than SHA384 are not recommended.

**`[-CertificateExpirationAttentionThreshold <int>]`**
Specify the number of days before a certificate expires to trigger a certificate expiration notification. This is a reminder of upcoming certificate expirations that can be handled with normal priority. A certificate will only trigger a notification when it is assigned to SharePoint objects.

**`[-CertificateExpirationWarningThreshold <int>]`**
Specify the number of days before a certificate expires to trigger a certificate expiration warning. This is a warning of imminent certificate expirations that should be handled with high priority. A certificate will only trigger a warning when it is assigned to SharePoint objects.

**`[-CertificateExpirationErrorThreshold <int>]`**
Specify the number of days after a certificate expired to trigger a certificate expiration alert. This is an alert about certificates that have already expired and should be handled with critical priority. A certificate will only trigger an alert when it is assigned to SharePoint objects.


## Certificates administrative action logging

Major certificate management actions are now logged in the SharePoint Administrative Actions log. The logging actions include:
- Administration.Security.Certificate.Export
- Administration.Security.Certificate.Import
- Administration.Security.Certificate.Install
- Administration.Security.Certificate.Move
- Administration.Security.Certificate.New
- Administration.Security.Certificate.Register
- Administration.Security.Certificate.Remove
- Administration.Security.Certificate.Rename
- Administration.Security.Certificate.Switch
- Administration.Security.Certificate.Uninstall
- Administration.Security.Certificate.Unregister

## Bug fixes and refinements

Following bug fixes have been made  in the certificate management experience:
- Usability improvements in the create/extend web application of the Central Administration UI.
- Better support for certificates with hash algorithms other than SHA-2.
- Import-SPCertificate provides a summary of the certificates that were just imported.
- Support for relative paths in PowerShell cmdlets.
- Switching the SPServerCertificatePipeBind to use the display name instead of the friendly name. Some certificates include a friendly name, but others (such as intermediate certificates) may not. Without a friendly name, it was not as easy to specify those certificates in our PowerShell cmdlets. The display name of a certificate will default to its friendly name if it exists. If a certificate does not have a friendly name, the display name will fall back to the common name from the certificate's subject field.
- Certificate files generated by the new certificate signing request, certificate renewal, and certificate export operations are now saved to the "Certificate Files" list in Central Administration. Farm administrators can download certificate files from this list at any time. This allows administrators to generate certificate files without requiring a file share, although you'll still be able to save them to a file share.
- Certificate export operations can now export certificate chains.
- Certificate export operations will now export extended properties by default.
- The Get/Set-SPCertificateDefaults cmdlets have been renamed to Get/Set-SPCertificateDefaultSettings. Additional changes to these cmdlets may happen in future builds.
- The Get/Set-SPCertificateDefaultSettings cmdlets have been renamed to Get/Set-SPCertificateSettings.

## SSL certificate management in central administration

SharePoint now adds support for managing your SSL certificates in Central Administration. Customers will see a new **Certificates** section in the **Security** landing page of Central Administration. Within this section you will find links to **Manage certificates, Configure certificate management settings**, and **View certificate files**.

The **Manage certificates** page is the main page for managing the certificates in your SharePoint farm. From here you will have full access to all of the certificate management functionality including creating new certificates, renewing existing certificates, viewing certificates, importing and exporting certificates, and so on. You will be able to filter and sort the list of certificates based on various criteria such as certificate store and expiration date. 

> [!NOTE]
> At this time only the certificate list and deletion functionality is enabled. Additional functionality will be enabled in future builds.

The **Configure certificate management settings** page lets you configure various settings such as your default organization information and certificate health analyzer rule notification thresholds.

> [!NOTE]
> This page is not currently available but will be enabled in future builds.

The **View certificate files** page lists the Certificate Signing Request files and certificate export files generated by SharePoint. This makes it easy to retrieve these files even if you are accessing the Central Administration site remotely and do not have direct connectivity to the file shares that SharePoint would have access to.

## New health analyzer rules for SSL certificates

SharePoint has implemented the following four new health analyzer rules for SSL certificates:
1. A Certificate notification contacts has not been configured health rule that provides notification through Central Administration when certificates are in use and no certificate notification contacts have been configured. This health rule will run weekly. Certificate notification contacts receive emails about SSL certificate expirations and can be configured by customers through the Configure certificate management settings page.
2. An Upcoming SSL certificate expirations health rule that provides advanced notification through both Central Administration and email of upcoming certificate expirations. This health rule will run weekly to notify certification notification contacts about certificates that are in use and will expire within the next 15 - 60 days. These thresholds are configurable by customers through the Configure certificate management settings page.
3. An SSL certificates are about to expire health rule that provides advanced notification through both Central Administration and email when certificates are about to expire. This health rule will run daily to notify certificate notification contacts about certificates that are in use and will expire within the next 15 days. This threshold is configurable by customers through the Configure certificate management settings page.
4. An SSL certificates have expired health rule that provides notification through both Central Administration and email when certificates have expired. This health rule will run daily to notify certificate notification contacts about certificates that are in use and have expired within the past 14 days. This threshold is configurable by customers through the Configure certificate management settings page.

> [!NOTE]
> The email functionality of these health rules is not currently enabled but will be enabled in future builds.






