---
title: "Change site collection version and upgrade settings"
ms.reviewer: 
ms.author: kaarins
author: kaarins
manager: pamgreen
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

When Office 365 updates become available, global and SharePoint admins in Office 365 are the first to hear about them. SharePoint has a hierarchical structure, so updates are delivered in a cascading way. Updates start at the organization level and then flow down to site collections and sites.
  
You, as a global or SharePoint admin, determine who is allowed to upgrade site collections and can restrict upgrade permissions to a select group, or delegate upgrade responsibilities to site collection admins. Each method has its benefits.
  
Limit upgrade options when you want to arrange a coordinated rollout of new features, or you have highly customized sites that need thorough testing before being upgraded. You can also delegate upgrade tasks when you have numerous site collections within your subscription. If, for example, you have team sites, personal sites, publishing sites, and project sites, delegation spreads the work around and enables site collection admins to determine when the time is right to implement the upgrades for their individual sites.
  
## About site collection versions

If you're rolling out an upgrade, you don't want it to affect workday tasks or prevent users from creating sites when and where they need them. With versions, you can update your subscription to the new environment but allow your users to continue creating sites that look and feel like the old version.

You can choose whether to allow versions in your subscription and decide how users can upgrade their own site collections. The classic settings page lets you choose from the following version options.
  
|
|
|**Option**|**Description**|
|Allow creation of old version site collections, but prevent creation of new version site collections. Prevent opt-in upgrade to the new version site collections.  <br/> |Tightly control the upgrade process and prevent users from using the new features until a later time.  <br/> |
|Allow creation of old version site collections and creation of new version site collections. Allow opt-in upgrade to the new version site collections.  <br/> |Give users the choice of what version they want in the newly upgraded environment.  <br/> |
|Prevent creation of old version site collections, but allow creation of new version site collections. Allow opt-in upgrade to the new version site collections. (This is the default choice.)  <br/> | Control the upgrade process so users can't use the old site collection features.  <br/> |
   
 **To configure version and upgrade settings for all site collections**
  
1. Go to the [Settings page of the new SharePoint admin center](https://admin.microsoft.com/sharepoint?page=settings&modern=true) and sign in with an account that has admin permissions for your organization.

>[!Note]
>If you have Office 365 Germany, [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=848041), then browse to the SharePoint admin center and open the Sharing page. <br>If you have Office 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the Settings page.
    
2. Choose **classic settings page**.
    
3. In **Global Experience Version Settings**, select the desired option.
    
4. Select **OK**.
    
    > [!NOTE]
    > Options appear dimmed (unavailable) if this is a new subscription or if the root (organization) level of an existing subscription hasn't been upgraded yet. 
  
 **To enable or disable upgrades on select site collections**
  
1. Go to the [More features page of the new SharePoint admin center](https://admin.microsoft.com/sharepoint?page=classicfeatures&modern=true) and sign in with an account that has admin permissions for your organization.

>[!Note]
>If you have Office 365 Germany, [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=848041), then browse to the SharePoint admin center and open the Sharing page. <br>If you have Office 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the More features page.
 
2. Under **Classic site collections page**, select **Open**. 

3. Select the site collection.
    
4. On the ribbon, select **Upgrade notifications** \> **Site collection upgrade settings**. 
    
5. For **Allow Upgrade**, choose **Yes** or **No**.
    
6. Select **Save**.
    
## See also

[Manage site collections and global settings in the SharePoint admin center](planning-guide.md)
