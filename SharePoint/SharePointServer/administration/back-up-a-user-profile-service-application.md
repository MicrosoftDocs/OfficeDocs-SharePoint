---
title: "Back up User Profile service applications in SharePoint Server"
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
ms.assetid: 80f7df54-738e-49ba-9ff9-2f312d77a271
description: "Learn how to back up the User Profile Service service application in SharePoint Server."
---

# Back up User Profile service applications in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
You can back up the User Profile service application by using the SharePoint Central Administration website, Microsoft PowerShell, or SQL Server tools. Which backup tool you use depends on what kind of environment you have deployed, what your backup schedule requires, and what service level agreements you have made with your organization.
  
> [!IMPORTANT]
> The steps in this article apply to only SharePoint Servers 2019, 2016, and 2013. 
  
    
## Before you begin
<a name="begin"> </a>

We recommend that you regularly back up at the farm level. However, business or IT requirements might require you to back up the User Profile Service service application. Regularly backing up the User Profile service application reduces the possibility of data losses that might occur from hardware failures, power outages, or other problems. It is a simple process that helps make sure that all service application-related data and configurations are available for recovery, if that is required.
  
For information about what to back up and which tools to use, see [Plan for backup and recovery in SharePoint Server](backup-and-recovery-planning.md). You can back up all the service applications in the farm by backing up the complete farm. For more information, see [Back up farms in SharePoint Server](back-up-a-farm.md).
  
Before you begin this operation, review the following information:
  
- Backing up the User Profile service application does not affect the state of the farm. However, it does require resources. Therefore, backing up the service application might affect farm performance while the backup is running. You can avoid performance issues by backing up the service application during hours when farm use is lowest.
    
- You must create a folder on the local computer or the network in which to store the backups. For better performance, we recommend that you back up to the local computer and then move the backup files to a network folder. For more information about how to create a backup folder, see [Prepare to back up and restore farms in SharePoint Server](prepare-to-back-up-and-restore.md).
    
## Use PowerShell to back up a User Profile service application
<a name="proc1"> </a>

You can use PowerShell to back the User Profile service application manually or as part of a script that can be run at scheduled intervals.
  
> [!NOTE]
> Backup of a User Profile service application can fail the first time that you use PowerShell to perform the backup. If this occurs, repeat the backup procedure using PowerShell. For details about a backup failure, see the spbackup.log or sprestore.log files in the backup directory. 
  
 **To back up the User Profile service application by using PowerShell**
  
1. Verify that you have the following memberships:
    
   - **securityadmin** fixed server role on the SQL Server instance. 
    
   - **db_owner** fixed database role on all databases that are to be updated. 
    
   - Administrators group on the server on which you are running the PowerShell cmdlets.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint 2013 Products cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint Management Shell.
    
3. At the PowerShell command prompt, type the following command:
    
   ```powershell
   Backup-SPFarm -Directory <BackupFolder> -BackupMethod Full -Item Farm\Shared Services\Shared Service Applications\<ServiceApplicationName> [-Verbose]
   ```

    Where:
    
   -  _\<BackupFolder\>_ is the path of a folder on the local computer or on the network in which you want to store the backups. 
    
   -  _\<ServiceApplicationName\>_ is the name of the User Profile Service service application that you want to back up. 
    
    
    > [!NOTE]
    > The User Profile Service service application always requires a full backup, 
  
4. You must also back up the service application proxy. To do this, at the PowerShell command prompt, type the following command:
    
   ```powershell
   Backup-SPFarm -Directory <BackupFolder> -BackupMethod Full -Item Farm\Shared Services\Shared Service Proxies\<ServiceApplicationProxyName > [-Verbose]
   ```

    Where:
    
   -  _\<BackupFolder\>_ is the path of a folder on the local computer or on the network in which you want to store the backups. 
    
   -  _\<ServiceApplicationProxyName\>_ is the name of the User Profile Service service application proxy that you want to back up. 
    
For more information, see [Backup-SPFarm](/powershell/module/sharepoint-server/Backup-SPFarm?view=sharepoint-ps). 
  
> [!NOTE]
> We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions. 
  
## Use Central Administration to back up a User Profile Service application
<a name="proc2"> </a>

You can use Central Administration to back up the User Profile service application. 
  
> [!NOTE]
> Backup of a User Profile service application can fail the first time that you use Central Administration to perform the backup. If this occurs, repeat the backup procedure using Central Administration. For details about a backup failure, see the spbackup.log or sprestore.log files in the backup directory. 
  
 **To back up the User Profile service application by using Central Administration**
  
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators SharePoint group.
    
2. Start **Central Administration**.
    
3. In Central Administration, on the home page, in the **Backup and Restore** section, click **Perform a backup**.
    
4. On the Perform a Backup — Step 1 of 2: Select Component to Back Up page, select the User Profile Service service application from the list of components, and then click **Next**.
    
5. On the Start Backup — Step 2 of 2: Select Backup Options page, in the **Backup Type** section, select **Full**.
    
    > [!NOTE]
    > The User Profile service application always requires a full backup. You must use the **Full** option. 
  
6. In the **Backup File Location** section, in the **Backup location box**, type the path of the backup folder, and then click **Start Backup**.
    
7. You must also back up the service application proxy. To do this, in Central Administration, on the home page, in the **Backup and Restore** section, click **Perform a backup**.
    
8. On the Perform a Backup — Step 1 of 2: Select Component to Back Up page, select the User Profile Service service application proxy from the list of components, and then click **Next**.
    
9. On the Start Backup — Step 2 of 2: Select Backup Options page, in the **Backup Type** section, select **Full**.
    
10. In the **Backup File Location** section, in the **Backup location box**, type the path of the backup folder, and then click **Start Backup**.
    
11. You can view the general status of all backup jobs at the top of the Backup and Restore Job Status page in the **Readiness** section. You can view the status for the current backup job in the lower part of the page in the **Backup** section. The status page updates every 30 seconds automatically. You can manually update the status details by clicking **Refresh**. Backup and recovery are Timer service jobs. Therefore, it may take several seconds for the backup to start.
    
    If you receive any errors, you can review them in the **Failure Message** column of the Backup and Restore Job Status page. You can also find more details in the Spbackup.log file at the UNC path that you specified in step 5. 
    
## Use SQL Server tools to back up a User Profile service application database
<a name="proc3"> </a>

You cannot back up the whole User Profile service application or service application proxy. You must use either PowerShell or Central Administration. However, you can back up all the databases that are associated with the User Profile Service service application. 
  
 **To back up a User Profile service application database by using SQL Server**
  
1. Verify that the user account that is performing this procedure is a member of the SQL Server **db_backupoperator** fixed database role on the database server where each database is stored. 
    
2. Before you back up the User Profile Service service application databases, you must export the Microsoft Identity Integration Server Key (MIIS) encryption key. You will import this exported key before you restore the databases. By default, the key is located on the server that runs SharePoint Server 2016 that is hosting the Microsoft Forefront Identity Manager services in the following directory:  _\<root directory drive\>_\Program Files\Microsoft Office Servers\16.0\Synchronization Service\Bin or  _\<root directory drive\>_\Program Files\Microsoft Office Servers\15.0\Synchronization Service\Bin. To export the key, type the following at the command prompt:
    
   ```
   miiskmu.exe
   ```

    Use the Microsoft Identity Integration Server Key Management Utility Wizard to export the key set.
    
3. Open SQL Server Management Studio and connect to the database server.
    
4. In Object Explorer, expand **Databases**.
    
5. Right-click the database that you want to back up, point to **Tasks**, and then click **Back Up**.
    
6. In the **Back Up Database** dialog box, confirm the database name. 
    
7. Next, select the kind of backup that you want to perform from the **Backup type** list. For more information about which backup type to use, see [Recovery Models (SQL Server)](http://go.microsoft.com/fwlink/p/?LinkID=715706&amp;clcid=0x409).
    
8. In the **Backup component** area, click **Database**.
    
9. Either use the default name that is provided or specify a name for the backup set in the **Name** text box. 
    
10. In the **Destination** area, specify where you want to store the backup. 
    
11. Click **OK** to back up the database. 
    
12. Repeat steps 1-10 for each User Profile service application database.
    
## See also
<a name="proc3"> </a>

#### Concepts

[Backup solutions in SharePoint Server](backup.md)
  
[Restore service applications in SharePoint Server](restore-a-service-application.md)
#### Other Resources

[Windows PowerShell for SharePoint Server reference](/powershell/module/sharepoint-server/?view=sharepoint-ps)

