---
title: "Sync on virtual desktops"
ms.author: kaarins
author: kaarins
manager: pamgreen
ms.audience: Admin
ms.topic: article
ms.service: one-drive
localization_priority: Normal
ms.custom: Adm_O365
search.appverid:
- MET150
- BCS160
ms.collection: 
- Strat_OD_admin
- M365-collaboration
ms.assetid: 6891b561-a52d-4ade-9f39-b492285e2c9b
description: "Learn about the OneDrive sync client support for desktop virtualization."
---

# Sync on virtual desktops

For all supported operating systems, the OneDrive sync client supports:

- Virtual desktops that persist between sessions. 
- Non-persistent environments that use [Windows Virtual Desktop preview](https://www.microsoft.com/microsoft-365/modern-desktop/enterprise/windows-virtual-desktop).

The sync client also supports non-persistent environments that have:

- [FSLogix Apps 2.8 or later](https://fslogix.com/products/fslogix-apps) and [FSLogix Office 365 Container](https://fslogix.com/products/office-365-container) 
- A Microsoft 365 or Office 365 subscription

For all of the following operating systems:

- Windows 10, 32 or 64-bit (supports VHDX files) 
- Windows 7, 32 or 64-bit (supports VHD files) 
- Windows Server 2016 R2 or Windows Server 2012 R2 (both support VHDX)
- Windows Server 2008 R2 (supports VHDX and VHD)

> [!NOTE]
> For Windows Server, the [SMB network file sharing protocol](/windows-server/storage/file-server/file-server-smb-overview) is also required. 

## See also

Learn more about [VHDX](/openspecs/windows_protocols/ms-vhdx/83f6b700-6216-40f0-aa99-9fcb421206e2) and [VHD](/windows/desktop/vstor/about-vhd)

For info about creating virtual hard disks, see [Manage virtual hard disks](/windows-server/storage/disk-management/manage-virtual-hard-disks)

[OneDrive for Business and VDI environments](/deployoffice/rds-onedrive-business-vdi)
