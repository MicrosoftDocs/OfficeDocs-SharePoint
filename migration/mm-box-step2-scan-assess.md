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

After you connect, Box users are automatically scanned. Once the scans are complete, download the generated reports and logs to investigate any possible issues that might block your migration.

A table summary appears at the top to give you an at-a-glance overview of your users. The summary includes content size, migration readiness, and any issues that need attention.

   ![Summary of scanned Box users](media/mm-box-scan-assess-summary.png)


1. Review the scanned users. Search for specific text, or select a filter to review the list more easily
2. Select **Look for new users** to manually search for more users.

    ![Box menu bar after scan](media/mm-box-scan-menu.png)



## Download reports

Summary and detailed scan reports are available to troubleshoot any issues.

1. Once the scan is complete, select **Download reports** from the menu bar for summary reports.

    ![Box menu bar after scan](media/mm-box-scan-menu.png)


2. Highlight a selected Box user, and select **Download scan log**  to download a detailed scan report of that user account. </br>

    ![Download individual scan log button](media/mm-box-scan-download-scan-log.png)

[ **Step 3: Copy to migrations**](mm-box-step3-copy-to-migrations.md)


>[!NOTE]
>Migration Manager Box isn't available for users of Office 365 operated by 21Vianet in China. It's also not available for users of Microsoft 365 with the German cloud that use the data trustee *German Telekom*. It is supported for users in Germany whose data location isn't in the German datacenter.
>
> This feature is also not supported for users of the Government Cloud, including GCC, Consumer, GCC High, or DoD.