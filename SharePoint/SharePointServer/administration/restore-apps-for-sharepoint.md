---
title: "Restore apps for SharePoint in SharePoint Server"
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
ms.assetid: 73e8ee39-0865-497a-b9e2-a0b0b46cde20
description: "Learn how to restore apps for SharePoint in SharePoint Server."
---

# Restore apps for SharePoint in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
You can restore an apps for SharePoint environment by using the SharePoint Central Administration website, Microsoft PowerShell, or SQL Server tools. The restore tool that you use depends on the kind of environment that you have deployed, your schedule requirements, and service level agreements that you have with your organization. 
  
The app for SharePoint content and packages are stored in the SharePoint Server content databases in individual site collections. The restore process requires you to restore all services that the app references. The apps for SharePoint can reference the following SharePoint Server databases which you may have to restore. You should also restore the site collection where the app for SharePoint is located if you are restoring the apps for SharePoint to the same environment.
  
- Content
    
- Configuration
    
- Secure Store Service application
    
- App Management service application
    
    
## Before you begin
<a name="begin"> </a>

Content databases can store data for multiple site collections. If you have apps for SharePoint hosted in many site collections you may also have multiple content databases. To back up and restore all of the apps for SharePoint in your environment, you must back up and restore all content databases and site collections in the farm. 
  
## Restore content databases
<a name="proc1"> </a>

You can restore a single content database or several content databases one at a time. For information about how to restore a content database in a farm, see [Restore content databases in SharePoint Server](restore-a-content-database.md). For information about how to back up and restore all the content databases in a farm at the same time, see [Back up farms in SharePoint Server](back-up-a-farm.md).
  
## Restore the configuration database
<a name="proc2"> </a>

In SharePoint Server you do not have to restore the configuration database because you can restore the farm configuration directly. For more information, see [Restore farm configurations in SharePoint Server](restore-a-farm-configuration.md).
  
## Restore the Secure Store Service application database
<a name="proc3"> </a>

The Secure Store Service database stores and maps credentials to specific identities or a group of identities. You must have the passphrase that was recorded when the Secure Store Service was backed up to restore it. To restore the Secure Store database, see [Restore Secure Store Service applications in SharePoint Server](restore-a-secure-store-service-application.md).
  
## Restore the App Management service application database
<a name="proc4"> </a>

The App Management service application database stores the app licenses and permissions for all apps downloaded from the App Catalog site in SharePoint Server. You must restore this database to make sure that the apps for SharePoint licenses and permissions are available in your farm. To restore the App Management database, follow the same procedures as most other SharePoint Server service applications. For more information, see [Restore service applications in SharePoint Server](restore-a-service-application.md).
  
## Restore a site collection
<a name="proc5"> </a>

You can only restore a site collection in SharePoint Server by using PowerShell. Use this section to restore a site collection that contains apps for SharePoint to the same SharePoint Server environment. To restore to a new farm, see [Restore apps for SharePoint to a new farm](#more).
  
> [!CAUTION]
> Any apps for SharePoint that contain remote components that are present on the backup copy of a site collection could cause problems. This is because two copies of the app for SharePoint are accessing the remote connection and can cause information disclosure or data loss. For example, when a site collection in a production environment is copied by a backup for a development purpose, this could unintentionally grant developers access to production data in remote sites if the app for SharePoint is not designed correctly. 
  
 **To restore a site collection by using PowerShell**
  
1. Verify that you have the following memberships:
    
   - **securityadmin** fixed server role on the SQL Server instance. 
    
   - **db_owner** fixed database role on all databases that are to be updated. 
    
   - Administrators group on the server on which you are running the PowerShell cmdlets.
    
     An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint Management Shell.
    
3. At the PowerShell command prompt, type the following command:
    
   ```
   Restore-SPSite -Identity <SiteCollectionURL> -Path <Backup file> [-DatabaseServer <DatabaseServerName>] [-DatabaseName <ContentDatabaseName>] [-HostHeader <Host header>] [-Force] [-GradualDelete] [-Verbose]
   ```

    Where:
    
   -  _\<SiteCollectionURL\>_ is URL for the site collection you want to restore. 
    
   -  _\<DatabaseServerName\>_ is name of the database server where the site collection resides. 
    
   -  _\<ContentDatabaseName\>_ is the name of the content database. 
    
    If you want to restore the site collection to a specific content database, use the  `DatabaseServer` and  `DatabaseName` parameters to specify the content database. If you do not specify a content database, the site collection will be restored to a content database chosen by SharePoint Server. 
    
    If you are restoring a host-named site collection, use the  `Identity` parameter to specify the URL of the host-named site collection and use the  `HostHeader` parameter to specify the URL of the web application that will hold the host-named site collection. 
    
    If you want to overwrite an existing site collection, use the  `Force` parameter. 
    
    > [!NOTE]
    > If the site collection that you are restoring is 1 gigabyte or larger, you can use the  `GradualDelete` parameter for better performance during the restore process. When this parameter is used, the site collection that is overwritten is marked as deleted, which immediately prevents any additional access to its content. The data in the marked site collection is then deleted gradually over time by a timer job instead of all at the same time, which reduces the effect on server performance. 
  
    For more information, see [Restore site collections in SharePoint Server](restore-site-collections.md)
    
    For more information, see [Restore-SPSite](/powershell/module/sharepoint-server/Restore-SPSite?view=sharepoint-ps).
    
    > [!NOTE]
    > We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions. 
  
## Restore apps for SharePoint to a new farm
<a name="more"> </a>

To restore apps for SharePoint to a new farm you must also backup and restore any services that the app references. These SharePoint Server service applications can include the Secure Store Service service application, Access Services in SharePoint, and the App Management Service. For more information, see the following articles:
  
- [Restore Secure Store Service applications in SharePoint Server](restore-a-secure-store-service-application.md)
    
- [Restore service applications in SharePoint Server](restore-a-service-application.md)
    
## See also
<a name="more"> </a>

#### Concepts

[Back up apps for SharePoint in SharePoint Server](back-up-apps-for-sharepoint.md)
  
[Restore content databases in SharePoint Server](restore-a-content-database.md)
  
[Restore site collections in SharePoint Server](restore-site-collections.md)

