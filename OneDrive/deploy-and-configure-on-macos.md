---
title: "Deploy and configure the new OneDrive sync app for Mac"
ms.reviewer: 
ms.author: adjoseph
author: adeejoseph
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
- m365initiative-healthyonedrive
- onedrive-toc
search.appverid:
- ODB160
- ODB150
- MET150
ms.assetid: eadddc4e-edc0-4982-9f50-2aef5038c307

description: "Learn how to change settings when deploying or managing the OneDrive sync app on macOS."
---

# Deploy and configure the new OneDrive sync app for Mac

There are two basic ways that you, as an administrator, can deploy the OneDrive sync app to Mac users in your organization:
  
- Install and set up the OneDrive sync app by following the instructions in [Sync files with OneDrive on macOS](https://support.office.com/article/d11b9f29-00bb-4172-be39-997da46f913f). To install the OneDrive sync app for Mac, a user has to be an administrator on the Mac or know an administrator account name and password. 
    
- Download the installer package file to your local network, and then use your software distribution tools to deploy the app to your users. By using a software distribution tool, you have more control over the deployment, including which users get the sync app and when. The OneDrive sync app for Mac uses the Apple Installer technology for installation allowing you to use the software distribution tools that you normally use to deploy software to Mac users. You can use [Microsoft Intune](/mem/intune/apps/apps-add-office365-macOS). Other common tools are [Jamf Pro](https://www.jamf.com/products/jamf-pro/), [Munki](https://www.munki.org/), and [AutoPkg](https://github.com/autopkg/autopkg). You can also use [Apple Remote Desktop](https://www.apple.com/remotedesktop/) and [AppleScript](https://developer.apple.com/library/mac/documentation/AppleScript/Conceptual/AppleScriptX/AppleScriptX.html).
  
## Manage OneDrive settings on macOS using property list (.plist) files

After the OneDrive sync app for Mac is installed, users can configure settings for the app. These settings are called preferences. As an administrator, you might want to provide users in your organization with a standard set of preferences. Preferences for the OneDrive sync app for Mac are stored in property list (.plist) files. 
  
|| Standalone | Mac App Store |
|:-----|:-----|:-----|
|**.plist location  <br/>**|~/Library/Preferences/com.microsoft.OneDrive.plist  <br/> |~/Library/Containers/com.microsoft.OneDrive-mac/Data/Library/Preferences/com.microsoft.OneDrive-mac.plist  <br/> |
|**Domain <br/>**|com.microsoft.OneDrive  <br/> |com.microsoft.OneDrive-mac  <br/> | 
  
## Configure sync app settings

Configure the settings on macOS as follows:
  
1. Quit the OneDrive app.

2. Define the settings you want to change by creating a .plist file with the values. You can also use a script to set the default values.

3. Deploy the settings onto the local computer.

4. Refresh the preferences cache.

    On the next start of OneDrive, the new settings will be picked up.

## Overview of settings

Use the following keys to preconfigure or change settings for your users. The keys are the same whether you run the standalone or Mac App Store edition of the sync app. However, the .plist file name and domain name will be different. When you apply the settings, ensure that you target the appropriate domain depending on the edition of the sync app.

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
- [FilesOnDemandEnabled](deploy-and-configure-on-macos.md#filesondemandenabled)
- [HideDockIcon](deploy-and-configure-on-macos.md#hidedockicon)
- [HydrationDisallowedApps](deploy-and-configure-on-macos.md#hydrationdisallowedapps)
- [KFMBlockOptIn (Preview)](deploy-and-configure-on-macos.md#kfmblockoptin-preview)
- [KFMBlockOptOut (Preview)](deploy-and-configure-on-macos.md#kfmblockoptout-preview)
- [KFMOptInWithWizard (Preview)](deploy-and-configure-on-macos.md#kfmoptinwithwizard-preview)
- [KFMSilentOptIn (Preview)](deploy-and-configure-on-macos.md#kfmsilentoptin-preview)
- [OpenAtLogin](deploy-and-configure-on-macos.md#openatlogin)
- [SharePointOnPremFrontDoorUrl](deploy-and-configure-on-macos.md#sharepointonpremfrontdoorurl)
- [SharePointOnPremPrioritizationPolicy](deploy-and-configure-on-macos.md#sharepointonpremprioritizationpolicy)
- [SharePointOnPremTenantName](deploy-and-configure-on-macos.md#sharepointonpremtenantname)
- [Tier](deploy-and-configure-on-macos.md#tier)
- [UploadBandwidthLimited](deploy-and-configure-on-macos.md#uploadbandwidthlimited)

### AllowTenantList

<a name="AllowTenantList"> </a>

This setting prevents the users from uploading files to other organizations by specifying a list of allowed tenant IDs. If you enable this setting, the user gets an error if they attempt to add an account from an organization that isn't in the allowed tenants list. If the user has already added the account, the files stop syncing. This setting takes priority over **Block syncing OneDrive accounts for specific organizations** setting. Do **NOT** enable both settings at the same time.

The parameter for the **AllowTenantList** key is **TenantID** and its value is a string, which determines the tenants for whom the **Allow Tenant** setting is applicable. For the setting to be complete, this parameter also requires a boolean value to be set to it. If the boolean value is set to **True**, the tenant is allowed to sync.

The example for this setting in the .plist file is:
<br/>\<key\>AllowTenantList</key\><br/>\<dict><br/>\<key\>TenantId1</key\><br/>\<true/\><br/>\<key\>TenantId2</key\><br/>\<true/\><br/>\</dict>

  
### AutomaticUploadBandwidthPercentage

<a name="AutomaticUploadBandwidthPercentage"> </a>

This setting enables the sync app to automatically set the amount of bandwidth that can be used for uploading files, based on available bandwidth.

To enable this setting, you must define a number between 1 and 99 that determines the percentage of bandwidth the sync app can use out of the total available bandwidth.

The example for this setting in the .plist file is:
<br/> \<key\>AutomaticUploadBandwidthPercentage\</key\>  <br/> \<integer\>(Bandwidth)\</integer\>  <br/> 


### BlockExternalSync

<a name="BlockExternalSync"> </a>

This setting prevents the sync app from syncing libraries and folders shared from other organizations.

Set the setting's value to **True**, to prevent the users from syncing OneDrive, SharePoint libraries, and folders with organizations other than the user's own organization. Set the value to **False** or don't enable the setting to allow the OneDrive, and SharePoint files to be synced with other organizations also.

The example for this setting in the .plist file is:
<br/>\<key\>BlockExternalSync\</key\><br/>\<(Bool)/\>


### BlockTenantList

<a name="BlockTenantList"> </a>
This setting prevents the users from uploading files to organizations that are included in the **blocked tenant IDs** list.

If you enable this setting, the users get an error if they attempt to add an account from an organization that is blocked. If a user has already added an account for a blocked organization, the files stop syncing. This setting does NOT work if you have **Allow syncing OneDrive accounts for only specific organizations** setting enabled. Do **NOT** enable both settings at the same time.

Enable this setting by defining IDs for the **TenantID** parameter, which determines the tenants to whom the **block tenant** setting is applicable. Also set the boolean value to **True** for the ID of every tenant you want to prevent from syncing with the OneDrive and SharePoint files and folders.

> [!NOTE]
> In the list, inclusion of the tenant ID alone doesn't suffice. It's mandatory to set the boolean value to **True**  for the ID of each tenant who is to be blocked. 

The example for this setting in the .plist file is:
<br/>\<key\>BlockTenantList</key\><br/>\<dict><br/>\<key\>TenantId1</key\><br/>\<true/\><br/>\<key\>TenantId2</key\><br/>\<true/\><br/>\</dict>

### DefaultFolderLocation

<a name="DefaultFolderLocation"> </a>
This setting specifies the default location of the OneDrive folder for each organization.

The parameters are **TenantID** and **DefaultFolderPath**.
The **TenantID** value is a string that determines the tenants to whom the **default folder location** setting is applicable.
The **DefaultFolderPath** value is a string that specifies the default location of the folder.

The following are the conditions governing the default folder location:
-**Mac app store**: The path must already exist when the user is setting up the sync app.
-**Standalone**: The path will be created (if it doesn't already exist) after the user sets up the sync app. Only with the Standalone sync app you can prevent users from changing the location. 

The example for this setting in the .plist file is:
<br/> \<key\>DefaultFolder</key\><br/>\<dict><br/>\<key\>Path</key\><br/>\<string>(DefaultFolderPath)\</string><br/>\<key\>TenantId</key\><br/>\<string>(TenantID)\</string><br/>\</dict>


### DisableAutoConfig

<a name="DisableAutoConfig"> </a>

This setting determines whether or not the Sync client can automatically sign in.

If you set this setting's value to 1, prevents Sync from automatically signing with an existing AAD credential that is made available to Microsoft applications

The example for this setting in the .plist file is:
<br/> \<key\>DisableAutoConfig</key\> <br/> \<integer\>1</integer\> <br/>


### DisableHydrationToast

<a name="DisableHydrationToast"> </a>

This setting prevents toasts from appearing when applications cause file contents to be downloaded.

If you set the setting's value to **True**, toasts do not appear when applications trigger the download of file contents.

The example for this setting in the .plist file is:
<br/> \<key\>DisableHydrationToast</key\><br/><(Bool)/\> <br/>


### DisablePersonalSync

<a name="DisablePersonalSync"> </a>

This setting blocks user from signing in and syncing files in personal OneDrive accounts. If this setting has been configured after a user has set up sync with a personal account, the user gets signed out.

If you set the setting's value to **True**, the users are prevented from adding or syncing personal accounts.

The example for this setting in the .plist file is:
<br/> \<key\>DisablePersonalSync\</key\>  <br/> \<(Bool)/\>  <br/>


### DisableTutorial

<a name="DisableTutorial"> </a>

This setting prevents the tutorial from being shown to the users after they set up OneDrive.

If you set this setting's value to **True**, the tutorial is blocked from being shown to the users after they set up the OneDrive.

The example for this setting in the .plist file is:
<br/>\<key\>DisableTutorial\</key\><br/>\<(Bool)/\>


### DownloadBandwidthLimited

<a name="DownloadBandwidthLimited"> </a>

This setting sets the maximum download throughput rate in kilobytes (KB)/sec for computers running the OneDrive sync app.

Set this setting's value to an integer between 50 KB/sec and the maximum rate is 100,000 KB/sec that determines the download throughput in KB/sec that the sync app can use.

The example for this setting in the .plist file is:
<br/> \<key\>DownloadBandwidthLimited\</key\>  <br/> \<integer\>(Download Throughput Rate in KB/sec)\</integer\>  <br/>


### EnableAllOcsiClients

<a name="EnableAllOcsiClients"> </a>

This setting lets multiple users use the Microsoft 365 Apps for enterprise, Office 2019, or Office 2016 desktop apps to simultaneously edit an Office file stored in OneDrive. It also lets users share files from the Office desktop apps.

> [!IMPORTANT]
> We recommend keeping this setting enabled to make syncing faster and reduce network bandwidth. [See all our recommendations for configuring the sync app](ideal-state-configuration.md).

If you set this setting to **True** or don't set this setting, the **Office** tab appears in OneDrive sync preferences, and **Use Office applications to sync Office files that I open** is selected, by default.

If you set this setting to **False**, the **Office** tab is hidden in the sync app, and coauthoring and in-app sharing for Office files are disabled. The **User can choose how to handle Office files in conflict** setting acts as disabled, and when file conflicts occur, both copies of the file are kept. For more information about the settings in the sync app, see [Use Office applications to sync Office files that I open](https://support.office.com/article/8a409b0c-ebe1-4bfa-a08e-998389a9d823).

The example for this setting in the .plist file is:
<br/>\<key\>EnableAllOcsiClients\</key\><br/>\<(Bool)/\>


### EnableODIgnore

<a name="EnableODIgnore"> </a>

This setting lets you enter keywords to prevent the OneDrive sync app from uploading certain files to OneDrive or SharePoint. You can enter complete names, such as "setup.exe" or use the asterisk (*) as a wildcard character to represent a series of characters, such as *.pst. Keywords aren't case-sensitive.

If you enable this setting, the sync app doesn't upload new files that match the keywords you specified. No errors appear for the skipped files, and the files remain in the local OneDrive folder. In Finder, the files appear with an "Excluded from sync" icon. 

Users will also see a message in the OneDrive activity center that explains why the files aren't syncing.
Set this setting's value to an integer between 50 KB/sec and the maximum rate of 100,000 KB/sec that determines the download throughput in KB/sec that the sync app can use.

The example for this setting in the .plist file is:
<br/>
\<key\>EnableODIgnore\</key\><br/> 
\<array\><br/>
\<string\>(Keyword such as *.PST)\</string\><br/>
\</array\><br/>


### FilesOnDemandEnabled

<a name="FilesOnDemandEnabled"> </a>

This setting specifies whether Files On-Demand is enabled. 

> [!IMPORTANT]
> We recommend keeping Files On-Demand enabled. [See all our recommendations for configuring the sync app](ideal-state-configuration.md)

If you don't set this setting, Files On-Demand will be enabled automatically as we roll out the feature, and users can turn the setting on or off.  

> [!NOTE]
> Beginning in macOS Monterey 12.1, Files On-Demand will be the default and there will not be a setting for users to turn it off.

If you set this setting to **True**, **FilesOnDemand** is enabled and the users who set up the sync app can view the online-only files, by default. 

If you set this setting to **False**, **FilesOnDemand** is disabled and the users won't be able to turn it on.

The example for this setting in the .plist file is:
<br/> \<key\>FilesOnDemandEnabled</key\>  <br/> <(Bool)/\> <br/>


### HideDockIcon

<a name="HideDockIcon"> </a>

This setting specifies whether a dock icon for OneDrive is shown.

If you set this setting's value to **True**, the OneDrive dock icon is hidden even if the app is running.

The example for this setting in the .plist file is:
<br/> \<key\>HideDockIcon\</key\>  <br/> \<(Bool)/\>  <br/>


### HydrationDisallowedApps

<a name="HydrationDisallowedApps"> </a>

This setting prevents apps from automatically downloading online-only files. You can use this setting to lock down apps that don't work correctly with your deployment of Files On-Demand.

To enable this setting, you must define a string in JSON format as described below:
<br/>`[{"ApplicationId":"appId","MaxBundleVersion":"1.1","MaxBuildVersion":"1.0"}]`<br/>
"appID" can be either the BSD process name or the bundle display name. "MaxBuildVersion" denotes the maximum build version of the app that will be blocked. "MaxBundleVersion" denotes the maximum bundle version of the app that will be blocked.

The example for this setting in the .plist file is:
<br/> \<key\>HydrationDisallowedApps </key\><br/> <string\> `[{"ApplicationId":"appId","MaxBundleVersion":"1.1","MaxBuildVersion":"1.0"}, {"ApplicationId":"appId2","MaxBundleVersion":"3.2","MaxBuildVersion":"2.0"}]`</string\><br/><(Bool)/\> <br/>


### KFMBlockOptIn (Preview)

<a name="KFMBlockOptIn"> </a>

> [!NOTE]
> Known Folder Move in macOS is currently in Private Preview. The following policies may not be available to everyone.

This setting prevents users from moving their Documents and Desktop folders to any OneDrive account.
  
If you enable this setting, users aren't prompted with a window to protect their important folders, and the *Manage backup* command is disabled. If the user has already moved their known folders, the files in those folders will remain in OneDrive. To redirect the known folders back to the user's device, select "No." This setting doesn't take effect if you've enabled "KFMOptInWithWizard" or "KFMSilentOptIn".

If you set this setting's value to 1, it will prevent Known Folder Move.  It you set the value to 2, it will redirect any  folders previously used for Known Folder Move back to the user’s device and stop the setting from running further.

The example for this setting in the .plist file is:
<br/> \<key\>KFMBlockOptIn</key\><br/> \<integer\>(1 or 2)</integer\> <br/> 


### KFMBlockOptOut (Preview)

<a name="KFMBlockOptOut"> </a>

This setting forces users to keep their Documents and Desktop folders directed to OneDrive.

If you enable this setting, the **Stop protecting** button in the **Set up protection of important folders** window is disabled, and users receive an error if they try to stop syncing a known folder.
  
The example for this setting in the .plist file is:
<br/> \<key\>KFMBlockOptOut</key\><br/> \<(Bool)/\>  <br/>


### KFMOptInWithWizard (Preview)

<a name="KFMOptInWithWizard"> </a>

This setting displays a wizard that prompts users to move their Documents and Desktop folders to OneDrive.

If you enable this setting and provide your tenant ID, users who are syncing their OneDrive will see the Known Folder Move wizard window when they're signed in. If they close the window, a reminder notification appears in the Activity Center until they move all their known folders. If a user has already redirected their known folders to a different OneDrive account, they will be prompted to direct their folders to the account for your organization (leaving existing files behind).
  
The example for this setting in the .plist file is:
<br/> \<key\>KFMOptInWithWizard</key\><br/>\<string\>(TenantID)\</string\><br/>


### KFMSilentOptIn (Preview)

<a name="KFMSilentOptIn"> </a>

Use this setting to redirect and move your users' Documents and/or Desktop folders to OneDrive without any user interaction.
  
You can move all folders at once or select the folders you want to move.  After a folder is moved, this setting won't affect that folder again.

The example for this setting in the .plist file is:
<br/> \<key\>KFMSilentOptIn</key\><br/>\<string\>(TenantID)\</string\><br/>

If you enable this setting and provide your tenant ID, you can choose whether to display a notification to users after their folders have been redirected:
<br/> \<key\>KFMSilentOptInWithNotification</key\><br/> \<(Bool)/\>  <br/>

If you don't set any of the following settings, then the default setting will move all the folders (Desktop and Documents) into OneDrive.  If you want to specify which folder(s) to move, you should set any combination of the following settings:

<br/> \<key\>KFMSilentOptInDesktop</key\><br/> \<(Bool)/\> 
<br/> \<key\>KFMSilentOptInDocuments</key\><br/> \<(Bool)/\>  <br/>


### OpenAtLogin

<a name="OpenAtLogin"> </a>

This setting specifies whether OneDrive starts automatically when the user logs in.

If you set this setting's value to **True**, OneDrive starts automatically when the user logs in on Mac.

The example for this setting in the .plist file is:
<br/> \<key\>OpenAtLogin\</key\>  <br/> \<(Bool)/\>  <br/>


### SharePointOnPremFrontDoorUrl

<a name="SharePointOnPremFrontDoorUrl"> </a>

This setting specifies the SharePoint Server 2019 on-premises URL that the OneDrive sync app must try to authenticate and sync against.

To enable this setting, you must define a string containing the URL of the on-premises SharePoint Server.

The example for this setting in the .plist file is:
<br/> \<key\>SharePointOnPremFrontDoorUrl</key\> <br/>\<string\>`https://Contoso.SharePoint.com\`</string\> <br/>

[More info about configuring the OneDrive sync app for SharePoint Server 2019](/sharepoint/install/new-onedrive-sync-client)


### SharePointOnPremPrioritizationPolicy

<a name="SharePointOnPremPrioritizationPolicy"> </a>

This setting determines whether or not the client should set up sync for SharePoint Server or SharePoint in Microsoft 365 first during the first-run scenario when the email is the same for both SharePoint Server on-premises and SharePoint in Microsoft 365 in a hybrid scenario.

If you set this setting's value to **1**, it is an indication that OneDrive should set up SharePoint Server on-premises first, followed by SharePoint in Microsoft 365.

The example for this setting in the .plist file is:
<br/> \<key\>SharePointOnPremPrioritizationPolicy</key\> <br/> \<integer\>(0 or 1)</integer\> <br/>


### SharePointOnPremTenantName

<a name="SharePointOnPremTenantName"> </a>

This setting enables you to specify the name of the folder created for syncing the SharePoint Server 2019 files specified in the Front Door URL.

If this setting is enabled, you can specify a TenantName that is the name the folder will use in the following convention:
<br/> OneDrive – TenantName (specified by you) <br/> TenantName (specified by you)

If you do not specify any TenantName, the folder will use the first segment of the FrontDoorURL as its name. For example, https<span>://</span>Contoso.SharePoint.com will use Contoso as the Tenant Name in the following convention:

<br/> OneDrive – Contoso <br/> Contoso

The example for this setting in the .plist file is:
<br/> \<key\>SharePointOnPremTenantName</key\> <br/> \<string\>Contoso</string\> <br/>

[More info about configuring the OneDrive sync app for SharePoint Server 2019](/sharepoint/install/new-onedrive-sync-client)


### Tier

<a name="Tier"> </a>

This setting lets you specify the ring for users in your organization. The OneDrive sync app updates to the public through three rings; first to Insiders, then to Production, and finally to Deferred.  When you enable this setting and select a ring, users aren't able to change it.  

**Insiders**: The Insiders ring users receive builds that let them preview new features coming to OneDrive.

**Production**: The Production ring users get the latest features as they become available. This ring is the default.

**Enterprise** (now called "Deferred"): The Deferred ring users get new features, bug fixes, and performance improvements last. This ring lets you deploy updates from an internal network location, and control the timing of the deployment (within a 60-day window).

> [!IMPORTANT]
> We recommend selecting several people in your IT department as early adopters to join the Insiders ring and receive features early. We also recommend leaving everyone else in the organization in the default Production ring to ensure they receive bug fixes and new features in a timely fashion. [See all our recommendations for configuring the sync app](ideal-state-configuration.md).

For more information on the builds currently available in each ring, see the [OneDrive release notes](https://support.office.com/article/845dcf18-f921-435e-bf28-4e24b95e5fc0?). For more information about the update rings and how the sync app checks for updates, see the [OneDrive sync app update process](sync-client-update-process.md).

|.plist Location  <br/> |Domain  <br/> |
|:-----|:-----|
| ~/Library/Preferences/com.microsoft.OneDriveUpdater.plist <br/> |com.microsoft.OneDriveUpdater  <br/> |

The example for this setting in the .plist file is:
<br/> \<key\>Tier\</key\>  <br/> \<string\>(UpdateRing)\</string\>  <br/> 


### UploadBandwidthLimited

<a name="UploadBandwidthLimited"> </a>

This setting defines the maximum upload throughput rate in KB/sec for computers running the OneDrive sync app.

To enable this setting, set a value between 50 and 100,000 that is the upload throughput rate the sync app can use.

The example for this setting in the .plist file is:
<br/> \<key\>UploadBandwidthLimited\</key\>  <br/> \<integer\>(Upload Throughput Rate in KB/sec)\</integer\>  <br/>
