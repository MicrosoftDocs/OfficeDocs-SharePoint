---
title: "Server role configuration isn't correct (SharePoint Server 2016)"
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
ms.assetid: 23829b00-db4c-4400-b236-e86ea60fa193
description: "Learn how to resolve the SharePoint Health Analyzer rule: Server role configuration isn't correct, for SharePoint Server."
---

# Server role configuration isn't correct (SharePoint Server 2016)

[!INCLUDE[appliesto-xxx-2016-xxx-xxx-md](../includes/appliesto-xxx-2016-xxx-xxx-md.md)] 
  
 **Rule Name:** Server role configuration isn't correct. 
  
 **Summary:** This new rule helps ensure that your servers are operating in their optimal MinRole configuration. This rule runs every night at midnight on each server in your SharePoint Server 2016 farm. The rule scans all service instances on the server to detect if any are not in compliance. 
  
 **Cause:** A service application on the server isn't correctly configured. 
  
 **Resolution: Automatically reconfigures the service to match the expected configuration**
  
1. If any service instance is not in compliance, the health rule automatically reconfigures the service to match the expected configuration.
    
2. No manual intervention by the SharePoint farm administrator is required.
    
3. The automatic repair functionality of this health rule can be disabled by the SharePoint farm administrator while still allowing the health rule to run.
    
4. If the health rule detects that a server is out of compliance and the automatic repair functionality is disabled, it generates a health report in Central Administration. The health report identifies which servers are out of compliance and offers the ability to automatically repair the server and also provide instructions about how to manually fix the servers.
    
    For more information, see the Health monitoring section in [Overview of MinRole Server Roles in SharePoint Server 2016](../install/overview-of-minrole-server-roles-in-sharepoint-server.md).
    

