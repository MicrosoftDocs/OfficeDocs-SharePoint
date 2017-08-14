---
title: Move site collections between databases in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: 86bb109d-865f-4f86-bb3d-87ecfc4e50ae
---


# Move site collections between databases in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Foundation 2013, SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-24* **Summary:** Learn how to prepare and move site collections between databases in SharePoint Server 2016 and SharePoint Server 2013.Under some circumstances, you might want to move one or more site collections to a different content database. For example, a site collection can outgrow the content database on which it resides, and you would have to move the site collection to a larger content database. In SharePoint Server, you should view this procedure as moving the site collection to a larger database.However, if site collections do not grow to their expected capacity, it might be convenient to combine several site collections onto one content database. In SharePoint Server, this process does not merge content databases, instead the site collections are moved to and joined on a new database.You can move site collections between databases in a SharePoint Server farm by using Microsoft PowerShell. You can also move site collections by using Backup and Restore procedures. For information about how to do this, see  [Back up site collections in SharePoint Server](html/back-up-site-collections-in-sharepoint-server.md) and [Restore site collections in SharePoint Server](html/restore-site-collections-in-sharepoint-server.md).In this article:
-  [Before you begin](#begin)
    
  
-  [Determining the size of the source site collection](#Section2)
    
  -  [To determine the size of the site collection by using Windows PowerShell](#proc1)
    
  
  -  [To archive and trim audit data by using Windows PowerShell](#proc2)
    
  
-  [Moving site collections between content databases](#Section3)
    
  
-  [To move a single site collection by using Windows PowerShell](#proc3)
    
  
-  [To move multiple site collections by using Windows PowerShell](#proc4)
    
  

## Before you begin
<a name="begin"> </a>

Before you begin this operation, the following conditions must be true:
- The destination content database must already exist.
    
  
- The source content database and destination content database must be located on the same instance of SQL Server.
    
  
- The source content database and destination content database must be attached to the same web application. For more information about how to add a content database to a web application, see  [Add content databases in SharePoint Server](html/add-content-databases-in-sharepoint-server.md).
    
  

## Determining the size of the source site collection
<a name="Section2"> </a>

When you move site collections to another content database the auditing data is copied. The size of the auditing data varies depending on the event collection settings for the site collection. If the auditing data is large, you can move the data to another database before you move the site collection. To do this, use the  [To archive and trim audit data by using Windows PowerShell](#proc2) procedure.Regardless of the reason for moving a site collection, you should always begin the task by determining the size of the site collection that is to be moved. You can then be sure that the destination hard disk can sufficiently contain the site collection contents. Verify that the destination hard disk has at least three times the free space that is required for the site collection.
> [!TIP:]

  
    
    

 **To determine the size of the site collection by using PowerShell**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.
    
    > [!NOTE:]
      
2. Start the SharePoint Management Shell.
    
  
3. At the PowerShell command prompt, type the following commands:
    
  ```
  
$used = (Get-SPSiteAdministration -Identity <http://ServerName/Sites/SiteName> ).DiskUsed
  ```


  ```
  $used
  ```


    
    
    Where:
    
  -  *<http://ServerName/Sites/SiteName>*  is the name of the site collection.
    
  

    The amount of disk space that is being used by the specified site collection is stored in the  *$used*  variable, and is displayed at the command prompt when the second command is run.
    
    > [!NOTE:]
      
For more information, see **Get-SPSiteAdministration**. **To archive and trim audit data by using PowerShell**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.
    
    > [!NOTE:]
      
2. Start the SharePoint Management Shell.
    
  
3. At the PowerShell command prompt, type the following command:
    
  ```
  
(Get-SPSite -Identity <http://ServerName/Sites/SiteName> ).Audit.TrimAuditLog(deleteEndDate)
  ```


    
    
    Where:
    
  -  *<http://ServerName/Sites/SiteName>*  is the name of the site collection.
    
  

    
    
    To delete the audit data without archiving it first, type the following command:
    


  ```
  (Get-SPSite -Identity <http://ServerName/Sites/SiteName> ).Audit.DeleteEntries(deleteEndDate)
  ```

For more information, see **Get-SPSite**.
> [!NOTE:]

  
    
    


## Moving site collections between content databases
<a name="Section3"> </a>

You can use the PowerShell command **Move-SPSite** to move site collections between content databases. Two procedures are provided here. The first procedure moves a single site collection to a new content database, and the second procedure moves multiple site collections to a new content database. **To move a single site collection**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.
    
    > [!NOTE:]
      
2. Start the SharePoint Management Shell.
    
  
3. At the PowerShell command prompt, type the following command:
    
  ```
  
Move-SPSite <http://ServerName/Sites/SiteName>  -DestinationDatabase <DestinationContentDb>
  ```


    
    
    Where:
    
  -  *<http://ServerName/Sites/SiteName>*  is the name of the site collection.
    
  
  -  *<DestinationContentDb>*  is the name of the destination content database.
    
  
 **To move multiple site collections**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.
    
    > [!NOTE:]
      
2. Start the SharePoint Management Shell.
    
  
3. At the PowerShell command prompt, type the following command:
    
  ```
  
Get-SPSite -ContentDatabase <SourceContentDb>  | Move-SPSite -DestinationDatabase <DestinationContentDb>
  ```


    
    
    Where:
    
  -  *<SourceContentDb>*  is the name of the original content database.
    
  
  -  *<DestinationContentDb>*  is the name of the destination content database.
    
  

    This command moves all site collections from the source content database to the destination content database.
    
  
For more information, see **Move-SPSite**.
> [!NOTE:]

  
    
    


# See also

#### 

 [Add content databases in SharePoint Server](html/add-content-databases-in-sharepoint-server.md)
  
    
    

  
    
    

