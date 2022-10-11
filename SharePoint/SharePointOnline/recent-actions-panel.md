---
title: "Review your recent actions in SharePoint admin center"
ms.reviewer: 
manager: serdars
recommendations: 
ms.author: mactra
author: its-mactra
ms.date: 10/10/2022
audience: admin
f1.keywords:
- NOCSH 
ms.topic: article
ms.service: sharepoint-online
ms.localizationpriority: medium
ms.collection:
- M365-collaboration
- Strat_SP_admin
search.appverid:
ms.assetid: TBD
description: "Monitor your changes in recent actions panel in SharePoint admin center"
---
# Review your recent actions in SharePoint admin center

Make changes to SharePoint site properties and review your most recent 30 actions [SharePoint admin center](/sharepoint/get-started-new-admin-center) actions with recent actions panel.

Changes to site properties like site name, site URL, site deletion and storage quota, will show as actions in your list of recent actions. The panel shows the previous and current values of site properties which is helpful to track changes.

The list of recent actions is limited to actions you made from the SharePoint admin center in the last 30 days. The recent actions panel doesn’t show the actions of other admins in your organization or changes made to organizational-level settings.  

While the recent actions panel will only show the last 30 actions in the last 30 days, you can download the .csv file to view all your changes in the last 30 days. The exported data from the .csv file is especially useful when you need to perform a deeper analysis.

## View recent actions of a site

1. In  the SharePoint admin center, expand **Sites** and select **Active sites**.
2. Select **Your recent actions**. The recent actions panel appears on the right and lists your most recent 30 actions made within the last 30 days.
3. You can select **Export** to download the list as a .csv file.
4. Select **View site details** to open the site info panel. From here, you can make changes to site properties like site name, site address, hub association, and aliases.

### Bulk site edits

Bulk site edits such as deleting multiple sites are listed as one action item in the recent actions panel. Select a bulk action item on the recent actions panel to see a list of sites affected by a bulk edit.

In the .csv file, a bulk site edit is listed as separate line items so you can see the details of which sites were affected. The bulk edit column of the report lets you quickly filter which changes were part of a bulk edit.

Here’s an example on how bulk edits are grouped as one action in the recent actions panel:

If you delete 4 SharePoint sites on May 21st at 6:15 PM, it will show as one item named Deleted 4 sites on the recent actions panel. Select the Deleted 4 sites action and the list of deleted SharePoint sites appears.
