---
ms.date: 03/13/2018
title: "The timer service failed to recycle (SharePoint Server)"
ms.reviewer: 
ms.author: serdars
author: SerdarSoysal
manager: serdars
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: troubleshooting
ms.service: sharepoint-server-itpro
ms.localizationpriority: medium
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 88878bbd-e26e-4fed-8f2a-40a81fb4d528
description: "Learn how to resolve the SharePoint Health Analyzer rule: The timer service failed to recycle, for SharePoint Server."
---

# The timer service failed to recycle (SharePoint Server)

[!INCLUDE[appliesto-2013-2016-2019-SUB-xxx-md](../includes/appliesto-2013-2016-2019-SUB-xxx-md.md)]
  
 **Summary:** The last attempt to recycle the timer service failed. More than half of the attempts during the past week have also failed. 
  
 **Cause:** The Timer Service Recycle job conflicts with other long-running timer jobs. 
  
 **Resolution: Change the schedule for the Timer Service Recycle job so that it does not conflict with other long-running timer jobs.**
  
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
2. On the SharePoint Central Administration website, click **Monitoring**.
    
3. On the Monitoring page, in the **Timer Jobs** section, click **Review job definitions**.
    
4. On the Job Definitions page, click **Timer Service Recycle**.
    
5. On the Edit Timer Job page, change the schedule so that it does not conflict with other long-running timer jobs, and then click **OK**. The default setting is to run daily at 6 AM.
    
For more information, see [Default timer jobs in SharePoint Server 2019](default-timer-jobs-in-sharepoint-server-2019.md), [Default timer jobs in SharePoint Server 2016](default-timer-jobs-in-sharepoint-server-2016.md), or [Default timer jobs in SharePoint 2013](default-timer-jobs-in-sharepoint-2013.md).
  


