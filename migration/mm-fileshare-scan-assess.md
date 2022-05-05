---
title: "Step 2: Scan and assess file shares using Migration Manager"
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
description: "Step 2:  Scan and assess file shares using Migration Manager."
---

# Step 2: Scan and assess file shares


File shares are scanned automatically once you add a source. Once the scans are complete, download the generated reports and logs to investigate any possible issues that might block your migration.

>[!Note]
>Two additional endpoints are required for the Scan feature. If you are not able to scan, check this list to make sure you have enabled these endpoints: [Required endpoints](mm-prerequisites.md#required-endpoints).

A table summary appears at the top to give you an at-a-glance overview of your users and content size.

:::image type="content" alt-text="File share scan summary." source="media/mm-fileshare-scan-data-table-summary.png":::

## Reviewing the scan results

1. Select **Add source path**

    :::image type="content" alt-text="Add sourcepath task." source="media/mm-fileshare-add-sourcepath-task.png":::

2. Review the scanned file shares. Search for specific text, or select a filter to review the list more easily.

1. Select **Add source path** if you want to scan additional file shares.

    :::image type="content" alt-text="Fileshare scan list." source="media/mm-fileshare-scan-list.png":::

## Download summary report and scan log

1. From the menu bar, select **Download summary report** to have a local copy of the summary view.
2. Highlight a single row and select  **Download scan log** from the menu bar, to troubleshoot the details of individual files. 

>[!NOTE]
>Migration Manager Box isn't available for users of Office 365 operated by 21Vianet in China.
>
> This feature is also not supported for users of the Government Cloud, including GCC, Consumer, GCC High, or DoD.