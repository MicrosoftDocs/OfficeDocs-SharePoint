---
title: "Disable RBS on content databases in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 2/27/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 75096f60-b94e-44c2-bc84-8aa3e2c4fff3
description: "Learn how to disable Remote BLOB Storage (RBS) on any SharePoint Server content database."
---

# Disable RBS on content databases in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
You can disable Remote BLOB Storage (RBS) on any content database. After you disable RBS on a content database, binary large objects (BLOBs) are stored inline in SQL Server for all subsequent writes to the content database. This article describes how to disable RBS on a content database.
  
You can disable RBS on a content database by setting the active provider name to the empty string in Microsoft PowerShell. Each content database has a **RemoteBlobStorageSettings** property that can be used to invoke the **SetActiveProviderName** method. 
  
This action does not change the storage location of any BLOBs that have previously been stored in RBS or inline storage. Disabling RBS does not uninstall RBS. We do not recommend that you uninstall RBS.
  
Before you begin this operation, review the following information about prerequisites:
  
## Disable RBS for a content database
<a name="proc1"> </a>

This operation can be performed on any Web server in the farm. You only have to perform the operation one time on one Web server for each content database for which you want to disable RBS.
  
> [!CAUTION]
> Do not use the **Disable()** method on the **RemoteBlobStorageSettings** object. This method is used only to uninstall RBS, and we do not recommend that you just disable the writing of new BLOBs into RBS. To completely remove RBS, perform the below task and then use [Move-SPSite](/powershell/module/sharepoint-server/move-spsite?view=sharepoint-ps) to move all sites into a non-RBS enabled database. This will allow you to delete the content database that previously had RBS enabled.
  
You must use Microsoft PowerShell cmdlets to disable RBS. There is no user interface option for this task.
  
 **To disable RBS by using PowerShell**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
2. Start the SharePoint Management Shell.
    
3. At the PowerShell command prompt, type the following commands:
    
  ```
  $site=Get-SPSite "<http://yourSiteURL>"
  $rbss=$site.ContentDatabase.RemoteBlobStorageSettings
  $rbss.SetActiveProviderName("")
  ```

Where  http://yourSiteURL is the Web application that is attached to the content database that is being disabled for RBS. 
    
For more information, see [Get-SPSite](/powershell/module/sharepoint-server/Get-SPSite?view=sharepoint-ps).
    
## See also
<a name="proc1"> </a>

#### Concepts

[Set a content database to use RBS with FILESTREAM in SharePoint Server](set-a-content-database-to-use-rbs.md)

