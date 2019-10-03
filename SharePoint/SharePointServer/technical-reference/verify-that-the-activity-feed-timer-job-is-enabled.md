---
title: "Verify that the Activity Feed Timer Job is enabled (SharePoint Server)"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 8/31/2017
audience: ITPro
ms.topic: troubleshooting
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: d04ccc23-89b1-4927-9607-2a1073d67580
description: "Learn how to resolve the SharePoint Health Analyzer rule: Verify that the Activity Feed Timer Job is enabled, for SharePoint Server."
---

# Verify that the Activity Feed Timer Job is enabled (SharePoint Server)

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
 **Rule Name:** Verify that the Activity Feed Timer Job is enabled. 
  
 **Summary:** You must enable the Activity Feed timer job if you want users to receive information about their colleagues, such as updates to profile properties and creation of social tags and notes. 
  
 **Cause:** The Activity Feed timer job is not enabled. 
  
 **Resolution: Enable the Activity Feed timer job**
  
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
2. On the SharePoint Central Administration website, on the Quick Launch, click **Monitoring**. 
    
3. On the Monitoring page, in the **Timer Jobs** section, click **Review job definitions**. 
    
4. On the Job Definitions page, in the list of timer jobs, click **User Profile Service Application - Activity Feed Job**. 
    
5. On the Edit Timer Job page, in the **Recurring Schedule** section, specify when you want the timer job to run, and then click **Enable**.
    
## See also

#### Concepts

[Default timer jobs in SharePoint Server 2019](default-timer-jobs-in-sharepoint-server-2019.md)
#### Other Resources

[Default timer jobs in SharePoint Server 2016](default-timer-jobs-in-sharepoint-server-2016.md)

[Default timer jobs in SharePoint 2013](default-timer-jobs-in-sharepoint-2013.md)

