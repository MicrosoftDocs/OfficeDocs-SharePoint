---
title: Flush the BLOB cache in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: b35d9b02-2207-417c-bb90-870474b6f57c
---


# Flush the BLOB cache in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-19* **Summary: ** Learn how to clear the contents of the BLOB cache for a web application in SharePoint Server 2016 and SharePoint Server 2013.A BLOB cache is a disk-based cache that stores binary large objects (BLOBs) such as frequently used image, audio, and video files, and other files that are used to display web pages. Each SharePoint front-end server maintains its own BLOB cache. When you enable a BLOB cache, you specify the file types to include in the cache and also the location of the BLOB cache. The first time that a BLOB file is requested, the file is copied from the database to the BLOB cache on the front-end server. Future requests to the front-end server for that same file are then served from the file that is stored in the BLOB cache, instead of being served from the database. This reduces the network traffic and the load on the database server. For more information about BLOB caches, see  [Plan for caching and performance in SharePoint Server](html/plan-for-caching-and-performance-in-sharepoint-server.md).
## Flush the BLOB cache
<a name="flush"> </a>

When you flush the BLOB cache, you clear the contents of the BLOB cache for a web application. This is useful if the BLOB cache becomes out of sync with the content. For example, after you restore a content database, the BLOB cache will be out of sync with the content. To correct that situation, you must flush the BLOB cache. The following procedure describes how to flush the BLOB cache for a web application.
> [!CAUTION:]

  
    
    


> [!NOTE:]

  
    
    

 **To flush the BLOB cache**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running PowerShell cmdlets.
    
  
  - Add memberships that are required beyond the minimums above.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.
    
    > [!NOTE:]
      
2. Copy the following code and paste it into a text editor, such as Notepad.
    
  ```
  
$webApp = Get-SPWebApplication "<WebApplicationURL> "
[Microsoft.SharePoint.Publishing.PublishingCache]::FlushBlobCache($webApp)
Write-Host "Flushed the BLOB cache for:" $webApp
  ```

3. Replace  *<WebApplicationURL>*  with the URL of the web application whose BLOB cache you want to clear.
    
  
4. Save the file, and name it FlushBLOBCache.ps1.
    
    > [!NOTE:]
      
5. Open **SharePoint Management Shell**.
    
  
6. Change to the directory where you saved the file.
    
  
7. At the Microsoft PowerShell command prompt, type the following command.
    
  ```
  
./FlushBLOBCache.ps1
  ```


# See also

#### 

 [Scripting with Windows PowerShell](https://go.microsoft.com/fwlink/p/?LinkId=193051)
  
    
    

  
    
    

