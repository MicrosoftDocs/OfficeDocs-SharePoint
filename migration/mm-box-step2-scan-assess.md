---
title: "Step 2: Scan and assess Box accounts using Migration Manager"
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
description: "Step 2:  Scan and assess Box users using Migration Manager."
---

# Step 2: Scan and assess Box users

After you connect, add the source paths to scan and assess your Box user accounts.

1. Select **Add source paths** and choose a method; to auto-discover users in Box, target a single source path, or bulk upload the source paths using a CSV file.

![add source paths manually in Box](media/mm-add-source-path.png)

![add source path selections](media/mm-add-source-path-choices-box.png)

2. After adding the source, highlight any or all of the accounts and then select **Scan**.

>[!Important]
> The total number cannot exceed 50,000 tasks.

3. Once the scan is complete, a table summary displays to give you an at-a-glance overview of your users. The summary includes content size, migration readiness, and any issues that need attention. 
4. Review the scanned users. Search for specific text, or select a filter to review the list more easily.

   ![Summary of scanned Box users](media/mm-box-scan-assess-summary.png)


## Download reports

Summary and detailed scan reports are available to assist you in troubleshooting. Download the generated reports and logs to investigate any possible issues that might block your migration.

1. Once the scan is complete, select **Download reports** from the menu bar for *summary* reports.

   ![add source paths manually in Box](media/mm-add-source-path.png)

2. Highlight a selected Box user, and select **Download scan log**  to download a *detailed* scan report of that user account. </br>

## Managing users who own large amounts of data

Upon completing your scan, download the Scan reports and review/address any large source data owners.

The more users simultaneously being transferred, the higher our throughput for your migration. Users with large data sets should be broken into smaller Service Accounts to facilitate faster transfers.

> [!IMPORTANT]
> To maximize throughput, **users should not own greater than 100,000 items or 1 TB of data**. The more users you have, and the smaller the amounts of data they own, the faster your migration proceeds.

**Examples**:

|Size|Action|
|---|---|
|If a user owns more than 400,000 items|Divide the items between four users each with 100,000 items.|
|If a user owns more than 5 TB of data|Divide between five users so that each user owns 1 TB. |

To create Service Accounts, you can work with your Box Admin to carry out the following steps:

1. Once you've identified a large user, determine how many Service Accounts will be required (see example above).
2. Create the Service Accounts in Box and assign them a license.
3. From the original large user, identify the folder(s) you would like to assign to the Service Account.
4. Change the ownership of said folder(s) to the new Service Account. This may require that the original owner first share it with the new owner, where the new owner would have to accept, then the original owner will then have the option to select them as owner. The original owner becomes co-owner of the folder and the permissions will reflect that new status in the Source account. The folder will no longer appear in their *My Files* folder but will now appear in *Shared with me*.
5. When it comes to migrating the Service Account, create a corresponding OneDrive user/SharePoint site to migrate the new Service Account content to.
6. Before making any changes, you should reach out to your tenant administrator, investigate any source custom solutions or integrations that you might be using, and determine if these ownership changes will have any impact.

When mapping, ensure that each Service Account has its own unique matching Destination account to optimize performance.

|Source Path |Destination Path |
|---|---|
|originaluser@contoso.com| originaluser@contoso.com/[upload folder]\* |
|serviceaccount1@contoso.com|serviceaccount1@contoso.com/[upload folder]\* |
|serviceaccount2@contoso.com |serviceaccount2@contoso.com/[upload folder]\* |
|serviceaccount3@contoso.com |serviceaccount3@contoso.com/[upload folder]\* |

Asterisk (\*) = optional folder

## [**Step 3: Copy to migrations**](mm-box-step3-copy-to-migrations.md)

> [!NOTE]
> Migration Manager Box isn't available for users of Office 365 operated by 21Vianet in China.
>
> This feature is also not supported for users of the Government Cloud, including GCC, Consumer, GCC High, or DoD.
