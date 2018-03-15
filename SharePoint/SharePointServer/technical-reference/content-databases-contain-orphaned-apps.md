---
title: "Content databases contain orphaned Apps (SharePoint Server)"
ms.author: stevhord
author: bentoncity
manager: pamgreen
ms.date: 2/22/2018
ms.audience: ITPro
ms.topic: troubleshooting
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: f6012bb0-04c1-4c9c-a4e6-0f45133f2da0
description: "Summary: Learn how to resolve the SharePoint Health Analyzer ruleContent databases contain orphaned Appsin SharePoint Server 2016 and SharePoint Server 2013."
---

# Content databases contain orphaned Apps (SharePoint Server)

 **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "Content databases contain orphaned Apps" in SharePoint Server 2016 and SharePoint Server 2013. 
  
 **Rule Name:** Content databases contain orphaned Apps. 
  
 **Summary:** In some situations, a content database that is used by SharePoint Server may become corrupted. The corrupted database may contain orphaned apps. Orphaned apps are not accessible, which causes unnecessary resource and license consumption and may result in failures in SharePoint upgrade. 
  
 **Cause:** There are orphaned apps in the content databases. 
  
 **Resolution: Remove the orphaned apps.**
  
-  The content database has orphaned apps on a site collection. Remove these apps. For more information, see [Remove app for SharePoint instances from a SharePoint site](../administration/remove-app-for-sharepoint-instances-from-a-sharepoint-site.md).
    
## See also

#### Concepts

[Install and manage apps for SharePoint Server](../administration/install-and-manage-apps-for-sharepoint-server.md)

