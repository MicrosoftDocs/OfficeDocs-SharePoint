---
title: "Back up service applications in SharePoint Server"
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
ms.assetid: 96dc4ef1-cec8-47d0-b995-46bca3e8eda2
description: "Learn how to back up a service application in SharePoint Server."
---

# Back up service applications in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
You can back up a service application by using the SharePoint Central Administration website or Microsoft PowerShell. Which backup tool you use depends on what kind of environment you have deployed, what your backup schedule requires, and what service level agreements you have made with your organization.
  
    
## Before you begin
<a name="begin"> </a>

We recommend that you regularly back up at the farm level. However, business or IT requirements might require you to back up a service application. Regularly backing up a service application reduces the possibility of data losses that might occur from hardware failures, power outages, or other problems. It is a simple process that helps make sure that all the service application-related data and configurations are available for recovery, if that is required. You can back up one service application at a time, or you can back up all service applications at the same time. For information about what to back up and which tools to use, see [Plan for backup and recovery in SharePoint Server](backup-and-recovery-planning.md). For more information, see [Back up farms in SharePoint Server](back-up-a-farm.md).
  
Backing up a service application does not affect the state of the farm. However, it does require resources. Therefore, backing up a service application might affect farm performance while the backup is running. You can avoid performance issues by backing up the service application during hours when farm use is lowest.
  
> [!NOTE]
> SharePoint Server backup backs up remote Binary Large Object (BLOB) stores but only if you are using the FILESTREAM remote BLOB store provider to put data in remote BLOB stores. If you are using another provider, you must manually back up the remote BLOB stores. 
  
Before you begin this operation, review the following information about prerequisites:
  
- You must create a folder on the local computer or the network in which to store the backups. For better performance, we recommend that you back up to the local computer and then move the backup files to a network folder. For more information about how to create a backup folder, see [Prepare to back up and restore farms in SharePoint Server](prepare-to-back-up-and-restore.md).
    
- SharePoint Server backup backs up the SQL Server Remote BLOB Store installation package from the Feature Pack for SQL Server 2008 R2 external content type definitions but does not back up the data source itself. To protect the data, you should back up the data source when you back up the SQL Server Remote BLOB Store installation package from the Feature Pack for SQL Server 2008 R2 or the farm.
    
- If you back up the SQL Server Remote BLOB Store installation package from the Feature Pack for SQL Server 2008 R2 or the farm and then restore the data source to a different location, you must change the location information in the external content type definition. If you do not, the SQL Server Remote BLOB Store installation package from the Feature Pack for SQL Server 2008 R2 might be unable to locate the data source.
    
## Use PowerShell to back up a service application in SharePoint
<a name="proc1"> </a>

You can use PowerShell to back up one or more service applications manually or as part of a script that can be run at scheduled intervals. 
  
 **To back up a service application by using PowerShell**
  
1. Verify that you have the following memberships:
    
   - **securityadmin** fixed server role on the SQL Server instance. 
    
   - **db_owner** fixed database role on all databases that are to be updated. 
    
   - Administrators group on the server on which you are running the PowerShell cmdlets.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server 2016 cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint Management Shell.
    
3. At the PowerShell command prompt, type the following command:
    
   ```powershell
   Backup-SPFarm -Directory <BackupFolder> -BackupMethod {Full | Differential} -Item <ServiceApplicationName> [-Verbose]
   ```

    Where:
    
   -  _\<BackupFolder\>_ is the path of a folder on the local computer or on the network in which you want to store the backups. 
    
   -  _\<ServiceApplicationName\>_ is the name of the service application that you want to back up. To display the name of the service application, at the PowerShell command prompt, type the following command:  `Backup-SPFarm -ShowTree`.
    
    To back up all the service applications, at the PowerShell command prompt, type the following command:
    
   ```powershell
   Backup-SPFarm -Directory <BackupFolder> -BackupMethod {Full | Differential} -Item "Farm\Shared Services" [-Verbose]
   ```

    > [!NOTE]
    > If you are backing up the service application for the first time, you must use the **Full** option. You must perform a full backup before you can perform a differential backup. Some service applications always require a full backup. For these service applications, even if you select the **Differential** option, the system performs a full backup. 
  
For more information, see [Backup-SPFarm](/powershell/module/sharepoint-server/Backup-SPFarm?view=sharepoint-ps).
  
> [!NOTE]
> We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions. 
  
## Use Central Administration to back up a service application in SharePoint
<a name="proc2"> </a>

You can use Central Administration to back up a service application.
  
 **To back up a service application by using Central Administration**
  
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators SharePoint group.
    
2. Start Central Administration.
    
3. In Central Administration, on the home page, in the **Backup and Restore** section, click **Perform a backup**.
    
4. On the Perform a Backup — Step 1 of 2: Select Component to Back Up page, select the service application from the list of components, and then click **Next**. To back up all the service applications, select the **Shared Service Applications** node. 
    
    > [!NOTE]
    > The service application might consist of several components. You must select the top-level component. 
  
5. On the Start Backup — Step 2 of 2: Select Backup Options page, in the **Backup Type** section, select either **Full** or **Differential**.
    
    > [!NOTE]
    > If you are backing up the service application for the first time, you must use the **Full** option. You must perform a full backup before you can perform a differential backup. Some service applications always require a full backup. For these service applications, the system performs a full backup even if you select the **Differential** option. 
  
6. In the **Backup File Location** section, in the **Backup location box**, type the path of the backup folder, and then click **Start Backup**.
    
7. You can view the general status of all backup jobs at the top of the Backup and Restore Job Status page in the **Readiness** section. You can view the status for the current backup job in the lower part of the page in the **Backup** section. The status page updates every 30 seconds automatically. You can manually update the status details by clicking **Refresh**. Backup and recovery are Timer service jobs. Therefore, it may take several seconds for the backup to start.
    
    If you receive any errors, you can review them in the **Failure Message** column of the Backup and Restore Job Status page. You can also find more details in the Spbackup.log file at the UNC path that you specified in step 5. 
    
## See also
<a name="proc2"> </a>

#### Concepts

[Restore service applications in SharePoint Server](restore-a-service-application.md)

