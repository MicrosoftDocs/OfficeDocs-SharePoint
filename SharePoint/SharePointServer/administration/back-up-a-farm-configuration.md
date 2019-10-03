---
title: "Back up farm configurations in SharePoint Server"
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
ms.assetid: a6d383c0-3817-4acd-afa9-ad7a9b7e6b5a
description: "Learn how to back up farm configurations in SharePoint Server."
---

# Back up farm configurations in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
You can back up a farm configuration by using the SharePoint Central Administration website or Microsoft PowerShell. The backup tool that you use depends on the kind of environment that you have deployed, your backup schedule requirements, and service level agreements that you have with your organization.
  
## Before you begin
<a name="begin"> </a>

We recommend that you regularly back up the complete farm by backing up both the configuration and content. However, you might want to perform configuration-only backups in test or development environments. Similarly, if you are using SQL Server tools to back up the databases for the farm, you will want to back up the configuration. Regularly backing up the farm reduces the possibility of data losses that can occur from hardware failures, power outages, or other problems. It helps make sure that all the farm data and configurations are available for recovery. For more information about what to back up, see [Plan for backup and recovery in SharePoint Server](backup-and-recovery-planning.md).
  
For information about which tool to use for backups, see [Overview of backup and recovery in SharePoint Server](backup-and-recovery-overview.md).
  
Before you begin this operation, review the following information:
  
- You must create a folder on the local computer or the network in which to store the backups. For better performance, we recommend that you back up to the local computer and then move the backup files to a network folder. For more information about how to create a backup folder, see [Prepare to back up and restore farms in SharePoint Server](prepare-to-back-up-and-restore.md).
    
- Backing up the farm configuration will not back up the information that you need to restore service applications. If you want to restore a service application, you must perform a configuration and content backup of the farm. For more information about how to back up service applications, see [Back up service applications in SharePoint Server](back-up-a-service-application.md).
    
- You cannot use either SQL Server tools or Data Protection Manager to back up the farm configuration.
    
## Use PowerShell to back up a SharePoint farm configuration
<a name="begin"> </a>

You can use PowerShell to back up the configuration from any configuration database on the current farm, on another farm, or from a configuration database that is not associated with any farm. You can back up a farm configuration manually or as part of a script that can be run at scheduled intervals.
  
 **To back up the configuration from any configuration database by using PowerShell**
  
1. Verify that you have the following memberships:
    
   - **securityadmin** fixed server role on the SQL Server instance. 
    
   - **db_owner** fixed database role on all databases that are to be updated. 
    
   - Administrators group on the server on which you are running the PowerShell cmdlets.
    
     An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server Products cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint Management Shell.
    
3. At the PowerShell command prompt, type the following command:
    
   ```powershell
   Backup-SPConfigurationDatabase -Directory <BackupFolder> -DatabaseServer <DatabaseServerName> -DatabaseName <DatabaseName> -DatabaseCredentials <WindowsPowerShellCredentialObject> [-Verbose]
   ```

    Where:
    
   -  _\<BackupFolder\>_ is the path to the folder that has the correct backup files. 
    
   -  _\<DatabaseServerName\>_ is the name of the database server for the farm that you are backing up. 
    
   -  _\<DatabaseName\>_ is the name of the farm configuration database. 
    
   - If you are not logged on with an account with **db_backupoperator** fixed database role on the database server where the configuration database is stored, you must specify the value for  `DatabaseCredentials` parameter. 
    
For more information, see [Backup-SPConfigurationDatabase](/powershell/module/sharepoint-server/Backup-SPConfigurationDatabase?view=sharepoint-ps).
  
> [!NOTE]
> We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions. 
  
## Use Central Administration to back up a SharePoint farm configuration
<a name="proc2"> </a>

You can use Central Administration to back up the configuration of the farm that Central Administration is running on. To back up the configuration of a remote farm, you must use the Central Administration Web site that is running on the remote farm. You cannot use Central Administration to back up an unattached configuration database.
  
 **To back up a farm configuration by using Central Administration**
  
1. Verify that the user account performing this procedure is a member of the Farm Administrators group.
    
2. On the Central Administration home page, in the **Backup and Restore** section, click **Perform a backup**.
    
3. On the Perform a Backup — Step 1 of 2: Select Component to Back Up page, select the farm from the list of components, and then click **Next**.
    
    > [!NOTE]
    > You can back up the configuration for any service or application. However, common practice is to back up configuration at the farm level. 
  
4. On the Start Backup — Step 2 of 2: Select Backup Options page, in the **Backup Type** section, select **Full**.
    
5. In the **Backup Only Configuration Settings** section, select the **Backup only configuration settings** option. 
    
6. In the **Backup File Location** section, type the Universal Naming Convention (UNC) path of the backup folder, and then click **Start Backup**.
    
7. You can view the general status of all backup jobs at the top of the Backup and Restore Job Status page in the **Readiness** section. You can view the status for the current backup job in the lower part of the page in the **Backup** section. The status page updates every 30 seconds automatically. You can manually refresh the status details by clicking **Refresh**. Backup and recovery are Timer service jobs. Therefore, it may take several seconds for the backup to start.
    
    If you receive any errors, you can review them in the **Failure Message** column of the Backup and Restore Job Status page. You can also find more details in the Spbackup.log file at the UNC path that you specified in step 5. 
    
## See also
<a name="proc2"> </a>

#### Concepts

[Restore farm configurations in SharePoint Server](restore-a-farm-configuration.md)

