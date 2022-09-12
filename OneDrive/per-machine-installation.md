---
title: Install the sync app per-machine (Windows)
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
description: In this article, you'll learn how to install the OneDrive sync app once for a Windows PC with multiple users.
---

# Install the sync app per-machine

By default, the OneDrive sync app installs per-user, meaning that you'll need to install the app for each user on a machine. With the per-machine installation option, you'll only need to install the app once on a PC. This option is especially useful for computers with multiple users and for when you don't want executable files running from a user profile.

Other than where the sync app is installed, the behavior is the same.

**Updates**

The OneDrive sync app with the installation option of either per-machine or per-user both use the [same release notes](https://support.office.com/article/845dcf18-f921-435e-bf28-4e24b95e5fc0), support the same update rings, and update in the same time-frame. [More info about the sync app update process](sync-client-update-process.md).

If you're moving from per-user to per-machine, update settings aren't affected.

## Requirements

The per-machine installation's system requirements will be the same as the per-user installation.

The per-machine installation option supports syncing OneDrive and SharePoint files in Microsoft 365 and in SharePoint Server 2019.

The  per-machine installation option provides automatic transitioning from the [previous OneDrive for Business sync app (Groove.exe)](transition-from-previous-sync-client.md).

## Deployment instructions

1. Download OneDriveSetup.exe.
2. Run "OneDriveSetup.exe /allusers" from a command prompt window (this will result in a User Account Control prompt) or by using Microsoft Endpoint Configuration Manager.

While the per-user option installs OneDrive for each user account on a PC under the %localappdata% folder, the per-machine option will install OneDrive under the "Program Files (x86)" or "Program Files" directory (depending on the OS architecture).

When setup completes, OneDrive will start. If accounts were added on the computer, they'll be migrated automatically.

## Verify per-machine installation

To verify that you have the per-machine installation, you can use the following registry detection rule in Configuration Manager:

|Field|Value|
|---|---|
|Hive|HKEY_LOCAL_MACHINE|
|Key|SOFTWARE\Microsoft\OneDrive|
|Name|Version|
|32bit on 64bit| TRUE|
|Type|REG_SZ|
|Value|19.043.0304.0007|

## Revert back to the per-user sync app

We don't support automated migration from per-machine to per-user. To revert back after installing per-machine, uninstall the sync app and [install the latest released version](https://go.microsoft.com/fwlink/?linkid=844652) without the "/allusers" parameter.
