---
ms.date: 07/11/2018
title: "Default SharePoint groups"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: serdars
recommendations: true
audience: Admin
f1.keywords:
- NOCSH
ms.topic: reference
ms.service: sharepoint-online
ms.localizationpriority: medium
ROBOTS: NOINDEX
ms.collection:  
- Strat_OD_share
- M365-collaboration
ms.custom: admindeeplinkSPO
search.appverid:
- SPO160
- BSA160
- MET150
ms.assetid: 13bb2b6b-dd8c-447e-b71b-0e4bb9efe1d3
description: "Learn what the default SharePoint groups are available for SharePoint sites in Microsoft 365."
---

# Default SharePoint groups

The default SharePoint groups are created automatically when you create a site (previously called a "site collection"). The default groups use SharePoint's default permission levels - sometimes called SharePoint roles - to grant users rights and access. The permission levels that these groups have represent common levels of access that users have to have. They are a good place to start when you add users to a SharePoint site. 
  
Administrators can create additional groups to align more closely with specific business needs. Deciding how to design and populate your SharePoint groups is an important decision that affects security for your site and site content. 
  
Here are links to information on understanding and setting SharePoint permissions.
  
- [Understanding permission levels in SharePoint](./understanding-permission-levels.md)
    
- [Edit and manage permissions for a SharePoint list or library](https://support.office.com/article/02D770F3-59EB-4910-A608-5F84CC297782)
    
## Permission levels for default SharePoint groups
<a name="__toc352237424"> </a>

SharePoint groups enable you to control access for sets of users instead of individual users. SharePoint groups are usually composed of many individual users. They can also hold Azure Active Directory security groups (created in Microsoft 365 or Azure AD), or can be a combination of individual users and security groups. 
  
Each SharePoint group has a permission level. A permission level is simply a collection of individual permissions, such as Open, View, Edit or Delete. All the users in a group automatically have the permission level of the group. You can organize users into any number of groups, depending on the complexity of your organization, or your needs.
  
Each site template has a set of SharePoint groups associated with it. When you create a site, you use a site template, and SharePoint automatically creates the correct set of SharePoint groups for the site. The specific collection of groups depends on the type of template that you choose. 
  
For example, the following table shows the groups and permission levels that are created for team sites:
  
| SharePoint groups | Default permission level | Applies to team sites |
|:-----|:-----|:-----|
|Approvers  | Approve  | No  | 
|Designers  | Design, Limited Access  | No  | 
|Hierarchy Managers  | Manage Hierarchy  | No  | 
|\<site name\> Members  | Edit  | Yes  | 
|\<site name\> Owners  | Full Control  | Yes  | 
|\<site name\> Visitors  | Read  | Yes  | 
|Restricted Readers  | Restricted Read  | No  | 
|Style Resource Readers  | Limited Access  | No  | 
|Quick Deploy Users  | Contribute  | No  | 
|Translation Managers  | Limited Access  | No  | 
   
## Suggested uses for SharePoint groups
<a name="__toc352237425"> </a>

The following table describes the SharePoint groups that are created when you use a standard site template to create a site. The table also provides suggested uses for each group.
  
| Group Name | Permission level | Use this group for |
|:-----|:-----|:-----|
|Approvers  | Approve  | Members of this group can edit and approve pages, list items, and documents.  | 
|Designers  | Design  | Members of this group can edit lists, document libraries, and pages in the site. Designers can create Master Pages and Page Layouts in the Master Page Gallery and can change the behavior and appearance of each subsite by using master pages and CSS files.  | 
|Hierarchy Managers  | Manage Hierarchy  | Members of this group can create sites, lists, list items, and documents.  | 
|Owners  | Full Control  | People who must be able to manage site permissions, settings, and appearance.  | 
|Members  | Edit or Contribute  | People who must be able to edit site content. Permission level depends on the site template that was used to create the site  | 
|Visitors  | Read  | People who must be able to see site content, but not edit it.  | 
|Restricted Readers  | Restricted Read  | People who should be able to view pages and documents but not view versions or permissions.  | 
|Style Resource Readers  | Restricted Read  | People in this group have Limited Access to the Style Library and Master Page Gallery.  | 
|Quick Deploy Users  | Contribute  | These users can schedule Quick Deploy jobs (Content Deployment).  | 
|Viewers  | View Only  | These users see content, but can't edit or download it.  | 
   
## Special SharePoint Groups
<a name="__toc352237426"> </a>
<a name="__toc339377366"> </a>

"Everyone except external users" is a special group that doesn't appear in the Microsoft 365 admin center, and "Company Administrator" acts like a group but is a role in Azure AD. 
  
 **Everyone except external users** All users added to your organization automatically become members of "Everyone except external users". Please note that you cannot change default permissions granted to "Everyone except external users" on Microsoft 365 group-connected team sites. If a group-connected team site is set to "Public", "Everyone except external users" has a default permission level of "Edit". When a group-connected team site is set to "Private", "Everyone except external users" can be manually added to the site through "Site permissions". To change the privacy setting for a group-connected team site, select the Settings icon, and then select **Site information**. 
  
 **Company Administrator** This group contains all users who are assigned the global admin role. For more info about this role and its permissions in Azure AD, see [Company administrator](/azure/active-directory/users-groups-roles/directory-assign-admin-roles#company-administrator). The root site for your organization is created with "Company Administrator" as the primary admin. 
  
## Site administrators 
  
| Description | SharePoint in Microsoft 365 | SharePoint Server |
|:-----|:-----|:-----|
|Who can use this group?  | Yes  | Yes  | 
   
A site can have several site admins, but must have one and only one primary administrator. Any site admin can add or remove other admins. Site admins have full control of the site root and any subsites in the site, and can audit all site content. 
  
In SharePoint Server, you designate a site collection administrator when you create a site.
  
## SharePoint admins
  
| Description | SharePoint in Microsoft 365 | SharePoint Server |
|:-----|:-----|:-----|
|Who can use this group?  | Yes  | No, by default.  <br/> Requires special installation.  | 
   
In SharePoint in Microsoft 365, there is also a SharePoint admin. A SharePoint admin can use the <a href="https://go.microsoft.com/fwlink/?linkid=2185219" target="_blank">SharePoint admin center</a> or PowerShell to manage settings for all sites. Any global admin in Microsoft 365 also has the permissions of a SharePoint admin. For more info about the SharePoint admin role, see [About the SharePoint admin role in Microsoft 365](sharepoint-admin-role.md).
    
If you are using SharePoint Server, you do not have a SharePoint admin or SharePoint admin center.

