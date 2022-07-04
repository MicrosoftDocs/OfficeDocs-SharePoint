---
title: "Replace a certificate assignment"
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
description: "Learn how SharePoint supports replacing all usage of an existing certificate within SharePoint with a different certificate."
---

# Replace a certificate assignment

SharePoint supports replacing all usage of an existing certificate within SharePoint with a different certificate. For example, if an existing certificate is approaching its expiration and you can replace this existing certificate with a new certificate. Use the [Switch-SPCertificate](/powershell/module/sharepoint-server/switch-spcertificate) Powershell cmdlet to replace the assignments of the existing certificate with the new certificate. All usage of the existing certificate within SharePoint will then be replaced with the new certificate.

For example:

```powershell
Switch-SPCertificate [-Identity] <SPServerCertificatePipeBind> [-NewCertificate] <SPServerCertificatePipeBind> [-WhatIf] [-Confirm] [<CommonParameters>]
```

The cmdlet parameters are:

|Parameter|Description|
|--- |--- |
|Identity| The certificate whose assignments you want to replace.|
|NewCertificate | The certificate that should replace all of the assignments of the certificate specified by the Identity parameter.|

For example:

```powershell
Switch-SPCertificate -Identity "Contoso SharePoint (2020)" -NewCertificate "Contoso SharePoint (2021)"
```