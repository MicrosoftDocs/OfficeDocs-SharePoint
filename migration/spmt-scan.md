---
title: "Scan and review a SharePoint Server site using SPMT"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: serdars
recommendations: true
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.subservice: sharepoint-migration
ms.localizationpriority: high
ms.collection: 
- IT_Sharepoint_Server_Top
- Strat_SP_gtc
- SPMigration
- M365-collaboration
- m365initiative-migratetom365
ms.custom:
- seo-marvel-mar2020
description: "Learn how to scan and review a SharePoint Server site using the SharePoint Migration Tool."
--- 
# Scan and assess a SharePoint Server site with SPMT

>[!Note:]
>This feature is currently in public preview and subject to change without notice. Normal service level agreements do not apply.


SPMT 4.0 integrates SharePoint Server assessment directly in the tool.  You can now scan your source sites before migration, review the assessment results, and make any changes before you start your migration.

Same as the migration experience, you can add a new scan by following the prompts and manage all your scan tasks in the scan list page.

   :::image type="content" source="media/spmt-4-home.png" alt-text="new landing page for spmt 4":::

1. Select **Add a scan**.
2. Select a method.  In this example, select a single site.

   :::image type="content" source="media/spmt-4-scan-select-method.png" alt-text="select a scan method - single or bulk":::

3. Enter the URL location of the site you want to scan and then select **Start**.  Alternatively, you can choose to save this scan and run it at a later time.

    :::image type="content" source="media/spmt-scan-single-site-url.png" alt-text="enter the url location of the site you want to scan":::

4. All of your scans are listed for you to review. Select the source URL link to launch the scan dashboard.

    :::image type="content" source="media/spmt-4-scans-list.png" alt-text="view the list of scans":::

5. The dashboard screen gives you a summary of the site content inventory and potential migration risks.  Review the inventory and risk breakdown by scrolling down to the bottom of the dashboard.

    :::image type="content" source="media/spmt-4-scan-dashboard-results.png" alt-text="review the scan results on the dashboard":::

