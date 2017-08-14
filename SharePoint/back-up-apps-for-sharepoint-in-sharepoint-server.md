---
title: Back up apps for SharePoint in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: a193cfdb-ac5e-45fa-bf83-87849e38ac27
---


# Back up apps for SharePoint in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** apps for SharePoint, SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-14* **Summary:** Learn how to back up apps for SharePoint Server in SharePoint Server 2013 and SharePoint Server 2016.We recommend that you regularly back up at the farm level. However, business or IT requirements might require you to back up the apps for SharePoint in addition to normal farm backups. If you regularly back up the apps for SharePoint environment, you reduce the possibility of data losses that might occur from hardware failures, power outages, or other problems. It is a simple process that helps make sure that data and configurations that compose the apps for SharePoint environment are available for recovery, if that is required. The app for SharePoint content and packages are in the SharePoint ServerUNRESOLVED_TOKEN_VAL() content databases in individual site collections. All app for SharePoint license and security data is stored in the App Management Service and the Secure Store Service application databases. Additional app for SharePoint data is stored in the SharePoint Server configuration database, in the form of Internet Information Services (IIS) web sites or web applications, and Web Part packages. You must back up the following SharePoint Server databases at the same time:
- Content - WSS_Content
    
  
- Configuration - SharePoint_Config
    
  
- Secure Store Service application - Secure_Store_Service_DB_<GUID>
    
  
- App Management service application - App_Management_<GUID>
    
  
If you have to eventually restore the databases, you have to restore the same version of each database that you backed up. In other words, don't restore a content database that's six months older than the configuration database.For more information about the SharePoint Server databases, see  [Database types and descriptions in SharePoint Server](html/database-types-and-descriptions-in-sharepoint-server.md). You can back up an apps for SharePoint environment by using the SharePoint Central Administration website, Microsoft PowerShell, or SQL Server tools.In this article:
-  [Back up content databases](#proc1)
    
  
-  [Back up the configuration database](#proc2)
    
  
-  [Back up the Secure Store Service application database](#proc3)
    
  
-  [Back up the App Management service application database](#proc4)
    
  
-  [Back up a site collection](#proc5)
    
  -  [To back up a site collection by using Windows PowerShell](#PS)
    
  

## Back up content databases
<a name="proc1"> </a>

Content databases can store data for multiple site collections. However, if you have many site collections, we recommend that you add enough content databases to keep the size of each database below 200 GB for optimal system performance. For more information, see  [Back up content databases in SharePoint Server](html/back-up-content-databases-in-sharepoint-server.md).
> [!NOTE:]

  
    
    


## Back up the configuration database
<a name="proc2"> </a>

The SharePoint Server configuration database stores data about all SharePoint databases and Internet Information Services (IIS) web sites or web applications. This includes trusted solutions, web part packages, site templates, and web application settings, and farm settings that are specific to SharePoint Server, such as default quota and blocked file types. For more information, see  [Back up farm configurations in SharePoint Server](html/back-up-farm-configurations-in-sharepoint-server.md).
## Back up the Secure Store Service application database
<a name="proc3"> </a>

The Secure Store Service database stores and maps credentials such as account names and passwords. To back up the Secure Store database for an apps for SharePoint environment, see  [Back up the Secure Store Service in SharePoint Server](html/back-up-the-secure-store-service-in-sharepoint-server.md).
> [!NOTE:]

  
    
    


## Back up the App Management service application database
<a name="proc4"> </a>

The App Management service application database stores the app licenses and permissions for all apps downloaded from the App Catalog site in SharePoint Server. To back up the App Management database, follow the same procedures as most other SharePoint Server service applications. For more information, see  [Back up service applications in SharePoint Server](html/back-up-service-applications-in-sharepoint-server.md).
## Back up a site collection
<a name="proc5"> </a>

You may have multiple site collections that host apps for SharePoint in your environment. When you backup apps for SharePoint you must also back up all site collections where the apps are hosted. **To back up a site collection by using PowerShell**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.
    
    > [!NOTE:]
      
2. Start the SharePoint Management Shell.
    
  
3. At the PowerShell command prompt, type the following command:
    
  ```
  
Backup-SPSite -Identity <SiteCollectionGUIDorURL> -Path <BackupFile> [-Force] [-NoSiteLock] [-UseSqlSnapshot] [-Verbose]
  ```


    
    
    Where:
    
  -  *<SiteCollectionGUIDorURL>*  is the ID or URL for the site collection you want to back up.
    
  
  -  *<BackupFile>*  is the path of where the backup file is located.
    
  

    If you want to overwrite a previously used backup file, use the Force parameter. You can use theNoSiteLock parameter to keep the read-only lock from being set on the site collection while it is being backed up. However, using this parameter can enable users to change the site collection while it is being backed up and could lead to possible data corruption during backup. To display the site collection GUID or URL at the PowerShell command prompt, type the following command:
    


  ```
  Get-SPSite | format-list -property id,url
  ```


    If the database server is running an Enterprise Edition of SQL Server, we recommend that you also use the UseSqlSnapshot parameter for more consistent backups. You can also export sites or lists from these snapshots.
    
    > [!NOTE:]
      

    For more information about how to use SQL snap-shots, see  [Back up databases to snapshots in SharePoint Server](html/back-up-databases-to-snapshots-in-sharepoint-server.md).
    
    For more details, see  [Back up site collections in SharePoint Server](html/back-up-site-collections-in-sharepoint-server.md)
    
  
For more information, see **Backup-SPSite**.
> [!NOTE:]

  
    
    


# See also

#### 

 [Plan for backup and recovery in SharePoint Server](html/plan-for-backup-and-recovery-in-sharepoint-server.md)
  
    
    
 [Restore apps for SharePoint in SharePoint Server](html/restore-apps-for-sharepoint-in-sharepoint-server.md)
  
    
    

  
    
    

