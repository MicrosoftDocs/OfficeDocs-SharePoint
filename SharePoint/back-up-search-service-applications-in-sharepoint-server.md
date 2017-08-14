---
title: Back up Search service applications in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: 59c0540e-1238-4138-b98d-0d74ca59b9db
---


# Back up Search service applications in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-20* **Summary:** Learn how to back up Search service applications in SharePoint Server 2016 and SharePoint Server 2013.You can back up a Search service application in a farm by using the SharePoint Central Administration website, Microsoft PowerShell, or SQL Server tools. Which backup tool you use depends on what kind of environment you have deployed, what your backup schedule requires, and what service level agreements you have made with your organization.In this article:
-  [Before you begin](#begin)
    
  
-  [Backing up a thesaurus file](#back_up_thesaurus_files)
    
  
-  [Use Windows PowerShell to back up search in SharePoint](#proc1)
    
  
-  [Use Central Administration to back up search in SharePoint](#proc2)
    
  
-  [Use SQL Server tools to back up search](#proc3)
    
  

## Before you begin
<a name="begin"> </a>

We recommend that you regularly back up at the farm level. However, business or IT requirements might require you to back up the search service and related resources. Regularly backing up the search system reduces the possibility of data losses that might occur from hardware failures, power outages, or other problems. It is a simple process that helps make sure that data and configurations that compose the search system are available for recovery, if that is required.Before you begin this operation, review the following information:
- You must create a folder on the local computer or the network in which to store the backups. For better performance, we recommend that you back up to the local computer and then move the backup files to a network folder.
    
  
- You cannot use SQL Server tools or Data Protection Manager to back up all of the search components.
    
  
- Backing up search does not affect the state of the farm. However, it does require resources. Therefore, backing up search might affect farm performance while the backup is running. You can avoid performance issues by backing up search during hours when farm use is lowest.
    
  

## Back up a thesaurus file
<a name="back_up_thesaurus_files"> </a>

Thesaurus files are used to specify synonyms for words or phrases that occur in search queries. You create and maintain the thesaurus files in systems external to SharePoint Server before you import them into SharePoint Server to make them available to the search system. The thesaurus files are therefore not included in the SharePoint Server search backup procedures outlined below.To back up your thesaurus files, you need to make sure that they are included in the backup procedures for the external system you are using to create and maintain the thesaurus files.
## Use PowerShell to back up search in SharePoint Server
<a name="proc1"> </a>

You can use PowerShell to back up search manually or as part of a script that can be run at scheduled intervals. This procedure backs up all of the search components including the databases, the search service configuration, and all of the index files. **To back up search by using PowerShell**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  
  - Farm Administrators SharePoint group.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server Products cmdlets.
    
    > [!NOTE:]
      
2. Start the SharePoint Management Shell.
    
  
3. At the PowerShell command prompt, type the following command:
    
  ```
  
Backup-SPFarm -Directory <BackupFolder> -BackupMethod {Full | Differential} -Item "Farm\\Shared Services\\Shared Services Applications\\<SearchServiceApplicationName>" [-Verbose]
  ```


    
    
    Where:
    
  -  *<BackupFolder>*  is the path of the folder that you use for storing backup files.
    
  
  -  *<SearchServiceApplicationName>*  is the name of the Search service application that you are backing up.
    
  

    > [!NOTE:]
      
For more information, see **Backup-SPFarm**.
> [!NOTE:]

  
    
    


## Use Central Administration to back up search in SharePoint Server
<a name="proc2"> </a>

You can use Central Administration to back up search. This procedure backs up all of the search components including the databases, the search service configuration, and all of the index files. **To back up search by using Central Administration**
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators SharePoint group.
    
  
2. Start **Central Administration**.
    
  
3. In Central Administration, on the home page, in the **Backup and Restore** section, click **Perform a backup**.
    
  
4. On the Perform a Backup — Step 1 of 2: Select Component to Back Up page, in the list of components, expand **Shared Services** and then expand **Shared Services Applications** to view the list of service applications in the farm. Select the search service application from the list of components, and then click **Next**.
    
    > [!NOTE:]
      
5. On the Start Backup — Step 2 of 2: Select Backup Options page, in the ** Backup Type** section, select either **Full** or **Differential**.
    
    > [!NOTE:]
      
6. In the **Backup File Location** section, in the **Backup location** box, type the path of the backup folder, and then click **Start Backup**.
    
  
7. You can view the general status of all backup jobs at the top of the Backup and Restore Job Status page in the **Readiness** section. You can view the status for the current backup job in the lower part of the page in the **Backup** section. The status page updates every 30 seconds automatically. You can manually update the status details by clicking **Refresh**. Backup and recovery are timer service jobs. Therefore, it might take several seconds for the backup to start.
    
    If you receive any errors, you can review them in the **Failure Message** column of the Backup and Restore Job Status page. You can also find more details in the Spbackup.log file at the UNC path that you specified in step 6.
    
  

## Use SQL Server tools to back up search
<a name="proc3"> </a>

You cannot back up the complete SharePoint Search service application by using SQL Server tools. However, you can use SQL Server tools to back up the databases that are associated with the Search service application. To back up the complete Search service application, use either PowerShell or Central Administration.To use SQL Server to back up the databases that are associated with the Search service application, you must follow these steps:
1. Pause the Search service application.
    
  
2. Back up all the Search service application databases with SQL Server tools.
    
  
3. Resume the Search service application.
    
  
 **To pause the Search service application by using PowerShell**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint 2016 cmdlets.
    
    > [!NOTE:]
      
2. Start the SharePoint Management Shell.
    
  
3. At the PowerShell command prompt, type the following command:
    
  ```
  
$ssa = Get-SPEnterpriseSearchServiceApplication -Identity <SearchServiceApplicationName> Suspend-SPEnterpriseSearchServiceApplication -Identity $ssa
  ```


    
    
    Where:
    
  -  *<SearchServiceApplicationName>*  is the name of the Search service application that you are backing up.
    
  
 **To back up all the Search service application databases by using SQL Server tools**
1. Verify that the user account that is performing this procedure is a member of the SQL Server **db_backupoperator** fixed database role on the database server where each database is stored.
    
  
2. Start SQL Server Management Studio and connect to the database server.
    
  
3. In Object Explorer, expand **Databases**.
    
  
4. Right-click the database that you want to back up, point to **Tasks**, and then click **Back Up**.
    
  
5. In the **Back Up Database** dialog box, confirm the database name.
    
  
6. Next, select the kind of backup that you want to perform from the **Backup type** list. For more information about which backup type to use, see [Recovery Models (SQL Server)](http://go.microsoft.com/fwlink/p/?LinkID=626889&amp;clcid=0x409) in SQL Server Books Online.
    
  
7. In the **Backup component** area, click **Database**..
    
  
8. Either use the default name that is provided or specify a name for the backup set in the **Name** text box.
    
  
9. In the Destination area, specify where you want to store the backup.
    
  
10. Click **OK** to back up the database.
    
  
11. Repeat steps 1-10 for the following databases:
    
  - Search Administration
    
  
  - Analytics Reporting
    
  
  - Crawl
    
  
  - Link
    
  
 **To resume the Search service application by using PowerShell**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.
    
    > [!NOTE:]
      
2. Start the SharePoint Management Shell.
    
  
3. At the PowerShell command prompt, type the following command:
    
  ```
  
$ssa = Get-SPEnterpriseSearchServiceApplication -Identity <SearchServiceApplicationName> Resume-SPEnterpriseSearchServiceApplication -Identity $ssa
  ```


    
    
    Where:
    
  -  *<SearchServiceApplicationName>*  is the name of the Search service application.
    
  

# See also

#### 

 [Restore Search service applications in SharePoint Server](html/restore-search-service-applications-in-sharepoint-server.md)
  
    
    

  
    
    

