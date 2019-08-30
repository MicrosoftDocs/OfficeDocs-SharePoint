---
title: "The settings for Word Automation Services are not within the recommended limits (SharePoint Server)"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 8/30/2017
audience: ITPro
ms.topic: troubleshooting
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 45d9570f-59d7-4f6b-b8e1-18868b27b0bc
description: "Learn how to resolve the SharePoint Health Analyzer ruleThe settings for Word Automation Services are not within the recommended limits, in SharePoint Server."
---

# The settings for Word Automation Services are not within the recommended limits (SharePoint Server)

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
 **Rule Name:** The settings for Word Automation Services are not within the recommended limits. 
  
 **Summary:** The throughput of Word Automation Services is limited by system resources on the application server. If the values for conversion processes and conversion throughput are set too high, the overall health of the application server can degrade, and other services on the computer can be affected. Additionally, Word Automation Services can experience decreased throughput and more conversion failures. 
  
 **Cause:** The settings for Word Automation Services are incorrect. 
  
 **Resolution: Change the settings for Word Automation Services.**
  
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
2. On the SharePoint Central Administration website, in the **Application Management** section, click **Manage service applications**.
    
3. On the Manage Service Applications page, in the list of service applications, click **Word Automation Services**.
    
4. In the **Conversion Processes** section, type a value that ranges from 1 to 1000 in the **Conversion processes** text box. The default conversion processes is set at 1. 
    
5. In the **Conversion Throughput** section, type a value that ranges from 1 to 59 in the **Frequency with which to start conversions (minutes)** text box, and a value that ranges from 1 to 1000 in the **Number of conversions to start (per conversion process)** text box, and then click **OK**. The default conversion throughput is set at 15.
    

