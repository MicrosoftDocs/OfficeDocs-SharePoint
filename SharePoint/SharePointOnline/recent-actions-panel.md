---
ms.date: 04/10/2023
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
ms.collection: 
- M365-collaboration
- Highpri
- Tier1
description: "Learn how to review recent admin actions in SharePoint admin center."
---
# Review recent SharePoint site actions

[!INCLUDE[Advanced Management](includes/advanced-management.md)]

With the recent actions panel, administrators can make changes to SharePoint site properties and review their most recent actions in the [SharePoint admin center](/sharepoint/get-started-new-admin-center).

Changes to site properties like site name, site deletion and storage quota show as recent actions.

The recent actions panel only shows the changes you make to site properties. Changes made by other administrators and organization-level changes won't show in the panel.

:::image type="content" source="media/RAC_panel.png" alt-text="Screenshot of Recent admin actions panel":::

> [!NOTE]
> Recent actions panel is not available for global readers. GDAP administrators will not be able to see the previous and current values of the administrator actions.

## Non-premium and premium features of recent actions panel

### Non-premium

The non-premium version of recent actions panel lets you:

- review actions made within the current session. Once you close the browser or sign out, the recent actions panel will clear the history.

### Premium

With the [Microsoft Syntex - SharePoint Advanced Management subscription](advanced-management.md), you'll have access to premium features of recent actions panel. The premium version lets you:

- review the last 30 actions made within the last 30 days in the recent actions panel.
- view additional details such as previous and current value of the settings changed and directly access the site details panel to review the change.
- export and download a. csv file detailing all the changes made within the last 30 days.

## Requirements

To access and use the **premium** version of this feature, your organization must have the following subscription:

- [Microsoft Syntex - SharePoint Advanced Management](advanced-management.md)

## View recent actions of a site

1. In the SharePoint admin center, expand **Sites** and select **Active sites**.
2. Select **Your recent actions**. The recent actions panel appears on the right and lists your most recent 30 actions made within the last 30 days.
3. Select **Export** to download the list as a .csv file.
4. Select **View site details** to open the site info panel. From here, you can make changes to site properties like site name, site address, hub association and aliases.

:::image type="content" source="media/Exported_CSV.png" alt-text="Screenshot of .csv file of recent admin actions":::

> [!NOTE]
>If you close the browser while actions are in-progress, they will not be recorded in the panel or .csv file. Failed actions are recorded in the panel, but are removed once you exit the current session. The export .csv file will not contain failed actions.

## Bulk site edits

Here’s an example of how bulk edits are grouped as one action in the recent actions panel:

You deleted 4 SharePoint sites on May 21 at 12:10 AM. The bulk edit will show as one item named Deleted 4 sites on the recent actions panel. Select the Deleted 4 sites action and the list of deleted SharePoint sites will appear.

:::image type="content" source="media/RAC_panel_bulk_edit_successful_and_failed_actions.png" alt-text="screenshot of recent actions panel with successful and failed actions":::

:::image type="content" source="media/RAC_panel_bulk_edit_delete_sites_selected_4_sites_expanded.png" alt-text="screenshot of recent actions panel with bulk edit action expanded to show sites affected":::

## Related articles

[Microsoft Syntex Advanced Management overview](advanced-management.md)
