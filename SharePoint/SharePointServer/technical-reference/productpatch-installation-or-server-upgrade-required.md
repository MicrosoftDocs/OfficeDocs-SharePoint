---
title: "Product / patch installation or server upgrade required (SharePoint Server)"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 8/30/2017
audience: ITPro
ms.topic: troubleshooting
ms.prod: sharepoint-server-itpro
localization_priority: Priority
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 89377b22-b1de-4f11-9a16-e54783c046fc
description: "Learn how to resolve the SharePoint Health Analyzer rule: Product / patch installation or server upgrade required,,,for SharePoint Server."
---

# Product / patch installation or server upgrade required (SharePoint Server)

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
 **Rule Name:** Product / patch installation or server upgrade required 
  
 **Summary:** You must install all required products on all servers in the farm, and all products should have the same software update and upgrade level across the farm. 
  
 **Cause:** You have not installed required products or updates, or the server needs to be upgraded. 
  
 **Resolution: Install software updates and security updates or upgrade the server.**
  
- Check if there are any pending updates and restart all the servers. 
    
**Install updates on the server.**
    
1. Log on to one server.
    
2. Verify that the user account that is performing this procedure is a member of the Administrators group on the local computer.
    
3. Open **Windows Update**. and check to see if there are any pending updates or a restart is required, schedule the updates or restart the computer.
    
4. Repeat the previous steps on all servers.
    
    For more information, see [Deploy software updates for SharePoint Server 2016](../upgrade-and-update/deploy-updates-for-sharepoint-server-2016.md).
    
If a previous upgrade attempt has failed, you must resolve upgrade issues before attempting upgrade again. You can use the SharePoint Central Administration website to find information about current and previous upgrade attempts and determine issues that may be preventing upgrade from succeeding. To do this in Central Administration, in the **Upgrade and Migration** section, click **Check upgrade status**.
    

