---
title: "Back up customizations in SharePoint Server"
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
ms.assetid: 8f98a750-19bb-4ea0-9ff5-719b85febbb3
description: "Learn how to back up customizations that are made to SharePoint Server sites."
---

# Back up customizations in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
You can back up customizations that are made to SharePoint Server sites by using the SharePoint Central Administration website or Microsoft PowerShell. Which backup tool you use depends on what kind of environment you have deployed, what your backup schedule requires, and what service level agreements you have made with your organization. 
  
    
## Before you begin
<a name="begin"> </a>

Before you begin this operation, review the following list of possible customizations that you can make to your sites:
  
- Customizations packaged as solutions (.wsp files). Solutions contain developed site elements, and are typically created by developers. Developed site elements include the following:
    
  - Web Parts
    
  - Workflows
    
  - Site and list definitions
    
  - Document converters
    
  - Event receivers
    
  - Timer jobs
    
  - Assemblies
    
- Authored site elements, which are typically created by web designers, are not explicitly compiled and are located in a content database. Authored site elements include the following:
    
  - Master pages
    
  - Cascading style sheets
    
  - Forms
    
  - Layout pages
    
- Changes to the Web.config file 
    
- Third-party solutions and their associated binary files and registry keys, such as IFilters
    
- Changes to sites created by direct editing through the browser
    
- Developed customizations that are not packaged as solutions
    
> [!NOTE]
> Each of these kinds of customizations requires a different type of backup. 
  
## Back up solution packages in SharePoint Server
<a name="proc1"> </a>

Solution packages can be created by using SharePoint Designer or Visual Studio. We strongly recommend that all customizations be deployed as solution packages. For more information, see [Creating SharePoint Solution Packages](/visualstudio/sharepoint/creating-sharepoint-solution-packages?view=vs-2017).
  
A solution package is a deployable, reusable file that can contain a set of features, site definitions, and assemblies that apply to sites, and that you can enable or disable individually. Solution packages can include Web Parts, site or list definitions, custom columns, new content types, custom fields, custom actions, coded workflows, or workflow activities and conditions.
  
The method that you use to back up solution packages is determined by whether the customizations are deployed as trusted solutions or sandboxed solutions (partially trusted code). 
  
Trusted solutions are solution packages that farm administrators deploy. Trusted solutions are deployed to the entire farm and can be used on any site within the farm. Trusted solutions are stored in the configuration database. Trusted solutions are backed up when a farm is backed up by using SharePoint Server backup, and are included in configuration-only backups. You can also back up trusted solutions as a group or individually. Trusted solutions are visible in the backup hierarchy.
  
Sandboxed solutions are solution packages that site collection administrators can deploy to a single site collection. Sandboxed solutions are stored in the content database that is associated with the site collection to which the solution packages are deployed. They are included in SharePoint Server farm, web application, content database, and site collection backups, but are not visible in the backup hierarchy and cannot be selected or backed up individually.
  
We recommend that you keep a backup of the original .wsp file and the source code used to build the .wsp file for both trusted solutions and sandboxed solutions. 
  
 ### To back up trusted solutions by using Central Administration
  
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
2. Start Central Administration.
    
3. In Central Administration, on the home page, in the **Backup and Restore** section, click **Perform a backup**.
    
4. On the **Perform a Backup — Step 1 of 2: Select Component to Back Up** page, select **Solutions**, and then click **Next**.
    
    You can also select an individual solution, if you only want to back up a single solution.
    
5. On the **Start Backup — Step 2 of 2: Select Backup Options** page, in the **Backup Type** section, select either **Full** or **Differential**.
    
    > [!NOTE]
    > If you are backing up the solution for the first time, you must use the **Full** option. You must perform a full backup before you can perform a differential backup. 
  
6. In the **Backup File Location** section, type the Universal Naming Convention (UNC) path of the backup folder, and then click **Start Backup**.
    
7. You can view the general status of all backup jobs at the top of the Backup and Restore Job Status page in the **Readiness** section. You can view the status of the current backup job in the lower part of the page in the **Backup** section. The status page updates every 30 seconds automatically. You can manually update the status details by clicking **Refresh**. Backup and recovery are Timer service jobs. Therefore, it may take several seconds for the backup to start.
    
    If you receive any errors, review the **Failure Message** column of the **Backup and Restore Job Status** page. You can also find more details in the Spbackup.log file at the UNC path that you specified in step 4. 
    
 ### To back up trusted solutions by using PowerShell
  
1. Verify that you have the following memberships:
    
   - **securityadmin** fixed server role on the SQL Server instance. 
    
   - **db_owner** fixed database role on all databases that are to be updated. 
    
   - Administrators group on the server on which you are running the PowerShell cmdlets.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint Management Shell.
    
3. At the PowerShell command prompt, type the following command to back up all of the solutions in the farm. To back up a single solution, add the name of the solution to the item path "farm\solutions".
    
   ```powershell
   Backup-SPFarm -backupmethod full -directory <UNC location> -item "farm\solutions"
   ```

    Where:
    
   -  _\<UNC location\>_ is the UNC location of the directory where you store the backup file. 
    
For more information, see [Backup-SPFarm](/powershell/module/sharepoint-server/Backup-SPFarm?view=sharepoint-ps).
  
> [!NOTE]
> We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions. 
  
### Backing up sandboxed solutions in SharePoint Server
<a name="SandboxedSolutions"> </a>

You cannot back up only sandboxed solutions. Instead, you must back up the farm, Web application, or content database with which the sandboxed solution is associated.
  
## Back up authored site elements in SharePoint Server
<a name="AuthoredSite"> </a>

You cannot back up only authored site elements. Instead, you must back up the farm, Web application, or content database with which the authored site element is associated.
  
## Back up workflows in SharePoint Server
<a name="Workflows"> </a>

Workflows are a special case of customizations that you can back up. Make sure that your backup and recovery plan addresses any of the following scenarios that apply to your environment:
  
- Declarative workflows, such as those that were created in SharePoint Designer, are stored in the content database for the site collection to which they are deployed. Backing up the content database protects these workflows.
    
- Custom declarative workflow actions have components in the following three locations: 
    
  - The Visual Studio 2013 assemblies for the actions are stored in the global assembly cache (GAC).
    
  - The XML definition files (.ACTIONS files) are stored in the 16\TEMPLATE\< _LCID_>\Workflow directory.
    
  - An XML entry to mark the action as an authorized type is stored in the Web.config file for the Web applications in which it is used.
    
    If the farm workflows use custom actions, you should use a file backup system to protect these files and XML entries. Similar to features such as Web Parts and event receivers, these files should be reapplied to the farm as needed after recovery.
    
- Workflows that depend on custom code, such as those that are created by using Visual Studio, are stored in two locations. The Visual Studio assemblies for the workflow are stored in the GAC, and the XML definition files are stored in the Features directory. This is the same as other types of SharePoint features such as Web Parts and event receivers. If the workflow was installed as part of a solution package, backing up the farm, Web application, content database, or site collection protects these workflows. 
    
- If you create a custom workflow that interacts with a site collection other than the one where the workflow is deployed, you must back up both site collections to protect the workflow. This includes workflows that write to a history list or other custom list in another site collection. Performing a farm backup is sufficient to back up all site collections in the farm and all workflows that are associated with them.
    
- Workflows that are not yet deployed must be backed up and restored separately. When you are developing a new workflow but have not yet deployed it to the SharePoint Server farm, make sure that you back up the folder where you store the workflow project files by a file system backup application.
    
## Back up changes to the Web.config file in SharePoint Server
<a name="WebConfig"> </a>

A common customization to SharePoint Server is to change the Web.config file. We strongly recommend that you make changes to the Web.config file by using Central Administration or the SharePoint Server APIs and object model. Because these changes are stored in the configuration database, they can be recovered from a farm or configuration-only backup. 
  
Changes to the Web.config file that are not made by using Central Administration or the SharePoint Server APIs and object model should be protected by using a file system backup. 
  
> [!NOTE]
> If you are using forms-based authentication, provider registration in the Web.config file is manual, and is not protected by SharePoint Server backup. In this case, make sure that you back up the Web.config file by using a file system backup. 
  
## Back up third-party products in SharePoint Server
<a name="ThirdParty"> </a>

If third-party products are deployed as solution packages, they are protected by SharePoint Server backup. We recommend that you keep all the original files, distribution media, documentation, and the license and product keys that are required for installation.
  
## Back up developed customizations that are not packaged as solutions in SharePoint Server
<a name="DevelopedCustomizations"> </a>

Backing up developed customizations that are not deployed as solution packages can be a complex process because the customization file locations might not be stored in standardized places and SharePoint Server does not automatically back them up.
  
Consult with the development team or customization vendor to determine whether the customizations involve additional add-in software or files in other locations. We recommend that you back up these directories with a file system backup solution. The following table lists locations where developed customizations are typically stored on Web servers.
  
|**Location**|**Description**|
|:-----|:-----|
|%PROGRAMFILES%\Common files\Microsoft Shared\Web Server Extensions\16  <br/> |Commonly updated files, custom assemblies, custom templates, custom site definitions  <br/> |
|Inetpub  <br/> |Location of IIS virtual directories  <br/> |
|%WINDIR%\Assembly  <br/> |Global assembly cache (GAC): a protected operating system location where the Microsoft .NET Framework code assemblies are installed to provide full system access  <br/> |
   
## See also
<a name="DevelopedCustomizations"> </a>

#### Concepts

[Restore customizations in SharePoint Server](restore-customizations.md)
  
[Back up farms in SharePoint Server](back-up-a-farm.md)
  
[Back up farm configurations in SharePoint Server](back-up-a-farm-configuration.md)
  
[Back up web applications in SharePoint Server](back-up-a-web-application.md)
  
[Back up content databases in SharePoint Server](back-up-a-content-database.md)
  
[Back up site collections in SharePoint Server](back-up-site-collections.md)
  
[Update Workflow in SharePoint Server](../governance/update-workflow-in-sharepoint-server.md)

