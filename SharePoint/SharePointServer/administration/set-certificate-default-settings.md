---
title: "Set certificate default settings"
ms.reviewer: 
ms.author: v-nsatapathy
author: nimishasatapathy
manager: serdars
ms.date: 06/20/2022
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-server-itpro
ms.localizationpriority: medium
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 88317397-e0cb-47c7-9093-7872bc685213
description: "Learn how SharePoint supports farm-wide default settings for certificate management by creating, renewing certificates, and certificate health rule thresholds."
---
 
# Set certificate default settings

[!INCLUDE[appliesto-xxx-xxx-xxx-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)]

SharePoint supports farm-wide default settings for certificate management. These include default properties for creating and renewing certificates and certificate health rule thresholds.

Use the [Set-SPCertificateSettings](/powershell/module/sharepoint-server/set-spcertificatesettings) PowerShell cmdlet to set the certificate management default settings.

```powershell
Set-SPCertificateSettings [-OrganizationalUnit <String>] [-Organization <String>] [-Locality <String>] [-State <String>] [-Country <String>] [-KeyAlgorithm {ECC | RSA}] [-KeySize {0 | 2048 | 4096 | 8192 | 16384}] [-EllipticCurve {Default | nistP256 | nistP384 | nistP521}] [-HashAlgorithm {Default | SHA256 | SHA384 | SHA512}] [-RsaSignaturePadding {Default | Pkcs1 | Pss}] [-CertificateExpirationAttentionThreshold <Int32>] [-CertificateExpirationWarningThreshold <Int32>] [-CertificateExpirationErrorThreshold <Int32>] [<CommonParameters>]]
```

The cmdlet parameters are:

|Parameter|Description|
|--- |--- |
|OrganizationalUnit | The name of your department within your organization or company.|
|Organization | The legally registered name of your organization or company.|
|Locality | The name of the city or locality where your organization is legally located. Don't abbreviate the name.|
|State | The name of the state or province where your organization is legally located. Don't abbreviate the name.|
|Country | The two letter country code where your organization is legally located. This must be an ISO 3166-1 alpha-2 country code.|
|KeyAlgorithm (ECC / RSA)| Specifies the key algorithm for your certificate. This choice will be used for both the public key and the private key of your certificate. <p>`RSA` is the most common and widely supported key algorithm for certificates. Select the RSA algorithm if you're unsure which type of key your certificate authority supports. `ECC` uses elliptic curve cryptography based on ECDSA keys with NIST P-256, P-384, or P-521 curves. <p>SSL/TLS connections are faster to complete with `ECC` certificates than `RSA` certificates at the equivalent security strength. Verify that your certificate authority supports `ECC` certificates before selecting it.|
|KeySize (0 / 2048 / 4096 / 8192 / 16384)| Specifies the size of your public and private RSA keys in bits. Larger key sizes provide more cryptographic strength than smaller key sizes, but they're also more computationally expensive and take more time to complete the SSL/TLS connection. <p>Select `2048` if you're unsure which key size to use. Key sizes larger than `4096` aren't recommended.|
|EllipticCurve (Default / nistP256 / nistP384 / nistP521)| Specifies the elliptic curve of your public and private ECC keys. Larger elliptic curves provide more cryptographic strength than smaller elliptic curves, but they're also more computationally expensive and take more time to complete the SSL/TLS connection.<p> Select `nistP256` if you're unsure which elliptic curve to use. Elliptic curves larger than `nistP384` aren't recommended.|
|HashAlgorithm (Default / SHA256 / SHA384 / SHA512)| Specifies the hash algorithm of your certificate signature, which your certificate authority will use to verify that your certificate request hasn't been tampered with. Larger hash algorithms provide more cryptographic strength than smaller hash algorithms, but they're also more computationally expensive. Select `SHA256` if you're unsure which hash algorithm to use. Hash algorithms larger than `SHA384` aren't recommended.|
|RsaSignaturePadding | Specifies the RSA signature padding mode for creating and renewing certificates with RSA keys. `Pkcs1` represents the RSASSA-PKCS1-v1_5 padding mode. `Pss` represents the RSASSA-PSS padding mode. The default RSA signature padding mode is `Pkcs1`.|
|CertificateExpirationAttentionThreshold | Specify the number of days before a certificate expires to trigger a certificate expiration notification. This is a reminder of upcoming certificate expirations that can be handled with normal priority. A certificate will only trigger a notification when it's assigned to SharePoint objects. This alert is disabled when set to 0.|
|CertificateExpirationWarningThreshold | Specifies the number of days before a certificate expires to trigger a certificate expiration warning. This is a warning of imminent certificate expirations that should be handled with high priority. A certificate will only trigger a warning when it is assigned to SharePoint objects. This warning is disabled when set to 0.|
|CertificateExpirationErrorThreshold | Specifies the number of days after a certificate expired to trigger a certificate expiration alert. This is an alert about certificates that have already expired and should be handled with critical priority. A certificate will only trigger an alert when it is assigned to SharePoint objects. This alert is disabled when set to 0.|
