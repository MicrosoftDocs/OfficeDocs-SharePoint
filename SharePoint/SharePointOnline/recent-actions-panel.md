---
ms.date: 03/14/2023
title: "Review recent SharePoint site actions"
ms.reviewer: cvelaga
manager: serdars
recommendations: true
ms.author: mactra
author: MachelleTranMSFT
audience: admin
f1.keywords:
- NOCSH 
ms.topic: article
ms.service: sharepoint-online
ms.localizationpriority: medium
ms.collection: M365-collaboration
description: "Learn how to review recent actions in SharePoint admin center."
---
# Review recent SharePoint site actions

[!INCLUDE[Advanced Management](includes/advanced-management.md)]

With the recent actions panel, administrators can make changes to SharePoint site properties and review their most recent 30 actions in the [SharePoint admin center](/sharepoint/get-started-new-admin-center).

> [!TIP]
> Recent actions panel is not available for global users. GDAP users will not be able to see the previous and current values of the admin actions.

Changes to site properties like site name, site deletion and storage quota, show as recent actions. The panel shows the previous and current values of site properties, which can be useful when tracking changes.

The recent actions panel only shows changes you made in the last 30 days. Changes made by other admins and organization-level changes won't show in the panel.

You can also export and download a .csv file of all your changes made in the last 30 days.

> [!NOTE]
> When exporting the .csv file, the panel might label files and in-progress actions as failed when they are not.

:::image type="content" source="media/RAC_panel.png" alt-text="Screenshot of Recent admin actions panel":::

## Requirements

To access and use this feature, your organization must have the following subscription:

- [Microsoft Syntex - SharePoint Advanced Management](advanced-management.md)

## View recent actions of a site

1. In the SharePoint admin center, expand **Sites** and select **Active sites**.
2. Select **Your recent actions**. The recent actions panel appears on the right and lists your most recent 30 actions made within the last 30 days.
3. Select **Export** to download the list as a .csv file.
4. Select **View site details** to open the site info panel. From here, you can make changes to site properties like site name, site address, hub association, and aliases.

:::image type="content" source="media/Exported_CSV.png" alt-text="Screenshot of .csv file of recent admin actions":::

> [!TIP]
> Failed and in-progress actions are shown on the panel temporarily and are removed once the browser window is closed. If the browser window is closed while an action is in progress, actions will not be added to the panel.

## Bulk site edits

Bulk edits are listed as one action item in the recent actions panel. Select a bulk action item to see a list of sites affected by a bulk edit. Bulk edits show as separate items in the .csv file. The bulk edit column lets you quickly filter which changes were part of a bulk edit.

Here’s an example of how bulk edits are grouped as one action in the recent actions panel:

You deleted 4 SharePoint sites on May 21 at 6:15 PM. The bulk edit will show as one item named Deleted 4 sites on the recent actions panel. Select the Deleted 4 sites action and the list of deleted SharePoint sites appears.

## Related articles

[Microsoft Syntex Advanced Management overview](advanced-management.md)
