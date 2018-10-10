---
title: "Configure Files On-Demand for Mac"
ms.author: kaarins
author: kaarins
manager: pamgreen
ms.audience: Admin
ms.topic: article
ms.service: one-drive
localization_priority: Normal
ms.collection: Strat_OD_sync
search.appverid:
- ODB160
- OFF160
- ODB150
- MET150
ms.assetid: 3eff17b9-c709-462f-946c-17719af68aca
description: "Learn how to configure Files On-Demand for Mac."
---

# Configure Files On-Demand for Mac

This article describes the preferences and scriptable commands you can use to set up OneDrive Files On-Demand for Mac. For more info about using Files On-Demand on a Mac, see [Try Files On-Demand for Mac](https://support.office.com/article/529f6d53-e572-4922-a585-e7a318c135f0).

> [!NOTE]
> The following configurations are subject to change. 

## Preferences  

PList Location 
- ~/Library/Preferences/com.microsoft.OneDrive.plist

Domain
- com.microsoft.OneDrive

|**Setting**|**Description**|**Parameters**|**Example Plist Entry**|
|:-----|:-----|:-----|:-----|
|FilesOnDemandPolicy  <br/> |This setting determines whether Files On-Demand should be enabled based on the OneDrive controlled rollout or the FilesOnDemandEnabled setting.  <br/> |FilesOnDemandPolicy (Bool): When set to true, Files On-Demand will be enabled or disabled based on FilesOnDemandEnabled.  <br/> |\<key\>FilesOnDemandPolicy\</key\>  <br/> \<(Bool)/\>  <br/> |
|FilesOnDemandEnabled  <br/> |This setting determines whether Files On-Demand should be enabled.    <br/> |FilesOnDemandEnabled (Bool): When set to true, Files On-Demand will be enabled or disabled.  <br/> |\<key\>FilesOnDemandEnabled\</key\>  <br/> \<(Bool)/\>  <br/> |
|IsHydrationToastAllowed  <br/> |This setting determines if a toast should appear when an application causes file contents to be downloaded.   <br/> |IsHydrationToastAllowed (Bool): When set to false, toasts will not appear when applications trigger the download of file contents.  <br/> |\<key\>IsHydrationToastAllowed\</key\>  <br/> \<(Bool)/\>  <br/> |
|HydrationDisallowedApps  <br/> |Applications will not be allowed to trigger the download of cloud-only files. You can use this setting to lock down applications that don't work correctly with your deployment of Files On-Demand.   <br/> |HydrationDisallowedApps (String): Json in the following format <br/>'[{"ApplicationId":"appId","MaxBundleVersion":"1.1","MaxBuildVersion":"1.0"}]'<br/> AppID can be either the BSD process name or the bundle display name. <br/> MaxBuildVersion denotes the maximum build version of the application that will be blocked <br/> MaxBundleVersion denotes the maximum bundle version of the application that will be blocked  <br/> |\<key\>HydrationDisallowedApps \</key\>  <br/> \<string> [{"ApplicationId":"appId","MaxBundleVersion":"1.1","MaxBuildVersion":"1.0"}, {"ApplicationId":"appId2","MaxBundleVersion":"3.2","MaxBuildVersion":"2.0"},]] 
</string>   <br/> |

## Scriptable commands

To query and set the file and folder status, use:
 
Query file status 

/Applications/OneDrive.app/Contents/MacOS/OneDrive /getpin <path> 
 
Set file status  

/Applications/OneDrive.app/Contents/MacOS/OneDrive /pin <path> 
/Applications/OneDrive.app/Contents/MacOS/OneDrive /unpin <path> 
/Applications/OneDrive.app/Contents/MacOS/OneDrive /clearpin <path> 

(where "pin" sets the file to always available on the device, "unpin" to locally available, and "clearpin" to online-only)
 
For folders, add the /r parameter to set the status for all items within the folder.

