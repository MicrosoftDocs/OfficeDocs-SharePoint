---
title: "Remove certificates"
ms.reviewer: 
ms.author: v-nsatapathy
author: nimishasatapathy
manager: serdars
ms.date: 06/20/2022
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
ms.localizationpriority: medium
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 88317397-e0cb-47c7-9093-7872bc685213
description: "Learn how you can use Secure Sockets Layer (SSL) certificate management to monitor and manage the lifecycle of SSL certificates in your SharePoint farm."
---

 
## Remove certificates

SharePoint supports removing certificates via [Remove-SPCertificate](/powershell/module/sharepoint-server/remove-spcertificate) PowerShell cmdlet.

- By default, SharePoint will not allow you to remove a certificate if it is currently assigned to a SharePoint object. You must override the default behavior if you want to force the removal of a certificate. If you override the default behavior, existing assignments of the certificate are cleared.
- The certificate and any private key associated with that certificate is removed from the Windows certificate store on every server in the SharePoint farm.
- The certificate and any private key associated with it is removed from the SharePoint configuration database.
- Any previous exports from the certificate through the SharePoint administration interface will not be removed. Those exported files will still exist.

Use the `Remove-SPCertificate` cmdlet to remove a certificate from SharePoint.

For example:

```powershell
Remove-SPCertificate [-Identity] <SPServerCertificatePipeBind> [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
```

The cmdlet parameters are:

|Parameter|Description|
|--- |--- |
|Identity| The certificate to remove from SharePoint.|
|Force | Specifies that the certificate should be removed from SharePoint, even if the certificate is currently assigned to SharePoint objects. If this parameter is specified, any existing assignments of the certificate are also cleared. If this parameter isn't specified and the certificate is assigned to a SharePoint object, the operation will fail.|


For example:

```powershell
Remove-SPCertificate -Identity "Contoso SharePoint (2020)"
```