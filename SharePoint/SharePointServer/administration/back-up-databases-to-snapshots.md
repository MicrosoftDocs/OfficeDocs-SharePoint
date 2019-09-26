---
title: "Back up databases to snapshots in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 101dd661-8843-4b98-bab7-89c14abe65b8
description: "Learn how to back up databases to snapshots in SharePoint Server by using SQL Server Enterprise."
---

# Back up databases to snapshots in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
You can only back up databases to snapshots in SharePoint Server by using SQL Server Enterprise tools.
  
## Before you begin
<a name="begin"> </a>

We recommend that you regularly back up the complete farm. Regularly backing up the farm reduces data losses that might occur from hardware failures, power outages, or other problems. It is a simple process and helps make sure that all the farm data and configurations are available for recovery, if that is required. For more information, see [Back up farms in SharePoint Server](back-up-a-farm.md). However, IT requirements might require you to backup databases to snapshots. Although you can back up any farm database to a snapshot, you typically back up content databases.
  
> [!IMPORTANT]
> Database snapshots do not replace a backup and restore strategy. To fully protect your SharePoint Server environment we advise you to perform regular backups to protect your farm in case you need to restore data after a failure.. 
  
Before you begin this operation, review the following information:
  
- You must first create a folder on the database server for your backup files. If you want to store the snapshots at another location, you can move the backup files to a backup folder on the network after the operation is completed.
    
- A database snapshot provides a read-only, static view of a source database as it existed at snapshot creation, minus any uncommitted transactions. Uncommitted transactions are rolled back in a newly created database snapshot because the Database Engine runs recovery after the snapshot was created (transactions in the database are not affected). For more information about database snapshots, see [Database Snapshots (SQL Server)](http://go.microsoft.com/fwlink/p/?LinkID=715786&amp;clcid=0x409). 
    
## Use SQL Server tools to back up a database to a snapshot in SharePoint Server
<a name="proc1"> </a>

If you want to back up databases to snapshots, you must use SQL Server tools. The databases that are associated with the farm are determined by the service applications and features that you have installed on the farm.
  
 **To back up a database to a snapshot by using SQL Server tools**
  
1. Verify that the user account that is performing this procedure is a member of the SQL Server **db_owner** fixed database role. 
    
2. Open SQL Server Management Studio and connect to the database server.
    
3. In Object Explorer, expand **Databases**.
    
4. Select the database that you want to back up, and then click **New Query**.
    
5. Copy the following text, and then paste it to the query pane.
    
   ```sql
   CREATE DATABASE <snapshot name>
   ON
   (
   NAME=<logical name of the database file>,
   FILENAME = 'c:\WSS_Backup1.ss')
   AS SNAPSHOT OF <database name>;
   ```

## See also
<a name="proc1"> </a>

#### Other Resources

[Database Snapshots (SQL Server)](http://go.microsoft.com/fwlink/p/?LinkID=715786&amp;clcid=0x409)
  
[Database Snapshots with AlwaysOn Availability Groups (SQL Server)](http://go.microsoft.com/fwlink/p/?LinkID=715787&amp;clcid=0x409)

