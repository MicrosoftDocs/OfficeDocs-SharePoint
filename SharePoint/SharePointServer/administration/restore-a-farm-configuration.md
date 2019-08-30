---
title: "Restore farm configurations in SharePoint Server"
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
ms.assetid: d849b7df-b26d-45f6-a74f-6641f18788cf
description: "Learn how to restore configuration information (such as antivirus, IRM, outbound email, and some customizations) for SharePoint Server."
---

# Restore farm configurations in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
You can restore a farm configuration in SharePoint Server by using the SharePoint Central Administration website or Microsoft PowerShell. Which backup tool you use depends on what kind of environment you have deployed, what your backup schedule requires, and what service level agreements you have made with your organization.
  
    
## Before you begin
<a name="begin"> </a>

Farm-level configuration recovery is performed only after a failure that involves the configuration database but does not involve other farm data, such as a content database or Web application. If restoring the farm configuration does not solve the problems, you must restore the complete farm. For more information about how to restore the complete farm, see [Restore farms in SharePoint Server](restore-a-farm.md). You can restore the configuration from a farm backup that used either the **Backup content and configuration settings** option or the **Backup only configuration settings** option. 
  
> [!NOTE]
> In earlier versions of SharePoint, you could not restore the configuration database and, therefore, you could not restore the configuration of a farm. Now you do not have to restore the configuration database because you can restore the farm configuration directly. 
  
## Using PowerShell to restore a farm's configuration in SharePoint
<a name="proc1"> </a>

You can use PowerShell to restore a farm's configuration.
  
 **To restore a farm's configuration by using PowerShell**
  
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
   Restore-SPFarm -Directory <RestoreShare> -RestoreMethod Overwrite -ConfigurationOnly
   ```

   Where _\<RestoreShare\>_ is network location where the backup file is stored. For more information, see [Restore-SPFarm](/powershell/module/sharepoint-server/Restore-SPFarm?view=sharepoint-ps). 

   > [!NOTE]
   > We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions. 
  
## Using Central Administration to restore a farm's configuration in SharePoint
<a name="proc2"> </a>

You can use Central Administration to restore a farm's configuration.
  
 **To restore a farm's configuration by using Central Administration**
  
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators SharePoint group on the computer that is running Central Administration.
    
2. **Verification:** Optionally, include steps that users should perform to verify that the operation was successful. 
    
    You must also be a member of the **sysadmin** fixed server role on the database server where each database is stored. 
    
3. In Central Administration, on the home page, in the **Backup and Restore** section, click **Restore from a backup**.
    
4. On the Restore from Backup — Step 1 of 3: Select Backup to Restore page, select the backup job that contains the farm backup from the list of backups, and then click **Next**.
    
    > [!NOTE]
    > You can view additional information about the backups by expanding the row that contains the backup. 
  
    > [!NOTE]
    > If the correct backup job does not appear, in the **Backup Directory Location** text box, enter the UNC path of the correct backup folder, and then click **Refresh**. 
  
5. On the Restore from Backup — Step 2 of 3: Select Component to Restore page, select the check box that is next to the farm, and then click **Next**.
    
6. On the Restore from Backup — Step 3 of 3: Select Restore Options page, in the **Restore Component** section, make sure that "Farm" appears in the **Restore the following content** list. 
    
    In the **Restore Only Configuration Settings** section, make sure that the **Restore content and configuration settings** option is selected. 
    
    In the **Restore Options** section, select the **Type of Restore** option. Use the **Same configuration** setting. A dialog box will appear that asks you to confirm the operation. Click **OK**.
    
    > [!NOTE]
    > If the **Restore Only Configuration Settings** section does not appear, then the backup that you selected is a configuration-only backup. 
  
    Click **Start Restore**.
    
7. You can view the general status of all recovery jobs at the top of the Backup and Restore Status page in the **Readiness** section. You can view the status of the current recovery job in the lower part of the page in the **Restore** section. The status page updates every 30 seconds automatically. You can manually update the status details by clicking **Refresh**. Backup and recovery are Timer service jobs. Therefore, it may take several seconds for the recovery to start.
    
    If you receive any errors, you can review them in the **Failure Message** column of the Backup and Restore Job Status page. You can also find more details in the Sprestore.log file at the UNC path that you specified in step 2. 
    
## See also
<a name="proc2"> </a>

#### Concepts

[Back up farm configurations in SharePoint Server](back-up-a-farm-configuration.md)

