---
title: "Remote Share Provider Diagnostic Tool"
ms.reviewer: 
ms.author: v-satapathy
manager: nimishasatapathy
ms.date: 6/28/2021
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid:
description: "Learn how the new diagnostic tool helps to validate the data consistency of the content database.."
---

# New Remote Share Provider Diagnostic Tool

[!INCLUDE[appliesto-xxx-xxx-xxx-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)]

We have a new PS cmdlet help admin to validate the data consistency of content database, which is Remote Share Provider enabled. It makes it easier for admin to figure out what are the problems in the remote storage.

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