---
title: "User permissions and permission levels in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 8/17/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: ff13b917-5236-48e6-89d5-8c78e61a72a8
description: "Learn about the default permission levels and user permissions in SharePoint Server."
---

# User permissions and permission levels in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
Default permission levels are predefined sets of permissions that you can assign to individual users, groups of users, or security groups, based on the functional requirements of the users and on security considerations. SharePoint Server permission levels are defined at the site collection level and are inherited from the parent object by default.
    
## Default permission levels
<a name="section1"> </a>

Default permission levels are made up of a set of permissions that enable users to perform a collection of related tasks. SharePoint Server includes seven permission levels. You can customize the permissions contained within five of these permission levels. You cannot customize the permissions within the Limited Access and Full Control permission levels.
  
> [!NOTE]
> Although you cannot directly edit the Limited Access and Full Control permission levels, you can make individual permissions unavailable for the entire web application, which removes those permissions from the Limited Access and Full Control permission levels. For more information, see [Manage permissions for a web application in SharePoint Server](/SharePoint/administration/manage-permissions-for-a-web-application). 
  
The following table lists the default permission levels for team sites in SharePoint Server.
  
|**Permission level**|**Description**|**Permissions included by default**|
|:-----|:-----|:-----|
|View Only  <br/> |Enables users to view application pages. The View Only permission level is used for the Excel Services Viewers group.  <br/> | View Application Pages  <br/>  View Items  <br/>  View Versions  <br/>  Create Alerts  <br/>  Use Self Service Site Creation  <br/>  View Pages  <br/>  Browse User Information  <br/>  Use Remote Interfaces  <br/>  Use Client Integration Features  <br/>  Open  <br/> |
|Limited Access  <br/> |Enables users to access shared resources and a specific asset. Limited Access is designed to be combined with fine-grained permissions to enable users to access a specific list, document library, folder, list item, or document, without enabling them to access the whole site. Limited Access cannot be edited or deleted.  <br/> | View Application Pages  <br/>  Browse User Information  <br/>  Use Remote Interfaces  <br/>  Use Client Integration Features  <br/>  Open  <br/> |
|Read  <br/> |Enables users to view pages and list items, and to download documents.  <br/> | Limited Access permissions, plus:  <br/>  View Items  <br/>  Open Items  <br/>  View Versions  <br/>  Create Alerts  <br/>  Use Self-Service Site Creation  <br/>  View Pages  <br/> |
|Contribute  <br/> |Enables users to manage personal views, edit items and user information, delete versions in existing lists and document libraries, and add, remove, and update personal Web Parts.  <br/> | Read permissions, plus:  <br/>  Add Items  <br/>  Edit Items  <br/>  Delete Items  <br/>  Delete Versions  <br/>  Browse Directories  <br/>  Edit Personal User Information  <br/>  Manage Personal Views  <br/>  Add/Remove Personal Web Parts  <br/>  Update Personal Web Parts  <br/> |
|Edit  <br/> |Enables users to manage lists.  <br/> | Contribute permissions, plus:  <br/>  Manage Lists  <br/> |
|Design  <br/> |Enables users to view, add, update, delete, approve, and customize items or pages in the website.  <br/> | Edit permissions, plus:  <br/>  Add and Customize Pages  <br/>  Apply Themes and Borders  <br/>  Apply Style Sheets  <br/>  Override List Behaviors  <br/>  Approve Items  <br/> |
|Full Control  <br/> |Enables users to have full control of the website.  <br/> |All permissions  <br/> |
   
If you use a site template other than the team site template, you will see a different list of default SharePoint permission levels. For example, the following table shows additional permission levels provided with the publishing template.
  
|**Permission level**|**Description**|**Permissions included by default**|
|:-----|:-----|:-----|
|Restricted Read  <br/> |View pages and documents. For publishing sites only.  <br/> | View Items  <br/>  Open Items  <br/>  View Pages  <br/>  Open  <br/> |
|Approve  <br/> |Edit and approve pages, list items, and documents. For publishing sites only.  <br/> | Contribute permissions, plus:  <br/>  Override List Behaviors  <br/>  Approve Items  <br/> |
|Manage Hierarchy  <br/> |Create sites; edit pages, list items, and documents, and change site permissions. For Publishing sites only.  <br/> | Design permissions minus the Approve Items, Apply Themes and Borders, and Apply Style Sheets permissions, plus:  <br/>  Manage permissions  <br/>  View Web Analytics Data  <br/>  Create Subsites  <br/>  Manage Alerts  <br/>  Enumerate Permissions  <br/>  Manage Web Site  <br/> |
   
## User permissions
<a name="section2"> </a>

SharePoint Server includes 33 permissions, which are used in the default permission levels. You can configure which permissions are included in a particular permission level (except for the Limited Access and Full Control permission levels), or you can create a new permission level to contain specific permissions.
  
Permissions are categorized as list permissions, site permissions, and personal permissions, depending on the objects to which they can be applied. For example, site permissions apply to a particular site, list permissions apply only to lists and libraries, and personal permissions apply only to certain objects, such as personal views and private Web Parts. The following tables describe what each permission is used for, the dependent permissions, and the permission levels in which it is included.
  
### List permissions

|**Permission**|**Description**|**Dependent permissions**|**Included in these permission levels by default**|
|:-----|:-----|:-----|:-----|
|Manage Lists  <br/> |Create and delete lists, add or remove columns in a list, and add or remove public views of a list.  <br/> |View Items, View Pages, Open  <br/> |Edit, Design, Full Control, Manage Hierarchy  <br/> |
|Override List Behaviors  <br/> |Discard or check in a document that is checked out to another user, and change or override settings that allow users to read/edit only their own items.  <br/> |View Items, View Pages, Open  <br/> |Design, Full Control  <br/> |
|Add Items  <br/> |Add items to lists, and add documents to document libraries.  <br/> |View Items, View Pages, Open  <br/> |Contribute, Edit, Design, Full Control  <br/> |
|Edit Items  <br/> |Edit items in lists, edit documents in document libraries, and customize Web Part pages in document libraries.  <br/> |View Items, View Pages, Open  <br/> |Contribute, Edit, Design, Full Control  <br/> |
|Delete Items  <br/> |Delete items from a list, and documents from a document library.  <br/> |View Items, View Pages, Open  <br/> |Contribute, Edit, Design, Full Control  <br/> |
|View Items  <br/> |View items in lists, and documents in document libraries.  <br/> |View Pages, Open  <br/> |Read, Contribute, Edit, Design, Full Control  <br/> |
|Approve Items  <br/> |Approve a minor version of list items or document.  <br/> |Edit Items, View Items, View Pages, Open  <br/> |Design, Full Control  <br/> |
|Open Items  <br/> |View the source of documents with server-side file handlers.  <br/> |View Items, View Pages, Open  <br/> |Read, Contribute, Edit, Design, Full Control  <br/> |
|View Versions  <br/> |View past versions of a list item or document.  <br/> |View Items, Open Items, View Pages, Open  <br/> |Read, Contribute, Edit, Design, Full Control  <br/> |
|Delete Versions  <br/> |Delete past versions of list items or documents.  <br/> |View Items, View Versions, View Pages, Open  <br/> |Contribute, Edit, Design, Full Control  <br/> |
|Create Alerts  <br/> |Create alerts.  <br/> |View Items, View Pages, Open  <br/> |Read, Contribute, Edit, Design, Full Control  <br/> |
|View Application Pages  <br/> |View forms, views, and application pages. Enumerate lists.  <br/> |Open  <br/> |All  <br/> |
   
### Site permissions

|**Permission**|**Description**|**Dependent permissions**|**Included in these permission levels by default**|
|:-----|:-----|:-----|:-----|
|Manage Permissions  <br/> |Create and change permission levels on the web site and assign permissions to users and groups.  <br/> |View Items, Open Items, View Versions, Browse Directories, View Pages, Enumerate Permissions, Browse User Information, Open  <br/> |Full Control  <br/> |
|View Web Analytics Data  <br/> |View reports on Web site usage.  <br/> |View Pages, Open  <br/> |Full Control  <br/> |
|Create Subsites  <br/> |Create subsites such as team sites, Meeting Workspace sites, and Document Workspace sites.  <br/> |View Pages, Browse User Information, Open  <br/> |Full Control  <br/> |
|Manage Web Site  <br/> |Grants the ability to perform all administration tasks for the web site, as well as manage content.  <br/> |View Items, Add and Customize Pages, Browse Directories, View Pages, Enumerate Permissions, Browse User Information, Open  <br/> |Full Control  <br/> |
|Add and Customize Pages  <br/> |Add, change, or delete HTML pages or Web Part pages, and edit the website.  <br/> |View Items, Browse Directories, View Pages, Open  <br/> |Design, Full Control  <br/> |
|Apply Themes and Borders  <br/> |Apply a theme or borders to the whole website.  <br/> |View Pages, Open  <br/> |Design, Full Control  <br/> |
|Apply Style Sheets  <br/> |Apply a style sheet (.css file) to the website.  <br/> |View Pages, Open  <br/> |Design, Full Control  <br/> |
|Create Groups  <br/> |Create a group of users that can be used anywhere within the site collection.  <br/> |View Pages, Browse User Information, Open  <br/> |Full Control  <br/> |
|Browse Directories  <br/> |Enumerate files and folders in a website by using SharePoint Designer 2013 and Web DAV interfaces.  <br/> |View Pages, Open  <br/> |Contribute, Edit, Design, Full Control  <br/> |
|Use Self-Service Site Creation  <br/> |Create a website using Self-Service Site Creation.  <br/> |View Pages, Browse User Information, Open  <br/> |Read, Contribute, Edit, Design, Full Control  <br/> |
|View Pages  <br/> |View pages in a website.  <br/> |Open  <br/> |Read, Contribute, Edit, Design, Full Control  <br/> |
|Enumerate Permissions  <br/> |Enumerate permissions on the website, list, folder, document, or list item.  <br/> |Browse Directories, View Pages, Browse User Information, Open  <br/> |Full Control  <br/> |
|Browse User Information  <br/> |View information about users of the website.  <br/> |Open  <br/> |All  <br/> |
|Manage Alerts  <br/> |Manage alerts for all users of the website.  <br/> |View Items, View Pages, Open, Create Alerts  <br/> |Full Control  <br/> |
|Use Remote Interfaces  <br/> |Use SOAP, Web DAV, the Client Object Model, or SharePoint Designer 2013 interfaces to access the website.  <br/> |Open  <br/> |All  <br/> |
|Use Client Integration Features  <br/> |Use features that launch client applications. Without this permission, users must work on documents locally and then upload their changes.  <br/> |Use Remote Interfaces, Open, View Items  <br/> |All  <br/> |
|Open  <br/> |Enables users to open a website, list, or folder to access items inside that container.  <br/> |None  <br/> |All  <br/> |
|Edit Personal User Information  <br/> |Enables users to change their own user information, such as adding a picture.  <br/> |Browse User Information, Open  <br/> |Contribute, Edit, Design, Full Control  <br/> |
   
### Personal permissions

|**Permission**|**Description**|**Dependent permissions**|**Included in these permission levels by default**|
|:-----|:-----|:-----|:-----|
|Manage Personal Views  <br/> |Create, change, and delete personal views of lists.  <br/> |View Items, View Pages, Open  <br/> |Contribute, Edit, Design, Full Control  <br/> |
|Add/Remove Personal Web Parts  <br/> |Add or remove personal Web Parts on a Web Part page.  <br/> |View Items, View Pages, Open, Update Personal Web Parts  <br/> |Contribute, Edit, Design, Full Control  <br/> |
|Update Personal Web Parts  <br/> |Update Web Parts to display personalized information.  <br/> |View Items, View Pages, Open  <br/> |Contribute, Edit, Design, Full Control  <br/> |
   
## See also
<a name="section2"> </a>

#### Other Resources

[Manage permissions for a web application in SharePoint Server](/SharePoint/administration/manage-permissions-for-a-web-application)

