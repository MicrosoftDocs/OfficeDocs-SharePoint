---
title: "Choose administrators and owners for the administration hierarchy in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 8/17/2017
audience: ITPro
ms.topic: get-started-article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 4f5e0b9a-7256-4c00-bc7f-e1735a9f5fbf
description: "Learn about the levels at which you can delegate administration of the SharePoint Server farm."
---

# Choose administrators and owners for the administration hierarchy in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
This article describes the administrator roles that correspond to the SharePoint Server server and site hierarchy. Many people can be involved in managing SharePoint Server. Administration of SharePoint Server occurs at the following levels: 
  
- Server or SharePoint farm 
    
- Shared services
    
- Web application
    
- Sites
    
- Document library or list
    
- Individual items
    
## Levels of administration
<a name="section1"> </a>

Most levels of the server and site hierarchy have a corresponding administration group. The administration groups that have administrative permissions at different levels are described in the following list:
  
- Server or farm level
    
  - **Farm Administrators group** Members of the Farm Administrators group have Full Control permissions to and responsibility for all servers in the server farm. Members can perform all administrative tasks in Central Administration for the server or server farm. They can assign administrators to manage service applications, which are instances of shared services. This group does not have access to individual sites or their content. 
    
  - **Windows Administrators group** Members of the Windows Administrators group on the local server can perform all farm administrator actions. Administrators on the local server can perform additional tasks, such as installing new products or applications, deploying Web Parts and new features to the global assembly cache, creating new Web applications and new Internet Information Services (IIS) Web sites, and starting services. Like farm administrators, members of this group on the local server have no access to site content, by default. 
    
    > [!NOTE]
    > Farm administrators and members of the local Administrators group can take ownership of specific site collections if it is necessary. For example, if a site administrator leaves the organization and a new administrator must be added, the farm administrator or a member of the local Administrators group can take ownership of the site collection to make the change. To take ownership, they can add themselves as the site collection administrator on the **Application Management** page. 
  
- Shared services level
    
  - **Service application administrators** These administrators are designated by the farm administrator. They can configure settings for a specific service application in a farm. However, these administrators cannot create service applications, access any other service applications in the farm, or perform any farm-level operations, such as topology changes. For example, the service application administrator for a Search service application in a farm can configure settings for that Search service application only. 
    
  - **Feature administrators** A feature administrator is associated with a specific feature or features of a service application. These administrators can manage a subset of service application settings, but not the entire service application. For example, a Feature administrator might manage the Audiences feature of the User Profile service application. 
    
- Web application level
    
  - The Web application level does not have a unique administrator group, but farm administrators have control over the Web applications within their scope. Members of the Farm Administrators group and members of the Administrators group on the local server can define a policy to grant individual users permissions at the Web application level. 
    
- Site level
    
  - **Site collection administrators** These administrators have the Full Control permission level on all Web sites in a site collection. They have Full Control access to all site content in that site collection, even if they do not have explicit permissions on that site. They can audit all site content and receive any administrative message. A primary and a secondary site collection administrator can be specified during the creation of a site collection. 
    
  - **Site owners** By default, members of the Owners group for a site have the Full Control permission level on that site. They can perform administrative tasks on the site, and on any list or library within that site. They receive e-mail notifications for events, such as the pending automatic deletion of inactive sites and requests for site access. 
    

