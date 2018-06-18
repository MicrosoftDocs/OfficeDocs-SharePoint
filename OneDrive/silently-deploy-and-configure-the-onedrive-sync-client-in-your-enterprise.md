---
title: "Silently deploy and configure the OneDrive sync client in your enterprise"
ms.author: kaarins
author: kaarins
ms.date: 5/30/2018
ms.audience: ITPro
ms.topic: article
ms.prod: office-online-server
localization_priority: Normal
ms.assetid: 64aa1f56-d7f6-4500-a408-1fde8fe6db36
description: "This article is for IT admins who would like to silently deploy and configure the new OneDrive sync client (OneDrive.exe) to managed Windows computers in their enterprise. This feature works for computers that are joined to Azure Active Directory (Azure AD)."
---

# Silently deploy and configure the OneDrive sync client in your enterprise

This article is for IT admins who would like to silently deploy and configure the new OneDrive sync client (OneDrive.exe) to managed Windows computers in their enterprise. This feature works for computers that are joined to Azure Active Directory (Azure AD).
  
## Overview

If you enable this feature, OneDrive.exe will attempt to sign in to the work or school account on the device that's joined to Azure AD. It will check the available disk space before syncing, and if it is large, OneDrive will prompt the user to choose folders to sync. You can [configure the size threshold by using Group Policy](use-group-policy.md#MaxOneDriveSize). 
  
If you enable this setting and the user is syncing files with the previous OneDrive for Business sync client (Groove.exe), the new sync client (OneDrive.exe) will attempt to take over syncing and import the user's sync settings. 
  
## Prerequisites

Before you can enable silent configuration, you need to join your devices to Azure AD. You can join devices running Windows 10 and Windows Server 2016 directly to Azure AD. To learn how, see [Set up Azure Active Directory joined devices](https://go.microsoft.com/fwlink/?linkid=864414).
  
If you have an on-premises environment that uses Active Directory, you can enable "hybrid Azure AD joined devices" to join devices on your domain to Azure AD. Devices must be running one of the following operating systems:
  
- Windows 10 
    
- Windows 8.1 
    
- Windows 7 
    
- Windows Server 2016 
    
- Windows Server 2012 R2 
    
- Windows Server 2012 
    
- Windows Server 2008 R2
    
> [!NOTE]
> For more info, see [How to configure hybrid Azure Active Directory joined devices](https://go.microsoft.com/fwlink/?linkid=864140). To check the join status and fix problems, see [Troubleshoot hybrid Azure AD-joined devices](https://go.microsoft.com/fwlink/?linkid=864415). 
  
## Enable silent configuration

1. Use Group Policy to enable silent configuration.  For info, see [Silently configure OneDrive using Windows 10 or domain credentials](use-group-policy.md#SilentConfig).
    
2. Use Group Policy to specify the maximum OneDrive size that will download automatically in silent configuration. For info, see [Configure the maximum OneDrive size for downloading all files automatically](use-group-policy.md#MaxOneDriveSize).
    
3. Optionally, use Group Policy to set the default location for the OneDrive folder. For info, see [Set the default location for the OneDrive folder](use-group-policy.md#DefaultRootDir).
    
## Send feedback
<a name="sendfeedback"> </a>

Please let us know if you have feedback on this feature or encounter any issues:
  
1. Right-click the blue OneDrive icon in the notification area, at the far right of the taskbar.
    
2. Click **Report a problem**.
    
3. Enter a brief description and include the phrase "SilentConfig" in your message to send your feedback directly to engineers working on this feature. 
    
4. Click **OK**. You'll receive an email message with a ticket number to track your feedback.
    

