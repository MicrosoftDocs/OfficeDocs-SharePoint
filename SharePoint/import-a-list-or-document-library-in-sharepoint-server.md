---
title: Import a list or document library in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: b3cb17a1-939c-4314-9f83-3c6b8a309bba
---


# Import a list or document library in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Foundation 2013, SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-24* **Summary:** Learn how to import a site, list, or document library in SharePoint Server 2016 and SharePoint Server 2013.You can import a site, list, or document library in SharePoint Server by using PowerShell.In this article:
-  [Before you begin](#begin)
    
  
-  [Importing a site, list, or document library in SharePoint](#proc1)
    
  -  [To import a site, list or document library by using Windows PowerShell](#PS)
    
  

## Before you begin
<a name="begin"> </a>

Although you can use either PowerShell or Central Administration to export a site, list, or document library, you can use only PowerShell to import a site, list, or document library. For information about how to export lists or libraries, see  [Export sites, lists, or document libraries in SharePoint Server](html/export-sites-lists-or-document-libraries-in-sharepoint-server.md).Before you begin this operation, review the following information:
- You can use importing as a method of restoring the items, or as a method of moving or copying the items from one farm to another farm. You can import a site, list, or document library from a backup of the current farm, from a backup of another farm, or from a read-only content database. To import from a read-only content database, you must first attach the read-only database. For more information, see  [Attach and restore read-only content databases in SharePoint Server](html/attach-and-restore-read-only-content-databases-in-sharepoint-server.md).
    
  
- You cannot import a site, list or document library exported from one version of SharePoint Server to another version of SharePoint Server.
    
  

## Importing a site, list, or document library in SharePoint Server
<a name="proc1"> </a>

You can use PowerShell to manually import a site, list, or document library or as part of a script that can be run regularly. **To import a site, list or document library by using PowerShell**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.
    
    > [!NOTE:]
      
2. Start the SharePoint Management Shell.
    
  
3. At the PowerShell command prompt, type the following command:
    
  ```
  
Import-SPWeb -Identity  <SiteURL>  -Path <ImportFileName>  [-Force] [-NoFileCompression] [-Verbose]
  ```


    
    
    Where:
    
  -  *<SiteURL>*  is the URL for the site that you are importing to.
    
  
  -  *<ImportFileName>*  is the name of the file that you are exporting from.
    
  

    > [!IMPORTANT:]
      

    You can also use the Get-SPWeb cmdlet and pass the ID toImport-SPWeb by using the PowerShell pipeline. The value of thePath parameter specifies the path and file name of the file from which to import the list or library. To include the user security settings with the list or document library, use theIncludeUserSecurity parameter. To overwrite the list or library that you specified, use theForce parameter. You can use theUpdateVersions parameter to specify how versioning conflicts will be handled. To view the progress of the operation, use theVerbose parameter.
    
    The NoFileCompression parameter lets you specify that no file compression is performed during the import process. Using this parameter can lower resource usage up to 30% during the export and import process. If you are importing a site, list, or document library that you exported from Central Administration, or if you exported a site, list, or document library by using PowerShell and you did not use theNoFileCompression parameter in theExport-SPWeb cmdlet, you cannot use this parameter in theImport-SPWeb cmdlet.
    
    > [!NOTE:]
      
For more information, see **Import-SPWeb**.
> [!NOTE:]

  
    
    


# See also

#### 

 [Export sites, lists, or document libraries in SharePoint Server](html/export-sites-lists-or-document-libraries-in-sharepoint-server.md)
  
    
    

  
    
    

