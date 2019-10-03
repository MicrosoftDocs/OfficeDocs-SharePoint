---
title: "Welcome to the SharePoint Products Configuration Wizard"
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
ms.assetid: c49561d4-fee2-4aa3-b01e-2887593f9971
description: "Summary: Learn how to use the SharePoint Products Configuration Wizard in SharePoint Server."
---

# Welcome to the SharePoint Products Configuration Wizard

 **Summary:** Learn how to use the SharePoint Products Configuration Wizard in SharePoint Server. 
  
The SharePoint Products Configuration Wizard performs basic tasks that require minimal user input and that must be performed to start SharePoint Central Administration, or that cannot be performed anywhere else.
  
In addition to using the configuration wizard to perform the initial configuration, you can use the configuration wizard at any time to perform the following tasks:
  
- Identify missing components.
    
- Validate your configuration.
    
- Identify, repair, or reset security and low-level configuration settings.
    
The configuration wizard might have to start, stop, or reset the SharePoint Administration Service, the SharePoint Timer Service, Internet Information Services (IIS), and services from other applications that depend on SharePoint Server and are appropriately registered.
  
To interrupt server operations, click **No** to exit the configuration wizard. 
  
> [!NOTE]
> You must successfully complete the configuration wizard to finish the server deployment before you can access SharePoint Central Administration to configure your site. 
  
After the configuration wizard is completed, the services that are required to run Central Administration are enabled. Then, you must use Central Administration to configure your site.
  
## Software requirements

Before you can install, configure, or operate the server, the following conditions must be met:
  
A 64-bit edition of a supported Windows Server 2012 R2 operating system or the latest version of Windows Server 2016.
  
If you install to a server farm, a supported version of SQL Server 2014 SP1.
  
Appropriate administrative credentials on the servers on which you are installing and a domain account to use as the service account.
  
## Server Roles

SharePoint farm administrators can define each server's role in a farm topology. The role of a server is specified when you create a new farm or join a server to an existing farm. SharePoint automatically configures the services on each server based on the server's role, and the performance of the farm is optimized based on that topology.
  
There are six predefined server roles you can choose. For additional information about server roles, see [MinRole overview](/sharepoint/install/overview-of-minrole-server-roles-in-sharepoint-server).
  
## Repair

You can use **Repair** to overwrite changed or damaged files and registry settings. 
  
For example, you can use **Repair** if a registry entry has been overwritten and you need to return to the default setting. 
  
When you repair an installation, the files that were installed are verified, missing components are detected, and then the configuration is repaired.
  
For information, see [How to: Repair SharePoint Products](how-to-repair-sharepoint-products.md).
  
## Update

Deploy cumulative updates and service packs for SharePoint products by using the SharePoint 2016 Products Configuration Wizard. The SharePoint 2016 Products Configuration Wizard is not used to deploy major upgrades for a server farm.
  
 **Applying updates to a farm**
  
After you apply an update, such as a service pack or cumulative update, you run the SharePoint 2016 Products Configuration Wizard to upgrade the farm to the new version. All servers in the farm must be updated to the same version and must have the same products and language packs installed before you can run the configuration wizard. If any servers in your farm were not updated, the **Farm Product and Patch Status** page appears and lists the current status for each server in the farm. From this page, you can determine which servers have to be updated. To update your servers, exit the SharePoint 2016 Products Configuration Wizard, run the update on the servers that have to be updated, and then run the configuration wizard again. 
  
 **Upgrading a server farm**
  
If you are upgrading a server farm to apply an update, you must use the following process:
  
1. Run Setup, and then run the SharePoint 2016 Products Configuration Wizard on the server that runs SharePoint Central Administration in your farm.
    
2. When you see the message about running Setup on other servers in the farm, you must run Setup and the SharePoint 2016 Products Configuration Wizard on the other servers to reach the same point.
    
3. When all servers in the farm display the message, return to the first web server, and then click **OK** to continue the upgrade process for the first server. 
    
4. After the wizard has completed on the first server, you can configure each of the other servers.
    

