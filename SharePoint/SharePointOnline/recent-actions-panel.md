---
title: "Recent Actions Panel"
ms.reviewer: 
manager: serdars
recommendations: 
ms.author: mactra
author: its-mactra
ms.date: 10/10/2022
audience: Admin
f1.keywords:
- NOCSH 
ms.topic: conceptual
ms.service: sharepoint-online
ms.localizationpriority: 
ms.collection:  
search.appverid:
ms.assetid: TBD
description: "Monitor your changes in Recent Actions panel in SharePoint admin center
---
# Recent Actions Panel in SharePoint admin center

![green check mark](media/yes.png) **Requires SharePoint Advanced Management**

Track changes and make quick edits to your SharePoint site property settings with Recent Actions Panel in [SharePoint admin center](https://review.learn.microsoft.com/sharepoint/get-started-new-admin-center).

Recent Actions Panel lets you review the top 30 actions you made in SharePoint admin center in the last 30 days. Site property changes like site name, site creation and deletion, site URL, sharing settings, and storage quota are listed as actions in the panel. Note that changes made to tenant-level settings, and changes made by other admins are not shown in your Recent Actions Panel.

You can use Recent Actions Panel to conduct audits since it provides you with a list of actions made by yourself as a SharePoint admin. It also acts as the first step for investigations and resolving SharePoint site helpdesk tickets.

## View recent actions of a site

1. In the left column of the SharePoint admin center, select **Sites**.
2. Select **Active Sites**, and then select **Recent Actions**.
The Recent Actions Panel appears on the right and lists your top 30 actions made within 30 days. You can select **Export** to downloaded the list as a .CSV file.

You can see the previous and current values of site property changes when you click on an action in the Recent Actions Panel. This is helpful when you've made changes to a SharePoint site and forgot what the previous values were.

### Bulk site edits

Changes made to multiple sites at the same time and date will show as one action in the Recent Actions Panel. Select a bulk action item to see a list of which sites were changed.

For example, if you delete 4 SharePoint sites on May 21st at 6:15 PM, it will show as one item called Deleted 4 sites on the Recent Actions Panel.

In the .CSV file, bulk edit items are listed as separate line items. The bulk edit column of the report helps you quickly identify which actions were bulk edits.

## Make changes to a site from Recent Actions Panel

Select an action from the Recent Actions Panel, and then select **View Site Details** to open the Site Info Panel for a SharePoint site. You can make quick changes to the site property settings underneath the **General** tab.
