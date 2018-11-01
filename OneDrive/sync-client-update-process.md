---
title: "The OneDrive sync client update process"
ms.author: kaarins
author: kaarins
manager: pamgreen
ms.date: 04/9/2018
ms.audience: Admin
ms.topic: reference
ms.service: one-drive
localization_priority: Normal
search.appverid:
- ODB160
- MET150
ms.assetid: 2f748bc6-6f01-4406-a791-ec047f066d6d
description: "Learn about the Production and Enterprise rings for OneDrive sync client updates"
---

# The OneDrive sync client update process

This article is for IT admins who manage the new OneDrive sync client in an enterprise environment. It explains how we release updates to the Windows sync client and the standalone Mac sync client through rings of validation, and how the sync client (OneDrive.exe) checks for updates.
  
> [!NOTE]
> If you allow your users to sync personal OneDrive accounts, the update process described in this article and any settings you select apply to all instances of the sync client.<br>The sync client installed from the Mac App Store follows a separate update process. After we finish rolling out updates within the Production ring, we publish them to the Mac App Store, where they're immediately released to everyone. 
  
## How we release updates through multiple rings

After we validate updates through rings within Microsoft, we release them to the first public ring, Insiders. To try these latest features, join the [Windows Insider program](https://insider.windows.com/) or the [Office Insider](https://products.office.com/office-insider) program. It takes about 3 days to roll out to this ring. Later, we release to organizations in the default update ring, Production. We roll them out to a small percentage of users in the ring at first, and slowly roll them out to everyone in the ring. This typically takes one to two weeks. At each increase along the way, we monitor telemetry for quality assurance purposes. In the rare case we detect an issue, we suspend the release, address the issue, and release a new update to users in the same order. After updates have completely rolled out within the Production ring, we release them to the next ring, Enterprise.
  
![Timeline of an update](media/5d705fbc-5553-4c7b-ae2f-cba394332a5e.png)
  
The Enterprise ring provides builds that have been monitored throughout the Production rollout, so fewer releases are suspended. The Enterprise ring also lets you as an admin:
  
- Control when you deploy updates (within 60 days of their release).
    
- Deploy new versions from an internal network location to avoid using Internet bandwidth. (If you don't deploy an update after 60 days, it will be automatically downloaded and installed.)
    
However, as the slowest ring, the Enterprise ring receives performance improvements, reliability fixes, and new features last.
  
> [!NOTE]
> Microsoft reserves the right to bypass the 60-day grace period for critical updates. 
  
To learn how to set the Enterprise ring for the Windows sync client using Group Policy, see [Delay updating OneDrive.exe until the second release wave](use-group-policy.md#EnableEnterpriseUpdate). To learn how to set it for the Mac sync client, see [Configure the new OneDrive sync client on macOS](deploy-and-configure-on-macos.md). For info about the Office 365 update process, see [Overview of update channels for Office 365 ProPlus](https://support.office.com/article/9ccf0f13-28ff-4975-9bd2-7e4ea2fefef4). For info about the Windows 10 update process, see [Build deployment rings for Windows 10 updates](https://go.microsoft.com/fwlink/?linkid=860294).
  
## How the sync client checks for and applies updates

The OneDrive sync client checks for available updates every 24 hours when it's running. If it has stopped and hasn't checked for updates in more than 24 hours, the sync client will check for updates as soon as it's started. Windows 10 also has a scheduled task that updates the sync client even when it's not running.
  
To determine if an update is available, the OneDrive sync client checks if:
  
- The latest version released to the update ring is higher than what's installed on the computer. If the installed version is too old to be updated to the current version, the sync client will first be updated to the minimum version within the ring.
    
- The update is available to the computer based on the rollout percentage we set within the ring.
    
If both of these are true, OneDrive downloads the update to a hidden folder without any user interaction. After the download is complete, OneDrive verifies and installs it. If OneDrive is running, it's stopped and then restarted. Users don't need to sign in again, and they don't need administrative rights to install the update.
  
For info about the latest releases, see [New OneDrive sync client release notes](https://support.office.com/article/845dcf18-f921-435e-bf28-4e24b95e5fc0).

> [!NOTE]
> To apply sync client updates, computers in your organization must be able to reach the following: "oneclient.sfx.ms" and "g.live.com." Make sure you don't block these URLs as they are also used to enable/disable features and bug fixes. [More info about the URLs and IP address ranges used in Office 365](https://support.office.com/article/8548a211-3fe7-47cb-abb1-355ea5aa88a2.) 
  
## Deploying updates in the Enterprise ring

At any given time, the next planned Enterprise ring release is published on the [OneDrive sync client release notes](https://support.office.com/article/845dcf18-f921-435e-bf28-4e24b95e5fc0) page with a link to the corresponding installer and the target date when that version will be released. On the specified date, the "Rolling out" version for the Enterprise ring becomes the new minimum. All sync clients below that version will automatically download the installer from the Internet and update themselves. 


To deploy an updated version of the sync client for Windows, run the following command using System Center Configuration Manager:
  
```
Execute <pathToExecutable>\OneDriveSetup.exe /update /restart
```

Where pathToExecutable is a location on the local computer or an accessible network share and OneDriveSetup.exe is the target version downloaded from the release notes page. Running this command restarts OneDrive.exe on all computers. If you don't want to restart the sync client, remove the /restart parameter. See [Deploy using SCCM](https://docs.microsoft.com/en-us/onedrive/deploy-on-windows) for tips on how to set up the SCCM deployment package.

To deploy an updated version of the sync client for Mac, deploy the OneDrive.pkg with the target version with your MDM solution.
  
  

