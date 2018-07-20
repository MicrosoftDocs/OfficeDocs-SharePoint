---
title: "Default SharePoint groups"
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 5/22/2018
ms.audience: Admin
ms.topic: reference
ms.service: sharepoint-online
localization_priority: Normal
search.appverid:
- SPO160
- BSA160
- MET150
ms.assetid: 13bb2b6b-dd8c-447e-b71b-0e4bb9efe1d3
description: "Learn what the default SharePoint security groups are available for SharePoint sites in Office 365."
---

# Default SharePoint groups

The default SharePoint groups are created automatically when you create a site collection. The default groups use SharePoint's default permission levels - sometimes called SharePoint roles - to grant users rights and access. The permission levels that these groups have represent common levels of access that users have to have. They are a good place to start when you add users to a SharePoint site. 
  
Administrators can create additional groups to align more closely with specific business needs. Deciding how to design and populate your SharePoint security groups is an important decision that affects security for your site and site content. 
  
Here are links to information on understanding and setting SharePoint permissions.
  
- [Understanding permission levels in SharePoint](https://support.office.com/article/87ecbb0e-6550-491a-8826-c075e4859848)
    
- [Edit and manage permissions for a SharePoint list or library](https://support.office.com/article/02D770F3-59EB-4910-A608-5F84CC297782)
    
- [How to create and edit Permission Levels](https://support.office.com/article/53c86040-07fa-4ea7-bc55-34ee96b437fe)
    
## Permission levels for default SharePoint groups
<a name="__toc352237424"> </a>

SharePoint groups enable you to control access for sets of users instead of individual users. SharePoint groups are usually composed of many individual users. They can also hold Windows Active Directory security groups (created in Office 365), or can be a combination of individual users and security groups. 
  
Each SharePoint group has a permission level. A permission level is simply a collection of individual permissions, such as Open, View, Edit or Delete. All the users in a group automatically have the permission level of the group. You can organize users into any number of groups, depending on the complexity of your organization, or your needs.
  
Each site template has a set of SharePoint groups associated with it. When you create a site, you use a site template, and SharePoint automatically creates the correct set of SharePoint groups for the site. The specific collection of groups depends on the type of template that you choose. 
  
For example, the following table shows the groups and permission levels that are created for the Public Website and the Team Site:
  
|**SharePoint groups**|**Default permission level**|**Applies to Public Website**|**Applies to Team Sites**|
|:-----|:-----|:-----|:-----|
|Approvers  <br/> |Approve  <br/> |Yes  <br/> |No  <br/> |
|Designers  <br/> |Design, Limited Access  <br/> |Yes  <br/> |No  <br/> |
|Hierarchy Managers  <br/> |Manage Hierarchy  <br/> |Yes  <br/> |No  <br/> |
|\<site name\> Members  <br/> |Edit  <br/> |Yes  <br/> |Yes  <br/> |
|\<site name\> Owners  <br/> |Full Control  <br/> |Yes  <br/> |Yes  <br/> |
|\<site name\> Visitors  <br/> |Read  <br/> |Yes  <br/> |Yes  <br/> |
|Restricted Readers  <br/> |Restricted Read  <br/> |Yes  <br/> |No  <br/> |
|Style Resource Readers  <br/> |Limited Access  <br/> |Yes  <br/> |No  <br/> |
|Quick Deploy Users  <br/> |Contribute  <br/> |Yes  <br/> |No  <br/> |
|Translation Mangers  <br/> |Limited Access  <br/> |Yes  <br/> |No  <br/> |
   
## Suggested uses for SharePoint groups
<a name="__toc352237425"> </a>

The following table describes the SharePoint groups that are created when you use a standard site template to create a site. The table also provides suggested uses for each group.
  
|**Group Name**|**Permission level )**|**Use this group for:**|
|:-----|:-----|:-----|
|Approvers  <br/> |Approve  <br/> |Members of this group can edit and approve pages, list items, and documents.  <br/> |
|Designers  <br/> |Design  <br/> |Members of this group can edit lists, document libraries, and pages in the site. Designers can create Master Pages and Page Layouts in the Master Page Gallery and can change the behavior and appearance of each site in the site collection by using master pages and CSS files..  <br/> |
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

In addition, special SharePoint groups support high-level administration tasks, such as site collection administrators, who have Full Control of all sites in a designated site collection.
  
### Company Administrator and Everyone except external users groups for Office 365 users
<a name="__toc339377366"> </a>

The Company Administrator and Everyone except external users groups contain admins and users for Office 365. They provide access for Office 365 users on a SharePoint site. 
  
 **Everyone except external users** When a user is added to Office 365, the user automatically becomes a member of Everyone except external users. This group has a default permission level of Contribute. When you grant permissions to this group, all users who are added to Office 365 can view, add, update, and delete items from lists and libraries (unless you change the default permission level for the group). 
  
 **Company Administrators**The Company Administrators group is added to the list of Site Collection administrators. This group has a permission level of Full Control. 
  
Although you can change the group membership for Company Administrators, it's important to be careful. Because the Company Administrators group members are Global admins in Office 365, and also Site Collection administrators, changing their group status might have unexpected consequences. For example, if you remove a Company Administrator as a site collection administrator, the Global admin group might no longer have Full Control permissions. 
  
> [!IMPORTANT]
>  Do not remove a **Company Administrators** or **Global admin** groups before you configure permissions appropriately. Be sure that these users have the permission level that they must have to perform necessary actions. If you do not make sure that these users have appropriate permission levels, SharePoint security configuration is much more difficult. For example, site administrators can't configure access for groups, but instead must grant access to sites a per-user basis. 
  
Site collection administrators 
  
||**SharePoint Online**|**SharePoint On-premises**|
|:-----|:-----|:-----|
|Who can use this group?  <br/> |Yes  <br/> |Yes  <br/> |
   
A SharePoint site can have primary and secondary site collection administrators. If you are a site collection administrator, you can designate more site collection administrators.
  
These users are the main contacts for a whole site collection. Site Collection Administrators have full control of all sites within the site collection, can audit all site content, and receive any administrative alert messages. 
  
In SharePoint On-premises, you designate a site collection administrator when you install a site.
  
In SharePoint Online, the account that you used when you set up SharePoint Online is automatically a site collection administrator. If you have to add more site collection administrators in SharePoint Online, an existing site collection administrator or the SharePoint online administrator can do so.
  
SharePoint administrators
  
||**SharePoint Online**|**SharePoint On-premises**|
|:-----|:-----|:-----|
|Who can use this group?  <br/> |Yes  <br/> |No, by default.  <br/> Requires special installation.  <br/> |
   
If you use SharePoint Online in Office 365 plans other than Office 365 Small Business and Office 365 Small Business Premium, there is also a SharePoint administrator. A SharePoint administrator can use the SharePoint admin center or PowerShell to manage settings for all site collections. Any Office 365 global administrator also has the permissions of a SharePoint admin.  
  
The SharePoint administrator can do any of the following tasks:
  
- Configure user profile and InfoPath forms services
    
- Setup search parameters
    
- Set up a secure store and business connectivity services
    
- Create a term store
    
- Define a records management system
    
- Monitor quotas
    
- Turn on or off the ability to invite external users to access the SharePoint Online site
    
- Create, update, or delete site collections
    
- Assign primary and secondary site collection owners to any site collection in their venue.
    
If you are using SharePoint on-premises, you do not have a SharePoint administrator or SharePoint admin center after a standard SharePoint installation.
  

