---
title: "Create a web application in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 2/28/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 121c8d83-a508-4437-978b-303096aa59df

description: "SharePoint Server web applications isolate content for specific types of users within your site collections."
---

# Create a web application in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
The following articles provide information about how to create web applications.
  
 **Introduction**
  
A SharePoint Server web application is composed of an Internet Information Services (IIS) web site that acts as a logical unit for the site collections that you create. Before you can create a site collection, you must first create a Web application. Each web application is represented by a different IIS web site with a unique or shared application pool. You can assign each web application a unique domain name. This helps prevent cross-site scripting attacks. When you create a new web application, you also create a new content database and define the authentication method used to connect to the database. In addition, you define an authentication method to be used by the IIS Web site in SharePoint Server.
  
|**        ![Building blocks](../media/mod_icon_buildingblock_M.png)                 **|**Content**|**Description**|
|:-----|:-----|:-----|
||[Configure Basic authentication for a claims-based Web application](configure-basic-authentication-for-a-claims-based-web-application.md) <br/> |Explains how to configure basic authentication for a web application that uses claims-based authentication in SharePoint Server.  <br/> |
||[Configure Digest authentication for a claims-based Web application](configure-digest-authentication-for-a-claims-based-web-application.md) <br/> |Explains how to configure digest authentication for a web application that uses claims-based authentication in SharePoint Server.  <br/> |
||[Edit general settings on a web application in SharePoint 2013](edit-general-settings-on-a-web-application.md) <br/> |Illustrates how to change general settings for a SharePoint Server web application in Central Administration.  <br/> |
   

