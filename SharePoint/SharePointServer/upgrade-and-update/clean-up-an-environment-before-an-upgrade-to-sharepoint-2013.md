---
title: "Clean up an environment before an upgrade to SharePoint 2013"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 9/27/2017
audience: ITPro
ms.topic: get-started-article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 67ca55e8-4d99-4346-b6ef-774e897ce992
description: "Make sure that your environment is in a healthy state, and delete unnecessary items before you upgrade to SharePoint."
---

# Clean up an environment before an upgrade to SharePoint 2013

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)]
  
Before you start to upgrade from SharePoint 2010 Products to SharePoint 2013, you should make sure that your environment is functioning in a healthy state and that you clean up any content that you do not have to upgrade. You can also take the time to remove or rearrange content so that you will have the structure that you want after you perform the upgrade.
  
## Items to clean up
<a name="Cleanup"> </a>

Many of these items can be removed or repaired by using Stsadm command-line tool or PowerShell cmdlets.
  
> [!IMPORTANT]
>  To use the Stsadm command-line tool, you must be a member of the Administrators group on the local computer. >  To use PowerShell cmdlets in the SharePoint Management Shell, you must have the following memberships: > **securityadmin** fixed server role on the SQL Server instance. > **db_owner** fixed database role on all databases that are to be updated. >  Administrators group on the server on which you are running the PowerShell cmdlets. 
  
### Delete unused or underused site collections and subwebs

You do not want to upgrade content that you do not have to keep. If it was unused for a long time and is not needed in the future, back it up, and then delete it to free storage and administrative resources, improve upgrade performance, and reduce upgrade risk. Be sure to communicate with site owners or organizational contacts regarding the site status — you want to make sure that the site is not needed before you delete it (for example, you do not want to delete sites that are required for compliance, such as emergency procedures, even though they may not be frequently updated).
  
For more information about how to delete site collections and subwebs, see the following articles:
  
- [Remove-SPSite](/powershell/module/sharepoint-server/Remove-SPSite?view=sharepoint-ps)
    
- [Remove-SPWeb](/powershell/module/sharepoint-server/Remove-SPWeb?view=sharepoint-ps)
    
### Check large lists (lists with lots of data)

By default, large list query throttling is turned on in SharePoint 2010 Products. This behavior has not changed in SharePoint 2013. If a list is very large, and users use a view or perform a query that exceeds the limit or throttling threshold, the view or query will not be permitted. If you are upgrading content from the server products in the Office 2007 release, check any large lists and have the site owner or list owner address the issue. For example, they can create indexed columns with filtered views, organize items into folders, set an item limit on the page for a large view, or use an external list. For more information about large list throttling and how to address issues with large lists, see [Manage lists and libraries with many items](https://go.microsoft.com/fwlink/p/?LinkId=251456). 
  
### Delete excess columns from wide lists (lists with too many columns) or remove wide lists

Wide lists are lists with more columns than fit in a single rowspan in the content database. During upgrade, the underlying storage in the database is changed to a sparse table structure, and a very wide list can cause upgrade to fail. Use the **Test-SPContentDatabase** command in PowerShell to look for wide lists in the content databases and then remove excess columns, or remove the wide list before you upgrade. 
  
For more information about maximum column sizes in a list, see [Column limits](../install/software-boundaries-and-limits-0.md#Column).
  
### Consider moving site collections into separate databases

If you have 5,000 or more site collections in a database, consider breaking them out into multiple databases. In SharePoint 2010 Products, there was a default warning at 9,000 site collections and a hard limit at 15,000 site collections. In SharePoint 2013, these values change to 2,000 site collections for the warning and 5,000 site collections for the limit. To avoid errors during upgrade or broken sites after upgrade, we recommend that you move some site collections into separate databases. If you have multiple content databases, you can also speed up an upgrade process by upgrading multiple databases in parallel. 
  
For more information about site collection limits, see [Content database limits](../install/software-boundaries-and-limits-0.md#ContentDB). For more information about how to move site collections to a new database, see [Move site collections between databases in SharePoint Server](../administration/move-site-collections-between-databases.md).
  
### Remove extraneous document versions

Large numbers of document versions can slow down an upgrade significantly. If you do not have to keep multiple versions, you can have users delete them manually or use the object model to find and remove them. For more information about how to programmatically remove extraneous versions, see [Versions Web Service](https://go.microsoft.com/fwlink/p/?LinkId=182330) on MSDN. 
  
### Remove unused templates, features, and Web Parts

First, verify that no sites are using the template, feature, or Web Part. You can use the **Stsadm -o EnumAllWebs** operation with the - **includefeatures** and - **includewebparts** parameters to identify these customizations in your environment. This operation identifies Web Parts, features, event handlers, and setup files that are being used in your environment. The **EnumAllWebs** command also specifies which files are used by which sites. Changes were made to the **EnumAllWebs** command in the February 2011 Cumulative update to make it return both site collection and web-level features. For more information, and to get the cumulative update, see [Description of the SharePoint Foundation 2010 cumulative update package (SharePoint Foundation server-package): March 3, 2011](https://go.microsoft.com/fwlink/p/?LinkId=254687).
  
You can remove a feature during site collection upgrade. Simple features can also be removed by deprecating them in the template. You can use feature upgrade to remove more complex features. For more information, see [Upgrading Features](https://go.microsoft.com/fwlink/p/?LinkId=254688) and [Feature Upgrade Overview](https://go.microsoft.com/fwlink/p/?LinkId=254690) on MSDN. 
  
For more information about how to identify customizations in your environment, see [Use a trial upgrade to SharePoint 2013 to find potential issues](/previous-versions/office/sharepoint-server-2010/cc262155(v=office.14)). If customizations are not being used, delete them. For more information about how to manage these kinds of customizations, see [Features and Templates](https://go.microsoft.com/fwlink/p/?LinkId=182338) and [Solutions and Web Part Packages](https://go.microsoft.com/fwlink/p/?LinkId=182332) on MSDN. 
  
### Remove PowerPoint Broadcast sites

These sites and site templates are not available in SharePoint 2013 because the Office Online Server are now installed separately from the SharePoint 2013 environment. Sites based on these templates will not work in SharePoint 2013. Remove these types of sites before you upgrade. 
  
You can use the **Get-SPSite** PowerShell command together with the following options to find these sites: 
  
```
Get-SPSite | Where-Object{$_.RootWeb.Template -eq "PowerPointBroadcast#0"}
```

This will return all sites that use that template.
  
You can also use the **Get-SPSite** and **Remove-SPSite** PowerShell commands together with the following options to remove these sites: 
  
```
Get-SPSite | Where-Object{$_.RootWeb.Template -eq "PowerPointBroadcast#0"} | Remove-SPSite
```

Be sure to back up these sites before you remove them. For more information, see [Get-SPSite](/powershell/module/sharepoint-server/Get-SPSite?view=sharepoint-ps) and [Remove-SPSite](/powershell/module/sharepoint-server/Remove-SPSite?view=sharepoint-ps).
  
### Remove FAST Search Center sites

You cannot upgrade FAST Search Center sites to the 2013 experience. Existing FAST Search Center sites can continue to work in 2010 mode after upgrade. If you want the new functionality, you must create new Enterprise Search Center sites in 2013 mode.
  
### Finish Visual Upgrades in SharePoint 2010 Products

During an upgrade from the server products in the Office 2007 release to SharePoint 2010 Products, you could allow site owners to use Visual Upgrade to keep sites in the old experience on the upgraded environment. When you upgrade to SharePoint 2013, all sites that are still in the old experience in SharePoint 2010 Products are automatically upgraded to the 2010 experience. If you want the opportunity to address any issues and review the sites before they are switched to the new experience, upgrade them to the new experience in your SharePoint 2010 Products environment and review them before you upgrade them to SharePoint 2013. We recommend that you finish visual upgrades before you upgrade to SharePoint 2013. Finishing visual upgrades before you upgrade provides the following benefits:
  
- You can address issues while you still have the server products in the Office 2007 release components available.
    
- You can have users be involved in reviewing and fixing issues in their sites.
    
- You can roll back to the old experience temporarily if it is necessary. You cannot roll back when you are in the SharePoint 2013 experience.
    
- You avoid adding potential errors to the upgrade process. The fewer operations occurring during upgrade, the better. Trying to troubleshoot errors is more difficult when you have more processes involved. And users might think that upgrade has caused an issue when it's really the experience changing to the new version. If you have an issue with how the site interface is displaying, how will you know whether it is an old issue from the site that was forced through visual upgrade, a problem with the 2010 mode in SharePoint 2013, or a problem with a new CSS file?
    
To check for sites in the old experience, on the SharePoint 2010 Products environment, you can use the **Get-SPSite** PowerShell command. 
  
 **To check for and upgrade sites still in the old experience in the SharePoint 2010 Products environment by using PowerShell**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint 2013 cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. On the **Start** menu, click **All Programs**.
    
3. Click **Microsoft SharePoint 2010 Products**.
    
4. Click **SharePoint 2010 Management Shell**.
    
5. At the PowerShell command prompt, type the following command to return all site collections that are in or have subwebs in the old experience:
    
  ```
  Get-SPSite | ForEach-Object{$_.GetVisualReport()}
  ```

6. At the PowerShell command prompt, type the following command to upgrade those sites to the new experience:
    
  ```
  Get-SPSite | ForEach-Object{$_.VisualUpgradeWebs()}
  ```

For more information, see [Get-SPSite](/powershell/module/sharepoint-server/Get-SPSite?view=sharepoint-ps) and [Manage visual upgrade (SharePoint Server 2010)](https://go.microsoft.com/fwlink/?LinkId=403882).
  
### Repair data issues

Make sure that you repair all issues in your databases or site content before you upgrade. In particular, check the following items:
  
- **Check databases for corrupted data**
    
    Clean up your databases to remove any orphaned sites or other corrupted data, such as a corrupted list. Consider defragmenting if you have removed sites or subsites from the database. For more information, see:
    
  - [Databaserepair: Stsadm operation](/previous-versions/office/sharepoint-2007-products-and-technologies/cc263282(v=office.12))
    
  - [Forcedeletelist: Stsadm operation](/previous-versions/office/sharepoint-2007-products-and-technologies/cc262609(v=office.12))
    
- **Check databases for duplicate or orphaned site collections**
    
    Make sure that site collections exist in only one content database. Occasionally, site collections can leave behind duplicate or orphaned references in old content databases if they are moved to new databases, or if a copy of a database was attached to the farm, or if there was an error when a site collection was provisioned. If a site collection is referenced in more than one content database or there is more than one instance of the site collection in a content database, it can cause issues when you upgrade by using the database attach upgrade method. If you upgrade a duplicate version of the site collection first, the site map in your configuration database might end up pointing to that version of the site instead of the current version. 
    
    Before you upgrade, use the **Enumallwebs** operation in stsadm command-line tool to discover which sites are in which content databases and compare the results. Also, examine each site collection in the results and check whether it is listed as missing in the site map. Being listed as missing indicates that it is an orphaned site. For more information, see [Enumallwebs: Stsadm operation](https://go.microsoft.com/fwlink/?LinkId=403887). If you find duplicate or orphaned sites, you can use the **Remove-SPSite** cmdlet in PowerShell to remove the duplicate or orphaned sites from the database. 
    
    For more information, see [Remove-SPSite](/powershell/module/sharepoint-server/Remove-SPSite?view=sharepoint-ps).
    
- **Check variations**
    
    In publishing environments, check for any variations that must be fixed. For more information, see [Variationsfixuptool: Stsadm operation](/previous-versions/office/sharepoint-2007-products-and-technologies/dd789658(v=office.12)).
    
## How to make structural changes
<a name="Structure"> </a>

To make structural changes to your environment, such as moving site collections or changing how your databases are allocated, you can use the following methods:
  
- **Move-SPSite** Use this to move site collections between databases. If a database is very large or contains lots of site collections, you can move sites to address this to make upgrade more efficient. Also, you can move all collaboration sites into one database and all My Sites into another to make the upgrade administration easier for those different sets of sites. You can also use this operation to divide large databases if they contain multiple site collections. This can also help increase upgrade efficiency. 
    
    For more information, see [Move-SPSite](/powershell/module/sharepoint-server/Move-SPSite?view=sharepoint-ps).
    
- **Export-SPWeb and Import-SPWeb** Use this method to move subwebs or site collections inside a farm or between farms. For more information, see [Export-SPWeb](/powershell/module/sharepoint-server/Export-SPWeb?view=sharepoint-ps) and [Import-SPWeb](/powershell/module/sharepoint-server/Import-SPWeb?view=sharepoint-ps).
    
## See also
<a name="Structure"> </a>

#### Other Resources

[Use a trial upgrade to SharePoint 2013 to find potential issues](/previous-versions/office/sharepoint-server-2010/cc262155(v=office.14))
  
[Best practices for upgrading from SharePoint 2010 to SharePoint 2013](best-practices-for-upgrading-from-sharepoint-2010-to-sharepoint-2013.md)

