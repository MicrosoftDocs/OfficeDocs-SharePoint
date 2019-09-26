---
title: "Automatic Update setting inconsistent across farm servers (SharePoint Server 2016)"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 5/30/2017
audience: ITPro
ms.topic: troubleshooting
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 2ddb9cfe-38fc-477c-88d1-beb190e36ab0
description: "Learn how to resolve the SharePoint Health Analyzer rule: Automatic update setting inconsistent across farm servers, for SharePoint Server."
---

# Automatic Update setting inconsistent across farm servers (SharePoint Server 2016)

[!INCLUDE[appliesto-xxx-2016-xxx-xxx-md](../includes/appliesto-xxx-2016-xxx-xxx-md.md)]. 
  
 **Rule Name:** Automatic update setting inconsistent across farm servers. 
  
 **Summary:** Servers in the SharePoint farm do not have the same Automatic Update settings configured. 
  
 **Cause:** One or more servers in the farm have update settings that are different from the other servers in the farm. 
  
 **Resolution: Ensure all servers in the farm have the same update settings**
  
1. Verify that you are a member of the Administrators group on the local computer.
    
2. In Control Panel, click **System and Security**, and then under **Windows Update**, click **Turn automatic updating on or off**. 
    
3. On the Choose your Windows Update settings page, make sure that the update settings are the same as other servers in your farm. Change the update settings if needed.
    
    > [!NOTE]
    > If you can't change the update settings, the update settings may be locked in group policy. If this is the case, ensure the same group policy is being applied to other servers in the farm. 
  

