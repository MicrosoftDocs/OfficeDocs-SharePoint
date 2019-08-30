---
title: "Restore service applications in SharePoint Server"
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
ms.assetid: 3e9dcd50-53e6-4471-a969-aeb4d079dfa3
description: "Learn how to restore a service application in SharePoint Server."
---

# Restore service applications in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
You can restore a service application in SharePoint Server by using the SharePoint Central Administration website or Microsoft PowerShell. Which backup tool you use depends on what kind of environment you have deployed, what your backup schedule requires, and what service level agreements you have made with your organization. 
  
    
## Before you begin
<a name="begin"> </a>

There are situations in which you might have to restore a specific service application instead of restoring the complete farm. Some service applications — for example, the Business Data Connectivity service application and the User Profile Service service application — provide data to other services and sites. As a result, users might experience some service interruption until the recovery process is completed.
  
Before you begin this operation, review the following information about how to restore service applications:
  
- You cannot back up from one version of SharePoint and restore to another version of SharePoint.
    
- SharePoint Server backs up the Business Data Connectivity service metadata store, which includes external content types, external systems, and Business Data Catalog models. Note that this does not back up the external data sources. To protect the data, the external data sources must be backed up.
    
- If you restore the service application or the farm and then restore the data source to a different location, you must configure the location information in the external content type definition. If you do not, the Business Data Connectivity service might be unable to locate the data source.
    
    > [!NOTE]
    > SharePoint Server restores remote Binary Large Object (BLOB) stores but only if you are using the FILESTREAM provider to put data in remote BLOB stores. If you are using another provider, you must manually restore remote BLOB stores. 
  
- You cannot restore the complete service application by using SQL Server tools. However, you can restore the databases that are associated with the service application.
    
## Use PowerShell to restore a service application in SharePoint Server
<a name="proc1"> </a>

You can use PowerShell to restore a service application.
  
 **To restore a service application by using PowerShell**
  
1. Verify that you have the following memberships:
    
   - **securityadmin** fixed server role on the SQL Server instance. 
    
   - **db_owner** fixed database role on all databases that are to be updated. 
    
   - Administrators group on the server on which you are running the PowerShell cmdlets.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. 
  
    For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps).
    
2. Start the SharePoint Management Shell.
    
3. At the PowerShell command prompt, type the following command:
    
   ```powershell
   Restore-SPFarm -Directory 
   <BackupFolder>
    -Item "
   <ServiceApplicationName>
   " -RestoreMethod Overwrite [-BackupId 
   <GUID>
   ] [-Verbose]
   ```

   Where:
    
   -  _\<BackupFolder\>_ is the path for the backup folder where the service application was backed up. 
    
   -  _\<ServiceApplicationName\>_ is the name of the service application. 
    
   -  _\<GUID\>_ is the ID of the backup to use. 
    
   To specify which backup to use, use the  `BackupId` parameter. You can view the backups for the farm by typing the following:  `Get-SPBackupHistory -Directory <BackupFolder> -ShowBackup`. If you do not specify the  `BackupId`, the most recent backup will be used. You cannot restore a service application from a configuration-only backup.
    
    To restore all the service applications, at the PowerShell command prompt, type the following command:
    
   ```powershell
   Restore-SPFarm -Directory 
   <BackupFolder>
    -Item "Farm\Shared Service Applications" -RestoreMethod Overwrite [-BackupId 
   <GUID>
   ] [-Verbose]
   ```

    Where:
    
   -  _\<BackupFolder\>_ is the path for the backup folder where the service application was backed up. 
    
   -  _\<GUID\>_ is the ID of the backup to use. 
    
For more information, see [Restore-SPFarm](/powershell/module/sharepoint-server/Restore-SPFarm?view=sharepoint-ps).
  
> [!NOTE]
> We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions. 
  
## Use Central Administration to restore a service application in SharePoint Server
<a name="proc2"> </a>

Use the following procedure to restore a service application by using the SharePoint Central Administration Web site.
  
 **To restore a service application by using Central Administration**
  
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators SharePoint group.
    
2. Start Central Administration.
    
3. In Central Administration, on the home page, in the **Backup and Restore** section, click **Restore from a backup**.
    
4. On the Restore from Backup — Step 1 of 3: Select Backup to Restore page, select the backup job that contains the service application backup, or a farm-level backup, from the list of backups, and then click **Next**. You can view more details about each backup by clicking the (+) next to the backup.
    
    > [!NOTE]
    > If the correct backup job does not appear, in the **Backup Directory Location** text box, type the path of the correct backup folder, and then click **Refresh**. You cannot use a configuration-only backup to restore the farm. 
  
5. On the Restore from Backup — Step 2 of 3: Select Component to Restore page, expand **Shared Services Applications**, select the check box that is next to the service application, and then click **Next**. To restore all the service applications, select the **Shared Services Applications** node. 
    
6. On the Restore from Backup — Step 3 of 3: Select Restore Options page, in the **Restore Component** section, make sure that **Farm\Shared Services Applications\\<Service application\>** appears in the **Restore the following component** list. 
    
    In the **Restore Options** section, under **Type of restore**, select the **Same configuration** option. A dialog box will appear that asks you to confirm the operation. Click **OK**.
    
    Click **Start Restore**.
    
7. You can view the general status of all recovery jobs at the top of the Backup and Restore Job Status page in the **Readiness** section. You can view the status for the current recovery job in the lower part of the page in the **Restore** section. The status page updates every 30 seconds automatically. You can manually update the status details by clicking **Refresh**. Backup and recovery are Timer service jobs. Therefore, it may take a several seconds for the recovery to start.
    
    If you receive any errors, you can review them in the **Failure Message** column of the Backup and Restore Job Status page. You can also find more details in the Sprestore.log file at the UNC path that you specified in step 3. 
    
## Use SQL Server tools to restore the databases associated with a service application in SharePoint Server
<a name="proc3"> </a>

You cannot restore the complete service application by using SQL Server tools. However, you can use SQL Server tools to restore the databases that are associated with the service application. To restore the complete service application, use either Microsoft PowerShell or Central Administration.
  
 **To restore the databases for a service application by using SQL Server tools**
  
1. Verify that the user account that you are using to restore the databases is a member of the **sysadmin** fixed server role on the database server where each database is stored. 
    
2. Open SQL Server Management Studio and connect to the database server.
    
3. In Object Explorer, expand **Databases**.
    
4. Right-click the database that you want to restore, point to **Tasks**, point to **Restore**, and then click **Database**. 
    
5. In the **Restore Database** dialog box, on the General page, select the database to restore to from the **To database** drop-down list. 
    
6. Select the restore source from the **From database** drop-down list. 
    
7. In the **Select the backup sets to restore section** area, select the check box next to the database. 
    
8. On the Options tab, select the recovery state from the **Recover state** section. 
    
    For more information about which recovery type to use, see [ Recovery Models (SQL Server) ](http://go.microsoft.com/fwlink/p/?LinkID=626889&amp;clcid=0x409) in SQL Server Books Online. 
    
9. Click **OK** to restore the database. 
    
10. Repeat steps 1-9 for each database that is associated with the service application.
    
## See also
<a name="proc3"> </a>

#### Concepts

[Back up service applications in SharePoint Server](back-up-a-service-application.md)

