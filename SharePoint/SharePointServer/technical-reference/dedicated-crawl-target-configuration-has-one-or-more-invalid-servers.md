---
title: "Dedicated crawl target configuration has one or more invalid servers (SharePoint Server)"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 8/29/2017
audience: ITPro
ms.topic: troubleshooting
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 80521ae8-be93-4d1c-9956-5f4bed1ac4a7
description: "Learn how to resolve the SharePoint Health Analyzer rule: Dedicated crawl target configuration has one or more invalid servers, for SharePoint Server."
---

# Dedicated crawl target configuration has one or more invalid servers (SharePoint Server)

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
 **Rule Name:** Dedicated crawl target configuration has one or more invalid servers. 
  
 **Summary:** Dedicated crawl target configuration has one or more invalid servers. This may degrade search crawl performance. 
  
 **Cause:** The URI is incorrect, or the server is not joined with a valid role to the SharePoint farm. 
  
 **Resolution: Make sure the uniform resource identifier (URI) is correct, and the server is joined with a valid role to the SharePoint farm.**
  
1. Make sure that the URI is correct. A valid URI meets the following criteria:
    
  - The host portion of the URI should be the name of a server that has joined the SharePoint farm.
    
  - The URI Scheme should be HTTP.
    
  - The URI must not contain an absolute path.
    
    For more information, see [URI class](https://go.microsoft.com/fwlink/p/?LinkID=193513).
    
2. Make sure that the server is joined with a valid role to the SharePoint farm. The server can be any of the following:
    
  - Front-end
    
  - Application server
    
  - Distributed cache
    
  - Search
    
  - Custom
    
  - Single-server farm or a stand-alone server in the SharePoint farm
    
For more information, see [Overview of MinRole Server Roles in SharePoint Server 2016](../install/overview-of-minrole-server-roles-in-sharepoint-server.md) and [Description of MinRole and associated services in SharePoint Server 2016](../administration/description-of-minrole-and-associated-services-in-sharepoint-server-2016.md).
  
## See also

#### Concepts

[Add a server to a SharePoint Server 2016 farm](../install/add-a-server-to-a-sharepoint-server-2016-farm.md)

