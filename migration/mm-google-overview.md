---
ms.date: 01/21/2021
title: "Overview: Migrate Google Workspace to Microsoft 365 with Migration Manager"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: serdars
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.subservice: sharepoint-migration
ms.localizationpriority: high
ms.collection: 
- m365solution-migratetom365
- m365solution-scenario
- M365-collaboration
- SPMigration
- highpri
ms.custom: admindeeplinkSPO
search.appverid: MET150
description: Overview of how to migrate from Google Workspace to Microsoft 365 with Migration Manager.
---

# Migrate Google Workspace to Microsoft 365 with Migration Manager


Collaborate all in one place by migrating your Google documents, data, and users to OneDrive, SharePoint, and Teams in Microsoft 365. 

![Migration Manager main landing page](media/mm-main-landing-google.png)

## How does it work?

- **Step 1:** [Connect to Google](mm-google-step1-connect.md).   Sign in to your Google account and add the Microsoft 365 migration app to your Google Workspace account custom apps. 
- **Step 2:** [Scan and assess](mm-google-step2-scan-assess.md). Google Drive accounts are scanned automatically for you. Once the scans are complete, download the generated reports and logs to investigate any possible issues that might block your migration.
- **Step 3:** [Copy to Migrations list](mm-google-step3-copy-to-migrations.md). After a Google Drive has been scanned and determined ready, add them to your migration list.
- **Step 4:** [Review destination paths](mm-google-step4-review-destinations.md).  We automatically map source paths to any exactly matching destination paths. Ensure content is being copied to the right place by reviewing and modifying as needed for each destination path.
- **Step 5:** [Map identities](mm-google-step5-map-identities.md).   Map your groups and users in Google Drive to an account in Microsoft 365 to migrate your Google Drive permission settings.
- **Step 6:** [Migrate and Monitor](mm-google-step6-migrate-monitor.md). After reviewing your migration setup, migrate your Google accounts and monitor the progress


## Get started

To get started:

Go to the <a href="https://go.microsoft.com/fwlink/?linkid=2185075" target="_blank">Migration center</a> in the SharePoint admin center, and sign in with an account that has [admin permissions](/sharepoint/sharepoint-admin-role) for your organization.

Make sure that you have:

- **Access to the destination**: You must either be a global admin or OneDrive/SharePoint admin to the Microsoft 365 tenant where you want to migrate your content. 

- **Access to the source**: Have Google account credentials that have read access to any Google user account you plan to migrate.

- **Prerequisites installed:** Make sure you have the necessary prerequisites installed.

## Google Shared Drives

>[!Important]
>We are not able to read or write permissions to Google Shared Drives, therefore we cannot migrate permissions or membership of Google Shared Drives. 
>
>Google Shared Drives do not allow explicit folder-level permissions. Instead, Shared Drive permissions are based on the Shared Drive members.
>
>If you are migrating Google Shared Drives, follow the steps below.


**To migrate Google Shared Drives:**

1. Manually gather the membership list of the Google Shared Drive during your migration planning.
2. Create the destination document library in the appropriate team site of your SharePoint tenant. At this time, we recommend that you re-establish the membership list of the Google Shared Drive on the destination document library in your SharePoint tenant
3. Migrate the Google Shared Drive. If you didn't do it in step 2, re-establish the membership list of the Google Shared Drive in the destination document library in your SharePoint tenant.

## What isn't migrated

### Google Drawings, Forms, Sites, and Maps

Google doesn't allow us to export Drawings, Forms, Sites, and Maps from Drive. These aren't migrated.

### Docs, Slides, and Sheets

Google's proprietary formats aren't compatible with anything other than a Google Workspace Drive. When migrating from Google Workspace, Migration Manager converts to the Microsoft Office format from Google's format.


|Google format|Office format|
|:-----|:-----|
|.gsheet|.xlsx|
|.gdoc|.docx|
|.gslide|.pptx|


>[!Note]
>The only way to migrate/download a Google format file is to request that they [Google] convert it. Microsoft does not control the conversion process, and the forced limitations are strictly on Google's end.

### File size of Google proprietary files

Google only started calculating the size of its proprietary files, including Google Docs, Sheets, and Slides, on May 2, 2022. Any Google proprietary files created and modified **before** May 2, 2022 don't include file size in the metadata info we get from the API calls. As a result, all Google proprietary files created before May 2, 2022 default to a scanned size of 1 byte and are reported as such in our *ScanSummary report*.

### Files marked as restricted

Google WorkspaceDrive lets owners disable the ability for users to copy, download, or print a file on a per-file basis. To work properly, this feature must be disabled on each file for which it has been enabled. It not enabled, you'll receive an error stating:

`Permissions issue: File marked as restricted or not copyable`

To disable this feature:

1. See the **Sharing** settings for a file, and select **Advanced**. 
2. Select the checkbox for the owner of the file to **Disable options to download, print, and copy for commenters and viewers.**
    
### What happens to Google Drive shortcuts?

Shortcut files aren't supported for migration and therefore not migrated.

## File size migration limit

We support files up to 15 GB in size for Google to Microsoft 365 migrations.


>[!NOTE]
>
>Migration Manager Google isn't available for users of Office 365 operated by 21Vianet in China.
>
>Google migration is not available for users of the Government Cloud, including GCC, Consumer, GCC High, or DoD.

