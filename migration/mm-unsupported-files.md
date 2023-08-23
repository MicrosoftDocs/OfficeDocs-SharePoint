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
|Google files (gdoc/gslides/gsheet) in Dropbox|These files can NOT be converted to Microsoft Office files, thus are unsupported for migration.|


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

>[!Note]
>We don't scan unorganized or "orphaned" files. As a result, they won't be migrated or shown in any of our reports. To learn more about unorganized files see:  [Unorganized or "orphaned" files in Google](https://support.google.com/drive/thread/4333474/can-t-find-a-file-s-location-on-drive-no-location-provided?hl=en)

### Google Docs, Slides, and Sheets are converted

Google's proprietary formats aren't compatible with anything other than a Google Workspace Drive. When you migrate your content from Google Workspace, the Google API converts the files into Microsoft Office files. The original files in Google Drive are not affected.

|Google format|Office format|
|:-----|:-----|
|.gsheet|.xlsx|
|.gdoc|.docx|
|.gslide|.pptx|
