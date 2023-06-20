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

Migration Manager doesn't support the migration of specific types of files. It's important, however, to understand how unsupported files in your scan or migration task affect your overall migration.

When Migration Manager discovers an unsupported file during a scan or migration, a failure error is generated at the item level. However, **the failure of a single file doesn't affect the final status of the scan or migration task.**  A scan task that includes unsupported files may still result in a "Ready to migrate" status, and a migration task with unsupported files may still show as "Complete". 

## General files that aren't migrated

- Files marked as restricted
- Shortcut files
- 0 byte files (limitation on destination - OneDrive)
- Single large files that exceeds the file size limit. Learn more at [File size limitations for migration to Microsoft 365](mm-file-size-limitations.md)
- Destination path URL that exceeds the file size limit set by Sharepoint or OneDrive (400 characters)


## What isn't migrated from Dropbox

|File|Explanation|
|:-----|:-----
|Dropbox papers| Dropbox doesn't allow us to export Dropbox paper (.paper files) and Dropbox paper templates (.paper files).|
|Dropbox & Dropbox Paper getting started instruction files|These files may cause migration failures and are ignored.|
|URL hyperlink files|Dropbox doesn't allow us to download URL hyperlink files that end with **.url** or **.web**.|


## What isn't migrated from Box

|File|Explanation|
|:-----|:-----
|Box getting started instruction files|These files may cause migration failures and are ignored.|
|Box Notes|Box notes aren't converted to the **.docx** format during migration.


## What isn't migrated from Google Drive

Google doesn't allow us to export these items from Drive.

- Google Drawings
- Google Forms
- Google Sites
- Google maps

### Google Docs, Slides, and Sheets are converted

Google's proprietary formats aren't compatible with anything other than a Google Workspace Drive. When you migrate your content from Google Workspace, Migration Manager converts to the Microsoft Office format from Google's format.

|Google format|Office format|
|:-----|:-----|
|.gsheet|.xlsx|
|.gdoc|.docx|
|.gslide|.pptx|

>[!Note]
> The only way to migrate/download a Google format file is to request that they (Google) convert it. Microsoft does not control the conversion process, and the forced limitations are strictly those of Google.