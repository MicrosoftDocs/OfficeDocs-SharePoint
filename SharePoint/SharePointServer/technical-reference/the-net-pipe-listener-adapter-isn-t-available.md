---
title: "The Net.Pipe Listener Adapter isn't available (SharePoint Server)"
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
ms.assetid: f8249a19-005f-4ae0-b7c0-04a683691fbf
description: "Learn how to resolve the SharePoint Health Analyzer rule: The Net.Pipe Listener Adapter isn't available, for SharePoint Server."
---

# The Net.Pipe Listener Adapter isn't available (SharePoint Server)

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
 **Rule Name:** The Net.Pipe Listener Adapter isn't available. 
  
 **Summary:** The Net.Pipe Listener Adapter is a Windows service that receives activation requests over the net.pipe protocol and passes them to the Windows Process Activation Service. 
  
 **Cause:** If the Net.Pipe Listener Adapter service is not installed or started then the SharePoint Health Analyzer rule triggers an alert. 
  
 **Resolution: Start the Net.Pipe Listener Adapter service on the server**
  
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
2. In Server Manager, click **Tools**, and then click **Services**.
    
3. In Services, double-click **Net.Pipe Listener Adapter** and make sure it is running. 
    
    > [!NOTE]
    > If the Net.Pipe Listener Adapter service is not found in the Services list you need to install it. The executable you need to run is SMSvcHost.exe and can be found at C:\Windows\Microsoft.NET\Framework64\v4.0.30319\SMSvcHost.exe. 
  

