---
title: "Use Group Policy to control OneDrive sync client settings"
ms.reviewer: 
ms.author: kaarins
author: kaarins
manager: pamgreen
audience: Admin
ms.topic: article
ms.service: one-drive
localization_priority: Priority
ms.collection: 
- Strat_OD_admin
- M365-collaboration
search.appverid:
- ODB160
- MOE150
- MED150
- MBS150
- ODB150
- MET150
ms.assetid: 0ecb2cf5-8882-42b3-a6e9-be6bda30899c
description: "Learn how to use Group Policy to administer settings for the OneDrive sync client."
---

# Use Group Policy to control OneDrive sync client settings

This article is for IT admins who manage the new OneDrive sync client in a Windows Server enterprise environment that uses Active Directory Domain Services (AD DS).
  
> [!NOTE]
> If you're not an IT admin, see [Sync files with the new OneDrive sync client in Windows](https://support.office.com/article/615391c4-2bd3-4aae-a42a-858262e42a49) for info about OneDrive sync settings. 


> [!VIDEO https://www.microsoft.com/videoplayer/embed/RE2CnSx]
 
## Manage OneDrive using Group Policy

1. Install the OneDrive sync client for Windows. (To see which builds are releasing and download builds, go to the [release notes](https://support.office.com/article/845dcf18-f921-435e-bf28-4e24b95e5fc0?).) Installing the sync client downloads the .adml and .admx files.
    
2. Browse to %localappdata%\Microsoft\OneDrive\BuildNumber\adm\, to the subfolder for your language as necessary. 
    
    (Where *BuildNumber* is the number displayed in sync client settings on the About tab.) 
    
    ![The ADM folder in the OneDrive installation directory](media/85e0fe3f-84eb-4a29-877f-c706dda4d075.png)
  
3. Copy the .adml and .admx files.

4. Paste the .admx file in your domain's Central Store, \\*domain*\sysvol\domain\Policies\PolicyDefinitions (where *domain* is your domain name, such as corp.contoso.com), and the .adml in the appropriate language subfolder (such as en-us). If the PolicyDefinitions folder does not exist, see [How to create and manage the Central Store for Group Policy Administrative Templates in Windows](https://support.microsoft.com/en-us/help/3087759).
    
5. Configure settings from the domain controller or on a Windows computer by running the [Remote Server Administration Tools](https://go.microsoft.com/fwlink/?linkid=871794). 
    
6. Link the Group Policy objects to an Active Directory container (site, domain, or organizational unit). For info, see [Link Group Policy objects to Active Directory containers](https://go.microsoft.com/fwlink/?linkid=871796).
    
7. Use security filtering to narrow the scope of a setting. By default, a setting is applied to all user and computer objects within the container to which it's linked, but you can use security filtering to narrow the scope of the policy's application to a subset of users or computers. For info, see [Filtering the scope of a GPO](https://go.microsoft.com/fwlink/?linkid=2004146).
    
The OneDrive Group Policy objects work by setting registry keys on the computers in your domain.
  
- When you enable or disable a setting, the corresponding registry key is updated on computers in your domain. If you later change the setting back to **Not configured**, the corresponding registry key is not modified and the change does not take effect. So after you configure a setting, set it to **Enabled** or **Disabled** going forward. 
    
- The location where registry keys are written has been updated. When you use the latest files, you might delete registry keys that you set previously.

> [!NOTE]
> For information about storage see [OneDrive Files On-Demand and Storage Sense for Windows 10](https://support.office.com/article/onedrive-files-on-demand-and-storage-sense-for-windows-10-de5faa9a-6108-4be1-87a6-d90688d08a48) and [Policy CSP - Storage](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-storage).

## List of policies

  
- [Allow syncing OneDrive accounts for only specific organizations](use-group-policy.md#AllowTenantList)
    
- [Allow users to choose how to handle Office file sync conflicts](use-group-policy.md#EnableHoldTheFile)

- [Block syncing OneDrive accounts for specific organizations](use-group-policy.md#BlockTenantList)
    
- [Coauthor and share in Office desktop apps](use-group-policy.md#EnableAllOcsiClients)

- [Configure team site libraries to sync automatically](use-group-policy.md#AutoMountTeamSites)

- [Continue syncing on metered networks](use-group-policy.md#DisablePauseOnMeteredNetwork)

- [Continue syncing when devices have battery saver mode turned on](use-group-policy.md#DisablePauseOnBatterySaver)

- [Convert synced team site files to online-only files](use-group-policy.md#DehydrateSyncedTeamSites)
 
- [Disable the tutorial that appears at the end of OneDrive Setup](use-group-policy.md#DisableFRETutorial)

- [Limit the sync client download speed to a fixed rate](use-group-policy.md#DownloadBandwidthLimit)

- [Limit the sync client upload rate to a percentage of throughput](use-group-policy.md#AutomaticUploadBandwidthPercentage)

- [Limit the sync client upload speed to a fixed rate](use-group-policy.md#UploadBandwidthLimit)
    
- [Prevent the sync client from generating network traffic until users sign in](use-group-policy.md#PreventNetworkTraffic)
    
- [Prevent users from changing the location of their OneDrive folder](use-group-policy.md#DisableCustomRoot)

- [Prevent users from fetching files remotely](use-group-policy.md#RemoteAccessGPOEnabled)

- [Prevent users from moving their Windows known folders to OneDrive](use-group-policy.md#BlockKnownFolderMove)

- [Prevent users from redirecting their Windows known folders to their PC](use-group-policy.md#KFMBlockOptOut)

- [Prevent users from syncing libraries and folders shared from other organizations](use-group-policy.md#BlockExternalSync)

- [Prevent users from syncing personal OneDrive accounts](use-group-policy.md#DisablePersonalSync)
 
- [Prompt users to move Windows known folders to OneDrive](use-group-policy.md#KFMOptInWithWizard)
    
- [Receive OneDrive sync client updates on the Enterprise ring](use-group-policy.md#EnableEnterpriseUpdate)

- [Require users to confirm large delete operations](use-group-policy.md#ForcedLocalMassDeleteDetection)

- [Set the default location for the OneDrive folder](use-group-policy.md#DefaultRootDir)
 
- [Set the maximum size of a user's OneDrive that can download automatically](use-group-policy.md#DiskSpaceCheckThresholdMB)

- [Set the sync client update ring](use-group-policy.md#GPOSetUpdateRing)
    
- [Silently move Windows known folders to OneDrive](use-group-policy.md#KFMOptInNoWizard)

- [Silently sign in users to the OneDrive sync client with their Windows credentials](use-group-policy.md#SilentAccountConfig)

- [Use OneDrive Files On-Demand](use-group-policy.md#FilesOnDemandEnabled)

> [!NOTE]
> "Specify SharePoint Server URL and organization name" and "Specify the OneDrive location in a hybrid environment" are for customers who have SharePoint Server 2019. [More info about using the new OneDrive sync client with SharePoint Server 2019](/SharePoint/install/new-onedrive-sync-client/)

    
## Computer Configuration policies
<a name="PerTen"> </a>

Computer Configuration policies can be found under Computer Configuration\Policies\Administrative Templates\OneDrive.
  
![Computer Configuration policies in the Group Policy Management Editor](media/07b81d35-9ccc-4c61-8a86-52d9bcff7ddb.png)
  

  
### Allow syncing OneDrive accounts for only specific organizations
<a name="AllowTenantList"> </a>

This setting lets you prevent users from easily uploading files to other organizations by specifying a list of allowed tenant IDs.

If you enable this setting, users will get an error if they attempt to add an account from an organization that is not allowed. If a user has already added the account, the files will stop syncing.

In the **Options** box, click **Show** to enter the tenant ID. 
  
This policy sets the following registry key.
  
[HKLM\SOFTWARE\Policies\Microsoft\OneDrive\AllowTenantList] "1111-2222-3333-4444"
  
(where "1111-2222-3333-4444" is the [tenant ID](find-your-office-365-tenant-id.md))
  
This setting will take priority over [Block syncing OneDrive accounts for specific organizations](use-group-policy.md#BlockTenantList). Do not enable both settings at the same time.
  
### Block syncing OneDrive accounts for specific organizations
<a name="BlockTenantList"> </a>

This setting lets you prevent users from easily uploading files to another organization by specifying a list of blocked tenant IDs.

If you enable this setting, users will get an error if they attempt to add an account from an organization that is blocked. If a user has already added the account, the files will stop syncing.
  
In the **Options** box, click **Show** to enter the tenant ID.
  
This policy sets the following registry key.
  
[HKLM\SOFTWARE\Policies\Microsoft\OneDrive\BlockTenantList] "1111-2222-3333-4444"﻿
  
(where "1111-2222-3333-4444" is the [tenant ID](find-your-office-365-tenant-id.md))
  
This setting will NOT work if you have [Allow syncing OneDrive accounts for only specific organizations](use-group-policy.md#AllowTenantList) enabled. Do not enable both settings at the same time.
  
### Convert synced team site files to online-only files
<a name="DehydrateSyncedTeamSites"> </a>

This setting lets you convert synced SharePoint files to online-only files when you enable OneDrive Files On-Demand. If you have many PCs syncing the same team site, enabling this setting helps you minimize network traffic and local storage usage.
  
If you enable this setting, files in currently syncing team sites will be changed to online-only files by default. Files later added or updated in the team site will also be downloaded as online-only files. To use this setting, the computer must be running Windows 10 Fall Creators Update (version 1709) or later, and OneDrive Files On-Demand must be enabled.
This feature is not enabled for on-premises SharePoint sites. 

Enabling this policy sets the following registry key value to 1.
  
[HKLM\SOFTWARE\Policies\Microsoft\OneDrive]"DehydrateSyncedTeamSites"="dword:00000001"

For info about querying and setting file and folder states, see [Set Files On-Demand states](files-on-demand-mac.md).
  
### Limit the sync client upload rate to a percentage of throughput
<a name="AutomaticUploadBandwidthPercentage"> </a>

This setting lets you balance the performance of different upload tasks on a computer by specifying the percentage of the computer's upload throughput that the OneDrive sync client (OneDrive.exe) can use to upload files. Setting this as a percentage lets the sync client respond to both increases and decreases in throughput. The lower the percentage you set, the slower files will upload. We recommend a value of 50% or higher. The sync client will periodically upload without restriction for one minute and then slow down to the upload percentage you set. This lets small files upload quickly while preventing large uploads from dominating the computer’s upload throughput. We recommend enabling this setting temporarily when you roll out [Silently move Windows known folders to OneDrive](use-group-policy.md#KFMOptInNoWizard) or [Prompt users to move Windows known folders to OneDrive](use-group-policy.md#KFMOptInWithWizard) to control the network impact of uploading known folder contents.

![Upload Throughput Calculation](media/limit-upload-rate-percentage-throughput.png)
  
> [!NOTE]
> The maximum throughput value detected by the sync client can sometimes be higher or lower than expected because of the different traffic throttling mechanisms that your Internet Service Provider (ISP) might use. <br>For info about estimating the network bandwidth you need for sync, see [Network utilization planning for the OneDrive sync client](network-utilization-planning.md).
  

If you enable this setting, and enter a percentage (from 10-99) in the **Bandwidth** box, computers will use the percentage of upload throughput that you specify when uploading files to OneDrive, and users will not be able to change it.

Enabling this policy sets the following registry key value. For example:
  
[HKLM\SOFTWARE\Policies\Microsoft\OneDrive]"AutomaticUploadBandwidthPercentage"="dword:000000﻿32"
  
The above registry key sets the upload throughput percentage to 50%, using the hexadecimal value for 50, which is 00000032.
  
If you disable or do not configure this setting, users can choose to limit the upload rate to a fixed value (in KB/second), or set it to "Adjust automatically," which sets the upload rate to 70% of  throughput. For info about the end-user experience, see [Change the OneDrive sync client upload or download rate](https://support.office.com/article/71cc69da-2371-4981-8cc8-b4558bdda56e).

> [!IMPORTANT]
> If you enable or disable this setting, and then change it back to Not Configured, the last configuration will remain in effect. We recommend enabling this setting instead of "Limit the sync client upload speed to a fixed rate" to limit the upload rate. You should not enable both settings at the same time.
 
### Prevent the sync client from generating network traffic until users sign in
<a name="PreventNetworkTraffic"> </a>

This setting lets you block the OneDrive sync client (OneDrive.exe) from generating network traffic (checking for updates, etc.) until users sign in to OneDrive or start syncing files on their computer.
  
If you enable this setting, users must sign in to the OneDrive sync client on their computer, or select to sync OneDrive or SharePoint files on the computer, for the sync client to start automatically.
  
If you disable or do not configure this setting, the OneDrive sync client will start automatically when users sign in to Windows. 

> [!IMPORTANT]
> If you enable or disable this setting, and then change it back to Not Configured, the last configuration will remain in effect. 

Enabling this policy sets the following registry key value to 1.
  
[HKLM\SOFTWARE\Policies\Microsoft\OneDrive]"PreventNetworkTrafficPreUserSignIn"="dword:00000001"

### Prevent users from fetching files remotely
<a name="RemoteAccessGPOEnabled"> </a>

This setting lets you block users from using the fetch feature when they’re signed in to the OneDrive sync client (OneDrive.exe) with their personal OneDrive account. The fetch feature lets users go to OneDrive.com, select a Windows computer that's currently online and running the OneDrive sync client, and access all files from that computer. By default, users can use the fetch feature.

If you enable this setting, users will be prevented from using the fetch feature.
  
Enabling this policy sets the following registry key value to 1.
  
[HKLM\SOFTWARE\Policies\Microsoft\OneDrive\Remote Access] "GPOEnabled"="dword:00000001"
  
If you disable or do not configure both this setting and [Prevent users from syncing personal OneDrive accounts](use-group-policy.md#DisablePersonalSync), users can use the fetch feature. For more info about fetching files, see [Fetch files on your PC](https://support.office.com/article/70761550-519c-4d45-b780-5a613b2f8822).

### Prevent users from moving their Windows known folders to OneDrive
<a name="BlockKnownFolderMove"> </a>

This setting prevents users from moving their Documents, Pictures, and Desktop folders to any OneDrive for Business account.
  
> [!NOTE]
> Moving known folders to personal OneDrive accounts is already blocked on domain-joined PCs. 
  
If you enable this setting, users won't be prompted with a window to protect their important folders, and the "Start protection" command will be disabled. If the user has already moved their known folders, the files in those folders will remain in OneDrive. This setting will not take effect if you've enabled "Prompt users to move Windows known folders to OneDrive" or "Silently move Windows known folders to OneDrive."
  
If you disable or do not configure this setting, users can choose to move their known folders.
  
Enabling this policy sets the following registry key value to 1.
  
[HKLM\SOFTWARE\Policies\Microsoft\OneDrive]"KFMBlockOptIn"="dword:00000001"
  

### Prevent users from redirecting their Windows known folders to their PC
<a name="KFMBlockOptOut"> </a>

This setting forces users to keep their Documents, Pictures, and Desktop folders directed to OneDrive.

> [!NOTE]
> This setting is available in the OneDrive sync client build 18.111.0603.0004 or later. 
  
If you enable this setting, the "Stop protecting" button in the "Set up protection of important folders" window will be disabled and users will receive an error if they try to stop syncing a known folder.
  
If you disable or do not configure this setting, users can choose to redirect their known folders back to their PC.
  
Enabling this policy sets the following registry key:
  
[HKLM\SOFTWARE\Policies\Microsoft\OneDrive]"KFMBlockOptOut"="dword:00000001"

### Prompt users to move Windows known folders to OneDrive
<a name="KFMOptInWithWizard"> </a>

This setting displays the following window that prompts users to move their Documents, Pictures, and Desktop folders to OneDrive.

> [!NOTE]
> This setting is available in the OneDrive sync client build 18.111.0603.0004 or later. 
  
![Window prompting users to protect important folders](media/protect-important-folders-gpo.png)
  
If you enable this setting and provide your tenant ID, users who are syncing their OneDrive will see the window above when they're signed in. If they close the window, a reminder notification will appear in the activity center until they move all three known folders. If a user has already redirected their known folders to a different OneDrive account, they will be prompted to direct the folders to the account for your organization (leaving existing files behind).
  
If you disable or do not configure this setting, the window that prompts users to protect their important folders won't appear. 
  
Enabling this policy sets the following registry key:
  
[HKLM\SOFTWARE\Policies\Microsoft\OneDrive]"KFMOptInWithWizard"="1111-2222-3333-4444"
  
(where "1111-2222-3333-4444" is the [tenant ID](find-your-office-365-tenant-id.md))

[More info about known folder move](redirect-known-folders.md) 

### Require users to confirm large delete operations
<a name="ForcedLocalMassDeleteDetection"> </a>

This setting makes users confirm that they want to delete files in the cloud when they delete a large number of synced files.

If you enable this setting, a warning will always appear when users delete a large number of synced files. If a user does not confirm a delete operation within 7 days, the files will not be deleted.

If you disable or do not configure this setting, users can choose to hide the warning and always delete files in the cloud.

Enabling this policy sets the following registry key value to 1.
  
[HKLM\SOFTWARE\Policies\Microsoft\OneDrive]"ForcedLocalMassDeleteDetection"="dword:00000001"

### Set the maximum size of a user's OneDrive that can download automatically
<a name="DiskSpaceCheckThresholdMB"> </a>

This setting is used in conjunction with [Silently sign in users to the OneDrive sync client with their Windows credentials](use-group-policy.md#SilentAccountConfig) on devices that don't have OneDrive Files On-Demand enabled. Any user who has a OneDrive that's larger than the specified threshold (in MB) will be prompted to choose the folders they want to sync before the OneDrive sync client (OneDrive.exe) downloads the files.
  
In the **Options** box, click **Show** to enter the tenant ID and the maximum size in MB (from 0 to 4294967295). The default value is 500. 
  
Enabling this policy sets the following registry key.
  
[HKLM\SOFTWARE\Policies\Microsoft\OneDrive\DiskSpaceCheckThresholdMB]"1111-2222-3333-4444"=dword:0005000
  
(where "1111-2222-3333-4444" is the [tenant ID](find-your-office-365-tenant-id.md) and 0005000 sets a threshold of 5000 MB) 
  
### Set the sync client update ring
<a name="GPOSetUpdateRing"> </a>

We release OneDrive sync client (OneDrive.exe) updates to the public through three rings- first to Insiders, then Production, and finally Enterprise. This setting lets you specify the ring for users in your organization. When you enable this setting and select a ring, users won't be able to change it.

Insiders ring users will receive builds that let them preview new features coming to OneDrive.

Production ring users will get the latest features as they become available. This ring is the default.

Enterprise ring users get new features, bug fixes, and performance improvements last. This ring lets you deploy updates from an internal network location and control the timing of the deployment (within a 60-day window).

If you disable or do not configure this setting, users can join the [Windows Insider program](https://insider.windows.com/) or the [Office Insider](https://products.office.com/office-insider) program to get updates on the Insiders ring.

Enabling this policy sets the following registry key: 
 
[HKLM\SOFTWARE\Policies\Microsoft\OneDrive]"GPOSetUpdateRing"="dword:0000000X"

Set the value 4 for Insider, 5 for Production, or 0 for Enterprise. Note that when you configure this setting to 5 for Production, or 0 for Enterprise, the "Get OneDrive Insider preview updates before release" checkbox will not appear on the client Settings > About tab.
  
For more info on the builds currently available in each ring, see the [release notes](https://support.office.com/article/845dcf18-f921-435e-bf28-4e24b95e5fc0?). For more info about the update rings and how the sync client checks for updates, see [The OneDrive sync client update process](sync-client-update-process.md).

### Silently move Windows known folders to OneDrive
<a name="KFMOptInNoWizard"> </a>

Use this setting to redirect your users' Documents, Pictures, and Desktop folders to OneDrive without any user interaction. This setting is available in the OneDrive sync client build 18.111.0603.0004 or later. Before sync client build 18.171.0823.0001, this setting redirected only empty known folders to OneDrive. Now, it redirects known folders that contain content and moves the content to OneDrive.

> [!NOTE]
> If you're using this setting with a build earlier than 18.171.0823.0001, we recommend also enabling [Prompt users to move Windows known folders to OneDrive](use-group-policy.md#KFMOptInWithWizard). 
  
If you enable this setting and provide your tenant ID, you can choose whether to display a notification to users after their folders have been redirected.
  
![OneDrive protection message](media/d28dbca8-f51a-43b2-b069-c483a53c6d0b.png)
  
If you disable or do not configure this setting, your users' known folders will not be silently redirected to OneDrive. 
  
Enabling this policy sets the following registry keys:
  
[HKLM\SOFTWARE\Policies\Microsoft\OneDrive]"KFMSilentOptIn"="1111-2222-3333-4444"
  
(where "1111-2222-3333-4444" is the [tenant ID](find-your-office-365-tenant-id.md))
  
[HKLM\SOFTWARE\Policies\Microsoft\OneDrive]"KFMSilentOptInWithNotification"
  
Setting this value to 1 displays a notification after successful redirection.

[More info about known folder move](redirect-known-folders.md) 
  
### Silently sign in users to the OneDrive sync client with their Windows credentials
<a name="SilentAccountConfig"> </a>

> [!IMPORTANT]
> ADAL is now enabled automatically when you enable this setting through Group Policy or by using the registry key, so you don't have to download and enable it separately.
  
If you enable this setting, users who are signed in on a PC that's joined to Azure AD can set up the sync client without entering their account credentials. Users will still be shown OneDrive Setup so they can select folders to sync and change the location of their OneDrive folder. If a user is using the previous OneDrive for Business sync client (Groove.exe), the new sync client will attempt to take over syncing the user's OneDrive from the previous client and preserve the user's sync settings. This setting is frequently used together with [Set the maximum size of a user's OneDrive that can download automatically](use-group-policy.md#DiskSpaceCheckThresholdMB) on PCs that don't have Files On-Demand, and with [Set the default location for the OneDrive folder](use-group-policy.md#DefaultRootDir).

Enabling this policy sets the following registry key value to 1.
  
[HKLM\SOFTWARE\Policies\Microsoft\OneDrive]"SilentAccountConfig"="dword:00000001"
  
For more info about this feature, see [Silently configure user accounts](use-silent-account-configuration.md).
Please let us know if you have feedback on this feature or encounter any issues. Right-click the OneDrive icon in the notification area and click "Report a problem." Please tag any feedback with "SilentConfig" so that your feedback will be sent directly to engineers working on this feature.

### Use OneDrive Files On-Demand
<a name="FilesOnDemandEnabled"> </a>

This setting lets you control whether OneDrive Files On-Demand is enabled for your organization. Files On-Demand helps you save storage space on your users' computers and minimize the network impact of sync. The feature is available to users running Windows 10 Fall Creators update (version 1709 or later). [Learn about OneDrive Files On-Demand](https://support.office.com/article/0e6860d3-d9f3-4971-b321-7092438fb38e).
  
If you enable this setting, new users who set up the sync client will download online-only files by default. If you disable this setting, Windows 10 users will have the same sync behavior as users of previous versions of Windows, and won't be able to turn on Files On-Demand. If you do not configure this setting, users can turn Files On-Demand on or off. 

Enabling this policy sets the following registry key value to 1.
  
[HKLM\SOFTWARE\Policies\Microsoft\OneDrive]"FilesOnDemandEnabled"="dword:00000001"
 
Meet Windows and OneDrive sync client requirements and still can't see Files On-Demand option available at "Settings"? Make sure service "Windows Cloud Files Filter Driver" start type is set to 2 (AUTO_START). Enabling this feature sets the following registry key value to 2.

[HKLM\SYSTEM\CurrentControlSet\Services\CldFlt]"Start"="dword:00000002"

### Prevent users from syncing libraries and folders shared from other organizations
<a name="BlockExternalSync"> </a>

The B2B Sync feature of the OneDrive sync client allows users at an organization to sync OneDrive for Business and SharePoint libraries and folders shared with them from another organization. [Learn about OneDrive B2B Sync](b2b-sync.md).

Enabling this setting will prevent users at your organization from being able to use B2B Sync. Once the setting is enabled (value 1) on a computer, the sync client will not sync libraries and folders shared from other organizations. Modify the setting to the disabled state (value 0) in order to restore B2B Sync capability for your users.

prevent B2B Sync with:
[HKLM\SOFTWARE\Policies\Microsoft\OneDrive] "BlockExternalSync"="dword:1"

restore B2B Sync with:
[HKLM\SOFTWARE\Policies\Microsoft\OneDrive] "BlockExternalSync"="dword:0"

## User Configuration policies
<a name="Glob"> </a>

User Configuration policies can be found under User Configuration\Policies\Administrative Templates\OneDrive.
  
![OneDrive settings in Group Policy Management Editor](media/8e121823-b5bf-440c-999d-c2a9ada4705d.png)
  
### Allow users to choose how to handle Office file sync conflicts
<a name="EnableHoldTheFile"> </a>

This setting specifies what happens when conflicts occur between Office file versions during sync. By default, users can decide if they want to merge changes or keep both copies. Users can also change settings in the OneDrive sync client to always keep both copies. (This option is available for Office 2016 or later only. With earlier versions of Office, both copies are always kept.) 

  
If you enable this setting, users can decide if they want to merge changes or keep both copies. Users can also configure the sync client to always fork the file and keep both copies as shown below.
  
![The Office tab of the Sync settings dialog box](media/ec60b062-1979-446d-b431-bf0baede0f8b.png)
  
Enabling this policy sets the following registry key value to 1.
  
[HKCU\SOFTWARE\Policies\Microsoft\OneDrive] ﻿"EnableHoldTheFile"="dword:00000001"

If you disable this setting, the Sync conflicts setting on the Office tab will be disabled and when a sync conflict occurs, both copies of the file will be kept. 
  
You must enable [Coauthor and share in Office desktop apps](use-group-policy.md#EnableAllOcsiClients) to enable this setting. For more info about the Office settings in the sync client, see [Use Office 2016 to sync Office files that I open](https://support.office.com/article/8a409b0c-ebe1-4bfa-a08e-998389a9d823).
  
  
### Continue syncing on metered networks
<a name="DisablePauseOnMeteredNetwork"> </a>

This setting lets you turn off the auto-pause feature when devices connect to metered networks. 

If you enable this setting, syncing will continue when devices are on a metered network. OneDrive will not automatically pause syncing. 

If you disable or do not configure this setting, syncing will pause automatically when a metered network is detected and a notification will be displayed. Users can choose not to pause by clicking "Sync Anyway" in the notification. When syncing is paused, users can resume syncing by clicking the OneDrive cloud icon in the notification area of the taskbar and then clicking the alert at the top of the activity center.

Enabling this policy sets the following registry key value to 1.

[HKCU\SOFTWARE\Policies\Microsoft\OneDrive] "DisablePauseOnMeteredNetwork"=dword:00000001
  
### Continue syncing when devices have battery saver mode turned on
<a name="DisablePauseOnBatterySaver"> </a>

This setting lets you turn off the auto-pause feature for devices that have battery saver mode turned on.  

If you enable this setting, syncing will continue when users turn on battery saver mode. OneDrive will not automatically pause syncing. 

If you disable or do not configure this setting, syncing will pause automatically when battery saver mode is detected and a notification will be displayed. Users can choose not to pause by clicking "Sync Anyway" in the notification. When syncing is paused, users can resume syncing by clicking the OneDrive cloud icon in the notification area of the taskbar and then clicking the alert at the top of the activity center.

Enabling this policy sets the following registry key value to 1.

[HKCU\SOFTWARE\Policies\Microsoft\OneDrive] "DisablePauseOnBatterySaver"=dword:00000001

### Coauthor and share in Office desktop apps
<a name="EnableAllOcsiClients"> </a>

This setting lets multiple users use the Office 365 ProPlus, Office 2019, or Office 2016 desktop apps to simultaneously edit an Office file stored in OneDrive. It also lets users share files from the Office desktop apps.
  
If you enable this setting, the Office tab will appear in OneDrive sync settings, and "Use Office 2016 to sync Office files that I open" will be selected by default.
  
![The Office tab in OneDrive sync client settings](media/c90cf228-c27e-4107-b4cf-2c0690a959a4.png)

Enabling this policy sets the following registry key value to 1:
  
[HKCU\SOFTWARE\Policies\Microsoft\OneDrive] ﻿"EnableAllOcsiClients"="dword:00000001"
  
If you disable this setting, the **Office** tab is hidden in the sync client, and coauthoring and in-app sharing for Office files is disabled. The **Users can choose how to handle Office files in conflict** setting will act as disabled and when file conflicts occur, both copies of the file will be kept. For more info about the settings in the sync client, see [Use Office 2016 to sync Office files that I open](https://support.office.com/article/8a409b0c-ebe1-4bfa-a08e-998389a9d823).

### Configure team site libraries to sync automatically
<a name="AutoMountTeamSites"> </a> 

This setting allows you to specify SharePoint team site libraries to sync automatically the next time users sign in to the OneDrive sync client (OneDrive.exe), within an eight-hour window, to help distribute network load. To use this setting, the computer must be running Windows 10 Fall Creators Update (version 1709) or later, and OneDrive Files On-Demand must be enabled.
This feature is not enabled for on-premises SharePoint sites. 

> [!IMPORTANT]
> Do not enable this setting for libraries with more than 5,000 files or folders.
> Do not enable this setting for the same library to more than 1,000 devices.

If you enable this setting, the OneDrive sync client will automatically sync the contents of the libraries you specified as online-only files the next time the user signs in. The user won't be able to stop syncing the libraries.  

If you disable this setting, team site libraries that you've specified won't be automatically synced for new users. Existing users can choose to stop syncing the libraries, but the libraries won't stop syncing automatically. 

To configure the setting, in the Options box, click **Show**, and then enter a friendly name to identify the library in the **Value Name** field and the entire library ID (tenantId=xxx&siteId=xxx&webId=xxx&listId=xxx&webUrl=httpsxxx&version=1) in the **Value** field. 

To find the library ID, sign in as a global or SharePoint admin in Office 365, browse to the library, and click the **Sync** button. In the "Starting sync" dialog box, click the **Copy library ID** link.

![The Getting ready to sync dialog box](media/copy-library-id.png)

Enabling this policy sets the following registry key, using the entire URL from the library you copied:

[HKCU\Software\Policies\Microsoft\OneDrive\TenantAutoMount]"LibraryName"="LibraryID" 



### Disable the tutorial that appears at the end of OneDrive Setup
<a name="DisableFRETutorial"> </a>

This setting lets you prevent the tutorial from launching in a web browser at the end of OneDrive Setup.

If you enable this setting, users will not see the tutorial after they complete OneDrive Setup. 
  
Enabling this policy sets the following registry key value to 1.
  
[HKCU\SOFTWARE\Policies\Microsoft\OneDrive] "DisableTutorial"="dword:00000001"

### Limit the sync client download speed to a fixed rate
<a name="DownloadBandwidthLimit"> </a>

This setting lets you configure the maximum speed at which the OneDrive sync client (OneDrive.exe) can download files. This rate is a fixed value in kilobytes per second, and applies only to syncing, not to downloading updates. The lower the rate, the slower files will download. 

We recommend that you use this setting in cases where Files On-Demand is NOT enabled and where strict traffic restrictions are required, such as when you initially deploy the sync client in your organization or enable syncing of team sites. We don't recommend that you use this setting on an ongoing basis because it will decrease sync client performance and negatively impact the user experience. After initial sync, users typically sync only a few files at a time, and it doesn't have a significant effect on network performance. If you enable this setting, computers will use the maximum download rate that you specify, and users will not be able to change it.

If you enable this setting, enter the rate (from 1 to 100000) in the **Bandwidth** box. The maximum rate is 100000 KB/s. Any input lower than 50 KB/s will set the limit to 50 KB/s, even if the UI shows a lower value.

If you disable or do not configure this setting, the download rate is unlimited and users can choose to limit it in OneDrive sync client settings. For info about the end-user experience, see [Change the OneDrive sync client upload or download rate](https://support.office.com/article/71cc69da-2371-4981-8cc8-b4558bdda56e).

   
Enabling this policy sets the following registry key value to a number from 50 through 100,000. For example:
  
[HKCU\SOFTWARE\Policies\Microsoft\OneDrive] "DownloadBandwidthLimit"="dword:000000﻿32"
  
The above registry key sets the download throughput rate limit to 50KB/sec, using the hexadecimal value for 50, which is 00000032.

> [!NOTE]
> OneDrive.exe must be restarted on users' computers to apply this setting. 
  
For info about estimating the network bandwidth you need for sync, see [Network utilization planning for the OneDrive sync client](network-utilization-planning.md).
 
### Limit the sync client upload speed to a fixed rate
<a name="UploadBandwidthLimit"> </a>

This setting lets you configure the maximum speed at which the OneDrive sync client (OneDrive.exe) can upload files. This rate is a fixed value in kilobytes per second. The lower the rate, the slower the computer will upload files. 

If you enable this setting and enter the rate (from 1 to 100000) in the **Bandwidth** box, computers will use the maximum upload rate that you specify, and users will not be able to change it in OneDrive settings. The maximum rate is 100000 KB/s. Any input lower than 50 KB/s will set the limit to 50 KB/s, even if the UI shows a lower value. 

If you disable or do not configure this setting, users can choose to limit the upload rate to a fixed value (in KB/second), or set it to "Adjust automatically" which sets the upload rate to 70% of  throughput. For info about the end-user experience, see [Change the OneDrive sync client upload or download rate](https://support.office.com/article/71cc69da-2371-4981-8cc8-b4558bdda56e).

We recommend that you use this setting only used in cases where strict traffic restrictions are required. In scenarios where you need to limit the upload rate (such as when you roll out Known Folder Move), we recommend enabling [Limit the sync client upload rate to a percentage of throughput](use-group-policy.md#AutomaticUploadBandwidthPercentage) to set a limit that adjusts to changing conditions. You should not enable both settings at the same time.

Enabling this policy sets the following registry key value to a number from 50 through 100,000. For example:
  
[HKCU\SOFTWARE\Policies\Microsoft\OneDrive]"UploadBandwidthLimit"="dword:000000﻿32"
  
The above registry key sets the upload throughput rate limit to 50KB/sec, using the hexadecimal value for 50, which is 00000032.

> [!NOTE]
> OneDrive.exe must be restarted on users' computers to apply this setting.  
  
For info about estimating the network bandwidth you need for sync, see [Network utilization planning for the OneDrive sync client](network-utilization-planning.md).
  
    
### Prevent users from changing the location of their OneDrive folder
<a name="DisableCustomRoot"> </a>

This setting lets you block users from changing the location of the OneDrive folder on their computer.
  
To use this setting, in the **Options** box, click **Show** to enter your [tenant ID](find-your-office-365-tenant-id.md), and enter 1 to enable the setting or 0 to disable it. 
  
If you enable this setting, the “Change location” link is hidden in OneDrive Setup. The OneDrive folder will be created in the default location, or in the custom location you specified if you enabled [Set the default location for the OneDrive folder](use-group-policy.md#DefaultRootDir).
  
Enabling this policy sets the following registry key value to 1.
 [HKCU\Software\Policies\Microsoft\OneDrive\DisableCustomRoot] "1111-2222-3333-4444"="dword:00000001"
  
(where "1111-2222-3333-4444" is the tenant ID)
  
If you disable this setting, users can change the location of their sync folder in OneDrive Setup.

  
### Prevent users from syncing personal OneDrive accounts
<a name="DisablePersonalSync"> </a>

This setting lets you block users from signing in with a Microsoft account to sync their personal OneDrive files. By default, users are allowed to sync personal OneDrive accounts. 
  
If you enable this setting, users will be prevented from setting up a sync relationship for their personal OneDrive account. Users who are already syncing their personal OneDrive when you enable this setting won’t be able to continue syncing (and will be shown a message that syncing has stopped), but any files synced to the computer will remain on the computer.
 
Enabling this policy sets the following registry key value to 1.
  
[HKCU\SOFTWARE\Policies\Microsoft\OneDrive]"DisablePersonalSync"="dword:00000001" 

### Receive OneDrive sync client updates on the Enterprise ring
<a name="EnableEnterpriseUpdate"> </a>

This setting lets you specify the Enterprise ring for users in your organization. We release OneDrive sync client (OneDrive.exe) updates to the public through three rings— first to Insiders, then Production, and finally Enterprise.

Selecting the Enterprise ring gives you some extra time to prepare for updates, but means users will need to wait to receive the latest improvements. The Enterprise ring also lets you deploy updates from an internal network location on your own schedule.

Enabling this policy sets the following registry key value to 1:
  
[HKCU\SOFTWARE\Policies\Microsoft\OneDrive] ﻿"EnableEnterpriseUpdate"="dword:00000001"
  
> [!IMPORTANT]
> This setting will be removed soon. We recommend using the new setting [Set the sync client update ring](use-group-policy.md#GPOSetUpdateRing) instead.
  
For more info about the update rings and how the sync client checks for updates, see [The OneDrive sync client update process](sync-client-update-process.md).

### Set the default location for the OneDrive folder
<a name="DefaultRootDir"> </a>

This setting lets you set a specific path as the default location of the OneDrive folder on users' computers. By default, the path is under %userprofile%.
  
If you enable this setting, the default location of the OneDrive - {organization name} folder will be the path that you specify. Click **Show** in the **Options** box to specify your tenant ID and the path. 
  
This policy sets the following registry key to a string that specifies the file path.
  
[HKCU\SOFTWARE\Policies\Microsoft\OneDrive\DefaultRootDir] "1111-2222-3333-4444"="{User path}"
  
(where "1111-2222-3333-4444" is the tenant ID)
  
If you disable this setting, the local  *OneDrive - {organization name}*  folder location will default to %userprofile%. 
  
> [!NOTE]
> The %logonuser% environment variable won't work through Group Policy. We recommend you use %username% instead. 
  
## See also
<a name="Glob"> </a>

[Deploy the new OneDrive sync client in an enterprise environment ](deploy-on-windows.md)
  
[Prevent users from installing the sync client](prevent-installation.md)
  
[Allow syncing only on computers joined to specific domains ](allow-syncing-only-on-specific-domains.md)
  
[Block syncing of specific file types ](block-file-types.md)

[Deploy and configure the new OneDrive sync client for Mac](deploy-and-configure-on-macos.md)
