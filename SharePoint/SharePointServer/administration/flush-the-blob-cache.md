---
title: "Flush the BLOB cache in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/20/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: b35d9b02-2207-417c-bb90-870474b6f57c
description: "Learn how to clear the contents of the BLOB cache for a web application in SharePoint Server."
---

# Flush the BLOB cache in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
A BLOB cache is a disk-based cache that stores binary large objects (BLOBs) such as frequently used image, audio, and video files, and other files that are used to display web pages. Each SharePoint front-end server maintains its own BLOB cache. When you enable a BLOB cache, you specify the file types to include in the cache and also the location of the BLOB cache. The first time that a BLOB file is requested, the file is copied from the database to the BLOB cache on the front-end server. Future requests to the front-end server for that same file are then served from the file that is stored in the BLOB cache, instead of being served from the database. This reduces the network traffic and the load on the database server. 
  
For more information about BLOB caches, see [Plan for caching and performance in SharePoint Server](caching-and-performance-planning.md).
  
## Flush the BLOB cache
<a name="flush"> </a>

When you flush the BLOB cache, you clear the contents of the BLOB cache for a web application. This is useful if the BLOB cache becomes out of sync with the content. For example, after you restore a content database, the BLOB cache will be out of sync with the content. To correct that situation, you must flush the BLOB cache. The following procedure describes how to flush the BLOB cache for a web application.
  
> [!CAUTION]
> Flushing the BLOB cache for a web application affects all site collections in the web application. 
  
> [!NOTE]
> You cannot use the user interface to flush the BLOB cache. Instead, you use Microsoft PowerShell and the SharePoint object model to complete this task. 
  
 **To flush the BLOB cache**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running PowerShell cmdlets.
    
  - Add memberships that are required beyond the minimums above.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see Permissions and [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Copy the following code and paste it into a text editor, such as Notepad.
    
  ```
  $webApp = Get-SPWebApplication "<WebApplicationURL>"
  [Microsoft.SharePoint.Publishing.PublishingCache]::FlushBlobCache($webApp)
  Write-Host "Flushed the BLOB cache for:" $webApp
  ```

3. Replace  _\<WebApplicationURL\>_ with the URL of the web application whose BLOB cache you want to clear. 
    
4. Save the file, and name it FlushBLOBCache.ps1.
    
    > [!NOTE]
    > You can use a different file name, but you must save the file as an ANSI-encoded text file that has the file name extension .ps1. 
  
5. Open **SharePoint Management Shell**.
    
6. Change to the directory where you saved the file.
    
7. At the Microsoft PowerShell command prompt, type the following command.
    
  ```
  ./FlushBLOBCache.ps1
  ```

## See also
<a name="flush"> </a>

#### Other Resources

[Scripting with Windows PowerShell](https://go.microsoft.com/fwlink/p/?LinkId=193051)

