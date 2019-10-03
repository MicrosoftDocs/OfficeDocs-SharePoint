---
title: "Back up web applications in SharePoint Server"
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
ms.assetid: e0ad657d-f5d1-4cae-bb0d-d2b619eed261
description: "Learn how to back up a web application in SharePoint Server by using Central Administration or Microsoft PowerShell."
---

# Back up web applications in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
You can back up a web application by using the SharePoint Central Administration website, PowerShell, or SQL Server tools. The backup tool that you use depends on the kind of environment that you have deployed, your backup schedule requirements, and service level agreements that you have with your organization. 
  
## Before you begin
<a name="begin"> </a>

Regularly backing up a web application reduces the possibility of data losses that might occur from hardware failures, power outages, or other problems. It is a simple process that can help make sure that all the web application-related data and configurations are available for recovery, if that is required. We recommend that web application backups be created in addition to regular backups at the farm level.
  
Before you begin this operation, review the following information:
  
- Before you begin, you must create a network folder in which to store the backups. Both the SharePoint Timer Service (SPTimerV4) service account and the server farm user account must have Full Control permissions to this folder. For more information about how to create a backup folder, see [Prepare to back up and restore farms in SharePoint Server](prepare-to-back-up-and-restore.md).
    
- You can back up only one web application at a time by using the procedures in this article. You can back up all web applications by backing up the complete farm.
    
- Backing up a web application does not affect the state of the farm. However, it does require resources and might slightly affect farm performance when the backup is running. You can avoid performance issues by backing up the web application during hours when farm use is lowest, such as outside office hours.
    
- If the web application uses the object cache, you must manually configure two special user accounts for the web application after you restore the web application. 
    
- When you back up a web application, the Internet Information Services (IIS) settings and all content databases that are associated with the web application are also backed up.
    
- When you back up a web application that is configured to use forms-based authentication, you must also use a file backup system to protect the Web.config files because the Web.config files were updated manually to register the membership and role providers, and manual changes to the Web.config files are not backed up. Similarly, Web.config files are not restored when you restore a Web application. After recovery, you must update the Web.config files and redeploy the providers. For more information, see [Plan for user authentication methods in SharePoint Server](../security-for-sharepoint-server/plan-user-authentication.md).
    
## Use PowerShell to back up a web application
<a name="begin"> </a>

You can use PowerShell to back up a web application manually or as part of a script that can be run at scheduled intervals.
  
 **To back up a web application by using PowerShell**
  
1. Verify that you have the following memberships:
    
   - **securityadmin** fixed server role on the SQL Server instance. 
    
   - **db_owner** fixed database role on all databases that are to be updated. 
    
    > [!NOTE]
    > Alternately, the user can be a member of the **db_backupoperator** fixed database role on all databases that are to be updated if you do not want to assign full rights of the **db_owner** role. 
  
   - Administrators group on the server on which you are running the PowerShell cmdlets.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint Management Shell.
    
3. At the PowerShell command prompt, type the following command:
    
   ```powershell
   Backup-SPFarm -Directory <BackupFolder> -BackupMethod {Full | Differential} -Item <WebApplicationName> [-Verbose]
   ```

    Where:
    
   -  _\<BackupFolder\>_ is the path of the folder that you use for storing backup files. 
    
   -  _\<WebApplicationName\>_ is the name of the web application. To display the name of the web application, at the PowerShell command prompt, type the following command:  `Backup-SPFarm -ShowTree`
    
    > [!NOTE]
    > If you are backing up the web application for the first time, you must use the  `Full` option. You must perform a full backup before you can perform a differential backup. 
  
For more information, see [Backup-SPFarm.](/powershell/module/sharepoint-server/Backup-SPFarm?view=sharepoint-ps). 
  
> [!NOTE]
> We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions. 
  
## Use Central Administration to back up a web application
<a name="proc2"> </a>

You can use Central Administration to back up a web application.
  
 **To back up a web application by using Central Administration**
  
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
2. Start Central Administration.
    
3. In Central Administration, on the home page, in the **Backup and Restore** section, click **Perform a backup**.
    
4. On the Perform a Backup — Step 1 of 2: Select Component to Back Up page, select the web application from the list of components, and then click **Next**.
    
    > [!NOTE]
    > The web application might consist of several components. You must select the top-level component. 
  
5. On the Start Backup — Step 2 of 2: Select Backup Options page, in the **Backup Type** section, select either **Full** or **Differential**.
    
    > [!NOTE]
    > If you are backing up the web application for the first time, you must use the **Full** option. You must perform a full backup before you can perform a differential backup. 
  
6. In the **Back Up Only Configuration Settings** section, click **Back up content and configuration settings**.
    
7. In the **Backup File Location** section, type the Universal Naming Convention (UNC) path of the backup folder, and then click **Start Backup**.
    
8. You can view the general status of all backup jobs at the top of the Backup and Restore Job Status page in the **Readiness** section. You can view the status for the current backup job in the lower part of the page in the **Backup** section. The status page updates every 30 seconds automatically. You can manually update the status details by clicking **Refresh**. Backup and recovery are Timer service jobs. Therefore, it may take several seconds for the backup to start.
    
    If you receive any errors, you can review them in the **Failure Message** column of the Backup and Restore Job Status page. You can also find more details in the Spbackup.log file at the UNC path that you specified in step 6. 
    
## Use SQL Server tools to back up a databases that are associated with a web application
<a name="proc3"> </a>

You cannot back up the complete web application by using SQL Server tools. However, you can back up all the databases that are associated with the web application. To back up the complete web application, use either PowerShell or Central Administration.
  
 **To back up a database associated with a web application by using SQL Server tools**
  
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

#### Concepts

[Restore web applications in SharePoint Server](restore-a-web-application.md)
  
[Back up farms in SharePoint Server](back-up-a-farm.md)
  
[Plan for backup and recovery in SharePoint Server](backup-and-recovery-planning.md)
  


