---
title: "One or more services have started or stopped unexpectedly (SharePoint Server)"
ms.reviewer: 
ms.author: serdars
author: SerdarSoysal
manager: serdars
ms.date: 8/31/2017
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: troubleshooting
ms.prod: sharepoint-server-itpro
ms.localizationpriority: medium
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: f91de311-e531-4a15-bcc4-b4af01774e0b
description: "Learn how to resolve the SharePoint Health Analyzer rul: eOne or more services have started or stopped unexpectedly, for SharePoint Server."
---

# One or more services have started or stopped unexpectedly (SharePoint Server)

[!INCLUDE[appliesto-2013-2016-2019-SUB-xxx-md](../includes/appliesto-2013-2016-2019-SUB-xxx-md.md)]
  
 **Rule Name:** One or more services have started or stopped unexpectedly. 
  
 **Summary:** A critical service required for the SharePoint farm to function is not running. 
  
 **Cause:** One or more critical services are not running on the specified server. 
  
 **Resolution: Start the service that is not running**
  
1. Verify that the user account that is performing this procedure is a member of the Administrators group on the local computer.
    
2. In Server Manager, click **Tools**, and then click **Services**.
    
3. Right-click the service that you want to start, and then click **Start**.
    

