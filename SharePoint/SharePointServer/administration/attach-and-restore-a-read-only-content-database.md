---
title: "Attach and restore read-only content databases in SharePoint Server"
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
ms.assetid: 5417b04a-c7d9-4e9a-86fb-ee1d1c63508b
description: "Learn how to attach and restore a read-only content database in SharePoint Server."
---

# Attach and restore read-only content databases in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
You can attach and restore a read-only content database in SharePoint Server by using PowerShell.
  
    
## Before you begin
<a name="begin"> </a>

A SharePoint Server farm in which content databases are set to be read-only can be part of a failure recovery environment that runs against mirrored or log-shipped content databases or part of a highly available maintenance or patching environment that provides user access when another version of the farm is being updated.
  
Before you begin this operation, review the following information about prerequisites:
  
- When you re-attach the read-only databases, they become read-write.
    
- For more information about how to use read-only databases, see [Run a farm that uses read-only databases in SharePoint Server](run-a-farm-that-uses-read-only-databases.md).
    
## Using PowerShell to attach and restore a read-only content database
<a name="proc1"> </a>

You can use only PowerShell to attach and restore a read-only content database.
  
 **To attach and restore a read-only content database by using PowerShell**
  
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
   Mount-SPContentDatabase -Name <DatabaseName> -WebApplication <WebApplicationID> [-Verbose]
   ```

    Where:
    
   -  _\<DatabaseName\>_ is name of the read-only database. 
    
   -  _\<WebApplicationID\>_ is ID assigned to the read-only database. 
    
    > [!NOTE]
    > Attaching a content database by using the  `Mount-SPContentDatabase` cmdlet differs from attaching a database in SQL Server by using SQL Server tools.  `Mount-SPContentDatabase` associates the content database with a Web application so that the contents can be read. 
  
For more information, see [Mount-SPContentDatabase](/powershell/module/sharepoint-server/Mount-SPContentDatabase?view=sharepoint-ps).
  
> [!NOTE]
> We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions. 
  
## See also
<a name="proc1"> </a>

#### Concepts

[Overview of backup and recovery in SharePoint Server](backup-and-recovery-overview.md)

