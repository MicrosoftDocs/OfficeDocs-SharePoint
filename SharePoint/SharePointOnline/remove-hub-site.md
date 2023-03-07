---
ms.date: 07/11/2018
title: "Remove a hub site"
ms.reviewer: metorres
ms.author: mikeplum
author: MikePlumleyMSFT
manager: serdars
recommendations: true
audience: Admin
f1.keywords:
- CSH
ms.topic: article
ms.service: sharepoint-online
ms.localizationpriority: medium
ms.collection:  
- Strat_SP_admin
- M365-collaboration
ms.custom:
- seo-marvel-apr2020
- admindeeplinkSPO
search.appverid:
- SPO160
- MET150
ms.assetid: 8b1f8b6b-09c6-41c9-b1ca-88cbeee86ba2
description: "In this article, you'll learn about how to remove (un-register) a hub site so that it no longer remains a hub site."
---

# Unregister a site as a hub site

If you're a Global Administrator or SharePoint Administrator in Microsoft 365, you can make a hub site no longer a hub site (unregister it as a hub site). Make sure you do this before you delete the hub site. When you unregister a hub site, the associated sites will not automatically disassociate from the hub site. Disassociating a site will remove the hub site navigation bar from the top of the site. The look that the site inherited from the hub site will stay the same and features such as additional navigation links, applications, or custom lists with specific columns that were added as part of the inherited hub site design will remain. Any hub-site-related web parts added to the home page will only show information from the site instead of from sites associated with the hub.
  
## Unregister a hub site in the new SharePoint admin center 

1. Go to <a href="https://go.microsoft.com/fwlink/?linkid=2185220" target="_blank">**Active sites** in the SharePoint admin center</a>, and sign in with an account that has [admin permissions](./sharepoint-admin-role.md) for your organization.

>[!NOTE]
>If you have Office 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the Active sites page.

2. Select the site, select **Hub** on the command bar, and then select **Unregister as hub site**.

    ![Unregistering a hub site](media/unregister-hub-site.png)

3. Select **OK**.  

## Related topics

To learn how to use Microsoft PowerShell to manage and delete hub sites, see [Manage SharePoint hub sites](/sharepoint/dev/features/hub-site/hub-site-powershell).

