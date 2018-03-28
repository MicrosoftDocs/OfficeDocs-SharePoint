---
title: "Verify that the Activity Feed Timer Job is enabled (SharePoint Server)"
ms.author: stevhord
author: bentoncity
manager: pamgreen
ms.date: 8/31/2017
ms.audience: ITPro
ms.topic: troubleshooting
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: d04ccc23-89b1-4927-9607-2a1073d67580
description: "Summary: Learn how to resolve the SharePoint Health Analyzer ruleVerify that the Activity Feed Timer Job is enabled, for SharePoint Server 2016 and SharePoint Server 2013."
---

# Verify that the Activity Feed Timer Job is enabled (SharePoint Server)

 **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "Verify that the Activity Feed Timer Job is enabled", for SharePoint Server 2016 and SharePoint Server 2013. 
  
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

[Timer job reference for SharePoint Server 2016](timer-job-reference-for-sharepoint-server-2016.md)
#### Other Resources

[Timer job reference for SharePoint 2013](timer-job-reference-for-sharepoint-2013.md)

