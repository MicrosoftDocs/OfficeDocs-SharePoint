---
title: "Application pools recycle when memory limits are exceeded (SharePoint Server)"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 2/22/2018
audience: ITPro
ms.topic: troubleshooting
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 9ccce076-f47b-44b8-9ec3-e0dcd46e9985
description: "Learn how to resolve the SharePoint Health Analyzer rule: Application pools recycle when memory limits are exceeded, for SharePoint Server."
---

# Application pools recycle when memory limits are exceeded (SharePoint Server)

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
 **Rule Name:** Application pools recycle when memory limits are exceeded. 
  
 **Summary:** Application pools recycle because memory limits have been enabled and exceeded. Recycling based on memory limits is not usually necessary in a 64-bit environment, and therefore recycling should not be enabled. Unnecessary recycling can result in dropped requests from the recycled worker process and slow performance for end users who are making requests to the new worker process. 
  
 **Cause:** Application pools are configured to recycle when memory limits are exceeded. 
  
 **Resolution: Change the application pool recycling settings in Internet Information Services (IIS).**
  
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
2. Identify the server on which this event occurs. On the SharePoint Central Administration website, in the **Monitoring** section, click **Review problems and solutions**, and then find the name of the server in the **Failing Servers** column. If there are multiple failing servers in a server farm, you must repeat the following steps on each failing server. 
    
3. Verify that the user account that is performing the following steps is a member of the Administrators group on the local computer that you identified in the previous step.
    
4. Log on to the server on which this event occurs.
    
5. In Server Manager, click **Tools**, and then click **Internet Information Services (IIS) Manager**.
    
6. In the Internet Information Services management console, in the **Connections** pane, expand the tree view, and then click **Application Pools**.
    
7. In the **Application Pools** list, right-click the application pool on which you want to disable the memory limits, and then click **Recycling**.
    
8. In the **Edit Application Pool Recycling Settings** dialog box, in the **Memory Based Maximums** section, clear the **Virtual memory usage (in KB)** and **Private memory usage (in KB)** check boxes, and then click **Next**. 
    
9. In the **Recycling Events to Log** dialog box, click **Finish**.
    
## See also

#### Other Resources

[Recycling Settings for an Application Pool \<recycling\>](http://go.microsoft.com/fwlink/?LinkID=761158&amp;clcid=0x409)

