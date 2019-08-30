---
title: "The Machine Translation Service is not running when it should be running (SharePoint Server)"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
audience: ITPro
ms.topic: troubleshooting
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: f140e0ad-07e4-42f8-a198-54d800355698
description: "Learn how to resolve the SharePoint Health Analyzer rule: The Machine Translation Service is not running when it should be running, for SharePoint Server."
---

# The Machine Translation Service is not running when it should be running (SharePoint Server)

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
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

[Default timer jobs in SharePoint Server 2019](default-timer-jobs-in-sharepoint-server-2019.md)
#### Other Resources

[Default timer jobs in SharePoint Server 2016](default-timer-jobs-in-sharepoint-server-2016.md)

[Default timer jobs in SharePoint 2013](default-timer-jobs-in-sharepoint-2013.md)

