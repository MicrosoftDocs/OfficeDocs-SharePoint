---
ms.date: 03/15/2019
title: OneDrive in Citrix Virtual Apps Deployment Guide
ms.reviewer: gacarini
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
- seo-marvel-apr2020
- onedrive-toc
search.appverid:
- MET150
- BCS160
ms.collection:
- Strat_OD_admin
- M365-collaboration
ms.assetid: 6891b561-a52d-4ade-9f39-b492285e2c9b
description: In this article, you'll learn how to enable OneDrive in Citrix Virtual Apps.
---

# OneDrive in Citrix Virtual Apps Deployment Guide

This deployment guide describes how to enable and use OneDrive in Citrix Virtual Apps. The reference links provided in this guide help IT administrators to deploy and manage the OneDrive sync app.

## Prerequisites:

To enable OneDrive in Citrix Virtual Apps, you must have the following  versions of Windows and Citrix Virtual Apps and Desktops (CVAD):

**Windows**:

- Windows 11: KB5014019 
- Windows Server 2022: KB5014021
- Windows 10: KB5014023
- Windows Server 2019: KB5014022

**Citrix**:

- [VDA](https://docs.citrix.com/en-us/citrix-virtual-apps-desktops.html) 2206 
- Only the multi-session OS VDA component is required for testing OneDrive. 
- To enable this feature, add the following registry details: 

    `HKEY_LOCAL_MACHINE\SOFTWARE\Citrix\Citrix Virtual Desktop Agent`<p>
    `Name: Shellbridge`<p>
    `Type: REG_DWORD`<p>
    `Value: 1`
    
    > [!IMPORTANT]
    > [FSLogix](/fslogix/how-to-install-fslogix) must be used in conjunction with Citrix Virtual Apps for OneDrive to be supported.

## How to setup OneDrive

1. Install OneDrive Sync app per machine. See [Install the sync app per-machine](per-machine-installation.md).
1. Install the latest version of FSLogix. See [Install FSLogix Applications.](/fslogix/how-to-install-fslogix)

    > [!NOTE]
    > All non-persistent VDI environments require the latest version of FSLogix. Ensure you install the latest version.

1. Silently configure user accounts. See [Silently configure user accounts - OneDrive | Microsoft Learn.](use-silent-account-configuration.md)

    > [!NOTE]
    > Silent sign-in should function if your machine is connected to Azure Active Directory (AAD). Make sure to turn off this setting if your computer is not AAD-joined.