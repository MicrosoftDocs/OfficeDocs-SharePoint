---
title: "Remove a hub site"
ms.reviewer: metorres
ms.author: kaarins
author: kaarins
manager: pamgreen
audience: Admin
f1.keywords:
- NOCSH
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

If you're a global or SharePoint admin in Microsoft 365, you can make a hub site no longer a hub site (unregister it as a hub site). Make sure you do this before you delete the hub site. When you unregister a hub site, any sites still associated with the hub will be disassociated the next time a user accesses them. Disassociating a site will remove the hub site navigation bar from the top of the site. The look that the site inherited from the hub site will stay the same and features such as additional navigation links, applications, or custom lists with specific columns that were added as part of the inherited hub site design will remain. Any hub-site-related web parts added to the home page will only show information from the site instead of from sites associated with the hub.
  
## Unregister a hub site in the new SharePoint admin center 

1. Go to the [Active sites page of the new SharePoint admin center](https://admin.microsoft.com/sharepoint?page=siteManagement&modern=true) and sign in with an account that has [admin permissions](/sharepoint/sharepoint-admin-role) for your organization.

>[!NOTE]
>If you have Microsoft 365 Germany, [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=848041), then browse to the SharePoint admin center and open the Active sites page. <br>If you have Microsoft 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the Active sites page.

2. Select the site, select **Hub**, and then select **Unregister as hub site**.

    ![Unregistering a hub site](media/unregister-hub-site.png)

3. Select **OK**.  

> [!NOTE]
> If a hub site has associated sites when you unregister it, it might take a while for the sites to be disassociated. If you re-register the hub site, the sites may remain associated.

## See also

To learn how to use Microsoft PowerShell to manage and delete hub sites, see [Manage SharePoint hub sites](/sharepoint/dev/features/hub-site/hub-site-powershell).
