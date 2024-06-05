---
title: "Verify that the critical User Profile Application and User Profile Proxy Application timer jobs are available and have not been mistakenly deleted (SharePoint Server)"
ms.reviewer: 
ms.author: serdars
author: SerdarSoysal
manager: serdars
ms.date: 8/31/2017
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: troubleshooting
ms.service: sharepoint-server-itpro
ms.localizationpriority: medium
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: bfe89420-2a60-4ce7-8b11-2b45fd38f822
description: "Learn how to resolve the SharePoint Health Analyzer rule: Verify that the critical User Profile Application and User Profile Proxy Application timer jobs are available and haven't been mistakenly deleted, for SharePoint Server."
---

# Verify that the critical User Profile Application and User Profile Proxy Application timer jobs are available and have not been mistakenly deleted (SharePoint Server)

[!INCLUDE[appliesto-2013-2016-2019-SUB-xxx-md](../includes/appliesto-2013-2016-2019-SUB-xxx-md.md)]
  
 **Rule Name:** Verify that the critical User Profile Application and User Profile Proxy Application timer jobs are available and haven't been mistakenly deleted. 
  
 **Summary:** User Profile Service Application or User Profile service proxy timer jobs aren't available and might have been deleted. 
  
 **Cause:** A required timer job for the User Profile service or the User Profile service proxy is missing.
  
 **Resolution: Edit the rule definition so that the configuration is automatically repaired.**
  
1. On the SharePoint Central Administration website, select **Monitoring**.
    
2. On the Monitoring page, in the **Health Analyzer** section, select **Review rule definitions**.
    
3. On the Health Analyzer Rule Definitions - All Rules page, in the **Category: Configuration** section, select the name of the rule. 
    
4. In the **Health Analyzer Rule Definitions** dialog, select **Edit Item**.
    
5. Select the **Repair Automatically** check box, and then select **Save**.
    
The system automatically creates the missing timer jobs.
  
For more information, see [Default timer jobs in SharePoint Server 2019](default-timer-jobs-in-sharepoint-server-2019.md), [Default timer jobs in SharePoint Server 2016](default-timer-jobs-in-sharepoint-server-2016.md), or [Default timer jobs in SharePoint 2013](default-timer-jobs-in-sharepoint-2013.md).
  

