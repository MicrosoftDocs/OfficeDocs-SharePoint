---
title: "Back up Search service applications in SharePoint Server"
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
ms.assetid: 59c0540e-1238-4138-b98d-0d74ca59b9db
description: "Learn how to back up Search service applications in SharePoint Server."
---

# Back up Search service applications in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
You can back up a Search service application in a farm by using the SharePoint Central Administration website, Microsoft PowerShell, or SQL Server tools. Which backup tool you use depends on what kind of environment you have deployed, what your backup schedule requires, and what service level agreements you have made with your organization.
  
    
## Before you begin
<a name="begin"> </a>

We recommend that you regularly back up at the farm level. However, business or IT requirements might require you to back up the search service and related resources. Regularly backing up the search system reduces the possibility of data losses that might occur from hardware failures, power outages, or other problems. It is a simple process that helps make sure that data and configurations that compose the search system are available for recovery, if that is required.
  
Before you begin this operation, review the following information:
  
- You must create a folder on the local computer or the network in which to store the backups. For better performance, we recommend that you back up to the local computer and then move the backup files to a network folder.
    
- You cannot use SQL Server tools or Data Protection Manager to back up all of the search components.
    
- Backing up search does not affect the state of the farm. However, it does require resources. Therefore, backing up search might affect farm performance while the backup is running. You can avoid performance issues by backing up search during hours when farm use is lowest.
    
## Back up a thesaurus file
<a name="back_up_thesaurus_files"> </a>

Thesaurus files are used to specify synonyms for words or phrases that occur in search queries. You create and maintain the thesaurus files in systems external to SharePoint Server before you import them into SharePoint Server to make them available to the search system. The thesaurus files are therefore not included in the SharePoint Server search backup procedures outlined below.
  
To back up your thesaurus files, you need to make sure that they are included in the backup procedures for the external system you are using to create and maintain the thesaurus files.
  
## Use PowerShell to back up search in SharePoint Server
<a name="proc1"> </a>

You can use PowerShell to back up search manually or as part of a script that can be run at scheduled intervals. This procedure backs up all of the search components including the databases, the search service configuration, and all of the index files.
  
 **To back up search by using PowerShell**
  
1. Verify that you have the following memberships:
    
   - **securityadmin** fixed server role on the SQL Server instance. 
    
   - **db_owner** fixed database role on all databases that are to be updated. 
    
   - Administrators group on the server on which you are running the PowerShell cmdlets.
    
   - Farm Administrators SharePoint group.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server Products cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint Management Shell.
    
3. At the PowerShell command prompt, type the following command:
    
   ```powershell
   Backup-SPFarm -Directory <BackupFolder> -BackupMethod {Full | Differential} -Item "Farm\Shared Services\Shared Services Applications\<SearchServiceApplicationName>" [-Verbose]
   ```

    Where:
    
   -  _\<BackupFolder\>_ is the path of the folder that you use for storing backup files. 
    
   -  _\<SearchServiceApplicationName\>_ is the name of the Search service application that you are backing up. 
    
    > [!NOTE]
    > If you are backing up the farm for the first time, you must use the **Full** option. You must perform a full backup before you can perform a differential backup. To view the progress of the backup operation, use the **Verbose** parameter. The **Differential** option only applies to the search databases. The search index files are always fully backed up, even when you use the **Differential** option. 
  
For more information, see [Backup-SPFarm](/powershell/module/sharepoint-server/Backup-SPFarm?view=sharepoint-ps). 
  
> [!NOTE]
> We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions. 
  
## Use Central Administration to back up search in SharePoint Server
<a name="proc2"> </a>

You can use Central Administration to back up search. This procedure backs up all of the search components including the databases, the search service configuration, and all of the index files. 
  
 **To back up search by using Central Administration**
  
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators SharePoint group.
    
2. Start **Central Administration**.
    
3. In Central Administration, on the home page, in the **Backup and Restore** section, click **Perform a backup**.
    
4. On the Perform a Backup — Step 1 of 2: Select Component to Back Up page, in the list of components, expand **Shared Services** and then expand **Shared Services Applications** to view the list of service applications in the farm. Select the search service application from the list of components, and then click **Next**.
    
    > [!NOTE]
    > The search service application might consist of several components. You must select the top-level component. By default, the service application is named "Search Service Application". 
  
5. On the Start Backup — Step 2 of 2: Select Backup Options page, in the **Backup Type** section, select either **Full** or **Differential**.
    
    > [!NOTE]
    > If you are backing up search for the first time, you must use the **Full** option. You must perform a full backup before you can perform a differential backup. The **Differential** option only applies to the search databases. The search index files are always fully backed up, even when you use the **Differential** option. 
  
6. In the **Backup File Location** section, in the **Backup location** box, type the path of the backup folder, and then click **Start Backup**.
    
7. You can view the general status of all backup jobs at the top of the Backup and Restore Job Status page in the **Readiness** section. You can view the status for the current backup job in the lower part of the page in the **Backup** section. The status page updates every 30 seconds automatically. You can manually update the status details by clicking **Refresh**. Backup and recovery are timer service jobs. Therefore, it might take several seconds for the backup to start.
    
    If you receive any errors, you can review them in the **Failure Message** column of the Backup and Restore Job Status page. You can also find more details in the Spbackup.log file at the UNC path that you specified in step 6. 
    
## Use SQL Server tools to back up search
<a name="proc3"> </a>

You cannot back up the complete SharePoint Search service application by using SQL Server tools. However, you can use SQL Server tools to back up the databases that are associated with the Search service application. To back up the complete Search service application, use either PowerShell or Central Administration.
  
To use SQL Server to back up the databases that are associated with the Search service application, you must follow these steps:
  
1. Pause the Search service application.
    
2. Back up all the Search service application databases with SQL Server tools.
    
3. Resume the Search service application.
    
### To pause the Search service application by using PowerShell

1. Verify that you have the following memberships:
    
   - **securityadmin** fixed server role on the SQL Server instance. 
    
   - **db_owner** fixed database role on all databases that are to be updated. 
    
   - Administrators group on the server on which you are running the PowerShell cmdlets.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint 2016 cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint Management Shell.
    
3. At the PowerShell command prompt, type the following command:
    
   ```powershell
   $ssa = Get-SPEnterpriseSearchServiceApplication -Identity <SearchServiceApplicationName> 
   Suspend-SPEnterpriseSearchServiceApplication -Identity $ssa
   ```

    Where:
    
   -  _\<SearchServiceApplicationName\>_ is the name of the Search service application that you are backing up. 
    
### To back up all the Search service application databases by using SQL Server tools

1. Verify that the user account that is performing this procedure is a member of the SQL Server **db_backupoperator** fixed database role on the database server where each database is stored. 
    
2. Start SQL Server Management Studio and connect to the database server.
    
3. In Object Explorer, expand **Databases**.
    
4. Right-click the database that you want to back up, point to **Tasks**, and then click **Back Up**.
    
5. In the **Back Up Database** dialog box, confirm the database name. 
    
6. Next, select the kind of backup that you want to perform from the **Backup type** list. For more information about which backup type to use, see [Recovery Models (SQL Server)](http://go.microsoft.com/fwlink/p/?LinkID=715706&amp;clcid=0x409). 
    
7. In the **Backup component** area, click **Database**..
    
8. Either use the default name that is provided or specify a name for the backup set in the **Name** text box. 
    
9. In the Destination area, specify where you want to store the backup.
    
10. Click **OK** to back up the database. 
    
11. Repeat steps 1-10 for the following databases:
    
  - Search Administration
    
  - Analytics Reporting
    
  - Crawl
    
  - Link
    
### To resume the Search service application by using PowerShell

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
   $ssa = Get-SPEnterpriseSearchServiceApplication -Identity <SearchServiceApplicationName> 
   Resume-SPEnterpriseSearchServiceApplication -Identity $ssa
   ```

    Where:
    
   -  _\<SearchServiceApplicationName\>_ is the name of the Search service application. 
    
## See also
<a name="proc3"> </a>

#### Concepts

[Restore Search service applications in SharePoint Server](restore-a-search-service-application.md)

