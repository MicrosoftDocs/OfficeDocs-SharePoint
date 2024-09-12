---
ms.date: 09/09/2024
title: "Deploy and configure the OneDrive sync app for Mac"
ms.reviewer: cagreen
ms.author: mactra
author: MachelleTranMSFT
manager: jtremper
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: one-drive
ms.localizationpriority: medium
ms.collection: 
- Strat_OD_admin
- M365-collaboration
- onedrive-toc
search.appverid:
- ODB160
- ODB150
- MET150
ms.assetid: eadddc4e-edc0-4982-9f50-2aef5038c307
description: "Learn how to change settings when deploying or managing the OneDrive sync app on macOS."
---

# Deploy and configure the OneDrive sync app for Mac

> [!IMPORTANT]
> The standalone OneDrive sync app is necessary for deploying and configuring Folder Backup settings. The Mac App Store OneDrive sync app is not currently supported with regards to Folder Backup.

There are two basic ways that you, as an administrator, can deploy the OneDrive sync app to Mac users in your organization:
  
- Install and set up the OneDrive sync app by following the instructions in [Sync files with OneDrive on macOS](https://support.office.com/article/d11b9f29-00bb-4172-be39-997da46f913f). To install the OneDrive sync app for Mac, a user has to be an administrator on the Mac.

- Download the installer package file to your local network, and then use your software distribution tools to deploy the app to your users. By using a software distribution tool, you have more control over the deployment, including which users get the sync app and when. The OneDrive sync app for Mac uses the Apple Installer technology for installation allowing you to use the software distribution tools that you normally use to deploy software to Mac users. You can use [Microsoft Intune](/mem/intune/apps/apps-add-office365-macOS). Other common tools are [Jamf Pro](https://www.jamf.com/products/jamf-pro/), [Munki](https://www.munki.org/), and [AutoPkg](https://github.com/autopkg/autopkg). You can also use [Apple Remote Desktop](https://www.apple.com/remotedesktop/) and [AppleScript](https://developer.apple.com/library/mac/documentation/AppleScript/Conceptual/AppleScriptX/AppleScriptX.html).
  
## Manage OneDrive settings on macOS using property list (.plist) files

After the OneDrive sync app for Mac is installed, users can configure settings for the app. These settings are called preferences. As an administrator, you might want to provide users in your organization with a standard set of preferences. Preferences for the OneDrive sync app for Mac are stored in property list (.plist) files.

|| Standalone | Mac App Store |
|:-----|:-----|:-----|
|**.plist location**  |/Library/Preferences/com.microsoft.OneDrive.plist  |/Library/Containers/com.microsoft.OneDrive-mac/Data/Library/Preferences/com.microsoft.OneDrive-mac.plist  |
|**Domain**  |com.microsoft.OneDrive  |com.microsoft.OneDrive-mac  |
  
## Configure sync app settings

Configure the settings on macOS as follows:
  
1. Define the settings you want to change by creating a .plist file with the values needed. You can use a script to set the values.

1. Quit the OneDrive app.

1. Deploy the settings onto the local computer.

1. Refresh the preferences cache.

On the next start of OneDrive, the new settings will be picked up.

## Background services

> [!IMPORTANT]
> macOS 13 (Ventura) contains new privacy enhancements. Beginning with this version, by default, applications cannot run in background without explicit consent. OneDrive must run its daemon process in background. This configuration profile grants Background Service permissions to OneDrive. If you previously configured OneDrive through Microsoft Intune, we recommend you update the deployment with this configuration profile.

You need to create system configuration profiles that OneDrive needs to open at sign-in and run reliably in the background. Here's an example:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1">
<dict>
<key>PayloadUUID</key>
<string>9FE052B5-E7B6-4BF9-94EB-DB611E0E323E</string>
<key>PayloadType</key>
<string>Configuration</string>
<key>PayloadOrganization</key>
<string>Microsoft Corporation</string>
<key>PayloadIdentifier</key>
<string>9FE052B5-E7B6-4BF9-94EB-DB611E0E323E</string>
<key>PayloadDisplayName</key>
<string>OneDrive - Background Services</string>
<key>PayloadDescription</key>
<string/>
<key>PayloadVersion</key>
<integer>1</integer>
<key>PayloadEnabled</key>
<true/>
<key>PayloadRemovalDisallowed</key>
<true/>
<key>PayloadScope</key>
<string>System</string>
<key>PayloadContent</key>
<array>
<dict>
<key>PayloadDescription</key>
<string>Background Service Management for OneDrive</string>
<key>PayloadIdentifier</key>
<string>4C3F2438-464E-43F5-8961-D4672D4A9F5D.privacy.C7B71805-73F2-43F6-A5AA-29C9CAD728B4</string>
<key>PayloadUUID</key>
<string>F9EE3920-EAD8-4472-AF2F-52D2B57FDB31</string>
<key>Rules</key>
<array>
<dict>
<key>RuleType</key>
<string>LabelPrefix</string>
<key>RuleValue</key>
<string>com.microsoft.OneDrive</string><!--This would be com.microsoft.OneDrive-mac for the Store app-->
</dict>
<dict>
<key>RuleType</key>
<string>BundleIdentifierPrefix</string>
<key>RuleValue</key>
<string>com.microsoft.OneDriveLauncher</string>
</dict>
</array>
<key>PayloadType</key>
<string>com.apple.servicemanagement</string>
<key>PayloadDisplayName</key>
<string>Background Service Management for OneDrive</string>
</dict>
</array>
</dict>
</plist>
```

## Overview of settings

Use the following keys to preconfigure or change settings for your users. The keys are the same whether you run the standalone or Mac App Store edition of the sync app. However, the .plist file name and domain name are different. When you apply the settings, ensure that you target the appropriate domain depending on the edition of the sync app.

## List of settings

- [AddedFolderHardDeleteOnUnmount](deploy-and-configure-on-macos.md#addedfolderharddeleteonunmount)
- [AddedFolderUnmountOnPermissionsLoss](deploy-and-configure-on-macos.md#addedfolderunmountonpermissionsloss)
- [AllowTenantList](deploy-and-configure-on-macos.md#allowtenantlist)
- [AutomaticUploadBandwidthPercentage](deploy-and-configure-on-macos.md#automaticuploadbandwidthpercentage)
- [BlockExternalSync](deploy-and-configure-on-macos.md#blockexternalsync)
- [BlockTenantList](deploy-and-configure-on-macos.md#blocktenantlist)
- [DefaultFolderLocation](deploy-and-configure-on-macos.md#defaultfolderlocation)
- [DisableAutoConfig](deploy-and-configure-on-macos.md#disableautoconfig)
- [DisableFirstDeleteDialog](deploy-and-configure-on-macos.md#disablefirstdeletedialog)
- [DisableCustomRoot](deploy-and-configure-on-macos.md#disablecustomroot)
- [DisableFirstDeleteDialog](deploy-and-configure-on-macos.md#disablefirstdeletedialog)
- [DisableFREAnimation](deploy-and-configure-on-macos.md#disablefreanimation)
- [DisableOfflineMode](#disableofflinemode)
- [DisableOfflineModeForExternalLibraries](#disableofflinemodeforexternallibraries)
- [DisablePersonalSync](deploy-and-configure-on-macos.md#disablepersonalsync)
- [DisableTutorial](deploy-and-configure-on-macos.md#disabletutorial)
- [DownloadBandwidthLimited](deploy-and-configure-on-macos.md#downloadbandwidthlimited)
- [EnableODIgnore](deploy-and-configure-on-macos.md#enableodignore)
- [EnableSyncAdminReports](deploy-and-configure-on-macos.md#enablesyncadminreports)
- [HideDockIcon](deploy-and-configure-on-macos.md#hidedockicon)
- [HydrationDisallowedApps](deploy-and-configure-on-macos.md#hydrationdisallowedapps)
- [KFMBlockOptIn](deploy-and-configure-on-macos.md#kfmblockoptin)
- [KFMBlockOptOut](deploy-and-configure-on-macos.md#kfmblockoptout)
- [KFMOptInWithWizard](deploy-and-configure-on-macos.md#kfmoptinwithwizard)
- [KFMSilentOptIn](deploy-and-configure-on-macos.md#kfmsilentoptin)
- [OpenAtLogin](deploy-and-configure-on-macos.md#openatlogin)
- [SharePointOnPremFrontDoorUrl](deploy-and-configure-on-macos.md#sharepointonpremfrontdoorurl)
- [SharePointOnPremPrioritizationPolicy](deploy-and-configure-on-macos.md#sharepointonpremprioritizationpolicy)
- [SharePointOnPremTenantName](deploy-and-configure-on-macos.md#sharepointonpremtenantname)
- [Tier](deploy-and-configure-on-macos.md#tier)
- [UploadBandwidthLimited](deploy-and-configure-on-macos.md#uploadbandwidthlimited)

### AddedFolderHardDeleteOnUnmount

This setting will control the contents of the folder when an unmount of an Added Folder is detected.

Set the setting's value to **True**, to hard-delete all the contents of the folder when an unmount of an Added Folder is received. Set the value to **False** or don't enable the setting to move the contents of the unmounted folder to the recycle-bin by default.

The example for this setting in the .plist file is:

```xml
<key>AddedFolderHardDeleteOnUnmount</key>
<(Bool)/>
```

### AddedFolderUnmountOnPermissionsLoss

This setting will control the contents of the folder and the folder itself when the Sync client detects that the user lost permissions to an Added Folder.

Set the setting's value to **True**, to hard-delete all the contents of the folder and the folder itself when the Sync client detects that the user lost permissions to an Added Folder. Set the value to **False** or don't enable the setting to efault mark the folder in error and prompt the user to remove it. When the user confirms the removals, the contents of the folder are moved to the recycle-bin.

The example for this setting in the .plist file is:

```xml
<key>AddedFolderUnmountOnPermissionsLoss</key>
<(Bool)/>
```

### AllowTenantList

This setting prevents the users from uploading files to other organizations by specifying a list of allowed tenant IDs. If you enable this setting, the user gets an error if they attempt to add an account from an organization that isn't in the allowed tenants list. If the user is already added the account, the files stop syncing. This setting takes priority over the **BlockTenantList** setting. Do **NOT** enable both settings at the same time.

The parameter for the **AllowTenantList** key is **TenantID** and its value is a string, which determines the tenants for whom the **Allow Tenant** setting is applicable. For the setting to be complete, this parameter also requires a boolean value to be set to it. If the boolean value is set to **True**, the tenant is allowed to sync.

The example for this setting in the .plist file is:

```xml
<key>AllowTenantList</key>
<dict>
<key>TenantId1</key>
<true/>
<key>TenantId2</key>
<true/>
</dict>
```
  
### AutomaticUploadBandwidthPercentage

This setting enables the sync app to automatically set the amount of bandwidth that can be used for uploading files, based on available bandwidth.

To enable this setting, you must define a number between 1 and 99 that determines the percentage of bandwidth the sync app can use out of the total available bandwidth.

The example for this setting in the .plist file is:

```xml
<key>AutomaticUploadBandwidthPercentage</key>
<integer>(Bandwidth)</integer>
```

### BlockExternalSync

This setting prevents the sync app from syncing libraries and folders shared from other organizations.

Set the setting's value to **True**, to prevent the users from syncing OneDrive, SharePoint libraries, and folders with organizations other than the user's own organization. Set the value to **False** or don't enable the setting to allow the OneDrive, and SharePoint files to be synced with other organizations also.

The example for this setting in the .plist file is:

```xml
<key>BlockExternalSync</key>
<(Bool)/>
```

### BlockTenantList

This setting prevents the users from uploading files to organizations that are included in the **blocked tenant IDs** list.

If you enable this setting, the users get an error if they attempt to add an account from an organization that is blocked. If a user is already added an account for a blocked organization, the files stop syncing. This setting does **NOT** work if you have the **AllowTenantList** setting enabled. Do **NOT** enable both settings at the same time.

Enable this setting by defining IDs for the **TenantID** parameter, which determines the tenants to whom the **block tenant** setting is applicable. Also set the boolean value to **True** for the ID of every tenant you want to prevent from syncing with the OneDrive and SharePoint files and folders.

> [!NOTE]
> In the list, inclusion of the tenant ID alone doesn't suffice. It's mandatory to set the boolean value to **True**  for the ID of each tenant who is to be blocked.

The example for this setting in the .plist file is:

```xml
<key>BlockTenantList</key>
<dict>
<key>TenantId1</key>
<true/>
<key>TenantId2</key>
<true/>
</dict>
```

### DefaultFolderLocation

This setting specifies the default location of the OneDrive folder for each organization.

The parameters are **TenantID** and **DefaultFolderPath**.
The **TenantID** value is a string that determines the tenants to whom the **default folder location** setting is applicable.
The **DefaultFolderPath** value is a string that specifies the default location of the folder. If you want to enforce the location to be the home directory of the user (that is, the default location), you can specify the path as ~/. The string would look like this:

`
<string>~/</string>
`

The following are the conditions governing the default folder location:
-**Mac App Store**: The path must already exist when the user is setting up the sync app.
-**Standalone**: The path will be created (if it doesn't already exist) after the user sets up the sync app. Only with the Standalone sync app you can prevent users from changing the location.

The example for this setting in the .plist file is:

```xml
<key>DefaultFolder</key>
<dict>
<key>Path</key>
<string>(DefaultFolderPath)</string>
<key>TenantId</key>
<string>(TenantID)</string>
</dict>
```

### DisableAutoConfig

This setting determines whether or not the sync app can automatically sign in.

If you set this setting's value to 1, the sync app is prevented from automatically signing with an existing Microsoft Entra credential that is made available to Microsoft applications.

The example for this setting in the .plist file is:

```xml
<key>DisableAutoConfig</key>
<integer>1</integer>
```

### DisableCustomRoot

This setting lets you block users from changing the location of the OneDrive folder on their computer.

If you set this setting's value to **True**, the Change location link is hidden in OneDrive Setup. The OneDrive folder is created in the default location, or in the custom location you specified if you enabled [DefaultFolderLocation](deploy-and-configure-on-macos.md#defaultfolderlocation).

The example for this setting in the .plist file is:

```xml
<key>DisableCustomRoot</key>
<(Bool)/>
```

### DisableFirstDeleteDialog

When a user deletes local files from a synced location, a warning message appears that the files are no longer available across all the devices of the user and on the web. This setting lets you hide the warning message.

If you set the setting's value to 1, users don't see the Deleted files are removed everywhere reminder when they delete files locally. (This reminder is called "Deleted files are removed for everyone" when a user deletes files from a synced team site.)

The example for this setting in the .plist file is:

```xml
<key>DisableFirstDeleteDialog</key>
<integer>1</integer>
```

### DisableFREAnimation

If you set the setting's value to 1, users don't see the Deleted files are removed everywhere reminder when they delete files locally. (This reminder is called "Deleted files are removed for everyone" when a user deletes files from a synced team site.)
This setting lets you prevent the animation from showing during OneDrive Setup.

If you set the setting's value to 1, animations will not be shown during OneDrive Setup.

The example for this setting in the .plist file is:

```xml
<key>DisableFREAnimation</key>
<integer>1</integer
```

### DisableOfflineMode

This setting prevents users from enabling offline mode in OneDrive on the web.

The preferences for this setting are stored in the following .plist files.

|  |Offline mode preferences location  |OneDrive group preferences  |
|---------|---------|---------|
|**.plist location**  | ~/Library/Preferences/com.microsoft.SharePoint-mac.plist        | ~/Library/Group Containers/UBF8T346G9.OneDriveStandaloneSuite/Library/Preferences/UBF8T346G9.OneDriveStandaloneSuite.plist        |

By default, offline mode is turned on for users of OneDrive on the web.

To prevent users at your organization from enabling offline mode in OneDrive on the web, use the following example:

```xml
<key>DisableOfflineMode</key>
<integer>1</integer>
```

To re-enable offline mode in OneDrive on the web for users, use the following example:

```xml
<key>DisableOfflineMode</key>
<integer>0</integer>
```

### DisableOfflineModeForExternalLibraries

This setting prevents users from enabling offline mode in OneDrive on the web for libraries and folders that are shared from other organizations.

The preferences for this setting are stored in the following .plist files:

|  |Offline mode preferences location  |OneDrive group preferences  |
|---------|---------|---------|
|**.plist location**|~/Library/Preferences/com.microsoft.SharePoint-mac.plist       | ~/Library/Group Containers/UBF8T346G9.OneDriveStandaloneSuite/Library/Preferences/UBF8T346G9.OneDriveStandaloneSuite.plist        |

To prevent users at your organization from enabling offline mode in OneDrive on the web for libraries and folders that are shared from other organizations, use the following example:

```xml
<key>DisableOfflineModeForExternalLibraries</key>
<integer>1</integer>
```

To re-enable offline mode in OneDrive on the web for libraries and folders that are shared from other organizations, use the following example:

```xml
<key>DisableOfflineModeForExternalLibraries </key>
<integer>0</integer>
```

### DisablePersonalSync

This setting blocks users from signing in and syncing files in personal OneDrive accounts. If this setting is configured after a user sets up sync with a personal account, the user gets signed out.

If you set the setting's value to **True**, users are prevented from adding or syncing personal accounts.

The example for this setting in the .plist file is:

```xml
<key>DisablePersonalSync</key>
<(Bool)/>
```

### DisableTutorial

This setting prevents the tutorial from being shown to the users after they set up OneDrive.

If you set this setting's value to **True**, the tutorial is blocked from being shown to the users after they set up the OneDrive sync app.

The example for this setting in the .plist file is:

```xml
<key>DisableTutorial</key>
<(Bool)/>
```

### DownloadBandwidthLimited

This setting sets the maximum download throughput rate in kilobytes (KB)/sec for computers running the OneDrive sync app.

Set this setting's value to an integer between 50 and 100000 to specify the download throughput in KB/sec that the sync app can use.

The example for this setting in the .plist file is:

```xml
<key>DownloadBandwidthLimited</key>
<integer>(Download Throughput Rate in KB/sec)</integer>
```

### EnableODIgnore

This setting lets you enter keywords to prevent the OneDrive sync app from uploading certain files to OneDrive or SharePoint. You can enter complete names, such as "setup.exe" or use the asterisk (*) as a wildcard character to represent a series of characters, such as*.pst. Keywords aren't case-sensitive.

If you enable this setting, the sync app doesn't upload new files that match the keywords you specified. No errors appear for the skipped files, and the files remain in the local OneDrive folder. In Finder, the files appear with an "Excluded from sync" icon.

Users see a message in the OneDrive activity center that explains why the files aren't syncing.

The example for this setting in the .plist file is:

```xml
<key>EnableODIgnore</key>
<array>
<string>(Keyword such as *.PST)</string>
</array>
```

### EnableSyncAdminReports

This setting lets the OneDrive sync app report device and health data that's to be included in sync admin reports. You must enable this setting on the devices you want to get reports from. For more information about these reports, see [OneDrive sync reports in the Apps Admin Center](/sharepoint/sync-health?tabs=macos).

If you disable or don't configure this setting, OneDrive sync app device and health data don't appear in the sync admin reports.

The following example shows how this setting looks like in the .plist file:

```xml
<key>EnableSyncAdminReports</key>
<integer>1</integer>
```

> [!NOTE]
> We recommend keeping Files On-Demand enabled. [See all our recommendations for configuring the sync app](ideal-state-configuration.md)

### HideDockIcon

This setting specifies whether a dock icon for OneDrive is shown.

If you set this setting's value to **True**, the OneDrive dock icon is hidden even if the app is running.

The example for this setting in the .plist file is:

```xml
<key>HideDockIcon</key>
<(Bool)/>
```

### HydrationDisallowedApps

This setting prevents apps from automatically downloading online-only files. You can use this setting to lock down apps that don't work correctly with your deployment of Files On-Demand.

To enable this setting, you must define a string in JSON format:

`[{"ApplicationId":"appId","MaxBundleVersion":"1.1","MaxBuildVersion":"1.0"}]`

"appID" can be either the BSD process name or the bundle display name. "MaxBuildVersion" denotes the maximum build version of the app that can be blocked. "MaxBundleVersion" denotes the maximum bundle version of the app that can be blocked.

The example for this setting in the .plist file is:

```xml
<key>HydrationDisallowedApps</key>
<string>[{"ApplicationId":"appId","MaxBundleVersion":"1.1","MaxBuildVersion":"1.0"}, {"ApplicationId":"appId2","MaxBundleVersion":"3.2","MaxBuildVersion":"2.0"}]</string>
<(Bool)/>
```

### KFMBlockOptIn

This setting prevents users from moving their Documents and Desktop folders to any OneDrive account.
  
If you enable KFMBlockOptIn, users aren't prompted to protect their Desktop and Documents folders, and the *Manage backup* command is disabled. If the user previously moved their Desktop and Documents folders, the files in those folders remain in OneDrive. This setting doesn't take effect if you enabled **KFMOptInWithWizard**" or **KFMSilentOptIn**.

If you set this setting's value to 1, it prevents Folder Backup. If you set the value to 2, it will redirect any  folders previously used for Folder Backup back to the user’s device and stop the setting from running further.

The example for this setting in the .plist file is:

```xml
<key>KFMBlockOptIn</key>
<integer>(1 or 2)</integer>
```

### KFMBlockOptOut

This setting forces users to keep their Documents and Desktop folders directed to OneDrive.

If you enable this setting, the **Stop Backup** button in the **Manage Folder Backup** window is disabled, and users receive an error if they try to stop syncing their Desktop or Documents folder.
  
The example for this setting in the .plist file is:

```xml
<key>KFMBlockOptOut</key>
<(Bool)/>
```

### KFMOptInWithWizard

This setting displays a wizard that prompts users to move their Documents and Desktop folders to OneDrive.

If you enable this setting and provide your tenant ID, users who are syncing their OneDrive sees the Folder Backup wizard window when they're signed in. If they close the window, a reminder notification appears in the Sync Activity Center until they move their Desktop and Documents folders.
  
The example for this setting in the .plist file is:

```xml
<key>KFMOptInWithWizard</key>
<string>(TenantID)</string>
```

### KFMSilentOptIn

Use this setting to redirect and move your users' Documents and/or Desktop folders to OneDrive without any user interaction.
  
You can move both folders at once or select which folder you want to move. After a folder is moved, this setting won't affect that folder again.

The example for this setting in the .plist file is:

```xml
<key>KFMSilentOptIn</key>
<string>(TenantID)</string>
```

If you enable this setting and provide your tenant ID, you can choose whether to display a notification to users after their folders are redirected:

```xml
<key>KFMSilentOptInWithNotification</key>
<(Bool)/>
```

If you don't set any of the following settings, then the default setting moves both folders into OneDrive. If you want to specify which folder to move, you should set any combination of the following settings:

```xml
<key>KFMSilentOptInDesktop</key>
<(Bool)/>
<key>KFMSilentOptInDocuments</key>
<(Bool)/>
```

### OpenAtLogin

> [!IMPORTANT]
> The OpenAtLogin setting will be deprecated with Sync app 24.113. Please refer to [Background services](deploy-and-configure-on-macos.md#background-services) to configure the appropriate profile for enabling OneDrive to start automatically when the user logs in.

This setting specifies whether OneDrive starts automatically when the user logs in.

If you set this setting's value to **True**, OneDrive starts automatically when the user logs in to their Mac.

The example for this setting in the .plist file is:

```xml
<key>OpenAtLogin</key>
<(Bool)/>
```

### SharePointOnPremFrontDoorUrl

This setting specifies the SharePoint Server 2019 on-premises URL that the OneDrive sync app must try to authenticate and sync against.

To enable this setting, you must define a string containing the URL of the on-premises SharePoint Server.

The example for this setting in the .plist file is:

```xml
<key>SharePointOnPremFrontDoorUrl</key>
<string>https://Contoso.SharePoint.com</string>
```

[More info about configuring the OneDrive sync app for SharePoint Server 2019](/sharepoint/install/configure-syncing-with-the-onedrive-sync-app)

### SharePointOnPremPrioritizationPolicy

This setting determines whether or not the sync app should set up sync for SharePoint Server on-premises or SharePoint in Microsoft 365 first during the first-run scenario when the account is the same for both SharePoint Server and SharePoint in Microsoft 365 in a hybrid scenario.

If you set this setting's value to **1**, the OneDrive sync app sets up SharePoint Server first, followed by SharePoint in Microsoft 365.

The example for this setting in the .plist file is:

```xml
<key>SharePointOnPremPrioritizationPolicy</key>
<integer>(0 or 1)</integer>
```

### SharePointOnPremTenantName

This setting enables you to specify the name of the folder created for syncing the SharePoint Server 2019 files specified in the Front Door URL.

If this setting is enabled, you can specify a TenantName that is the name the folder uses in the following convention:
   OneDrive – TenantName (specified by you)
   TenantName (specified by you)

If you don't specify any TenantName, the folder uses the first segment of the FrontDoorURL as its name. For example, https://</span>Contoso.SharePoint.com uses Contoso as the Tenant Name in the following convention: OneDrive – Contoso

The example for this setting in the .plist file is:

```xml
<key>SharePointOnPremTenantName</key>
<string>Contoso</string>
```

[More info about configuring the OneDrive sync app for SharePoint Server 2019](/sharepoint/install/configure-syncing-with-the-onedrive-sync-app)

### Tier

This setting lets you specify the sync app update ring for users in your organization. The OneDrive sync app updates to the public through three rings; first to Insiders, then to Production, and finally to Deferred. When you enable this setting and select a ring, users aren't able to change it.

We recommend selecting several people in your IT department as early adopters to join the Insiders ring and receive features early. We also recommend leaving everyone else in the organization in the default Production ring to ensure they receive bug fixes and new features in a timely fashion. [See all our recommendations for configuring the sync app](ideal-state-configuration.md).

**Insiders**: The Insiders ring users receive builds that let them preview new features coming to OneDrive.

**Production**: The Production ring users get the latest features as they become available. This ring is the default.

**Enterprise** (also known as "Deferred"): The Enterprise ring users get new features, bug fixes, and performance improvements last. This ring lets you deploy updates from an internal network location, and control the timing of the deployment (within a 60-day window).

For more information on the builds currently available in each ring, see the [OneDrive release notes](https://support.office.com/article/845dcf18-f921-435e-bf28-4e24b95e5fc0?). For more information about the update rings and how the sync app checks for updates, see the [OneDrive sync app update process](sync-client-update-process.md).

|.plist Location |Domain |
|:-----|:-----|
| ~/Library/Preferences/com.microsoft.OneDriveUpdater.plist |com.microsoft.OneDriveUpdater |

The example for this setting in the .plist file is:

```xml
<key>Tier</key>
<string>(UpdateRing)</string>
```

> [!NOTE]
> If you want to hide the option "Get pre-release Microsoft internal updates to display", you will need to opt into the Deferred update ring.
> For example, `defaults write com.microsoft.OneDrive Tier -string "Deferred"`.

### UploadBandwidthLimited

This setting defines the maximum upload throughput rate for computers running the OneDrive sync app.

To enable this setting, set a value between 50 and 100000 that is the upload throughput rate in KB/sec the sync app can use.

The example for this setting in the .plist file is:

```xml
<key>UploadBandwidthLimited</key>
<integer>(Upload Throughput Rate in KB/sec)</integer>
```

## Related articles

[Find your Microsoft 365 tenant ID](find-your-office-365-tenant-id.md)

[OneDrive sync reports in the Apps Admin Center (EnableSyncAdminReports)](sync-health.md)
