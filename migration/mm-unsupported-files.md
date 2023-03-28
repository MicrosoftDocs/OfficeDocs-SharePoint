---
title: "Unsupported file types in Migration Manager"
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
search.appverid: MET150
description: Learn about unsupported file types in Migration Manager and how they affect your overall migration.
---

# Unsupported files in Migration Manager

Migration Manager doesn't support the migration of specific types of files. It's important, however, to understand how unsupported files in your scan or migration task will affect your overall migration.

When Migration Manager discovers an unsupported file during a scan or migration, a failure error is generated at the item level. However, **the failure of a single file doesn't affect the final status of the scan or migration task.**  A scan task that includes unsupported files may still result in a "ready to migrate" status, and a migration task with unsupported files may still show as "complete". 

## Unsupported files

Migration Manager doesn't support the following file types: 

|Source|Unsupported files|
|:-----|:-----|
|Google Drive|Drawings, Forms, Sites, and Maps|
|Box| Box Notes, default files (including Welcome to Box.pdf)|
|Dropbox|Dropbox Paper, default files (including Get started with Dropbox.pdf)</br>Google docs (gdoc/gslides/gsheet) created in Dropbox|
|General|Shortcut files|
|General|Files marked as restricted|
