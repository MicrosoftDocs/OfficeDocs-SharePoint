---
ms.date: 08/02/2023
title: "About the SharePoint Administrator role in Microsoft 365"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: jtremper
recommendations: true
audience: Admin
f1.keywords:
- CSH
ms.topic: overview
ms.service: sharepoint-online
ms.localizationpriority: medium
ms.custom: 
- Adm_O365
- seo-marvel-apr2020
- admindeeplinkSPO
ms.collection:  
- Strat_SP_admin
- M365-collaboration
- m365initiative-spsitemanagement
- essentials-manage
search.appverid:
- SPO160
- MOE150
- GEA150
- BSA160
- BCS160
- GSP150
- MET150
ms.assetid: f08144d5-9d50-4922-8e77-4e1a27b40705
description: "Learn about the SharePoint Administrator role in Microsoft 365. SharePoint Administrators administer SharePoint and OneDrive in your organization."
---

# About the SharePoint Administrator role in Microsoft 365

Users assigned the SharePoint Administrator role have access to the <a href="https://go.microsoft.com/fwlink/?linkid=2185219" target="_blank">SharePoint admin center</a> and can create and manage sites, designate site admins, manage sharing settings, and manage Microsoft 365 groups, including creating, deleting, and restoring groups, and changing group owners.

Global Administrators in Microsoft 365 can assign users the SharePoint Administrator. The Global Administrator role already has all the permissions of the SharePoint Administrator role. 

For info about assigning a user the SharePoint administrator role, see [Assign admin roles in the Microsoft 365 admin center](/microsoft-365/admin/add-users/assign-admin-roles). If a user's role is changed so they gain or lose access to the SharePoint admin center, it takes about an hour for the change to take effect.

#### Site management

Global Administrators and SharePoint Administrators don't have automatic access to all sites and each user's OneDrive, but they can give themselves access to any site or OneDrive. They can also use Microsoft PowerShell to manage SharePoint and OneDrive. See more about this role's [Key tasks of the SharePoint admin](sharepoint-admin-role.md#BK_KeyTasks) below. 

Site admins have permission to manage sites, but they don't need to have an admin role in Microsoft 365, and don't have access to the SharePoint admin center.

For info about adding or removing a site admin, see [Manage site admins](manage-site-collection-administrators.md).

#### Term store administration

There is a separate role within SharePoint called the Term Store administrator. Users assigned to this role can add or change terms in the term store (a directory of common terms you want to use across your organization). To learn more, see [Assign roles and permissions to manage term sets](assign-roles-and-permissions-to-manage-term-sets.md).

#### API access

To manage API access in the SharePoint admin center, the application administrator role or the Global administrator role might be required. For more information, see [Manage access to Microsoft Entra ID-secured APIs](api-access.md).

## Key tasks of the SharePoint admin
<a name="BK_KeyTasks"> </a>

Here are some of the key tasks users can do when they are assigned to the SharePoint Administrator role: 
  
- [Create sites](create-site-collection.md)
    
- [Delete sites](delete-site-collection.md)
    
- [Manage sharing settings at the organization level](turn-external-sharing-on-or-off.md)
    
- [Add and remove site admins](manage-site-collection-administrators.md)
    
- [Manage site storage limits](manage-site-collection-storage-limits.md)

    
  
## Related topics
<a name="BK_KeyTasks"> </a>

[About Microsoft 365 admin roles](/office365/admin/add-users/about-admin-roles)
  
[Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online)
