---
title: Plan for SharePoint in Microsoft 365
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: serdars
recommendations: true
audience: Admin
f1.keywords: NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.localizationpriority: medium
ms.collection:  
ms.custom: intro-get-started
search.appverid: MET150
description: 
---

# Plan for SharePoint in Microsoft 365

Content storage and collaboration needs


What's the desired outcome of rolling out ODSP?


[Microsoft Teams deployment overview](/microsoftteams/deploy-overview)

Cutover from old system to new system


	• Should migration throughput be the rollout driver?


	Should ODSP admins specialize or work from a queue? How many and how organized?
• What are the customization requirements?
## Customization / templates

[Customizing SharePoint](/sharepoint/extend-and-develop)




## Migrating with FastTrack

FastTrack is a Microsoft benefit that is included in your subscription. FastTrack provides you with a set of best practices, tools, resources, and experts committed to helping you deploy Microsoft 365. Guidance around SharePoint and OneDrive onboarding, migration, and adoption are included in the benefit offering. This guidance includes: help to discover what's possible, creating a plan for success, and onboarding new users, providing guidance on migrating content from file share, Box, or Google Drive source environments, and introducing capabilities at a flexible pace. 

FastTrack guidance provides enablement of both SharePoint and OneDrive as well as getting the source environment ready for your transition. For more details, see [FastTrack Center Benefit Overview](/fasttrack/data-migration/). Interested in getting started? Visit the [FastTrack web site](https://www.microsoft.com/fasttrack/), review resources, and submit a Request for Assistance.


## Site lifecycle

[Manage site creation in SharePoint](manage-site-creation.md)

As a global or SharePoint admin in Microsoft 365, you can let your users create and administer their own SharePoint sites, determine what kind of sites they can create, and specify the location of the sites. By default, users can create communication sites and Microsoft 365 group-connected team sites.

 Note

Disabling site creation for users does not remove their ability to create Microsoft 365 groups or resources, such as Microsoft Teams, which rely on a group. When a Microsoft 365 group is created, a SharePoint site is also created. To restrict creation of Microsoft 365 groups and the resources that rely on groups see Manage who can create Microsoft 365 Groups.

[Microsoft 365 group expiration policy](/microsoft-365/solutions/microsoft-365-groups-expiration-policy)

A Microsoft 365 groups expiration policy can help remove inactive groups from the system and make things cleaner.

When a group expires, all of its associated services (the mailbox, Planner, SharePoint site, team, etc.) are also deleted.

[Create guidelines for site usage](sites-usage-guidelines.md)

Provide general policy statements that you want your users to follow. These may include key business uses you have defined for sites, internal communication policies, or security and privacy guidelines.

## Hubs and architecture

[Planning your SharePoint hub sites](planning-hub-sites.md)


## Pre-provision accounts

[Pre-provision OneDrive for users in your organization](pre-provision-accounts)

By default, the first time that a user browses to their OneDrive it's automatically created (provisioned) for them. In some cases, such as the following, you might want your users' OneDrive locations to be ready beforehand, or pre-provisioned:

Your organization has a custom process for adding new employees, and you want to create a OneDrive when you add a new employee.

Your organization plans to migrate from SharePoint Server on-premises to Microsoft 365.

Your organization plans to migrate from another online storage service.

## Sync

Even though users can upload, download, and interact with SharePoint and OneDrive files from a web browser, the ideal experience comes with the OneDrive sync app for Windows and Mac, and the iOS and Android mobile apps.

The OneDrive sync app has a variety of configuration options for compliance, performance, user experience, and disk space management. While these can be configured at any time, it's important to consider some of them as part of your rollout plan.

**Key decisions for sync:**

- [How do you want to deploy the sync app?](how-do-you-want-to-deploy-the-sync-app)
- [Do you want to allow users to sync files?](#do-you-want-to-allow-users-to-sync-files)
- [How do you want to manage sync on Windows computers?](#how-do-you-want-to-manage-sync-on-windows-computers)
- [Which update ring do you want to use?](#which-update-ring-do-you-want-to-use)
- [Do you want to limit network utilization for sync?](#do-you-want-to-limit-network-utilization-for-sync)
- [Do you want to sync common folders with OneDrive?](#do-you-want-to-sync-common-folders-with-onedrive)
- [Do you want to limit which domains users can sync with?](do-you-want-to-limit-which-domains-users-can-sync-with)
- [Do you want to allow users to sync their personal OneDrive?](do-you-want-to-allow-users-to-sync-their-personal-onedrive)
- [Do you want to block certain file types from being synced?](do-you-want-to-block-certain-file-types-from-being-synced)
- [Does you need to sync files in a hybrid environment with SharePoint Server?](does-you-need-to-sync-files-in-a-hybrid-environment-with-sharepoint-server)

For information about the recommended configuration options for the sync app, see [Recommended sync app configuration](ideal-state-configuration.md).

### How do you want to deploy the sync app?

You have several different options for deploying the OneDrive sync app: manually, using scripting, using Windows Autopilot (for the sync app on Windows), using an MDM such as Intune, or using Microsoft Endpoint Configuration Manager.

The OneDrive sync app is included as part of Windows 10, Windows 11, and Office 2016 or higher. You do not need to deploy the sync app to devices running these, though you may need to update the sync app to the latest version.

To deploy the OneDrive sync app to Windows using Microsoft Endpoint Configuration Manager, see [Deploy OneDrive apps by using Microsoft Endpoint Configuration Manager](deploy-on-windows.md).

If you need to install the sync app on a single computer, see [Install the sync app per machine](per-machine-installation.md).

For a full list of OneDrive sync app requirements, see [OneDrive sync app system requirements](https://support.office.com/article/cc0cb2b8-f446-445c-9b52-d3c2627d681e).

### How do you want to manage sync on Windows computers?

You can manage OneDrive sync app settings on Windows computers using Windows Group Policy or by using administrative templates in Intune. Using group policy requires that Windows computers be joined to an Active Directory domain. Using Intune requires that the device be managed by Microsoft Endpoint Manager.

For information, see:

- [Use OneDrive policies to control sync settings](use-group-policy.md)

- [Use administrative templates in Intune](configure-sync-intune.md)

Mac settings are configured using .plist files. For information, see [Deploy and configure the OneDrive sync app for Mac](deploy-and-configure-on-macos.md).

### Which update ring do you want to use?

You can select how soon your users receive updates we release for the sync app.

- **Insiders ring** - In this ring, users get the first changes that are released to the public. We recommend selecting several people in your IT department to join this ring. 

- **Production ring** – In this ring, users get fixes and new features in a timely fashion. We recommend leaving everyone else in the organization in this ring.

- **Deferred ring** – In this ring, you have more control over the deployment of updates, but users have to wait longer to receive fixes and new features.

Configure the following policy to set the sync app update ring.

|Policy|Windows GPO|Mac|
|:-----|:----------|:--|
|Set the sync app update ring|[GPOSetUpdateRing](use-group-policy.md#set-the-sync-app-update-ring)|[Tier](deploy-and-configure-on-macos.md#tier)|

For details about the update process for the OneDrive sync app, see [The OneDrive sync app update process](sync-client-update-process.md).

### Do you want to limit network utilization for sync?

Depending on your network capacity, you may want to consider limiting how much network bandwidth the sync app can use. This can be useful during a migration phase when large amounts of content are being synced.

Use the following policies to limit the network bandwidth used by the sync app.

|Policy|Windows GPO|Mac|
|:-----|:----------|:--|
|Limit the sync app upload rate to a percentage of throughput|[AutomaticUploadBandwidthPercentage](use-group-policy.md#limit-the-sync-app-upload-rate-to-a-percentage-of-throughput)|[AutomaticUploadBandwidthPercentage](deploy-and-configure-on-macos.md#automaticuploadbandwidthpercentage)|
|Enable automatic upload bandwidth management for OneDrive|[EnableAutomaticUploadBandwidthManagement](use-group-policy.md#enable-automatic-upload-bandwidth-management-for-onedrive)|N/A|


### Do you want to sync commonly used folders with OneDrive?

Users often save files to their documents folder or desktop. They may not realize that they should save these files in OneDrive. You can automatically sync these commonly used folders to OneDrive, prompt users to do so, or prevent them from doing so.

Use the following policies to configure how users commonly used folders are synced with OneDrive.

|Policy|Windows GPO|Mac|
|:-----|:----------|:--|
|Silently move commonly used folders to OneDrive|[KFMSilentOptIn](use-group-policy.md#silently-move-windows-known-folders-to-onedrive)|[KFMSilentOptIn](deploy-and-configure-on-macos.md#kfmsilentoptin)|
|Prompt users to move their commonly used folders to OneDrive|[KFMOptInWithWizard](use-group-policy.md#prompt-users-to-move-windows-known-folders-to-onedrive)|[KFMOptInWithWizard](deploy-and-configure-on-macos.md#kfmoptinwithwizard)|
|Prevent users from stopping sync of their commonly used folders to OneDrive|[KFMBlockOptOut](use-group-policy.md#prevent-users-from-redirecting-their-windows-known-folders-to-their-pc)|[KFMBlockOptOut](deploy-and-configure-on-macos.md#kfmblockoptout)|
|Prevent users from moving their commonly used folders to OneDrive|[KFMBlockOptIn](use-group-policy.md#prevent-users-from-moving-their-windows-known-folders-to-onedrive)|[KFMBlockOptIn](deploy-and-configure-on-macos.md#kfmblockoptin)|

For more information about syncing commonly used folder with OneDrive, see [Redirect and move Windows known folders to OneDrive](redirect-known-folders.md) and [Redirect and move macOS Desktop and Documents folders to OneDrive](redirect-known-folders-macos.md).

### Do you want to limit which organizations users can sync with?

By default, users can sync shared libraries from other organizations. You can limit this to specific organizations or disable it all together.

Use the following policies to configure which organizations users can sync with.

|Policy|Windows GPO|Mac|
|:-----|:----------|:--|
|Allow syncing OneDrive accounts for only specific organizations|[AllowTenantList](use-group-policy.md#allow-syncing-onedrive-accounts-for-only-specific-organizations)|[AllowTenantList](deploy-and-configure-on-macos.md#allowtenantlist)|
|Block syncing OneDrive accounts for specific organizations|[BlockTenantList](use-group-policy.md#block-syncing-onedrive-accounts-for-specific-organizations)|[BlockTenantList](deploy-and-configure-on-macos.md#blocktenantlist)|
|Prevent users from syncing libraries and folders shared from other organizations|[BlockExternalSync](use-group-policy.md#prevent-users-from-syncing-libraries-and-folders-shared-from-other-organizations)|[BlockExternalSync](deploy-and-configure-on-macos.md#blockexternalsync)|

For more information about syncing with other organizations, see [B2B Sync](b2b-sync.md).

### Do you want to allow users to sync their personal OneDrive?

Depending on your governance practices, you can prevent users from syncing their personal OneDrive accounts to devices managed by your organization.

Use the following policies to specify if users can sync personal OneDrive accounts.

|Policy|Windows GPO|Mac|
|:-----|:----------|:--|
|Prevent users from syncing personal OneDrive accounts|[DisablePersonalSync](use-group-policy.md#prevent-users-from-syncing-personal-onedrive-accounts)|[DisablePersonalSync](deploy-and-configure-on-macos.md#disablepersonalsync)|

### Do you want to block certain file types from being uploaded?

You can specify if you don't want users to be able to upload certain types of files using the sync app. Use the following policy to configure this.

|Policy|Windows GPO|Mac|
|:-----|:----------|:--|
|Exclude specific kinds of files from being uploaded|[EnableODIgnoreListFromGPO](use-group-policy.md#exclude-specific-kinds-of-files-from-being-uploaded)|[EnableODIgnore](deploy-and-configure-on-macos.md#enableodignore)|

For more information about preventing syncing of certain file types, see [Block syncing of specific file types](block-file-types.md).

### Does you need to sync files in a hybrid environment with SharePoint Server?

If your organization uses SharePoint Server 2019 or SharePoint Server Subscription Edition, you can sync files using the OneDrive sync app. For information, see [Configure syncing with the new OneDrive sync app](/SharePoint/install/new-onedrive-sync-client/).

If you are using the previous OneDrive sync app (Groove.exe), see [Transition from the previous OneDrive for Business sync app](transition-from-previous-sync-client.md) for information on how to move to the new OneDrive sync app.

## Change management


## Support

User training important - how to use the service in a compliant manner and avoid security issues.

[OneDrive help & learning](https://support.microsoft.com/onedrive)

[SharePoint help & learning](https://support.microsoft.com/sharepoint)

Provide training for users and support, cheat sheets, office hours.