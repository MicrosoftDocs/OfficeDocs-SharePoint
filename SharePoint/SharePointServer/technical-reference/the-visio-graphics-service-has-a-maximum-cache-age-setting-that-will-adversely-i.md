---
title: "The Visio Graphics Service has a maximum cache age setting that will adversely impact performance (SharePoint Server)"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 8/30/2017
audience: ITPro
ms.topic: troubleshooting
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 28b06934-933b-4899-a7a6-707eb0516552
description: "Learn how to resolve the SharePoint Health Analyzer rule: The Visio Graphics Service has a maximum cache age setting that will adversely impact performance, for SharePoint Server."
---

# The Visio Graphics Service has a maximum cache age setting that will adversely impact performance (SharePoint Server)
[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
 **Rule Name:** The Visio Graphics Service has a maximum cache age setting that will adversely impact performance 
  
 **Summary:** The Visio Graphics Service has a maximum cache age setting that will adversely impact performance. If the **Maximum Cache Age** setting is longer than 60 minutes it might result in a large memory load of the Visio Graphics Service. 
  
 **Cause:** The **Maximum Cache Age** setting was set greater than 60 minutes. 
  
 **Resolution: Reduce the value of the Maximum Cache Age setting**
  
1. Verify that the user account that is performing this procedure is an administrator of the Visio Graphics Service service application.
    
2. In Central Administration, on the Home page, in the **Application Management** section, click **Manage service applications**.
    
3. On the Service Applications page, click the Visio Graphics service application.
    
4. On the Manage the Visio Graphics Service page, click **Global Settings**.
    
5. Ensure that the settings have the values that are listed in the following table. If they do not, type the value in the corresponding text box and then click **OK**.
    
|**Setting**|**Value**|
|:-----|:-----|
|**Maximum Web Drawing Size** <br/> |\<= 25 (Megabytes)  <br/> |
|**Minimum Cache Age** <br/> |\>= 5 (Minutes)  <br/> |
|**Maximum Cache Age** <br/> |\<= 60 (Minutes)  <br/> |
|**Maximum Recalc Duration** <br/> |\<= 60 (Seconds)  <br/> |
|**Maximum Cache Size** <br/> |\>= 5120 (Megabytes)  <br/> |
   
    

