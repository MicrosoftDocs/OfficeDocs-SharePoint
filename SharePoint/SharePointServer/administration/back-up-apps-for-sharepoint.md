---
title: "Back up apps for SharePoint in SharePoint Server"
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
ms.assetid: a193cfdb-ac5e-45fa-bf83-87849e38ac27
description: "Learn how to back up apps for SharePoint in SharePoint Server."
---

# Back up apps for SharePoint in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
We recommend that you regularly back up at the farm level. However, business or IT requirements might require you to back up the apps for SharePoint in addition to normal farm backups. If you regularly back up the apps for SharePoint environment, you reduce the possibility of data losses that might occur from hardware failures, power outages, or other problems. It is a simple process that helps make sure that data and configurations that compose the apps for SharePoint environment are available for recovery, if that is required. 
  
The app for SharePoint content and packages are in the SharePoint Server content databases in individual site collections. All app for SharePoint license and security data is stored in the App Management Service and the Secure Store Service application databases. Additional app for SharePoint data is stored in the SharePoint Server configuration database, in the form of Internet Information Services (IIS) web sites or web applications, and Web Part packages. You must back up the following SharePoint Server databases at the same time:
  
- Content - WSS_Content
    
- Configuration - SharePoint_Config
    
- Secure Store Service application - Secure_Store_Service_DB_\<GUID\>
    
- App Management service application - App_Management_\<GUID\>
    
If you have to eventually restore the databases, you have to restore the same version of each database that you backed up. In other words, don't restore a content database that's six months older than the configuration database.
  
You can back up an apps for SharePoint environment by using the SharePoint Central Administration website, Microsoft PowerShell, or SQL Server tools.
  
    
## Back up content databases
<a name="proc1"> </a>

Content databases can store data for multiple site collections. However, if you have many site collections, we recommend that you add enough content databases to keep the size of each database below 200 GB for optimal system performance. For more information, see [Back up content databases in SharePoint Server](back-up-a-content-database.md).
  
> [!NOTE]
> SharePoint Server content databases become very large. We recommend that you back up each content database as a separate process from other database or farm backups. 
  
## Back up the configuration database
<a name="proc2"> </a>

The SharePoint Server configuration database stores data about all SharePoint databases and Internet Information Services (IIS) web sites or web applications. This includes trusted solutions, web part packages, site templates, and web application settings, and farm settings that are specific to SharePoint Server, such as default quota and blocked file types. For more information, see [Back up farm configurations in SharePoint Server](back-up-a-farm-configuration.md).
  
## Back up the Secure Store Service application database
<a name="proc3"> </a>

The Secure Store Service database stores and maps credentials such as account names and passwords. To back up the Secure Store database for an apps for SharePoint environment, see [Back up the Secure Store Service in SharePoint Server](back-up-the-secure-store-service.md).
  
> [!NOTE]
> Make sure that you record the passphrase when you back up the Secure Store database. You must have the passphrase available to restore the Secure Store database. 
  
## Back up the App Management service application database
<a name="proc4"> </a>

The App Management service application database stores the app licenses and permissions for all apps downloaded from the App Catalog site in SharePoint Server. To back up the App Management database, follow the same procedures as most other SharePoint Server service applications. For more information, see [Back up service applications in SharePoint Server](back-up-a-service-application.md).
  
## Back up a site collection
<a name="proc5"> </a>

You may have multiple site collections that host apps for SharePoint in your environment. When you backup apps for SharePoint you must also back up all site collections where the apps are hosted.
  
 **To back up a site collection by using PowerShell**
  
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
   Backup-SPSite -Identity <SiteCollectionGUIDorURL> -Path <BackupFile> [-Force] [-NoSiteLock] [-UseSqlSnapshot] [-Verbose]
   ```

    Where:
    
   -  _\<SiteCollectionGUIDorURL\>_ is the ID or URL for the site collection you want to back up. 
    
   -  _\<BackupFile\>_ is the path of where the backup file is located. 
    
    If you want to overwrite a previously used backup file, use the  `Force` parameter. You can use the  `NoSiteLock` parameter to keep the read-only lock from being set on the site collection while it is being backed up. However, using this parameter can enable users to change the site collection while it is being backed up and could lead to possible data corruption during backup. To display the site collection GUID or URL at the PowerShell command prompt, type the following command: 
    
   ```powershell
   Get-SPSite | format-list -property id,url
   ```

    If the database server is running an Enterprise Edition of SQL Server, we recommend that you also use the  `UseSqlSnapshot` parameter for more consistent backups. You can also export sites or lists from these snapshots. 
    
    > [!NOTE]
    > If the RBS provider that you are using does not support snapshots, you can't use snapshots for content deployment or backup. For example, the SQL FILESTREAM provider does not support snapshots. 
  
    For more information about how to use SQL snap-shots, see [Back up databases to snapshots in SharePoint Server](back-up-databases-to-snapshots.md).
    
    For more details, see [Back up site collections in SharePoint Server](back-up-site-collections.md)
    
    For more information, see [Backup-SPSite](/powershell/module/sharepoint-server/backup-spsite?view=sharepoint-ps).
    
> [!NOTE]
> We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions. 
  
## See also
<a name="proc5"> </a>

#### Concepts

[Plan for backup and recovery in SharePoint Server](backup-and-recovery-planning.md)
  
[Restore apps for SharePoint in SharePoint Server](restore-apps-for-sharepoint.md)

