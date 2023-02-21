---
ms.date: 08/17/2022
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

# File size limitations for migration to Microsoft 365

Whether you're using Migration Manager or the SharePoint Migration Tool (SPMT) for your migration project, the maximum file size allowed depends on the location of your source content. Cloud scenarios have a file size limit of 15 GB, while file share migrations support files up to 250 GB in size.

## Migration Manager

|Scenario|Maximum file size supported|
|:-----|:-----|
|File share to Microsoft 365|250 GB|
|Google to Microsoft 365 |15 GB|
|Dropbox to Microsoft 365 |15 GB|
|Egnyte to Microsoft 365 |15 GB|
|Box to Microsoft 365|15 GB|


## SharePoint Migration Tool (SPMT)

|Scenario|Maximum file size supported|
|:-----|:-----|
|SharePoint Server to Microsoft 365|250 GB|
|File share to Microsoft 365 |250 GB|

## Migration API

|Scenario|Maximum file size supported|
|:-----|:-----|
|File migration to Microsoft 365|250 GB|
