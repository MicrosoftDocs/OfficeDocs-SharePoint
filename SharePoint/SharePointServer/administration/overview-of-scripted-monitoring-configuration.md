---
title: "Overview of scripted monitoring configuration in SharePoint Server"
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
ms.assetid: 9e7368a1-9299-4827-b756-45fb3b4ad809
description: "Learn how to use Microsoft PowerShell and XML to automate the configuration of monitoring settings for SharePoint Server."
---

# Overview of scripted monitoring configuration in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
You can change the monitoring settings for SharePoint Server environments several ways. One way is to use the SharePoint Central Administration website. You might use this to make a single change to a small, local farm. Another way is to use PowerShell cmdlets directly. You might use this to make a single change to a local or remote farm. Still another way is to create your own PowerShell scripts. You might use these scripts to make multiple complex changes to local or remote farms that might be done repeatedly.
  
Scripted monitoring configuration involves a set of PowerShell script files and XML data files, called Profiles, to enable administrators to automate configuration of the monitoring settings in SharePoint Server environments, including back up and restore of these settings. Administrators can run the scripts before, during, and after changes to the farm. Changes might include updates of the farm topology, major security changes, software updates, or performance tests. The scripts change the monitoring settings so that all of the necessary monitoring data are collected during the event without flooding the Logging database during normal operation.
  
- Diagnostic Settings
    
- Usage Service settings
    
- Usage definitions
    
- Log level settings
    
- Timer job settings
    
- SharePoint Health Analyzer rule settings
    
You can run scripted monitoring configuration to backup and restore monitoring settings for the farm without having to run backup and restore. You can use it to change the monitoring settings so that all of the necessary monitoring data is collected during the event without flooding the Logging database during normal operation. You can also run the scripts to tune the level of monitoring during different phases of the SharePoint lifecycle. For more information, see [Run scripted monitoring configuration in SharePoint Server](run-scripted-monitoring-configuration.md).
  
You can also copy and modify the backup Profile to create Profiles for specific purposes. For more information, see [Profile schema reference in SharePoint Server](profile-schema-reference.md).
  
## The components of scripted monitoring configuration

Scripted monitoring configuration consists of both PowerShell scripts and Profiles that contain the settings data for changes in the farm. The scripts are available on the TechNet Library. Following are the scripts and Profiles that are involved:
  
- **BackupMonitoringSettings.ps1**
    
    Run this PowerShell script on a farm to back up various logging settings to an XML file.
    
    > [!IMPORTANT]
    > This script is available on the TechNet Gallery at [Scripted Monitoring Configuration - BackupMonitoringSettings](https://go.microsoft.com/fwlink/p/?LinkId=299269). 
  
- **AlterMonitoringSettings.ps1**
    
    Run this PowerShell script on a server to restore or change various logging settings by using an XML Profile as a data source.
    
    > [!IMPORTANT]
    > This script is available on the TechNet Gallery at [Scripted Monitoring Configuration - AlterMonitoringSettings](https://go.microsoft.com/fwlink/p/?LinkId=299270). 
  
- **Backup Profile**
    
    The **BackupMonitoringSettings.ps1** script creates this XML file which contains all of the monitoring settings mentioned above. You can use the **AlterMonitoringSettings.ps1** script backup file to restore the settings to the farm. You can also use this file as a template to create another Profile or to make changes to another farm. 
    
- **Profiles**
    
    Create one or more of these XML files to modify the settings to the farm by using the **AlterMonitoringSettings.ps1** script. 
    
## The scripted monitoring configuration process

1. **Run the BackupMonitoringSettings.ps1 script**
    
    Run this script on a farm to back up various monitoring settings to an XML Profile that the script creates. The XML file name is in the form "BackupSetting_[DATE] @ [Time].xml". The script creates a new file every time you run it.
    
2. **Create a Profile by copying and altering settings in the backup Profile**
    
    You can make a copy of the BackupSettings.xml file and change the settings. You can then use the updated file as the source for changes to your farm.
    
    > [!IMPORTANT]
    > Always preserve the original BackupSettings.xml file so that you can use it to restore your farm to the original configuration. To create custom Profiles, modify a copy of the BackupSettings.xml file. 
  
3. **Applying settings changes by running the AlterMonitorngSettings.ps1 script**
    
    After you create your own Profile, you can run the **AlterMonitoringSettings.ps1** script to apply those changes to the farm. 
    
4. **Restore settings**
    
    To restore the setting to a previous state, run the **AlterMonitoringSettings.ps1** script and provide the path of a BackupSettings.xml file. 
    
5. **Apply a Profile to another farm**
    
    You can also use a Profile to apply the settings from one farm to another farm. Or you can use an updated settings file to apply settings to many farms.
    
## See also

#### Concepts

[Profile schema reference in SharePoint Server](profile-schema-reference.md)
  
[Run scripted monitoring configuration in SharePoint Server](run-scripted-monitoring-configuration.md)
#### Other Resources

[App Management Service cmdlets in SharePoint Server](/powershell/module/sharepoint-server/?view=sharepoint-ps)

