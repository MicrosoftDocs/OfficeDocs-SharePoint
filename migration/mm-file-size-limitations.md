---
title: "File size limitations when migrating files to Microsoft 365"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: serdars
recommendations: true
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.subservice: sharepoint-migration
ms.localizationpriority: high
ms.collection: 
- M365-collaboration
- SPMigration
ms.custom: admindeeplinkSPO
search.appverid: MET150
description: File size limitations when migrating files with Migration Manager and SharePoint Migration Tool (SPMT).
---

# File size limitations for migration 

Depending on the location of your source content, the supported file size limits vary.  Cloud scenarios have a file size limit of 15 GB, while file share migrations support files up to 250 GB in size.

## File size limits when using Migration Manager 
|Scenario|Maximum file size migrated|
|:-----|:-----|
|File share to Microsoft 365|250 GB|
|Google to Microsoft 365 |15 GB|
|Dropbox to Microsoft 365 |15 GB|
|Egnyte to Microsoft 365 |15 GB|
|Box to Microsoft 365|15 GB|


## File size limits when uisng SharePoint Migration tool

|Scenario|Maximum file size migrated|
|:-----|:-----|
|SharePoint Server to Microsoft 365|250 GB|
|File share to Microsoft 365 |250 GB|

## File size limits using Migration API

|Scenario|Maximum file size migrated|
|:-----|:-----|
|File migration to Microsoft 365|250 GB|