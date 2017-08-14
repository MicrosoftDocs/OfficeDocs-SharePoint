---
title: Disable RBS on content databases in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: 75096f60-b94e-44c2-bc84-8aa3e2c4fff3
---


# Disable RBS on content databases in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Foundation 2013, SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-19* **Summary:** Learn how to disable Remote BLOB Storage (RBS) on any SharePoint Server 2016 and SharePoint Server 2013 content database.You can disable Remote BLOB Storage (RBS) on any content database. After you disable RBS on a content database, binary large objects (BLOBs) are stored inline in SQL Server for all subsequent writes to the content database. This article describes how to disable RBS on a content database.You can disable RBS on a content database by setting the active provider name to the empty string in Microsoft PowerShell. Each content database has a **RemoteBlobStorageSettings** property that can be used to invoke the **SetActiveProviderName** method.This action does not change the storage location of any BLOBs that have previously been stored in RBS or inline storage. Disabling RBS does not uninstall RBS. We do not recommend that you uninstall RBS.Before you begin this operation, review the following information about prerequisites:
## Disable RBS for a content database
<a name="proc1"> </a>

This operation can be performed on any Web server in the farm. You only have to perform the operation one time on one Web server for each content database for which you want to disable RBS.
> [!CAUTION:]

  
    
    

You must use Windows PowerShell 3.0 cmdlets to disable RBS. There is no user interface option for this task. **To disable RBS by using PowerShell**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  
2. Start the SharePoint Management Shell.
    
  
3. At the PowerShell command prompt, type the following commands:
    
  ```
  
$site=Get-SPSite "<http://yourSiteURL> "
$rbss=$site.ContentDatabase.RemoteBlobStorageSettings
$rbss.SetActiveProviderName("")
  ```


    Where  *<http://yourSiteURL>*  is the Web application that is attached to the content database that is being disabled for RBS.
    
    For more information, see **Get-SPSite**.
    
  

# See also

#### 

 [Set a content database to use RBS with FILESTREAM in SharePoint Server](html/set-a-content-database-to-use-rbs-with-filestream-in-sharepoint-server.md)
  
    
    

  
    
    

