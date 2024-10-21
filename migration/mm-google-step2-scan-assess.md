---
ms.date: 08/07/2023
title: "Step 2: Scan and assess Google accounts using Migration Manager"
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
- m365solution-migratefileshares
- m365solution-migratetom365
- m365solution-scenario
- M365-collaboration
- SPMigration
- highpri
- m365initiative-migratetom365
search.appverid: MET150
description: "Step 2:  Scan and assess Google users using Migration Manager."
---

# Step 2: Scan and assess Google Drives

After you have connected to Google, add the Drives to scan and assess.

1. Select **Add Drives** and choose a method: to look for new users in Google Drives, target a single source path, or bulk upload the source paths using a CSV file.  You can choose to automatically start scanning or do it later.  However, all drives must be scanned before you can migrate them.

   :::image type="content" source="media/mm-google-add-drive-choices.png" alt-text="select how to add google drives":::

2. After adding the drives, highlight any or all of the drives and then select **Scan** if you haven't already.

>[!Important]
> The total number cannot exceed 50,000 tasks.

3. Once the scan is complete, a table summary displays to give you an at-a-glance overview of your users. The summary includes content size, migration readiness, and any issues that need attention. Review the scanned users. Search for specific text, or select a filter to review the list more easily or download summary and detailed reports to troubleshoot further.

## Download reports

Summary and detailed scan reports are available to assist you in troubleshooting. Download the generated reports and logs to investigate any possible issues that might block your migration.

1. Once the scan is complete, select **Download reports**.

   ![download reports for google](media/mm-google-download-reports-button.png)

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

## Go to [**Step 3: Copy to migrations**](mm-Google-step3-copy-to-migrations.md)

