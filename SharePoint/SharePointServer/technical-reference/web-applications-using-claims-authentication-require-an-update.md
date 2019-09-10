---
title: "Web Applications using Claims authentication require an update (SharePoint Server)"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 12/5/2017
audience: ITPro
ms.topic: troubleshooting
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 9d2d8945-5a6f-45dc-91bd-b588720ba745
description: "Learn how to resolve the SharePoint Health Analyzer rule: Web Applications using Claims authentication require an update, for SharePoint Server."
---

# Web Applications using Claims authentication require an update (SharePoint Server)

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
 **Rule Name:** Web Applications using Claims authentication require an update. 
  
 **Event ID:** None 
  
 **Summary:** Web applications that use claims-based authentication are at risk for a potential security vulnerability that might allow users to elevate privileges. Web servers that host Web applications that use claims-based authentication are potentially vulnerable. 
  
 **Cause:** This can happen when you deploy a Microsoft ASP.NET 2.0-based Web application to a Web site that is hosted on a server running SharePoint Server and you have Internet Information Services (IIS) 7.0 or IIS 7.5 running in Integrated mode on the server. 
  
If you deploy partially trusted Web Parts or create external lists on the SharePoint site, these Web Parts or external lists can have more permissions than they should have. This issue might create a security risk on the SharePoint site. For example, these Web Parts or external lists may unexpectedly generate database requests or HTTP requests.
  
This issue occurs because of a change in the ASP.NET 2.0 authentication component. The change causes the partially trusted Web Parts or external lists to impersonate the application pool account. Therefore, the Web Parts have full permission to access the SharePoint site.
  
 **Resolution: Install the update**
  
- For more information about this update, see [Knowledge Base article 979917](https://support.microsoft.com/kb/979917).
    

