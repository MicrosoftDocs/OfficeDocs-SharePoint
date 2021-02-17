---
title: "Redirect and move Windows known folders to OneDrive"
ms.reviewer: cagreen
ms.author: kaarins
author: kaarins
manager: serdars
audience: Admin
f1.keywords:
- NOCSH
ms.topic: get-started-article
ms.service: one-drive
localization_priority: Normal
ms.collection: 
- Strat_OD_admin
- M365-collaboration
ms.custom:
- seo-marvel-apr2020
search.appverid:
- ODB160
- ODB150
- GOB150
- GOB160
- MET150
ms.assetid: e1b3963c-7c6c-4694-9f2f-fb8005d9ef12
description: In this article, you'll learn how to redirect users' Documents folders or other known folders to OneDrive.
---

# Redirect and move Windows known folders to OneDrive

This article is for IT admins managing the OneDrive sync app.
  
There are two primary advantages of moving or redirecting Windows known folders (Desktop, Documents, Pictures, Screenshots, and Camera Roll) to Microsoft OneDrive for the users in your domain:
  
- Your users can continue using the folders they're familiar with. They don't have to change their daily work habits to save files to OneDrive.

- Saving files to OneDrive backs up your users' data in the cloud and gives them access to their files from any device.

For these reasons, we recommend moving or redirecting known folders to OneDrive if you're an enterprise or large organization. [See all our recommendations for configuring the sync app](ideal-state-configuration.md). Small or medium businesses may also find this useful, but keep in mind you'll need some experience configuring policies. For info about the end-user experience, see [Protect your files by saving them to OneDrive](https://support.office.com/article/d61a7930-a6fb-4b95-b28a-6552e77c3057). 

## Prepare to move known folders on existing devices

We recommend that you upgrade to the latest available build before you deploy to decrease deployment issues. Known Folder Move doesn't work for users syncing OneDrive files in SharePoint Server. 

To check eligibility on existing devices, data volume, and item counts as you decide on a rollout plan, and to later monitor progress of the rollout, use the Known Folder Move PowerShell script. 

> [!IMPORTANT]
> If your organization is large and your users have a lot of files in their known folders, make sure you roll out the configuration slowly to minimize the network impact of uploading files. For users who have a lot of files in their known folders, consider using the policy [Limit the sync app upload rate to a percentage of throughput](use-group-policy.md#limit-the-sync-app-upload-rate-to-a-percentage-of-throughput) temporarily to minimize the network impact and then disable the policy once uploads are complete. 
  
## About the Known Folder Move policies

OneDrive policies can be set using Group Policy, [Intune Windows 10 Administrative Templates](configure-sync-intune.md), or by configuring registry settings. For a full reference of available policies and their registry settings, see [Use OneDrive policies to control sync settings](use-group-policy.md).  

The following policies control the Known Folder Move feature: 
  
- [Prompt users to move Windows known folders to OneDrive](use-group-policy.md#prompt-users-to-move-windows-known-folders-to-onedrive)

    Use this setting to give the users a call to action to move their Windows known folders.

    ![Screenshot of the dialog that prompts users to protect their important folders](media/protect-important-folders-gpo.png)

    If users dismiss the prompt, a reminder notification will appear in the activity center until they move all known folders or an error occurs with the move, in which case the reminder notification will be dismissed.

    ![Screenshot of the notification that reminds users to protect their important folders](media/protect-important-folders-notification.png)

    If a user has already redirected their known folders to a different OneDrive account, they'll be prompted to direct the folders to the account for your organization (leaving existing files behind).
    
    > [!IMPORTANT]
    > We recommend deploying the prompt policy for existing devices only, and limiting the deployment to 5,000 devices a day and not exceeding 20,000 devices a week.
  
- [Silently move Windows known folders to OneDrive](use-group-policy.md#silently-move-windows-known-folders-to-onedrive)
    
    Use this setting to redirect and move known folders to OneDrive without any user interaction. Move all the folders or select the desired individual folders. After a folder is moved, the policy will not affect the folder again, even if the selection for the folder changes. 

    > [!NOTE]
    > You can choose to display a notification to users after their folders have been redirected. 

    A number of errors can prevent this setting from taking effect, such as:

    - A file exceeds the maximum path length
    - The known folders aren't in the default locations
    - Folder protection is unavailable
    - Known folders are prohibited from being redirected

    For info about these errors, see [Fix problems with folder protection](https://support.office.com/article/d61a7930-a6fb-4b95-b28a-6552e77c3057#BKMK_FixProblems).

    > [!IMPORTANT]
    > We recommend deploying the silent policy for existing devices and new devices while limiting the deployment of existing devices to 1,000 devices a day and not exceeding 4,000 devices a week. We also recommend using this setting together with "Prompt users to move Windows known folders to OneDrive." If moving the known folders silently does not succeed, users will be prompted to correct the error and continue. 
   
- [Prevent users from redirecting their Windows known folders to their PC](use-group-policy.md#prevent-users-from-redirecting-their-windows-known-folders-to-their-pc)

    Use this setting to force users to keep their known folders directed to OneDrive.

    > [!NOTE]
    > Users can direct their known folders by opening OneDrive sync app settings, clicking the **Backup** tab, and then clicking **Manage backup**.
  
- [Prevent users from moving their Windows known folders to OneDrive](use-group-policy.md#prevent-users-from-moving-their-windows-known-folders-to-onedrive)

For info about using the OneDrive policies, see [Use Group Policy to control OneDrive sync app settings](use-group-policy.md).

## Transition from the Windows Folder Redirection Group Policy objects

The OneDrive Known Folder Move Group Policy objects won't work if you previously used [Windows Folder Redirection Group Policy objects](/windows-server/storage/folder-redirection/deploy-folder-redirection) to redirect the Documents, Pictures, or Desktop folders to a location other than OneDrive. The OneDrive Group Policy objects won't affect the Music and Videos folders, so you can keep them redirected with the Windows Group Policy objects. Follow these steps to switch to using the Known Folder Move Group Policy objects.

- If folders have been redirected to OneDrive using Windows Folder Redirection Group Policy:

  1. Disable the Window Folder Redirection Group Policy and make sure to leave the folder and contents on OneDrive.
  2. Enable KFM Group Policy. Known folders remain in OneDrive.
  
- If folders have been redirected to a location on a local PC:

  1. Disable the Window Folder Redirection Group Policy and make sure to leave the folder and contents at the redirected location.
  2. Enable KFM Group Policy. Known folders move to OneDrive.
  
- If folders have been redirected to a network file share: 

  > [!NOTE]
  > We recommend using Windows 10 Fall Creators Update (version 1709 or later) or Windows Server 2019 and the current version of OneDrive to get the benefits from Files On-Demand.
  
  1. [Use a migration tool](/sharepointmigration/migrate-to-sharepoint-online) to copy contents in the network file share location to a user's OneDrive, making sure that all contents go into the existing Documents, Pictures, or Desktop folders.
  2. Disable the Window Folder Redirection Group Policy and make sure to leave the folder and contents on the network file share. 
  3. Enable KFM Group Policy. Known folders move to OneDrive and will merge with the existing Desktop, Documents, and Pictures folders which contain all the file share content that you moved in the first step.
