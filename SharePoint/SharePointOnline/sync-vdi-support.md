---
ms.date: 09/09/2024
title: "Use the sync app on virtual desktops"
ms.reviewer: kafeaver
ms.author: mactra
author: MachelleTranMSFT
manager: jtremper
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
  - Windows 10 and 11, 32-bit or 64-bit (supports VMDK files)
  - Windows Server 2022 (supports VHDX)
  - Windows Server 2019 (supports VHDX)
  - Windows Server 2016 (supports VHDX)
  - Windows Server 2012 R2 (supports VHDX)

> [!NOTE]
> It is not supported to roam the OneDrive registry hive as part of a non-persistent VDI environment. Do not roam `HKEY_CURRENT_USER\Software\Microsoft\OneDrive\` in your non-persistent VDI user profiles.

> [!NOTE]
> The minimum supported versions are: OneDrive 19.174.0902.0013 and FSLogix Apps [2.9.7653.47581](/fslogix/whats-new).
>
> Using the OneDrive sync app with non-persistent environments requires that you [install the sync app per machine](./per-machine-installation.md).
>
> For Windows Server, the [SMB network file sharing protocol](/windows-server/storage/file-server/file-server-smb-overview) is also required.
>
> The OneDrive sync app is supported in a remote app scenario hosted as a Citrix Virtual App.
>
> The OneDrive sync app with FSLogix does not support running multiple instances of the same container simultaneously.

## Set up OneDrive in Citrix Virtual Apps

This article describes how to enable and use OneDrive in Citrix Virtual Apps.

### Prerequisites

To enable OneDrive in Citrix Virtual Apps, you must have the following versions of Windows and Citrix Virtual Apps and Desktops (CVAD):

**Windows**:

- Windows 11: KB5014019
- Windows Server 2022: KB5014021
- Windows 10: KB5014023
- Windows Server 2019: KB5014022

**Citrix**:

- CVAD 7 2203 LTSR CU1 or later.
- VDA 2212 enables Shellbridge by default. All earlier versions require Shellbridge to be enabled manually.
- To enable this feature, On 2203 LTSR TS VDA (2019 Server, 2022 Server, Windows 10 RDSH, or Windows 11 RDSH) add the following registry details:

    `HKEY_LOCAL_MACHINE\SOFTWARE\Citrix\Citrix Virtual Desktop Agent`<p>
    `Name: Shellbridge`<p>
    `Type: REG_DWORD`<p>
    `Value: 1`

To ensure that the feature is correctly enabled, open a command window (cmd.exe) and run `start ms-settings:printers`. If the feature is enabled, the printer setting window is displayed.

**We recommend adding OneDrive.exe to `LogoffCheckSysModules`**.

   `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Citrix\wfshell\TWI` <p>
   `Value Name:LogoffCheckSysModules` <p>
   `Type:REG_SZ` <p>
   `String:OneDrive.exe, Microsoft.Sharepoint.exe` <p>

> [!IMPORTANT]
> [FSLogix](/fslogix/how-to-install-fslogix) must be used in conjunction with Citrix Virtual Apps for OneDrive to be supported.

### How to set up OneDrive

1. Install OneDrive Sync app per machine. See [Install the sync app per-machine](per-machine-installation.md).
1. Install the latest version of FSLogix. See [Install FSLogix Applications](/fslogix/how-to-install-fslogix).

    > [!NOTE]
    > All non-persistent VDI environments require the latest version of FSLogix. Ensure you install the latest version. See [OneDrive sync error FSLogix_unsupported_environment on VMs](/sharepoint/troubleshoot/sync/fslogix-unsupported-environment-sync-error-vm).

1. Add OneDrive to `HKLM\Software\Microsoft\Windows\CurrentVersion\` by using the following command:

    `REG ADD HKLM\Software\Microsoft\Windows\CurrentVersion\Run /v OneDrive /t REG_SZ /d "\"C:\Program Files\Microsoft OneDrive\OneDrive.exe\" /background"`

1. Silently configure user accounts. See [Silently configure user accounts](use-silent-account-configuration.md).

    > [!NOTE]
    > Silent sign-in should work if your machine is connected to Microsoft Entra ID. Make sure to turn off this setting if your computer is not Microsoft Entra joined.

## See also

Learn more about [VHDX](/openspecs/windows_protocols/ms-vhdx/83f6b700-6216-40f0-aa99-9fcb421206e2) and [VHD](/windows/desktop/vstor/about-vhd).

For info about creating virtual hard disks, see [Manage virtual hard disks](/windows-server/storage/disk-management/manage-virtual-hard-disks).
