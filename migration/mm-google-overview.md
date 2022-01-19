---
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
search.appverid: MET150
description: Overview of how to migrate from Google Workspace to Microsoft 365 with Migration Manager.
---

# Migrate Google Workspace to Microsoft 365 with Migration Manager

>[!Note]
>This release currently supports the migration of up to approximately 10,000 Google Workspace accounts in a single migration. For larger migrations, we recommend you connect with [FastTrack](https://www.microsoft.com/fasttrack).

Collaborate all in one place by migrating your Google documents, data, and users to OneDrive, SharePoint, and Teams in Microsoft 365. 

![Migration Manager main landing page](media/mm-main-landing-google.png)

## How does it work?

- **Step 1:** [Connect to Google](mm-google-step1-connect.md).   Sign in to your Google account and add the Microsoft 365 migration app to your Google Workspace account custom apps. 
- **Step 2:** [Scan and assess](mm-google-step2-scan-assess.md) Google Drive accounts are scanned automatically for you. Once the scans are complete, download the generated reports and logs to investigate any possible issues that might block your migration.
- **Step 3:** [Copy to Migrations list](mm-google-step3-copy-to-migrations.md) After a Google Drive has been scanned and determined ready, add them to your migration list.
- **Step 4:** [Review destination paths](mm-google-step4-review-destinations.md)  We automatically map source paths to any exactly matching destination paths. Ensure content is being copied to the right place by reviewing and modifying as needed for each destination path.
- **Step 5:** [Map identities](mm-google-step5-map-identities.md)   Map your groups and users in Google Drive to an account in Microsoft 365 to migrate your Google Drive sharing settings.
- **Step 6:** [Migrate and Monitor](mm-google-step6-migrate-monitor.md) After reviewing your migration setup, migrate your Google accounts and monitor the progress


## Get started

To get started:

Go to the [Migration Manager page of the new SharePoint admin center](https://aka.ms/ODSP-MM-FS), and sign in with an account that has [admin permissions](/sharepoint/sharepoint-admin-role) for your organization.

Make sure that you have:

- **Access to the destination**: You must either be a global admin or OneDrive/SharePoint admin to the Microsoft 365 tenant where you want to migrate your content. 

- **Access to the source**: Have Google account credentials that have read access to any Google user account you plan to migrate.

- **Prerequisites installed:** Make sure you have the necessary prerequisites installed.

## Google Shared Drives

We are not able to read or write permissions to Google Shared Drives - therefore, we cannot migrate permissions or membership of Google Shared Drives. 

**If you are migrating Google Shared Drives:**

1.  Manually gather the membership list of the Google Shared Drive during your migration planning.
2. Create the team site and document library in SharePoint (destination) **before** you start your migration. You can optionally re-establish the membership list of the shared drive as this time.
3. Migrate the shared folder.  If you didn't do it in step 2, manually make any membership changes to the shared folder.



>[!NOTE]
>Migration Manager Google Workspace isn't available for users of Office 365 operated by 21Vianet in China. It's also not available for users of Microsoft 365 with the German cloud that use the data trustee *German Telekom*. It is supported for users in Germany whose data location isn't in the German datacenter.
>
> This feature is also not supported for users of the Government Cloud, including GCC, Consumer, GCC High, or DoD.

