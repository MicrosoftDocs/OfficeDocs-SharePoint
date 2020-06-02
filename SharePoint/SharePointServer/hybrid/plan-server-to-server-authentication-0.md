---
title: "Plan server-to-server authentication"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 6/20/2017
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: concetpual
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- Ent_O365_Hybrid
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
- M365-collaboration
- SPO_Content
ms.assetid: 6951d670-e2a8-4a7e-b3ea-ccc9c00a0ffc
description: "Plan and prepare to configure server-to-server authentication from SharePoint Server to Microsoft 365 for SharePoint hybrid."
---

# Plan server-to-server authentication

[!INCLUDE[appliesto-2013-2016-2019-SPO-md](../includes/appliesto-2013-2016-2019-SPO-md.md)]
  
Server-to-server authentication enables your SharePoint Server farm to consume content and resources from your Microsoft 365 organization. For example, search can be configured to allow federated users to see both SharePoint Server and SharePoint Online search results in a SharePoint Server search portal.
  
The major thing that you need to plan for when configuring server-to-server authentication between SharePoint Server and Microsoft 365 is your web application configuration.
  
## Plan your web application configuration for hybrid server-to-server authentication

This section helps you plan how to configure your SharePoint Server web application to support hybrid functionality.
  
Outbound requests to SharePoint Online can be made from any web application in the on-premises SharePoint farm that uses **Integrated Windows authentication using NTLM**, as shown in the following image.
  
![Claim authentication types for SharePoint hybrid](../media/ClaimAuthenticationTypes.gif)
  
If your existing web application is not configured to use Integrated Windows authentication using NTLM, you must either create a web application or extend your existing web application and configure it to use Integrated Windows authentication using NTLM.
  
If you have to create a new web application to configure for hybrid functionality, you have two choices:
  
- **Extend an existing web application to connect to an existing content database.** This creates a new website in Internet Information Services (IIS) with a unique URL and authentication configuration. The extended web application can be used to access the same site collections and content as the original web application by using the new URL. 
    
    This is the best choice if you want users to go to an enterprise search portal in an existing site collection to use hybrid search.
    
- **Create a new web application and a new content database.** This creates a new web application that has a new, empty content database in which you can create a new site collection with an enterprise search portal. 
    
    This is the best choice if you want users to go to an enterprise search portal in a new site collection to use hybrid search.
    
Integrated Windows authentication using NTLM is required to allow the SharePoint Authentication service to pass user claims to SharePoint Online using OAuth.
  

