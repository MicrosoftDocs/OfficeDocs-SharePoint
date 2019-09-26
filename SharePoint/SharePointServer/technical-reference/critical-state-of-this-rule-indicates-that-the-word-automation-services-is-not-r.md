---
title: "Critical state of this rule indicates that the Word Automation Services is not running when it should be running (SharePoint Server)"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 8/28/2017
audience: ITPro
ms.topic: troubleshooting
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: e00cc8ed-8a01-4928-9175-49efe03288a1
description: "Learn how to resolve the SharePoint Health Analyzer rule: Critical state of this rule indicates that the Word Automation Services is not running when it should be running, for SharePoint Server."
---

# Critical state of this rule indicates that the Word Automation Services is not running when it should be running (SharePoint Server)

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
 **Rule Name:** Critical state of this rule indicates that the Word Automation Services is not running when it should be running. 
  
 **Summary:** Word Automation Services uses a timer job to pull conversion items from the Word Automation Services database and then assign those conversion items to individual application servers. If the timer job does not run, conversion items cannot start to convert. 
  
 **Cause:** The Word Automation Services timer job is not enabled. 
  
 **Resolution: Enable the Word Automation Services timer job.**
  
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
2. On the SharePoint Central Administration website, click **Monitoring**. 
    
3. On the Monitoring page, in the **Timer Jobs** section, click **Review job definitions**. 
    
4. On the Job Definitions page, in the list of timer jobs, click **Word Automation Services Timer Job**. 
    
5. On the Edit Timer Job page, in the **Recurring Schedule** section, specify when you want the timer job to run, and then click **Enable**.
    

