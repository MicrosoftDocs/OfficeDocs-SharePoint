---
title: "One or more web applications are configured to use Windows Classic authentication (SharePoint Server)"
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
ms.assetid: cab37e59-7ae1-403a-8fa2-37fe0701961e
description: "Learn how to resolve the SharePoint Health Analyzer rule: One or more web applications are configured to use Windows Classic authentication, for SharePoint Server."
---

# One or more web applications are configured to use Windows Classic authentication (SharePoint Server)

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
 **Rule Name:** One or more web applications are configured to use Windows Classic authentication. 
  
 **Summary:** This health rule is triggered when at least one Web application is configured to use Windows Classic authentication mode. Windows Classic authentication is deprecated in SharePoint Server. We recommend that you migrate to claims-based authentication, because many of the features in SharePoint Server require the claims-based authentication mode. 
  
 **Cause:** Web applications are configured to use Windows Classic authentication mode. 
  
 **Resolution: Migrate Web applications from classic mode to claims-based authentication.**
  
- You have to migrate Web applications from classic mode to claims-based authentication. For more information, see [Migrate from classic-mode to claims-based authentication in SharePoint Server](/previous-versions/office/sharepoint-server-2010/gg251985(v=office.14)).
    

