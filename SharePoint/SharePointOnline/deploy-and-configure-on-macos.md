---
title: "Deploy and configure the OneDrive sync app for Mac"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: serdars
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
|**.plist location**  |~/Library/Preferences/com.microsoft.OneDrive.plist  |~/Library/Containers/com.microsoft.OneDrive-mac/Data/Library/Preferences/com.microsoft.OneDrive-mac.plist  |
|**Domain**  |com.microsoft.OneDrive  |com.microsoft.OneDrive-mac  |
  
## Configure sync app settings

Configure the settings on macOS as follows:
  
1. Define the settings you want to change by creating a .plist file with the values needed. You can use a script to set the values.

1. Quit the OneDrive app.

1. Deploy the settings onto the local computer.

1. Refresh the preferences cache.

On the next start of OneDrive, the new settings will be picked up.

## Overview of settings

Use the following keys to pre-configure or change settings for your users. The keys are the same whether you run the standalone or Mac App Store edition of the sync app. However, the .plist file name and domain name will be different. When you apply the settings, ensure that you target the appropriate domain depending on the edition of the sync app.

## List of settings

- [AllowTenantList](deploy-and-configure-on-macos.md#allowtenantlist)
- [AutomaticUploadBandwidthPercentage](deploy-and-configure-on-macos.md#automaticuploadbandwidthpercentage)
- [BlockExternalSync](deploy-and-configure-on-macos.md#blockexternalsync)
- [BlockTenantList](deploy-and-configure-on-macos.md#blocktenantlist)
- [DefaultFolderLocation](deploy-and-configure-on-macos.md#defaultfolderlocation)
- [DisableAutoConfig](deploy-and-configure-on-macos.md#disableautoconfig)
- [DisableHydrationToast](deploy-and-configure-on-macos.md#disablehydrationtoast)
- [DisablePersonalSync](deploy-and-configure-on-macos.md#disablepersonalsync)
- [DisableTutorial](deploy-and-configure-on-macos.md#disabletutorial)
- [DownloadBandwidthLimited](deploy-and-configure-on-macos.md#downloadbandwidthlimited)
- [EnableAllOcsiClients](deploy-and-configure-on-macos.md#enableallocsiclients)
- [EnableODIgnore](deploy-and-configure-on-macos.md#enableodignore)
- [EnableSyncAdminReports](sync-health.md)
- [FilesOnDemandEnabled](deploy-and-configure-on-macos.md#filesondemandenabled)
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

### AllowTenantList

<a name="AllowTenantList"> </a>

This setting prevents the users from uploading files to other organizations by specifying a list of allowed tenant IDs. If you enable this setting, the user gets an error if they attempt to add an account from an organization that isn't in the allowed tenants list. If the user has already added the account, the files stop syncing. This setting takes priority over the **BlockTenantList** setting. Do **NOT** enable both settings at the same time.

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

<a name="AutomaticUploadBandwidthPercentage"> </a>

This setting enables the sync app to automatically set the amount of bandwidth that can be used for uploading files, based on available bandwidth.

To enable this setting, you must define a number between 1 and 99 that determines the percentage of bandwidth the sync app can use out of the total available bandwidth.

The example for this setting in the .plist file is:
```xml
<key>AutomaticUploadBandwidthPercentage</key>
<integer>(Bandwidth)</integer>
```

### BlockExternalSync

<a name="BlockExternalSync"> </a>

This setting prevents the sync app from syncing libraries and folders shared from other organizations.

Set the setting's value to **True**, to prevent the users from syncing OneDrive, SharePoint libraries, and folders with organizations other than the user's own organization. Set the value to **False** or don't enable the setting to allow the OneDrive, and SharePoint files to be synced with other organizations also.

The example for this setting in the .plist file is:
```xml
<key>BlockExternalSync</key>
<(Bool)/>
```

### BlockTenantList

<a name="BlockTenantList"> </a>
This setting prevents the users from uploading files to organizations that are included in the **blocked tenant IDs** list.

If you enable this setting, the users get an error if they attempt to add an account from an organization that is blocked. If a user has already added an account for a blocked organization, the files stop syncing. This setting does **NOT** work if you've the **AllowTenantList** setting enabled. Do **NOT** enable both settings at the same time.

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

<a name="DefaultFolderLocation"> </a>
This setting specifies the default location of the OneDrive folder for each organization.

The parameters are **TenantID** and **DefaultFolderPath**.
The **TenantID** value is a string that determines the tenants to whom the **default folder location** setting is applicable.
The **DefaultFolderPath** value is a string that specifies the default location of the folder.

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

<a name="DisableAutoConfig"> </a>

This setting determines whether or not the sync app can automatically sign in.

If you set this setting's value to 1, the sync app is prevented from automatically signing with an existing Microsoft Azure Active Directory (Azure AD) credential that is made available to Microsoft applications.

The example for this setting in the .plist file is:
```xml
<key>DisableAutoConfig</key>
<integer>1</integer>
```

### DisableHydrationToast

<a name="DisableHydrationToast"> </a>

This setting prevents toasts from appearing when applications cause file contents to be downloaded.

If you set the setting's value to **True**, toasts don't appear when applications trigger the download of file contents.

The example for this setting in the .plist file is:
```xml
<key>DisableHydrationToast</key>
<(Bool)/>
```

### DisablePersonalSync

<a name="DisablePersonalSync"> </a>

This setting blocks users from signing in and syncing files in personal OneDrive accounts. If this setting has been configured after a user has set up sync with a personal account, the user gets signed out.

If you set the setting's value to **True**, users are prevented from adding or syncing personal accounts.

The example for this setting in the .plist file is:
```xml
<key>DisablePersonalSync</key>
<(Bool)/>
```

### DisableTutorial

<a name="DisableTutorial"> </a>

This setting prevents the tutorial from being shown to the users after they set up OneDrive.

If you set this setting's value to **True**, the tutorial is blocked from being shown to the users after they set up the OneDrive sync app.

The example for this setting in the .plist file is:
```xml
<key>DisableTutorial</key>
<(Bool)/>
```


### DownloadBandwidthLimited

<a name="DownloadBandwidthLimited"> </a>

This setting sets the maximum download throughput rate in kilobytes (KB)/sec for computers running the OneDrive sync app.

Set this setting's value to an integer between 50 and 100000 to specify the download throughput in KB/sec that the sync app can use.

The example for this setting in the .plist file is:
```xml
<key>DownloadBandwidthLimited</key>
<integer>(Download Throughput Rate in KB/sec)</integer>
```

### EnableAllOcsiClients

<a name="EnableAllOcsiClients"> </a>

This setting lets multiple users use the Microsoft 365 Apps for enterprise, Office 2019, or Office 2016 desktop apps to simultaneously edit an Office file stored in OneDrive. It also lets users share files from the Office desktop apps.

> [!IMPORTANT]
> We recommend keeping this setting enabled to make syncing faster and reduce network bandwidth usage. [See all our recommendations for configuring the sync app](ideal-state-configuration.md).

If you set this setting to **True** or don't set this setting, the **Office** tab appears in OneDrive sync preferences, and **Use Office applications to sync Office files that I open** is selected, by default.

If you set this setting to **False**, the **Office** tab is hidden in the sync app, and coauthoring and in-app sharing for Office files are disabled. The **User can choose how to handle Office files in conflict** setting is disabled, and when file conflicts occur, both copies of the file are kept. For more information about the settings in the sync app, see [Use Office applications to sync Office files that I open](https://support.office.com/article/8a409b0c-ebe1-4bfa-a08e-998389a9d823).

The example for this setting in the .plist file is:
```xml
<key>EnableAllOcsiClients</key>
<(Bool)/>
```

### EnableODIgnore

<a name="EnableODIgnore"> </a>

This setting lets you enter keywords to prevent the OneDrive sync app from uploading certain files to OneDrive or SharePoint. You can enter complete names, such as "setup.exe" or use the asterisk (*) as a wildcard character to represent a series of characters, such as *.pst. Keywords aren't case-sensitive.

If you enable this setting, the sync app doesn't upload new files that match the keywords you specified. No errors appear for the skipped files, and the files remain in the local OneDrive folder. In Finder, the files appear with an "Excluded from sync" icon.

Users will also see a message in the OneDrive activity center that explains why the files aren't syncing.

The example for this setting in the .plist file is:
```xml
<key>EnableODIgnore</key>
<array>
<string>(Keyword such as *.PST)</string>
</array>
```

### FilesOnDemandEnabled

<a name="FilesOnDemandEnabled"> </a>

This setting specifies whether Files On-Demand is enabled.

> [!NOTE]
> Beginning in macOS Monterey 12.1, Files On-Demand will be permanently enabled and this setting will no longer have any effect.

#### macOS versions prior to Monterey 12.1

If you set this setting to **True**, **FilesOnDemand** is enabled and the users who set up the sync app can view the online-only files, by default.

If you set this setting to **False**, **FilesOnDemand** is disabled and the users won't be able to turn it on.

The example for this setting in the .plist file is:
```xml
<key>FilesOnDemandEnabled</key>
<(Bool)/>
```

> [!NOTE]
> We recommend keeping Files On-Demand enabled. [See all our recommendations for configuring the sync app](ideal-state-configuration.md)

### HideDockIcon

<a name="HideDockIcon"> </a>

This setting specifies whether a dock icon for OneDrive is shown.

If you set this setting's value to **True**, the OneDrive dock icon is hidden even if the app is running.

The example for this setting in the .plist file is:
```xml
<key>HideDockIcon</key>
<(Bool)/>
```

### HydrationDisallowedApps

<a name="HydrationDisallowedApps"> </a>

This setting prevents apps from automatically downloading online-only files. You can use this setting to lock down apps that don't work correctly with your deployment of Files On-Demand.

To enable this setting, you must define a string in JSON format as described below:
<br/>`[{"ApplicationId":"appId","MaxBundleVersion":"1.1","MaxBuildVersion":"1.0"}]`<br/>
"appID" can be either the BSD process name or the bundle display name. "MaxBuildVersion" denotes the maximum build version of the app that will be blocked. "MaxBundleVersion" denotes the maximum bundle version of the app that will be blocked.

The example for this setting in the .plist file is:
```xml
<key>HydrationDisallowedApps</key>
<string>[{"ApplicationId":"appId","MaxBundleVersion":"1.1","MaxBuildVersion":"1.0"}, {"ApplicationId":"appId2","MaxBundleVersion":"3.2","MaxBuildVersion":"2.0"}]</string>
<(Bool)/>
```

### KFMBlockOptIn

<a name="KFMBlockOptIn"> </a>

This setting prevents users from moving their Documents and Desktop folders to any OneDrive account.
  
If you enable KFMBlockOptIn, users aren't prompted to protect their Desktop and Documents folders, and the *Manage backup* command is disabled. If the user has already moved their Desktop and Documents folders, the files in those folders will remain in OneDrive. This setting doesn't take effect if you've enabled **KFMOptInWithWizard**" or **KFMSilentOptIn**.

If you set this setting's value to 1, it will prevent Folder Backup.  If you set the value to 2, it will redirect any  folders previously used for Folder Backup back to the user’s device and stop the setting from running further.

The example for this setting in the .plist file is:
```xml
<key>KFMBlockOptIn</key>
<integer>(1 or 2)</integer>
```

### KFMBlockOptOut

<a name="KFMBlockOptOut"> </a>

This setting forces users to keep their Documents and Desktop folders directed to OneDrive.

If you enable this setting, the **Stop Backup** button in the **Manage Folder Backup** window is disabled, and users receive an error if they try to stop syncing their Desktop or Documents folder.
  
The example for this setting in the .plist file is:
```xml
<key>KFMBlockOptOut</key>
<(Bool)/>
```

### KFMOptInWithWizard

<a name="KFMOptInWithWizard"> </a>

This setting displays a wizard that prompts users to move their Documents and Desktop folders to OneDrive.

If you enable this setting and provide your tenant ID, users who are syncing their OneDrive will see the Folder Backup wizard window when they're signed in. If they close the window, a reminder notification appears in the Sync Activity Center until they move their Desktop and Documents folders.
  
The example for this setting in the .plist file is:
```xml
<key>KFMOptInWithWizard</key>
<string>(TenantID)</string>
```

### KFMSilentOptIn

<a name="KFMSilentOptIn"> </a>

Use this setting to redirect and move your users' Documents and/or Desktop folders to OneDrive without any user interaction.
  
You can move both folders at once or select which folder you want to move.  After a folder is moved, this setting won't affect that folder again.

The example for this setting in the .plist file is:
```xml
<key>KFMSilentOptIn</key>
<string>(TenantID)</string>
```

If you enable this setting and provide your tenant ID, you can choose whether to display a notification to users after their folders have been redirected:
```xml
<key>KFMSilentOptInWithNotification</key>
<(Bool)/>
```

If you don't set any of the following settings, then the default setting will move both folders into OneDrive.  If you want to specify which folder to move, you should set any combination of the following settings:
```xml
<key>KFMSilentOptInDesktop</key>
<(Bool)/>
<key>KFMSilentOptInDocuments</key>
<(Bool)/>
```

### OpenAtLogin

<a name="OpenAtLogin"> </a>

This setting specifies whether OneDrive starts automatically when the user logs in.

If you set this setting's value to **True**, OneDrive starts automatically when the user logs in to their Mac.

The example for this setting in the .plist file is:
```xml
<key>OpenAtLogin</key>
<(Bool)/>
```

### SharePointOnPremFrontDoorUrl

<a name="SharePointOnPremFrontDoorUrl"> </a>

This setting specifies the SharePoint Server 2019 on-premises URL that the OneDrive sync app must try to authenticate and sync against.

To enable this setting, you must define a string containing the URL of the on-premises SharePoint Server.

The example for this setting in the .plist file is:
```xml
<key>SharePointOnPremFrontDoorUrl</key>
<string>https://Contoso.SharePoint.com</string>
```

[More info about configuring the OneDrive sync app for SharePoint Server 2019](/sharepoint/install/configure-syncing-with-the-onedrive-sync-app)

### SharePointOnPremPrioritizationPolicy

<a name="SharePointOnPremPrioritizationPolicy"> </a>

This setting determines whether or not the sync app should set up sync for SharePoint Server on-premises or SharePoint in Microsoft 365 first during the first-run scenario when the account is the same for both SharePoint Server and SharePoint in Microsoft 365 in a hybrid scenario.

If you set this setting's value to **1**, the OneDrive sync app will set up SharePoint Server first, followed by SharePoint in Microsoft 365.

The example for this setting in the .plist file is:
```xml
<key>SharePointOnPremPrioritizationPolicy</key>
<integer>(0 or 1)</integer>
```

### SharePointOnPremTenantName

<a name="SharePointOnPremTenantName"> </a>

This setting enables you to specify the name of the folder created for syncing the SharePoint Server 2019 files specified in the Front Door URL.

If this setting is enabled, you can specify a TenantName that is the name the folder will use in the following convention:
   OneDrive – TenantName (specified by you)
   TenantName (specified by you)

If you don't specify any TenantName, the folder will use the first segment of the FrontDoorURL as its name. For example, https<span>://</span>Contoso.SharePoint.com will use Contoso as the Tenant Name in the following convention:
   OneDrive – Contoso
   Contoso

The example for this setting in the .plist file is:
```xml
<key>SharePointOnPremTenantName</key>
<string>Contoso</string>
```

[More info about configuring the OneDrive sync app for SharePoint Server 2019](/sharepoint/install/configure-syncing-with-the-onedrive-sync-app)

### Tier

<a name="Tier"> </a>

This setting lets you specify the sync app update ring for users in your organization. The OneDrive sync app updates to the public through three rings; first to Insiders, then to Production, and finally to Deferred.  When you enable this setting and select a ring, users aren't able to change it.

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
> For example, `default write com.microsoft.OneDrive Tier -string "Deferred"`.                                                                      

### UploadBandwidthLimited

<a name="UploadBandwidthLimited"> </a>

This setting defines the maximum upload throughput rate for computers running the OneDrive sync app.

To enable this setting, set a value between 50 and 100000 that is the upload throughput rate in KB/sec the sync app can use.

The example for this setting in the .plist file is:
```xml
<key>UploadBandwidthLimited</key>
<integer>(Upload Throughput Rate in KB/sec)</integer>
```

## Related articles

[Find your Microsoft 365 tenant ID](find-your-office-365-tenant-id.md)
