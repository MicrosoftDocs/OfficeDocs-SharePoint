---
title: "Permission levels and permissions in SharePoint 2007"
ms.author: mikeplum
author: MikePlumleyMSFT
manager: scotv
ms.date: 5/16/2014
ms.audience: Admin
ms.topic: article
ms.prod: office-online-server
localization_priority: Normal
ms.assetid: 49d456eb-d3c8-4402-86b1-deb911224afb

---

# Permission levels and permissions in SharePoint 2007

## In this article
<a name="__top"> </a>

> [Default permission levels in Windows SharePoint Services 3.0](permission-levels-and-permissions-in-sharepoint-2007.md#bm1)
    
> [List, site, and personal permissions](permission-levels-and-permissions-in-sharepoint-2007.md#bm2)
    
> [Dependencies and descriptions](permission-levels-and-permissions-in-sharepoint-2007.md#bm3)
    
Although sites that are built on Windows SharePoint Services often have additional default SharePoint groups, Windows SharePoint Services 3.0 includes five permission levels by default. Each of these permission levels has specific permissions associated with it. As a site owner, you can choose which permissions are associated with these permission levels (except for the Limited Access and Full Control permission levels) or add new permission levels to combine different sets of permissions.
  
> [!NOTE]
> Prior to Windows SharePoint Services 3.0, permission levels were called site groups and SharePoint groups were called cross-site groups. 
  
As a site owner, you can associate permissions with permission levels and also associate permission levels with users and SharePoint groups. Users and SharePoint groups are associated with securable objects such as sites, lists, list items, libraries, folders within lists and libraries, and documents. For more information about assigning permissions in different securable objects, see [About controlling access to sites and site content](https://support.office.com/article/1106594c-82f4-4447-ab6c-74b680b1bb40).
  
The following tables list and describe the permission levels that you can assign to users and SharePoint groups and the permissions you can assign to permission levels. For each permission, the permission level that it is associated with it, by default, is listed. For each permission, any permissions dependent on it are listed, as well as any default permission levels that include the permission.
  
## Default permission levels in Windows SharePoint Services 3.0
<a name="bm1"> </a>

|****Permission Level****|****Description****|
|:-----|:-----|
|Full Control  <br/> |This permission level contains all permissions. Assigned to the Site name Owners SharePoint group, by default. This permission level cannot be customized or deleted.  <br/> |
|Design  <br/> |Can create lists and document libraries, edit pages and apply themes, borders, and style sheets in the Web site. Not assigned to any SharePoint group, by default.  <br/> |
|Contribute  <br/> |Can add, edit, and delete items in existing lists and document libraries. Assigned to the Site name Members SharePoint group, by default.  <br/> |
|Read  <br/> |Read-only access to the Web site. Users and SharePoint groups with this permission level can view items and pages, open items, and documents. Assigned to the Site name Visitors SharePoint group, by default.  <br/> |
|Limited Access  <br/> |The Limited Access permission level is designed to be combined with fine-grained permissions to give users access to a specific list, document library, item, or document, without giving them access to the entire site. However, to access a list or library, for example, a user must have permission to open the parent Web site and read shared data such as the theme and navigation bars of the Web site. The Limited Access permission level cannot be customized or deleted.  <br/> > [!NOTE]> You cannot assign this permission level to users or SharePoint groups. Instead, Windows SharePoint Services 3.0 automatically assigns this permission level to users and SharePoint groups when you grant them access to an object on your site that requires that they have access to a higher level object on which they do not have permissions. For example, if you grant users access to an item in a list and they do not have access to the list itself, Windows SharePoint Services 3.0 automatically grants them Limited Access on the list, and also the site, if needed.           |
   
[Top of Page](permission-levels-and-permissions-in-sharepoint-2007.md#__top)
  
## List, site, and personal permissions
<a name="bm2"> </a>

Windows SharePoint Services 3.0 includes 33 permissions, which are used in the five default permission levels. You can change which permissions are included in a particular permission level (except for the Limited Access and Full Control permission levels) or create a new permission level to contain a specific set of permissions that you specify.
  
Permissions are categorized as list permissions, site permissions, and personal permissions, depending upon the objects to which they can be applied. For example, site permissions apply to a particular site, list permissions apply only to lists and libraries, and personal permissions apply only to things like personal views, private Web Parts, etc. The following tables show permissions and the permission levels they are assigned to, by default. 
  
### List Permissions

|****Permission****|****Full Control****|****Design****|****Contribute****|****Read****|****Limited Access****|
|:-----|:-----|:-----|:-----|:-----|:-----|
|Manage Lists  <br/> |X  <br/> |X  <br/> ||||
|Override Check-Out  <br/> |X  <br/> |X  <br/> ||||
|Add Items  <br/> |X  <br/> |X  <br/> |X  <br/> |||
|Edit Items  <br/> |X  <br/> |X  <br/> |X  <br/> |||
|Delete Items  <br/> |X  <br/> |X  <br/> |X  <br/> |||
|View Items  <br/> |X  <br/> |X  <br/> |X  <br/> |X  <br/> ||
|Approve Items  <br/> |X  <br/> |X  <br/> ||||
|Open Items  <br/> |X  <br/> |X  <br/> |X  <br/> |X  <br/> ||
|View Versions  <br/> |X  <br/> |X  <br/> |X  <br/> |X  <br/> ||
|Delete Versions  <br/> |X  <br/> |X  <br/> |X  <br/> |||
|Create Alerts  <br/> |X  <br/> |X  <br/> |X  <br/> |X  <br/> ||
|View Application Pages  <br/> |X  <br/> |X  <br/> |X  <br/> |X  <br/> |X  <br/> |
   
### Site Permissions

|****Permission****|****Full Control****|****Design****|****Contribute****|****Read****|****Limited Access****|
|:-----|:-----|:-----|:-----|:-----|:-----|
|Manage Permissions  <br/> |X  <br/> |||||
|View Usage Data  <br/> |X  <br/> |||||
|Create Subsites  <br/> |X  <br/> |||||
|Manage Web Site  <br/> |X  <br/> |||||
|Add and Customize Pages  <br/> |X  <br/> |X  <br/> ||||
|Apply Themes and Borders  <br/> |X  <br/> |X  <br/> ||||
|Apply Style Sheets  <br/> |X  <br/> |X  <br/> ||||
|Create Groups  <br/> |X  <br/> |||||
|Browse Directories  <br/> |X  <br/> |X  <br/> |X  <br/> |||
|Use Self-Service Site Creation  <br/> |X  <br/> |X  <br/> |X  <br/> |X  <br/> ||
|View Pages  <br/> |X  <br/> |X  <br/> |X  <br/> |X  <br/> ||
|Enumerate Permissions  <br/> |X  <br/> |||||
|Browse User Information  <br/> |X  <br/> |X  <br/> |X  <br/> |X  <br/> |X  <br/> |
|Manage Alerts  <br/> |X  <br/> |||||
|Use Remote Interfaces  <br/> |X  <br/> |X  <br/> |X  <br/> |X  <br/> |X  <br/> |
|Use Client Integration Features  <br/> |X  <br/> |X  <br/> |X  <br/> |X  <br/> |X  <br/> |
|Open  <br/> |X  <br/> |X  <br/> |X  <br/> |X  <br/> |X  <br/> |
|Edit Personal User Information  <br/> |X  <br/> |X  <br/> |X  <br/> |||
   
### Personal Permissions

|****Permission****|****Full Control****|****Design****|****Contribute****|****Read****|****Limited Access****|
|:-----|:-----|:-----|:-----|:-----|:-----|
|Manage Personal Views  <br/> |X  <br/> |X  <br/> |X  <br/> |||
|Add/Remove Private Web Parts  <br/> |X  <br/> |X  <br/> |X  <br/> |||
|Update Personal Web Parts  <br/> |X  <br/> |X  <br/> |X  <br/> |||
   
[Top of Page](permission-levels-and-permissions-in-sharepoint-2007.md#__top)
  
## Dependencies and descriptions
<a name="bm3"> </a>

Many permissions are dependent on other permissions. When you select a permission that is dependent on another, the permission on which it is dependent is also automatically selected. Likewise, clearing a permission on which other permissions are dependent also clears the dependent permissions. The following tables describe what each permission is used for and lists dependent permissions, if applicable. 
  
### List permissions

|****Permission****|****Description****|****Dependent permissions****|
|:-----|:-----|:-----|
|Manage Lists  <br/> |Create and delete lists, add or remove columns in a list, and add or remove public views of a list.  <br/> |View Items, View Pages, Open, Manage Personal Views  <br/> |
|Override Check-Out  <br/> |Discard or check in a document which is checked out to another user.  <br/> |View Items, View Pages, Open  <br/> |
|Add Items  <br/> |Add items to lists, add documents to document libraries, and add Web discussion comments.  <br/> |View Items, View Pages, Open  <br/> |
|Edit Items  <br/> |Edit items in lists, edit documents in document libraries, edit Web discussion comments in documents, and customize Web Part Pages in document libraries.  <br/> |View Items, View Pages, Open  <br/> |
|Delete Items  <br/> |Delete items from a list, documents from a document library, and Web discussion comments in documents.  <br/> |View Items, View Pages, Open  <br/> |
|View Items  <br/> |View items in lists, documents in document libraries, and Web discussion comments.  <br/> |View Pages, Open  <br/> |
|Approve Items  <br/> |Approve a minor version of a list item or document.  <br/> |Edit Items, View Items, View Pages, Open  <br/> |
|Open Items  <br/> |View the source of documents with server-side file handlers.  <br/> |View Items, View Pages, Open  <br/> |
|View Versions  <br/> |View past versions of a list item or document.  <br/> |View Items, View Pages, Open  <br/> |
|Delete Versions  <br/> |Delete past versions of a list item or document.  <br/> |View Items, View Versions, View Pages, Open  <br/> |
|Create Alerts  <br/> |Create e-mail alerts.  <br/> |View Items, View Pages, Open  <br/> |
|View Application Pages  <br/> |View documents and views in a list or document library.  <br/> |Open  <br/> |
   
### Site permissions

|****Permission****|****Description****|****Dependent permissions****|
|:-----|:-----|:-----|
|Manage Permissions  <br/> |Create and change permission levels on the Web site and assign permissions to users and groups.  <br/> |Approve Items, Enumerate Permissions, Open  <br/> |
|View Usage Data  <br/> |View reports on Web site usage.  <br/> |Approve Items, Open  <br/> |
|Create Subsites  <br/> |Create subsites such as team sites, Meeting Workspace sites, and Document Workspace sites.  <br/> |View Pages, Open  <br/> |
|Manage Web Site  <br/> |Perform all administration tasks for the Web site as well as manage content.  <br/> |View Pages, Open  <br/> |
|Add and Customize Pages  <br/> |Add, change, or delete HTML pages or Web Part pages, and edit the Web site using a Windows SharePoint Services-compatible editor.  <br/> |View Items, Browse Directories, View Pages, Open  <br/> |
|Apply Themes and Borders  <br/> |Apply a theme or borders to the entire Web site.  <br/> |View Pages, Open  <br/> |
|Apply Style Sheets  <br/> |Apply a style sheet (.css file) to the Web site.  <br/> |View Pages, Open  <br/> |
|Create Groups  <br/> |Create a group of users that can be used anywhere within the site collection.  <br/> |View Pages, Open  <br/> |
|Browse Directories  <br/> |Enumerate files and folders in a Web site using an interface such as SharePoint Designer or Web-based Distributed Authoring and Versioning (Web DAV).  <br/> |View Pages, Open  <br/> |
|Use Self-Service Site Creation  <br/> |Create a Web site using Self-Service Site Creation.  <br/> |View Pages, Open  <br/> |
|View Pages  <br/> |View pages in a Web site.  <br/> |Open  <br/> |
|Enumerate Permissions  <br/> |Enumerate permissions on the Web site, list, folder, document, or list item.  <br/> |View Items, Open Items, View Versions, Browse Directories, View Pages, Open  <br/> |
|Browse User Information  <br/> |View information about users of the Web site.  <br/> |Open  <br/> |
|Manage Alerts  <br/> |Manage alerts for all users of the Web site  <br/> |View Items, Create Alerts, View Pages, Open  <br/> |
|Use Remote Interfaces  <br/> |Use Simple Object Access Protocol (SOAP), Web DAV, or SharePoint Designer interfaces to access the Web site.  <br/> |Open  <br/> |
|Open  <br/> |Open a Web site, list, or folder to access items inside that container.  <br/> |No dependent permissions  <br/> |
|Edit Personal User Information  <br/> |Allow a user to change his or her own user information, such as adding a picture.  <br/> |Browse User Information, Open  <br/> |
   
### Personal permissions

|****Permission****|****Description****|****Dependent permissions****|
|:-----|:-----|:-----|
|Manage Personal Views  <br/> |Create, change, and delete personal views of lists.  <br/> |View Items, View Pages, Open  <br/> |
|Add/Remove Private Web Parts  <br/> |Add or remove private Web Parts on a Web Part Page.  <br/> |View Items, View Pages, Open, Update Personal Web Parts  <br/> |
|Update Personal Web Parts  <br/> |Update Web Parts to display personalized information.  <br/> |View Items, View Pages, Open  <br/> |
   
[Top of Page](permission-levels-and-permissions-in-sharepoint-2007.md#__top)
  

