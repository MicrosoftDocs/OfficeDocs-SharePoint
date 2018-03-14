---
title: "Move site collections between databases in SharePoint Server"
ms.author: stevhord
author: bentoncity
manager: pamgreen
ms.date: 2/28/2018
ms.audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 86bb109d-865f-4f86-bb3d-87ecfc4e50ae
description: "Summary: Learn how to prepare and move site collections between databases in SharePoint Server 2016 and SharePoint 2013."
---

# Move site collections between databases in SharePoint Server

 **Summary:** Learn how to prepare and move site collections between databases in SharePoint Server 2016 and SharePoint 2013. 
  
Under some circumstances, you might want to move one or more site collections to a different content database. For example, a site collection can outgrow the content database on which it resides, and you would have to move the site collection to a larger content database. In SharePoint Server, you should view this procedure as moving the site collection to a larger database.
  
However, if site collections do not grow to their expected capacity, it might be convenient to combine several site collections onto one content database. In SharePoint Server, this process does not merge content databases, instead the site collections are moved to and joined on a new database.
  
You can move site collections between databases in a SharePoint Server farm by using Microsoft PowerShell. You can also move site collections by using Backup and Restore procedures. For information about how to do this, see [Back up site collections in SharePoint Server](back-up-site-collections.md) and [Restore site collections in SharePoint Server](restore-site-collections.md).
  
In this article:
  
- [Before you begin](#begin)
    
- [Determining the size of the source site collection](#Section2)
    
  - [To determine the size of the site collection by using Microsoft PowerShell](#proc1)
    
  - [To archive and trim audit data by using Microsoft PowerShell](#proc2)
    
- [Moving site collections between content databases](#Section3)
    
- [To move a single site collection by using Microsoft PowerShell](#proc3)
    
- [To move multiple site collections by using Microsoft PowerShell](#proc4)
    
## Before you begin
<a name="begin"> </a>

Before you begin this operation, the following conditions must be true:
  
- The destination content database must already exist.
    
- The source content database and destination content database must be located on the same instance of SQL Server.
    
- The source content database and destination content database must be attached to the same web application. For more information about how to add a content database to a web application, see [Add content databases in SharePoint Server](add-a-content-database.md).
    
## Determining the size of the source site collection
<a name="Section2"> </a>

When you move site collections to another content database the auditing data is copied. The size of the auditing data varies depending on the event collection settings for the site collection. If the auditing data is large, you can move the data to another database before you move the site collection. To do this, use the [To archive and trim audit data by using Microsoft PowerShell](#proc2) procedure. 
  
Regardless of the reason for moving a site collection, you should always begin the task by determining the size of the site collection that is to be moved. You can then be sure that the destination hard disk can sufficiently contain the site collection contents. Verify that the destination hard disk has at least three times the free space that is required for the site collection.
  
> [!TIP]
> You can stay current about the space that site collections are using by creating site quotas and e-mail alerts.. 
  
 **To determine the size of the site collection by using PowerShell**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](http://technet.microsoft.com/library/2ddfad84-7ca8-409e-878b-d09cb35ed4aa.aspx). 
  
2. Start the SharePoint Management Shell.
    
3. At the PowerShell command prompt, type the following commands:
    
  ```
  $used = (Get-SPSiteAdministration -Identity <http://ServerName/Sites/SiteName>).DiskUsed
  ```

  ```
  $used
  ```

    Where:
    
  -  _\<http://ServerName/Sites/SiteName\>_ is the name of the site collection. 
    
    The amount of disk space that is being used by the specified site collection is stored in the  _$used_ variable, and is displayed at the command prompt when the second command is run. 
    
    > [!NOTE]
    > The amount of disk space that is displayed does not include the disk space that is used by the auditing data that will be moved with the site collection. 
  
For more information, see [Get-SPSiteAdministration](http://technet.microsoft.com/library/a05769b1-7559-4af4-8524-5cbcc1bd4f25.aspx).
  
 **To archive and trim audit data by using PowerShell**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](http://technet.microsoft.com/library/2ddfad84-7ca8-409e-878b-d09cb35ed4aa.aspx). 
  
2. Start the SharePoint Management Shell.
    
3. At the PowerShell command prompt, type the following command:
    
  ```
  (Get-SPSite -Identity <http://ServerName/Sites/SiteName>).Audit.TrimAuditLog(deleteEndDate)
  ```

    Where:
    
  -  _\<http://ServerName/Sites/SiteName\>_ is the name of the site collection. 
    
    To delete the audit data without archiving it first, type the following command:
    
  ```
  (Get-SPSite -Identity <http://ServerName/Sites/SiteName>).Audit.DeleteEntries(deleteEndDate)
  ```

For more information, see [Get-SPSite](http://technet.microsoft.com/library/f3422bf4-0f9b-4f22-94c8-2a0606a31b16.aspx).
  
> [!NOTE]
> We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions. 
  
## Moving site collections between content databases
<a name="Section3"> </a>

You can use the PowerShell command **Move-SPSite** to move site collections between content databases. Two procedures are provided here. The first procedure moves a single site collection to a new content database, and the second procedure moves multiple site collections to a new content database. 
  
 **To move a single site collection**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](http://technet.microsoft.com/library/2ddfad84-7ca8-409e-878b-d09cb35ed4aa.aspx). 
  
2. Start the SharePoint Management Shell.
    
3. At the PowerShell command prompt, type the following command:
    
  ```
  Move-SPSite <http://ServerName/Sites/SiteName> -DestinationDatabase <DestinationContentDb>
  ```

    Where:
    
  -  _\<http://ServerName/Sites/SiteName\>_ is the name of the site collection. 
    
  -  _\<DestinationContentDb\>_ is the name of the destination content database. 
    
### To move multiple site collections

1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](http://technet.microsoft.com/library/2ddfad84-7ca8-409e-878b-d09cb35ed4aa.aspx). 
  
2. Start the SharePoint Management Shell.
    
3. At the PowerShell command prompt, type the following command:
    
  ```
  Get-SPSite -ContentDatabase <SourceContentDb> | Move-SPSite -DestinationDatabase <DestinationContentDb>
  ```

    Where:
    
  -  _\<SourceContentDb\>_ is the name of the original content database. 
    
  -  _\<DestinationContentDb\>_ is the name of the destination content database. 
    
    This command moves all site collections from the source content database to the destination content database.
    
For more information, see [Move-SPSite](http://technet.microsoft.com/library/e3bf1b34-78b9-4643-b0dd-24444e3cffc5.aspx).
  
> [!NOTE]
> We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions. 
  
## See also
<a name="Section3"> </a>

#### Concepts

[Add content databases in SharePoint Server](add-a-content-database.md)

