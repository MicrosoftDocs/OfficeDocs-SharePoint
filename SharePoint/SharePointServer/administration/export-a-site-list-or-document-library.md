---
title: "Export sites, lists, or document libraries in SharePoint Server"
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
ms.assetid: 1e637e17-2634-4601-a574-299a7c27bb24
description: "Learn how to export a site, list, or document library in SharePoint Server."
---

# Export sites, lists, or document libraries in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
You can export a site, list, or document library in SharePoint Server by using the SharePoint Central Administration website or Microsoft PowerShell. The backup tool that you use depends on the kind of environment that you have deployed, your backup schedule requirements, and service level agreements that you have made with your organization. 
  
    
## Before you begin
<a name="begin"> </a>

We recommend that you regularly back up the complete farm. However, business or IT requirements might require you to export a site, list, or document library. Regularly exporting sites, lists, and document libraries reduces data losses that might occur from hardware failures, power outages, or other problems. It is a simple process and helps make sure that data is available for recovery, if that is required. You can only export one site, list, or document library at a time.
  
For information about what to back up and which tools to use, see [Plan for backup and recovery in SharePoint Server](backup-and-recovery-planning.md).
  
Before you begin this operation, review the following information about prerequisites:
  
- Before you begin, you must create a folder on the local computer or the network in which to store the export file. For better performance, we recommend that you export to the local computer and then move the export file to a network folder.
    
- You cannot use SQL Server tools or Data Protection Manager to export a site, list or document library.
    
## Use PowerShell to export a site, list, or document library in SharePoint Server
<a name="proc1"> </a>

You can use PowerShell to export a site, list, or document library manually or as part of a script that can be run at scheduled intervals.
  
 **To export a site, list or document library by using PowerShell**
  
1. Verify that you have the following memberships:
    
   - **securityadmin** fixed server role on the SQL Server instance. 
    
   - **db_owner** fixed database role on all databases that are to be updated. 
    
   - Administrators group on the server on which you are running the PowerShell cmdlets.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint Management Shell.
    
3. At the PowerShell command prompt, type the following command:
    
   ```powershell
   Export-SPWeb -Identity <SiteURL> -Path <Path and File Name> [-ItemUrl <URL of Site, List, or Library>] [-IncludeUserSecurity] [-IncludeVersions] [-NoFileCompression] [-GradualDelete] [-Verbose]
   ```

    Where:
    
   -  _\<SiteURL\>_ is URL for the site, list, or library that you are exporting. 
    
   -  _\<Path and FileName\>_ is path and name for the site, list, or library that you are exporting. 
    
   -  _\<URL of Site, List, or Library\>_ is the URL for the site, list, or library where you are exporting. 
    
    If you are exporting a large site, list, or document library, you can use the  `GradualDelete` parameter. When this parameter is used, the site collection is marked as deleted, which immediately prevents any further access to its content. The data in the deleted site collection is then deleted gradually over time by a timer job instead of at one time, which reduces its effect on the performance of farm servers and SQL Server. 
    
    To specify which version of the site, list, or document library to include, use the  `IncludeVersions` parameter and specify "LastMajor" (default), "CurrentVersion", "LastMajorandMinor", or "All". To include the user security settings with the list or document library, use the  `IncludeUserSecurity` parameter. If you want to overwrite the file that you specified, use the  `Force` parameter. To view the progress of the backup operation, use the  `Verbose` parameter. 
    
    The  `NoFileCompression` parameter lets you specify that no file compression is performed during the export process. Using this parameter can lower resource usage up to 30% during the export process. Using this parameter will result in a backup folder being created instead of a compressed file. If you use the  `NoFileCompression` parameter in the  `Export-SPWeb` command, you must also use it when you import the content by using the  `Import-SPWeb` command. 
    
For more information, see [Export-SPWeb](/powershell/module/sharepoint-server/Export-SPWeb?view=sharepoint-ps). 
  
> [!NOTE]
> We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions. 
  
## Use Central Administration to export a site, list, or document library in SharePoint Server
<a name="proc2"> </a>

You can use Central Administration to export a site, list, or document library. You can only export one site, list, or document library at a time.
  
 **To export a site, list, or document library by using Central Administration**
  
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
2. Start Central Administration.
    
3. In Central Administration, on the home page, click **Backup and Restore**.
    
4. On the **Backup and Restore** page, in the **Granular Backup** section, click **Export a site or list**.
    
5. On the **Site or List Export** page, in the **Site Collection** section, select the site collection from the **Site Collection** list, and then select the site from the **Site** list. 
    
6. If you are exporting a site, skip this step, Select the list or document library from the **List** list. 
    
7. In the **File Location** section, in the **Filename** box, type the UNC path of the shared folder and the file to which you want to export the list or document library. The file name must use the .cmp extension. 
    
8. If the file already exists and you want to use this file, select the **Overwrite existing files** check box. Otherwise, specify a different file name. 
    
9. If you want to export all the security and permissions settings with the list or library, in the **Export Full Security** section, select the **Export full security** check box. 
    
10. If you want to specify which version of the list or library to export, select one of the following versions from the **Export versions** list: 
    
    - All Versions
    
    - Last Major
    
    - Current Version
    
    - Last Major and Last Minor
    
11. When you have specified the settings that you want, click **Start Export**.
    
12. You can view the status of all backup jobs at the top of the **Granular Backup Job Status** page. You can view the status of the current backup job in the **Content Export** section of the page. The status page updates every 30 seconds automatically. You can manually update the status details by clicking **Refresh**. Backup and recovery are Timer service jobs. Therefore, it may take several seconds for the backup to start.
    
    If you receive any errors, you can review them in the **Failure Message** column of the Backup and Restore Job Status page. You can also find more details in the \<file name>\.export.log file at the UNC path that you specified in step 6. 
    
## See also
<a name="proc2"> </a>

#### Concepts

[Plan for backup and recovery in SharePoint Server](backup-and-recovery-planning.md)
#### Other Resources

[Use Windows PowerShell to administer SharePoint Server](/powershell/module/sharepoint-server/?view=sharepoint-ps)

