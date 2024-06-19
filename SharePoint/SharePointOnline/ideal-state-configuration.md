---
ms.date: 07/01/2023
title: "Recommended sync app configuration"
ms.reviewer: gacarini
ms.author: mactra
author: MachelleTranMSFT
manager: jtremper
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: conceptual
ms.service: one-drive
ms.localizationpriority: medium
ms.collection: 
- Strat_OD_admin
- M365-collaboration
ms.custom:
- seo-marvel-apr2020
- onedrive-toc
search.appverid:
- ODB160
- ODB150
- GOB150
- GOB160
- MET150
ms.assetid: b664e743-ae8b-4a93-aefd-1b20c584a93a
description: "View our recommendations for deploying and configuring the OneDrive sync app."
---

# Recommended sync app configuration

For the best performance, reliability, and user experience, follow these "ideal state" recommendations when you configure the OneDrive sync app.

|![Diagram that shows the Download symbol.](/office/media/icons/download-blue.png)</br>Updates and rings   |![Diagram that shows the Chat symbol.](/office/media/icons/chat.png)</br>Windows Notification Service  |![Diagram that shows a Cloud symbol](/office/media/icons/cloud.png) </br>Files On-Demand and Storage Sense |![Diagram that shows the User settings symbol](/office/media/icons/users-settings.png)</br>Silent account configuration |![Diagram that shows the Migration arrow symbol](/office/media/icons/migration-blue.png)</br>Known Folder Move|
|---------|---------|---------|---------|---------|---------|
|Allow traffic. Select some people for the Insiders ring and leave the rest in Production    |   Allow traffic      |   Keep Files On-Demand enabled and enable Storage Sense policies      |     Enable the policy    |     Enable the policies    |

## Updates and rings

- **Allow access to oneclient.sfx.ms and g.live.com**. Computers must be able to reach these URLs to apply updates and bug fixes, and enable or disable features. Updates are installed automatically; so, you don't need to package and deploy them. Because OneDrive runs in the background, updates are also installed silently and don't impact users.
- **Use the Insiders and Production rings**. Select several people in your IT department as early adopters to join the Insiders ring and receive features early. Leave everyone else in the organization on the default Production ring to ensure they receive bug fixes and new features in a timely fashion. This recommendation applies even if you are on the Semi-Annual Enterprise Channel for Windows and Office. For more information about the rings, see [Sync app update process](sync-client-update-process.md). To set the update ring on Windows, see [Set the sync app update ring](use-group-policy.md#set-the-sync-app-update-ring). To set it on Mac, see [Deploy and configure the new OneDrive sync app for Mac](deploy-and-configure-on-macos.md#tier).

## Windows Notification Service
  
- **Make sure connection to the service is enabled**. Work with your network team to ensure proxies:  

  - Allow network traffic to bypass *.wns.windows.com
  - Avoid HTTPS decryption for *.wns.windows.com

    This requirement applies to both Windows and Mac. [See the complete list of required URL and IP address ranges](/office365/enterprise/urls-and-ip-address-ranges#sharepoint-online-and-onedrive-for-business).

## Files On-Demand and Storage Sense

- **Keep Files On-Demand enabled**. OneDrive Files On-Demand helps users access all their files (individual or shared) without having to download them and use storage space. This setting is on by default for Windows 10 and Mac. To check this setting for Windows, see [Use OneDrive Files On-Demand](use-group-policy.md#use-onedrive-files-on-demand). To check it for Mac, see [Deploy and configure the new OneDrive sync app for Mac](deploy-and-configure-on-macos.md).
- **Use Storage Sense policies on PCs**. These policies let you automatically clean up "locally available" files users haven't explicitly pinned as "always available". [More info about Storage policies](/windows/client-management/mdm/policy-csp-storage)

## Silent account configuration

- **Silently configure user accounts on PCs**. When you enable the silent account configuration policy, users are signed in automatically; so, they don't need to open OneDrive or enter their password. For more information, see [Use silent account configuration](use-silent-account-configuration.md).

## Known Folder Move

Windows users are familiar and comfortable with saving files to their Desktop, Documents, and Pictures folders from years of developing it as a habit. When you redirect and move these folders to OneDrive, users can continue saving files to these locations, and they're backed up and available from any device. For more information, see [Redirect known folders](redirect-known-folders.md).

- **On new PCs, enable the silent policy**. [Silently move Windows known folders to OneDrive](use-group-policy.md#silently-move-windows-known-folders-to-onedrive)
- **On existing PCs, gradually enable the prompt and/or silent policy**. [About the Known Folder Move Group Policy objects](redirect-known-folders.md#about-the-known-folder-move-policies)

## Office integration

- **Keep Office file collaboration enabled** Office uses differential sync to sync only changes instead of the entire file each time. This makes sync faster and reduces network bandwidth. This setting is on by default on Windows and Mac. For more info, see [Coauthor and share in Office desktop apps](use-group-policy.md#coauthor-and-share-in-office-desktop-apps). For info about this setting for Mac, see [Deploy and configure the new OneDrive sync app for Mac](deploy-and-configure-on-macos.md).

## Offline mode

- **Keep offline mode enabled** With offline mode, users can work with OneDrive in the web in low or no internet situations. This setting is on by default on Windows and Mac. For more info, see [Prevent users from getting silently signed in to offline experiences on the web](lists-sync-policies.md#prevent-users-from-getting-silently-signed-in-to-offline-experiences-on-the-web), [Prevent users at your organization from enabling offline mode in OneDrive on the web](#prevent-users-at-your-organization-from-enabling-offline-mode-in-onedrive-on-the-web), and [Prevent users at your organization from enabling offline mode in OneDrive on the web for libraries and folders that are shared from other organizations](#prevent-users-at-your-organization-from-enabling-offline-mode-in-onedrive-on-the-web-for-libraries-and-folders-that-are-shared-from-other-organizations). For info about this setting for Mac, see [DisableOfflineMode](deploy-and-configure-on-macos#disableofflinemode) and [DisableOfflineModeForExternalLibraries](deploy-and-configure-on-macos#disableofflinemodeforexternallibraries).
