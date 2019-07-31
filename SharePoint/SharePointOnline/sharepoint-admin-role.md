---
title: "About the SharePoint admin role in Microsoft 365"
ms.author: kaarins
author: kaarins
manager: pamgreen
audience: Admin
ms.topic: overview
ms.service: sharepoint-online
localization_priority: Normal
ms.custom: Adm_O365
ms.collection:  
- Strat_SP_admin
- M365-collaboration
search.appverid:
- SPO160
- MOE150
- GEA150
- BSA160
- BCS160
- GSP150
- MET150
ms.assetid: f08144d5-9d50-4922-8e77-4e1a27b40705
description: "SharePoint admins manage your document storage. They also assign site collection administrators and Term Store Administrators.  "
---

# About the SharePoint admin role in Microsoft 365

Global administrators in Microsoft 365 can assign users the SharePoint administrator role for help with administering SharePoint Online. The global admin already has all the permissions of a SharePoint admin. When you purchase a Microsoft 365 or Office 365 subscription, a team site is automatically created, and the global admin is set as the primary site collection administrator. For info about assigning a user the SharePoint administrator role, see [Assign admin roles in Office 365 for business](/office365/admin/add-users/assign-admin-roles).

> [!TIP]
> When you assign someone the SharePoint admin role, you may also want to assign them to Service administrator role. This way they can see important information in the Microsoft 365 admin center, such as the health of the SharePoint Online service, and change and release notifications. 

   ![Manage admin roles in the Microsoft 365 admin center](media/sharepoint-admin-role.png)
  
Users assigned the SharePoint admin role have access to the SharePoint admin center and can create and manage site collections, designate site collection administrators, manage user profiles, and more. 

> [!IMPORTANT]
> SharePoint admins can now manage Office 365 groups, including creating, deleting, and restoring groups, and changing group owners.

Global admins and SharePoint admins don't have automatic access to all sites and each user's OneDrive, but they can give themselves access to any site or OneDrive. They can also use Microsoft PowerShell to manage SharePoint and OneDrive. See more about this role's [Key tasks of the SharePoint administrator](sharepoint-admin-role.md#BK_KeyTasks) below. 
  
Site admins are users that have permission to manage sites (previously called "site collections"), including the site root and any subsites. They don't need to have an admin role in Microsoft 365, and don't have access to the SharePoint admin center. A site can have several site administrators, but must have one and only one primary administrator. 
  
> [!NOTE]
> Global admins, SharePoint admins, and site collection admins all need to be assigned a SharePoint Online license. <br>There is a separate role within SharePoint called the **Term Store Administrator**. Users assigned this role can add or change terms in the term store (a directory of common terms you want to use across your organization). To learn more, see [Assign roles and permissions to manage term sets](assign-roles-and-permissions-to-manage-term-sets.md). 
  
## Key tasks of the SharePoint administrator
<a name="BK_KeyTasks"> </a>

Here are some of the key tasks users can do when they are assigned to the SharePoint admin role: 
  
- [Create sites](create-site-collection.md)
    
- [Delete sites](delete-site-collection.md)
    
- [Manage site collections and global settings](planning-guide.md)
    
- [Turn external sharing on or off for SharePoint Online](turn-external-sharing-on-or-off.md)
    
- [Add and remove site admins](manage-site-collection-administrators.md)
    
- [Manage site collection storage limits](manage-site-collection-storage-limits.md)
    
- [Manage SharePoint Online user profiles](manage-user-profiles.md)
    
  
## See also
<a name="BK_KeyTasks"> </a>

[About Office 365 admin roles](/office365/admin/add-users/about-admin-roles)
  
[Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online)

