---
title: "Default SharePoint groups"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
audience: Admin
ms.topic: reference
ms.service: sharepoint-online
localization_priority: Normal
ROBOTS: NOINDEX
ms.collection:  
- Strat_OD_share
- M365-collaboration
search.appverid:
- SPO160
- BSA160
- MET150
ms.assetid: 13bb2b6b-dd8c-447e-b71b-0e4bb9efe1d3
description: "Learn what the default SharePoint security groups are available for SharePoint sites in Office 365."
---

# Default SharePoint groups

The default SharePoint groups are created automatically when you create a site (previously called a "site collection"). The default groups use SharePoint's default permission levels - sometimes called SharePoint roles - to grant users rights and access. The permission levels that these groups have represent common levels of access that users have to have. They are a good place to start when you add users to a SharePoint site. 
  
Administrators can create additional groups to align more closely with specific business needs. Deciding how to design and populate your SharePoint security groups is an important decision that affects security for your site and site content. 
  
Here are links to information on understanding and setting SharePoint permissions.
  
- [Understanding permission levels in SharePoint](/sharepoint/understanding-permission-levels)
    
- [Edit and manage permissions for a SharePoint list or library](https://support.office.com/article/02D770F3-59EB-4910-A608-5F84CC297782)
    
- [How to create and edit permission levels](/sharepoint/how-to-create-and-edit-permission-levels)
    
## Permission levels for default SharePoint groups
<a name="__toc352237424"> </a>

SharePoint groups enable you to control access for sets of users instead of individual users. SharePoint groups are usually composed of many individual users. They can also hold Azure Active Directory security groups (created in Office 365 or Azure AD), or can be a combination of individual users and security groups. 
  
Each SharePoint group has a permission level. A permission level is simply a collection of individual permissions, such as Open, View, Edit or Delete. All the users in a group automatically have the permission level of the group. You can organize users into any number of groups, depending on the complexity of your organization, or your needs.
  
Each site template has a set of SharePoint groups associated with it. When you create a site, you use a site template, and SharePoint automatically creates the correct set of SharePoint groups for the site. The specific collection of groups depends on the type of template that you choose. 
  
For example, the following table shows the groups and permission levels that are created for team sites:
  
|**SharePoint groups**|**Default permission level**|**Applies to team sites**|
|:-----|:-----|:-----|:-----|
|Approvers  <br/> |Approve  <br/> |No  <br/> |
|Designers  <br/> |Design, Limited Access  <br/> |No  <br/> |
|Hierarchy Managers  <br/> |Manage Hierarchy  <br/> |No  <br/> |
|\<site name\> Members  <br/> |Edit  <br/> |Yes  <br/> |
|\<site name\> Owners  <br/> |Full Control  <br/> |Yes  <br/> |
|\<site name\> Visitors  <br/> |Read  <br/> |Yes  <br/> |
|Restricted Readers  <br/> |Restricted Read  <br/> |No  <br/> |
|Style Resource Readers  <br/> |Limited Access  <br/> |No  <br/> |
|Quick Deploy Users  <br/> |Contribute  <br/> |No  <br/> |
|Translation Mangers  <br/> |Limited Access  <br/> |No  <br/> |
   
## Suggested uses for SharePoint groups
<a name="__toc352237425"> </a>

The following table describes the SharePoint groups that are created when you use a standard site template to create a site. The table also provides suggested uses for each group.
  
|**Group Name**|**Permission level )**|**Use this group for:**|
|:-----|:-----|:-----|
|Approvers  <br/> |Approve  <br/> |Members of this group can edit and approve pages, list items, and documents.  <br/> |
|Designers  <br/> |Design  <br/> |Members of this group can edit lists, document libraries, and pages in the site. Designers can create Master Pages and Page Layouts in the Master Page Gallery and can change the behavior and appearance of each subsite by using master pages and CSS files.  <br/> |
|Hierarchy Managers  <br/> |Manage Hierarchy  <br/> |Members of this group can create sites, lists, list items, and documents.  <br/> |
|Owners  <br/> |Full Control  <br/> |People who must be able to manage site permissions, settings, and appearance.  <br/> |
|Members  <br/> |Edit or Contribute  <br/> |People who must be able to edit site content. Permission level depends on the site template that was used to create the site  <br/> |
|Visitors  <br/> |Read  <br/> |People who must be able to see site content, but not edit it.  <br/> |
|Restricted Readers  <br/> |Restricted Read  <br/> |People who should be able to view pages and documents but not view versions or permissions.  <br/> |
|Style Resource Readers  <br/> |Restricted Read  <br/> |People in this group have Limited Access to the Style Library and Master Page Gallery.  <br/> |
|Quick Deploy Users  <br/> |Contribute  <br/> |These users can schedule Quick Deploy jobs (Content Deployment).  <br/> |
|Viewers  <br/> |View Only  <br/> |These users see content, but can't edit or download it.  <br/> |
   
## Special SharePoint Groups
<a name="__toc352237426"> </a>
<a name="__toc339377366"> </a>

"Everyone except external users" is a special group that doesn't appear in the Microsoft 365 admin center, and "Company Administrator" acts like a group but is a role in Azure AD. 
  
 **Everyone except external users** All users added to your organization automatically become members of "Everyone except external users". Please note that you cannot change default permissions granted to "Everyone except external users" on Office 365 group-connected team sites. If a group-connected team site is set to "Public," "Everyone except external users" has a default permission level of "Edit." When a group-connected team site is set to "Private," "Everyone except external users" can't be granted any permission to the site. Although the "Site permissions" tab will allow modifications to be granted, a background job will block such modifications to take effect. To change the privacy setting for a group-connected team site, select the Settings icon, and then select **Site information**.  
  
 **Company Administrator** This group contains all users who are assigned the global admin role. For more info about this role and its permissions in Azure AD, see [Company administrator](/azure/active-directory/users-groups-roles/directory-assign-admin-roles#company-administrator). The root site for your organization is created with "Company Administrator" as the primary admin. 
  
## Site administrators 
  
||**SharePoint Online**|**SharePoint on-premises**|
|:-----|:-----|:-----|
|Who can use this group?  <br/> |Yes  <br/> |Yes  <br/> |
   
A site can have several site admins, but must have one and only one primary administrator. Any site admin can add or remove other admins. Site admins have full control of the site root and any subsites in the site, and can audit all site content. 
  
In SharePoint on-premises, you designate a site collection administrator when you create a site.
  
## SharePoint administrators
  
||**SharePoint Online**|**SharePoint On-premises**|
|:-----|:-----|:-----|
|Who can use this group?  <br/> |Yes  <br/> |No, by default.  <br/> Requires special installation.  <br/> |
   
In SharePoint Online, there is also a SharePoint administrator. A SharePoint administrator can use the SharePoint admin center or PowerShell to manage settings for all sites. Any global admin in Microsoft 365 also has the permissions of a SharePoint admin. For more info about the SharePoint admin role, see [About the SharePoint admin role in Microsoft 365](sharepoint-admin-role.md).
    
If you are using SharePoint on-premises, you do not have a SharePoint administrator or SharePoint admin center.
  

