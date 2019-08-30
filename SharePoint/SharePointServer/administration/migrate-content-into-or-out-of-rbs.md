---
title: "Migrate content into or out of RBS in SharePoint Server"
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
ms.assetid: 0317c126-78ed-47e0-9109-fe143ddb0259
description: "Learn how to migrate content into or out of Remote BLOB Storage (RBS), or to a different RBS provider for SharePoint Server."
---

# Migrate content into or out of RBS in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
After installing RBS and setting a content database to use RBS, all existing content in that database can be migrated into the database's active provider. You use the same Microsoft PowerShell command to migrate content into or out of RBS, or to another RBS provider. When RBS is implemented, SQL Server itself is regarded as an RBS provider. 
  
You can migrate content databases at any time. But we recommend that you perform migrations during low usage periods so that this activity does not cause decrease in performance for users. Migration moves all content from the specified content database into the storage mechanism of the newly named provider. 
  
## Migrate a content database
<a name="proc1"> </a>

This operation can be performed on any front-end or application server in the farm. You only have to perform the operation one time on one front-end or application server for each content database that you want to migrate.
  
 **To migrate a content database by using Microsoft PowerShell**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
2. Start the SharePoint Management Shell.
    
3. At the PowerShell command prompt, type the commands in the following steps.
    
4. To obtain the content database RBS settings object:
    
  ```
  $rbs=(Get-SPContentDatabase <ContentDbName>).RemoteBlobStorageSettings
  ```

    Where  _\<ContentDbName\>_ is the name of the content database. 
    
5. To view a list the RBS providers installed on the Web server:
    
  ```
  $rbs.GetProviderNames()
  ```

6. To set the active RBS provider:
    
  ```
  $rbs.SetActiveProviderName(<NewProvider>)
  ```

    Where  _\<NewProvider\>_ is the name of the provider that you want to make active for this content database. If you want to migrate the content database out of RBS completely and back into SQL Server inline storage, set this value to  `()`.
    
7. Migrate the data from RBS to the new provider or to SQL Server:
    
  ```
  $rbs.Migrate()
  ```

## See also
<a name="proc1"> </a>

#### Concepts

[Set a content database to use RBS with FILESTREAM in SharePoint Server](set-a-content-database-to-use-rbs.md)

