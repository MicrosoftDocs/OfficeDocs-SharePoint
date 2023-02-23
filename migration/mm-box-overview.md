---
ms.date: 01/21/2021
title: "Overview: Migrate Box using Migration Manager"
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
ms.custom: admindeeplinkSPO
ms.collection: 
- m365solution-migratetom365
- m365solution-scenario
- M365-collaboration
- SPMigration
- highpri
search.appverid: MET150
description: Overview of migration from Box to Microsoft 365 using Migration Manager.
---

# Migrate Box to Microsoft 365 with Migration Manager

Collaborate all in one place by migrating your Box documents, data, and users to OneDrive, SharePoint, and Teams in Microsoft 365. 

:::image type="content" alt-text="Migration Manager main landing page" source="media/mm-main-landing.png":::

## How does it work?

- **Step 1:** [Connect to Box](mm-box-step1-connect.md).   Sign in to your Box account and add the Microsoft 365 migration app to your Box account custom apps. 
- **Step 2:** [Scan and assess](mm-box-step2-scan-assess.md) Box user accounts are scanned automatically for you. Once the scans are complete, download the generated reports and logs to investigate any possible issues that might block your migration.
- **Step 3:** [Copy to Migrations list](mm-box-step3-copy-to-migrations.md) After a Box user has been scanned and determined ready, add them to your migration list.
- **Step 4:** [Review destination paths](mm-box-step4-review-destinations.md)  We automatically map source paths to any exactly matching destination paths. Ensure content is being copied to the right place by reviewing and modifying as needed for each destination path.
- **Step 5:** [Map identities](mm-box-step5-map-identities.md)   Map your groups and users in Box to an account in Microsoft 365 to migrate your Box sharing settings.
- **Step 6:** [Migrate and Monitor](mm-box-step6-migrate-monitor.md) After reviewing your migration setup, migrate your Box accounts and monitor the progress


## Get started

To get started:

Go to the <a href="https://go.microsoft.com/fwlink/?linkid=2185075" target="_blank">Migration center in the SharePoint admin center</a>, and sign in with an account that has [admin permissions](/sharepoint/sharepoint-admin-role) for your organization.

Make sure that you have:

- **Access to the destination**: You must either be a global admin or OneDrive/SharePoint admin to the Microsoft 365 tenant where you want to migrate your content. 

- **Access to the source**: Have Box account credentials that have read access to any Box user account you plan to migrate.

- **Prerequisites installed:** Make sure you have the necessary prerequisites installed.

## File size migration limit

We support files up to 15 GB in size for Box to Microsoft 365 migrations.

## Box notes

Box notes are not converted to a .docx format during migration.  

>[!NOTE]
>Migration Manager Box isn't available for users of Office 365 operated by 21Vianet in China.
>
> This feature is also not supported for users of the Government Cloud, including GCC, Consumer, GCC High, or DoD.
