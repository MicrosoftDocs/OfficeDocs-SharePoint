---
title: "Back up farms in SharePoint Server"
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
ms.assetid: 8daa31a5-0f8c-4bd6-84c9-ee1f5074594d
description: "Learn how to back up a SharePoint Server farm."
---

# Back up farms in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
You can back up a SharePoint Server farm by using the SharePoint Central Administration website, Microsoft PowerShell, or SQL Server tools. The backup tool that you use depends on the kind of environment that you have deployed, your backup schedule requirements, and service level agreements that you have with your organization.
  
## Before you begin
<a name="begin"> </a>

We recommend that you regularly back up the complete farm by backing up both the configuration and content. Regularly backing up the farm reduces the possibility of data losses that might occur from hardware failures, power outages, or other problems. It is a simple process and helps so that all the farm data and configurations are available for recovery, if that is required.
  
For information about which tool to use for backups, see [Plan for backup and recovery in SharePoint Server](backup-and-recovery-planning.md).
  
Before you begin this operation, review the following information to help you prepare your farm backup:
  
- You must create a folder on the local computer or the network in which to store the backups. For better performance, we recommend that you back up to the local computer and then move the backup files to a network folder. For more information about how to create a backup folder, see [Prepare to back up and restore farms in SharePoint Server](prepare-to-back-up-and-restore.md).
    
- Performing a backup does not affect the state of the farm. However, it does require resources and might slightly affect farm performance when the backup is running. You can avoid performance issues by backing up the farm during hours when farm use is lowest, such as outside office hours.
    
- The farm backup process does not back up any certificates that you used to form trust relationships. Ensure that you have copies of these certificates before you back up the farm. You must re-establish these trust relationships after restoring the farm.
    
- Backing up the farm backs up the configuration and Central Administration content databases, but these cannot be restored using SharePoint Server tools. For more information about how to back up and restore all the farm databases, see [Move all databases in SharePoint Server](move-all-databases.md).
    
- When you back up a farm that contains a Web application that is configured to use forms-based authentication, you must also use a file backup system to protect the Web.config files because the Web.config files were updated manually to register the membership and role providers, and manual changes to the Web.config files are not backed up. Similarly, Web.config files are not restored when you restore a Web application. After recovery, you must update the Web.config files and redeploy the providers. For more information, see [Plan for user authentication methods in SharePoint Server](../security-for-sharepoint-server/plan-user-authentication.md).
    
- SharePoint Server backup backs up the Business Data Connectivity service external content type definitions but does not back up the data source itself. To protect the data, you should back up the data source when you back up the Business Data Connectivity service or the farm.
    
    If you restore the Business Data Connectivity service or the farm and then restore the data service to a different location, you must change the location information in the external content type definition. If you do not, the Business Data Connectivity service might be unable to locate the data source.
    
- SharePoint Server backup backs up remote Binary Large Object (BLOB) stores but only if you are using the FILESTREAM remote BLOB store provider to put data in remote BLOB stores.
    
    If you are using another provider, you must manually back up the remote BLOB stores.
    
- If you are using SQL Server with Transparent Data Encryption (TDE), and you are backing up your environment by using either SharePoint tools or SQL Server tools, the TDE encryption key in not backed up or restored. You must back up the key manually. When restoring, you must manually restore the key before you restore the data. For more information, see [Understanding Transparent Data Encryption (TDE)](http://go.microsoft.com/fwlink/p/?LinkID=715703&amp;clcid=0x409).
    
## Use PowerShell to back up a farm in SharePoint Server
<a name="begin"> </a>

You can use PowerShell to back up the farm manually or as part of a script that can be run at scheduled intervals.
  
 **To back up a farm by using PowerShell**
  
1. Verify that you have the following memberships:
    
   - **securityadmin** fixed server role on the SQL Server instance. 
    
   - **db_owner** fixed database role on all databases that are to be updated. 
    
   - Administrators group on the server on which you are running the PowerShell cmdlets.
    
     An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint Management Shell.
    
3. At the PowerShell command prompt, type the following command:
    
   ```powershell
   Backup-SPFarm -Directory <BackupFolder> -BackupMethod {Full | Differential} [-Verbose]
   ```

    Where:
    
   -  _\<BackupFolder\>_ is the path of a folder on the local computer or the network in which you want to store the backups. 
    
    > [!NOTE]
    > If you are backing up the farm for the first time, you must use the **Full** option. You must perform a full backup before you can perform a differential backup. 
  
For more information, see [Backup-SPFarm](/powershell/module/sharepoint-server/Backup-SPFarm?view=sharepoint-ps).
  
> [!NOTE]
> We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions. 
  
## Use Central Administration to back up a SharePoint Server farm
<a name="proc2"> </a>

You can use Central Administration to back up the farm.
  
 **To back up a farm by using Central Administration**
  
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators SharePoint group.
    
2. In Central Administration, on the home page, in the **Backup and Restore** section, click **Perform a backup**.
    
3. On the Perform a Backup — Step 1 of 2: Select Component to Back Up page, select the farm from the list of components, and then click **Next**.
    
4. On the Start Backup — Step 2 of 2: Select Backup Options page, in the **Backup Type** section, select either **Full** or **Differential**.
    
    > [!NOTE]
    > If you are backing up the farm for the first time, you must use the **Full** option. You must perform a full backup before you can perform a differential backup. 
  
5. In the **Back Up Only Configuration Settings** section, click **Back up content and configuration settings**.
    
6. In the **Backup File Location** section, type the UNC path of the backup folder, and then click **Start Backup**.
    
7. You can view the general status of all backup jobs at the top of the Backup and Restore Status page in the **Readiness** section. You can view the status for the current backup job in the lower part of the page in the **Backup** section. The status page updates every 30 seconds automatically. You can manually update the status details by clicking **Refresh**. Backup and recovery are Timer service jobs. Therefore, it may take several seconds for the backup to start.
    
    If you receive any errors, you can review them in the **Failure Message** column of the Backup and Restore Job Status page. You can also find more details in the Spbackup.log file at the UNC path that you specified in step 6. 
    
## Use SQL Server tools to back up a SharePoint Server farm
<a name="proc3"> </a>

If you want to back up the complete farm, you must use either PowerShell or Central Administration. You cannot back up the complete farm by using the SQL Server tools because you cannot use the tools to back up the farm's configuration. However, you can back up all the databases that are associated with the farm. The databases that are associated with the farm are determined by the services and features that you have installed on the farm.
  
 **To back up the databases associated with a farm by using SQL Server tools**
  
1. Verify that the user account that is performing this procedure is a member of the SQL Server **db_owner** fixed database role on all databases that are to be backed up. 
    
2. Open SQL Server Management Studio and connect to the correct instance of the SQL Server Database Engine.
    
3. In Object Explorer, expand **Databases**.
    
4. Right-click the database that you want to back up, point to **Tasks**, and then click **Back Up**.
    
5. In the **Back Up Database** dialog box, confirm the database name. 
    
6. Next, select the kind of backup that you want to perform from the **Backup type** list. For more information about which backup type to use, see [Recovery Models (SQL Server)](http://go.microsoft.com/fwlink/p/?LinkID=715706&amp;clcid=0x409).
    
7. In the **Backup component** area, click **Database**.
    
8. Either use the default name that is provided or specify a name for the backup set in the **Name** text box. 
    
9. In the **Destination** area, specify where you want to store the backup. 
    
10. Click **OK** to back up the database. 
    
11. Repeat steps 1-10 for each farm database.
    
## See also
<a name="proc3"> </a>


