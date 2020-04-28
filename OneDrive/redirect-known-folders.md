---
title: "Redirect and move Windows known folders to OneDrive"
ms.reviewer: zhdong
ms.author: kaarins
author: kaarins
manager: pamgreen
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
description: "In this article, you'll learn how to redirect users' Documents folders or other known folders to OneDrive."
---

# Redirect and move Windows known folders to OneDrive

This article is for IT admins managing the OneDrive sync app in a Windows Server enterprise environment that uses Active Directory Domain Services.
  
There are two primary advantages of moving or redirecting Windows known folders (Desktop, Documents, Pictures, Screenshots, and Camera Roll) to OneDrive for the users in your domain:
  
- Your users can continue using the folders they're familiar with. They don't have to change their daily work habits to save files to OneDrive.

- Saving files to OneDrive backs up your users' data in the cloud and gives them access to their files from any device.

For these reasons, we recommend moving or redirecting known folders to OneDrive if you're an enterprise or large organization. Small or medium businesses may also find this useful, but keep in mind you'll need some experience with Group Policy. For info about the end-user experience, see [Protect your files by saving them to OneDrive](https://support.office.com/article/d61a7930-a6fb-4b95-b28a-6552e77c3057).
  
## About the Known Folder Move Group Policy objects

To use the following Group Policy objects, you need the OneDrive sync build 18.111.0603.0004 or later. You can see your build number in the About tab in OneDrive settings.  We recommend upgrading to the latest available build before deploying to decrease deployment issues. Known Folder Move does not work for users syncing OneDrive files in SharePoint Server.  

> [!IMPORTANT]
   > If your organization is large and your users have a lot of files in their known folders, make sure you roll out the Group Policy objects slowly to minimize the network impact of uploading files. For users who have a lot of files in their known folders, consider using the policy "[Limit the sync app upload rate to a percentage of throughput](use-group-policy.md#AutomaticUploadBandwidthPercentage)" temporarily if you would like to minimize the network impact and then disable the policy once uploads are complete.
  
- [Prompt users to move Windows known folders to OneDrive](use-group-policy.md#KFMOptInWithWizard)

    Use this setting to give the users a call to action to move their Windows known folders.

    ![Screenshot of the dialog that prompts users to protect their important folders](media/protect-important-folders-gpo.png)

    If users dismiss the prompt, a reminder notification will appear in the activity center until they move all known folders or an error occurs with the move, in which case the reminder notification will be dismissed.

    ![Screenshot of the notification that reminds users to protect their important folders](media/protect-important-folders-notification.png)

    If a user has already redirected their known folders to a different OneDrive account, they'll be prompted to direct the folders to the account for your organization (leaving existing files behind).
    
    We recommend deploying the prompt policy for existing devices only, and limiting the deployment to 5,000 devices a day and not exceeding 20,000 devices a week.
  
- [Silently move Windows known folders to OneDrive](use-group-policy.md#KFMOptInNoWizard)
    
    Use this setting to redirect known folders to OneDrive without any user interaction. Before sync app build 18.171.0823.0001, this setting redirected only empty known folders to OneDrive. Now, it redirects known folders that contain content and moves the content to OneDrive.

    > [!NOTE]
    > You can choose to display a notification to users after their folders have been redirected.  

    A number of errors can prevent this setting from taking effect, such as:
    - A file exceeds the maximum path length
    - The known folders aren't in the default locations
    - A folder isn't selected for syncing
    - Folder protection is unavailable
    - Known folders are prohibited from being redirected


    For info about these errors, see [Fix problems with folder protection](https://support.office.com/article/d61a7930-a6fb-4b95-b28a-6552e77c3057#BKMK_FixProblems).

    We recommend deploying the silent policy for existing devices and new devices while limiting the deployment of existing devices to 1,000 devices a day and not exceeding 4,000 devices a week.  We also recommend using this setting together with "Prompt users to move Windows known folders to OneDrive." If moving the known folders silently does not succeed, users will be prompted to correct the error and continue.  
   
- [Prevent users from redirecting their Windows known folders to their PC](use-group-policy.md#KFMBlockOptOut)

    Use this setting to force users to keep their known folders directed to OneDrive.

    > [!NOTE]
    > Users can direct their known folders by opening OneDrive sync app settings, clicking the **Backup** tab, and then clicking **Manage backup**.
  
- [Prevent users from moving their Windows known folders to OneDrive](use-group-policy.md#BlockKnownFolderMove)

For info about using the OneDrive Group Policy objects, see [Use Group Policy to control OneDrive sync app settings](use-group-policy.md).

## Moving from previous Windows Folder Redirection Group Policy
The OneDrive Known Folder Move Group Policy objects won't work if you previously used Windows Folder Redirection Group Policy objects to redirect the Documents, Pictures, or Desktop folders to a location other than OneDrive. The OneDrive Group Policy objects won't affect the Music and Videos folders, so you can keep them redirected with the Windows Group Policy objects. Here are the steps you must take to get into a state where the Known Folder Move Group Policy will work:
- If folder(s) have been redirected to OneDrive using Windows Folder Redirection Group Policy
  1. Disable the Window Folder Redirection Group Policy, make sure to leave the folder and contents on OneDrive
  2. Enable KFM Group Policy
  3. Your known folders shouldn't have moved anywhere
- If folder(s) have been redirect to location on local PC 
  1. Disable the Window Folder Redirection Group Policy, make sure to redirect the folder(s) back to the user profile location
  2. Enable KFM Group Policy
  3. Known folders should be moved successfully to OneDrive
- If folder(s) have been redirected to Network Share 

  >[!NOTE]
  > Windows 10 Fall Creators Update (version 1709 or later) or Windows Server 2019 and OneDrive build 17.3.7064.1005 or later recommended to get Files on Demand benefits
  
  1. Use a migration tool ([Mover](https://docs.microsoft.com/en-us/sharepointmigration/mover-fileshare-to-o365), [SharePoint Migration Tool](https://docs.microsoft.com/en-us/sharepointmigration/introducing-the-sharepoint-migration-tool), etc.) to copy contents in Network Share location to user's ODB, make sure all content goes into existing Documents, Pictures, or Desktop (create if it doesn’t exist) folders.
  2. Disable the Window Folder Redirection Group Policy, make sure to leave the folder and contents on OneDrive 
  3. Enable KFM Group Policy
  4. Known folders should be moved to OneDrive and will merge with the existing Desktop, Documents, and Pictures folders which should contain all of the Network share content that you moved in step b.

For info about Windows Folder Redirection, see [Deploy Folder Redirection with Offline Files](/windows-server/storage/folder-redirection/deploy-folder-redirection). 
