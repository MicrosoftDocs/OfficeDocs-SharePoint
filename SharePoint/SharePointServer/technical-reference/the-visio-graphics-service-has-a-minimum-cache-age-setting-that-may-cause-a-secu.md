---
title: "The Visio Graphics Service has a minimum cache age setting that may cause a security issue ((SharePoint Server)"
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
ms.assetid: 4fcd074b-32b1-49b3-9910-5bb174894603
description: "Learn how to resolve the SharePoint Health Analyzer rule: The Visio Graphics Service has a minimum cache age setting that may cause a security issue, for SharePoint Server."
---

# The Visio Graphics Service has a minimum cache age setting that may cause a security issue ((SharePoint Server)

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
 **Rule Name:** The Visio Graphics Service has a minimum cache age setting that may cause a security issue 
  
 **Summary:** Setting **Minimum Cache Age** to 0 minutes may leave the Visio Graphics Service open to a denial of service (DoS) attack. A value of 0 for this setting might lead to large processor and network load of the Visio Graphics Service and SharePoint Server, decreasing the expected performance of both. However, increasing this value means that users will not see their data-connected diagrams refreshing as frequently. 
  
 **Cause:** The **Minimum Cache Age** setting was set to 0 minutes. 
  
 **Resolution: Increase the value of the Minimum Cache Age setting**
  
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
   
    

