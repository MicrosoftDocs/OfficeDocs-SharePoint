---
title: Restore apps for SharePoint in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: 73e8ee39-0865-497a-b9e2-a0b0b46cde20
---


# Restore apps for SharePoint in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** apps for SharePoint, SharePoint Foundation 2013, SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-25* **Summary:** Learn how to restore apps for SharePoint in SharePoint Server 2016 and SharePoint Server 2013.You can restore an apps for SharePoint environment by using the SharePoint Central Administration website, Microsoft PowerShell, or SQL Server tools. The restore tool that you use depends on the kind of environment that you have deployed, your schedule requirements, and service level agreements that you have with your organization. The app for SharePoint content and packages are stored in the SharePoint Server content databases in individual site collections. The restore process requires you to restore all services that the app references. The apps for SharePoint can reference the following SharePoint Server databases which you may have to restore. You should also restore the site collection where the app for SharePoint is located if you are restoring the apps for SharePoint to the same environment.
- Content
    
  
- Configuration
    
  
- Secure Store Service application
    
  
- App Management service application
    
  
For more information about the SharePoint Server databases, see  [Database types and descriptions in SharePoint Server](html/database-types-and-descriptions-in-sharepoint-server.md). In this article:
-  [Before you begin](#begin)
    
  
-  [Restore content databases](#proc1)
    
  
-  [Restore the configuration database](#proc2)
    
  
-  [Restore the Secure Store Service application database](#proc3)
    
  
-  [Restore the App Management service application database](#proc4)
    
  
-  [Restore a site collection](#proc5)
    
  
-  [Restore apps for SharePoint to a new farm](#more)
    
  

## Before you begin
<a name="begin"> </a>

Content databases can store data for multiple site collections. If you have apps for SharePoint hosted in many site collections you may also have multiple content databases. To back up and restore all of the apps for SharePoint in your environment, you must back up and restore all content databases and site collections in the farm. 
## Restore content databases
<a name="proc1"> </a>

You can restore a single content database or several content databases one at a time. For information about how to restore a content database in a farm, see  [Restore content databases in SharePoint Server](html/restore-content-databases-in-sharepoint-server.md). For information about how to back up and restore all the content databases in a farm at the same time, see  [Back up farms in SharePoint Server](html/back-up-farms-in-sharepoint-server.md).
## Restore the configuration database
<a name="proc2"> </a>

In SharePoint Server you do not have to restore the configuration database because you can restore the farm configuration directly. For more information, see  [Restore farm configurations in SharePoint Server](html/restore-farm-configurations-in-sharepoint-server.md).
## Restore the Secure Store Service application database
<a name="proc3"> </a>

The Secure Store Service database stores and maps credentials to specific identities or a group of identities. You must have the passphrase that was recorded when the Secure Store Service was backed up to restore it. To restore the Secure Store database, see  [Restore Secure Store Service applications in SharePoint Server](html/restore-secure-store-service-applications-in-sharepoint-server.md).
## Restore the App Management service application database
<a name="proc4"> </a>

The App Management service application database stores the app licenses and permissions for all apps downloaded from the App Catalog site in SharePoint Server. You must restore this database to make sure that the apps for SharePoint licenses and permissions are available in your farm. To restore the App Management database, follow the same procedures as most other SharePoint Server service applications. For more information, see  [Restore service applications in SharePoint Server](html/restore-service-applications-in-sharepoint-server.md).
## Restore a site collection
<a name="proc5"> </a>

You can only restore a site collection in SharePoint Server by using PowerShell. Use this section to restore a site collection that contains apps for SharePoint to the same SharePoint Server environment. To restore to a new farm, see  [Restore apps for SharePoint to a new farm](#more).
> [!CAUTION:]

  
    
    

 **To restore a site collection by using PowerShell**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.
    
    > [!NOTE:]
      
2. Start the SharePoint Management Shell.
    
  
3. At the PowerShell command prompt, type the following command:
    
  ```
  
Restore-SPSite -Identity <SiteCollectionURL> -Path <Backup file> [-DatabaseServer <DatabaseServerName>] [-DatabaseName <ContentDatabaseName>] [-HostHeader <Host header>] [-Force] [-GradualDelete] [-Verbose]
  ```


    
    
    Where:
    
  -  *<SiteCollectionURL>*  is URL for the site collection you want to restore.
    
  
  -  *<DatabaseServerName>*  is name of the database server where the site collection resides.
    
  
  -  *<ContentDatabaseName>*  is the name of the content database.
    
  

    If you want to restore the site collection to a specific content database, use the DatabaseServer andDatabaseName parameters to specify the content database. If you do not specify a content database, the site collection will be restored to a content database chosen by SharePoint Server.
    
    If you are restoring a host-named site collection, use the Identity parameter to specify the URL of the host-named site collection and use theHostHeader parameter to specify the URL of the web application that will hold the host-named site collection.
    
    If you want to overwrite an existing site collection, use the Force parameter.
    
    > [!NOTE:]
      

    For more information, see  [Restore site collections in SharePoint Server](html/restore-site-collections-in-sharepoint-server.md)
    
    For more information, see **Restore-SPSite**.
    
    > [!NOTE:]
      

## Restore apps for SharePoint to a new farm
<a name="more"> </a>

To restore apps for SharePoint to a new farm you must also backup and restore any services that the app references. These SharePoint Server service applications can include the Secure Store Service service application, Access Services in SharePoint, and the App Management Service. For more information, see the following articles:
-  [Restore Secure Store Service applications in SharePoint Server](html/restore-secure-store-service-applications-in-sharepoint-server.md)
    
  
-  [Restore service applications in SharePoint Server](html/restore-service-applications-in-sharepoint-server.md)
    
  

# See also

#### 

 [Back up apps for SharePoint in SharePoint Server](html/back-up-apps-for-sharepoint-in-sharepoint-server.md)
  
    
    
 [Restore content databases in SharePoint Server](html/restore-content-databases-in-sharepoint-server.md)
  
    
    
 [Restore site collections in SharePoint Server](html/restore-site-collections-in-sharepoint-server.md)
  
    
    

  
    
    

