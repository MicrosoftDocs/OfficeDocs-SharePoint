---
title: "Unsupported file types in Migration Manager"
ms.date: 08/30/2023
ms.reviewer: 
ms.author: heidip
author: MicrosoftHeidi
manager: jtremper
recommendations: true
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: microsoft-365-migration
ms.localizationpriority: high
ms.collection: 
- M365-collaboration
- SPMigration
- m365initiative-migratetom365
search.appverid: MET150
description: Learn about unsupported file types in Migration Manager and how they affect your overall migration.
---

# Unsupported files in Migration Manager
Migration Manager does not support the migration of specific file types. However, it's crucial to understand how these unsupported files impact your overall migration process.

When Migration Manager encounters an unsupported file during a scan or migration, it generates a failure error at the item level. However, **these unsupported files do not impact the final status of the scan or migration task**. Even if a scan task includes only unsupported files for all failed items, it can still achieve a "Ready to migrate" status. Similarly, a migration task with only unsupported files for all failed items can still be marked as "Completed".

## General files that aren't migrated
- Files marked as restricted
- Shortcut files
- 0-byte files
- Single large files that exceed the file size limit. Learn more at [File size limitations](mm-file-size-limitations.md)
- Destination path URL that exceeds 400 characters

## What isn't migrated from Google Drive
These items are not migrated:
- Google Sites
- Google Maps
> [!Important]
> - Google Forms are now migrated by default. Forms Desintination must be designated for migration tasks with Forms. [Learn more about Forms Destination](/sharepointmigration/mm-google-step4-review-destinations)
> - Google Drawings are migrated as PNG files by default.
> - We don't scan unorganized or "orphaned" files. As a result, they won't be migrated or shown in any of our reports. To learn more about unorganized files see:  [Unorganized or "orphaned" files in Google](https://support.google.com/drive/thread/4333474/can-t-find-a-file-s-location-on-drive-no-location-provided?hl=en)

### Google Docs, Slides, and Sheets are converted
During migration, the Google Export API converts the below Google files into Microsoft Office files. The original files in Google Drive aren't affected.

|Google format|Office format|
|:-----|:-----|
|.gsheet|.xlsx|
|.gdoc|.docx|
|.gslide|.pptx|

## What isn't migrated from Dropbox

|File|Explanation|
|:-----|:-----
|Dropbox papers| Dropbox doesn't allow us to export Dropbox paper (.paper files) and Dropbox paper templates (.paper files).|
|Dropbox & Dropbox Paper getting started instruction files|These files can cause migration failures and are ignored.|
|URL hyperlink files|Dropbox doesn't allow us to download URL hyperlink files that end with **.url** or **.web**.|
|Google files (gdoc/gslides/gsheet) in Dropbox|Dropbox doesn't allow us to download Google files.|


## What isn't migrated from Box

|File|Explanation|
|:-----|:-----
|Box getting started instruction files|These files can cause migration failures and are ignored.|

>[!Note]
>Migration Manager now supports converting Box notes to .docx format. However, certain elements such as File Preview, Table of Contents, and Annotations will be omitted during the conversion process.



