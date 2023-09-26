---
title: "Move certificates between certificate stores"
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
description: "Learn how SharePoint supports moving certificates."
---
 
# Move certificates between certificate stores

[!INCLUDE[appliesto-xxx-xxx-xxx-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)]

SharePoint supports moving certificates between certificate stores using the [Move-SPCertificate](/powershell/module/sharepoint-server/move-spcertificate) PowerShell cmdlet.

```powershell
Move-SPCertificate [-Identity] <SPServerCertificatePipeBind> -NewStore {Default | EndEntity | Intermediate | Root} [-Force]
```

The cmdlet parameters are:

|Parameter|Description|
|--- |--- |
|Identity| The certificate to move.|
|NewStore (Default / EndEntity / Intermediate / Root)| The certificate store to move the certificate to. If Default is specified, SharePoint will automatically select the appropriate certificate store for the certificate.|
|Force|Specifies that the certificate should be moved to a different certificate store, even if the certificate is currently assigned to SharePoint objects.<br> If this parameter is specified, any existing assignments of the certificate are cleared. If this parameter isn't specified and the certificate is assigned to a SharePoint object, the operation will fail.|

Example cmdlet syntax:

```powershell
Move-SPCertificate -Identity "Contoso SharePoint (2020)" -NewStore EndEntity
```
