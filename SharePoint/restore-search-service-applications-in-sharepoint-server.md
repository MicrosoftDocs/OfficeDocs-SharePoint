---
title: Restore Search service applications in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: f50ca1b2-5075-49f6-9689-46c7b8a29b47
---


# Restore Search service applications in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-20* **Summary:** Learn how to restore the Search service application in SharePoint Server 2016 and SharePoint Server 2013.You can restore search by using the SharePoint Central Administration website, Microsoft PowerShell, or SQL Server tools. The restore tool that you use depends on the kind of environment that you have deployed, your schedule requirements, and service level agreements that you have made with your organization. In this article:
-  [Before you begin](#begin)
    
  
-  [Restore a thesaurus file](#restore_thesaurus_files)
    
  
-  [Use Windows PowerShell to restore SharePoint Search service application](#proc1)
    
  
-  [Use Central Administration to restore SharePoint Search service application](#proc2)
    
  
-  [Use SQL Server tools to restore the databases for a Search service application](#proc3)
    
  

## Before you begin
<a name="begin"> </a>

There are situations in which you might have to restore a specific service application instead of restoring the complete farm. Some service applications — for example, the SharePoint Search service application, Business Data Connectivity service application, and the User Profile Service service application — provide data to other services and sites. As a result, users might experience some service interruption until the recovery process is completed.Before you begin this operation, review the following information:
- Backing up and restoring search does not affect the state of the farm. However, it does require resources. Therefore, backup and restore for search might affect farm performance while the backup is running. You can avoid performance issues by backing up search during hours when farm use is lowest.
    
  
- You cannot restore the complete service application by using SQL Server tools. However, you can restore the databases that are associated with the service application.
    
  

## Restore a thesaurus file
<a name="restore_thesaurus_files"> </a>

Thesaurus files are used to specify synonyms for words or phrases that occur in search queries. You create and maintain the thesaurus files in systems external to SharePoint Server before you import them into SharePoint Server to make them available to the search system. The thesaurus files are therefore not included in the default SharePoint Server search backup procedures, and also not in the search recovery procedures outlined below. **To restore a thesaurus file**
1. Follow one of the procedures below to restore the SharePoint Server Search service application.
    
  
2. If necessary, restore the thesaurus file using the restore procedures for the external system you are using to create and maintain thesaurus files.
    
  
3. Import the thesaurus file to the SharePoint Server search system by using the Import-SPEnterpriseSearchThesaurus PowerShell cmdlet as described in  [Deploy a thesaurus dictionary](create-and-deploy-a-thesaurus-in-sharepoint-server.md#proc2).
    
  

## Use PowerShell to restore a SharePoint Search service application
<a name="proc1"> </a>

You can use PowerShell to restore a service application. **To restore a Search service application by using PowerShell**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  
  - Farm Administrators SharePoint group.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.
    
    > [!NOTE:]
      
2. Make sure that the server you are restoring to use the same drive mapping as the server where you created the backup.
    
  
3. Start the SharePoint Management Shell.
    
  
4. At the PowerShell command prompt, type the following command:
    
  ```
  
Restore-SPFarm -Directory <BackupFolder>  -Item "<ServiceApplicationName> " -RestoreMethod Overwrite [-BackupId <GUID> ] [-Verbose]
  ```


    
    
    Where:
    
  -  *<BackupFolder>*  is the path for the backup folder where the service application was backed up.
    
  
  -  *<ServiceApplicationName>*  is the name the service application.
    
  
  -  *<GUID>*  is the ID of the backup to use.
    
  

    To specify which backup to use, use the BackupId parameter. You can view the backups for the farm by typing the following:Get-SPBackupHistory -Directory <BackupFolder> -ShowBackup. If you do not specify the BackupId, the most recent backup will be used. You cannot restore a service application from a configuration-only backup.
    
    To restore all the service applications, at the PowerShell command prompt, type the following command:
    


  ```
  Restore-SPFarm -Directory <BackupFolder>  -Item "Farm\\Shared Service Applications" -RestoreMethod Overwrite [-BackupId <GUID> ] [-Verbose]
  ```


    Where:
    
  -  *<BackupFolder>*  is the path for the backup folder where the service application was backed up.
    
  
  -  *<GUID>*  is the ID of the backup to use.
    
  

    For more information, see **Restore-SPFarm**.
    
  
5. When you restore a Search service application, it is automatically paused. To resume the Search service application when the restore has completed, type the following command: 
    
  ```
  $ssa = Get-SPEnterpriseSearchServiceApplication <SearchServiceApplicationName> $ssa.ForceResume(0x02)
  ```


    Where:
    
  -  *<SearchServiceApplicationName>*  is the name the service application you want to resume.
    
  

> [!NOTE:]

  
    
    


> [!NOTE:]

  
    
    


## Use Central Administration to restore a SharePoint Search service application
<a name="proc2"> </a>

Use the following procedure to restore a search service application by using the SharePoint Central Administration website. **To restore a Search service application by using Central Administration**
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators SharePoint group.
    
  
2. Make sure that the server you are restoring to use the same drive mapping as the server where you created the backup.
    
  
3. Start Central Administration.
    
  
4. In Central Administration, on the home page, in the **Backup and Restore** section, click **Restore from a backup**.
    
  
5. On the Restore from Backup — Step 1 of 3: Select Backup to Restore page, select the backup job that contains the service application backup, or a farm-level backup, from the list of backups, and then click **Next**. You can view more details about each backup by clicking the (+) next to the backup.
    
    > [!NOTE:]
      
6. On the Restore from Backup — Step 2 of 3: Select Component to Restore page, expand **Shared Services Applications**, select the check box that is next to the Search service application, and then click **Next**. To restore all the service applications, select the **Shared Services Applications** node.
    
  
7. On the Restore from Backup — Step 3 of 3: Select Restore Options page, in the **Restore Component** section, make sure that **Farm\\Shared Services Applications\\<Service application>** appears in the **Restore the following component** list.
    
    In the **Restore Options** section, under **Type of restore**, select the **Same configuration** option. A dialog box will appear that asks you to confirm the operation. Click **OK**.
    
    Click **Start Restore**.
    
  
8. You can view the general status of all recovery jobs at the top of the Backup and Restore Job Status page in the **Readiness** section. You can view the status for the current recovery job in the lower part of the page in the **Restore** section. The status page updates every 30 seconds automatically. You can manually update the status details by clicking **Refresh**. Backup and recovery are Timer service jobs. Therefore, it may take a several seconds for the recovery to start.
    
    If you receive any errors, you can review them in the **Failure Message** column of the Backup and Restore Job Status page. You can also find more details in the Sprestore.log file at the UNC path that you specified in step 3.
    
  
9. When you restore a Search service application, it is automatically paused. To resume the Search service application when the restore has completed you need to use PowerShell:
    
1. Verify that you have the following memberships:
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.
    
    > [!NOTE:]
      
2. Start the SharePoint Management Shell.
    
  
3. At the PowerShell command prompt, type the following command:
    
  ```
  
$ssa = Get-SPEnterpriseSearchServiceApplication <SearchServiceApplicationName>
$ssa.ForceResume(0x02)

  ```


    Where:
    
  -  *<SearchServiceApplicationName>*  is the name the service application you want to resume.
    
  

> [!NOTE:]

  
    
    


## Use SQL Server tools to restore the databases for a Search service application
<a name="proc3"> </a>

You cannot restore the complete SharePoint Search service application by using SQL Server tools. However, you can use SQL Server tools to restore the databases that are associated with the service application. To restore the complete Search service application, use either PowerShell or Central Administration. **To restore the databases for a Search service application by using SQL Server tools**
1. Verify that the user account that you are using to restore the databases is a member of the SQL Server **sysadmin** fixed server role on the database server where each database is stored.
    
  
2. Open SQL Server Management Studio and connect to the database server.
    
  
3. In Object Explorer, expand **Databases**.
    
  
4. Right-click the database that you want to restore, point to **Tasks**, point to **Restore**, and then click **Database**.
    
  
5. In the **Restore Database** dialog box, on the General page, select the database to restore to from the **To database** drop-down list.
    
  
6. Select the restore source from the **From database** drop-down list.
    
  
7. In the **Select the backup sets to restore section** area, select the check box next to the database.
    
  
8. On the Options tab, select the recovery state from the **Recover state** section.
    
    For more information about which recovery type to use, see  [ Recovery Models (SQL Server)](http://go.microsoft.com/fwlink/p/?LinkID=626889&amp;clcid=0x409).
    
  
9. Click **OK** to restore the database.
    
  
10. Repeat steps 1-9 for each database that is associated with the service application.
    
  

# See also

#### 

 [Back up Search service applications in SharePoint Server](html/back-up-search-service-applications-in-sharepoint-server.md)
  
    
    

  
    
    

