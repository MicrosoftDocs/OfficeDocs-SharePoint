---
title: "Restore farms in SharePoint Server"
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
ms.assetid: 7942ef65-c309-402d-b4bb-d54e686fc5d9
description: "Learn how to restore a SharePoint Server farm."
---

# Restore farms in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
You can restore a SharePoint Server farm by using the SharePoint Central Administration website, Microsoft PowerShell, or SQL Server tools. The backup tool that you use depends on the kind of environment that you have deployed, the backup schedule, and service level agreements that you have made with your organization.
  
    
## Before you begin
<a name="begin"> </a>

Farm-level recovery is usually performed only after a failure that involves the complete farm, or where partial recovery of part of the farm is not possible. If you only have to restore part of the farm, a specific database, a service application, a list, or document library, or a specific document, use another recovery method. For more information about alternate forms of recovery, see [Related content](#proc4).
  
 Farm recovery is usually performed for any of the following reasons: 
  
- Restoring a farm after a fire, disaster, equipment failure, or other data-loss event.
    
- Restoring farm configuration settings and data to a specific previous time and date.
    
- Moving a SharePoint Server deployment from one farm to another farm.
    
Before you begin this operation, review the following information about how to recover a farm in SharePoint:
  
- You cannot back up from one version of SharePoint Server 2019 and restore to another version of SharePoint Server 2019. The same applies to SharePoint Servers 2016 and 2013.
    
- Backing up the farm will back up the configuration and Central Administration content databases, but these cannot be restored using SharePoint Server tools. For more information about how to back up and restore all of the farm databases, see [Move all databases in SharePoint Server](move-all-databases.md).
    
- When you restore the farm by using SharePoint Server, the restore process will not automatically start all of the service applications. You must manually start them by using Central Administration or Microsoft PowerShell. Do not use SharePoint Products Configuration Wizard to start the services because doing this will also re-provision the services and service proxies. For more information, see [Start or stop a service in SharePoint Server](start-or-stop-a-service.md).
    
- The identifier (ID) of each content database is retained when you restore or reattach a database by using built-in tools. Default change log retention behavior when using built-in tools is as follows:
    
  - The change logs for all databases are retained when you restore a farm.
    
  - The change log for content databases is retained when you reattach or restore a database.
    
    When a database ID and change log are retained, the search system continues crawling based on the regular schedule that is defined by crawl rules.
    
    When you restore an existing database and do not use the overwrite option, a new ID is assigned to the restored database, and the database change log is not preserved. The next crawl of the database will add data from the content database to the index.
    
    If a restore is performed and the ID in the backup package is already being used in the farm, a new ID is assigned to the restored database and a warning is added to the restore log. The ability to perform an incremental crawl instead of a full crawl depends on the content database ID being the same as before and the change log token that is used by the search system being valid for the current change log in the content database. If the change log is not preserved, the token is not valid and the search system has to perform a full crawl.
    
- SharePoint Server backup backs up the Business Data Connectivity service external content type definitions but does not back up the data source itself. To protect the data, you should back up the data source when you back up the Business Data Connectivity service or the farm.
    
    If you restore the Business Data Connectivity service or the farm and then restore the data source to a different location, you must change the location information in the external content type definition. If you do not, the Business Data Connectivity service might be unable to locate the data source.
    
- SharePoint Server restores remote Binary Large Objects (BLOB) stores only if you are using the FILESTREAM remote BLOB store provider to put data in remote BLOB stores.
    
    If you are using another provider, you must manually restore the remote BLOB stores.
    
- If you are sharing service applications across farms, be aware that trust certificates that were exchanged are not included in farm backups. You must back up your certificate store separately or keep the certificates in a separate location. When you restore a farm that shares a service application, you must import and redeploy the certificates, and then re-establish any inter-farm trusts.
    
    For more information, see [Exchange trust certificates between farms in SharePoint Server](exchange-trust-certificates-between-farms.md).
    
- After a Web application that is configured to use claims-based authentication is restored, duplicate or additional claims providers are often visible. If duplicates appear, then you must manually save each Web application zone to remove them. For more information, see [Restore web applications in SharePoint Server](restore-a-web-application.md).
    
- Additional steps are required when you restore a farm that contains a Web application that is configured to use forms-based authentication. For more information, see [Restore web applications in SharePoint Server](restore-a-web-application.md).
    
## Using PowerShell to restore a farm in SharePoint
<a name="proc1"> </a>

You can use Microsoft PowerShell to restore a farm.
  
 **To restore a farm by using PowerShell**
  
1. Verify that you have the following memberships:
    
   - **securityadmin** fixed server role on the SQL Server instance. 
    
   - **db_owner** fixed database role on all databases that are to be updated. 
    
   - Administrators group on the server on which you are running the PowerShell cmdlets.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Open the SharePoint Management Shell.
    
3. At the PowerShell command prompt, type the following command:
    
   ```powershell
   Restore-SPFarm -Directory <BackupFolder> -RestoreMethod Overwrite [-BackupId <GUID>]
   ```

   Where:
    
   -  _\<BackupFolder\>_ is the path of the folder you use for storing backup files. 
    
   -  _\<GUID\>_ is the identifier of the backup to restore from. 
    
   > [!NOTE]
   > If you are not logged on as the Farm account, you are prompted for the Farm account's credentials. 
  
   If you do not specify the `BackupId`, the most recent backup will be used. To view the backups for the farm, at the Microsoft PowerShell command prompt,type the following command: 
    
   ```powershell
   Get-SPBackupHistory -Directory <BackupFolder> -ShowBackup [-Verbose]
   ```

   Where:
    
   -  _\<BackupFolder\>_ is the path of the folder you use for storing backup files. 
    
    You cannot use a configuration-only backup to restore content databases together with the configuration. 
    
4. To restart a service application, at the PowerShell command prompt, type the following command:
    
   ```powershell
   Start-SPServiceInstance -Identity <ServiceApplicationID>
   ```

   Where _\<ServiceApplicationID\>_ is the GUID of the service application. 
    
For more information about how to restart service applications by using PowerShell, see [Start-SPServiceInstance](/powershell/module/sharepoint-server/Start-SPServiceInstance?view=sharepoint-ps).
    
For more information about how to restore the farm by using PowerShell_2nd_NoVer, see Restore-SPFarm.PShell_stsadm_deprecated
  
## Using Central Administration to restore a farm
<a name="proc2"> </a>

You can use the Central Administration Web site to restore a farm.
  
 **To restore a farm by using Central Administration**
  
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators SharePoint group. 
    
2. In Central Administration, on the home page, in the **Backup and Restore** section, click **Restore from a backup**.
    
3. On the Restore from Backup — Step 1 of 3: Select Backup to Restore page, from the list of backups, select the backup job that contains the farm backup, and then click **Next**. You can view more details about each backup by clicking the (+) next to the backup. 
    
    > [!NOTE]
    > If the correct backup job does not appear, in the **Backup Directory Location** text box, type the Universal Naming Convention (UNC) path of the correct backup folder, and then click **Refresh**. You cannot use a configuration-only backup to restore the farm. 
  
4. On the Restore from Backup — Step 2 of 3: Select Component to Restore page, select the check box that is next to the farm, and then click **Next**.
    
5. On the Restore from Backup — Step 3 of 3: Select Restore Options page, in the **Restore Component** section, make sure that **Farm** appears in the **Restore the following component** list. 
    
    In the **Restore Only Configuration Settings** section, make sure that the **Restore content and configuration settings** option is selected. 
    
    In the **Restore Options** section, under **Type of Restore**, select the **Same configuration** option. A dialog box will appear that asks you to confirm the operation. Click **OK**.
    
    > [!NOTE]
    > If the **Restore Only Configuration Settings** section does not appear, the backup that you selected is a configuration-only backup. You must select another backup. 
  
    Click **Start Restore**.
    
6. You can view the general status of all recovery jobs at the top of the Backup and Restore Job Status page in the **Readiness** section. You can view the status for the current recovery job in the lower part of the page in the **Restore** section. The status page updates every 30 seconds automatically. You can manually update the status details by clicking **Refresh**. Backup and recovery are Timer service jobs. Therefore, it may take several seconds for the recovery to start.
    
    If you receive any errors, you can review them in the **Failure Message** column of the Backup and Restore Job Status page. You can also find more details in the Sprestore.log file at the UNC path that you specified in step 3. 
    
7. When the restore process has completed, you may need to restart one or more service applications. In Central Administration, on the home page, in the **Systems Settings** section, click **Manage services on server**. On the Services on Server page, start any services related to service applications that you want to run by clicking **Restart** in the **Action** column next to the service application. 
    
8. Re-establish any trust relationships. For more information, see [Exchange trust certificates between farms in SharePoint Server](exchange-trust-certificates-between-farms.md).
    
## Using SQL Server tools to restore a farm
<a name="proc3"> </a>

Although you cannot restore the complete farm by using SQL Server tools, you can restore most of the farm databases. If you restore the databases by using SQL Server tools, you must restore the farm configuration by using Central Administration or PowerShell. For more information about how to restore the farm's configuration settings, see [Restore farm configurations in SharePoint Server](restore-a-farm-configuration.md).
  
> [!NOTE]
> The search index is not stored in SQL Server. If you use SQL Server tools to back up and restore search, you must perform a full crawl after you restore the content database. 
  
Before you restore SharePoint Server, we recommend that you configure a recovery farm for site and item recovery.
  
Restore the databases by following these steps:
  
1. If possible, back up the live transaction log of the current database to protect any changes that were made after the last full backup.
    
2. Restore the last full database backup.
    
3. Restore the most recent differential database backup that occurred after the most recent full database backup.
    
4. Restore all transaction log backups that occurred after the most recent full or differential database backup.
    
Use the following procedure to restore your farm databases.
  
 **To restore a farm by using SQL Server tools**
  
1. Verify that the user account that is performing this procedure is a member of the **sysadmin** fixed server role. 
    
2. If the SharePoint Timer service is running, stop the service and wait for several minutes for any currently running stored procedures to finish. Do not restart the service until after you restore all the databases that you have to restore.
    
3. Start SQL Server Management Studio and connect to the database server.
    
4. In Object Explorer, expand **Databases**.
    
5. Right-click the database that you want to restore, point to **Tasks**, point to **Restore**, and then click **Database**.
    
    The database is automatically taken offline during the recovery operation and cannot be accessed by other processes.
    
6. In the **Restore Database** dialog box, specify the destination and the source, and then select the backup set or sets that you want to restore. 
    
    The default values for destination and source are appropriate for most recovery scenarios.
    
7. In the **Select a page** pane, click **Options**.
    
8. In the **Restore options** section, select only **Overwrite the existing database**. Unless your environment or policies require otherwise, do not select the other options in this section. 
    
9. In the **Recovery state** section: 
    
   - If you have included all the transaction logs that you must restore, select **RECOVER WITH RECOVERY**.
    
   - If you must restore additional transaction logs, select **RECOVER WITH NORECOVERY**.
    
   - The third option, **RECOVER WITH STANDBY** is not used in this scenario. 
    
    > [!NOTE]
    > For more information about these recovery options, see [Restore Database (Options Page)]( http://go.microsoft.com/fwlink/p/?LinkID=717045&amp;clcid=0x409). 
  
10. Click **OK** to complete the recovery operation. 
    
11. Except for the configuration database, repeat steps 4 through 9 for each database that you are restoring. 
    
    > [!IMPORTANT]
    > If you are restoring the User Profile database (by default named "User Profile Service_ProfileDB_\<GUID\>"), then also restore the Social database (by default named "User Profile Service_SocialDB_\<GUID\>"). Failing to do this can cause inaccuracies in the User Profile data that might be difficult to detect and fix. 
  
12. To restore the configuration settings, you must use the existing configuration database or manually create a new database and restore the configuration to that database. For more information about how to restore the farm configuration, see [Restore farm configurations in SharePoint Server](restore-a-farm-configuration.md).
    
13. Start the SharePoint Timer service.
    
14. Start any service applications that have to be restarted. In Central Administration, on the home page, in the **Systems Settings** section, click **Manage services on server**. On the Services on Server page, start any services related to service applications that you want to run by clicking **Restart** in the **Action** column next to the service application. 
    

## <a name="proc4"></a>Related content

The following list shows other recovery methods that you can use when you only need to restore part of your farm: 
  
- [Back up farms in SharePoint Server](back-up-a-farm.md)
    
- [Restore farm configurations in SharePoint Server](restore-a-farm-configuration.md)
    
- [Restore web applications in SharePoint Server](restore-a-web-application.md)
    
- [Restore content databases in SharePoint Server](restore-a-content-database.md)
    

