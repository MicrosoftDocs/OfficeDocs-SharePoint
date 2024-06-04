---
title: "One or more app domains for web applications aren't configured correctly (SharePoint Server)"
ms.reviewer: 
ms.author: serdars
author: SerdarSoysal
manager: serdars
ms.date: 8/31/2017
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: troubleshooting
ms.service: sharepoint-server-itpro
ms.localizationpriority: medium
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 76a4e2e3-7e10-41da-b3a8-fe62e193dc24
description: "Learn how to resolve the SharePoint Health Analyzer rule: One or more app domains for web applications aren't configured correctly, for SharePoint Server."
---

# One or more app domains for web applications aren't configured correctly (SharePoint Server)

[!INCLUDE[appliesto-2013-2016-2019-SUB-xxx-md](../includes/appliesto-2013-2016-2019-SUB-xxx-md.md)] 
  
 **Rule Name:** One or more app domains for web applications aren't configured correctly. 
  
 **Summary:** This health rule checks to see if the multiple app domains feature is enabled by looking at the state of the  _Microsoft.SharePoint.Administration.SPWebService.ContentService.SupportMultipleAppDomains_ property. If this is enabled, the health rule then checks to see if there are multiple web application zones in each web application. If there are, it continues to check if there's an app domain defined for each web application zone. The health rule alert is triggered if the final condition isn't met. It's also triggered if the web application and app domain aren't using the same Internet Information Services (IIS) port binding, web application zone, application pool account, and authentication type. 
  
 **Cause:** The SharePoint Server environment isn't set to use multiple app domains, or the web application is incorrectly configured for multiple web application zones. 
  
 **Resolution:**
  
1. You have to configure the app domains for web applications. For more information, see [Enable apps in AAM or host-header environments for SharePoint 2016](../administration/plan-for-apps-for-sharepoint.md).
