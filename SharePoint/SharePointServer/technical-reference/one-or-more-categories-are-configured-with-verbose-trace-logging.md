---
title: "One or more categories are configured with Verbose trace logging (SharePoint Server)"
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
ms.assetid: c78266d8-33de-4edc-94ea-b8110ac8db81
description: "Learn how to resolve the SharePoint Health Analyzer rule: One or more categories are configured with verbose trace logging, for SharePoint Server."
---

# One or more categories are configured with Verbose trace logging (SharePoint Server)

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
 **Rule Name:** One or more categories are configured with Verbose trace logging. 
  
 **Summary:** SharePoint Server writes diagnostic logging information to record activity on the server. The logs contain information that can help you diagnose server problems. This rule occurs when diagnostic logging is set to verbose. The verbose setting is appropriate when you have to diagnose a server problem, but you should turn off verbose logging during normal operations. 
  
 **Cause:** One or more categories of diagnostic logging are set to verbose. 
  
 **Resolution: Reset diagnostic logging to the default level**
  
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
2. On the SharePoint Central Administration website, click **Monitoring**. 
    
3. On the Monitoring page, in the **Reporting** section, click **Configure diagnostic logging**. 
    
4. On the Diagnostic Logging page, in the **Event Throttling** section, in the **Least critical event to report to the event log** list and **Least critical event to report to the trace log** list, select **Reset to default**. 
    
5. Click **OK**.
    

