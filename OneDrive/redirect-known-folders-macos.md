---
title: "Redirect and move macOS known folders to OneDrive"
ms.reviewer: cagreen
ms.author: mabond
author: mkbond007
manager: serdars
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: one-drive
ms.localizationpriority: medium
ms.collection: 
- Strat_OD_admin
- M365-collaboration
- m365initiative-healthyonedrive
- onedrive-toc
ms.custom:
search.appverid:
- ODB160
- ODB150
- GOB150
- GOB160
- MET150
description: In this article, you'll learn how to redirect users' Desktop and Documents folders to OneDrive on macOS using Folder Backup (Known Folder Move).
---
# Redirect and move macOS Desktop and Documents folders to OneDrive

This article is for IT admins managing the OneDrive sync app for macOS.
  
There are two primary advantages of moving or redirecting macOS Desktop and Documents folders to Microsoft OneDrive for the users in your organization:
  
- Your users can continue using the folders they're familiar with. They don't have to change their daily work habits to save files to OneDrive.

- Saving files to OneDrive backs up your users' data in the cloud and gives them access to their files from any device.

For these reasons, we recommend moving or redirecting Desktop and Documents folders to OneDrive if you're an enterprise or large organization. [See all our recommendations for configuring the sync app](ideal-state-configuration.md). Small or medium businesses may also find this useful, but keep in mind you'll need some experience configuring policies. For info about the end-user experience, see [Protect your files by saving them to OneDrive](https://support.office.com/article/d61a7930-a6fb-4b95-b28a-6552e77c3057).

> [!NOTE]
> OneDrive sync for macOS will now run natively on Apple silicon. This means that OneDrive will take full advantage of the performance improvements of Apple silicon. This support is generally available starting with build 22.022. Users will be automatically updated over the next few releases.
>
> If you are running the Standalone app and would like to install the Apple silicon version sooner, you can download the latest build from the [OneDrive relase notes for Mac](https://support.microsoft.com/en-us/office/onedrive-release-notes-845dcf18-f921-435e-bf28-4e24b95e5fc0#OSVersion=Mac).

## Prepare to move Desktop and Documents folders on existing devices

The [standalone OneDrive sync app](https://support.microsoft.com/en-us/office/onedrive-release-notes-845dcf18-f921-435e-bf28-4e24b95e5fc0#OSVersion=Mac) (not from the Mac App Store) is required for folder backup. This app requires Full Disk Access, which can be granted and deployed by IT admins. 

We recommend that you upgrade to the latest available build before you deploy to decrease deployment issues.

> [!IMPORTANT]
> If your organization is large and your users have a lot of files in their Desktop and Documents folders, make sure you roll out the configuration slowly to minimize the network impact of uploading files. For users who have a lot of files in their folders, consider using the setting [AutomaticUploadBandwidthPercentage](deploy-and-configure-on-macos.md#automaticuploadbandwidthpercentage) temporarily to minimize the network impact and then disable the setting once uploads are complete.
  
## About the Folder Backup settings

You can set OneDrive settings using software distribution tools such as [Microsoft Intune](/mem/intune/apps/apps-add-office365-macOS) as well as [Jamf Pro](https://www.jamf.com/products/jamf-pro/), [Munki](https://www.munki.org/), [AutoPkg](https://github.com/autopkg/autopkg), [Apple Remote Desktop](https://support.apple.com/guide/remote-desktop/welcome/mac), and [AppleScript](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptX/AppleScriptX.html). You can also configure keys in a .plist file. For a full reference of available preferences and their settings, see [Deploy and configure the OneDrive sync app for macOS](deploy-and-configure-on-macos.md).  

For new machines, Folder Backup can be configured from the start, so all new files are uploaded to the cloud. This is great for organizations as it increases user engagement with OneDrive, and admins can easily protect files with enterprise-level security and compliance that comes built in.

The following settings control the Folder Backup feature:
  
- [Prompt users to move Desktop and Documents folders to OneDrive](deploy-and-configure-on-macos.md#kfmoptinwithwizard)

    Use this setting to give the users a call to action to move their Desktop and Documents macOS folders.

    If users dismiss the prompt, a reminder notification will appear in the activity center until they move all available folders.

    If a user has already redirected their known folders to a different OneDrive account, they'll be prompted to direct the folders to the account for your organization (leaving existing files behind).
    
    > [!IMPORTANT]
    > We recommend deploying the prompt policy for existing devices only, and limiting the deployment to 5,000 devices a day and not exceeding 20,000 devices a week.
  
- [Silently move macOS Desktop and Documents folders to OneDrive](deploy-and-configure-on-macos.md#kfmsilentoptin)
    
    Use this setting to redirect and move folders to OneDrive without any user interaction. Move all the folders or select the desired individual folders. By default, the Desktop and Documents folders will be moved. After a folder is moved, the policy won't affect the folder again, even if the selection for the folder changes.

    > [!NOTE]
    > You can choose to display a notification to users after their folders have been redirected.

    Various errors can prevent this setting from taking effect, such as:

    - A file exceeds the maximum path length
    - The known folders aren't in the default locations
    - Folder protection is unavailable
    - Known folders are prohibited from being redirected

    For info about these errors, see [Fix problems with folder protection](https://support.office.com/article/d61a7930-a6fb-4b95-b28a-6552e77c3057#BKMK_FixProblems).

    > [!IMPORTANT]
    > We recommend deploying the silent policy for existing devices and new devices while limiting the deployment of existing devices to 1,000 devices a day and not exceeding 4,000 devices a week. We also recommend using this setting together with [KFMOptInWithWizard](deploy-and-configure-on-macos.md#kfmoptinwithwizard). If moving the Desktop and Documents folders silently does not succeed, users will be prompted to correct the error and continue.
   
- [Prevent users from redirecting their macOS Desktop and Documents folders to their Mac](deploy-and-configure-on-macos.md#kfmblockoptout)

    Use this setting to force users to keep their Desktop and Documents folders directed to OneDrive.
  
- [Prevent users from moving their macOS Desktop and Documents folders to OneDrive](deploy-and-configure-on-macos.md#kfmblockoptin)
    
    Use this setting to force users from moving their Desktop and Documents folders to any OneDrive account.

For info about using the OneDrive sync settings, see [Deploy and configure the OneDrive sync app for macOS](deploy-and-configure-on-macos.md).