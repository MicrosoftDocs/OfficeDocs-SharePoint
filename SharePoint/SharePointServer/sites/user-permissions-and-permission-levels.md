---
title: "On-premises SharePoint Server user permissions and permission levels"
ms.reviewer: WesleyFive
ms.author: serdars
author: SerdarSoysal
manager: serdars
ms.date: 10/18/2023
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-server-itpro
ms.localizationpriority: medium
ms.assetid: ff13b917-5236-48e6-89d5-8c78e61a72a8
description: "Learn about the default permission levels and user permissions in SharePoint Server."
---

# On-premises SharePoint Server user permissions and permission levels

[!INCLUDE[appliesto-2013-2016-2019-SUB-xxx-md](../includes/appliesto-2013-2016-2019-SUB-xxx-md.md)]
  
Default permission levels are predefined sets of permissions that you can assign to individual users, groups of users, or security groups, based on the functional requirements of the users and on security considerations. SharePoint Server permission levels are defined at the site collection level and are inherited from the parent object by default.

Learn about [Sharing and permissions in the SharePoint modern experience in Microsoft 365](../../SharePointOnline/modern-experience-sharing-permissions.md).
    
## Default permission levels
<a name="section1"> </a>

Default permission levels are made up of a set of permissions that enable users to perform a collection of related tasks. SharePoint Server includes seven permission levels. You can customize the permissions contained within five of these permission levels. You can't customize the permissions within the Limited Access and Full Control permission levels.
  
> [!NOTE]
> Although you can't directly edit the Limited Access and Full Control permission levels, you can make individual permissions unavailable for the entire web application, which removes those permissions from the Limited Access and Full Control permission levels. For more information, see [Manage permissions for a web application in SharePoint Server](../administration/manage-permissions-for-a-web-application.md). 
  
The following table lists the default permission levels for team sites in SharePoint Server.
  
| Permission level | Description | Permissions included by default |
|:-----|:-----|:-----|
|View Only  |Enables users to view application pages. The View Only permission level is used for the Excel Services Viewers group. <br> For SharePoint Server 2019 and Subscription Edition, the View Only permission level won't be provided until the “SharePoint Server Enterprise Site Collection features” is activated. | View Application Pages  <br/>  View Items  <br/>  View Versions  <br/>  Create Alerts  <br/>  Use Self Service Site Creation  <br/>  View Pages  <br/>  Browse User Information  <br/>  Use Remote Interfaces  <br/>  Use Client Integration Features  <br/>  Open  |
|Limited Access  |Enables users to access shared resources and a specific asset. Limited Access is designed to be combined with fine-grained permissions to enable users to access a specific list, document library, folder, list item, or document, without enabling them to access the whole site. Limited Access can't be edited or deleted. Note: when sharing a link to a document with all users in your organization, SharePoint will assign the Limited Access permission via a group name "Limited Access System Group" that's applied the first time a user - who doesn't otherwise have permission via the link - accesses the resource   | View Application Pages  <br/>  Browse User Information  <br/>  Use Remote Interfaces  <br/>  Use Client Integration Features  <br/>  Open  |
|Read  |Enables users to view pages and list items, and to download documents.  | Limited Access permissions, plus:  <br/>  View Items  <br/>  Open Items  <br/>  View Versions  <br/>  Create Alerts  <br/>  Use Self-Service Site Creation  <br/>  View Pages  |
|Contribute  |Enables users to manage personal views; edit items and user information; delete versions in existing lists and document libraries; and add, remove, and update personal Web Parts.  | Read permissions, plus:  <br/>  Add Items  <br/>  Edit Items  <br/>  Delete Items  <br/>  Delete Versions  <br/>  Browse Directories  <br/>  Edit Personal User Information  <br/>  Manage Personal Views  <br/>  Add/Remove Personal Web Parts  <br/>  Update Personal Web Parts  |
|Edit  |Enables users to manage lists.  | Contribute permissions, plus:  <br/>  Manage Lists  |
|Design  |Enables users to view, add, update, delete, approve, and customize items or pages in the website.  | Edit permissions, plus:  <br/>  Add and Customize Pages  <br/>  Apply Themes and Borders  <br/>  Apply Style Sheets  <br/>  Override List Behaviors  <br/>  Approve Items  |
|Full Control  |Enables users to have full control of the website.  |All permissions  |
   
If you use a site template other than the team site template, you'll see a different list of default SharePoint permission levels. For example, the following table shows additional permission levels provided with the publishing template.
  
| Permission level | Description | Permissions included by default |
|:-----|:-----|:-----|
|Restricted Read  |View pages and documents. For publishing sites only.  | View Items  <br/>  Open Items  <br/>  View Pages  <br/>  Open  |
|Approve  |Edit and approve pages, list items, and documents. For publishing sites only.  | Contribute permissions, plus:  <br/>  Override List Behaviors  <br/>  Approve Items  |
|Manage Hierarchy  |Create sites; edit pages, list items, and documents; and change site permissions. For Publishing sites only.  | Design permissions minus the Approve Items, Apply Themes and Borders, and Apply Style Sheets permissions, plus:  <br/>  Manage permissions  <br/>  View Web Analytics Data  <br/>  Create Subsites  <br/>  Manage Alerts  <br/>  Enumerate Permissions  <br/>  Manage Web Site  |
   
## User permissions
<a name="section2"> </a>

SharePoint Server includes 33 permissions, which are used in the default permission levels. You can configure which permissions are included in a particular permission level (except for the Limited Access and Full Control permission levels), or you can create a new permission level to contain specific permissions.
  
Permissions are categorized as list permissions, site permissions, and personal permissions, depending on the objects to which they can be applied. For example, site permissions apply to a particular site, list permissions apply only to lists and libraries, and personal permissions apply only to certain objects, such as personal views and private Web Parts. The following tables describe what each permission is used for, the dependent permissions, and the permission levels in which it's included.
  
### List permissions

| Permission | Description | Dependent permissions | Included in these permission levels by default |
|:-----|:-----|:-----|:-----|
|Manage Lists  |Create and delete lists, add or remove columns in a list, and add or remove public views of a list.  |View Items, View Pages, Open  |Edit, Design, Full Control, Manage Hierarchy  |
|Override List Behaviors  |Discard or check-in a document that's checked out to another user, and change or override settings that allow users to read/edit only their own items.  |View Items, View Pages, Open  |Design, Full Control  |
|Add Items  |Add items to lists, and add documents to document libraries.  |View Items, View Pages, Open  |Contribute, Edit, Design, Full Control  |
|Edit Items  |Edit items in lists, edit documents in document libraries, and customize Web Part pages in document libraries.  |View Items, View Pages, Open  |Contribute, Edit, Design, Full Control  |
|Delete Items  |Delete items from a list, and documents from a document library.  |View Items, View Pages, Open  |Contribute, Edit, Design, Full Control  |
|View Items  |View items in lists, and documents in document libraries.  |View Pages, Open  |Read, Contribute, Edit, Design, Full Control  |
|Approve Items  |Approve a minor version of list items or a document.  |Edit Items, View Items, View Pages, Open  |Design, Full Control  |
|Open Items  |View the source of documents with server-side file handlers.  |View Items, View Pages, Open  |Read, Contribute, Edit, Design, Full Control  |
|View Versions  |View past versions of a list item or document.  |View Items, Open Items, View Pages, Open  |Read, Contribute, Edit, Design, Full Control  |
|Delete Versions  |Delete past versions of list items or documents.  |View Items, View Versions, View Pages, Open  |Contribute, Edit, Design, Full Control  |
|Create Alerts  |Create alerts.  |View Items, View Pages, Open  |Read, Contribute, Edit, Design, Full Control  |
|View Application Pages  |View forms, views, and application pages. Enumerate lists.  |Open  |All  |
   
### Site permissions

| Permission | Description | Dependent permissions | Included in these permission levels by default |
|:-----|:-----|:-----|:-----|
|Manage Permissions  |Create and change permission levels on the website and assign permissions to users and groups.  |View Items, Open Items, View Versions, Browse Directories, View Pages, Enumerate Permissions, Browse User Information, Open  |Full Control  |
|View Web Analytics Data  |View reports on website usage.  |View Pages, Open  |Full Control  |
|Create Subsites  |Create subsites such as team sites, Meeting Workspace sites, and Document Workspace sites.  |View Pages, Browse User Information, Open  |Full Control  |
|Manage Web Site  |Grants the ability to perform all administration tasks for the website, and to manage content.  |View Items, Add and Customize Pages, Browse Directories, View Pages, Enumerate Permissions, Browse User Information, Open  |Full Control  |
|Add and Customize Pages  |Add, change, or delete HTML pages or Web Part pages, and edit the website.  |View Items, Browse Directories, View Pages, Open  |Design, Full Control  |
|Apply Themes and Borders  |Apply a theme or borders to the whole website.  |View Pages, Open  |Design, Full Control  |
|Apply Style Sheets  |Apply a style sheet (.css file) to the website.  |View Pages, Open  |Design, Full Control  |
|Create Groups  |Create a group of users that can be used anywhere within the site collection.  |View Pages, Browse User Information, Open  |Full Control  |
|Browse Directories  |Enumerate files and folders in a website by using SharePoint Designer 2013 and Web DAV interfaces.  |View Pages, Open  |Contribute, Edit, Design, Full Control  |
|Use Self-Service Site Creation  |Create a website using Self-Service Site Creation.  |View Pages, Browse User Information, Open  |Read, Contribute, Edit, Design, Full Control  |
|View Pages  |View pages in a website.  |Open  |Read, Contribute, Edit, Design, Full Control  |
|Enumerate Permissions  |Enumerate permissions on the website, list, folder, document, or list item.  |Browse Directories, View Pages, Browse User Information, Open  |Full Control  |
|Browse User Information  |View information about users of the website.  |Open  |All  |
|Manage Alerts  |Manage alerts for all users of the website.  |View Items, View Pages, Open, Create Alerts  |Full Control  |
|Use Remote Interfaces  |Use SOAP, Web DAV, the Client Object Model, or SharePoint Designer 2013 interfaces to access the website.  |Open  |All  |
|Use Client Integration Features  |Use features that launch client applications. Without this permission, users must work on documents locally and then upload their changes.  |Use Remote Interfaces, Open, View Items  |All  |
|Open  |Enables users to open a website, list, or folder to access items inside that container.  |None  |All  |
|Edit Personal User Information  |Enables users to change their own user information, such as adding a picture.  |Browse User Information, Open  |Contribute, Edit, Design, Full Control  |
   
### Personal permissions

| Permission | Description | Dependent permissions | Included in these permission levels by default |
|:-----|:-----|:-----|:-----|
|Manage Personal Views  |Create, change, and delete personal views of lists.  |View Items, View Pages, Open  |Contribute, Edit, Design, Full Control  |
|Add/Remove Personal Web Parts  |Add or remove personal Web Parts on a Web Part page.  |View Items, View Pages, Open, Update Personal Web Parts  |Contribute, Edit, Design, Full Control  |
|Update Personal Web Parts  |Update Web Parts to display personalized information.  |View Items, View Pages, Open  |Contribute, Edit, Design, Full Control  |
   
## See also
<a name="section2"> </a>

#### Other Resources

[Manage permissions for a web application in SharePoint Server](../administration/manage-permissions-for-a-web-application.md)
