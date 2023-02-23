---
ms.date: 01/21/2021
title: "Overview: Migrate Dropbox using Migration Manager"
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
description: Overview of migration from Dropbox to Microsoft 365 using Migration Manager.
---

# Migrate Dropbox to Microsoft 365 with Migration Manager


Collaborate all in one place by migrating your Dropbox documents, data, and users to OneDrive, SharePoint, and Teams in Microsoft 365. 

:::image type="content" alt-text="Migration Manager main landing page" source="media/mm-main-landing-Dropbox.png":::

## How does it work?

- **Step 1:** [Connect to Dropbox](mm-Dropbox-step1-connect.md).  Sign in to your Dropbox administrator account to connect to your Microsoft 365 migration.
- **Step 2:** [Scan and assess](mm-Dropbox-step2-scan-assess.md) Dropbox accounts are scanned automatically for you. Once the scans are complete, download the generated reports and logs to investigate any possible issues that might block your migration.
- **Step 3:** [Copy to Migrations list](mm-Dropbox-step3-copy-to-migrations.md) After Dropbox has been scanned and determined ready, add them to your migration list.
- **Step 4:** [Review destination paths](mm-Dropbox-step4-review-destinations.md)  We automatically map source paths to any exactly matching destination paths. Ensure content is being copied to the right place by reviewing and modifying as needed for each destination path.
- **Step 5:** [Map identities](mm-Dropbox-step5-map-identities.md)   Map your groups and users in Dropbox to an account in Microsoft 365 to migrate your Dropbox sharing settings.
- **Step 6:** [Migrate and Monitor](mm-Dropbox-step6-migrate-monitor.md) After reviewing your migration setup, migrate your Dropbox accounts and monitor the progress


## Get started

To get started:

Go to the <a href="https://go.microsoft.com/fwlink/?linkid=2185075" target="_blank">Migration center</a> in the SharePoint admin center, and sign in with an account that has [admin permissions](/sharepoint/sharepoint-admin-role) for your organization.

Make sure that you have:

- **Access to the destination**: You must either be a global admin or OneDrive/SharePoint admin to the Microsoft 365 tenant where you want to migrate your content. 

- **Access to the source**: Have Dropbox account credentials that have read access to any Dropbox user account you plan to migrate.

- **Prerequisites installed:** Make sure you have the necessary prerequisites installed.

## File size migration limit

We support files up to 15 GB in size for Dropbox to Microsoft 365 migrations.

>[!NOTE]
>Migration Manager Dropbox isn't available for users of Office 365 operated by 21Vianet in China.
>
> This feature is also not supported for users of the Government Cloud, including GCC, Consumer, GCC High, or DoD.


