---
ms.date: 09/16/2024
title: "Change a specific user's OneDrive storage space"
ms.reviewer: pramod.balusu
ms.author: mactra
author: MachelleTranMSFT
manager: jtremper
audience: Admin
f1.keywords:
- NOCSH
ms.topic: how-to
ms.service: one-drive
ms.localizationpriority: medium
search.appverid:
- ODB160
- ODB150
- MET150
ms.collection: 
- Strat_OD_admin
- M365-collaboration
- Essentials-manage
ms.custom:
- seo-marvel-apr2020
- onedrive-toc
ms.assetid: 7448173d-a38c-48cf-acbb-09ac1b6237d4
description: In this article, you learn how to change a user's OneDrive storage space in Microsoft 365 using either PowerShell or the SharePoint admin center.
---

# Change a specific user's OneDrive storage space

As an IT administrator, you can adjust a user's OneDrive storage space using the SharePoint admin center or PowerShell.

> [!NOTE]
> For setting the default storage space for all users, see [Set the default storage space for OneDrive users](set-default-storage-space.md). For details on available storage for your Microsoft 365 subscription, see the [OneDrive service description](/office365/servicedescriptions/onedrive-for-business-service-description).

> [!IMPORTANT]
> If a user has run out of storage, advise them to proactively review and manage their storage. Instructions can be found at [Manage your OneDrive for work](https://support.microsoft.com/office/manage-your-onedrive-for-work-or-school-storage-31519161-059c-4764-b6f8-f5cd29f7fe68).

## Change storage space in the Microsoft 365 admin center

1. Sign in to the [Microsoft 365 admin center](https://admin.microsoft.com) with your admin credentials.

    > [!NOTE]
    > For Office 365 operated by 21Vianet (China), [sign in here](https://login.partner.microsoftonline.cn).

2. In the left pane, expand **Users** and select **Active users**.

3. Select the user whose storage you want to change.

4. Go to the **OneDrive** tab.

5. Under **Storage used**, select **Edit**.

6. Choose the **Maximum storage for this user** option and set the storage limit.

7. Select **Save**.

    ![OneDrive storage settings screenshot](media/edit-user-storage-limit.png)

When users need more storage beyond the initial 5 TB, Microsoft increases their storage as follows:

- When a user reaches 90% of their 5 TB capacity, Microsoft increases their storage to up to 25 TB. Admins can set a lower limit if desired.
- If usage drops below 90%, storage limit resets to 5 TB.
- For users reaching 90% of their 25 TB capacity, more storage is provided via SharePoint team sites. Contact [Microsoft Support](https://go.microsoft.com/fwlink/?linkid=869559) for assistance.

    > [!NOTE]
    > For Office 365 A1 users, storage is limited to 100 GB. For more information, see [Office 365 Education service descriptions](/office365/servicedescriptions/office-365-platform-service-description/office-365-education).

## Change storage space using PowerShell

1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).

    > [!NOTE]
    > Uninstall any previous versions of the SharePoint Online Management Shell before installing the latest version.

2. Save the following PowerShell script to a file (for example, you can save it as _UpdateOneDriveStorage.ps1_):

    ```PowerShell
    $TenantUrl = Read-Host "Enter the SharePoint admin center URL"
    Connect-SPOService -Url $TenantUrl

    $OneDriveSite = Read-Host "Enter the OneDrive Site URL"
    $OneDriveStorageQuota = Read-Host "Enter the OneDrive Storage Quota in MB"
    $OneDriveStorageQuotaWarningLevel = Read-Host "Enter the OneDrive Storage Quota Warning Level in MB"
    Set-SPOSite -Identity $OneDriveSite -StorageQuota $OneDriveStorageQuota -StorageQuotaWarningLevel $OneDriveStorageQuotaWarningLevel
    Write-Host "Done"
    ```

3. Open the SharePoint Online Management Shell and run the script:

    ```PowerShell
    PS C:\>.\UpdateOneDriveStorage.ps1
    ```

    > [!NOTE]
    > If you receive an error regarding script execution, you may need to adjust your PowerShell execution policies. For more information, see [About execution policies](/powershell/module/microsoft.powershell.core/about/about_execution_policies).

4. Enter the required values when prompted, including:
   - The SharePoint admin center URL (for example, `https://contoso-admin.sharepoint.com`)
   - The OneDrive site URL (for example, `https://contoso-my.sharepoint.com/personal/user_contoso_onmicrosoft_com`)
   - Storage Quota in MB
   - Storage Quota Warning Level in MB

Here's a reference table for MB to TB conversions:

| MB        | TB |
| --------- |--|
| 1,048,576 | 1  |
| 2,097,152 | 2  |
| 3,145,728 | 3  |
| 4,194,304 | 4  |
| 5,242,880 | 5  |

> [!NOTE]
> To change storage space for multiple users, you can list OneDrive accounts via PowerShell and use the [Set-SPOSite](/powershell/module/sharepoint-online/set-sposite) command to apply changes.

## Troubleshooting OneDrive storage issues

If you encounter issues when adjusting storage or if the storage amount reverts to its original value, a Microsoft 365 administrator can run diagnostics in the admin center.

1. In the Microsoft 365 admin center, select **Run Tests** to launch the OneDrive storage quota diagnostic.

    > [!NOTE]
    > Diagnostics are unavailable for GCC High, DoD, Microsoft 365 operated by 21Vianet, or Microsoft 365 Education.

2. Follow the recommendations provided by the diagnostic.

    > [!NOTE]
    > For information on disabling OneDrive creation for specific users, see [Manage user profiles in the SharePoint admin center](/sharepoint/manage-user-profiles).
