---
title: Configure backup and restore permissions in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: 3a25437a-e994-42c7-b4df-ac9fa29f38f5
---


# Configure backup and restore permissions in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-06-20* **Summary:** Learn how to configure permissions for backup and restore operations in SharePoint Server 2016 and SharePoint Server 2013.You can configure backup and restore permissions for SharePoint Server by using the SharePoint Central Administration website or PowerShell. The backup tool that you use depends on the kind of environment that you have deployed, your backup schedule requirements, and service level agreements that you have made with your organization.In this article:
-  [Before you begin](#begin)
    
  
-  [Permissions for the SPTimerV4 timer service and SQL Server account in SharePoint Server](#proc1)
    
  
-  [Group memberships required to run backup and restore operations in Central Acministration](#proc2)
    
  
-  [Setting permissions to run SharePoint backup and restore operations by using Windows PowerShell](#proc3)
    
  

## Before you begin
<a name="begin"> </a>

Before you back up or restore SharePoint Server, you must make sure that the timer service account, SQL Server service account, and users who run the backup or restore operations have the correct permissions or are members of the correct Windows security groups or SharePoint groups. You must configure these permissions and group memberships when you first deploy SharePoint Server. You have to update permissions and group memberships when you add new farm components to the environment and if you want to add users who will perform backup and restore operations.
## Permissions for the SharePoint Timer service and SQL Server account in SharePoint Server
<a name="proc1"> </a>

The SharePoint Timer Server and the SQL Server service account in SharePoint Server perform backup and restore operations on behalf of users. These service accounts require Full Control permissions on any backup folders.
## Group memberships required to run backup and restore operations in Central Administration
<a name="proc2"> </a>

You must make sure all user accounts that use Central Administration to back up or restore your farm and farm components have the group memberships that are described in the following table.
### 

Farm component Member of Administrators group on the local computer Member of Farm Administrators SharePoint group Farm  <br/> Yes  <br/> No  <br/> Service Application  <br/> Yes  <br/> No  <br/> Content Database  <br/> Yes  <br/> No  <br/> Site Collection  <br/> No  <br/> Yes  <br/> Site, list, document library  <br/> No  <br/> Yes  <br/> 
## Setting permissions to run SharePoint backup and restore operations by using PowerShell
<a name="proc3"> </a>

You must make sure that all user accounts that use PowerShell to back up or restore your farm and farm components are added to the **SharePoint_Shell_Access** role for a specified database and have the permissions described in the table later in this section.You can run the **Add-SPShellAdmin** cmdlet to add a user account to this role. You must run the command for each user account. Moreover, you must run the command for all databases to which you want to grant access.
> [!NOTE:]

  
    
    


> [!IMPORTANT:]

  
    
    

 **To add a user to or remove a user from the SharePoint_Shell_Access role by using PowerShell**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.
    
    > [!NOTE:]
      
2. Start the SharePoint 2016 Management Shell or the SharePoint 2013 Management Shell.
    
  
3. At the PowerShell command prompt, type the following command:
    
  ```
  
Add-SPShellAdmin -Username <User account> -Database <Database ID>
  ```


    
    
    Where:
    
  -  *<Database ID>*  is the GUID assigned to the database.
    
  

    To add a user account to all the databases in the farm, type the following command:
    


  ```
  ForEach ($db in Get-SPDatabase) {Add-SPShellAdmin -Username <User account> -Database $db}
  ```


    
    
    Where:
    
  -  *<User account>*  is the user whose account you want to add.
    
  

    To remove a user account from all the databases in the farm, type the following command:
    


  ```
  ForEach ($db in Get-SPDatabase) {Remove-SPShellAdmin -Username <User account> -Database $db}
  ```


    
    
    Where:
    
  -  *<User account>*  is the user whose account you want to remove.
    
  

    To view the user accounts currently added to the databases in the farm, type the following command:
    


  ```
  ForEach ($db in Get-SPDatabase) {Get-SPShellAdmin -Database $db}
  ```


    
    
  
For more information, see **Add-SPShellAdmin**.
> [!NOTE:]

  
    
    

You might also have to grant additional permissions to the users who run the backup or restore operation by using PowerShell. The following table shows the permissions that are required.
### 

Farm component Member of Administrators group on the local computer Member of Farm Administrators SharePoint group Full control on backup folder Farm  <br/> Yes  <br/> No  <br/> Yes  <br/> Service Application  <br/> Yes  <br/> No  <br/> Yes  <br/> Content Database  <br/> Yes  <br/> No  <br/> Yes  <br/> Site Collection  <br/> No  <br/> Yes  <br/> Yes  <br/> Site, list, document library  <br/> Yes  <br/> No  <br/> Yes  <br/> 
# See also

#### 

 [Plan for backup and recovery in SharePoint Server](html/plan-for-backup-and-recovery-in-sharepoint-server.md)
  
    
    
 [Prepare to back up and restore farms in SharePoint Server](html/prepare-to-back-up-and-restore-farms-in-sharepoint-server.md)
  
    
    
 [Overview of backup and recovery in SharePoint Server](html/overview-of-backup-and-recovery-in-sharepoint-server.md)
  
    
    

  
    
    

