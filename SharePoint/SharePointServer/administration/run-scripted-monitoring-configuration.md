---
title: "Run scripted monitoring configuration in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 9/20/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 5d1e3bb7-35e5-4756-b93c-f0a86c2bc244
description: "Learn how to use Microsoft PowerShell scripts and Profile files to automatically back up, restore, or change monitoring settings in a SharePoint Server nvironment."
---

# Run scripted monitoring configuration in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
Scripted monitoring configuration uses PowerShell scripts and XML files, which are known as **Profiles**, to back up, restore, or configure monitoring settings in the SharePoint Server 2016 environment. For more conceptual information about scripted monitoring configuration, see [Overview of scripted monitoring configuration in SharePoint Server](overview-of-scripted-monitoring-configuration.md).
  
> [!NOTE]
> You must download the PowerShell scripts to back up, restore, or change the farm monitoring settings. When you run the **BackupMonitoringSettings.ps1** SharePoint Server script, you create the backup Profile from which you can create other Profiles. 
  
## Use the BackupMonitoringSettings.ps1 script

You can use scripted monitoring configuration to back up the monitoring settings for the farm. You should do this immediately after you complete the deployment of the farm to make sure that that you can restore the farm to its original settings. You can also back up the settings before or after any changes to the farm.
  
> [!IMPORTANT]
> This script is available on the TechNet Gallery at [Scripted Monitoring Configuration - BackupMonitoringSettings](https://go.microsoft.com/fwlink/p/?LinkID=299269). 
  
 **To back up the farm monitoring settings**
  
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
  .\BackupMonitoringSettings.ps1 "<ProfileFolder>"
  ```

    Where:
    
  -  _\<ProfileFolder\>_ is full path of the folder that you want to store the backup settings Profile in. The XML file name is in the form "BackupSetting_[DATE] @ [Time].xml". The script will create a new file every time that it is run. 
    
## Use the AlterMonitoringSettings.ps1 script

You can use scripted monitoring configuration to change or restore the monitoring settings for the farm. To change the settings, create a copy of the backup Profile and change the settings in the copy to create a new Profile. To apply the settings in the new Profile, run the **AlterMonitoringSettings.ps1** script and specify the path of the specific Profile you want to use. For more information about how to create Profiles, see [Profile schema reference in SharePoint Server](profile-schema-reference.md). 
  
> [!IMPORTANT]
> This script is available on the TechNet Gallery at [Scripted Monitoring Configuration - AlterMonitoringSettings](https://go.microsoft.com/fwlink/p/?LinkID=299270). 
  
### Restore settings

You can use scripted monitoring configuration to restore the monitoring settings for the farm at any time. You can restore the settings to any values for which you have a corresponding Profile.
  
 **To restore the farm monitoring settings**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint Management Shell.
    
3. At the PowerShell command prompt, navigate to the folder that you downloaded the **BackupMonitoringSettings.ps1** and **AlterMonitoringSettings.ps1** scripts to. 
    
4. At the PowerShell command prompt, type the following command:
    
  ```
  .\AlterMonitoringSettings.ps1 "<ProfilePath>"
  ```

    Where:
    
  -  _\<ProfilePath\>_ is full path of the backup Profile that you want to use to restore the monitoring settings for the farm. 
    
### Apply settings changes

You can use scripted monitoring configuration to change the monitoring settings for the farm. To change the settings, run the **RestoreMonitoringSettings.ps1** script and specify the path of the specific Profile that you want to use. For more information about how to create Profiles, see [Profile schema reference in SharePoint Server](profile-schema-reference.md).
  
 **To apply monitoring settings changes to the farm**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  - Add memberships that are required beyond the minimums above.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint Management Shell.
    
3. At the PowerShell command prompt, navigate to the folder that you downloaded the **BackupMonitoringSettings.ps1** and **AlterMonitoringSettings.ps1** scripts to. 
    
4. At the PowerShell command prompt, type the following command:
    
  ```
  .\AlterMonitoringSettings.ps1 "<ProfilePath>"
  ```

    Where:
    
  -  _\<ProfilePath\>_ is full path of the specific Profile that you want to use to configure the monitoring settings for the farm. 
    
## See also

#### Concepts

[Overview of scripted monitoring configuration in SharePoint Server](overview-of-scripted-monitoring-configuration.md)
  
[Profile schema reference in SharePoint Server](profile-schema-reference.md)

