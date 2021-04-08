---
title: "What is permissions inheritance?"
ms.reviewer: srice
ms.author: mikeplum
author: MikePlumleyMSFT
manager: serdars
recommendations: true
audience: Admin
ROBOTS: NOINDEX
f1.keywords:
- NOCSH
ms.topic: reference
ms.service: sharepoint-online
localization_priority: Normal
search.appverid:
- MET150
ms.assetid: 06bb1ed1-d150-42f4-9600-fb261d4b590c
description: "What is permissions inheritance in SharePoint."
---

# Permissions inheritance in SharePoint

While SharePoint allows considerable customization of site permissions, including changing inheritance, we highly recommend not breaking inheritance. Use the built-in SharePoint groups for communication sites and manage team site permissions through the associated Microsoft 365 group. Use sharing links to share individual files and folders with people outside the site. This allows for much easier administration. For information about managing permissions in the SharePoint modern experience,see [Sharing and permissions in the SharePoint modern experience](modern-experience-sharing-permissions.md).

## What is permissions inheritance?

Permissions inheritance means that the permission settings of an element in a site collection are passed on to the children of that element. In this way, sites inherit permissions from the top-level ("root") site of the site collection, libraries inherit from the site that contains the library, and so on. Permission inheritance enables you to make a permission assignment once, and have that permission apply to all sites, lists, libraries, folders and items that inherit permissions. This behavior can reduce complexity and the amount of time site collection administrators and site owners spend on security management.
  
By default, SharePoint sites inherit permissions from a parent site. This means that when you assign a user to the Members group, the user's permissions automatically cascade down through all the sites, lists, libraries, folders and items that inherit the permission level.
  
## What is a parent in SharePoint permissions?
<a name="__toc340139789"> </a>

The term parent, when used in SharePoint permissions, is just a way to emphasize inheritance. The parent passes down its permission settings to all its children. By default, the root site of a site collection is the first parent for all the sites and other objects that are below it in the site hierarchy.
  
The root site of a site collection is not the only parent. Every securable object (sites, libraries, lists, and so on) in a site collection can be a parent. That is, the root site is the parent of its subsites, each site is the parent of its libraries and lists, and each list is the parent of the list items in it. In this terminology, an object with a parent is known as a child. So, a subsite is the child of its parent site, a list item is the child of its list parent, and so on.

> [!IMPORTANT]
> We recommend creating a site collection for each unit of work instead of using subsites create a hierarchical structure. [Learn about using hub sites to organize your intranet](planning-hub-sites.md) 
  
By default, permissions are inherited from parent to child. That is, if you do not change the permission structure, then a list item inherits permissions (through its parent list) from the root site in the collection. However, even if you break inheritance for a list, that list is still a parent for its own list items. The list items for the list inherit the permissions that the list has, and if you change the permissions for the list, the list items inherit the changes.
  
When you first break this chain of inheritance from parent to child, the child starts with a copy of the parent's permissions. Then, you edit these permissions to make them the way that you want. You can add permissions, remove permissions, create special groups, and so on. None of the changes affect the original parent. And, if you decide that breaking inheritance was the wrong decision, you can resume inheriting permissions at any time.

When a user shares or stops sharing an item that contains other items with broken inheritance, a one-time push down of that permission addition or removal is sent to all child items, even those with broken inheritance. This is true for both direct permissions and sharing links. When managing permissions for an item with broken inheritance, users are able to remove any direct permissions on it. If an item with broken inheritance is accessible by a sharing link that was created on one of its parent folders and a user does not want that link to grant access to the item, then users can either remove the link entirely or they can move the file outside of the folder for which sharing link has permissions.
  
## More about permissions inheritance
<a name="__toc340139790"> </a>

Permission inheritance enables an administrator to assign permission levels at one time, and have the permissions apply throughout the site collection. Permissions pass from parent to child throughout the SharePoint hierarchy, from the top level of a site to the bottom. Permission inheritance can save time for site administrators, especially on large or complex site collections.
  
However, some scenarios have different requirements. In one scenario, you might have to restrict access to a site because it contains sensitive information that you must protect. In a different scenario, you might want to expand access and invite others to share information. If you want, you can break the inheritance behavior (stop inheriting permissions) at any level in the hierarchy.
  
Let's look at examples of these different scenarios.
  
Suppose that you have a company called Northwind Traders. You create a communication site called "Benefits" with the URL northwindtraders.sharepoint.com/sites/benefits. At the site collection root, you set up SharePoint groups, assign permission levels, and add users to the groups.
  
Suppose then that you create subsites for the "Benefits" site, such as "Health care" (northwindtraders.sharepoint.com/sites/benefits/healthcare) and "Retirement" (northwindtraders.sharepoint.com/sites/benefits/retirement). These subsites could even contain more subsites. For example, the "Health care" subsite could have a "Dental" subsite (northwindtraders.sharepoint.com/sites/benefits/healthcare/dental).
  
### A scenario that uses default behavior
<a name="__toc340139791"> </a>

By default, permissions pass directly to subsites. That is, the groups and permission levels that you assigned at the site collection root pass down automatically to the subsite for reuse.
  
### A scenario that restricts access to a site and its children
<a name="__toc340139792"> </a>

Suppose that your company offers special benefits only for executives. In this case, the administrators decide to separate the "Executive" subsite and break inheritance from the parent site, "Benefits."
  
The site owners for the "Executive" site change the permissions for the site, removing some groups and creating others. The subsites of the "Executive" site, "Bonuses" and "Company transportation," now inherit permissions only from the "Executive" subsite. Only the groups and users for "Executive" can access the lists and libraries that contain sensitive information.
  
For ease of maintenance, we recommend that you use a similar method to restrict access. That is, organize your site so that sensitive material is in the same place. If you organize the site this way, you only have to break inheritance one time, for that specific site or library. This is much less overhead. It requires much less work than creating separate permission structures in many locations for individual subsites and libraries.
  
### A scenario that shares access to a folder and its children
<a name="__toc340139793"> </a>

Suppose that an employee at Northwind Traders hired consultants and wants to collaborate with them on documents in SharePoint. The employee doesn't want to give the consultants access to anything else on the SharePoint site.
  
When the employee shares the folder with the consultants, SharePoint automatically handles all the details of permissions and access, by breaking inheritance on the folder itself. The consultants can access all the documents in the folder but can't view or access any other information on the site. Even though inheritance is technically broken, if people are later added to the parent site collection, they will automatically be given permission to the shared folder.
  

