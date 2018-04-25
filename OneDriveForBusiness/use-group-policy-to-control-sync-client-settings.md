---
title: "Use Group Policy to control OneDrive sync client settings"
ms.author: kaarins
author: kaarins
manager: pamgreen
ms.date: 4/10/2018
ms.audience: Admin
ms.topic: article
ms.prod: office-online-server
localization_priority: Normal
ms.collection: Strat_OD_admin
search.appverid:
- ODB160
- MOE150
- MED150
- MBS150
- ODB150
ms.assetid: 0ecb2cf5-8882-42b3-a6e9-be6bda30899c
description: "Learn how to use group policy to administer settings for the OneDrive sync client."
---

# Use Group Policy to control OneDrive sync client settings

 *Last updated: April 2018* 
  
This article is for IT admins managing the OneDrive sync client in a Windows Server enterprise environment that uses Active Directory Domain Services (AD DS).
  
> [!NOTE]
> If you're not an IT admin, see [Sync files with the new OneDrive sync client in Windows](https://support.office.com/article/615391c4-2bd3-4aae-a42a-858262e42a49) for info about OneDrive sync settings. 
  
## Manage OneDrive using Group Policy

1. Install the latest OneDrive sync client on a PC running Windows 10. This downloads the .adml and .admx files.
    
2. Browse to **%localappdata%\Microsoft\OneDrive\ *BuildNumber*  \adm\ **, to the subfolder for your language as necessary. 
    
    (Where  *BuildNumber*  is the number displayed in sync client settings on the About tab.) 
    ![The ADM folder in the OneDrive installation directory](media/85e0fe3f-84eb-4a29-877f-c706dda4d075.png)
  
3. Copy the .adml and .admx files and paste them in your domain's Central Store, \\ *domain*  \sysvol\domain\Policies\PolicyDefinition, (where  *domain*  is your domain name, such as corp.contoso.com), in the corresponding language folder. 
    
4. Configure settings from the domain controller or on a Windows computer by running the [Remote Server Administration Tools](https://go.microsoft.com/fwlink/?linkid=871794). For info about applying policies to different parts of your organization, see [Link Group Policy objects to Active Directory containers](https://go.microsoft.com/fwlink/?linkid=871796).
    
The OneDrive Group Policy objects work by setting registry keys on the computers in your domain.
  
- When you enable or disable a policy, the corresponding registry key is updated on computers in your domain. If you later set the policy back to **Not configured**, the corresponding registry key is not modified and the effective policy setting does not change. So after you configure a policy, use the **Enabled** and **Disabled** settings for that policy going forward. 
    
- The location where registry keys are written has been updated. When you use the latest files, you might delete registry keys that you set previously.
    
## Computer Configuration policies
<a name="PerTen"> </a>

Computer Configuration policies can be found under Computer Configuration\Policies\Administrative Templates\OneDrive.
  
![Computer Configuration policies in the Group Policy Management Editor](media/07b81d35-9ccc-4c61-8a86-52d9bcff7ddb.png)
  
The following Computer Configuration policies are available:
  
- [Allow syncing OneDrive accounts for only specific organizations](use-group-policy-to-control-sync-client-settings.md#TenantAllowList)
    
- [Block syncing OneDrive accounts for specific organizations](use-group-policy-to-control-sync-client-settings.md#TenantBlockList)
    
- [Enable OneDrive Files On-Demand](use-group-policy-to-control-sync-client-settings.md#FilesOnDemand)
    
- [Migrate pre-existing team sites with OneDrive Files On-Demand](use-group-policy-to-control-sync-client-settings.md#TeamSiteFOD)
    
- [Prevent OneDrive from generating network traffic until the user signs in to OneDrive](use-group-policy-to-control-sync-client-settings.md#PreventNetworkTraffic)
    
- [Set the maximum percentage of upload bandwidth that OneDrive.exe uses](use-group-policy-to-control-sync-client-settings.md#MaxBandwidth)
    
- [Silently configure OneDrive using Windows 10 or domain credentials](use-group-policy-to-control-sync-client-settings.md#SilentConfig)
    
- [(Preview) Configure the maximum OneDrive size for downloading all files automatically](use-group-policy-to-control-sync-client-settings.md#MaxOneDriveSize)
    
### Allow syncing OneDrive accounts for only specific organizations
<a name="TenantAllowList"> </a>

This policy lets you allow users to sync OneDrive accounts for only some organizations by specifying a list of allowed tenant IDs. If you enable this setting, users will get an error if they attempt to add an account from an organization not on the list. If a user has already the account, the files will stop syncing.
  
[HKLM\SOFTWARE\Policies\Microsoft\OneDrive\AllowTenantList] "1111-2222-3333-4444"﻿
  
(where "1111-2222-3333-4444" is the Tenant ID)
  
To block specific organizations instead, use "Block syncing OneDrive accounts for specific organizations."
  
This setting will take priority over the policy "Block syncing OneDrive accounts for specific organizations." Do not enable both policies at the same time.﻿
  
### Block syncing OneDrive accounts for specific organizations
<a name="TenantBlockList"> </a>

This policy lets you block users from uploading files to another organization by specifying a list of blocked tenant IDs. If you enable this setting, users will get an error if they attempt to add an account from an organization that is blocked. If a user has already added the account, the files will stop syncing.
  
[HKLM\SOFTWARE\Policies\Microsoft\OneDrive\BlockTenantList] "1111-2222-3333-4444"﻿
  
(where "1111-2222-3333-4444" is the Tenant ID)
  
To specify a list of allowed organizations instead, use "Allow syncing OneDrive accounts for only specific organizations."
  
This setting will NOT work if you have the policy "Allow syncing OneDrive accounts for only specific organizations." enabled. Do not enable both policies at the same time.
  
### Enable OneDrive Files On-Demand
<a name="FilesOnDemand"> </a>

This policy lets you control whether OneDrive Files On-Demand is enabled for your organization. Files On-Demand helps you save storage space on your users' computers and minimize the network impact of sync. The feature is available to users running Windows 10 Fall Creators update. [Learn about OneDrive Files On-Demand](https://support.office.com/article/0e6860d3-d9f3-4971-b321-7092438fb38e).
  
If you enable this setting, new users who set up the sync client will download online-only files by default. If you disable this setting, Windows 10 users will have the same sync behavior as users of previous versions of Windows, and won't be able to turn on OneDrive Files On-Demand. If you do not configure this setting, OneDrive Files On-Demand can be turned on or off by users.﻿
  
### Migrate pre-existing team sites with OneDrive Files On-Demand
<a name="TeamSiteFOD"> </a>

This policy lets you convert synced SharePoint files to online-only files when you enable OneDrive Files On-Demand. Enabling this policy helps you minimize network traffic and local storage usage if you have many PCs syncing the same team site.
  
If you enable this policy, files in currently syncing team sites will be changed to online-only files by default. Files later added or updated in the team site will also be downloaded as online-only files.
  
### Prevent OneDrive from generating network traffic until the user signs in to OneDrive
<a name="PreventNetworkTraffic"> </a>

This policy lets you prevent the OneDrive sync client (OneDrive.exe) from generating network traffic (checking for updates, etc.) until the user signs in to OneDrive or starts syncing files to the local computer.
  
If you enable this setting, users must sign in to the OneDrive sync client on the local computer, or select to sync OneDrive or SharePoint files on the computer, for the sync client to start automatically.
  
If this setting is not enabled, the OneDrive sync client will start automatically when users sign in to Windows. If you enable or disable this setting, do not return the setting to Not Configured. Doing so will not change the configuration and the last configured setting will remain in effect.
  
### Set the maximum percentage of upload bandwidth that OneDrive.exe uses
<a name="MaxBandwidth"> </a>

This policy lets you configure the maximum percentage of a computer's available upload throughput that the OneDrive sync client can use to upload. (OneDrive only uses this bandwidth when syncing files.) The bandwidth available to a computer is constantly changing, so defining a percentage lets the sync client respond to increases and decreases in bandwidth availability while syncing in the background.
  
If you enable this setting, as a file is being uploaded, the OneDrive sync client measures how much content is being uploaded and how long it takes for a period of 60 seconds to identify the maximum upload throughput to the service at that time. Maximum upload throughput is based on the peak observed throughput value during the measurement interval.
  
![Upload Throughput Calculation](media/4cf2e62a-7eb4-4107-92ce-fbc219816b9d.jpg)
  
Note: The obtained maximum throughput value can sometimes be higher or lower than expected because of the different traffic throttling mechanisms that your Internet Service Provider (ISP) might use.
  
This calculated value is then multiplied by the percentage you define in this setting and is used as the throughput cap for the next 10 minutes. After 10 minutes, the sync client will perform another 60-second measurement and readjust based on the results of the new maximum upload throughput value for that measurement period. Upload throughput is not throttled during the 60-second measurement interval and allows files to be uploaded at the maximum available throughput. This enables two key scenarios. First, a very small file will get uploaded quickly because it can fit in the interval where the sync client is measuring the maximum possible speed. Second, for any long running upload, sync will keep optimizing the upload speed per the percentage value set by this setting.
  
Enabling this policy sets the following registry key value to a number from 10 through 99. For example:
  
[HKLM\SOFTWARE\Microsoft\OneDrive] "AutomaticUploadBandwidthPercentage"=dword:000000﻿32
  
The above registry key sets the upload throughput percentage to 50%, using the hexadecimal value for 50, which is 00000032.
  
The lower the percentage you set, the longer it will take the sync client to upload files. We recommend a value of 50% or higher. The default maximum percentage is 99%. If you enable this setting, users will not be able to change the upload rate by opening sync client settings and clicking the Network tab.
  
For info about estimating the network bandwidth you need for the sync client and controlling sync throughput, see [Network utilization planning for the OneDrive sync client](network-utilization-planning.md).
  
### Silently configure OneDrive using Windows 10 or domain credentials
<a name="SilentConfig"> </a>

Important: if you enable this setting, ADAL must be enabled or the account configuration will fail. Download and open [EnableADAL.reg](https://aka.ms/EnableADAL) to enable ADAL and restart the sync client. 
  
This policy lets you configure the OneDrive sync client silently using the primary Windows account on Windows 10, and domain credentials on Windows 7 and later.
  
If you enable this setting, OneDrive.exe will attempt to sign in to the work or school account using these credentials. It will check the available disk space before syncing, and if it is large, OneDrive will prompt the user to choose their folders. The threshold for which the user is prompted can be configured using DiskSpaceCheckThresholdMB. OneDrive will attempt to sign in on every account on the computer and once successful, that account will no longer attempt silent configuration.
  
If you enable this setting and the user is using the previous OneDrive for Business sync client, the new sync client will attempt to take over syncing. The new sync client will attempt to import the user's sync settings from the previous sync client.
  
If you disable this setting, OneDrive will not attempt to automatically sign in users.
  
[HKLM\SOFTWARE\Policies\Microsoft\OneDrive]
  
﻿"SilentAccountConfig"=dword:00000001
  
This policy can be used with DiskSpaceCheckThresholdMB as well as DefaultRootDir.
  
Please let us know if you have feedback on this feature or encounter any issues. Right-click the OneDrive icon in the notification area and click "Report a problem." Please tag any feedback with "SilentConfig" so that your feedback will be sent directly to engineers working on this feature.
  
### (Preview) Configure the maximum OneDrive size for downloading all files automatically
<a name="MaxOneDriveSize"> </a>

This setting is used in conjunction with SilentAccountConfig. Any user who has a OneDrive that's larger than the specified threshold (in MB) will be prompted to choose the folders they would like to sync before the OneDrive sync client (OneDrive.exe) downloads the files.
  
[HKLM\SOFTWARE\Policies\Microsoft\OneDrive\DiskSpaceCheckThresholdMB]
  
Example: ﻿"1111-2222-3333-4444" = dword:0005000
  
(where "1111-2222-3333-4444" is the Tenant ID and 0005000 sets a threshold of 5000MB)
  
## User Configuration policies
<a name="Glob"> </a>

User Configuration policies can be found under User Configuration\Policies\Administrative Templates\OneDrive.
  
![OneDrive settings in Group Policy Management Editor](media/8e121823-b5bf-440c-999d-c2a9ada4705d.png)
  
The following User Configuration policies are available:
  
- [Set the default location for the OneDrive folder](use-group-policy-to-control-sync-client-settings.md#DefaultRootDir)
    
- [Prevent users from changing the location of their OneDrive folder](use-group-policy-to-control-sync-client-settings.md#DisableCustomRoot)
    
- [Prevent users from synchronizing personal OneDrive accounts](use-group-policy-to-control-sync-client-settings.md#DisablePersonalSync)
    
- [Set the maximum download throughput that OneDrive.exe uses](use-group-policy-to-control-sync-client-settings.md#SetMaxDownloadTput)
    
- [Coauthoring and in-app sharing for Office files](use-group-policy-to-control-sync-client-settings.md#EnableAllOcsiClients)
    
- [Delay updating OneDrive.exe until the second release wave](use-group-policy-to-control-sync-client-settings.md#EnableEnterpriseUpdate)
    
- [Users can choose how to handle Office files in conflict](use-group-policy-to-control-sync-client-settings.md#EnableHoldTheFile)
    
- [Prevent users from using the remote file fetch feature to access files on the computer](use-group-policy-to-control-sync-client-settings.md#RemoteAccessGPOEnabled)
    
- [Set the maximum upload throughput that OneDrive.exe uses](use-group-policy-to-control-sync-client-settings.md#SetMaxUploadTput)
    
### Set the default location for the OneDrive folder
<a name="DefaultRootDir"> </a>

This policy lets you set a specific path as the default location of the OneDrive folder when users go through the Welcome to OneDrive wizard to set up the sync client. By default, the path is under %userprofile%.
  
To use this policy, you must specify your [tenant ID](https://support.office.com/article/6891b561-a52d-4ade-9f39-b492285e2c9b) and the desired default path in Group Policy Editor. This policy sets the following registry key to a string that specifies the file path. 
  
[HKCU\SOFTWARE\Microsoft\OneDrive\DefaultRootDir] ﻿"{Tenant ID}"="{User path}"
  
If you enable this setting, the local  *OneDrive - \<tenant name\>*  folder location will default to the path that you specify in the OneDrive ADMX file. 
  
If you disable this setting, the local  *OneDrive - \<tenant name\>*  folder location will default to %userprofile%. 
  
If you need to apply this setting to more than one tenant, enter the additional tenant IDs to the desired default path entries in Group Policy Editor.
  
Note: The %logonuser% environment variable won't work through Group Policy. We recommend you use %username% instead.
  
### Prevent users from changing the location of their OneDrive folder
<a name="DisableCustomRoot"> </a>

This policy lets you prevent users from changing the location of the OneDrive folder on their computer.
  
To use this policy, you must enter your [tenant ID](https://support.office.com/article/6891b561-a52d-4ade-9f39-b492285e2c9b) and desired path in Group Policy Editor.﻿ Enabling this policy sets the following registry key value to 1. 
  
[HKCU\Software\Policies\Microsoft\OneDrive\DisableCustomRoot] "{Tenant ID}"=dword:00000001
  
If you enable this setting, users cannot change the location of their "OneDrive - {tenant name}" folder during the Welcome to OneDrive wizard. This forces users to use either the default location, or, if you've set the **Set the default location for the OneDrive folder** setting, ensures all users have their local OneDrive folder in the location that you've specified. 
  
If you disable this setting, users can change the location of their sync folder during the Welcome to OneDrive wizard.
  
For more info about using this policy as part of redirecting Windows known folders (such as the Documents folder) to OneDrive, see [Redirect known folders to OneDrive for Business](redirect-windows-known-folders.md).
  
### Prevent users from synchronizing personal OneDrive accounts
<a name="DisablePersonalSync"> </a>

This policy lets you block users from syncing personal files to the OneDrive storage space they get with a Microsoft account. By default, users are allowed to sync personal OneDrive accounts. Enabling this policy sets the following registry key value to 1.
  
[HKCU\SOFTWARE\Microsoft\OneDrive] ﻿"DisablePersonalSync"=dword:00000001
  
If you enable this setting, users will be prevented from setting up a sync relationship for their personal OneDrive account. If they had previously been syncing a personal OneDrive account, they are shown an error when they start the sync client, but their files remain on the computer.
  
If you disable this setting, users are allowed to sync personal OneDrive accounts.
  
### Set the maximum upload throughput that OneDrive.exe uses
<a name="SetMaxUploadTput"> </a>

This policy lets you set the maximum upload throughput rate in kilobytes (KB)/sec for computers running the OneDrive sync client. The minimum rate is 50 KB/sec and the maximum rate is 100,000 KB/sec. The lower the upload throughput rate that you configure, the longer computers running OneDrive.exe will take to upload files. 
  
By default, the upload throughput rate is unlimited and can be configured by the user directly in the sync client. If you enable this setting, computers affected by this policy will use the maximum upload throughput rate that you specify and the users will not be able to change upload rate in sync client settings themselves. Note that OneDrive.exe has to be restarted on users' devices to apply the configuration specified in this setting. If you disable this setting, users can configure the maximum upload rate for their computer by opening sync client settings and clicking the Network tab. 
  
We recommend that you use this setting only used in cases where strict traffic restrictions are required, such as when you initially deploy the sync client in your organization. We don't recommend that you use this setting on an ongoing basis because it will decrease sync client performance and negatively impact the user experience. 
  
Enabling this policy sets the following registry key value to a number from 50 through 100,000. For example:
  
[HKCU\SOFTWARE\Policies\Microsoft\OneDrive] "UploadBandwidthLimit"=dword:000000﻿32
  
The above registry key sets the upload throughput rate limit to 50KB/sec, using the hexadecimal value for 50, which is 00000032.
  
For info about estimating the network bandwidth you need for the sync client and controlling sync throughput, see [Network utilization planning for the OneDrive sync client](network-utilization-planning.md).
  
### Coauthoring and in-app sharing for Office files
<a name="EnableAllOcsiClients"> </a>

This policy enables users to collaborate on documents in real time and share them from the Office 2016 and Office 2103 desktop apps. Enabling this policy sets the following registry key value to 1:
  
[HKCU\SOFTWARE\Microsoft\OneDrive] ﻿"EnableAllOcsiClients"=dword:00000001
  
If you enable this setting, it displays the Office tab in OneDrive sync settings, and selects "Use Office 2016 to sync Office files that I open" by default.
  
![Screenshot of the Office tab in Settings for the new OneDrive for Business sync client](media/c90cf228-c27e-4107-b4cf-2c0690a959a4.png)
  
If you disable this setting, the **Office** tab is hidden in the sync client, and coauthoring and in-app sharing for Office files is disabled. The **Users can choose how to handle Office files in conflict** setting will act as disabled and in case of file conflicts, both copies will be kept. For more info about the settings in the sync client, see [Use Office 2016 to sync Office files that I open](https://support.office.com/article/8a409b0c-ebe1-4bfa-a08e-998389a9d823).
  
### Delay updating OneDrive.exe until the second release wave
<a name="EnableEnterpriseUpdate"> </a>

We release updates to OneDrive.exe in two rings. The first ring, "Production," is the default. It typically takes one to two weeks to completely roll out to this ring. After we finish rolling out to the Production ring, we release to the second ring, "Enterprise." Selecting the Enterprise ring gives you up to 60 days to prepare for updates and control their deployment within your organization. Enabling this policy sets the following registry key value to 1:
  
[HKCU\SOFTWARE\Microsoft\OneDrive] ﻿"EnableEnterpriseUpdate"=dword:00000001
  
If you enable this setting, OneDrive sync clients in your domain (including those used for syncing personal accounts) will be updated during the second ring.
  
If you disable this setting, OneDrive sync clients will be updated as soon as updates are available during the first ring.
  
For more info about the update rings and how the sync client checks for updates, see [The OneDrive sync client update process](the-sync-client-update-process.md).
  
### Users can choose how to handle Office files in conflict
<a name="EnableHoldTheFile"> </a>

This policy determines what happens when there's a conflict between Office 2016 file versions during synchronization. By default, the users is allowed to decide if they want to merge changes or keep both copies. Users can also configure the sync client to always fork the file and keep both copies. (This option is only available for Office 2016. With earlier versions of Office, the file is always forked and both copies are kept.) Enabling this policy sets the following registry key value to 1.
  
[HKCU\SOFTWARE\Microsoft\OneDrive] ﻿"EnableHoldTheFile"=dword:00000001
  
If you enable this setting, users can decide if they want to merge changes or keep both copies. Users can also configure the sync client to always fork the file and keep both copies as shown below.
  
![The Office tab of the Sync settings dialog box](media/ec60b062-1979-446d-b431-bf0baede0f8b.png)
  
If you disable this setting, then the file is always forked and both copies are kept in the case of a sync conflict. The configuration setting in the sync client is disabled.
  
You must enable the "Coauthoring and in-app sharing for Office files" policy to enable this policy. For more info about the settings in the sync client, see [Use Office 2016 to sync Office files that I open](https://support.office.com/article/8a409b0c-ebe1-4bfa-a08e-998389a9d823).
  
### Prevent users from using the remote file fetch feature to access files on the computer
<a name="RemoteAccessGPOEnabled"> </a>

This policy lets you block users from using the fetch feature when they are logged in with their Microsoft account to OneDrive.exe. The fetch feature allows users to go to OneDrive.com, select a Windows computer that's currently online and running the OneDrive sync client, and access all your personal files from that computer. By default, users can use the fetch feature.
  
There are two settings - one for 32-bit computers and one for 64-bit computers. Enabling these settings sets the following registry key values to 1.
  
[HKLM\SOFTWARE\Microsoft\OneDrive\Remote Access] ﻿"GPOEnabled"=dword:00000001
  
[HKLM\SOFTWARE\Wow6432Node\Microsoft\OneDrive\Remote Access] "GPOEnabled"=dword:00000001
  
If you enable this setting, users will be prevented from using the fetch feature.
  
If you disable this setting, users can use the fetch feature.
  
### Set the maximum download throughput that OneDrive.exe uses
<a name="SetMaxDownloadTput"> </a>

This policy lets you set the maximum download throughput rate in kilobytes (KB)/sec for computers running the OneDrive sync client. The minimum rate is 50 KB/sec and the maximum rate is 100,000 KB/sec. The lower the download throughput rate that you configure, the longer computers running OneDrive.exe will take to download files. 
  
By default, the download throughput rate is unlimited and can be configured by the user directly in the sync client. If you enable this setting, computers affected by this policy will use the maximum download throughput rate that you specify and the users will not be able to change the download rate in sync client settings themselves. Note, that OneDrive.exe has to be restarted on users' devices to apply the configuration specified in this setting. If you disable this setting, users can configure the maximum download rate for their computer by opening sync client settings and clicking the Network tab. 
  
We recommend that you use this setting in cases where Files On-Demand is NOT enabled and where strict traffic restrictions are required, such as when you initially deploy the sync client in your organization or enable syncing of team sites. We don't recommend that you use this setting on an ongoing basis because it will decrease sync client performance and negatively impact the user experience. 
  
Enabling this policy sets the following registry key value to a number from 50 through 100,000. For example:
  
[HKCU\SOFTWARE\Policies\Microsoft\OneDrive] "DownloadBandwidthLimit"=dword:000000﻿32
  
The above registry key sets the download throughput rate limit to 50KB/sec, using the hexadecimal value for 50, which is 00000032.
  
For info about estimating the network bandwidth you need for the sync client and controlling sync throughput, see [Network utilization planning for the OneDrive sync client](network-utilization-planning.md).
  
## Related Topics
<a name="Glob"> </a>

[Deploy the new OneDrive sync client in an enterprise environment ](deploy-the-sync-client-for-windows.md)
  
[Prevent users from installing the sync client](prevent-users-from-installing-the-sync-client.md)
  
[Allow syncing only on computers joined to specific domains ](allow-syncing-only-on-computers-joined-to-specific-domains.md)
  
[Block syncing of specific file types ](block-syncing-of-specific-file-types.md)
  

