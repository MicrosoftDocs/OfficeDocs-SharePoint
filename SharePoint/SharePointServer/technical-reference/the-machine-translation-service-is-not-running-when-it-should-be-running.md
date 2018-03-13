---
title: "The Machine Translation Service is not running when it should be running (SharePoint Server)"
ms.author: stevhord
author: bentoncity
manager: pamgreen
ms.date: 8/30/2017
ms.audience: ITPro
ms.topic: troubleshooting
ms.prod: office-online-server
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: f140e0ad-07e4-42f8-a198-54d800355698
description: "Summary: Learn how to resolve the SharePoint Health Analyzer ruleThe Machine Translation Service is not running when it should be running, in SharePoint Server 2016 and SharePoint Server 2013."
---

# The Machine Translation Service is not running when it should be running (SharePoint Server)

 **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "The Machine Translation Service is not running when it should be running", in SharePoint Server 2016 and SharePoint Server 2013. 
  
 **Rule Name:** The Machine Translation Service is not running when it should be running. 
  
 **Summary:** The Machine Translation Service batch mode uses a timer job to pull translation items from the Machine Translation Service database and then assign those translation items to individual application servers. If the timer job doesn't run, items can't be translated. 
  
 **Cause:** The Machine Translation Service timer job isn't enabled. 
  
 **Resolution: Enable the Machine Translation Service timer job.**
  
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
2. On Central Administration , click **Monitoring**.
    
3. On the Job Definitions page, in the list of timer jobs, click **Machine Translation Service Timer Job**.
    
4. On the Edit Timer Job page, in the **Recurring Schedule** section, specify when you want the timer job to run, and then click **Enable**.
    
    The default is every 15 minutes.
    
## See also

#### Concepts

[Timer job reference for SharePoint Server 2016](timer-job-reference-for-sharepoint-server-2016.md)
#### Other Resources

[Timer job reference for SharePoint 2013](timer-job-reference-for-sharepoint-2013.md)

