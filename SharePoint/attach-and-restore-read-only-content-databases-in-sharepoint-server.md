---
title: Attach and restore read-only content databases in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: 5417b04a-c7d9-4e9a-86fb-ee1d1c63508b
---


# Attach and restore read-only content databases in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Foundation 2013, SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-26* **Summary:** Learn how to attach and restore a read-only content database in SharePoint Server 2013 and SharePoint Server 2016.You can attach and restore a read-only content database in SharePoint Server by using PowerShell.In this article:
-  [Before you begin](#begin)
    
  
-  [Using Windows PowerShell to attach and restore a read-only content database](#proc1)
    
  -  [To attach and restore a read-only content database by using Windows PowerShell](#PS)
    
  

## Before you begin
<a name="begin"> </a>

A SharePoint Server farm in which content databases are set to be read-only can be part of a failure recovery environment that runs against mirrored or log-shipped content databases or part of a highly available maintenance or patching environment that provides user access when another version of the farm is being updated.Before you begin this operation, review the following information about prerequisites:
- When you re-attach the read-only databases, they become read-write.
    
  
- For more information about how to use read-only databases, see  [Run a farm that uses read-only databases in SharePoint Server](html/run-a-farm-that-uses-read-only-databases-in-sharepoint-server.md).
    
  

## Using PowerShell to attach and restore a read-only content database
<a name="proc1"> </a>

You can use only PowerShell to attach and restore a read-only content database. **To attach and restore a read-only content database by using PowerShell**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.
    
    > [!NOTE:]
      
2. Start the SharePoint Management Shell.
    
  
3. At the PowerShell command prompt, type the following command:
    
  ```
  
Mount-SPContentDatabase -Name <DatabaseName> -WebApplication <WebApplicationID> [-Verbose]
  ```


    
    
    Where:
    
  -  *<DatabaseName>*  is name of the read-only database.
    
  
  -  *<WebApplicationID>*  is ID assigned to the read-only database.
    
  

    > [!NOTE:]
      
For more information, see **Mount-SPContentDatabase**.
> [!NOTE:]

  
    
    


# See also

#### 

 [Overview of backup and recovery in SharePoint Server](html/overview-of-backup-and-recovery-in-sharepoint-server.md)
  
    
    

  
    
    

