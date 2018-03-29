---
title: "Manage administrators for a site collection"
ms.author: kaarins
author: kaarins
manager: pamgreen
ms.date: 9/11/2017
ms.audience: Admin
ms.topic: article
ms.service: o365-administration
localization_priority: Normal
ms.collection: Strat_SP_admin
ms.assetid: 9a7e46f9-3fc4-4297-955a-82cb292a5be0
description: "Learn how to add and remove site collection admins."
---

# Manage administrators for a site collection

This article describes how site collection admins can add and remove other site collection admins. It also describes how global admins and SharePoint admins can add and remove admins on any site collections.
  
- A **global administrator** in Office 365 includes all the permissions of a SharePoint admin. A **SharePoint administrator** can create and manage site collections, designate site collection admins, change organization-wide SharePoint settings, and more. 
    
-  A **site collection administrator** has permission to manage a site collection. A site collection can have several admins, but only one primary admin. When SharePoint admins create site collections, they specify the primary site collection administrator and can add other admins as backups. Site collection admins don't have access to the SharePoint Online admin center. 
    
> [!NOTE]
> A **term store administrator** can add or change terms in the term store (a directory of common terms you want to use across your organization). To learn more, see [Assign roles and permissions to manage term sets](https://support.office.com/article/951216b9-81ac-4850-9ea0-7ad4c45eb231). 
  
## Add or remove site collection admins (as a site collection admin)
<a name="__toc341786266"> </a>

Follow these steps to add or remove other site collection admins from Site Settings.
  
1. Go to the site.
    
2. Click **Settings**![Gear shaped settings button](../media/96dc60c0-3b6b-4dd7-b246-7d1750653462.png) and then **Site Settings**.
    
     ![Choose Settings, Site Settings](../media/475ae6dd-1b16-4a13-a6d3-37c41ff05a24.png)
  
3. Under **Users and Permissions** click **Site collection administrators**.
    
     ![Site collection administrators highlighted under users and permissions](../media/a1b732b1-a641-45a8-8088-29a1de50c0e8.PNG)
  
4. Add or remove names in the Site Collection Administrators box, and then click **OK**.
    
## Add or remove site collection admins (as a global admin or SharePoint admin)
<a name="__toc341786265"> </a>

Before you manage administrators for site collections, make sure you have a plan for your site collections and their permissions. For info about this, see [Manage site collections and global settings in the SharePoint admin center](manage-site-collections-and-global-settings-in-the-sharepoint-admin-center). If you're a global admin and want info about assigning other users the SharePoint admin role in Office 365, see [Assigning admin permissions](https://support.office.com/article/F44FBE43-7E11-475B-A1B2-3F00719A853A).
  
Follow these steps to add or remove site collection admins by using the SharePoint admin center:
  
1. [Sign in to Office 365](e9eb7d51-5430-4929-91ab-6157c5a050b4) as a global admin or SharePoint admin. 
    
2. Select the app launcher icon ![The icon that looks like a waffle and represents a button click that will reveal multiple application tiles for selection.](../media/3b8a317e-13ba-4bd4-864e-1ccd47af39ee.png) in the upper-left and choose **Admin** to open the Office 365 admin center. (If you don't see the Admin tile, you don't have Office 365 administrator permissions in your organization.) 
    
3. In the left pane, choose **Admin centers** > **SharePoint**.
    
4. Point to the site collection for which you want to change the administrators, and then select the check box in front of it. 
    
     ![SPO Selecting a collection from within the site collection list](../media/6e5db026-befa-46b7-9e05-77c022919c88.PNG)
  
5. Click **Owners**, and then click **Manage Administrators**.
    
     ![SPO Site administrator owners button with Manage Administrators highlighted.](../media/45326c50-d66f-44e7-b5f3-65ff85ca18f7.PNG)
  
6. Change the name in the **Primary Site Collection Administrator** box, or add or remove names in the **Site Collection Administrators** box. 
    
     ![Site administrator dialog box.](../media/488ca762-cbe2-458c-8e21-7f640471a565.PNG)
  
7. Click **Check Names**![Check Names button](../media/bfa3e094-27e7-4ded-b5b9-de97518f6375.png) to verify that the user names are valid. 
    
8. Click **OK** **.**
    

