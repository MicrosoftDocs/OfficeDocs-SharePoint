---
title: "Move all databases in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 3/7/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: d9dac189-0736-448d-928c-68bf38603613
description: "Learn how to move all databases associated with SharePoint Server to a new database server."
---

# Move all databases in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
You can use the SharePoint Central Administration website, or SQL Server tools to move all databases that are associated with SharePoint Server to a new database server.
  
## Before you begin
<a name="begin"> </a>

The procedures in this article explain how to move the following kinds of databases that are hosted on a single database server: 
  
- Configuration database
    
- Central Administration content database
    
- Content databases
    
- Service application databases
    
> [!IMPORTANT]
> To move database files within the same instance of SQL Server we recommend that you use the **FILENAME** clause of the **ALTER DATABASE** statement. For more information, see [Move User Databases](http://go.microsoft.com/fwlink/p/?LinkID=717306). 
  
> [!NOTE]
> To move a database to another instance of SQL Server or to another server, we recommend that you use procedures found in [Database Detach and Attach (SQL Server)](http://go.microsoft.com/fwlink/p/?LinkID=717308) or [Back Up and Restore of SQL Server Databases](http://go.microsoft.com/fwlink/p/?LinkID=717309). 
  
The following are the minimum permissions that are required to perform this process:
  
- You must be a member of the Farm Administrators SharePoint group.
    
- On the computer that is running the SharePoint Central Administration Web site, you must be a member of the Administrators group.
    
- On the database server from which the databases are being moved, you must be a member of the following:
    
  - The Administrators group
    
  - The **db_backupoperator** fixed database role 
    
- On the database server to which the databases are being moved, you must be a member of the following:
    
  - The Administrators group
    
  - The **db_owner** fixed database role 
    
In some environments, you must coordinate the move procedures with the database administrator. Be sure to follow applicable policies and guidelines for managing databases.
  
> [!IMPORTANT]
> When you move databases, all farm sites and assets are unavailable to users until the process is complete. Complete this operation outside normal business hours. 
  
## Move all databases
<a name="proc1"> </a>

To move all databases from one database server to another database server, you have to work in both SharePoint Server and SQL Server. 
  
Before you begin this operation, review the steps in this process:
  
1. Prepare the new database server.
    
2. Close all open SharePoint Management Shell windows.
    
3. Stop all services that are related to SharePoint Server and Internet Information Services (IIS). 
    
4. Detach the databases from the current SQL Server instance.
    
5. Copy or move all files that are associated with the databases (.mdf, .ndf, and .ldf), to the new destination server that runs SQL Server.
    
6. Make sure that all of the SQL Server logins, fixed server roles, fixed database roles, and permissions for the databases are configured correctly on the new destination database server.
    
    > [!NOTE]
    > It is important that the destination server where you move the databases has the same database information that the current SQL Server instance has. For details about how to do this, see [How to transfer logins and passwords between instances of SQL Server](http://go.microsoft.com/fwlink/p/?LinkID=512204). For more information, see [Server-Level Roles](http://go.microsoft.com/fwlink/p/?LinkID=717323) and [Database-Level Roles](http://go.microsoft.com/fwlink/p/?LinkID=717324). 
  
7. Attach the databases to the new destination server that runs SQL Server.
    
8. Use SQL Server connection aliases to point to the new database server and update all web servers.
    
    If you do not want to use SQL Server connection aliases use one of the following procedures to update the database connections for your SharePoint Server farm.
    
  - [Scenario 1](#PS): Use this procedure to update the database connections if you use SharePoint Server and SQL Server AlwaysOn Availability Groups for high availability or disaster recovery. 
    
  - [Scenario 2](#MAN): Use this procedure if you must use manual steps or if you move the databases from a SharePoint Server Single-server farm role installation to a new Single-server farm role installation.
    
9. Restart all services that you stopped in step 3.
    
### To prepare the new database server

Use the procedures in [Configure SQL Server security for SharePoint Server](../security-for-sharepoint-server/configure-sql-server-security-for-sharepoint-environments.md) to configure the new database server. 
  
The new database server must run either the same version of Windows Server and SQL Server as the existing database server, or one of the following versions:

For SharePoint Server 2019:

- Windows Server 2019

- Windows Server 2016

- SQL Server 2016

- SQL Server 2017
  
For SharePoint Server 2016:
  
- Windows Server 2012 R2 
    
- Windows Server 2016
    
- SQL Server 2014 Service Pack 1 (SP1)
    
- SQL Server 2016
    
For SharePoint 2013:
  
- Windows Server 2008 R2
    
- Windows Server 2008 R2 Service Pack 1 (SP1)
    
- Windows Server 2012
    
- SQL Server 2008
    
- SQL Server 2012
    
- SQL Server 2014
    
The version of the existing SharePoint Server and Windows Server must also support the version of the new SQL Server where the DBs are being moved. For more information, see [Hardware and software requirements for SharePoint Server 2016](../install/hardware-and-software-requirements.md) and [Hardware and software requirements for SharePoint 2013](../install/hardware-and-software-requirements-0.md).
  
### To close all open sessions of SharePoint Management Shell

1. Close all open SharePoint Management Shell windows, and all open command prompt windows.
    
### To stop the farm

1. On the server that is running Central Administration, stop the following services:
    
  - SharePoint Administration
    
  - SharePoint Timer
    
  - SharePoint Tracing
    
  - SharePoint User Code Host
    
  - SharePoint VSS Writer
    
  - World Wide Web Publishing Service
    
  - SharePoint Server Search 16
    
2. On the server that is running Central Administration, at a command prompt, type **iisreset /stop**. 
    
### To detach databases

1. In SQL Server Management Studio on the original database server, detach the databases that you want to move from the instance to which they are attached. If you are running many databases, you may want to run a Transact-SQL script to detach databases.
    
    A database cannot be detached if any one of the following is true:
    
  - The database is being mirrored.
    
  - A database snapshot exists on the database.
    
    For more information, see: [Database Detach and Attach (SQL Server)](http://go.microsoft.com/fwlink/p/?LinkID=717308), [Detach a Database](http://go.microsoft.com/fwlink/p/?LinkID=717329), and [sp_detach_db (Transact-SQL)](http://go.microsoft.com/fwlink/p/?LinkID=717330).
    
### To move database files to the new server

1. Verify that the user account that is performing this procedure is a member of the following:
    
    On the database server from which the databases are being moved, you must be a member of the following:
    
  - The Administrators group
    
  - The **db_backupoperator** fixed database role 
    
    On the database server to which the databases are being moved, you must be a member of the following:
    
  - The Administrators group
    
  - The **db_owner** fixed database role 
    
2. Use Windows Explorer to locate the .mdf, .ldf, and .ndf files that are associated with each database that you are moving. 
    
3. Copy or move the files to the destination directory on the new computer that is running SQL Server.
    
### To set up permissions on the new server

1. Verify that the user account that is performing this procedure is a member of the following:
    
  - The Administrators group
    
  - The **db_owner** fixed database role 
    
2. On the destination database server, start Management Studio and transfer your logon credentials and permissions from the original instance to the destination instance. We recommend that you transfer permissions by running a script. An example script is available in [How to transfer logins and passwords between instances of SQL Server](http://go.microsoft.com/fwlink/p/?LinkID=512204). 
    
    For more information about how to transfer SQL Server metadata between instances, see [Managing Metadata When Making a Database Available on Another Server Instance](http://go.microsoft.com/fwlink/p/?LinkID=717342).
    
### To attach databases to the new instance of SQL Server

1. Verify that the user account that is performing this procedure is a member of the following:
    
  - The Administrators group
    
  - The **db_owner** fixed database role 
    
2. On the destination database server, attach the databases to the new instance. For more information, see [Attach a Database](http://go.microsoft.com/fwlink/p/?LinkID=717343) and [sp_attach_db (Transact-SQL)](http://go.microsoft.com/fwlink/p/?LinkID=717344).
    
The following procedures provide methods to connect to the new SQL Server instance or update the database connections. Use the procedure that works best for your SharePoint Server farm environment.

> [!IMPORTANT]
> If you're using SharePoint Server and SQL Server AlwaysOn Availability Groups before moving the databases, you should point to the AG Listner. If you're moving from a single-server farm to an AlwayOn Availability Group then you should use the cliconfg.exe.
  
### To point the web application to the new database server by setting up SQL Server connection aliases

1. This procedure must be performed on all servers in the SharePoint Server farm that connect to the instance of SQL Server that hosts the databases.
    
2. Verify that the user account that is performing this procedure is a member of the following:
    
  - The Administrators group
    
  - The **db_owner** fixed database role 
    
3. Start the SQL Server Client Network Utility (cliconfg.exe). This utility is typically located in the C:\Windows\SysWOW64 and C:\Windows\System32 folder.
    
4. On the **General** tab, verify that TCP/IP is enabled.
    
5. On the **Alias** tab, click **Add**. The Add Network Library Configuration window appears. 
    
6. In the **Server alias** box, enter the name of the current instance of SQL Server. 
    
7. In the **Network libraries** area, click **TCP/IP**.
    
8. In the **Connection parameters** area, in the **Server name** box, enter the new server name and instance to associate with the alias, and then click **OK**. This is the name of the new server that is hosting the SharePoint Server databases. 
    
9. Repeat steps 3 through 8 on all servers in the farm that connect to the new instance of SQL Server.
    
10. Optional. If your environment relies on System Center 2012 - Data Protection Manager (DPM) or a third-party application that uses the Volume Shadow Copy Service framework for backup and recovery, you must install the SQL Server connectivity components on each web server or application server by running SQL Server setup. For more information, see [Install SQL Server 2014 from the Installation Wizard (Setup)](http://go.microsoft.com/fwlink/p/?LinkID=717350) and [Windows Server Installation and Upgrade](/windows-server/get-started/installation-and-upgrade).
    
You can use these Microsoft PowerShell cmdlets to deploy, manage, and remove availability groups in SQL Server with SharePoint Server:
  
- **Add-DatabaseToAvailabilityGroup**
    
- **Remove-DatabaseFromAvailabilityGroup**
    
- **Get-AvailabilityGroupStatus**
    
Use the following procedure to update the database connections if you use SharePoint Server and SQL Server AlwaysOn Availability Groups for high availability or disaster recovery.
  
 <a name="PS"></a>**Scenario 1: To update the database connections by using PowerShell**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint Management Shell.
    
3. At the PowerShell command prompt, type the following commands:
    
  ```
  Add-DatabaseToAvailabilityGroup -AGName "<AGGroupName>" -DatabaseName "<DatabaseName>" [-FileShare "<\\server\share>"]
  ```

Where:
    
  - \<AGGroupName\> is the name of the Avaliability Group.
    
  - \<DatabaseName\> is the name of the database that you are adding to the Availability Group
    
  - If the optional **-FileShare** parameter is used, <\\server\share> is the name of the server and the share that you use. 
    
4. Repeat these steps for all databases that you move, including the Configuration and Central Administration Content databases.
    
Use the next procedure for the following scenarios:
  
- If you must use manual steps
    
- If you move the databases from a SharePoint Server 2016 Single-Server Farm role type to a new Single-Server Farm role type or from a SharePoint 2013 single-server installation to a new single-server installation.
    
    > [!NOTE]
    > The Single-Server Farm role replaces the Standalone Install mode available in previous SharePoint Server releases. For more information, see [Overview of MinRole Server Roles in SharePoint Server 2016](../install/overview-of-minrole-server-roles-in-sharepoint-server.md). 
  
- If you use Availability Groups then you must manually add the databases to the availability groups as appropriate to their high availability/disaster recovery support. For more information, see [Add a Database to an Availability Group (SQL Server)](http://go.microsoft.com/fwlink/p/?LinkID=717351)
    
- If you use SQL Mirroring then make sure your mirroring is setup appropriately. For more information, see [Setting Up Database Mirroring (SQL Server)](http://go.microsoft.com/fwlink/p/?LinkID=717353) and [Database Mirroring (SQL Server)](http://go.microsoft.com/fwlink/p/?LinkID=717354).
    
 <a name="MAN"></a>**Scenario 2: To update the database connections by using Microsoft PowerShell**
  
1. Start the SharePoint Management Shell.
    
2. At the PowerShell command prompt, type the following commands:
    
  ```
  $db = Get-SPDatabase -Identity <guid>
  ```

Where \<GUID\> is the ID of the database that you move.
    
> [!NOTE]
> Use **Get-SPDatabase** without parameters to see a list of all databases with GUIDs. 
  
  ```
  $db.ChangeDatabaseInstance("<DBServerName>")
  ```

Where \<DBServerName\> is the name or alias of the new SQL Server or is the AlwaysOn Availability Group listener DNS name.
    
  ```
  $db.Update()
  ```

3. If you use SQL Server database mirroring then you must remember to populate the FailoverServiceInstance property on the SharePoint database.
    
  ```
  $db.failoverserviceinstance("<DBServerName>")
  ```

Where \<DBServerName\> is the name or alias of the mirrored SQL Server.
    
  ```
  $db.update()
  ```

4. Repeat these steps for all databases that you move, including the Configuration and Central Administration Content databases.
    
### To restart the services in the farm

1. Verify that the user account that is performing this procedure is a member of the Farm Administrators SharePoint group.
    
2. On the server that is running the SharePoint Central Administration website, at a command prompt, type **iisreset /start**. 
    
3. In the Microsoft Management Console Services snap-in, start all of the services that are related to SharePoint Server and IIS. These include the following services:
    
  - SharePoint Administration
    
  - SharePoint Timer
    
  - SharePoint Tracing
    
  - SharePoint User Code Host
    
  - SharePoint VSS Writer
    
  - World Wide Web Publishing Service
    
  - SharePoint Server Search
    
## See also
<a name="proc1"> </a>

#### Concepts

[Database types and descriptions in SharePoint Server](../technical-reference/database-types-and-descriptions.md)
#### Other Resources

[Quick reference guide: SharePoint Server 2016 databases](https://download.microsoft.com/download/D/5/D/D5DC1121-8BC5-4953-834F-1B5BB03EB691/DBrefguideSPS2016_tabloid.pdf)
  
[Databases that support SharePoint 2013](https://go.microsoft.com/fwlink/p/?LinkId=257370)
  
[Add a database server to an existing farm in SharePoint 2013](/previous-versions/office/sharepoint-server-2010/cc262781(v=office.14))

