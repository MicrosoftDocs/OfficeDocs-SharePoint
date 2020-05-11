---
title: "Recommended sync app configuration"
ms.reviewer: kaarins
ms.author: kaarins
author: jackwi-alt
manager: pamgreen
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: conceptual
ms.service: one-drive
localization_priority: Normal
ms.collection: 
- Strat_OD_admin
- M365-collaboration
ms.custom:
- seo-marvel-apr2020
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

For the best performance, reliability, and user experience, follow these "ideal state" recommendations when you configure the sync app.

## Updates and rings

- **Allow access to oneclient.sfx.ms and g.live.com**. Devices must be able to reach these URLs to apply updates. Updates are installed automatically, so you don't need to package and deploy them. Because OneDrive runs in the background, updates are also installed silently and don't impact users. 
- **Use the Insiders and Production rings**. Select several people in your IT department as early adopters to join the Insiders ring and receive features early. Leave everyone else in the organization on the default Production ring to ensure they receive bug fixes and new features in a timely fashion. This recommendation applies even if you are on the Semi-Annual Channel for Windows and Office. For more info, see [Sync app update process](sync-client-update-process.md).

## Windows Notification Service
  
- **Allow traffic to \*.wns.windows.com**. The OneDrive sync app uses Windows Push Notification Services (WNS) for optimum performance and battery life. [See the complete list of required URL and IP address ranges](/office365/enterprise/urls-and-ip-address-ranges#sharepoint-online-and-onedrive-for-business).

## Files On-Demand and Storage Sense

- **Keep Files On-Demand enabled**. OneDrive Files On-Demand helps users access all their files (individual or shared) without having to download them and use storage space. This setting is on by default for Windows and Mac. 
- **Use Storage Sense policies on PCs**. These policies let you automatically clean up "locally available" files users haven't explicitly pinned as "always available". [More info about Storage policies](/windows/client-management/mdm/policy-csp-storage)

 
## Office integration

- **Keep Office file collaboration enabled** Office uses differential sync to sync only changes instead of the entire file each time. This makes sync faster and reduces network bandwidth. This setting is on by default on Windows and Mac. For more info, see [Coauthor and share in Office desktop apps](use-group-policy.md#coauthor-and-share-in-office-desktop-apps).

## Silent account configuration

- **Silently configure user accounts on PCs**. When you enable the silent account configuration policy, users are signed in automatically so they don't need to open OneDrive or enter their password. For more info, see [Use silent account configuration](use-silent-account-configuration.md).

## Known Folder Move

Windows users are familiar and comfortable with saving files to their Desktop, Documents, and Pictures folders from years of developing it as a habit. When you redirect and move these folders to OneDrive, users can continue saving files to these locations and they're backed up and available from any device. For more info, see [Redirect known folders](redirect-known-folders.md).

- **On new PCs, enable the silent policy**. [Silently move Windows known folders to OneDrive](use-group-policy.md#silently-move-windows-known-folders-to-onedrive)
- **On existing PCs, gradually enable the prompt and/or silent policy**. [About the Known Folder Move Group Policy objects](use-group-policy.md#about-the-known-folder-move-group-policy-objects)



