---
title: "The Security Token Service is not available (SharePoint Server)"
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
ms.assetid: fb4e9a7d-1ad2-4a89-ad90-85d61b44f56d
description: "Learn how to resolve the SharePoint Health Analyzer rule: The Security Token Service is not available, for SharePoint Server."
---

# The Security Token Service is not available (SharePoint Server)

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
 **Rule Name:** The Security Token Service is not available. 
  
 **Summary:** The Security Token Service is not issuing tokens. 
  
 **Cause:** The service could be malfunctioning or in a bad state, or some assemblies are missing when you deploy the custom claims provider. 
  
 **Resolution: Restart the Security Token Service application pool.**
  
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
2. Identify the server on which this event occurs. On the SharePoint Central Administration website, in the **Monitoring** section, click **Review problems and solutions**, and then find the name of the server in the **Failing Servers** column. If there are multiple failing servers in a server farm, you must repeat the following steps on each failing server. 
    
3. Verify that the user account that is performing the following steps is a member of the Administrators group on the local computer that you identified in the previous step.
    
4. Log on to the server on which this event occurs.
    
5. Open **Server Manager**, click **Tools**, and then click **Internet Information Services (IIS) Manager**.
    
6. In the Internet Information Services management console, in the **Connections** pane, expand the tree view, and then click **Application Pools**.
    
7. In the **Application Pools** list, right-click **SecurityTokenServiceApplicationPool**, and then click **Start**. If the application pool is started already, click **Stop** and then, in the **Action** pane, click **Start** to restart it. 
    
**Resolution: Install the missing assemblies into the global assembly cache (GAC) manually.**
  
1. Check the event logs and ULS logs on all servers to find out which assemblies of the custom claims provider are missing.
    
2. Install the missing assemblies into the global assembly cache manually. For more information, see [How to: Install an Assembly into the Global Assembly Cache](https://go.microsoft.com/fwlink/p/?LinkId=169102).
    

