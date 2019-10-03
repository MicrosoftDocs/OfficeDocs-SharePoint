---
title: "Manage web parts in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 9/19/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 39928a90-e197-4755-af49-130e1ba6f5e5
description: "Helps you prepare to manage security for web parts pages and controls that are used with SharePoint Server."
---

# Manage web parts in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
In SharePoint Server, a web parts page is a collection of web parts that combines list data, timely information, or useful graphics into a dynamic web page. The layout and content of a web parts page can be set for all users and then, optionally, personalized for individual users. A site owner or a site member with the appropriate permissions can create and customize web parts pages by using a browser to add, reconfigure, or remove web parts.
  
You can use web parts on web parts pages, wiki pages, content pages, and publishing pages.
  
The web parts infrastructure in SharePoint Server exists on a layer above the ASP.NET web parts infrastructure. To effectively protect SharePoint sites, server administrators must be familiar with security guidelines and best practices for ASP.NET. For more information, see [Security Guidelines: ASP.NET](https://go.microsoft.com/fwlink/p/?LinkId=103423).
  
> [!NOTE]
> The apps for SharePoint add functionality to a site. Site owners can add apps for SharePoint to SharePoint sites so that they and other users of the site can use the application. For more information, see [Add apps for SharePoint to a SharePoint site](../administration/add-apps-for-sharepoint-to-a-sharepoint-site.md). 
  
## Security for web parts pages and controls

Protecting web parts pages and controls is a collaborative effort. Developers, site administrators, and server administrators must work together to improve security for web parts and web parts pages. Developers should validate Web Part input to prevent server attacks. Server administrators must configure Internet Information Services (IIS) to use an appropriate authentication method. 
  
Server administrators also configure and deploy web parts solutions to a web server or web farm. After the solution is deployed, site administrators or server administrators define the permission levels and permissions that allow access to web parts pages.
  
The following table shows the security roles that are responsible for configuring permissions on Web Parts pages and Web Parts.
  
**Table: Security roles to configure Web Parts and Web Parts pages**

|**Role**|**Category**|**Applies to**|**Description**|**Recommended guidelines**|
|:-----|:-----|:-----|:-----|:-----|
|Developer  <br/> |Input Validation  <br/> |Web Part code  <br/> |Input validation refers to how your application filters, scrubs, or rejects input before additional processing. This includes verification that the input that your application receives is valid and safe.  <br/> |[Building Secure ASP.NET Pages and Controls](https://go.microsoft.com/fwlink/p/?LinkId=103424) <br/> [Creating Web Parts For SharePoint](https://go.microsoft.com/fwlink/p/?LinkId=274097) <br/> |
|Server administrator  <br/> |Authentication  <br/> |IIS  <br/> |Authentication is the process where an entity validates the identity of another entity, typically through credentials such as a user name and password.  <br/> |[Plan for user authentication methods in SharePoint Server](../security-for-sharepoint-server/plan-user-authentication.md) <br/> |
|Site administrator/ Server administrator  <br/> |Authorization  <br/> |Site collections  <br/> |Authorization is the process that provides access controls for Web sites, lists, folders, or items by determining which users can perform specific actions on a given object. The authorization process assumes that the user has already been authenticated.  <br/> |[Authorization and Authentication](https://go.microsoft.com/fwlink/p/?LinkId=103428) <br/> |
|Server administrator  <br/> |Configuration Management  <br/> |.NET Framework configuration  <br/> |Configuration management encompasses a broad range of settings that allow an administrator to manage the Web application and its environment. These settings are stored in XML configuration files, some of which control computer-wide settings, while others control application-specific configurations. You can define special security constraints in configuration files and computer-level code access security permissions.  <br/> |[Code Access Security](https://go.microsoft.com/fwlink/p/?LinkId=274098) <br/> [Microsoft Windows SharePoint Services and Code Access Security](https://go.microsoft.com/fwlink/p/?LinkId=103436) <br/> [Using Code Access Security with ASP.NET](https://go.microsoft.com/fwlink/p/?LinkId=103438) <br/> |
   
Thank you to Waqas Sarwar, Microsoft MVP, for providing the following article about web part security in SharePoint Server 2016, [SharePoint 2016 Central Admin - Security - Manage Web Part security](https://krossfarm.com/?p=1483).
  
The following articles about managing web parts in SharePoint Server are available in this section:
  
|**Content**|**Description**|
|:-----|:-----|
|[Configure and deploy web parts in SharePoint Server](configure-and-deploy-web-parts.md) <br/> |How to secure and deploy web parts in SharePoint Server.  <br/> |
|[Edit existing web parts in SharePoint Server](edit-existing-web-parts-in-sharepoint.md) <br/> |How to edit web parts and web part properties in SharePoint Server,  <br/> |
   
## See also

#### Concepts

[Configure and deploy web parts in SharePoint Server](configure-and-deploy-web-parts.md)
  
[Edit existing web parts in SharePoint Server](edit-existing-web-parts-in-sharepoint.md)
  
[Security for SharePoint Server](../security-for-sharepoint-server/security-for-sharepoint-server.md)
  
[Plan for user authentication methods in SharePoint Server](../security-for-sharepoint-server/plan-user-authentication.md)
#### Other Resources

[Add, edit, minimize, or delete a Web Part from a page](https://support.office.com/en-us/article/Add-edit-minimize-or-delete-a-Web-Part-from-a-page-362b1684-ad95-4a53-b826-443d8d9bdee0)
  
[Using web parts on pages](https://support.office.com/en-us/article/Using-web-parts-on-pages-336e8e92-3e2d-4298-ae01-d404bbe751e0?ui=en-US&amp;rs=en-US&amp;ad=US)

