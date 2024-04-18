---
ms.date: 08/11/2023
title: "Overview: Migrate Google Workspace to Microsoft 365 with Migration Manager"
ms.reviewer: 
ms.author: heidip
author: MicrosoftHeidi
manager: jtremper
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: microsoft-365-migration
ms.localizationpriority: high
ms.collection: 
- m365solution-migratetom365
- m365solution-scenario
- M365-collaboration
- SPMigration
- highpri
- m365initiative-migratetom365
ms.custom: admindeeplinkSPO
search.appverid: MET150
description: Overview of how to migrate from Google Workspace to Microsoft 365 with Migration Manager.
---

# Migrate Google Workspace to Microsoft 365 with Migration Manager

Collaborate all in one place by migrating your Google Workspace files, metadata, and permissions to OneDrive and SharePoint in Microsoft 365. 

## How does it work?

- **Step 1:** [Connect to Google](mm-google-step1-connect.md). Sign in to your Google account and install Microsoft 365 migration app in Google Workspace Marketplace. 

- **Step 2:** [Scan and assess](mm-google-step2-scan-assess.md). Add Google Drives for scanning. Once the scans are complete, download [Scan reports](/sharepointmigration/mm-cloud-reports) to investigate any possible issues that might block your migration.
- **Step 3:** [Copy to Migrations list](mm-google-step3-copy-to-migrations.md). After a Google Drive has been scanned as "Ready to migrate", add them to your migration list.

- **Step 4:** [Review destination paths](mm-google-step4-review-destinations.md). We automatically map source paths to any exactly matching destination paths. Ensure content is being copied to the right place by reviewing and modifying as needed for each destination path.

- **Step 5:** [Map identities](mm-google-step5-map-identities.md). Map your groups and users in Google Drive to those in Microsoft 365 to migrate metadata and permissions correctly.

- **Step 6:** [Migrate and Monitor](mm-google-step6-migrate-monitor.md). After reviewing your [migration setup](/sharepointmigration/mm-project-settings), migrate your Google Drives and monitor the progress.

>[!Tip]
>Watch this video to help get started:  [Migrate Google files to Microsoft 365 with Migration Manager](https://youtu.be/GZ4kTX31U-A)


## Get started

To get started:

Go to the Migration overview page in the **Microsoft Admin Center** or Migration Manager in the **SharePoint Admin center.** Sign in with an account that has [admin permissions](/sharepoint/sharepoint-admin-role) for your organization.

Make sure that you have:

- **Access to the destination**: You must either be a global admin or OneDrive/SharePoint admin to the Microsoft 365 tenant where you want to migrate your content. 

- **Access to the source**: Have Google account credentials that have read access to any Google user account you plan to migrate.

- **Prerequisites installed:** Make sure you have the necessary prerequisites installed.

## Google Shared Drives and permissions

Google Shared drives can now be discovered and migrated normally. Google Shared Drive permissions are migrated according to what you have set in Project settings, under [general permission setting](/sharepointmigration/mm-project-settings-permissions#migrate-permissions). 

Folder permissions are migrated by default. File permissions are migrated on demand. 

We recommend the following steps when migrating permissions in your shared drive:

- Recreate a Microsoft 365 group with the same memberships as the Google Drive group. You can either create a new group or edit the group linked to the Team site designated as the migration destination for the Google Shared Drive.
- In the 'Map Identities' setting, map the original Google Drive group of the shared drive to the Microsoft 365 group.


## What isn't migrated

Google Sites and Google Maps migration are not supported, while Google Docs/Sheets/Slides/Forms are migrated as equivalent file types in Microsoft 365. [Learn more about the unsupported files](/sharepointmigration/mm-unsupported-files)

### File size of Google proprietary files

Google only started calculating the size of its proprietary files, including Google Docs, Sheets, Forms, and Slides, on May 2, 2022. Any Google proprietary files created and modified **before** May 2, 2022 won't include file size in the metadata info we get from the API calls. As a result, all Google proprietary files created before May 2, 2022 default to a scanned size of 1 byte and are reported as such in our *ScanSummary report*.

### Files marked as restricted

Google Workspace/Drive allows owners to control the ability for users to copy, download, or print files on a per-file basis. By default, this feature is enabled for each file. To ensure a successful migration, this setting must remain enabled. Disabling it may result in the following error when migrating a file owned by another user:
`Permissions issue: File marked as restricted or not copyable`
To enable this setting:
1. Navigate to the **Share** panel for the file.
1. Click on the **Settings Icon** located at the top right corner.
1. Select the checkbox for the setting "**Viewers and commenters can see the option to download, print, and copy.**"



