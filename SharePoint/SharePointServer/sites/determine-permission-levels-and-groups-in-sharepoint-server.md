---
title: "Determine permission levels and groups in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 8/17/2017
audience: ITPro
ms.topic: concetpual
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 8409bf0e-3ddd-4837-b415-23255952f0bb

description: "Learn how to define the correct SharePoint Server permission levels at the site collection level."
---

# Determine permission levels and groups in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
A SharePoint group is a set of users that can be managed together. A permission level is a set of permissions that can be assigned to a specific group for a specific securable object. SharePoint groups and permission levels are defined at the site collection level and are inherited from the parent object by default. This article describes default groups and permission levels and helps you decide whether to use them as they are, customize them, or create different groups and permission levels. 
    
The most important decision about your site and content security in SharePoint Server is how to group your users and which permission levels to assign.
  
## Review available default groups
<a name="section1"> </a>

SharePoint groups enable you to manage sets of users instead of individual users. These groups can contain many individual users, or they can include the contents of any corporate identity system, including Active Directory Domain Services (AD DS), LDAPv3-based directories, application-specific databases and new user-centric identity models, such as Windows Live ID. SharePoint groups do not confer specific rights to the site; they are a way to designate a set of users. You can organize yours users into any number of groups, depending on the size and complexity of your organization or Web site. SharePoint groups cannot be nested.
  
The following table displays default groups that are created for team sites in SharePoint Server. Each default group is assigned a default permission level.
  
|**Group name**|**Default permission level**|**Description**|
|:-----|:-----|:-----|
|Visitors  <br/> |Read  <br/> |Use this group to grant people Read permissions to the SharePoint site.  <br/> |
|Members  <br/> |Edit  <br/> |Use this group to grant people Edit permissions to the SharePoint site.  <br/> |
|Owners  <br/> |Full Control  <br/> |Use this group to grant people Full Control permissions to the SharePoint site.  <br/> |
|Viewers  <br/> |View Only  <br/> |Use this group to grant people View Only permissions to the SharePoint site.  <br/> |
   
If you use a site template other than the team site template, you will see a different list of default SharePoint groups. For example, the following table shows the additional groups provided by a publishing site template.
  
|**Group name**|**Default permission level**|**Description**|
|:-----|:-----|:-----|
|Restricted Readers  <br/> |Restricted Read to the site, plus Limited Access to specific lists  <br/> |Members of this group can view pages and documents, but cannot view historical versions or review user rights information.  <br/> |
|Style Resource Readers  <br/> |Read to the Master Page Gallery and Restricted Read to the Style Library.  <br/> |Members of this group are given Read permission to the Master Page Gallery and Restricted Read permission to the Style Library. By default, all authenticated users are a member of this group.  <br/> > [!NOTE]> Do not remove all authenticated users from this group. Because Master Page Gallery and Style Library are shared across all sites in the site collection and must be accessible to all users of all sites. If you remove all authenticated users from the group, anyone with this permission level on a subsite will not be able to render the site. SharePoint will not automatically add or remove users of subsites to or from this group as needed.           |
|Designers  <br/> |Design, Limited Access  <br/> |Members of this group can to view, add, update, delete, approve, and customize the layout of site pages by using the browser or SharePoint Designer 2013.  <br/> |
|Approvers  <br/> |Approve, plus Limited Access  <br/> |Members of this group can edit and approve pages, list items, and documents.  <br/> |
|Hierarchy Managers  <br/> |Manage Hierarchy, plus Limited Access  <br/> |Members of this group can create sites, lists, list items, and documents.  <br/> |
   
> [!TIP]
> The Limited Access permission level is used to give groups access to a specific list, library, folder, document, or item, without giving them access to the entire site. Do not remove this permission level from the groups listed above. If this permission level is removed, the groups might not be able to navigate through the site to get the specific items with which they need to interact. 
  
Make most users members of the Visitors or Members groups. By default, users in the Members group can contribute to the site by adding or removing items or documents, but cannot change the structure, site settings, or appearance of the site. The Visitors group has read-only access to the site, which means that they can see pages and items, and open items and documents, but cannot add or remove pages, items, or documents.
  
If the default groups do not map to the exact user groups in your organization, you can create custom groups. 
  
Besides the above SharePoint groups, there are also administrator groups for higher-level administration tasks. They are Windows administrators, SharePoint farm administrators, and site collection administrators.
  
For more information, see [Choose administrators and owners for the administration hierarchy in SharePoint 2013](choose-administrators-and-owners-for-the-administration-hierarchy-in-sharepoint.md).
  
## Review available permission levels
<a name="section2"> </a>

The ability to view, change, or manage a site is determined by the permission level that you assign to a user or group. This permission level controls all permissions for the site and the child objects that inherit the site's permissions. Without the appropriate permission levels, the users might be unable to perform their tasks, or they could perform tasks that you did not want them to perform.
  
By default, the following permission levels are available:
  
- **View Only ** Includes permissions that enable users to view pages, list items, and documents. 
    
- **Limited Access ** Includes permissions that enable users to view specific lists, document libraries, list items, folders, or documents, without giving access to all the elements of a site. You cannot edit this permission level directly. 
    
    > [!NOTE]
    > If this permission level is removed, group members might be unable to navigate the site to access items, even if they have the appropriate permissions for an item within the site. 
  
- **Read ** Includes permissions that enable users to view items on the site pages. 
    
- **Edit ** Includes permissions that enable users to add, edit and delete lists; can view, add, update and delete list items and documents. 
    
- **Contribute ** Includes permissions that enable users to add or change items on the site pages or in lists and document libraries. 
    
- **Design ** Includes permissions that enable users to view, add, update, delete, approve, and customize the layout of site pages by using the browser or SharePoint Designer 2013. 
    
- **Full Control ** Includes all permissions. 
    
For more information about permissions that are included in the default permission levels, see [User permissions and permission levels in SharePoint 2013](user-permissions-and-permission-levels.md).
  
The following additional permission levels are provided with the publishing template by default:
  
- **Approve ** Includes permissions to edit and approve pages, list items, and documents. 
    
- **Manage Hierarchy ** Includes permissions to sites and edit pages, list items, and documents. 
    
- **Restricted Read ** Includes permissions to view pages and documents, but not historical versions or permissions information. 
    
## Determine whether you need custom permission levels or groups
<a name="section3"> </a>

The default groups and permission levels provide a general framework for permissions, covering many organization types and roles within those organizations. However, they might not map exactly to how the users are organized or to the many different tasks that the users perform on your sites. If the default groups and permission levels do not suit your organization, you can create custom groups, change the permissions included in specific permission levels, or create custom permission levels.
  
### Do you need custom groups?

The decision to create custom groups is fairly straightforward and has little effect on your site's security. You should create custom groups instead of using the default groups if either of the following situations applies:
  
- You have more (or fewer) user roles within your organization than are obvious in the default groups. For example, if in addition to Approvers, Designers, and Hierarchy Managers, you have a set of people who are tasked with publishing content to the site, you might want to create a Publishers group.
    
- There are well-known names for unique roles within your organization that perform very different tasks in the sites. For example, if you are creating a public site to sell your organization's products, you might want to create a Customers group that replaces Visitors or Viewers.
    
- You want to preserve a one-to-one relationship between Windows security groups and the SharePoint groups. For example, if your organization has a security group that is named Web Site Managers, you might want to use that name as a group name for easy identification when you manage the site.
    
- You prefer other group names.
    
### Do you need custom permission levels?

The decision to customize permission levels is less straightforward than the decision to customize SharePoint groups. If you customize the permissions assigned to a permission level, you must keep track of that change, verify that it works for all groups and sites affected by the change, and make sure that that the change does not adversely affect your security or your server capacity or performance.
  
For example, if you customize the Contribute permission level to include the Create Subsites permission that is typically part of the Full Control permission level, members of the Contributors group can create and own subsites, and can potentially invite malicious users to their subsites or post unapproved content. If you customize the Read permission level to include the View Usage Data permission that is typically part of the Full Control permission level, all members of the Visitors group can see usage data, which could cause performance issues.
  
You should customize the default permission levels if either of the following situations applies:
  
- A default permission level includes all permissions except one that the users must have to do their jobs, and you want to add that permission.
    
- A default permission level includes a permission that the users do not have to have.
    
    > [!NOTE]
    > Do not customize the default permission levels if your organization has security or other concerns about a specific permission that is part of the permission level. If you want to make that permission unavailable for all users assigned to the permission level or levels that include that permission, turn off the permission for all Web applications in your server farm, instead of change all of the permission levels To manage permissions for a web application, see [Manage permissions for a web application in SharePoint Server](/SharePoint/administration/manage-permissions-for-a-web-application). 
  
If you must make several changes to a permission level, create a custom permission level that includes all of the permissions that you need.
  
You might want to create additional permission levels if either of the following conditions is true:
  
- You want to exclude several permissions from a specific permission level.
    
- You want to define a unique set of permissions for a new permission level.
    
To create a permission level, you can create a permission level and then select the permissions that you want to include.
  
> [!NOTE]
> Some permissions depend on other permissions. If you clear a permission that another permission depends on, the other permission is also cleared. 
  

