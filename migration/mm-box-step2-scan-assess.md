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
localization_priority: Priority
ms.collection: 
- M365-collaboration
- SPMigration
search.appverid: MET150
description: "Step 2:  Scan and assess Box users using Migration Manager."
---

# Step 2: Scan and assess Box users (preview)

>[!Note]
> Features described in this topic are part of a public preview release. The content and the functionality may change and are not subject to the standard SLAs for support.
>
>This preview release currently supports the migration of up to approximately 1500 Box accounts in a single migration. For larger migrations, we recommend you use the [Mover migration tool](https://Mover.io).



Box users are scanned automatically for you. Once the scans are complete, download the generated reports and logs to investigate any possible issues that might block your migration.

A table summary appears at the top to give you an at-a-glance overview of your users and content size.

![Scan data summary table](media/mm-box-scan-data-table-summary.png)

1.  Review the scanned users. Select **Look for new users** if you want to manually search for more users.

![Scan data list](media/mm-box-scan-list.png)

2. Search for specific text, or select a filter to review the list more easily.

 ![Box scan list filters](media/mm-box-scan-list-filters.png)

3. Once the scan is complete, select **Download scan log** from the menu bar, to troubleshoot any issues. The file will be available from your task bar or downloads folder: **Scan task report.csv**


[ **Step 3: Copy to migrations**](mm-box-step3-copy-to-migrations.md)


>[!NOTE]
>Migration Manager Box preview isn't available for users of Office 365 operated by 21Vianet in China. It's also not available for users of Microsoft 365 with the German cloud that use the data trustee *German Telekom*. It is supported for users in Germany whose data location isn't in the German datacenter.
>
> This feature is also not supported for users of the Government Cloud, including GCC, Consumer, GCC High, or DoD.