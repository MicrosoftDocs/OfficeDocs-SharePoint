---
title: "Install the sync client per machine"
ms.reviewer: 
ms.author: kaarins
author: kaarins
manager: pamgreen
audience: Admin
ms.topic: article
ms.service: one-drive
localization_priority: Normal
ms.custom: Adm_O365
search.appverid:
- MET150
- BCS160
ms.collection: 
- Strat_OD_admin
- M365-collaboration
ms.assetid: 6891b561-a52d-4ade-9f39-b492285e2c9b
description: "Learn how to install the OneDrive sync client for every user account on a Windows PC."
---

# Install the sync client per machine (preview)

By default, the OneDrive sync client installs per user, meaning OneDrive.exe needs to be installed for each user account on the PC under the %localappdata% folder. With the new per-machine installation option, you can install OneDrive under the “Program Files (x86)” directory, meaning all profiles on the computer will use the same OneDrive.exe binary. Other than where the sync client is installed, the behavior is the same.  

The new per-machine sync client provides:

- Automatic transitioning from the previous OneDrive sync client (Groove.exe)
- Automatic conversion from per-user to per-machine
- Automatic updates when a new version is available

The per-machine sync client supports syncing OneDrive and SharePoint files in Microsoft 365 and in SharePoint Server 2019. 

## Requirements

- All Windows versions supported by the sync client. [Learn more](https://support.office.com/article/onedrive-system-requirements-cc0cb2b8-f446-445c-9b52-d3c2627d681e)
- Sync client build 19.043.0304.0006 or later. For info about which sync client build is available in each ring, see [New OneDrive sync client release notes](https://support.office.com/article/845dcf18-f921-435e-bf28-4e24b95e5fc0).
- To apply sync client updates, computers in your organization must be able to reach the following: "oneclient.sfx.ms" and "g.live.com." Make sure you don't block these URLs. They are also used to enable and disable features and apply bug fixes. [More info about the URLs and IP address ranges used in Office 365](/office365/enterprise/urls-and-ip-address-ranges).

  
## Deployment instructions

1. Download OneDriveSetup.exe.
2. Run “OneDriveSetup.exe /allusers” from a command prompt window (will result in a UAC prompt) or by using SCCM. This will install the sync client under the “Program Files (x86)\Microsoft OneDrive” directory. 
When setup completes, OneDrive will start. If accounts were added on the computer, they'll be migrated automatically.  
  
## FAQ

**Do I need to move to the per-machine sync client?** 
The per-machine sync client is helpful especially for multi-user computers and when you don’t want exe files running from the user profile. Over time, we will recommend that more and more customers switch to per-machine installation. 
 
**With per-machine installation, will a single OneDrive.exe process be shared by all users on the computer?** 
No, although a single version of OneDrive.exe is installed, a new process is created for every OneDrive account syncing on the computer. 
 
**Will the same update rings apply to per-machine?** 
If you selected the Insiders ring (via the [Windows Insider program](https://insider.windows.com/) or [Office Insider](https://products.office.com/office-insider) programs) or are in the default Production ring, you will continue to be in the same ring as before. 
 
In the past you may have used a user group policy (under HKCU) to select the Enterprise ring ([Receive OneDrive sync client updates on the Enterprise ring](https://docs.microsoft.com/en-us/OneDrive/use-group-policy#EnableEnterpriseUpdate)). This group policy will not work with the per-machine install. To select the ring, use the computer group policy (under HKLM) instead ([Set the sync client update ring](use-group-policy.md#GPOSetUpdateRing)).

> [!NOTE]
> We do not recommend selecting the Enterprise ring while this feature is in preview because you will not receive bug fixes for any issues we find.  
 
**Does the per-machine sync client follow the same update process/cadence as the per-user sync client?** 
Yes, the per-machine sync client will auto-update on the same cadence as the per-user sync client and the same rings are supported (see question above). The [release notes](https://support.office.com/article/845dcf18-f921-435e-bf28-4e24b95e5fc0) are the same. [More info about the sync client update process](sync-client-update-process.md)
 
The sync client is an extension of the service and a very thin client so auto-updating to the latest version is critical to maintaining a high-quality sync experience. As a result, we recommend that you keep your users in the default Production ring and rely on auto-update to take care of updating to the latest version. If your organization requires you to deploy updates manually through SCCM, we recommend that you select the Enterprise ring and deploy the upcoming builds before auto-update takes effect as described here. 

**Do automatic updates of the per-machine sync client require user intervention?**
User intervention is not required for the per-machine sync client to update itself. Elevation is required when you first set it up. During setup, we install a scheduled task and a Windows service, which are used to perform the updates silently without user intervention since they run in elevated mode.

**How do I revert back to the per-user sync client if required?** 
We do not support automated migration from per-machine to per-user. To revert back after installing per-machine, please uninstall the sync client and [install the latest released version](https://go.microsoft.com/fwlink/?linkid=844652) without the “/allusers” parameter.

**How can I detect the installation through SCCM?** 

For SCCM, to detect the install we used the following two registry detection rules with an OR() connector:

|Field|Value|
|---|---|
|Hive|   HKEY_LOCAL_MACHINE|
|Key|    SOFTWARE\Wow6432Node\Microsoft\OneDrive|
|Value|  Version|
|32bit on 64bit| TRUE|
|Type|   Version|
|Value|  19.043.0304.0007|


|Field|Value|
|---|---|
|Hive|   HKEY_LOCAL_MACHINE|
|Key|    SOFTWARE\Microsoft\OneDrive|
|Value|  Version|
|32bit on 64bit| FALSE|
|Type|   Version|
|Value|  19.043.0304.0007|

This allows the per-machine version to be detected independent of the underlying client architecture.


  

