---
title: "Delete and restore site collections in SharePoint Server"
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
ms.assetid: 44c05570-37c1-49dd-8015-015f8908199c
description: "How to delete and restore SharePoint Server site collection content, user information, and the site hierarchy."
---

# Delete and restore site collections in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
If you've created a team site to track progress on a specific project, and the project has ended, you might decide to delete the site collection after a certain amount of time has passed. 
  
When you delete a site collection, you are deleting the hierarchy of sites that comprise the collection. Deleting a site collection, also permanently destroys all content and user information, such as the following:
  
- Documents and document libraries.
    
- Lists and list data, including surveys, discussions, announcements, and events.
    
- Site configuration settings.
    
- Role and security information that is related to the website.
    
- Subsites of the top-level website, their contents, and user information.
    
> [!NOTE]
> You should back up a site collection before you delete it. For more information, see [Plan for backup and recovery in SharePoint Server](../administration/backup-and-recovery-planning.md). 
  
If the site collection is associated with a Project Server service application, you must remove the association and delete the Project Web App before you delete the site collection. You can remove the site collection association with the Project Server service application from service application settings page in the SharePoint Central Administration website.
  
    
## Before you begin
<a name="begin"> </a>

Before you delete a site collection, ensure that a backup copy of the site collection and all of its contents exists.
  
There are two recycle bins in SharePoint and the retention time for each is as follows:
  
- Site Recycle Bin (First-Stage) = 30 days
    
- Site Collection (Second Stage) = 50% of the site quota
    
The maximum possible retention time for an item is 30 days. If you don't reach the second stage quota limit, the deleted item stays in one of the recycle bins for 30 days. If an item is deleted and resides in the first stage recycle bin, it is retained for the entire 30 days since it will still count against your quota. If an item is deleted and resides in or is moved to the second stage recycle bin, it does not count against your quota unless it's a deleted SharePoint web application, but the retention time for this item could be less than the 30 days if the total amount of content in the second stage bin exceeds the 50% of the site quota.
  
## Delete a site collection by using Central Administration
<a name="section1"> </a>

After you perform this procedure, the site collection and all of its content and user information will be permanently destroyed.
  
 **To delete a site collection by using Central Administration**
  
1. Verify that you have the following administrative credentials:
    
   - To delete a site collection, the user account that is performing this procedure must be a member of the Farm Administrators SharePoint group.
    
2. Open Central Administration.
    
3. On the Central Administration website, click **Application Management**.
    
4. On the **Application Management** page, in the **Site Collections** section, click **Delete a site collection**.
    
5. On the **Delete Site Collection** page, in the **Site Collection** list, click **Change Site Collection**.
    
    The **Select Site Collection** webpage dialog box appears. 
    
6. In the **Web Application** list, click **Change Web Application**.
    
    The **Select Web Application** webpage dialog box appears. 
    
7. Click the name of the web application that contains the site collection that you want to delete. Relative URLs of sites in the site collections of the web application that you have selected appear on the **Select Site Collection** dialog box. 
    
8. Click the relative URL of the site collection that you want to delete, and then click **OK**.
    
9. Read the Warning section and verify that the site collection information is correct.
    
10. On the **Delete Site Collection** page, click **Delete**.
    
## Delete a site collection by using Microsoft PowerShell
<a name="section2"> </a>

After you perform this procedure, the site collection and all of its content and user information will be permanently destroyed.
  
 **To delete a site collection by using PowerShell**
  
1. Verify that you meet the following minimum requirements: 
    
   - **securityadmin** fixed server role on the SQL Server instance. 
    
   - **db_owner** fixed database role on all databases that are to be updated. 
    
   - Local Administrators group on the server on which you are running the Microsoft PowerShell cmdlets.
    
2. Open the SharePoint Management Shell.
    
3. At the PowerShell command prompt, type the following command, and then press ENTER:
    
   ```powershell
   Remove-SPSite -Identity "<URL>" -GradualDelete
   ```

   Where:  _\<URL\>_ is the unique address of the site collection you want to delete. 
    
This command removes the specified site collection and all subsites. Gradual deletion reduces the load on the system during the deletion process.
    
The previous procedure illustrates a common way to use the **Remove-SPSite** cmdlet to delete a site collection. You can specify different parameters to configure this command differently. For more information, see [Remove-SPSite](/powershell/module/sharepoint-server/Remove-SPSite?view=sharepoint-ps).
    
> [!NOTE]
> We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions. 
  
## Restore a site collection by using Microsoft PowerShell
<a name="section3"> </a>

If you've accidentally deleted a site collection, you can restore it using PowerShell.
  
When a site collection (that is, a **SPSite** object) is accidentally deleted in SharePoint Server, the deleted site collection is stored in the **SPDeletedSite** object, not the **SPSite** object. To restore a deleted site collection, you must use the [Restore-SPDeletedSite](/powershell/module/sharepoint-server/restore-spdeletedsite?view=sharepoint-ps) cmdlet or programmatically access the object model.

SharePoint Server 2019 users can restore items that they've deleted themselves, and also items that other users in the site have deleted. Users need edit permission on the deleted items so they're visible in their SharePoint recycle bin. 
  
## See also
<a name="section3"> </a>

#### Concepts

[Create a site collection in SharePoint Server](create-a-site-collection.md)
  
[Overview of sites and site collections in SharePoint Server](sites-and-site-collections-overview.md)

