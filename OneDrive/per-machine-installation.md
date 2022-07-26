---
title: "Install the sync app per machine"
ms.reviewer: gacarini
ms.author: mabond
author: mkbond007
manager: serdars
audience: Admin
f1.keywords:
- CSH
ms.topic: article
ms.service: one-drive
ms.localizationpriority: medium
ms.custom:
- Adm_O365
- seo-marvel-apr2020
- onedrive-toc
search.appverid:
- MET150
- BCS160
ms.collection:
- Strat_OD_admin
- M365-collaboration
ms.assetid: 6891b561-a52d-4ade-9f39-b492285e2c9b
description: "In this article, you'll learn how to install the OneDrive sync app for every user account on a Windows PC."
---

# Install the sync app per machine

By default, the OneDrive sync app installs per user, meaning OneDrive.exe needs to be installed for each user account on the PC under the %localappdata% folder. With the new per-machine installation option, you can install OneDrive under the "Program Files (x86)"  or "Program Files" directory (depending on the OS architecture), meaning all profiles on the computer will use the same OneDrive.exe binary. Although a single version of OneDrive.exe is installed, a new process is created for every OneDrive account syncing on the computer. Other than where the sync app is installed, the behavior is the same.

The new per-machine sync app provides:

- Automatic transitioning from the previous OneDrive for Business sync app (Groove.exe)
- Automatic conversion from per-user to per-machine
- Automatic updates when a new version is available

The per-machine sync app is helpful especially for multi-user computers and when you don't want .exe files running from the user profile. Gradually, we recommended more customers switch to per-machine installation.

The per-machine sync app supports syncing OneDrive and SharePoint files in Microsoft 365 and in SharePoint Server 2019.

## Requirements

- All Windows versions supported by the sync app. [Learn more](https://support.office.com/article/cc0cb2b8-f446-445c-9b52-d3c2627d681e).
- Sync app builds 19.174.0902.0013 or later. For info about which sync app build is available in each ring, see [OneDrive sync app release notes](https://support.office.com/article/845dcf18-f921-435e-bf28-4e24b95e5fc0).
- To apply sync app updates, computers in your organization must allow the following URLs: "oneclient.sfx.ms" and "g.live.com". Make sure you don't block these URLs, as they're also used to enable and disable features and apply bug fixes. [More info about the URLs and IP address ranges used in Microsoft 365](/office365/enterprise/urls-and-ip-address-ranges).

## Deployment instructions

1. Download OneDriveSetup.exe.
2. Run "OneDriveSetup.exe /allusers" from a command prompt window (this will result in a User Account Control prompt) or by using Microsoft Endpoint Configuration Manager. This will install the sync app under the "Program Files (x86)\Microsoft OneDrive" directory or "Program Files\Microsoft OneDrive" directory (depending on the OS architecture).

When setup completes, OneDrive will start. If accounts were added on the computer, they'll be migrated automatically.

## Verify per-machine installation

To verify that you have the per-machine installation, you can use the following registry detection rule in Configuration Manager:

|Field|Value|
|---|---|
|Hive|HKEY_LOCAL_MACHINE|
|Key|SOFTWARE\Microsoft\OneDrive|
|Value|Version|
|32bit on 64bit| TRUE|
|Type|REG_SZ|
|Value|19.043.0304.0007|

## Updates

We recommend that you keep your users in the default Production ring and rely on automatic updates to keep them on the latest version in order to maintain a high-quality sync experience.

The per-machine sync app will automatically update on the same cadence as the per-user sync app and the same rings are supported. The [release notes](https://support.office.com/article/845dcf18-f921-435e-bf28-4e24b95e5fc0) are also the same. [More info about the sync app update process](sync-client-update-process.md)

If your organization requires you to deploy updates manually through Configuration Manager, we recommend that you select the Deferred (also known as "Enterprise") ring, and deploy the upcoming builds *before* automatic updates takes effect as described here.

### User intervention

Elevation is required when you first set up the OneDrive sync app. During setup, we install a scheduled task and a Windows service, which are used to perform the updates silently without user intervention since they run in elevated mode.

User intervention isn't required for the per-machine sync app automatic updates.

## Ring selection

To select the ring, use the group policy ([Set the sync app update ring](use-group-policy.md#set-the-sync-app-update-ring)).

If you selected the Insiders ring (via the [Windows Insider program](https://insider.windows.com/) or [Office Insider](https://products.office.com/office-insider) programs) or are in the default Production ring, you are in the same ring as before.

## Revert back to the per-user sync app

We don't support automated migration from per-machine to per-user. To revert back after installing per-machine, uninstall the sync app and [install the latest released version](https://go.microsoft.com/fwlink/?linkid=844652) without the "/allusers" parameter.
