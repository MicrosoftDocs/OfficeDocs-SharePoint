---
title: "Deploy and configure the new OneDrive sync client for Mac"
ms.author: kaarins
author: kaarins
manager: pamgreen
ms.audience: Admin
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

description: "Learn how to change settings when deploying or managing the OneDrive sync client on macOS."
---

# Deploy and configure the new OneDrive sync client for Mac

This article is for IT administrators managing OneDrive for Business settings in work or school environments. If you're not an IT administrator, read [Get started with the new OneDrive sync client on Mac OS X](https://support.office.com/article/d11b9f29-00bb-4172-be39-997da46f913f).
  
## Manage OneDrive settings on macOS using property list (Plist) files

Use the following keys to preconfigure or change settings for your users. The keys are the same whether you run the store edition or the standalone edition of the sync client, but the property list file name and domain name will be different. When you apply the settings, make sure to target the appropriate domain depending on the edition of the sync client.
  
||**Standalone**|**Mac App Store**|
|:-----|:-----|:-----|
|PList Location  <br/> |~/Library/Preferences/com.microsoft.OneDrive.plist  <br/> |~/Library/Containers/com.microsoft.OneDrive-mac/Data/Library/Preferences/com.microsoft.OneDrive-mac.plist  <br/> |
|Domain  <br/> |com.microsoft.OneDrive  <br/> |com.microsoft.OneDrive-mac  <br/> |
   
## Deploy the sync client settings

Deploy the settings on macOS in the typical way:
  
1. Quit the OneDrive application.
    
2. Define the settings you want to change by creating a Plist with the values, or use a script to set the default values.
    
3. Deploy the settings onto the local computer.
    
4. Refresh the preferences cache.
    
    On the next start of OneDrive, the new settings will be picked up.
    
## Overview of settings

The following table lists all the settings that are currently exposed for the OneDrive sync client. You need to configure the parameters in parentheses.
  
|**Setting**|**Description**|**Parameters**|**Example Plist Entry**|
|:-----|:-----|:-----|:-----|
|Disable personal accounts  <br/> |Blocks users from signing in and syncing files in personal OneDrive accounts. If this key is set after a user has set up sync with a personal account, the user will be signed out.  <br/> |DisablePersonalSync (Bool): When set to true, this parameter prevents users from adding or syncing personal accounts.  <br/> |\<key\>DisablePersonalSync\</key\>  <br/> \<(Bool)/\>  <br/> |
|Default folder location  <br/> |Specifies the default location of the OneDrive folder for each organization  <br/> |TenantID (String): TenantID determines which accounts the default folder location setting should apply to. [Find your Office 365 tenant ID](find-your-office-365-tenant-id.md) <br/> DefaultFolderPath (String): DefaultFolder specifies the default folder location.  <br/> Mac App Store:  <br/> The path must already exist when users set up the sync client.  <br/> Standalone:  <br/> The path will be created on users' computers if it doesn't already exist. Only with the Standalone sync client can you prevent users from changing the location.  <br/> |\<key\>Tenants\</key\>  <br/> \<dict\>  <br/> \<key\>(TenantID)\</key\>  <br/> \<dict\>  <br/> \<key\>DefaultFolder\</key\>  <br/> \<string\>(DefaultFolderPath)\</string\>  <br/> \</dict\>  <br/> \</dict\>  <br/> |
|Automatic upload bandwidth percentage  <br/> |Enables the sync client to automatically set the amount of bandwidth used based on available bandwidth for uploading files  <br/> |AutomaticUploadBandwidthPercentage (int): This parameter determines the percentage of local upload bandwidth that the sync client can use. Accepted values are from 1 through 99.  <br/> |\<key\>AutomaticUploadBandwidthPercentage\</key\>  <br/> \<int\>(Bandwidth)\</int\>  <br/> |
|Set maximum upload throughput  <br/> |Sets the maximum upload throughput rate in kilobytes (KB)/sec for computers running the OneDrive sync client  <br/> | UploadBandwidthLimited (int): This parameter determines the upload throughput in KB/sec that the sync client can use. The minimum rate is 50 KB/sec and the maximum rate is 100,000 KB/sec.  <br/> |\<key\>UploadBandwidthLimited\</key\>  <br/> \<int\>(Upload Throughput Rate in KB/sec)\</int\>  <br/> |
|Set maximum download throughput  <br/> |Sets the maximum download throughput rate in kilobytes (KB)/sec for computers running the OneDrive sync client  <br/> |DownloadBandwidthLimited (int): This parameter determines the download throughput in KB/sec that the sync client can use. The minimum rate is 50 KB/sec and the maximum rate is 100,000 KB/sec.  <br/> |\<key\>DownloadBandwidthLimited\</key\>  <br/> \<int\>(Download Throughput Rate in KB/sec)\</int\>  <br/> |
|Dock icon  <br/> |Specifies whether a dock icon for OneDrive is shown  <br/> |HideDockIcon (Bool): When set to true, this parameter hides the OneDrive dock icon even when the application is running.  <br/> |\<key\>HideDockIcon\</key\>  <br/> \<(Bool)/\>  <br/> |
|Open at login  <br/> |Specifies whether OneDrive starts automatically when the user logs in  <br/> |OpenAtLogin (Bool): When set to true, OneDrive will start automatically when the user logs in on the Mac.  <br/> |\<key\>OpenAtLogin\</key\>  <br/> \<(Bool)/\>  <br/> |
|Enable Files On-Demand  <br/> |Specifies whether Files On-Demand is enabled. If you don't set this setting, Files On-Demand will be enabled automatically as we roll out the feature, and users can turn the setting on or off  <br/> |FilesOnDemandEnabled (Bool): When set to true, new users who set up the sync client will download online-only files by default. When set to false, Files On-Demand will be disabled and users won't be able to turn it on.  <br/> |\<key\>FilesOnDemandEnabled</key\>  <br/> <(Bool)/\> <br/> |
|Disable download toasts  <br/> |Prevents toasts from appearing when applications cause file contents to be downloaded   <br/> |DisableHydrationToast (Bool): When set to true, toasts will not appear when applications trigger the download of file contents.   <br/> |\<key\>DisableHydrationToast</key\><br/><(Bool)/\> <br/> |
|Block apps from downloading online-only files  <br/> |Prevents applications from automatically downloading online-only files. You can use this setting to lock down applications that don't work correctly with your deployment of Files On-Demand.    <br/> |HydrationDisallowedApps (String): Json in the following format <br/>`[{"ApplicationId":"appId","MaxBundleVersion":"1.1","MaxBuildVersion":"1.0"}]`<br/>"AppID" can be either the BSD process name or the bundle display name. MaxBuildVersion denotes the maximum build version of the application that will be blocked. MaxBundleVersion denotes the maximum bundle version of the application that will be blocked  <br/> |\<key\>HydrationDisallowedApps </key\><br/> <string\> `[{"ApplicationId":"appId","MaxBundleVersion":"1.1","MaxBuildVersion":"1.0"}, {"ApplicationId":"appId2","MaxBundleVersion":"3.2","MaxBuildVersion":"2.0"}]`</string\><br/><(Bool)/\> <br/> |
|SharePoint Server Front Door URL  <br/> |Specifies the SharePoint Server 2019 on-premises URL that the OneDrive sync client should try to authenticate and sync against  <br/> |SharePointOnPremFrontDoorUrl (string): The URL of the on-premises SharePoint Server.  <br/> |\<key\>SharePointOnPremFrontDoorUrl</key\> <br/>\<string\>https://Contoso.SharePoint.com\</string\> <br/> |
|SharePoint Server Tenant Name  <br/> |Specifies the name of the folder created for syncing the SharePoint Server 2019 files specified in the Front Door URL.  <br/> | SharePointOnPremTenantName (string): The name that will be used when creating a folder to sync the on-premises SharePoint Server files. If specified, the folder names will take the form of:<br/> OneDrive – TenantName <br/> TenantName<br/> If not specified, the folder names will use the first segment of the FrontDoorURL as the Tenant Name.<br/> Example - https://Contoso.SharePoint.com will use Contoso as the Tenant Name   <br/> |\<key\>SharePointOnPremTenantName</key\> <br/> \<string\>Contoso</string\> <br/> |
|SharePoint OnPrem Prioritization   <br/> |For hybrid scenarios where the email is the same for both SharePoint Server on-premises and SharePoint Online, determines whether or not the client should set up sync for SharePoint Server or SharePoint Online first during the first-run scenario.   <br/> |SharePointOnPremPrioritizationPolicy (int): This parameter determines which service to attempt to authenticate against for setting up sync.<br/> 1 indicates OneDrive should setup SharePoint Server on-premises first, followed by SharePoint Online.  <br/> |\<key\>SharePointOnPremPrioritizationPolicy</key\> <br/> \<int\>(0 or 1)</int\> <br/> |   
|BlockExternalSync|Prevents the sync client from syncing libraries and folders shared from other organizations.|BlockExternalSync (Bool): Set to true to prevent syncing OneDrive for Business and SharePoint libraries and folders from organizations other than the user's own organization. Set to false or do not include the setting to allow.<br/>[Learn about OneDrive B2B Sync](b2b-sync.md).|\<key\>BlockExternalSync\</key\><br/>\<(Bool)/\>|

You can also configure the OneDrive Standalone sync client to receive delayed updates.
  
|||
|:-----|:-----|
|PList Location  <br/> |~/Library/Preferences/com.microsoft.OneDriveUpdater.plist  <br/> |
|Domain  <br/> |com.microsoft.OneDriveUpdater  <br/> |
   
|**Setting**|**Description**|**Parameters**|**Example Plist Entry**|
|:-----|:-----|:-----|:-----|
|Tier  <br/> |Defines the update ring for the computer  <br/> |UpdateRing (String): This parameter has two different values.  <br/> Production - The default update ring for OneDrive updates.  <br/> Insiders - This update ring receives updates that are "pre-production" and will allow you to play with features before they are released. Note that builds from this ring may be less stable.  <br/> Enterprise - This update ring receives updates after they have rolled out through the Production ring. It also lets you control the deployment of updates. For more info about the update rings and how the sync client checks for updates, see [The OneDrive sync client update process](sync-client-update-process.md).  <br/> |\<key\>Tier\</key\>  <br/> \<string\>(UpdateRing)\</string\>  <br/> |
   

