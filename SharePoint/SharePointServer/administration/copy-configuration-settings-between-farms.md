---
title: "Copy configuration settings between farms in SharePoint Server"
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
ms.assetid: 8404adef-6bfb-4795-be16-15739e1212f5
description: "Learn how to copy configuration settings from one SharePoint Server farm to another."
---

# Copy configuration settings between farms in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
You can copy configuration settings between SharePoint Server farms by using Microsoft PowerShell. 
  
    
## Before you begin
<a name="begin"> </a>

There are many ways in which you can copy configurations from one farm to another. Determine which method to use based on the configuration settings that you want to copy and how often you have to copy them.
  
- Back up and restore a farm without the content databases attached. This method gives you farm settings and Web application settings, in addition to the settings for any service applications that you select. 
    
- Back up and restore configurations only. This method provides you with the core SharePoint Foundation settings only.
    
    > [!NOTE]
    > This method does not include Web application or service application settings. If Web application settings are required in the restored farm, use one of the other methods. 
  
- Create a deployment script, based on your documented configuration. This method may be more work at first, but is easy to use to maintain standardization. 
    
## Backup and restore a farm without content databases to copy configuration settings in SharePoint Server
<a name="proc1"> </a>

To copy configuration settings by using a farm backup, we recommend that you first detach the content databases from the farm. This is not a step that we recommend that you take with a live production farm. 
  
> [!NOTE]
> Creating a farm backup without content databases does back up the service applications. 
  
 **To back up and restore a farm without content databases by using PowerShell**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint Management Shell.
    
3. At the PowerShell command prompt, type the following command to document the current Web application URLs and content database mappings.
    
   ```powershell
   Get-SPWebApplication | %{$_.Name;$_.Url;%{$_.ContentDatabases|%{$_.Name};Write-Host ""}}
   ```

4. Either unmount all content databases, as in the following example:
    
   ```powershell
   Get-SPContentDatabase | Dismount-SPContentDatabase
   ```

   Or unmount a specific content database, as in the following example:
    
   ```powershell
   Get-SPContentDatabase WSS_Content | Dismount-SPContentDatabase
   ```

5. Back up the farm.
    
   ```powershell
   Backup-SPFarm -Directory \\servername\share -BackupMethod Full
  
   ```

    > [!NOTE]
    > You can view the progress of the backup by looking at the  _\\servername\share\spbr####_\spbackup.log file. 
  
6. After the backup is complete, re-mount the content databases.
    
   ```powershell
   Mount-SPContentDatabase -Name <WSS_Content> -WebApplication <http://servername>
   ```

    Replace the placeholders with each of the mappings documented in step 1.
    
    Where:
    
    -  _\<WSS_Content\>_ is the \<name and ID of the database\>. 
    
    -  _\<http://servername\>_ is \<the URL of the Web Application\>. 
    
For more information, see [Mount-SPContentDatabase](/powershell/module/sharepoint-server/mount-spcontentdatabase?view=sharepoint-ps). 
  
> [!NOTE]
> We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions. 
  
## Back up and recover configuration settings only
<a name="proc2"> </a>

As part of farm backup, you can choose to back up only configuration settings. A configuration-only backup extracts and backs up many, but not all, configuration settings from a configuration database. By using built-in tools, you can back up the configuration of any configuration database, whether it is currently attached to a farm or not. For detailed information about how to back up a configuration, see [Back up farm configurations in SharePoint Server](back-up-a-farm-configuration.md).A configuration backup can be restored to the same — or any other — server farm. When a configuration is restored, it will overwrite any settings present in the farm that have values that are set within the configuration backup. If any settings present in the farm are not contained in the configuration backup, they will not be overwritten. For detailed information about how to restore a farm configuration, see [Restore farm configurations in SharePoint Server](restore-a-farm-configuration.md).
  
## See also
<a name="proc2"> </a>

#### Concepts

[Overview of backup and recovery in SharePoint Server](backup-and-recovery-overview.md)

