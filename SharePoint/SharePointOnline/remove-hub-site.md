---
title: "Remove a hub site"
ms.author: kaarins
author: kaarins
manager: pamgreen
ms.audience: Admin
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
search.appverid:
- SPO160
- MET150
ms.assetid: 8b1f8b6b-09c6-41c9-b1ca-88cbeee86ba2
description: "Learn how to make a hub site no longer a hub site (unregister it as a hub site)"
---

# Unregister a site as a hub site

If you're a global or SharePoint admin in Office 365, you can make a hub site no longer a hub site (unregister it as a hub site). Make sure you do this before you delete the hub site. When you demote a hub site, any sites still associated with the hub site will be disassociated the next time a user accesses them.

## Unregister a hub site in the new SharePoint admin center

> [!NOTE]
>  Some functionality is introduced gradually to organizations that have opted in to the [Targeted release option in Office 365](/office365/admin/manage/release-options-in-office-365). This means that you may not yet see some features described in this article.

1. In the new SharePoint admin center, under **Sites**, click **Active sites**.

2. Select the site, click **Hub site**, and then click **Unregister as hub site**.

3. Click **OK**. 

## Unregister a hub site by using PowerShell
  
1. Download and install the latest [SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251). If you already have a previous version installed, uninstall it first and then install the latest version.
    
2. Connect the SharePoint Online Management Shell to SharePoint Online for your organization. For info, see [Connect the SharePoint Online PowerShell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).
    
3. Run the following command:
    
  ```PowerShell
  Unregister-SPOHubSite URL
  ```

   (Where  *URL*  is the URL of the site.) 
    

