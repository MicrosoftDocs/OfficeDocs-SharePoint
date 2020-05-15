---
title: "The OneDrive sync app update process"
ms.reviewer: joleung
ms.author: kaarins
author: kaarins
manager: pamgreen
audience: Admin
f1.keywords:
- NOCSH
ms.topic: reference
ms.service: one-drive
localization_priority: Normal
ms.collection: 
- Strat_OD_admin
- M365-collaboration
search.appverid:
- ODB160
- MET150
ms.assetid: 2f748bc6-6f01-4406-a791-ec047f066d6d
description: "Learn about the Production and Deferred rings for OneDrive sync app updates"
---

# The OneDrive sync app update process

This article is for IT admins who manage the new OneDrive sync app (OneDrive.exe) in an enterprise environment. It explains how we release updates to the sync app for Windows and the standalone sync app for Mac through rings of validation, and how the sync app checks for updates. Note that if you deploy OneDrive alongside Office (via the Office Deployment Tool or some other means), OneDrive will continue to check for updates independent of any Office update restrictions you set.
  
> [!NOTE]
> If you allow your users to sync personal OneDrive accounts, the update process described in this article and any settings you select apply to all instances of the sync app.<br>The sync app installed from the Mac App Store follows a separate update process. After we finish rolling out updates within the Production ring, we publish them to the Mac App Store, where they're immediately released to everyone.
  
## How we release updates through multiple rings

After we validate updates through rings within Microsoft, we release them to the first public ring, Insiders. To try these latest features, join the [Windows Insider program](https://insider.windows.com/) or the [Office Insider](https://products.office.com/office-insider) program. It takes about 3 days to roll out to this ring. Later, we release to organizations in the default update ring, Production. We roll them out to a small percentage of users in the ring at first, and slowly roll them out to everyone in the ring. This typically takes one to two weeks. At each increase along the way, we monitor telemetry for quality assurance purposes. In the rare case we detect an issue, we suspend the release, address the issue, and release a new update to users in the same order. After updates have completely rolled out within the Production ring, we release them to the next ring, Enterprise.
  
![Timeline of an update](media/5d705fbc-5553-4c7b-ae2f-cba394332a5e.png)
  
The Deferred ring provides builds that have been monitored throughout the Production rollout, so fewer releases are suspended. The Deferred ring also lets you as an admin:
  
- Control when you deploy updates (within 60 days of their release).

- Deploy new versions from an internal network location to avoid using Internet bandwidth. (If you don't deploy an update after 60 days, it will be automatically downloaded and installed.)

However, as the slowest ring, the Deferred ring receives performance improvements, reliability fixes, and new features last.
  
> [!NOTE]
> Microsoft reserves the right to bypass the 60-day grace period for critical updates. 
  
To learn how to set the Deferred ring for the Windows sync app using Group Policy, see [Set the sync app update ring](use-group-policy.md#set-the-sync-app-update-ring). To learn how to set it for the Mac sync app, see [Configure the new OneDrive sync app on macOS](deploy-and-configure-on-macos.md). For info about the Microsoft 365 update process, see [Overview of update channels for Microsoft 365 Apps for enterprise](/DeployOffice/overview-of-update-channels-for-office-365-proplus). For info about the Windows 10 update process, see [Build deployment rings for Windows 10 updates](/windows/deployment/update/waas-deployment-rings-windows-10-updates).
  
## How the sync app checks for and applies updates

The OneDrive sync app checks for available updates every 24 hours when it's running. If it has stopped and hasn't checked for updates in more than 24 hours, the sync app will check for updates as soon as it's started. Windows 10 also has a scheduled task that updates the sync app even when it's not running.
  
To determine if an update is available, the OneDrive sync app checks if:
  
- The latest version released to the update ring is higher than what's installed on the computer. If the installed version is too old to be updated to the current version, the sync app will first be updated to the minimum version within the ring.
    
- The update is available to the computer based on the rollout percentage we set within the ring.
    
If both of these are true, OneDrive downloads the update to a hidden folder without any user interaction. After the download is complete, OneDrive verifies and installs it. If OneDrive is running, it's stopped and then restarted. Users don't need to sign in again, and they don't need administrative rights to install the update.
  
For info about the latest releases, see [New OneDrive sync app release notes](https://support.office.com/article/845dcf18-f921-435e-bf28-4e24b95e5fc0).

> [!NOTE]
> To apply sync app updates, computers in your organization must be able to reach the following: "oneclient.sfx.ms" and "g.live.com." Make sure you don't block these URLs. They are also used to enable and disable features and apply bug fixes. See [More info about the URLs and IP address ranges used in Microsoft 365](/office365/enterprise/urls-and-ip-address-ranges). 
  
## Deploying updates in the Deferred ring

At any given time, the next planned Deferred ring release is published on the [OneDrive sync app release notes](https://support.office.com/article/845dcf18-f921-435e-bf28-4e24b95e5fc0) page with a link to the corresponding installer and the target date when that version will be released. On the specified date, the "Rolling out" version for the Deferred ring becomes the new minimum. All sync apps below that version will automatically download the installer from the Internet and update themselves. 

To deploy an updated version of the sync app for Windows, run the following command using Microsoft Endpoint Configuration Manager:
  
```
Execute <pathToExecutable>\OneDriveSetup.exe /update /restart
```

Where pathToExecutable is a location on the local computer or an accessible network share and OneDriveSetup.exe is the target version downloaded from the release notes page. Running this command restarts OneDrive.exe on all computers. If you don't want to restart the sync app, remove the /restart parameter. See [Deploy using Microsoft Endpoint Configuration Manager](deploy-on-windows.md) for tips on how to set up the Microsoft Endpoint Configuration Manager deployment package.

To deploy an updated version of the sync app for Mac, deploy the OneDrive.pkg with the target version by using your MDM solution.
