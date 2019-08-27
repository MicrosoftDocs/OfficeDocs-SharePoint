---
title: "Silently configure user accounts"
ms.reviewer: 
ms.author: kaarins
author: kaarins
manager: pamgreen
audience: ITPro
ms.topic: article
ms.service: one-drive
localization_priority: Normal
ms.collection: 
- Strat_OD_admin
- M365-collaboration
search.appverid:
- ODB160
- MET150
ms.assetid: 64aa1f56-d7f6-4500-a408-1fde8fe6db36
description: "Learn how IT admins can enable silent account configuration when deploying the OneDrive sync client in an enterprise."
---

# Silently configure user accounts

This article is for IT admins who would like to silently configure user accounts when deploying the new OneDrive sync client (OneDrive.exe) to managed Windows computers in their enterprise. This feature works for computers that are joined to Azure Active Directory (Azure AD).
  
## Overview

If you enable this feature, OneDrive.exe will attempt to sign in to the work or school account on the device that's joined to Azure AD. Before if begins syncing, it will check the available disk space. If syncing the user's entire OneDrive would cause the available space to drop below 1 GB or if the size exceeds the threshold you set (on devices that don't have Files On-Demand enabled), OneDrive will prompt the user to choose folders to sync. For info about setting this threshold using Group Policy, see [Set the maximum size of a user's OneDrive that can download automatically](use-group-policy.md#DiskSpaceCheckThresholdMB). 
  
If you enable this setting and the user is syncing files with the previous OneDrive for Business sync client (Groove.exe), the new sync client (OneDrive.exe) will attempt to take over syncing and import the user's sync settings. 
  
## Prerequisites

Before you can enable silent account configuration, you need to join your devices to Azure AD. You can join devices running Windows 10 and Windows Server 2016 directly to Azure AD. To learn how, see [Join your work device to your organization's network](/azure/active-directory/user-help/user-help-join-device-on-network). 
  
If you have an on-premises environment that uses Active Directory, you can enable [hybrid Azure AD joined devices](/azure/active-directory/devices/hybrid-azuread-join-plan) to join devices on your domain to Azure AD. Devices must be running one of the following operating systems:
  
- Windows 10 
    
- Windows 8.1 
    
- Windows 7 

- Windows Server 2019
    
- Windows Server 2016 
    
- Windows Server 2012 R2 
    
- Windows Server 2012 
    
- Windows Server 2008 R2

If you federate your on-premises Active Directory with Azure AD, you must use AD FS to enable this feature. For info about using Azure AD Connect, see [Getting started with Azure AD Connect using express settings](/azure/active-directory/hybrid/how-to-connect-install-custom).
    
> [!NOTE]
> For more info, see [How to configure hybrid Azure Active Directory joined devices](/azure/active-directory/devices/hybrid-azuread-join-plan). To check the join status and fix problems, see [Troubleshoot hybrid Azure AD-joined devices](/azure/active-directory/devices/troubleshoot-hybrid-join-windows-current). 
  
## Enable silent configuration

If the computers on your network are joined to Active Directory on-premises, you can use domain group policy to configure silent account configuration.

Using Group Policy:
  
1. Enable silent account configuration. For info, see [Silently sign in users to the OneDrive sync client with their Windows credentials](use-group-policy.md#SilentAccountConfig). If a device is not already joined to Azure AD, enabling this setting will join it.
    
2. Optionally, specify the maximum OneDrive size that will download automatically in silent configuration. For info, see [Set the maximum size of a user's OneDrive that can download automatically](use-group-policy.md#DiskSpaceCheckThresholdMB). Note that if you enable Files On-Demand, OneDrive will ignore the maximum size value.
    
3. Optionally, set the default location for the OneDrive folder. For info, see [Set the default location for the OneDrive folder](use-group-policy.md#DefaultRootDir).
    
> [!TIP]
> To test single sign-on, run OneDrive setup using the /silent parameter and enter your user name. Setup should not prompt for credentials. 
  
> [!NOTE]
> Silent account configuration won't work on devices for which you've required multi-factor authentication. Select third-party identity providers (IdPs) are supported, but there are caveats. For more information, make sure to check out the [Azure AD federation compatibility list](/azure/active-directory/hybrid/how-to-connect-fed-compatibility).

If the computers on your network are not connected to Active Directory on-premises, but only to Azure AD, we recommend using Intune and a Microsoft PowerShell script to set the registry keys required to enable silent config. Be sure you have [automatic enrollment set up for Windows 10 devices](/intune/quickstart-setup-auto-enrollment). 

Using a script:

```PowerShell
$HKLMregistryPath = 'HKLM:\SOFTWARE\Policies\Microsoft\OneDrive'##Path to HKLM keys

$DiskSizeregistryPath = 'HKLM:\SOFTWARE\Policies\Microsoft\OneDrive\DiskSpaceCheckThresholdMB'##Path to max disk size key

$TenantGUID = 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'

IF(!(Test-Path $HKLMregistryPath))

{New-Item -Path $HKLMregistryPath -Force}

IF(!(Test-Path $DiskSizeregistryPath))

{New-Item -Path $DiskSizeregistryPath -Force}

New-ItemProperty -Path $HKLMregistryPath -Name 'SilentAccountConfig' -Value '1' -PropertyType DWORD -Force | Out-Null ##Enable silent account configuration

New-ItemProperty -Path $DiskSizeregistryPath -Name $TenantGUID -Value '102400' -PropertyType DWORD -Force | Out-Null ##Set max OneDrive threshold before prompting
``` 

## Send feedback
<a name="sendfeedback"> </a>

Please let us know if you have feedback on this feature or encounter any issues:
  
1. Right-click the blue OneDrive icon in the notification area, at the far right of the taskbar.
    
2. Click **Report a problem**.
    
3. Enter a brief description and include the phrase "SilentConfig" in your message to send your feedback directly to engineers working on this feature. 
    
4. Click **OK**. You'll receive an email message with a ticket number to track your feedback.
    

