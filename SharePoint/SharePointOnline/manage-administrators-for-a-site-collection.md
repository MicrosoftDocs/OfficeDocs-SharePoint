---
title: "Manage administrators for a site collection"
ms.author: kaarins
author: kaarins
manager: pamgreen
ms.date: 4/17/2018
ms.audience: Admin
ms.topic: article
ms.service: o365-administration
localization_priority: Normal
ms.collection: Strat_SP_admin
search.appverid:
- SPO160
- GSA150
- BSA160
- GSP150
ms.assetid: 9a7e46f9-3fc4-4297-955a-82cb292a5be0
description: "Learn how to add and remove site collection admins."
---

# Manage administrators for a site collection

This article describes how global admins and SharePoint admins in Office 365 can add and remove site collection admins for any site collection. If you're an owner of a communication site, or a site that belongs to an Office 365 group, see [Manage your SharePoint site settings](https://support.office.com/article/8376034d-d0c7-446e-9178-6ab51c58df42#__BKMKMngSitePermissions) for info about giving people access to your site. If you're a site collection admin for a classic site, see [Manage your SharePoint site settings](https://support.office.com/article/8376034d-d0c7-446e-9178-6ab51c58df42#id0eaabaaa=server). 
  
> [!NOTE]
> If you're a global admin and want info about assigning other users the SharePoint admin role in Office 365, see [Assigning admin permissions](https://support.office.com/article/F44FBE43-7E11-475B-A1B2-3F00719A853A). 
  
## Add or remove site collection admins
<a name="__toc341786265"> </a>

If a site belongs to an Office 365 group, you can add or remove group members in the Office 365 admin center. For info, see [Add or remove members from Office 365 groups using the Office 365 admin center](https://support.office.com/article/e186d224-a324-4afa-8300-0e4fc0c3000a). 
  
If you want to change the admins for a communication site or a site that belongs to an Office 365 group, and you as the global or SharePoint admin are also an owner of the site, see [Manage your SharePoint site settings](https://support.office.com/article/8376034d-d0c7-446e-9178-6ab51c58df42#__BKMKMngSitePermissions). If you aren't a site owner, you need to use PowerShell to add or remove site owners. For info, see [Add-PnPSiteCollectionAdmin](https://go.microsoft.com/fwlink/?linkid=872301) and [Remove-PnPSiteCollectionAdmin](https://go.microsoft.com/fwlink/?linkid=872302).
  
To add or remove site collection admins on classic sites, use the SharePoint admin center:
  
1. Sign in to Office 365 as a global admin or SharePoint admin.
    
2. Select the app launcher icon ![The icon that looks like a waffle and represents a button click that will reveal multiple application tiles for selection.](media/3b8a317e-13ba-4bd4-864e-1ccd47af39ee.png) in the upper-left and choose **Admin** to open the Office 365 admin center. (If you don't see the Admin tile, you don't have Office 365 administrator permissions in your organization.) 
    
3. In the left pane, choose **Admin centers** > **SharePoint**.
    
4. Point to the site collection for which you want to change the administrators, and then select the check box in front of it. 
    ![SPO Selecting a collection from within the site collection list](media/6e5db026-befa-46b7-9e05-77c022919c88.PNG)
  
5. Click **Owners**, and then click **Manage Administrators**.
    ![SPO Site administrator owners button with Manage Administrators highlighted.](media/45326c50-d66f-44e7-b5f3-65ff85ca18f7.PNG)
  
6. Change the name in the **Primary Site Collection Administrator** box, or add or remove names in the **Site Collection Administrators** box. 
    ![Site administrator dialog box.](media/488ca762-cbe2-458c-8e21-7f640471a565.PNG)
  
7. Click **Check Names**![Check Names button](media/bfa3e094-27e7-4ded-b5b9-de97518f6375.png) to verify that the user names are valid. 
    
8. Click **OK** **.**
    

