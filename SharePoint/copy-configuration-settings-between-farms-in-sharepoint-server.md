---
title: Copy configuration settings between farms in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: 8404adef-6bfb-4795-be16-15739e1212f5
---


# Copy configuration settings between farms in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Foundation 2013, SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-20* **Summary:** Learn how to copy configuration settings from one SharePoint Server 2016 or SharePoint Server 2013 farm to another.You can copy configuration settings between SharePoint Server farms by using Microsoft PowerShell. In this article:
-  [Before you begin](#begin)
    
  
-  [Backup and restore a farm without content databases to copy configuration settings in SharePoint](#proc1)
    
  -  [To back up and restore a farm without content databases by using Windows PowerShell](#PS)
    
  
-  [Back up and recover configuration settings only](#proc2)
    
  

## Before you begin
<a name="begin"> </a>

There are many ways in which you can copy configurations from one farm to another. Determine which method to use based on the configuration settings that you want to copy and how often you have to copy them.
- Back up and restore a farm without the content databases attached. This method gives you farm settings and Web application settings, in addition to the settings for any service applications that you select. 
    
  
- Back up and restore configurations only. This method provides you with the core SharePoint Foundation settings only.
    
    > [!NOTE:]
      
- Create a deployment script, based on your documented configuration. This method may be more work at first, but is easy to use to maintain standardization. 
    
  

## Backup and restore a farm without content databases to copy configuration settings in SharePoint Server
<a name="proc1"> </a>

To copy configuration settings by using a farm backup, we recommend that you first detach the content databases from the farm. This is not a step that we recommend that you take with a live production farm. 
> [!NOTE:]

  
    
    

 **To back up and restore a farm without content databases by using PowerShell**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.
    
    > [!NOTE:]
      
2. Start the SharePoint Management Shell.
    
  
3. At the PowerShell command prompt, type the following command to document the current Web application URLs and content database mappings.
    
  ```
  
Get-SPWebApplication | %{$_.Name;$_.Url;%{$_.ContentDatabases|%{$_.Name};Write-Host ""}}
  ```


    
    
  
4. Either unmount all content databases, as in the following example:
    
  ```
  Get-SPContentDatabase | Dismount-SPContentDatabase
  ```


    Or unmount a specific content database, as in the following example:
    


  ```
  Get-SPContentDatabase WSS_Content | Dismount-SPContentDatabase
  ```

5. Back up the farm.
    
  ```
  Backup-SPFarm -Directory \\\\servername\\share -BackupMethod Full

  ```


    > [!NOTE:]
      
6. After the backup is complete, re-mount the content databases.
    
  ```
  
Mount-SPContentDatabase -Name <WSS_Content>  -WebApplication <http://servername>
  ```


    Replace the placeholders with each of the mappings documented in step 1.
    
    Where:
    
  -  *<WSS_Content>*  is the <name and ID of the database>.
    
  
  -  *<http://servername>*  is <the URL of the Web Application>.
    
  
For more information, see **Get-SPAlternateURL**.
> [!NOTE:]

  
    
    


## Back up and recover configuration settings only
<a name="proc2"> </a>

As part of farm backup, you can choose to back up only configuration settings. A configuration-only backup extracts and backs up many, but not all, configuration settings from a configuration database. By using built-in tools, you can back up the configuration of any configuration database, whether it is currently attached to a farm or not. For detailed information about how to back up a configuration, see  [Back up farm configurations in SharePoint Server](html/back-up-farm-configurations-in-sharepoint-server.md).A configuration backup can be restored to the same — or any other — server farm. When a configuration is restored, it will overwrite any settings present in the farm that have values that are set within the configuration backup. If any settings present in the farm are not contained in the configuration backup, they will not be overwritten. For detailed information about how to restore a farm configuration, see  [Restore farm configurations in SharePoint Server](html/restore-farm-configurations-in-sharepoint-server.md).
# See also

#### 

 [Overview of backup and recovery in SharePoint Server](html/overview-of-backup-and-recovery-in-sharepoint-server.md)
  
    
    

  
    
    

