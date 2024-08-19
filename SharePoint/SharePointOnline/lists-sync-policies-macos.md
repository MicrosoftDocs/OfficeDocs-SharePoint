---
ms.date: 03/03/2023
title: "Configure lists sync on Mac"
ms.author: ruihu
author: maggierui
manager: jtremper
audience: Admin
f1.keywords:
ms.topic: article
ms.service: sharepoint-online
ms.localizationpriority: high
search.appverid:
ms.collection: 
- M365-collaboration
description: "Learn how to configure lists sync on Mac by using Group Policy objects (GPOs)."
---

# Use macOS preferences to control Lists sync settings

This article describes macOS preferences for Microsoft Lists (and SharePoint lists). For info about controlling OneDrive sync settings on macOS, see [Deploy and configure OneDrive on macOS](/sharepoint/deploy-and-configure-on-macos).

## Manage Lists sync settings on macOS using property list files

Lists sync gets packaged, installed, and updated through the OneDrive sync standalone (non-App Store) app's existing update mechanism. As a result, some Lists sync preferences are listed under the OneDrive group domain. After the OneDrive sync app for Mac is installed, users can configure settings for Lists sync. As an administrator, you might want to provide users in your organization with a standard set of preferences. Preferences for the Lists sync app for Mac are stored in property list `.plist` files.
  
|| Lists sync preferences | OneDrive group preferences |
|:-----|:-----|:-----|
|**.plist location**  |~/Library/Preferences/com.microsoft.SharePoint-mac.plist  |~/Library/Group Containers/UBF8T346G9.OneDriveStandaloneSuite/Library/Preferences/UBF8T346G9.OneDriveStandaloneSuite.plist  |

## List of policies by string ID

- `DisableNucleusSync` - [Prevent Lists sync from running on the device](lists-sync-policies-macos.md#prevent-lists-sync-from-running-on-the-device)

- `BlockExternalListSync` - [Prevent users from syncing lists shared from other organizations](lists-sync-policies-macos.md#prevent-users-from-syncing-lists-shared-from-other-organizations)

- `DisableNucleusSilentConfig` - [Prevent users from getting silently signed in to Lists sync with existing Microsoft account credentials being used across Microsoft apps on macOS](lists-sync-policies-macos.md#prevent-users-from-getting-silently-signed-in-to-lists-sync-with-existing-microsoft-account-credentials-being-used-across-microsoft-apps-on-macos)

### Prevent Lists sync from running on the device

By default, Lists sync is turned on for users of Microsoft Lists. If you set this preference, Lists sync will be blocked from running on the device.

**Location**: [Lists Sync preferences](lists-sync-policies-macos.md#manage-lists-sync-settings-on-macos-using-property-list-files)

Prevent Lists sync from running on the device:

```xml
<key>DisableNucleusSync</key>
<integer>1</integer>
```

Re-enable Lists sync on the device:

```xml
<key>DisableNucleusSync</key>
<integer>0</integer>
```

### Prevent users from syncing lists shared from other organizations

Enabling this setting prevents users at your organization from syncing lists that are shared from other organizations. After the setting is enabled (value 1) on a computer, lists shared from other organizations won't sync. Disable the setting (value 0) to allow your users to sync external lists.

**Location**: [Lists Sync preferences](lists-sync-policies-macos.md#manage-lists-sync-settings-on-macos-using-property-list-files)

Prevent external List sync with:

```xml
<key>BlockExternalListSync</key>
<integer>1</integer>
```

Restore external List sync with:

```xml
<key>BlockExternalListSync</key>
<integer>0</integer>
```

### Prevent users from getting silently signed in to Lists sync with existing Microsoft account credentials being used across Microsoft apps on macOS

Lists sync is set up to automatically sign users in with credentials being used across other Microsoft apps on macOS like OneDrive. If you enable this setting, automatic sign-in and Lists sync setup wouldn't occur.

**Location**: [OneDrive group preferences](lists-sync-policies-macos.md#manage-lists-sync-settings-on-macos-using-property-list-files)

Prevent Lists sync silent configuration:

```xml
<key>DisableNucleusSilentConfig</key>
<integer>1</integer>
```

Restore Lists sync silent configuration with:

```xml
<key>DisableNucleusSilentConfig</key>
<integer>0</integer>
```
