---
title: "Immediate translations for the Machine Translation service are disabled (SharePoint Server)"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 12/5/2017
audience: ITPro
ms.topic: troubleshooting
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 987f22e3-53cc-4e6a-93e7-0851af4f31db
description: "Learn how to resolve the SharePoint Health Analyzer rule:Immediate translations for the Machine Translation service are disabled, for SharePoint Server."
---

# Immediate translations for the Machine Translation service are disabled (SharePoint Server)

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
 **Rule Name:** Immediate translations for the Machine Translation service are disabled. 
  
 **Summary:** There are several features in SharePoint Server that rely on the Machine Translation Service synchronous translation mode. If immediate translations are disabled, these features don't function correctly. 
  
 **Cause:** Synchronous translations for the Machine Translation service are disabled. 
  
 **Resolution: Enable synchronous translations for the Machine Translation service.**
  
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
2. On the SharePoint Central Administration website, in the **Application Management** section, click **Manage service applications**.
    
3. On the Manage Service Applications page, in the list of service applications, click **Machine Translation Service**.
    
4. In the **Maximum Synchronous Translation Requests** section, type a value that ranges from 1 to 1000 in the **Maximum number of synchronous translation requests (per server)** text box. A value of 0 indicates that synchronous translations are disabled. 
    

