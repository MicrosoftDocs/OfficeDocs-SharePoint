---
title: Restore site collections in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: f8f81869-a51f-4d7f-b4b6-52dd99078c23
---


# Restore site collections in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Foundation 2013, SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-25* **Summary:** Learn how to restore a single site collection in SharePoint Server 2016 and SharePoint Server 2013.You can only restore a site collection in SharePoint Server by using PowerShell.In this article:
-  [Using Windows PowerShell to restore a site collection in SharePoint](#proc1)
    
  -  [To restore a site collection by using Windows PowerShell](#PS)
    
  

## Using PowerShell to restore a site collection in SharePoint Server
<a name="proc1"> </a>

You can use PowerShell to restore a site collection manually or as part of a script that can be run at scheduled intervals. **To restore a site collection by using PowerShell**
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
    
    If you are restoring a host-named site collection, use the Identity parameter to specify the URL of the host-named site collection and use theHostHeader parameter to specify the URL of the Web application that will hold the host-named site collection.
    
    If you want to overwrite an existing site collection, use the Force parameter.
    
    > [!NOTE:]
      
For more information, see **Restore-SPSite**.
> [!NOTE:]

  
    
    


# See also

#### 

 [Back up site collections in SharePoint Server](html/back-up-site-collections-in-sharepoint-server.md)
  
    
    

  
    
    

