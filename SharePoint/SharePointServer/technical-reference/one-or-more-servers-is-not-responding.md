---
title: "One or more servers is not responding (SharePoint Server)"
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
ms.assetid: 9c470892-d865-4796-ad45-8b050f29aead
description: "Learn how to resolve the SharePoint Health Analyzer rule: One or more servers is not responding, for SharePoint Server."
---

# One or more servers is not responding (SharePoint Server)

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
 **Rule Name:** One or more servers is not responding. 
  
 **Summary:** SharePoint Server cannot detect one or more servers in the farm. These servers are managed by the farm, but do not respond. 
  
 **Cause:** The servers are not running, are disconnected from the network, or are physically removed from the farm. 
  
 **Resolution: Ensure that the servers are running and connected to the network, restart the SharePoint Timer Service, or remove the server record from the SharePoint topology.**
  
- Make sure the SharePoint Timer Service is started. If not, start the service. 
    
1. Verify that the user account that is performing this procedure is a member of the Administrators group on the local computer.
    
2. In **Server Manager**, click **Tools**, and then click **Services**.
    
3. In the **Services** list, make sure the status of **SharePoint Timer Service** is **Started**. If not, right-click **SharePoint Timer Service**, and click **Start**.
    
    Alternatively, you can start the SharePoint 2010 Timer service by doing the following on each server that does not respond:

    - Verify that the user account that is performing this procedure is a member of the Administrators group on the local computer.

    - Open the Command Prompt window, type the following command, and then press ENTER:

    - `net start SPTimerV4`
    
**If the server was intentionally removed from the farm, follow these steps to remove the record of the server from the SharePoint topology in Central Administration.**
    
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
2. On the SharePoint Central Administration website, in the **System Settings** section, click **Manage servers in this farm**.
    
3. In the **Server** list, find the server that you want to remove, and then click **Remove Server**.
    
4. In the warning message dialog box, click **OK**.
    

