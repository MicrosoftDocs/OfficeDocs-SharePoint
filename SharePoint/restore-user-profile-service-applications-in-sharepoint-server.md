---
title: Restore User Profile Service applications in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: 9061f245-7b75-4211-af5f-b87ec09b5c82
---


# Restore User Profile Service applications in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-20* **Summary:** Learn how to restore the User Profile Service service application in SharePoint Server 2016 and SharePoint Server 2013.You can restore the User Profile Service application by using the SharePoint Central Administration website, Microsoft PowerShell, or SQL Server tools. Which backup tool you use depends on what kind of environment you have deployed, what your backup schedule requires, and what service level agreements you have made with your organization. 
> [!IMPORTANT:]

  
    
    

In this article:
-  [Before you begin](#begin)
    
  
-  [Using Windows PowerShell to restore the User Profile service application in SharePoint](#proc1)
    
  
-  [Using Central Administration to restore a User Profile service application in SharePoint](#proc2)
    
  
-  [Using SQL Server tools to restore the databases associated with the User Profile service application in SharePoint](#proc3)
    
  

## Before you begin
<a name="begin"> </a>

This article describes how to restore the User Profile Service application instead of restoring the complete farm.Before you begin this operation, review the following information about how to restore a User Profile service application:
- The User Profile service application provides data to other services and sites. As a result, users might experience some service interruption until the recovery process is completed.
    
  
- You cannot back up from one version of SharePoint Server and restore to another version of SharePoint Server.
    
  
- For information about how to at the same time restore all the service applications in a farm, see  [Restore farms in SharePoint Server](html/restore-farms-in-sharepoint-server.md).
    
  

## Using PowerShell to restore the User Profile service application in SharePoint Server
<a name="proc1"> </a>

You can use Microsoft PowerShell to restore a User Profile service application. **To restore the User Profile service application by using PowerShell**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.
    
    > [!NOTE:]
      
2. Start the SharePoint Management Shell.
    
  
3. At the PowerShell command prompt, type the following command:
    
  ```
  
Restore-SPFarm -Directory <BackupFolder>  -Item Shared Services\\Shared Services Applications\\<ServiceApplicationName>  -RestoreMethod Overwrite [-BackupId <GUID> ] [-Verbose]
  ```


    
    
    Where:
    
  -  *<BackupFolder>*  is the path of the folder where the backups are stored.
    
  
  -  *<ServiceApplicationName>*  is the name of the service application.
    
  
  -  *<GUID>*  is the identifier of the backup to use in the restore process.
    
  

    If you do not specify the BackupId, the most recent backup will be used. You cannot restore a service application from a configuration-only backup.
    
  
For more information, see **Restore-SPFarm**.
> [!NOTE:]

  
    
    


## Using Central Administration to restore a User Profile service application in SharePoint Server
<a name="proc2"> </a>

Use the following procedures to restore a User Profile service application by using the SharePoint Central Administration Web site. **To restore the User Profile service application by using Central Administration**
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators SharePoint group.
    
  
2. Start Central Administration.
    
  
3. In Central Administration, on the home page, in the **Backup and Restore** section, click **Restore from a backup**.
    
  
4. On the Restore from Backup — Step 1 of 3: Select Backup to Restore page, select the backup job that contains the service application backup, or a farm-level backup, from the list of backups, and then click **Next**. You can view more details about each backup by clicking the (+) next to the backup.
    
    > [!NOTE:]
      
5. On the Restore from Backup — Step 2 of 3: Select Component to Restore page, expand **Shared Services Applications**, select the check box that is next to the User Profile Service service application, and then click **Next**.
    
  
6. On the Restore from Backup — Step 3 of 3: Select Restore Options page, in the **Restore Component** section, make sure that **Farm\\Shared Services Applications\\<User Profile Service service application name>** appears in the **Restore the following component** list.
    
    In the **Restore Options** section, under **Type of restore**, select the **Same configuration** option. A dialog box will appear that asks you to confirm the operation. Click **OK**.
    
  
7. Click **Start Restore**.
    
  
8. You can view the general status of all recovery jobs at the top of the Backup and Restore Job Status page in the **Readiness** section. You can view the status for the current recovery job in the lower part of the page in the **Restore** section. The status page updates every 30 seconds automatically. You can manually update the status details by clicking **Refresh**. Backup and recovery are Timer service jobs. Therefore, it may take a several seconds for the recovery to start.
    
    If you receive any errors, you can review them in the **Failure Message** column of the Backup and Restore Job Status page. You can also find more details in the Sprestore.log file at the UNC path that you specified in step 3.
    
  

## Using SQL Server tools to restore the databases associated with the User Profile service application in SharePoint Server
<a name="proc3"> </a>

You cannot restore the complete service application or service application proxy by using SQL Server tools. However, you can use SQL Server tools to restore the databases that are associated with the service application. To restore the complete service application, use either PowerShell or Central Administration.
> [!IMPORTANT:]

  
    
    

 **To restore the databases associated with the User Profile service application by using SQL Server tools**
1. Verify that the user account that you are using to restore the databases is a member of the SQL Server  **sysadmin** fixed server role on the database server where each database is stored.
    
  
2. Start Central Administration.
    
  
3. In Central Administration, in the **System Settings** section, click **Manage services on server**.
    
  
4. On the Services on Server page, find **User Profile Service**. If the service is started, click **Stop** to stop the service.
    
  
5. Before you restore the User Profile Service service application databases, you must import the Microsoft Identity Integration Server (MIIS) encryption key that you exported before backing up the databases. You only have to do this one time for the restore process. To do this, on the server to which you are restoring the service application, type the following at the command prompt:
    
  ```
  
miiskmu.exe /i exported.key {<GUID> }
  ```


    Where  *<GIUD>*  is the identifier of the key.
    
  
6. Open SQL Server Management Studio and connect to the database server.
    
  
7. In Object Explorer, expand **Databases**.
    
  
8. Right-click the database that you want to restore, point to **Tasks**, and then click **Restore Database**.
    
  
9. In the **Restore Database** dialog box, on the **Options** page, select the kind of recovery that you want to perform from the **Recovery state** list.
    
    For more information about which recovery type to use, see  [ Recovery Models (SQL Server)](http://go.microsoft.com/fwlink/p/?LinkID=626889&amp;clcid=0x409).
    
  
10. On the **General** page, in the **Destination for restore** section, select the database from the **To database** list.
    
  
11. In the **Source for restore** section, select the backup source from the **From database** list.
    
  
12. Alternatively, if you have moved the backup files to another computer, select the **From device** option. If the correct backup is not listed in the **Select the backup sets to restore** box, browse to the file by clicking the ellipsis button.
    
  
13. Select the backup to restore from the **Select the backup sets to restore** box, and then click OK.
    
  
14. Click **OK** to restore the database.
    
  
15. Repeat steps 5-11 for the following databases associated with the User Profile Service service application (the names that are listed are the default names):
    
  - User Profile Service_ProfileDB_ *<GUID>* 
    
  
  - User Profile Service_SocialDB_ *<GUID>* 
    
  
  - User Profile Service_SyncDB_ *<GUID>* 
    
  
16. In Central Administration, in the **System Settings** section, click **Manage services on server**.
    
  
17. On the Services on Server page, find **User Profile Service**. If the service is stopped, click **Start** to start the service.
    
  

# See also

#### 

 [Restore solutions in SharePoint Server](html/restore-solutions-in-sharepoint-server.md)
  
    
    
 [Back up User Profile service applications in SharePoint Server](html/back-up-user-profile-service-applications-in-sharepoint-server.md)
  
    
    

#### 

 **Windows PowerShell for SharePoint Server 2016 reference**
  
    
    

  
    
    

