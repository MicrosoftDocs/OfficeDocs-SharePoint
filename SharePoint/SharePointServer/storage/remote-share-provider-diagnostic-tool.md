---
title: "Remote Share Provider Diagnostic Tool"
ms.reviewer: 
ms.author: v-nsatapathy
manager: nimishasatapathy
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 5cdce2aa-fa6e-4888-a34f-de61713f5096
description: "Learn how the new diagnostic tool helps to validate the data consistency of the content database.."
---

# New Remote Share Provider diagnostic tool

[!INCLUDE[appliesto-xxx-xxx-xxx-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)]

We have a new PowerShell cmdlet help admin to validate the data consistency of content database, which is Remote Share Provider enabled. It makes it easier for admin to figure out what are the problems in the remote storage.

```
SYNTEX

Test-SPRemoteShareBlobStore 

-ContentDatabase <SPContentDatabasePipeBind>

[-LogPath <String>]

The comlet parameters are:

-ContentDatabase <SPContentDatabasePipeBind>

The content database need to be validated against

[-LogPath <String>]
 ```
The path of the validation log
