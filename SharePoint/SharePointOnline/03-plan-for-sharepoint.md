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




### Migrating with FastTrack

FastTrack is a Microsoft benefit that is included in your subscription. FastTrack provides you with a set of best practices, tools, resources, and experts committed to helping you deploy Microsoft 365. Guidance around SharePoint and OneDrive onboarding, migration, and adoption are included in the benefit offering. This guidance includes: help to discover what's possible, creating a plan for success, and onboarding new users, providing guidance on migrating content from file share, Box, or Google Drive source environments, and introducing capabilities at a flexible pace. 

FastTrack guidance provides enablement of both SharePoint and OneDrive as well as getting the source environment ready for your transition. For more details, see [FastTrack Center Benefit Overview](/fasttrack/data-migration/). Interested in getting started? Visit the [FastTrack web site](https://www.microsoft.com/fasttrack/), review resources, and submit a Request for Assistance.


## Site lifecycle

[Microsoft 365 group expiration policy](/microsoft-365/solutions/microsoft-365-groups-expiration-policy)



## Hubs and architecture

## Pre-provision accounts

## Sync


[Recommended sync app configuration](/onedrive/ideal-state-configuration)

Even though users can upload, download, and interact with SharePoint and OneDrive files from a web browser, the ideal OneDrive experience comes with the OneDrive sync app for Windows and Mac, and the iOS and Android mobile apps. 

For a full list of OneDrive sync app requirements, see [OneDrive sync app system requirements](https://support.office.com/article/cc0cb2b8-f446-445c-9b52-d3c2627d681e).


- To manage the sync app deployment centrally, prevent users from installing the sync app when they go to their OneDrive in a web browser: [Prevent installation](prevent-installation.md)

- To make sure that users sync OneDrive files only on managed computers, configure OneDrive to sync only on PCs that are joined to specific domains: [Allow syncing only on specific domains](allow-syncing-only-on-specific-domains.md)

- To prevent users from uploading specific file types, such as exe or mp3 files: [Block file types](block-file-types.md)




Sync decisions:

allow sync at all?
update ring
deployment options
throttle sync during migration

kfm
GPO vs. Intune
Specific policies



**Key decisions for sync:**

- [Do you want to allow users to sync files?](#do-you-want-to-allow-users-to-sync-files)
- [How do you want to manage sync on Windows computers?](#how-do-you-want-to-manage-sync-on-windows-computers)
- [Which update ring do you want to use?](#which-update-ring-do-you-want-to-use)
- [Do you want to limit network utilization for sync?](#do-you-want-to-limit-network-utilization-for-sync)
- [Do you want to sync common folders with OneDrive?](#do-you-want-to-sync-common-folders-with-onedrive)
- [Do you want to limit which domains users can sync with?](do-you-want-to-limit-which-domains-users-can-sync-with)
- [Do you want to allow users to sync their personal OneDrive?](do-you-want-to-allow-users-to-sync-their-personal-onedrive)
- [Do you want to block certain file types from being synced?](do-you-want-to-block-certain-file-types-from-being-synced)
- [Does you need to sync files in a hybrid environment with SharePoint Server?](does-you-need-to-sync-files-in-a-hybrid-environment-with-sharepoint-server)



### Do you want to allow users to sync files?


### How do you want to manage sync on Windows computers?


### Which update ring do you want to use?


- (GPOSetUpdateRing) [Set the sync app update ring](use-group-policy.md#set-the-sync-app-update-ring)


### Do you want to limit network utilization for sync?

- (AutomaticUploadBandwidthPercentage) [Limit the sync app upload rate to a percentage of throughput](use-group-policy.md#limit-the-sync-app-upload-rate-to-a-percentage-of-throughput)


- (EnableAutomaticUploadBandwidthManagement) [Enable automatic upload bandwidth management for OneDrive](use-group-policy.md#enable-automatic-upload-bandwidth-management-for-onedrive)


### Do you want to sync common folders with OneDrive?


- (KFMBlockOptIn) [Prevent users from moving their Windows known folders to OneDrive](use-group-policy.md#prevent-users-from-moving-their-windows-known-folders-to-onedrive)

- (KFMBlockOptOut) [Prevent users from redirecting their Windows known folders to their PC](use-group-policy.md#prevent-users-from-redirecting-their-windows-known-folders-to-their-pc)

- (KFMOptInWithWizard) [Prompt users to move Windows known folders to OneDrive](use-group-policy.md#prompt-users-to-move-windows-known-folders-to-onedrive)

- (KFMSilentOptIn) [Silently move Windows known folders to OneDrive](use-group-policy.md#silently-move-windows-known-folders-to-onedrive)



### Do you want to limit which domains users can sync with?


- (AllowTenantList) [Allow syncing OneDrive accounts for only specific organizations](use-group-policy.md#allow-syncing-onedrive-accounts-for-only-specific-organizations)

- (BlockExternalSync) [Prevent users from syncing libraries and folders shared from other organizations](use-group-policy.md#prevent-users-from-syncing-libraries-and-folders-shared-from-other-organizations)

- (BlockTenantList) [Block syncing OneDrive accounts for specific organizations](use-group-policy.md#block-syncing-onedrive-accounts-for-specific-organizations)


### Do you want to allow users to sync their personal OneDrive?


- (DisablePersonalSync) [Prevent users from syncing personal OneDrive accounts](use-group-policy.md#prevent-users-from-syncing-personal-onedrive-accounts)


### Do you want to block certain file types from being synced?

- (EnableODIgnoreListFromGPO) [Exclude specific kinds of files from being uploaded](use-group-policy.md#exclude-specific-kinds-of-files-from-being-uploaded)

### Does you need to sync files in a hybrid environment with SharePoint Server?

- (SharePointOnPremFrontDoorUrl) Specify SharePoint Server URL and organization name. This setting is for customers who have SharePoint Server 2019. For info about using the new OneDrive sync app with SharePoint Server 2019, see [Configure syncing with the new OneDrive sync app](/SharePoint/install/new-onedrive-sync-client/).

- (SharePointOnPremPrioritization) Specify the OneDrive location in a hybrid environment. This setting is for customers who have SharePoint Server 2019. For info about using the new OneDrive sync app with SharePoint Server 2019, see [Configure syncing with the new OneDrive sync app](/SharePoint/install/new-onedrive-sync-client/).



### Sync app update process

You can select how soon your users receive updates we release for the sync app.

- **Insiders ring** - In this ring, users get the first changes that are released to the public. We recommend selecting several people in your IT department to join this ring. 

- **Production ring** – In this ring, users get fixes and new features in a timely fashion. We recommend leaving everyone else in the organization in this ring.

- **Deferred ring** – In this ring, you have more control over the deployment of updates, but users have to wait longer to receive fixes and new features.

You configure this setting using the OneDrive policy [Set the sync app update ring](use-group-policy.md#set-the-sync-app-update-ring).

For details about the update process for the OneDrive sync app, see [The OneDrive sync app update process](sync-client-update-process.md).

Key decision:

- Which ring do you want to use for updates to the OneDrive sync app?

## Deployment options

You have several different options for deploying the OneDrive sync app: manually, using scripting, using Windows Autopilot (for the sync app on Windows), using an MDM such as Intune, or using Microsoft Endpoint Configuration Manager.

The OneDrive sync app is included as part of Windows 10, Windows 11, and Office 2016 or higher. You do not need to deploy the sync app to devices running these, though you may need to update the sync app to the latest version.

### Deploy OneDrive using Microsoft Endpoint Configuration Manager

To deploy the OneDrive sync app to Windows using Microsoft Endpoint Configuration Manager, see [Deploy OneDrive apps by using Microsoft Endpoint Configuration Manager](deploy-on-windows.md).


- **Sync** - On the <a href="https://go.microsoft.com/fwlink/?linkid=2185072" target="_blank">Settings page in the SharePoint admin center</a>, select **Sync** to configure sync restrictions based on file types, require that synced devices be domain joined, or restrict synchronization from computers running macOS. Depending on your device management tool, the PC device restrictions in this section may overlap other management settings.

## Manage OneDrive by using Group Policy

You can use Group Policy to manage OneDrive settings for domain-joined computers in your environment. For info, see [Use OneDrive policies to control OneDrive sync app settings](use-group-policy.md). Using Group Policy, you can [redirect and move Windows known folders to OneDrive](redirect-known-folders.md), and [enable silent account configuration](use-silent-account-configuration.md).

## Known Folder Move

Known Folder Move makes it easier to move files in your users' Desktop, Documents, and Pictures folders to OneDrive. This lets users continue working in the folders they're familiar with and access their files from any device. It also helps you make sure your users' files are backed up in the cloud if anything happens to their device. For more info, see [Redirect and move Windows known folders to OneDrive](redirect-known-folders.md).

## Change management


## Support

User training important - how to use the service in a compliant manner and avoid security issues.

Provide training for users and support, cheat sheets, office hours.