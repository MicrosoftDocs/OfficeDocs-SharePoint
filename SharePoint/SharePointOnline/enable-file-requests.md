---
ms.date: 09/16/2024
title: "Enable File Requests in SharePoint or OneDrive"
ms.reviewer: srice
ms.author: mactra
author: MachelleTranMSFT
manager: jtremper
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: one-drive
ms.localizationpriority: medium
ms.collection: 
- Strat_OD_admin
- M365-collaboration
ms.custom:
- admindeeplinkSPO
- onedrive-toc
search.appverid: 
  - SPO160
  - MET150
ms.assetid:
description: Learn how to enable a file request in OneDrive or Sharepoint.
---

# Enable file requests in SharePoint or OneDrive

With the [file request feature](https://support.microsoft.com/office/create-a-file-request-f54aa7f8-2589-4421-b351-d415fc3b83af) in OneDrive or SharePoint, users can request files by sending a link where others can upload files. When users upload files, they can't view, edit, delete, or download files in the folder or see who else has uploaded.

Admins can manage the **Request files** feature via the SharePoint Online Management Shell.

> [!IMPORTANT]
> File request is only available if:
>
> - You’re using OneDrive for work or school.
> - The admin has [enabled **Anyone** links](/sharepoint/turn-external-sharing-on-or-off).
> - Folder permissions are set to **View, edit, and upload** for **Anyone** links.
> - **Allow only specific security groups** isn’t enabled.
> - Not available for Office 365 operated by 21Vianet, OneDrive for home, or Office 365 Germany.

> [!NOTE]
> Disabling **Anyone** links also disables **Request files** on SharePoint and OneDrive.

## Enable or disable request files for SharePoint

To manage **Request files** for SharePoint:

1. Ensure [**Anyone** links are enabled](/sharepoint/turn-external-sharing-on-or-off#change-the-organization-level-external-sharing-setting).
2. Set folder permissions to **View, edit, and upload**.
3. Verify `CoreRequestFilesLinkEnabled` is **True** via the SharePoint Online Management Shell:
   - Run `Get-SPOTenant`.
   - If not set to **True**, use `Set-SPOTenant -CoreRequestFIlesLinkEnabled $True`.

(Optional) Set link expiration using `Set-SPOTenant -CoreRequestFilesLinkExpirationInDays`.

## Enable or Disable Request Files for OneDrive

To manage **Request files** for OneDrive:

1. Enable [**Anyone** links](/sharepoint/turn-external-sharing-on-or-off#change-the-organization-level-external-sharing-setting).
2. Set folder permissions to **View, edit, and upload**.
3. Configure **Anyone** links for OneDrive at the tenant level.
4. Verify `OneDriveRequestFilesLinkEnabled` is **True** via the SharePoint Online Management Shell:
   - Run `Get-SPOTenant`.
   - If not set to **True**, use `Set-SPOTenant -OneDriveRequestFilesLinkEnabled $True`.

(Optional) Set link expiration using `Set-SPOTenant -OneDriveRequestFilesLinkExpirationInDays`.

## Enable or Disable Request Files per Site

To manage **Request files** for a specific site:

1. Ensure [**Anyone** links are enabled](/sharepoint/turn-external-sharing-on-or-off#change-the-organization-level-external-sharing-setting).
2. Set folder permissions to **View, edit, and upload**.
3. Verify `RequestFilesLinkEnabled` is **True** via the SharePoint Online Management Shell:
   - Run `$r=Get-SPOSite -Identity <SiteURL> -Detailed`.
   - If not set to **True**, use `Set-SPOSite -RequestFIlesLinkEnabled $True`.

(Optional) Set link expiration using `Set-SPOSite -RequestFilesLinkExpirationInDays`.

For more information on file requests, see [Create a file request](https://support.microsoft.com/office/create-a-file-request-f54aa7f8-2589-4421-b351-d415fc3b83af).
