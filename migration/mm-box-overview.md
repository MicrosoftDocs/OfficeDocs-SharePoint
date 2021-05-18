---
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
localization_priority: Priority
ms.collection: 
- m365solution-migratetom365
- m365solution-scenario
- M365-collaboration
- SPMigration
search.appverid: MET150
description: Overview of migration from Box to Microsoft 365 using Migration Manager.
---

# Migrate Box to Microsoft 365 with Migration Manager (preview)


#### Got a minute?

![take our survey about your experience migratiungi](https://docs.microsoft.com/office/media/icons/sign-up-blue.png)  Please take our <a href="https://microsoft.qualtrics.com/jfe/form/SV_5BeuymEC0Dnkn30" target="_blank">short survey about migrating to Microsoft 365</a>. We'd love to hear from you!

</br>

>[!Note]
> Features described in this topic are part of a public preview release. The content and the functionality may change and are not subject to the standard SLAs for support.
>
>This preview release currently supports the migration of up to approximately 1500 Box accounts in a single migration. For larger migrations, we recommend you use the [Mover migration tool](https://Mover.io).


Collaborate all in one place by migrating your Box documents, data, and users to OneDrive, SharePoint, and Teams in Microsoft 365. 

![Migration Manager main landing page](media/mm-main-landing.png)

## How does it work?

- **Step 1:** [Connect to Box](mm-box-step1-connect.md).   Sign in to your Box account and add the Microsoft 365 migration app to your Box account custom apps. 
- **Step 2:** [Scan and assess](mm-box-step2-scan-assess.md) Box user accounts are scanned automatically for you. Once the scans are complete, download the generated reports and logs to investigate any possible issues that might block your migration.
- **Step 3:** [Copy to Migrations list](mm-box-step3-copy-to-migrations.md) After a Box user has been scanned and determined ready, add them to your migration list.
- **Step 4:** [Review destination paths](mm-box-step4-review-destinations.md)  We automatically map source paths to any exactly matching destination paths. Ensure content is being copied to the right place by reviewing and modifying as needed for each destination path.
- **Step 5:** [Map identities](mm-box-step5-map-identities.md)   Map your groups and users in Box to an account in Microsoft 365 to migrate your Box sharing settings.
- **Step 6:** [Migrate and Monitor](mm-box-step6-migrate-monitor.md) After reviewing your migration setup, migrate your Box accounts and monitor the progress


## Get started

To get started:

Go to the [Migration Manager page of the new SharePoint admin center](https://aka.ms/ODSP-MM-BOX), and sign in with an account that has [admin permissions](/sharepoint/sharepoint-admin-role) for your organization.

Make sure that you have:

- **Access to the destination**: You must either be a global admin or OneDrive/SharePoint admin to the Microsoft 365 tenant where you want to migrate your content. 

- **Access to the source**: Have Box account credentials that have read access to any Box user account you plan to migrate.

- **Prerequisites installed:** Make sure you have the necessary prerequisites installed.

>[!NOTE]
>Migration Manager Box preview isn't available for users of Office 365 operated by 21Vianet in China. It's also not available for users of Microsoft 365 with the German cloud that use the data trustee *German Telekom*. It is supported for users in Germany whose data location isn't in the German datacenter.
>
> This feature is also not supported for users of the Government Cloud, including GCC, Consumer, GCC High, or DoD.





