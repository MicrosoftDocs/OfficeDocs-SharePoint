---
title: "Rename certificate friendly names"
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
description: "Learn how SharePoint supports changing the friendly name of certificates."
---
 
# Rename certificate friendly names

[!INCLUDE[appliesto-xxx-xxx-xxx-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)]

SharePoint supports changing the friendly name of certificates using the [Rename-SPCertificate](/powershell/module/sharepoint-server/rename-spcertificate) PowerShell cmdlet.

```powershell
Rename-SPCertificate [-Identity] <SPServerCertificatePipeBind> -NewFriendlyName <string>
```

The cmdlet parameters are:

|Parameter|Description|
|--- |--- |
|Identity| The certificate to be renamed. |
|NewFriendlyName|The new friendly name for the certificate.|

Example cmdlet syntax:

```powershell
Rename-SPCertificate -Identity "Contoso SharePoint" -NewFriendlyName "Contoso SharePoint (2020)"
```