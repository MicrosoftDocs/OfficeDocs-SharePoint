---
title: "Import certificates"
ms.reviewer: 
ms.author: serdars
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
description: "Learn how to import certificates."
---

 
# Import certificates

[!INCLUDE[appliesto-xxx-xxx-xxx-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)]

SharePoint supports both Rivest, Shamir, Adleman (RSA) and Elliptic Curve Cryptography (ECC) certificates. You can import certificates from Personal Exchange Format (PFX) (PKCS #12) files, P7B (PKCS #7) files, and CER files. Only PFX files will contain private keys for certificates, which are necessary for a server certificate to be assigned to an Internet Information Services (IIS) website. However, the entire certificate chain, from the end entity (leaf) certificate to the root certificate must be imported to SharePoint for SSL connections to be successful.

Certificates are automatically deployed to the Windows certificate store on each server in the SharePoint farm when they're imported into SharePoint. Certificates are also automatically deployed to new servers in the SharePoint farm when those servers join the farm.

> [!NOTE]
> Disconnecting a server from a SharePoint farm will not automatically remove SharePoint-managed certificates from that server's Windows certificate store. Uninstalling SharePoint from a server will not automatically remove SharePoint-managed certificates from that server's Windows certificate store.

Use the [Import-SPCertificate](/powershell/module/sharepoint-server/import-spcertificate) PowerShell cmdlet to import certificates from certificate files.


```powershell
Import-SPCertificate [-Path] <String> [-Password <SecureString>] [-Store {EndEntity | Intermediate | Pending | Root}] [-Exportable] [-Replace] [-AssignmentCollection <SPAssignmentCollection>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

The cmdlet parameters are:

|Parameter|Description|
|--- |--- |
|Path| The path to the PFX, P7B, or CER file containing certificates.|
|Password | The password if the certificate file is protected by a password (for PFX files).|
|Store (EndEntity / Intermediate / Pending / Root)| The certificate store that certificates should be imported into. Unless there's a need to override SharePoint's automatic certificate detection, we recommend omitting this parameter, so that SharePoint will automatically select the appropriate certificate store for each certificate.|
|Exportable| Specifies whether private keys of the certificates imported into SharePoint may be exported. If this parameter isn't specified, the private keys of certificates deployed to the Windows Certificate Store on each server in the SharePoint farm won't be exportable, and SharePoint won't allow you to export the private keys from within the SharePoint administration interface.|
|Replace| Specifies that if the certificates being imported are renewing existing certificates, the certificate assignments of the existing certificates should be immediately replaced with the imported certificates.|

Example cmdlet syntax:

```powershell
$password = ConvertTo-SecureString -AsPlainText -Force 
Import-SPCertificate -Path "\\server\fileshare\certificates.pfx" -Password $password -Exportable
```