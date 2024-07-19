---
ms.date: 05/23/2024
title: Sync in SharePoint and OneDrive
ms.reviewer: 
ms.author: ruihu
author: maggierui
manager: jtremper
recommendations: true
audience: Admin
f1.keywords:
- NOCSH
ms.topic: conceptual
ms.service: sharepoint-online
ms.collection: 
- M365-collaboration
- Tier2
ms.custom:
- seo-marvel-apr2020
ms.localizationpriority: medium
search.appverid:
- MET150
description: "In this article, you learn about syncing SharePoint and OneDrive files using the OneDrive sync app for Windows and Mac."
---

# Sync in SharePoint and OneDrive

When users install the OneDrive sync app for Windows or Mac, and sync the files on a team site, they can work with the files in File Explorer or Finder. They can also easily save files to the team site from the programs they use.

If the user adds, changes, or deletes files and folders on the site, the changes also apply to the files and folders of the user's computer and vice versa.

To upload files to the team site, users can copy or move them to the site in File Explorer or Finder. They can also use File Explorer or Finder to easily organize the document library by creating new folders, and moving and renaming files and folders. All these changes sync automatically.

Windows 10 devices come with the OneDrive sync app installed. Office 2016 and later installations also have the sync app installed.

## SharePoint file sync and OneDrive shortcuts

Users have two options when syncing files in SharePoint libraries and Teams. They can

- [Add shortcuts to libraries and folders to their OneDrive](https://support.microsoft.com/office/d66b1347-99b7-4470-9360-ffc048d35a33).
- [Use the Sync button in the document library](https://support.microsoft.com/office/6de9ede8-5b6e-4503-80b2-6190f3354a88).

## Deciding between OneDrive sync options

Both OneDrive shortcuts and OneDrive Sync options allow essentially the same thing—users can access files on their local computer in Explorer or Finder.

However, adding OneDrive shortcuts allows content to be accessed on all devices, whereas sync is related to a specific device. Additionally, OneDrive shortcuts offer improved performance versus using the sync button.

We recommend using OneDrive shortcuts as the more versatile option.

### Turn off OneDrive sync for SharePoint libraries

You can turn off OneDrive sync from all the SharePoint libraries in your organization with SharePoint Online Management Shell. 

To turn off OneDrive sync from all the SharePoint libraries in your organization:

1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).

    > [!NOTE]
    > If you installed a previous version of the SharePoint Online Management Shell, go to Add or remove programs and uninstall "SharePoint Online Management Shell." 

2. Connect to SharePoint as a [Global Administrator or SharePoint Administrator](./sharepoint-admin-role.md) in Microsoft 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online). by using this [Set-SPOTenant](/powershell/module/sharepoint-online/set-spotenant) PowerShell cmdlet to remove the OneDrive sync button:

3. Run the following cmdlets: 

    ```PowerShell
    Set-SPOTenant -HideSyncButtonOnTeamSite $true
    ```

Removing the sync button blocks new syncs from being started but doesn't affect existing syncs.

## Related articles

[Read the release notes and install the latest fully released versions](https://support.office.com/article/845dcf18-f921-435e-bf28-4e24b95e5fc0).

Read about [Invalid file names and file types in OneDrive and SharePoint](https://support.office.com/article/64883a5d-228e-48f5-b3d2-eb39e07630fa).

[Fix OneDrive sync problems](https://support.office.com/article/fix-onedrive-sync-problems-0899b115-05f7-45ec-95b2-e4cc8c4670b2)
