---
title: "The Visio Graphics Service has a maximum cache size setting that may adversely impact performance ((SharePoint Server)"
ms.reviewer: 
ms.author: serdars
author: SerdarSoysal
manager: serdars
ms.date: 8/30/2017
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: troubleshooting
ms.prod: sharepoint-server-itpro
ms.localizationpriority: medium
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 5e242415-c288-48c7-a373-29acc359ad95
description: "Learn how to resolve the SharePoint Health Analyzer rule: The Visio Graphics Service has a Maximum Cache Size setting that will adversely impact performance, for SharePoint Server."
---

# The Visio Graphics Service has a maximum cache size setting that may adversely impact performance ((SharePoint Server)

[!INCLUDE[appliesto-2013-2016-2019-SUB-xxx-md](../includes/appliesto-2013-2016-2019-SUB-xxx-md.md)] 
  
 **Rule Name:** The Visio Graphics Service has a Maximum Cache Size setting that will adversely impact performance 
  
 **Summary:** The Visio Graphics Service has a maximum Cache size setting that will adversely affect performance. If the **Maximum Cache Size** setting is smaller than 1024 MB, it might decrease the expected performance of the Visio Graphics Service. 
  
 **Cause:** The **Maximum Cache Size** setting was set smaller than 1024 MB. 
  
 **Resolution: Increase the value of the Maximum Cache Size setting**
  
1. Verify that the user account that is performing this procedure is an administrator of the Visio Graphics Service service application. 
    
2. In Central Administration, on the Home page, in the **Application Management** section, click **Manage service applications**.
    
3. On the Service Applications page, click the Visio Graphics service application.
    
4. On the Manage the Visio Graphics Service page, click **Global Settings**.
    
5. Ensure that the settings have the values that are listed in the following table. If they do not, type the value in the corresponding text box and click **OK**.
    
|**Setting**|**Value**|
|:-----|:-----|
|**Maximum Web Drawing Size** <br/> |\<= 25 (Megabytes)  <br/> |
|**Minimum Cache Age** <br/> |\>= 5 (Minutes)  <br/> |
|**Maximum Cache Age** <br/> |\<= 60 (Minutes)  <br/> |
|**Maximum Recalc Duration** <br/> |\<= 60 (Seconds)  <br/> |
|**Maximum Cache Size** <br/> |\>= 5120 (Megabytes)  <br/> |
   
    

