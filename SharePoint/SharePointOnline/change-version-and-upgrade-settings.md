---
title: "Change site collection version and upgrade settings"
ms.author: kaarins
author: kaarins
manager: pamgreen
ms.date: 6/29/2018
ms.audience: Admin
ms.topic: get-started-article
ms.service: o365-administration
localization_priority: Normal
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
  
1. Sign in to Office 365 as a global admin or SharePoint admin.
    
2. Select the app launcher icon ![The app launcher icon in Office 365](media/e5aee650-c566-4100-aaad-4cc2355d909f.png) in the upper-left and choose **Admin** to open the Office 365 admin center. (If you don't see the Admin tile, you don't have Office 365 administrator permissions in your organization.) 
    
3. In the left pane, choose **Admin centers** \> **SharePoint**.
    
4. Choose **settings**.
    
5. In **Global Experience Version Settings**, select the desired option.
    
6. Select **OK**.
    
    > [!NOTE]
    > Options appear dimmed (unavailable) if this is a new subscription or if the root (tenant) level of an existing subscription hasn't been upgraded yet. 
  
 **To enable or disable upgrades on select site collections**
  
1. Sign in to Office 365 as a global admin or SharePoint admin.
    
2. Select the app launcher icon ![The app launcher icon in Office 365](media/e5aee650-c566-4100-aaad-4cc2355d909f.png) in the upper-left and choose **Admin** to open the Office 365 admin center. (If you don't see the Admin tile, you don't have Office 365 administrator permissions in your organization.) 
    
3. In the left pane, choose **Admin centers** \> **SharePoint**.
    
4. Go to **site collections** and select the one you want. 
    
5. On the ribbon, select **Upgrade** \> **Site collection upgrade settings**. 
    
6. For **Allow Upgrade**, choose **Yes** or **No**.
    
7. Select **Save**.
    
## See also

[Manage site collections and global settings in the SharePoint admin center](planning-guide.md)

