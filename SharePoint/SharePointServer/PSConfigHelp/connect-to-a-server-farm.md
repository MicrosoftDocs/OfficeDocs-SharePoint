---
title: "Connect to a server farm"
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
ms.assetid: c4775220-8ea8-40ba-ba6f-299558732f4f
description: "Summary: Learn how to connect to a server farm in SharePoint Server."
---

# Connect to a server farm

 **Summary:** Learn how to connect to a server farm in SharePoint Server. 
  
You can create a new server farm or manage the connection to an existing SharePoint farm. You must provide the database server name, the database name, and the credentials for a user account that will be used for database access. If you are connecting to an existing farm, you will also have to specify a passphrase to use to connect to the farm. For more information, see [Specify farm security settings](specify-farm-security-settings.md).
  
All the servers in the farm must use the same configuration database. If the database does not exist, a new database will be created. If the database name is the same as an existing database, the database must not contain any tables, stored procedures, or other objects.
  
Enter the credentials for the user account that the SharePoint product will use for database connectivity. If the configuration database is hosted on a different computer, the account must be a domain account.
  
You can select one of the following options: 
  
- **Do not modify these settings**
    
- **Connect to an existing server farm**
    
- **Create a new server farm**
    
- **Disconnect from this server farm**
    
> [!NOTE]
> All of these options might not appear in your installation. The options that are displayed depend on the configuration and state of your server farm. 
  
The configuration wizard checks for an existing connection to a configuration database. If a connection does not exist, a new server farm is created. If a connection exists, settings are not modified.
  
When you manage the database connection to an existing server farm, the configuration wizard ensures that one or more SharePoint Central Administration web site exist in the server farm and are registered in the configuration database. This is designed to prevent a situation where a server farm exists but a SharePoint Central Administration web site is not installed to manage the installation.
  
If you select **Disconnect from this server farm**, the configuration wizard removes the server from the farm, and then updates the SharePoint Central Administration site for the farm.
  
If the computer you are disconnecting has a SharePoint Central Administration web site, it is removed, and the entry in the configuration database is removed.
  

