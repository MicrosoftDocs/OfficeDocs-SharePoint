---
ms.date: 07/02/2021
title: "Lists sync policies"
ms.reviewer: andreye
ms.author: matteva
author: MattEEvans
manager: pamgreen
recommendations: true
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.localizationpriority: high
search.appverid:
- SPO160
- MET150
ms.collection:  
- M365-collaboration
description: "Learn how to control Lists sync by using Group Policy objects (GPOs)."
---
# Use Group Policy to control Lists sync settings

This article describes the Group Policy objects (GPOs) for Microsoft Lists (and SharePoint lists) that admins can configure by using Group Policy. Use the registry key info to confirm that a setting is enabled. Lists sync policies are listed under OneDrive because Lists sync gets packaged, installed, and updated through the OneDrive sync app's existing update mechanism. For info about controlling OneDrive sync settings by Group Policy, see [OneDrive policies](/onedrive/use-group-policy).

## List of policies by string ID

- (DisableListsSync) [Prevent Lists sync from running on this device](lists-sync-policies.md#prevent-lists-sync-from-running-on-this-device)

- (BlockExternalListSync) [Prevent users from syncing lists shared from other organizations](lists-sync-policies.md#prevent-users-from-syncing-lists-shared-from-other-organizations)

- (DisableNucleusSilentConfig) [Prevent users from getting silently signed in to offline experiences on the web](#prevent-users-from-getting-silently-signed-in-to-offline-experiences-on-the-web)

### Prevent Lists sync from running on this device

By default, Lists sync is turned on for users of Microsoft Lists which allows users to access and edit their lists even when offline. If you enable this policy, Lists sync will be blocked from running on the device.

Prevent Lists sync from running on the device:

`[HKLM\SOFTWARE\Policies\Microsoft\OneDrive] "DisableNucleusSync" = "dword:1"`

Re-enable Lists sync on the device:

`[HKLM\SOFTWARE\Policies\Microsoft\OneDrive] "DisableNucleusSync" = "dword:0"`

### Prevent users from syncing lists shared from other organizations

Enabling this setting prevents users at your organization from syncing lists that are shared from other organizations. After the setting is enabled (by entering value **1**) on a computer, lists shared from other organizations won't sync. Disable the setting (by entering value **0**) to allow your users to sync external lists.

Prevent external List sync with:

`[HKLM\SOFTWARE\Policies\Microsoft\OneDrive] "BlockExternalListSync" = "dword:1`

Restore external List sync with:

`[HKLM\SOFTWARE\Policies\Microsoft\OneDrive] "BlockExternalListSync" = "dword:0"`

### Prevent users from getting silently signed in to offline experiences on the web

Offline experiences in Microsoft Lists and OneDrive on the web are set up to automatically sign in users with their Microsoft Entra account credentials. If you enable this setting, people who used offline experiences in Microsoft Lists and OneDrive on the web previously and who are signed in on an Microsoft Entra-joined PC will no longer be able to set up offline experiences without entering their account credentials.  

> [!IMPORTANT]
> If the M365 browser extension isn't installed on users' Chromium-based browsers (Microsoft Edge, Google Chrome, and so on), we recommend leaving silent account configuration enabled to ensure the seamless operation of List sync.

Enabling this policy sets the following registry key value to 1:

`[HKLM\SOFTWARE\Policies\Microsoft\OneDrive] "DisableNucleusSilentConfig" = "dword:00000001"`

For more info about this feature, including troubleshooting steps, see [Silently configure user accounts](/onedrive/use-silent-account-configuration).

## Control Lists sync on unmanaged devices and based on location  

You can use the following settings to control access to Lists sync from unmanaged devices and configure network location-based access to List sync.

[Control access from unmanaged devices](control-access-from-unmanaged-devices.md)

[Control access to SharePoint and OneDrive based on network location](control-access-based-on-network-location.md)
