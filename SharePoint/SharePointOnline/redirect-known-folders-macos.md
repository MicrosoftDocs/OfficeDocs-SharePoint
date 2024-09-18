---
ms.date: 09/16/2024
title: "Redirect and move macOS known folders to OneDrive"
ms.reviewer: cagreen
ms.author: mactra
author: MachelleTranMSFT
manager: jtremper
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

For these reasons, we recommend moving (redirecting) Desktop and Documents folders to OneDrive with Folder Backup if you're an enterprise or large organization. [See all our recommendations for configuring the sync app](ideal-state-configuration.md). Small or medium businesses may also find this useful, but keep in mind you'll need some experience configuring settings. For info about the end-user experience, see [Protect your files by saving them to OneDrive](https://support.office.com/article/d61a7930-a6fb-4b95-b28a-6552e77c3057).

> [!NOTE]
> OneDrive sync for macOS runs natively on Apple silicon. This support is generally available starting with build 22.022.

## Prepare to move Desktop and Documents folders on existing devices

The [standalone OneDrive sync app](https://support.microsoft.com/office/845dcf18-f921-435e-bf28-4e24b95e5fc0#OSVersion=Mac) (not from the Mac App Store) is required for Folder Backup. This app requires Full Disk Access, which can be granted and deployed by IT admins. For more information, see [Configure device restriction settings in Microsoft Intune](/mem/intune/configuration/device-restrictions-configure).

We recommend that you upgrade to the latest available build before you deploy.

<!---
For information on issues that can prevent folders from being moved, see [Fix problems with folder protection](https://support.office.com/article/d61a7930-a6fb-4b95-b28a-6552e77c3057#BKMK_FixProblems). 
--->

> [!IMPORTANT]
> If your organization is large and your users have a lot of files in their Desktop and Documents folders, make sure you roll out the configuration slowly to minimize the network impact of uploading files. For users who have a lot of files in their folders, consider using the setting [AutomaticUploadBandwidthPercentage](deploy-and-configure-on-macos.md#automaticuploadbandwidthpercentage) temporarily to minimize the network impact and then disable the setting once uploads are complete.

### Folders redirected to other organizations

If a user’s Desktop and Documents folders are currently redirected to OneDrive in a different organization, redirecting to your organization’s OneDrive will create new Desktop and Documents folders and the user will see an empty desktop. The user will have to manually migrate files from the other organization’s OneDrive to OneDrive in your organization. We recommend that you disable the redirect to the other organization before redirecting to your organization if possible.
  
## About the Folder Backup settings

You can set OneDrive settings using software distribution tools such as [Microsoft Intune](/mem/intune/apps/apps-add-office365-macOS) and [Jamf Pro](https://www.jamf.com/products/jamf-pro/), [Munki](https://www.munki.org/), [AutoPkg](https://github.com/autopkg/autopkg), [Apple Remote Desktop](https://support.apple.com/guide/remote-desktop/welcome/mac), and [AppleScript](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptX/AppleScriptX.html). You can also configure settings in a .plist file. For a full reference of available preferences and their settings, see [Deploy and configure the OneDrive sync app for macOS](deploy-and-configure-on-macos.md).  

For new machines, Folder Backup can be configured from the start, so all new files are uploaded to the cloud. This is great for organizations as it increases user engagement with OneDrive, and admins can easily protect files with enterprise-level security and compliance that comes built in.

The following settings control the Folder Backup feature:
  
- [Prompt users to move Desktop and Documents folders to OneDrive (KFMOptInWithWizard)](deploy-and-configure-on-macos.md#kfmoptinwithwizard)

    Use **KFMOptInWithWizard** to give the users a call to action to move their Desktop and Documents macOS folders.

    :::image type="content" source="media/redirect-macos-manage-folder-backup.png" alt-text="Screenshot of the dialog that prompts users to back up their important folders.":::

    If users dismiss the prompt, a reminder notification appears in the Sync Activity Center until they move all available folders.

    :::image type="content" source="media/redirect-macos-folder-backup.png" alt-text="Screenshot of the notification that reminds users to protect their important folders.":::

    > [!IMPORTANT]
    > We recommend deploying the prompt setting for existing devices only, and limiting the deployment to 5,000 devices a day and not exceeding 20,000 devices a week between macOS and Windows.
  
- [Silently move macOS Desktop and Documents folders to OneDrive (KFMSilentOptIn)](deploy-and-configure-on-macos.md#kfmsilentoptin)

    Use **KFMSilentOptIn** to redirect and move folders to OneDrive without any user interaction. Move all the folders or select the desired individual folders. By default, the Desktop and Documents folders are moved. After a folder is moved, the setting won't affect the folder again, even if the selection for the folder changes.

    You can choose to display a notification to users after their folders have been redirected.

    We also recommend using this setting together with **[KFMOptInWithWizard](deploy-and-configure-on-macos.md#kfmoptinwithwizard)**. If moving the Desktop and Documents folders silently doesn't succeed, users are prompted to correct the error and continue.

    > [!IMPORTANT]
    > We recommend deploying the silent setting for existing devices and new devices while limiting the deployment of existing devices to 1,000 devices a day and not exceeding 4,000 devices a week between macOS and Windows.

- [Prevent users from turning off Folder Backup (KFMBlockOptOut)](deploy-and-configure-on-macos.md#kfmblockoptout)

    Use **KFMBlockOptOut** to force users to keep their Desktop and Documents folders directed to OneDrive.

    > [!NOTE]
    > Users can direct their Desktop and Documents folders by opening OneDrive sync app preferences, clicking the **Backup tab**, and then clicking **Manage Backup**.
  
- [Prevent users from moving their macOS Desktop and Documents folders to OneDrive (KFMBlockOptIn)](deploy-and-configure-on-macos.md#kfmblockoptin)

    Use **KFMBlockOptIn** to prevent users from moving their Desktop and Documents folders to any OneDrive account.

For info about using the OneDrive sync settings, see [Deploy and configure the OneDrive sync app for macOS](deploy-and-configure-on-macos.md).

