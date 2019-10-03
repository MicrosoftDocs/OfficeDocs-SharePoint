---
title: "Plan site permissions in SharePoint Server"
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
ms.assetid: c1ffc9a1-29ec-4482-b391-f2e0c7f5d1b6
description: "Learn about how to plan site permissions for SharePoint Server to provide secure access to sites and content."
---

# Plan site permissions in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
This article helps you plan access control at the site collection, site, subsite, and site content (list or library, folder, item or document) levels.
  
This article does not address planning the security of your entire server or server farm. For more information about planning other aspects of security, such as authentication methods and authentication modes, see [Plan authentication in SharePoint Server](/SharePoint/install/install).
  
## Plan for site permissions
<a name="section4"> </a>

When you create permissions, you must balance the ease of administration and performance against the requirement to control access to individual items. If you use fine-grained permissions extensively, you will spend more time managing the permissions, and users may experience slower performance when they try to access site content. 
  
Use the following guidelines to plan site permissions:
  
1. Follow the principle of least-privileged: Users should have only the permission levels or individual permissions they must have to perform their assigned tasks.
    
2. Use standard groups (such as Members, Visitors, and Owners) and control permissions at the site level.
    
  - Make most users members of the Members or Visitors groups. By default, users in the Members group can contribute to the site by adding or removing items or documents, but cannot change the structure, site settings, or appearance of the site. The Visitors group has read-only access to the site, which means that they can see pages and items, and open items and documents, but cannot add or remove pages, items, or documents.
    
  - Limit the number of people in the Owners group. Only those users that you trust to change the structure, settings, or appearance of the site should be in the Owners group.
    
3. Use permission levels instead of assign individual permissions.
    
> [!NOTE]
>  You can create additional SharePoint groups and permission levels if that you must have more control over the actions that the users can take. For example, if you do not want the Read permission level on a specific subsite to include the Create Alerts permission, break the inheritance and customize the Read permission level for that subsite. >  SharePoint Foundation 2013 and SharePoint Server use **Check Permissions** to determine a user or group's permissions on all resources in a site collection. You can now find both the user's directly assigned permissions and the permissions assigned to any groups of which the user is a member by checking permissions for a specific site or site content. 
  
## Plan for permission inheritance
<a name="section5"> </a>

It is much easier to manage permissions when there is a clear hierarchy of permissions and inherited permissions. It becomes more difficult when some lists in a site have fine-grained permissions applied, and when some sites have subsites with unique permissions and others with inherited permissions. As much as possible, arrange sites and subsites, and lists and libraries so they can share most permissions. Separate sensitive data into their own lists, libraries, or subsites.
  
For example, it's much easier to manage a site that has permission inheritance as described in the following table. 
  
|**Securable object**|**Description**|**Unique or inherited permissions**|
|:-----|:-----|:-----|
|SiteA  <br/> |Group home page  <br/> |Unique  <br/> |
|SiteA/SubsiteA  <br/> |Sensitive group  <br/> |Unique  <br/> |
|SiteA/SubsiteA/ListA  <br/> |Sensitive data  <br/> |Unique  <br/> |
|SiteA/SubsiteA/LibraryA  <br/> |Sensitive documents  <br/> |Unique  <br/> |
|SiteA/SubsiteB  <br/> |Group shared project information  <br/> |Inherited  <br/> |
|SiteA/SubsiteB/ListB  <br/> |Non-sensitive data  <br/> |Inherited  <br/> |
|SiteA/SubsiteB/LibraryB  <br/> |Non-sensitive documents  <br/> |Inherited  <br/> |
   
However, it is not as easy to manage a site that has permission inheritance as shown in the following table. 
  
|**Securable object**|**Description**|**Unique or inherited permissions**|
|:-----|:-----|:-----|
|SiteA  <br/> |Group home page  <br/> |Unique  <br/> |
|SiteA/SubsiteA  <br/> |Sensitive group  <br/> |Unique  <br/> |
|SiteA/SubsiteA/ListA  <br/> |Non-sensitive data  <br/> |Unique, but same permissions as SiteA  <br/> |
|SiteA/SubsiteA/LibraryA  <br/> |Non-sensitive documents, but with one or two sensitive documents  <br/> |Inherited, with unique permissions at the document level  <br/> |
|SiteA/SubsiteB  <br/> |Group shared project information  <br/> |Inherited  <br/> |
|SiteA/SubsiteB/ListB  <br/> |Non-sensitive data, but with one or two sensitive items  <br/> |Inherited, with unique permissions at the item level  <br/> |
|SiteA/SubsiteB/LibraryB  <br/> |Non-sensitive documents, but with a special folder that contain sensitive documents  <br/> |Inherited, with unique permissions at the folder and document level  <br/> |
   

