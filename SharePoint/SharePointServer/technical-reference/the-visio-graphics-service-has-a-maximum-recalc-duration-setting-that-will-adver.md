---
title: "The Visio Graphics Service has a maximum recalc duration setting that will adversely impact user perceived performance ((SharePoint Server)"
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
ms.assetid: 20e1e0c3-7d5c-489c-a588-a11b30adffb9
description: "Learn how to resolve the SharePoint Health Analyzer rule: The Visio Graphics Service has a maximum recalc duration setting that will adversely impact user perceived performance, for SharePoint Server."
---

# The Visio Graphics Service has a maximum recalc duration setting that will adversely impact user perceived performance ((SharePoint Server)

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
 **Rule Name:** The Visio Graphics Service has a maximum recalc duration setting that will adversely impact user perceived performance 
  
 **Summary:** The Visio Graphics Service has a maximum recalculation duration setting that will adversely affect performance. If the **Maximum Recalc Duration** setting is longer than 60 seconds, it might result in large processor load of the Visio Graphics Service and SharePoint Server, decreasing the expected performance of both. 
  
A shorter duration increases performance by only allowing simple data-connected diagrams to be recalculated by the server, minimizing CPU and memory usage. A longer duration allows the recalculation of more complex data-connected diagrams while using more CPU cycles and memory. The default duration is 60 seconds.
  
 **Cause:** The **Maximum Recalc Duration** setting was set longer than 60 seconds. 
  
 **Resolution: Decrease the value of the Maximum Recalc Duration setting**
  
1. Verify that the user account that is performing this procedure is an administrator of the Visio Graphics Service service application. 
    
2. In Central Administration, in the **Application Management** section, click **Manage service applications**.
    
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
   
    

