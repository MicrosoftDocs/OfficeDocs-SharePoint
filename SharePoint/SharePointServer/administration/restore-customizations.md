---
title: "Restore customizations in SharePoint Server"
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
ms.assetid: 38147eec-d89a-478a-956a-779fe76c6679
description: "Learn how to restore customizations that are made to SharePoint Server sites."
---

# Restore customizations in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
You can restore any customizations that are made to SharePoint Server by using Central Administration or PowerShell. The restore tool that you use depends on the kind of environment that you have deployed, your schedule requirements, and what service level agreements that you have made with your organization.
  
    
## Before you begin
<a name="begin"> </a>

Before you begin this operation, review the following information:
  
- We recommend that you keep a backup of the original .wsp file and of the source code used to build the .wsp file for both trusted and sandboxed solutions. 
    
## Restoring solution packages in SharePoint Server
<a name="proc1"> </a>

The method that you use to restore solution packages is determined by whether the customizations were deployed as trusted solutions or sandboxed solutions.
  
Trusted solutions are solutions that farm administrators deploy. They are deployed to the complete farm, and can be used on any site within the farm. Trusted solutions are stored in the configuration database. Trusted solutions are backed up when a farm is backed up by using SharePoint Server backup, and are included in configuration-only backups, and can also be backed up as a group, or individually. They are visible in the restore hierarchy.
  
Sandboxed solutions are solutions that site collection administrators can deploy to a single site collection. Sandboxed solutions are stored in the content database associated with the site collection that they are deployed to. They are included in SharePoint Server farm, Web application, content database, and site collection backups, but are not visible in the restore hierarchy, and cannot be selected or restored individually.
  
### To restore a trusted solution by using Central Administration

1. Verify that the user account that is performing this procedure is a member of the Farm Administrators SharePoint group. 
    
2. Start Central Administration.
    
3. In Central Administration, on the home page, in the **Backup and Restore** section, click **Restore from a backup**.
    
4. On the Restore from Backup — Step 1 of 3: Select Backup to Restore page, from the list of backups, select the backup job that contains the solution package, and then click **Next**. You can view more details about each backup by clicking the (+) next to the backup. 
    
    > [!NOTE]
    > If the correct backup job does not appear, in the **Backup Directory Location** text box, type the Universal Naming Convention (UNC) path of the correct backup folder, and then click **Refresh**. 
  
5. On the Restore from Backup — Step 2 of 3: Select Component to Restore page, select the check box that is next to the solution, and then click **Next**.
    
6. On the Restore from Backup — Step 3 of 3: Select Restore Options page, in the **Restore Component** section, make sure that **Solution** appears in the **Restore the following component** list. 
    
    In the **Restore Only Configuration Settings** section, make sure that the **Restore content and configuration settings** option is selected. 
    
    In the **Restore Options** section, under **Type of Restore**, select the **Same configuration** option. A dialog box appears that asks you to confirm the operation. Click **OK**.
    
    Click **Start Restore**.
    
7. You can view the general status of all recovery jobs at the top of the Backup and Restore Job Status page in the **Readiness** section. You can view the status for the current recovery job in the lower part of the page in the **Restore** section. The status page updates every 30 seconds automatically. You can manually update the status details by clicking **Refresh**. Backup and recovery are Timer service jobs. Therefore, it may take several seconds for the recovery to start.
    
    If you receive any errors, you can review them in the **Failure Message** column of the Backup and Restore Job Status page. You can also find more details in the Sprestore.log file at the UNC path that you specified in step 3. 
    
### To restore a trusted solution by using PowerShell

1. Verify that you have the following memberships:
    
   - **securityadmin** fixed server role on the SQL Server instance. 
    
   - **db_owner** fixed database role on all databases that are to be updated. 
    
   - Administrators group on the server on which you are running the PowerShell cmdlets.
    
     An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint Management Shell.
    
3. At the PowerShell command prompt, type the following command:
    
   ```
   Restore-SPFarm -Directory <BackupFolder> -RestoreMethod Overwrite -BackupId <GUID> -Item <SolutionPath>
   ```

    Where:
    
   -  _\<BackupFolder\>_ is the UNC location of the directory that you want to restore from. 
    
   -  _\<GUID\>_ is the GUID of the backup ID that you want to restore from. If you do not specify a backup, the most recent one is used. 
    
   -  _\<SolutionPath\>_ is the path of the solution within the backup tree (usually farm\solutions\  _SolutionName_).
    
For more information, see [Restore-SPFarm](/powershell/module/sharepoint-server/Get-SPContentDatabase?view=sharepoint-ps). 
  
> [!NOTE]
> We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions. 
  
### Restoring a sandboxed solution
<a name="proc2"> </a>

You cannot restore only customizations that were deployed as sandboxed solutions. Instead, you must restore the farm, Web application, content database, or site collection with which the customization is associated.
  
## Restoring authored site elements in SharePoint Server
<a name="proc3"> </a>

You cannot restore only authored site elements. Instead, you must restore the farm, Web application, or content database with which the authored site element is associated.
  
## Restoring workflows in SharePoint Server
<a name="proc4"> </a>

Workflows are a special case of customizations that you can restore. Make sure that the backup and recovery plan includes any of the following scenarios that apply to the environment:
  
- Declarative workflows, such as those that are created in SharePoint Designer, are stored in the content database for the site collection to which they are deployed. Restoring the content database or site collection restores these workflows.
    
- Custom declarative workflow actions have components in the following three locations: 
    
  - The Visual Studio 2013 assemblies for the actions are stored in the global assembly cache (GAC).
    
  - The XML definition files (.actions files) are stored in the 16\TEMPLATE\< _LCID_>\Workflow directory.
    
  - An XML entry to mark the action as an authorized type is stored in the Web.config file for the Web applications in which it is used.
    
    If the farm workflows use custom actions, you should use a file restore system to restore these files and XML entries. You can reapply the files as needed after recovery.
    
- Workflows that depend on custom code, such as those that are created by using Visual Studio 2013, are stored in two locations. The Visual Studio 2013 assemblies for the workflow are stored in the GAC, and the XML definition files are stored in the Features directory. This is the same as other types of SharePoint Server features such as Web Parts and event receivers. If the workflow was installed as part of a solution package, follow the instructions for restoring solution packages. 
    
- If you create a custom workflow that interacts with a site collection other than the one where the workflow is deployed, you must restore both site collections to recover the workflow. Restoring a farm is sufficient to recover all site collections in the farm and all workflows that are associated with them.
    
- Workflows that are not deployed must be restored separately by using a file system backup application. 
    
## Restoring changes to the Web.config file in SharePoint Server
<a name="proc5"> </a>

You can recover changes to the Web.config file made by using Central Administration or the SharePoint Server APIs and object model by performing a farm or configuration-only restore. 
  
You should use a file system backup to protect changes to the Web.config file that are not made by using Central Administration or the SharePoint APIs and object model. You can recover the backup by using a file system restore. 
  
## Restoring developed customizations that are not packaged as solutions in SharePoint Server
<a name="proc7"> </a>

Restoring developed customizations that are not packaged as solutions can be a complex process because the customization file locations are not standardized.
  
Consult with the development team or customization vendor to determine whether the customizations involve additional add-in software or files in other locations. We recommend that you restore directories with a file system restore solution. The following table lists locations where customizations are typically stored on Web servers.
  
|**Location**|**Description**|
|:-----|:-----|
|%PROGRAMFILES%\Common files\Microsoft Shared\Web Server Extensions\16  <br/> |Commonly updated files, custom assemblies, custom templates, custom site definitions  <br/> |
|Inetpub  <br/> |Location of IIS virtual directories  <br/> |
|%WINDIR%\Assembly  <br/> |Global assembly cache (GAC): a protected operating system location where the Microsoft .NET Framework code assemblies are installed to provide full system access  <br/> |
   
## See also
<a name="proc7"> </a>

#### Concepts

[Back up customizations in SharePoint Server](back-up-customizations.md)
  
[Restore farms in SharePoint Server](restore-a-farm.md)
  
[Restore farm configurations in SharePoint Server](restore-a-farm-configuration.md)
  
[Restore web applications in SharePoint Server](restore-a-web-application.md)
  
[Restore content databases in SharePoint Server](restore-a-content-database.md)
  
[Restore site collections in SharePoint Server](restore-site-collections.md)

