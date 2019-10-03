---
title: "The Visio Graphics Service has a minimum cache age setting that will adversely impact performance ((SharePoint Server)"
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
ms.assetid: 062b6ff7-a4ee-408f-811e-fdba45ca3c08
description: "Learn how to resolve the SharePoint Health Analyzer rule: The Visio Graphics Service has a minimum cache age setting that will adversely impact performance, for SharePoint Server."
---

# The Visio Graphics Service has a minimum cache age setting that will adversely impact performance ((SharePoint Server)

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
 **Rule Name:** The Visio Graphics Service has a minimum cache age setting that will adversely impact performance 
  
 **Summary:** The Visio Graphics Service has a minimum cache age setting that will adversely affect performance. If the **Minimum Cache Age** setting is shorter than 5 minutes, it might result in large processor and network load of the Visio Graphics Service and SharePoint Server, decreasing the expected performance of both. However, increasing this value means that users will not see their data-connected diagrams refreshing as frequently. 
  
 **Cause:** The **Minimum Cache Age** setting was set shorter than 5 minutes. 
  
 **Resolution: Increase the value of the Minimum Cache Age setting**
  
1. Verify that the user account that is performing this procedure is an administrator of the Visio Graphics Service service application.
    
2. In Central Administration, on the Home page, in the **Application Management** section, click **Manage service applications**.
    
3. On the Service Applications page, click the Visio Graphics service application.
    
4. On the Manage the Visio Graphics Service page, click **Global Settings**.
    
5. Ensure that the settings have the values listed in the following table. If they do not, type the values in the corresponding text boxes, and then click **OK**.
    
|**Setting**|**Value**|
|:-----|:-----|
|**Maximum Web Drawing Size** <br/> |\<= 25 (Megabytes)  <br/> |
|**Minimum Cache Age** <br/> |\>= 5 (Minutes)  <br/> |
|**Maximum Cache Age** <br/> |\<= 60 (Minutes)  <br/> |
|**Maximum Recalc Duration** <br/> |\<= 60 (Seconds)  <br/> |
|**Maximum Cache Size** <br/> |\>= 5120 (Megabytes)  <br/> |
   
    

