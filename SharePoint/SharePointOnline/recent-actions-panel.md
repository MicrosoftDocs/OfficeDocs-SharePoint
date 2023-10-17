---
ms.date: 10/11/2023
title: "Review recent SharePoint administrator site actions"
ms.reviewer: daminasy
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
- M365-sam
- Highpri
- Tier1
description: "Learn how to review recent admin actions in SharePoint admin center."
---
# Review recent SharePoint administrator site actions

[!INCLUDE[Advanced Management](includes/advanced-management.md)]

With the recent actions panel, administrators can make changes to SharePoint site properties and review their most recent actions in the [SharePoint admin center](/sharepoint/get-started-new-admin-center).

Changes to site properties like site name, site deletion and storage quota show as recent actions.

The recent actions panel only shows the changes you make to site properties. Changes made by other administrators and organization-level changes don't show in the panel.

:::image type="content" source="media/RAC_panel.png" alt-text="Screenshot of Recent admin actions panel":::

> [!NOTE]
> Recent actions panel is not available for global readers. [GDAP administrators](/partner-center/gdap-introduction) won't be able to see the previous and current values of the administrator actions.

## Requirements

The following features require [Microsoft Syntex - SharePoint Advanced Management](advanced-management.md)

- Review the last 30 actions made within the last 30 days in the recent actions panel.
- View more details such as previous and current value of the settings changed and directly access the site details panel to review the change.
- Export and download a. csv file detailing all the changes made within the last 30 days.

> [!IMPORTANT]
> Without Microsoft Syntex - SharePoint Advanced Management, you can only view actions made in the current session. Once you close the browser or sign out, the recent actions panel will clear the history.

## View recent actions of a site

1. In the SharePoint admin center, expand **Sites** and select **Active sites**.
2. Select **Your recent actions**. The recent actions panel appears and lists your most recent 30 actions made within the last 30 days.
3. Select **Export** to download the list as a .csv file.
4. Select **View site details** to open the site info panel. From here, you can make changes to site properties like site name, site address, hub association and aliases.

:::image type="content" source="media/Exported_CSV.png" alt-text="Screenshot of .csv file of recent admin actions":::

> [!NOTE]
>If you close the browser while actions are in-progress, they will not be recorded in the panel or .csv file. Failed actions are recorded in the panel, but are removed once you exit the current session. The export .csv file will not contain failed actions.

## Bulk site edits

Here's an example of how bulk edits are grouped as one action in the recent actions panel:

You deleted 4 SharePoint sites on May 21 at 12:10 AM. The bulk edit shows as one item named Deleted 4 sites on the recent actions panel. Select the Deleted 4 sites action and the list of deleted SharePoint sites appear.

:::image type="content" source="media/RAC_panel_bulk_edit_successful_and_failed_actions.png" alt-text="screenshot of recent actions panel with successful and failed actions":::

:::image type="content" source="media/RAC_panel_bulk_edit_delete_sites_selected_4_sites_expanded.png" alt-text="screenshot of recent actions panel with bulk edit action expanded to show sites affected":::

## Related articles

[Microsoft Syntex Advanced Management overview](advanced-management.md)
