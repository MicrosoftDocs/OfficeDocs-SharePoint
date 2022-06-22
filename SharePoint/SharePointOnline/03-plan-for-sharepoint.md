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


	FastTrack

## Site lifecycle

[Microsoft 365 group expiration policy](/microsoft-365/solutions/microsoft-365-groups-expiration-policy)



## Hubs and architecture

## Sync

Even though you can upload, download, and interact with your OneDrive files from a web browser, the ideal OneDrive experience comes from the Windows and Mac sync apps and the iOS and Android mobile apps. OneDrive is available for most operating systems and browsers and requires minimal hardware. For a full list of app requirements for using OneDrive, see [OneDrive system requirements](https://support.office.com/article/cc0cb2b8-f446-445c-9b52-d3c2627d681e).

If you already have the OneDrive sync app installed on Windows devices, start by determining the version or versions of OneDrive in your environment. Depending on your findings, you may need to change your deployment process to accommodate the current version (for example, run takeover commands in PowerShell to ensure that data sync responsibilities transition to the new sync app). To determine which version of OneDrive you're using, see [Which version of OneDrive am I using?](https://support.office.com/article/19246eae-8a51-490a-8d97-a645c151f2ba)

### Sync app update process

You can select how soon your users receive updates we release for the sync app.

- **Insiders ring** - In this ring, users get the first changes that are released to the public. We recommend selecting several people in your IT department to join this ring. 

- **Production ring** – In this ring, users get fixes and new features in a timely fashion. We recommend leaving everyone else in the organization in this ring.

- **Deferred ring** – In this ring, you have more control over the deployment of updates, but users have to wait longer to receive fixes and new features.

You configure this setting using the OneDrive policy [Set the sync app update ring](use-group-policy.md#set-the-sync-app-update-ring).

For details about the update process for the OneDrive sync app, see [The OneDrive sync app update process](sync-client-update-process.md).

To find out about new features available in current OneDrive updates as well as the current and historical version numbers, see [New OneDrive sync app release notes](https://support.office.com/article/845dcf18-f921-435e-bf28-4e24b95e5fc0).

Key decision:

- Which ring do you want to use for updates to the OneDrive sync app?


- To manage the sync app deployment centrally, prevent users from installing the sync app when they go to their OneDrive in a web browser: [Prevent installation](prevent-installation.md)

- To make sure that users sync OneDrive files only on managed computers, configure OneDrive to sync only on PCs that are joined to specific domains: [Allow syncing only on specific domains](allow-syncing-only-on-specific-domains.md)

- To prevent users from uploading specific file types, such as exe or mp3 files: [Block file types](block-file-types.md)

## Deployment options

You have several different options for deploying OneDrive: manually, using scripting, using Windows Autopilot (for the sync app on Windows), using an MDM such as Intune, or using Microsoft Endpoint Configuration Manager.

The OneDrive sync app is included as part of Windows 10 and Office 2016. You do not need to deploy the sync app to devices running these, though you may need to update the sync app to the latest version.

## Deploy OneDrive using Microsoft Endpoint Configuration Manager

To deploy the OneDrive sync app to Windows using Microsoft Endpoint Configuration Manager, see [Deploy OneDrive apps by using Microsoft Endpoint Configuration Manager](deploy-on-windows.md).

> [!VIDEO https://www.microsoft.com/videoplayer/embed/RE2CnSr]

Before you can deploy applications to computers running macOS, you need to complete some prerequisite tasks on the Microsoft Endpoint Configuration Manager site. For detailed info about these prerequisites and how to prepare a Configuration Manager environment for Mac management, see [Prepare to deploy client software to Macs](/configmgr/core/clients/deploy/prepare-to-deploy-mac-clients/). When you've completed the prerequisites, you can deploy applications to Macs by completing the steps described in [Create Mac computer applications with Configuration Manager](/configmgr/apps/get-started/creating-mac-computer-applications). For info about configuring the OneDrive sync app for macOS, see [Deploy and configure the new OneDrive sync app for Mac](deploy-and-configure-on-macos.md).

- **Sync** - On the <a href="https://go.microsoft.com/fwlink/?linkid=2185072" target="_blank">Settings page in the SharePoint admin center</a>, select **Sync** to configure sync restrictions based on file types, require that synced devices be domain joined, or restrict synchronization from computers running macOS. Depending on your device management tool, the PC device restrictions in this section may overlap other management settings.

## Manage OneDrive by using Group Policy

You can use Group Policy to manage OneDrive settings for domain-joined computers in your environment. For info, see [Use OneDrive policies to control OneDrive sync app settings](use-group-policy.md). Using Group Policy, you can [redirect and move Windows known folders to OneDrive](redirect-known-folders.md), and [enable silent account configuration](use-silent-account-configuration.md).

## Known Folder Move

Known Folder Move makes it easier to move files in your users' Desktop, Documents, and Pictures folders to OneDrive. This lets users continue working in the folders they're familiar with and access their files from any device. It also helps you make sure your users' files are backed up in the cloud if anything happens to their device. For more info, see [Redirect and move Windows known folders to OneDrive](redirect-known-folders.md).

## Change management


## Support

User training important - how to use the service in a compliant manner and avoid security issues.

Provide training for users and support, cheat sheets, office hours.