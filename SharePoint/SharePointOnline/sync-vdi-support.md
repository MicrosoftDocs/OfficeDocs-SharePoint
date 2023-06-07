---
ms.date: 04/23/2019
title: "Use the sync app on virtual desktops"
ms.reviewer: sraja
ms.author: mikeplum
author: MikePlumleyMSFT
manager: serdars
audience: Admin
f1.keywords:
- CSH
ms.topic: article
ms.service: one-drive
ms.localizationpriority: medium
ms.custom: 
- Adm_O365
- onedrive-toc
search.appverid:
- MET150
- BCS160
ms.collection: 
- Strat_OD_admin
- M365-collaboration
ms.assetid: 
description: "Learn about the OneDrive sync app support for desktop virtualization."
---

# Use the sync app on virtual desktops

For all [supported operating systems](https://support.office.com/article/cc0cb2b8-f446-445c-9b52-d3c2627d681e), the OneDrive sync app supports:

- Virtual desktops that persist between sessions. 
- Non-persistent virtual desktops that use [Azure Virtual Desktop](/azure/virtual-desktop).
- Non-persistent virtual desktops that have [FSLogix Apps](/fslogix/configure-profile-container-tutorial) or [FSLogix Office Container](/fslogix/configure-office-container-tutorial), and a Microsoft 365 subscription for all of the following operating systems:
  - Windows 10, 32 or 64-bit (supports VHDX files) 
  - Windows 7, 32 or 64-bit (supports VHD files) 
  - Windows Server 2019 (supports VHDX)
  - Windows Server 2016 (supports VHDX)
  - Windows Server 2012 R2 (supports VHDX)
  - Windows Server 2008 R2 (supports VHD)
 
> [!NOTE]
> The minimum supported versions are: OneDrive 19.174.0902.0013 and FSLogix Apps [2.9.7653.47581](/fslogix/whats-new).
>
> Using the OneDrive sync app with non-persistent environments requires that you [install the sync app per machine](./per-machine-installation.md).
>
> For Windows Server, the [SMB network file sharing protocol](/windows-server/storage/file-server/file-server-smb-overview) is also required.
>
> The OneDrive sync app is supported in a remote app scenario hosted as a [Citrix Virtual App](onedrive-in-citrix-virtual-apps-deployment-guide.md).
>
> The OneDrive sync app with FSLogix does not support running multiple instances of the same container simultaneously.

## See also

Learn more about [VHDX](/openspecs/windows_protocols/ms-vhdx/83f6b700-6216-40f0-aa99-9fcb421206e2) and [VHD](/windows/desktop/vstor/about-vhd).

For info about creating virtual hard disks, see [Manage virtual hard disks](/windows-server/storage/disk-management/manage-virtual-hard-disks).

