---
ms.date: 06/10/2022
title: Plan file sync for SharePoint and OneDrive in Microsoft 365
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: jtremper
recommendations: true
audience: Admin
f1.keywords: NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.localizationpriority: medium
ms.collection:  
ms.custom: intro-get-started
search.appverid: MET150
description: Learn how to plan file sync for SharePoint and OneDrive in your organization
---

# Plan file sync for SharePoint and OneDrive in Microsoft 365

Even though users can upload, download, and interact with SharePoint and OneDrive files from a web browser, the ideal experience comes with the OneDrive sync app for Windows and Mac, and the iOS and Android mobile apps.

The OneDrive sync app has a variety of configuration options for compliance, performance, user experience, and disk space management. While these can be configured at any time, it's important to consider some of them as part of your rollout plan.

**Key decisions for sync:**

- [How do you want to deploy the sync app?](#how-do-you-want-to-deploy-the-sync-app)
- [How do you want to manage sync on Windows computers?](#how-do-you-want-to-manage-sync-on-windows-computers)
- [Which update ring do you want to use?](#which-update-ring-do-you-want-to-use)
- [Do you want to limit network utilization for sync?](#do-you-want-to-limit-network-utilization-for-sync)
- [Do you want to sync commonly used folders with OneDrive](#do-you-want-to-sync-commonly-used-folders-with-onedrive)
- [Do you want to limit which organizations users can sync with?](#do-you-want-to-limit-which-organizations-users-can-sync-with)
- [Do you want to allow users to sync their personal OneDrive?](#do-you-want-to-allow-users-to-sync-their-personal-onedrive)
- [Do you want to block certain file types from being uploaded?](#do-you-want-to-block-certain-file-types-from-being-uploaded)
- [Do you need to sync files in a hybrid environment with SharePoint Server?](#do-you-need-to-sync-files-in-a-hybrid-environment-with-sharepoint-server)
- [Do you want to limit sync to computers joined to a specific domain?](#do-you-want-to-limit-sync-to-computers-joined-to-a-specific-domain)

For information about the recommended configuration options for the sync app, see [Recommended sync app configuration](/onedrive/ideal-state-configuration).

## How do you want to deploy the sync app?

You have several different options for deploying the OneDrive sync app: manually, using scripting, using Windows Autopilot (for the sync app on Windows), using a mobile device management solution such as Intune, or using Microsoft Endpoint Configuration Manager.

The OneDrive sync app is included as part of Windows 10, Windows 11, and Office 2016 or higher. You do not need to deploy the sync app to devices running these, though you may need to update the sync app to the latest version.

To deploy the OneDrive sync app to Windows using Microsoft Endpoint Configuration Manager, see [Deploy OneDrive apps by using Microsoft Endpoint Configuration Manager](/onedrive/deploy-on-windows).

If you need to install the sync app on a single computer, see [Install the sync app per machine](/onedrive/per-machine-installation).

For a full list of OneDrive sync app requirements, see [OneDrive sync app system requirements](https://support.office.com/article/cc0cb2b8-f446-445c-9b52-d3c2627d681e).

## How do you want to manage sync on Windows computers?

You can manage OneDrive sync app settings on Windows computers using Windows Group Policy or by using administrative templates in Intune. Using group policy requires that Windows computers be joined to an Active Directory domain. Using Intune requires that the device be managed by Microsoft Endpoint Manager.

For information, see:

- [Use OneDrive policies to control sync settings](/onedrive/use-group-policy)

- [Use administrative templates in Intune](/onedrive/configure-sync-intune)

Mac settings are configured using .plist files. For information, see [Deploy and configure the OneDrive sync app for Mac](/onedrive/deploy-and-configure-on-macos).

## Which update ring do you want to use?

You can select how soon your users receive updates we release for the sync app.

- **Insiders ring** - In this ring, users get the first changes that are released to the public. We recommend selecting several people in your IT department to join this ring. 

- **Production ring** – In this ring, users get fixes and new features in a timely fashion. We recommend leaving everyone else in the organization in this ring.

- **Enterprise ring** – In this ring, you have more control over the deployment of updates, but users have to wait longer to receive fixes and new features.

Configure the following policy to set the sync app update ring.

|Policy|Windows GPO|Mac|
|:-----|:----------|:--|
|Set the sync app update ring|[GPOSetUpdateRing](/onedrive/use-group-policy#set-the-sync-app-update-ring)|[Tier](/onedrive/deploy-and-configure-on-macos#tier)|

For details about the update process for the OneDrive sync app, see [The OneDrive sync app update process](/onedrive/sync-client-update-process).

## Do you want to limit network utilization for sync?

Depending on your network capacity, you may want to consider limiting how much network bandwidth the sync app can use. This can be useful during a migration phase when large amounts of content are being synced.

Use the following policies to limit the network bandwidth used by the sync app.

|Policy|Windows GPO|Mac|
|:-----|:----------|:--|
|Limit the sync app upload rate to a percentage of throughput|[AutomaticUploadBandwidthPercentage](/onedrive/use-group-policy#limit-the-sync-app-upload-rate-to-a-percentage-of-throughput)|[AutomaticUploadBandwidthPercentage](/onedrive/deploy-and-configure-on-macos#automaticuploadbandwidthpercentage)|
|Enable automatic upload bandwidth management for OneDrive|[EnableAutomaticUploadBandwidthManagement](/onedrive/use-group-policy#enable-automatic-upload-bandwidth-management-for-onedrive)|N/A|


## Do you want to sync commonly used folders with OneDrive?

Users often save files to their documents folder or desktop. They may not realize that they should save these files in OneDrive. You can automatically sync these commonly used folders to OneDrive, prompt users to do so, or prevent them from doing so.

Use the following policies to configure how users commonly used folders are synced with OneDrive.

|Policy|Windows GPO|Mac|
|:-----|:----------|:--|
|Silently move commonly used folders to OneDrive|[KFMSilentOptIn](/onedrive/use-group-policy#silently-move-windows-known-folders-to-onedrive)|[KFMSilentOptIn](/onedrive/deploy-and-configure-on-macos#kfmsilentoptin)|
|Prompt users to move their commonly used folders to OneDrive|[KFMOptInWithWizard](/onedrive/use-group-policy#prompt-users-to-move-windows-known-folders-to-onedrive)|[KFMOptInWithWizard](/onedrive/deploy-and-configure-on-macos#kfmoptinwithwizard)|
|Prevent users from stopping sync of their commonly used folders to OneDrive|[KFMBlockOptOut](/onedrive/use-group-policy#prevent-users-from-redirecting-their-windows-known-folders-to-their-pc)|[KFMBlockOptOut](/onedrive/deploy-and-configure-on-macos#kfmblockoptout)|
|Prevent users from moving their commonly used folders to OneDrive|[KFMBlockOptIn](/onedrive/use-group-policy#prevent-users-from-moving-their-windows-known-folders-to-onedrive)|[KFMBlockOptIn](/onedrive/deploy-and-configure-on-macos#kfmblockoptin)|

For more information about syncing commonly used folder with OneDrive, see [Redirect and move Windows known folders to OneDrive](/onedrive/redirect-known-folders) and [Redirect and move macOS Desktop and Documents folders to OneDrive](/onedrive/redirect-known-folders-macos).

## Do you want to limit which organizations users can sync with?

By default, users can sync shared libraries from other organizations. You can limit this to specific organizations or disable it all together.

Use the following policies to configure which organizations users can sync with.

|Policy|Windows GPO|Mac|
|:-----|:----------|:--|
|Allow syncing OneDrive accounts for only specific organizations|[AllowTenantList](/onedrive/use-group-policy#allow-syncing-onedrive-accounts-for-only-specific-organizations)|[AllowTenantList](/onedrive/deploy-and-configure-on-macos#allowtenantlist)|
|Block syncing OneDrive accounts for specific organizations|[BlockTenantList](/onedrive/use-group-policy#block-syncing-onedrive-accounts-for-specific-organizations)|[BlockTenantList](/onedrive/deploy-and-configure-on-macos#blocktenantlist)|
|Prevent users from syncing libraries and folders shared from other organizations|[BlockExternalSync](/onedrive/use-group-policy#prevent-users-from-syncing-libraries-and-folders-shared-from-other-organizations)|[BlockExternalSync](/onedrive/deploy-and-configure-on-macos#blockexternalsync)|

For more information about syncing with other organizations, see [B2B Sync](/onedrive/b2b-sync).

## Do you want to allow users to sync their personal OneDrive?

Depending on your governance practices, you can prevent users from syncing their personal OneDrive accounts to devices managed by your organization.

Use the following policies to specify if users can sync personal OneDrive accounts.

|Policy|Windows GPO|Mac|
|:-----|:----------|:--|
|Prevent users from syncing personal OneDrive accounts|[DisablePersonalSync](/onedrive/use-group-policy#prevent-users-from-syncing-personal-onedrive-accounts)|[DisablePersonalSync](/onedrive/deploy-and-configure-on-macos#disablepersonalsync)|

## Do you want to block certain file types from being uploaded?

You can specify if you don't want users to be able to upload certain types of files using the sync app. Use the following policy to configure this.

|Policy|Windows GPO|Mac|
|:-----|:----------|:--|
|Exclude specific kinds of files from being uploaded|[EnableODIgnoreListFromGPO](/onedrive/use-group-policy#exclude-specific-kinds-of-files-from-being-uploaded)|[EnableODIgnore](/onedrive/deploy-and-configure-on-macos#enableodignore)|

This can also be configured in the SharePoint admin center. For more information, see [Block syncing of specific file types](/onedrive/block-file-types).

## Do you need to sync files in a hybrid environment with SharePoint Server?

If your organization uses SharePoint Server 2019 or SharePoint Server Subscription Edition, you can sync files using the OneDrive sync app. For information, see [Configure syncing with the new OneDrive sync app](/SharePoint/install/new-onedrive-sync-client/).

If you are using the previous OneDrive sync app (Groove.exe), see [Transition from the previous OneDrive for Business sync app](/onedrive/transition-from-previous-sync-client) for information on how to move to the new OneDrive sync app.

## Do you want to limit sync to computers joined to a specific domain?

To make sure that users sync OneDrive files only on managed computers, you can configure OneDrive to sync only on PCs that are joined to specific domains. for more information, see [Allow syncing only on computers joined to specific domains](/onedrive/allow-syncing-only-on-specific-domains).

## Next steps

> [!div class="nextstepaction"]
> [Plan for content migration](plan-rollout-migration.md)

## Related topics

[Plan for SharePoint and OneDrive in Microsoft 365](plan-for-sharepoint-onedrive.md)

