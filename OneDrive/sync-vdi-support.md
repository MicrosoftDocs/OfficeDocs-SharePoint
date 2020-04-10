---
title: "Use the sync app on virtual desktops"
ms.reviewer: sraja
ms.author: kaarins
author: kaarins
manager: pamgreen
audience: Admin
f1.keywords:
- CSH
ms.topic: article
ms.service: one-drive
localization_priority: Normal
ms.custom: 
- Adm_O365
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
- Non-persistent environments that use [Windows Virtual Desktop](https://www.microsoft.com/microsoft-365/modern-desktop/enterprise/windows-virtual-desktop).

The sync app also supports non-persistent environments that have [FSLogix Apps 2.8 or later](https://fslogix.com/products/fslogix-apps), [FSLogix Microsoft 365 Container](https://fslogix.com/products/microsoft-365-container), and a Microsoft 365 subscription for all of the following operating systems:

- Windows 10, 32 or 64-bit (supports VHDX files) 
- Windows 7, 32 or 64-bit (supports VHD files) 
- Windows Server 2019 (supports VHDX)
- Windows Server 2016 (supports VHDX)
- Windows Server 2012 R2 (supports VHDX)
- Windows Server 2008 R2 (supports VHD)

 Using the OneDrive sync app with non-persistent environments requires that you [install the sync app per machine](https://docs.microsoft.com/onedrive/per-machine-installation).

> [!NOTE]
> If you are running FSLogix with Files On-Demand on Windows 10 or Windows Sever 2019, the minimum supported versions are: OneDrive 19.174.0902.0013, FSLogix Apps 1909 HF_01 (2.9.7237.48865).

> [!NOTE]
> For Windows Server, the [SMB network file sharing protocol](/windows-server/storage/file-server/file-server-smb-overview) is also required.

## See also

Learn more about [VHDX](/openspecs/windows_protocols/ms-vhdx/83f6b700-6216-40f0-aa99-9fcb421206e2) and [VHD](/windows/desktop/vstor/about-vhd).

For info about creating virtual hard disks, see [Manage virtual hard disks](/windows-server/storage/disk-management/manage-virtual-hard-disks).
