---
title: "Change site collection version and upgrade settings"
ms.reviewer: 
ms.author: kaarins
author: kaarins
manager: pamgreen
ms.date: 6/29/2018
audience: Admin
ms.topic: get-started-article
ms.service: sharepoint-online
localization_priority: Normal
ms.collection:  
- Strat_SP_admin
- M365-collaboration
search.appverid:
- SPO160
- MET150
ms.assetid: bff957b8-6c29-4578-ada8-9e5d42c04489
description: "This article describes how to configure which version of SharePoint is used when creating a site collection and whether or not the site collection can be upgraded to a new version of SharePoint."
---

# Change site collection version and upgrade settings

When Office 365 updates become available, global and SharePoint admins in Office 365 are the first to hear about them. SharePoint Online has a hierarchical structure, so updates are delivered in a cascading way. Updates start at the organization level and then flow down to site collections and sites. 
  
You, as a global or SharePoint admin, determine who is allowed to upgrade site collections and can restrict upgrade permissions to a select group, or delegate upgrade responsibilities to site collection admins. Each method has its benefits. 
  
Limit upgrade options when you want to arrange a coordinated rollout of new features, or you have highly customized sites that need thorough testing before being upgraded. You can also delegate upgrade tasks when you have numerous site collections within your subscription. If, for example, you have team sites, personal sites, publishing sites, and project sites, delegation spreads the work around and enables site collection admins to determine when the time is right to implement the upgrades for their individual sites.
  
## About site collection versions

If you're rolling out an upgrade, you don't want it to affect workday tasks or prevent users from creating sites when and where they need them. With versions, you can update your subscription to the new environment but allow your users to continue creating sites that look and feel like the old version. 

You can choose whether to allow versions in your subscription and decide how users can upgrade their own site collections. The classic SharePoint admin center lets you choose from the following version options.
  
|
|
|**Option**|**Description**|
|Allow creation of old version site collections, but prevent creation of new version site collections. Prevent opt-in upgrade to the new version site collections.  <br/> |Tightly control the upgrade process and prevent users from using the new features until a later time.  <br/> |
|Allow creation of old version site collections and creation of new version site collections. Allow opt-in upgrade to the new version site collections.  <br/> |Give users the choice of what version they want in the newly upgraded environment.  <br/> |
|Prevent creation of old version site collections, but allow creation of new version site collections. Allow opt-in upgrade to the new version site collections. (This is the default choice.)  <br/> | Control the upgrade process so users can't use the old site collection features.  <br/> |
   
 **To configure version and upgrade settings for all site collections**
  
1. Sign in to https://admin.microsoft.com as a global or SharePoint admin. (If you see a message that you don't have permission to access the page, you don't have Office 365 administrator permissions in your organization.)
    
    > [!NOTE]
    > If you have Office 365 Germany, sign in at https://portal.office.de. If you have Office 365 operated by 21Vianet (China), sign in at https://login.partner.microsoftonline.cn/. Then select the Admin tile to open the admin center.  
    
2. In the left pane, under **Admin centers**, select **SharePoint**. (You might need to select **Show all** to see the list of admin centers.) If this opens the new SharePoint admin center, select **Classic SharePoint admin center** in the left pane.
    
3. Choose **settings**.
    
4. In **Global Experience Version Settings**, select the desired option.
    
5. Select **OK**.
    
    > [!NOTE]
    > Options appear dimmed (unavailable) if this is a new subscription or if the root (organization) level of an existing subscription hasn't been upgraded yet. 
  
 **To enable or disable upgrades on select site collections**
  
1. Sign in to https://admin.microsoft.com as a global or SharePoint admin. (If you see a message that you don't have permission to access the page, you don't have Office 365 administrator permissions in your organization.)
    
    > [!NOTE]
    > If you have Office 365 Germany, sign in at https://portal.office.de. If you have Office 365 operated by 21Vianet (China), sign in at https://login.partner.microsoftonline.cn/. Then select the Admin tile to open the admin center.  
    
2. In the left pane, under **Admin centers**, select **SharePoint**. (You might need to select **Show all** to see the list of admin centers.) If this opens the new SharePoint admin center, select **Classic SharePoint admin center** in the left pane.
    
3. Select **site collections** in the left pane, and select the site you want. 
    
4. On the ribbon, select **Upgrade** \> **Site collection upgrade settings**. 
    
5. For **Allow Upgrade**, choose **Yes** or **No**.
    
6. Select **Save**.
    
## See also

[Manage site collections and global settings in the SharePoint admin center](planning-guide.md)

