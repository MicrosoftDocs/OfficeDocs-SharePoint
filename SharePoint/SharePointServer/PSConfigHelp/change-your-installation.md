---
title: "Change your installation"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 3/1/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ROBOTS: NOINDEX
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: b43d4383-ba69-405d-aa6e-5d3f0035a1f1
description: "Summary: Learn how to change your installation in SharePoint Server."
---

# Change your installation

 **Summary:** Learn how to change your installation in SharePoint Server. 
  
You can use the SharePoint Products Configuration Wizard to repair and uninstall SharePoint Server.
  
## Repair

You can use **Repair** to overwrite changed or damaged files and registry settings. 
  
For example, you can use **Repair** if a registry entry has been overwritten and you need to return to the default setting. 
  
When you repair an installation, the files that were installed are verified, missing components are detected, and then the configuration is repaired.
  
> [!NOTE]
> If you have applied any software updates, such as a service pack, you can still repair your installation. However, only original files will be repaired, and not files that have been updated with newer versions. 
  
## Remove

You can use **Remove** to uninstall SharePoint Server. Uninstalling removes most files and subfolders located in the installation folders. SQL Server databases are detached, but are not removed completely from the database server. When you remove SharePoint Server, all user data is left in the database files. The **Remove** option removes the web servers and application servers, but not the database servers in the farm. To remove a database server from a farm, you must first move any databases that are hosted by that server to another database server in the farm. You can then use Central Administration to remove the database server. 
  

