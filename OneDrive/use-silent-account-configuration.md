---
title: "Silently configure user accounts"
ms.reviewer: wsproule
ms.author: kaarins
author: kaarins
manager: pamgreen
audience: ITPro
f1.keywords:
- NOCSH
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
ms.custom: seo-marvel-apr2020
description: "Learn how IT admins can enable silent account configuration when deploying the OneDrive sync app in an enterprise."
---

# Silently configure user accounts

This article is for IT admins who would like to silently configure user accounts when deploying the new OneDrive sync app (OneDrive.exe) to managed Windows computers in their enterprise. This feature works for computers that are joined to Azure Active Directory (Azure AD).
  
If you enable this feature, OneDrive.exe will attempt to silently (without user interaction) sign in to the work or school user account that was used to sign into Windows (known as the Windows Primary Account). That windows account must be an Azure Active Directory (AAD) account or be linked to an AAD account through a hybrid authentication configuration (see Prerequisites below). Before OneDrive.exe begins syncing, it will check the available disk space. If syncing the user's entire OneDrive would cause the available space to drop below 1 GB or if the size exceeds the threshold you set (on devices that don't have Files On-Demand enabled), OneDrive will prompt the user to choose folders to sync. For info about setting this threshold using Group Policy, see [Set the maximum size of a user's OneDrive that can download automatically](use-group-policy.md#set-the-maximum-size-of-a-users-onedrive-that-can-download-automatically). 
  
When the user is configured in the sync client, if the same user account is syncing files with the previous OneDrive for Business sync app (Groove.exe), the new sync app (OneDrive.exe) will attempt to take over syncing those files.

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
  
1. Enable silent account configuration. For info, see [Silently sign in users to the OneDrive sync app with their Windows credentials](use-group-policy.md#silently-sign-in-users-to-the-onedrive-sync-app-with-their-windows-credentials). 
    
2. Optionally, specify the maximum OneDrive size that will download automatically in silent configuration. For info, see [Set the maximum size of a user's OneDrive that can download automatically](use-group-policy.md#set-the-maximum-size-of-a-users-onedrive-that-can-download-automatically). Note that if you enable Files On-Demand, OneDrive will ignore the maximum size value.
    
3. Optionally, set the default location for the OneDrive folder. For info, see [Set the default location for the OneDrive folder](use-group-policy.md#set-the-default-location-for-the-onedrive-folder).
    
> [!TIP]
> See the [Verify SilentAccountConfig](use-silent-account-configuration.md#VerifySilentAccountConfig) section below to verify and troubleshoot your configuration.
  
> [!NOTE]
> Silent account configuration won't work on devices for users who require multi-factor authentication. Select third-party identity providers (IdPs) are supported, but there are caveats. For more information, make sure to check out the [Azure AD federation compatibility list](/azure/active-directory/hybrid/how-to-connect-fed-compatibility).

If the computers on your network are not connected to Active Directory on-premises, but only to Azure AD, we recommend using Intune and a Microsoft PowerShell script to set the registry keys required to enable silent config. Be sure you have [automatic enrollment set up for Windows 10 devices](/intune/quickstart-setup-auto-enrollment). 

Using a script:

```PowerShell
$HKLMregistryPath = 'HKLM:\SOFTWARE\Policies\Microsoft\OneDrive'##Path to HKLM keys
$DiskSizeregistryPath = 'HKLM:\SOFTWARE\Policies\Microsoft\OneDrive\DiskSpaceCheckThresholdMB'##Path to max disk size key
$TenantGUID = 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'

if(!(Test-Path $HKLMregistryPath)){New-Item -Path $HKLMregistryPath -Force}
if(!(Test-Path $DiskSizeregistryPath)){New-Item -Path $DiskSizeregistryPath -Force}

New-ItemProperty -Path $HKLMregistryPath -Name 'SilentAccountConfig' -Value '1' -PropertyType DWORD -Force | Out-Null ##Enable silent account configuration
New-ItemProperty -Path $DiskSizeregistryPath -Name $TenantGUID -Value '102400' -PropertyType DWORD -Force | Out-Null ##Set max OneDrive threshold before prompting
``` 

## Windows Image Prep requirements

SilentAccountConfig creates a SilentBusinessConfigCompleted registry entry once SilentAccountConfig has successfully provisioned the user in OneDrive.exe. This prevents SilentAccountConfig from reprovisioning the user in OneDrive.exe if the user manually stops syncing.

If SilentAccountConfig has successfully completed on a machine you're going to use as your master for building a Windows deployment image (i.e. SysPrep), you need to ensure this registry key is removed before you prepare your image. You can do so by running the following command:

```console
reg delete HKCU\Software\Microsoft\OneDrive /v SilentBusinessConfigCompleted /f
```

<a name="VerifySilentAccountConfig"></a>
## Verify SilentAccountConfig

### Instructions for SharePoint Online (SPO):
1. Unlink all pre-existing Business instances in OneDrive.

2. Clear the registry of any previous successful Silent Business Config runs:

   ```console
   reg delete HKCU\Software\Microsoft\OneDrive /v SilentBusinessConfigCompleted /f
   ```

3. Set the Silent Config policy registry entry (must be run from an administrator CMD window):

   ```console
   reg add HKLM\SOFTWARE\Policies\Microsoft\OneDrive /v SilentAccountConfig /t REG_DWORD /d 0x1 /f
   ```

4. Sign out of Windows (Ctrl+Alt+Delete Sign Out).

5. Sign into Windows.

6. Shortly you should see a blue cloud tray icon. Clicking on the blue cloud tray icon should show the activity center pop-up showing ongoing/recent activity from the first sync. If so, SilentAccountConfig has worked correctly.

7. If instead, you see the "Set up OneDrive" first run wizard dialog, SilentAccountConfig was unable to silently sign in or failed for another reason. Verify you have completed these steps correctly by repeating them again. Perform the [Verify Single Sign On (SSO)](use-silent-account-configuration.md#VerifySSO) steps below to confirm that SSO is not a problem. Gather sync client logs to send to the engineering team for further help.
 
### Instructions for On-Premises SharePoint 2019+ Server:

1. Ensure you can manually get the OneDrive sync client to sync content with your on-premises SharePoint 2019 Server before proceeding. See [Configure sync app for syncing with SharePoint Server](/sharepoint/install/new-onedrive-sync-client) for details.

2. Set the SharePointOnPremPrioritization reg key value to 1 (this will ensure on-premises takes precedence over SPO, deleting the reg key to revert to SPO):

   ```console
   reg add HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\OneDrive /v SharePointOnPremPrioritization /t REG_DWORD /d 0x1 /f
   ```

3. Follow steps 1 through 6 in the SPO instructions above.

4. If instead, you see the "Set up OneDrive" first run wizard dialog, SilentAccountConfig was unable to silently sign in or failed for another reason. Verify you have completed these steps correctly by repeating them again. Gather sync client logs to send to the engineering team for further help.

### To prevent Silent Business Config:

```console
reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\OneDrive /v SilentAccountConfig /f
```

<a name="VerifySSO"></a>
## Verify that Single Sign On (SSO) is working

The most common reason for SilentAccountConfig to fail is the credentials are not available to OneDrive.exe without user interaction. Proceed with these instructions to determine if this is a problem in your case.

If you have a machine you think should work with SilentAccountConfig you can manually verify that SSO is working correctly to ensure that the environment is configured correctly.
 
1. Temporarily force ADAL on by running this command:

   ```console
   reg add HKCU\Software\Microsoft\OneDrive /v EnableADAL /t REG_DWORD /d 1 /f
   ```

2. Shut down any running OneDrive.exe processes (verify in the Task Manager Details tab - Ctrl+Shift+Esc).

3. Start menu - OneDrive, you should see the **Set up OneDrive** dialog (if not unlink/stop syncing any business accounts and start over).

4. Enter the same email address that the user used to sign into Windows (try alias@domain and domain\alias forms).

5. Click the **Sign In** button on the dialog.

6. The dialog should switch to a "signing in" page with a spinning icon for a few seconds. It should then proceed to the next part of the wizard without asking for a password.

7. If you do not get a password prompt, congratulations, your auth environment is properly configured and SilentAccountConfig should work for your users.

8. If you do see a password prompt, the environment is not configured properly for silent sign on.  This could be due to a problem with how the machine is domain joined (for example, a trust relationship problem), a problem with ADFS configuration, an AAD CA policy requiring user interaction, you didn't provide the same user email address as the one used to sign into Windows, or some other reason.  You will need to resolve whatever is blocking silent sign on before SilentAccountConfig will work for you.

9. Remove the EnableADAL key you added in step 1:

   ```console
   reg delete HKCU\Software\Microsoft\OneDrive /v EnableADAL /f
   ```

> [!NOTE]
> When using SilentAccountConfig, you do not need to specify EnableADAL=1.  This is only necessary when manually testing SSO in the above steps where we manually sign in (instead of using SilentAccountConfig to sign in).  However, if you want users who manually set up OneDrive sync to benefit from SSO to minimize how often they need to enter a password in sync, you can deploy the EnableADAL key on your users' computers.
