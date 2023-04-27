---
ms.date: 04/19/2023
title: Set up OneDrive in Citrix Virtual Apps
ms.reviewer: gacarini
ms.author: mikeplum
author: MikePlumleyMSFT
manager: serdars
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: one-drive
ms.localizationpriority: medium
ms.custom:
- Adm_O365
search.appverid:
- MET150
- BCS160
ms.collection:
- Strat_OD_admin
- M365-collaboration
description: In this article, you'll learn how to enable OneDrive in Citrix Virtual Apps.
---

# Set up OneDrive in Citrix Virtual Apps

This article describes how to enable and use OneDrive in Citrix Virtual Apps.

## Prerequisites:

To enable OneDrive in Citrix Virtual Apps, you must have the following  versions of Windows and Citrix Virtual Apps and Desktops (CVAD):

**Windows**:

- Windows 11: KB5014019 
- Windows Server 2022: KB5014021
- Windows 10: KB5014023
- Windows Server 2019: KB5014022

**Citrix**:

- CVAD 7 2203 LTSR CU1 or later 
- VDA 2212 enables Shellbridge by default, all earlier versions require Shellbridge to be enabled manually  
- To enable this feature, On 2203 LTSR TS VDA (2019 Server, 2022 Server, Windows 10 RDSH or Windows 11 RDSH) add the following registry details: 

    `HKEY_LOCAL_MACHINE\SOFTWARE\Citrix\Citrix Virtual Desktop Agent`<p>
    `Name: Shellbridge`<p>
    `Type: REG_DWORD`<p>
    `Value: 1`

  To ensure that the feature is correctly enabled, Launch a published command prompt (cmd.exe) and run start `ms-settings:printers`. If the feature is enabled, the printer setting window is displayed.

**We recommend adding OneDrive.exe to `LogoffCheckSysModules`**.

    `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Citrix\wfshell\TWI` <p>
    `Value Name:LogoffCheckSysModules` <p>
    `Type:REG_SZ` <p>
    `String:OneDrive.exe, Microsoft.Sharepoint.exe` 

 
> [!IMPORTANT]
> [FSLogix](/fslogix/how-to-install-fslogix) must be used in conjunction with Citrix Virtual Apps for OneDrive to be supported.

## How to setup OneDrive

1. Install OneDrive Sync app per machine. See [Install the sync app per-machine](per-machine-installation.md).
1. Install the latest version of FSLogix. See [Install FSLogix Applications](/fslogix/how-to-install-fslogix).

    > [!NOTE]
    > All non-persistent VDI environments require the latest version of FSLogix. Ensure you install the latest version.

1. Add OneDrive to HKLM\Software\Microsoft\Windows\CurrentVersion\Run by using the following command.

    `REG ADD HKLM\Software\Microsoft\Windows\CurrentVersion\Run /v OneDrive /t REG_SZ /d "\"C:\Program Files\Microsoft OneDrive\OneDrive.exe\" /background"`

1. Silently configure user accounts. See [Silently configure user accounts](use-silent-account-configuration.md).

    > [!NOTE]
    > Silent sign-in should function if your machine is connected to Azure Active Directory. Make sure to turn off this setting if your computer is not Azure AD-joined.
