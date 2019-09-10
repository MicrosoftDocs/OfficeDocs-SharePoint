---
title: "The settings for the Machine Translation Service are not within the recommended limits (SharePoint Server)"
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
ms.assetid: eb5d2d46-8bf6-43d7-add0-e9d61290a4d0
description: "Learn how to resolve the SharePoint Health Analyzer rule: The settings for the Machine Translation Service are not within the recommended limits, for SharePoint Server."
---

# The settings for the Machine Translation Service are not within the recommended limits (SharePoint Server)

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
 **Rule Name:** The settings for the Machine Translation Service are not within the recommended limits. 
  
 **Summary:** The throughput of the Machine Translation Service is limited by system resources on the application server. If the values for translation processes and translation throughput are set too high, the overall health of the application server can decrease, and other services on the computer can be affected. Additionally, the Machine Translation Service can experience decreased throughput and more translation failures. 
  
 **Cause:** The settings for the Machine Translation Service are incorrect. 
  
 **Resolution: Change the settings for the Machine Translation Service.**
  
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
2. On the SharePoint Central Administration website, in the **Application Management** section, click **Manage service applications**.
    
3. On the Manage Service Applications page, in the list of service applications, click **Machine Translation Service**.
    
4. In the **Translation Processes** section, type a value that ranges from 1 to 1000 in the **Translation processes** box. The default value for Translation processes is set at 1. 
    

