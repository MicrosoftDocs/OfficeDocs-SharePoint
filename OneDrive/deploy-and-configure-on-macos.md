---
title: "Deploy and configure the new OneDrive sync app for Mac"
ms.reviewer: joleung
ms.author: kaarins
author: kaarins
manager: pamgreen
audience: Admin
f1.keywords:
- NOCSH
ms.topic: get-started-article
ms.service: one-drive
localization_priority: Normal
ms.collection: 
- Strat_OD_admin
- M365-collaboration
search.appverid:
- ODB160
- ODB150
- MET150
ms.assetid: eadddc4e-edc0-4982-9f50-2aef5038c307

description: "Learn how to change settings when deploying or managing the OneDrive sync app on macOS."
---

# Deploy and configure the new OneDrive sync app for Mac

There are two basic ways that you, as an administrator, can deploy the OneDrive sync app to Mac users in your organization:
  
- Have users install and set up the OneDrive sync app themselves by following the instructions in [Sync files with OneDrive on Mac OS X](https://support.office.com/article/d11b9f29-00bb-4172-be39-997da46f913f). To install the OneDrive sync app for Mac, a user has to be an administrator on the Mac or know an administrator account name and password. 
    
- Download the installer package file to your local network, and then use your software distribution tools to deploy the app to your users. By using a software distribution tool, you have more control over the deployment, including which users get the sync app and when. The OneDrive sync app for Mac uses the Apple Installer technology for installation. This means you can continue to use the software distribution tools that you normally use to deploy software to Mac users. You can use [Microsoft Intune](/mem/intune/apps/apps-add-office365-macOS). Other common tools are [Jamf Pro](https://www.jamfsoftware.com/products/casper-suite/), [Munki](https://www.munki.org/), and [AutoPkg](https://github.com/autopkg/autopkg). You can also use [Apple Remote Desktop](https://www.apple.com/remotedesktop/) and [AppleScript](https://developer.apple.com/library/mac/documentation/AppleScript/Conceptual/AppleScriptX/AppleScriptX.html).
  
## Manage OneDrive settings on macOS using property list (Plist) files

After the OneDrive sync app for Mac is installed, users can configure settings for the app. These settings are called preferences. As an administrator, you might want to provide users in your organization with a standard set of preferences. Preferences for the OneDrive sync app for Mac are stored in preference files. These files are often referred to as .plist files. 
  
||**Standalone**|**Mac App Store**|
|:-----|:-----|:-----|
|**PList Location  <br/>**|~/Library/Preferences/com.microsoft.OneDrive.plist  <br/> |~/Library/Containers/com.microsoft.OneDrive-mac/Data/Library/Preferences/com.microsoft.OneDrive-mac.plist  <br/> |
|**Domain <br/>**|com.microsoft.OneDrive  <br/> |com.microsoft.OneDrive-mac  <br/> | 
  
## Configure sync app settings

Configure the settings on macOS in the typical way:
  
1. Quit the OneDrive app.

2. Define the settings you want to change by creating a Plist with the values, or use a script to set the default values.

3. Deploy the settings onto the local computer.

4. Refresh the preferences cache.

    On the next start of OneDrive, the new settings will be picked up.

## Overview of settings

Use the following keys to preconfigure or change settings for your users. The keys are the same whether you run the standalone or Mac App Store edition of the sync app, but the property list file name and domain name will be different. When you apply the settings, make sure to target the appropriate domain depending on the edition of the sync app.

### AllowTenantList

This setting prevents the users from uploading files to other organizations by specifying a list of allowed tenant IDs. If you enable this setting, the user gets an error if they attempt to add an account from an organization that is not in the allowed tenants list. If the user has already added the account, the files stop syncing. This setting takes priority over **Block syncing OneDrive accounts for specific organizations** setting. Do not enable both settings at the same time.

The parameter for the **AllowTenantList** key is **TenantID** and its value is a string which determines the tenants for whom the **Allow Tenant** setting is applicable. This parameter also needs a boolean value too be set to it for the setting to be complete. If the boolean value is set to **True**, the tenant is allowed to sync.

The example for this setting in the **.plist** file is:
<key>TenantID</key>
<array>
 <dict>
  <key>TenantID1</key>
  <Bool>True</Bool>
  <key>TenantID2</key>
  <Bool>True</Bool>
 </dict>
</array>
  
### AutomaticUploadBandwidthPercentage

This setting enables the sync app to automatically set the amount of bandwidth that can be used for uploading files, based on available bandwidth.

To enable this setting, you must define a number between 1 and 99 which determines the percentage of bandwidth the sync app can use out of the total available bandwidth.

The example for this setting in the **.plist** file is:
<key>AutomaticUploadBandwidthPercentage</key>
<int>Bandwidth</int>

### BlockExternalSync

This setting prevents the sync app from syncing libraries and folders shared from other organizations.

If you set the setting's value to **True**, the users are prevented from syncing OneDrive and SharePoint libraries and folders with organizations other than the user's own organization. Set this value to **False** or do not enable the setting to allow the OneDrive and SharePoint files to be synced with other organizations also.

The example for this setting in the **.plist** file is:
<key>BlockExternalSync</key>
<Bool/>

### BlockTenantList

This setting prevents the users from uploading files to organizations that are included in the **blocked tenant IDs** list that is specified. 

If you enable this setting, the users get an error if they attempt to add an account from an organization that is blocked. If a user has already added an account for a blocked organization, the files stop syncing. This setting does NOT work if you have **Allow syncing OneDrive accounts for only specific organizations** setting enabled. Do not enable both settings at the same time.

You must enable this setting by defining IDs for the **TenantID** parameter which determines the tenants to whom the **block tenant** setting is applicable. You must also set the boolean value to **True** for the ID of every tenant you want to prevent from syncing with the OneDrive and SharePoint files and folders.

**Note**: In the list, inclusion of the tenant ID alone does not suffice. It is mandatory to set the boolean value to **True**  for the ID of each tenant who is to be blocked. 

The example for this setting in the **.plist** file is:
<key>BlockTenantList</key>
<array>
 <dict>
  <key>TenantID1</key>
  <Bool>True</Bool>
  <key>TenantID2</key>
  <Bool>True</Bool>
 </dict>
</array>

### DefaultFolderLocation

This setting specifies the default location of the OneDrive folder for each organization.

The parameters are **TenantID** and **DefaultFolderPath**.
The **TenantID** value is a string that determines the tenants to whom the **default folder location** setting is applicable.
The **DefaultFolderPath** value is a string that specifies the default location of the folder.

The following are the conditions governing the default folder location:
-**Mac app store**: The path must already exist when the user is setting up the sync app.
-**Standalone**: The path will be created (if it doesn't already exist) after the user sets up the sync app. Only with the Standalone sync app you can prevent users from changing the location. 

The example for this setting in the **.plist** file is:
<key>DefaultFolder</key>
<array>
 <dict>
  <key>Path</key>
  <string>(DefaultFolderPath)</string>
  <key>TenantId</key>
  <string>(TenantID)</string>
 </dict>
</array>

### DisableHydrationToast

This setting prevents toasts from appearing when applications cause file contents to be downloaded.

If you set the setting's value to **True**, toasts do not appear when applications trigger the download of file contents.

The example for this setting in the **.plist** file is:
<key>DisableHydrationToast</key>
<Bool/>

### DisablePersonalSync

This setting blocks users from signing in and syncing files in personal OneDrive accounts. If this setting has been configured after a user has set up sync with a personal account, the user gets signed out.

If you set the setting's value to **True**, the users are prevented from adding or syncing personal accounts.

The example for this setting in the **.plist** file is:
<key>DisablePersonalSync</key>
<Bool/>

### DisableTutorial

This setting prevents the tutorial from being shown to the users after they set up OneDrive.

If you set this setting's value to **True**, the tutorial is blocked from being shown to the users after they set up the OneDrive.

The example for this setting in the **.plist** file is:
<key>DisableTutorial</key>
<Bool/>

### DownloadBandwidthLimited

This setting sets the maximum download throughput rate in kilobytes (KB)/sec for computers running the OneDrive sync app.

You must set this setting's value to an integer between 50 KB/sec and the maximum rate is 100,000 KB/sec which determines the download throughput in KB/sec which the sync app can use.

The example for this setting in the **.plist** file is:
<key>DownloadBandwidthLimited</key>
<int>(Download Throughput Rate in KB/sec)</int>

### FilesOnDemandEnabled

This setting specifies whether Files On-Demand is enabled. 

If you don't set this setting, Files On-Demand will be enabled automatically as we roll out the feature, and users can turn the setting on or off.

If you set this setting to **True**, **FilesOnDemand** is enabled and the users who set up the sync app can view the online-only files, by default. 

If you set this setting to **False**, **FilesOnDemand** is disabled and the users won't be able to turn it on.

The example for this setting in the **.plist** file is:
<key>FilesOnDemandEnabled</key>
<Bool/>

### HideDockIcon

This setting specifies whether a dock icon for OneDrive is shown.

If you set this setting's value to **True**, the OneDrive dock icon is hidden even if the app is running.

The example for this setting in the **.plist** file is:
<key>HideDockIcon</key>
<Bool/>

### HydrationDisallowedApps

This setting prevents apps from automatically downloading online-only files. You can use this setting to lock down apps that don't work correctly with your deployment of Files On-Demand.

To enable this setting, you must define a string in JSON format as described below:
<br/>`[{"ApplicationId":"appId","MaxBundleVersion":"1.1","MaxBuildVersion":"1.0"}]`<br/>
"appID" can be either the BSD process name or the bundle display name. "MaxBuildVersion" denotes the maximum build version of the app that will be blocked. "MaxBundleVersion" denotes the maximum bundle version of the app that will be blocked.

The example for this setting in the **.plist** file is:
<key>HydrationDisallowedApps</key>
<string>
[{"ApplicationId":"appId","MaxBundleVersion":"1.1","MaxBuildVersion":"1.0"}, {"ApplicationId":"appId2","MaxBundleVersion":"3.2","MaxBuildVersion":"2.0"}]
</string>
<Bool/>

### OpenAtLogin

This setting specifies whether OneDrive starts automatically when the user logs in.

If you set this setting's value to **True**, OneDrive starts automatically when the user logs in on Mac.

The example for this setting in the **.plist** file is:
<key>OpenAtLogin</key>
<Bool/>

### SharePointOnPremFrontDoorUrl

This setting specifies the SharePoint Server 2019 on-premises URL that the OneDrive sync app must try to authenticate and sync against. 

To enable this setting, you must define a string containing the URL of the on-premises SharePoint Server.

The example for this setting in the **.plist** file is:
<key>SharePointOnPremFrontDoorUrl</key>
<string>https://Contoso.SharePoint.com</string>

### SharePointOnPremPrioritizationPolicy

This setting determines whether or not the client should set up sync for SharePoint Server or SharePoint in Microsoft 365 first during the first-run scenario when the email is the same for both SharePoint Server on-premises and SharePoint in Microsoft 365 in a hybrid scenario.

If you set this setting's value to **1**, it is an indication that OneDrive should set up SharePoint Server on-premises first, followed by SharePoint in Microsoft 365.

The example for this setting in the **.plist** file is:
<key>SharePointOnPremPrioritizationPolicy</key>
<int>(0 or 1)</int>

### SharePointOnPremTenantName

This setting enables you to specify the name of the folder created for syncing the SharePoint Server 2019 files specified in the Front Door URL.

If this setting is enabled, you can specify a TenantName which is the name the folder will use in the following convention:
<br/> OneDrive – TenantName (specified by you) <br/> TenantName (specified by you)

If you do not specify any TenantName, the folder will use the first segment of the FrontDoorURL as the its name. For example, https://Contoso.SharePoint.com will use Contoso as the Tenant Name in the following convention:
<br/> OneDrive – Contoso <br/> Contoso


The example for this setting in the **.plist** file is:
<key>SharePointOnPremTenantName</key>
<string>Contoso</string>

### UploadBandwidthLimited

This setting defines the maximum upload throughput rate in KB/sec for computers running the OneDrive sync app.

To enable this setting, set a value between 50 and 100,000 which is the upload throughput rate the sync app can use.

The example for this setting in the **.plist** file is:
<key>UploadBandwidthLimited</key>
<int>(Upload Throughput Rate in KB/sec)</int>

You can also configure the OneDrive Standalone sync app to receive delayed updates.
  
|PList Location  <br/> |Domain  <br/> |
|:-----|:-----|
| ~/Library/Preferences/com.microsoft.OneDriveUpdater.plist <br/> |com.microsoft.OneDriveUpdater  <br/> |
   
|**Setting**|**Description**|**Parameters**|**Example Plist Entry**|
|:-----|:-----|:-----|:-----|
|Tier  <br/> |Defines the update ring for the computer  <br/> |UpdateRing (String): This parameter has two different values.  <br/> Production - The default update ring for OneDrive updates.  <br/> Insiders - This update ring receives updates that are "pre-production" and that allow you to play with features before they are released. Note that builds from this ring may be less stable.  <br/> Enterprise - This update ring (now called "Deferred") receives updates after they have been rolled out through the Production ring. It also lets you control the deployment of updates. For more information about the update rings and the procedure used by the sync app for checking for updates, see [The OneDrive sync app update process](sync-client-update-process.md).  <br/> |\<key\>Tier\</key\>  <br/> \<string\>(UpdateRing)\</string\>  <br/> |
