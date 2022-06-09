---
title: "Step 2: Scan and assess Google accounts using Migration Manager"
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
- m365solution-migratefileshares
- m365solution-migratetom365
- m365solution-scenario
- M365-collaboration
- SPMigration
search.appverid: MET150
description: "Step 2:  Scan and assess Google users using Migration Manager."
---

# Step 2: Scan and assess Google Drives

After you have connected to Google, the drives are displayed automatically for you. Once the scan is complete, download the generated reports and logs to investigate any possible issues that might block your migration.

A table summary appears at the top to give you an at-a-glance overview of your users and content size.

![google table summary of scan drives](media/mm-google-table-summary.png)

1. Select **Scan**. Review the scanned drives.
2. Search for specific text, or select a filter to review the list more easily.

   ![filter options for google drive scan results](media/mm-google-filters-scan.png)

3. To include other sources, select **Add source path**. Choose to look for new sources, enter a specific source, or bulk upload many sources via a CSV file.

   ![add more google source drives](media/mm-google-add-source-paths.png)

## Download reports

Summary and detailed reports are available to troubleshoot any issues.

1. Once the scan is complete, select **Download reports**.

   ![download reports for google](media/mm-dropbox-summary-report-menu.png)

2. To download a detailed scan report for an individual account, select a single row, then select **Download scan log**.   </br>

## Managing users who own large amounts of data

Upon completing your scan, download the scan reports and review/address any large source data owners.

The more users simultaneously being transferred, the higher our throughput for your migration. Users with large data sets should be broken into smaller Service Accounts to facilitate faster transfers.

> [!IMPORTANT]
> To maximize throughput, **users should not own greater than 100,000 items or 1 TB of data**. The more users you have, and the smaller the amounts of data they own, the faster your migration proceeds.

**Examples**:

|Size|Action|
|---|---|
|If a user owns more than 400,000 items|Divide the items between four users each with 100,000 items.|
|If a user owns more than 5 TB of data|Divide between five users so that each user owns 1 TB. |

To create Service Accounts, work with your G-Suite Admin to carry out the following steps:

1. Once you have identified a large user, determine how many Service Accounts will be required (see example above).
2. Create the Service Accounts in G-Suite and assign them a license.
3. From the original large user, identify the folder(s) you would like to assign to the Service Account.
4. Change the ownership of said folder(s) to the new Service Account. This may require that the original owner first share it with the new owner, where the new owner would have to accept, then the original owner will then have the option to select them as owner. The original owner becomes co-owner of the folder and the permissions will reflect that new status in the Source account. The Folder will no longer appear in their My Files folder but will now appear in Shared with me.
5. When it comes to migrating the Service Account, create a corresponding OneDrive user/SharePoint site to migrate the new Service Account content to.

When mapping please ensure that each Service Account has its own unique matching Destination account to optimize performance.

|Source Path|Destination Path|
|---|---|
|originaluser@contoso.com|originaluser@contoso.com/[upload folder]*|
|serviceaccount1@contoso.com|serviceaccount1@contoso.com/[upload folder]*|
|serviceaccount2@contoso.com|serviceaccount2@contoso.com/[upload folder]*|
|serviceaccount3@contoso.com|serviceaccount3@contoso.com/[upload folder]*|

Asterisk (*) = optional folder

**NEXT:**  [ **Step 3: Copy to migrations**](mm-Google-step3-copy-to-migrations.md)

> [!NOTE]
> Migration Manager Google isn't available for users of Office 365 operated by 21Vianet in China.
>
> This feature is also not supported for users of the Government Cloud, including GCC, Consumer, GCC High, or DoD.