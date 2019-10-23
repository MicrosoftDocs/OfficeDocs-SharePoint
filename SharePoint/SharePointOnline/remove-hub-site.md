---
title: "Remove a hub site"
ms.reviewer: metorres
ms.author: kaarins
author: kaarins
manager: pamgreen
audience: Admin
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
ms.collection:  
- Strat_SP_admin
- M365-collaboration
search.appverid:
- SPO160
- MET150
ms.assetid: 8b1f8b6b-09c6-41c9-b1ca-88cbeee86ba2
description: "Learn how to make a hub site no longer a hub site (unregister it as a hub site)"
---

# Unregister a site as a hub site

If you're a global or SharePoint admin in Office 365, you can make a hub site no longer a hub site (unregister it as a hub site). Make sure you do this before you delete the hub site. When you demote a hub site, any sites still associated with the hub site will be disassociated the next time a user accesses them.
  
## Unregister a hub site in the new SharePoint admin center 

1. Sign in to https://admin.microsoft.com as a global or SharePoint admin. (If you see a message that you don't have permission to access the page, you don't have Office 365 administrator permissions in your organization.)
    
    > [!NOTE]
    > If you have Office 365 Germany, sign in at https://portal.office.de. If you have Office 365 operated by 21Vianet (China), sign in at https://login.partner.microsoftonline.cn/. Then select the Admin tile to open the admin center.  

2. In the left pane, under **Admin centers**, select **SharePoint**. (You might need to select **Show all** to see the list of admin centers.) 

3. If the classic SharePoint admin center appears, select **Open it now** at the top of the page to open the new SharePoint admin center.
      
4. In the left pane of the new SharePoint admin center, select **Active sites**.

5. Select the site, select **Hub**, and then select **Unregister as hub site**. 

    ![Unregistering a hub site](media/unregister-hub-site.png)

6. Select **OK**.  

> [!NOTE]
> If a hub site has associated sites then you unregister it, it might take a while for the sites to be disassociated. If you re-register the hub site, the sites may remain associated.

## See also

To learn how to use Microsoft PowerShell to manage and delete hub sites, see [Manage SharePoint hub sites](/sharepoint/dev/features/hub-site/hub-site-powershell).

