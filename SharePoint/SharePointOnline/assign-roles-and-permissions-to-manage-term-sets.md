---
title: "Assign roles and permissions to manage term sets"
ms.reviewer: vrchowdh
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
audience: End User
f1.keywords: NOCSH
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
ms.collection:  
- M365-collaboration
search.appverid:
- SPO160
- OSU150
- MET150
ms.assetid: 951216b9-81ac-4850-9ea0-7ad4c45eb231
description: "Learn about the roles for managing metadata term sets on a SharePoint site, and how to assign people to those roles"
---

# Assign roles and permissions to manage term sets

The tasks that you can do in the term store are determined by the specific role that you're assigned. 

To be able to create or change a term, you must have one of three specific roles: term store admin, group manager, or contributor. 
  
A term store admin can do these tasks:
  
- Create or delete term set groups.
    
- Add or remove group managers or contributors, or other term store admins
    
- Change the working languages for the term store.
    
- Any task that a group manager or contributor can do.

When you set up a term set, you can designate a group or a person as an Owner, Contact, or Stakeholders for the term set. These labels do not grant any specific permission to work with the term set. Instead, they provide a useful way to track the business owners or stakeholders for a term set. 

## Add term store admins
  
1. In the SharePoint admin center, under **Content services**, click **Term store**.
    
2. In the tree view pane on the left, select the taxonomy.
    
3. In the **Term store** page, for **Admins**, select **Edit**. The **Edit term store admin** panel appears. Enter the names or email addresses of the people who you want to add as term store admins. Select **Save**.
    
## Add group managers
<a name="__toc332890716"> </a>

A group manager can do these tasks:
  
- Add or remove contributors.
    
- Any task that a contributor can do.
    
> [!IMPORTANT]
>  You must be a term store admin to add new Group Managers. 
  
To add a group manager:
  
1. In the SharePoint admin center, under **Content services**, click **Term store**.

2. In the tree view pane on the left, select the Group for which you want to add a Group Manager. 
    
3. From the **People** page, select **Edit**. The **Edit name and description** panel appears. Add a term group name and description to help users understand the purpose of this term group. Select **Save**.

4.  For **Group Managers**, to add people who can create new term groups, set and assign users to the group manager and contributor role, select **Edit**. The **Edit admins** panel appears. Enter the names or email addresses of the people who you want to add as Group Managers. Select **Save**.
    
    
## Add contributors
<a name="__toc332890717"> </a>

A contributor can create or change a term set.
  
You must be either a term store admin or a group manager of a specific group to add contributors to that group.
  
1. In the SharePoint admin center, under **Content services**, click **Term store**.

2. In the tree view pane on the left, select the Group to which you want to add a Contributor. 
    
3. For **Contributors**, set and assign users to the group manager and contributor role, select **Edit**. The **Edit contributors** panel appears. Enter the names or email addresses of the people who you want to add as Contributors. Select **Save**. 

## Metadata tasks that site users can perform
<a name="__toc332890714"> </a>

Site users who do not have an assigned role in the term store can use terms and terms sets in other ways. 
  
Site members can do the following tasks with managed metadata: 
  
- Update values in managed metadata columns (if terms sets associated with the columns are open and if the column lets fill-in choices).
    
- Add new terms to a term set when they update the value for a managed metadata column.
    
- Create new enterprise keywords when they update the enterprise keywords column for a list or library.
    
- Use metadata navigation in lists or libraries to filter the display of items.
    
- Use managed terms or enterprise keywords in search queries, and then refine search results based on these terms.
    
In addition, site users who have appropriate permissions (such as site owners) can create new managed metadata columns for lists, libraries, or content types. When site users create these columns, they can create new term sets that apply only to the site (previously called "site collection"), and they can manage the terms within these term sets. 
  
