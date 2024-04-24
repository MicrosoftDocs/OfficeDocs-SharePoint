---
ms.date: 09/01/2023
title: "Change a specific user's OneDrive storage space"
ms.reviewer: jmcdowe
ms.author: mactra
author: MachelleTranMSFT
manager: jtremper
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
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
description: In this article, you'll learn how to change a user's OneDrive storage space.
---

# Change a specific user's OneDrive storage space

As a global or SharePoint admin in Microsoft 365, you can set the OneDrive storage space for a specific user.
  
> [!NOTE]
> For info about setting the default storage space, see [Set the default storage space for OneDrive users](set-default-storage-space.md). For info about the storage available for your Microsoft 365 subscription, see the [OneDrive service description](/office365/servicedescriptions/onedrive-for-business-service-description).

> [!NOTE]
> If your organization is configured for multi-geo, you need to use PowerShell to change a user's OneDrive storage space. Editing storage limits isn't available in the Microsoft 365 admin center.  

> [!IMPORTANT]
> If a user has run out of storage, consider instructing them to proactively identify and review items that are taking up space by following the instructions at [Manage your OneDrive for work](https://support.microsoft.com/en-us/office/manage-your-onedrive-for-work-or-school-storage-31519161-059c-4764-b6f8-f5cd29f7fe68).

## Change a user's storage space in the Microsoft 365 admin center

1. Sign in to <https://admin.microsoft.com> as a global or SharePoint admin. (If you see a message that you don't have permission to access the page, you don't have Microsoft 365 admin permissions in your organization.)

> [!NOTE]
> If you have Office 365 operated by 21Vianet (China), [sign in](https://login.partner.microsoftonline.cn/). Then, select the Admin tile to open the admin center.

2. In the left pane, select **Users** \> **Active users**.

3. Select the user.

4. Select the **OneDrive** tab.

5. Under **Storage used** click **Edit**.

6. Select the **Maximum storage for this user** option, and type the storage limit that you want to use.

7. Click **Save**.

    ![Screenshot of the OneDrive storage settings in the Microsoft 365 admin center](media/edit-user-storage-limit.png)

When you need cloud storage for individual users beyond the initial 5 TB, additional cloud storage will be granted as follows:

- When a user has filled their 5 TB of OneDrive storage to at least 90% capacity, Microsoft will increase your default storage space in OneDrive to up to 25 TB per user (admins might set a lower per-user limit if they want to). The storage limit will be reset to 5 TB if OneDrive storage utilization drops below 90% of the 5 TB capacity.

- For any user that reaches at least 90% capacity of their 25 TB of OneDrive storage, additional cloud storage will be provided as 25 TB SharePoint team sites to individual users.  For more information and assistance, contact [Microsoft Support](https://go.microsoft.com/fwlink/?linkid=869559).

- Admins can check for OneDrive eligibility beyond 5 TB via [Check OneDrive site eligibility for increased storage](/sharepoint/troubleshoot/storage/check-storage-increase-eligibility).

    > [!NOTE]
    > For Office 365 A1 users, the OneDrive storage limit is up to 100 GB. For details, see [Office 365 Education service descriptions](/office365/servicedescriptions/office-365-platform-service-description/office-365-education).

## Change a user's storage space by using PowerShell

1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).

    > [!NOTE]
    > If you installed a previous version of the SharePoint Online Management Shell, go to Add or remove programs and uninstall "SharePoint Online Management Shell."

2. Save the following script as a PowerShell file. For example, you could save it to a file named UpdateOneDriveStorage.ps1.

    ```PowerShell
    $TenantUrl = Read-Host "Enter the SharePoint admin center URL" 
    Connect-SPOService -Url $TenantUrl 
 
    $OneDriveSite = Read-Host "Enter the OneDrive Site URL" 
    $OneDriveStorageQuota = Read-Host "Enter the OneDrive Storage Quota in MB" 
    $OneDriveStorageQuotaWarningLevel = Read-Host "Enter the OneDrive Storage Quota Warning Level in MB" 
    Set-SPOSite -Identity $OneDriveSite -StorageQuota $OneDriveStorageQuota -StorageQuotaWarningLevel $OneDriveStorageQuotaWarningLevel 
    Write-Host "Done" 
    ```

3. Open the SharePoint Online Management Shell. Run the script in the location you saved it.

    ```PowerShell
    PS C:\>.\ UpdateOneDriveStorage.ps1
    ```

    > [!NOTE]
    > If you get an error message about being unable to run scripts, you might need to change your execution policies. For more info about PowerShell execution policies, see [About Execution Policies](/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.1&preserve-view=true).

4. When prompted, enter the SharePoint admin center URL. For example, `https://contoso-admin.sharepoint.com` is the Contoso SharePoint admin center URL.

5. Sign in as a global or SharePoint admin in Microsoft 365.

6. Enter the OneDrive site URL: For example, `https://contoso-my.sharepoint.com/personal/user_contoso_onmicrosoft_com`.

7. Enter the OneDrive Storage Quota in MB.

8. Enter the OneDrive Storage Quota Warning Level in MB.

   | MB  | TB |
   | ------------- | ------------- |
   | 1048576 | 1  |
   | 2097152 | 2  |
   | 3145728 | 3  |
   | 4194304 | 4 |
   | 5242880 | 5 |
   | 6291456 | 6 |
   | 7340032 | 7 |
   | 8388608 | 8 |
   | 9437184 | 9 |
   | 10485760 | 10 |

> [!NOTE]
> To change the storage space for multiple users, use PowerShell to [Display a list of OneDrive accounts by using PowerShell](list-onedrive-urls.md) and use [Set-SPOSite](/powershell/module/sharepoint-online/set-sposite?preserve-view=true&view=sharepoint-ps&preserve-view=true) to make the change.

## Diagnose issues with changing the OneDrive storage

If you are attempting to change the OneDrive storage for a user and are not able to do so or the storage amount reverts to the original value, a Microsoft 365 administrator can run tests to determine what might be preventing the storage from changing.

> [!NOTE]
> If you're an administrator and you're having trouble changing the OneDrive storage for a user or the storage amount reverts to the original value, select **Run Tests** below, which will populate the OneDrive storage quota diagnostic in the Microsoft 365 admin center. These tests will help determine what may be preventing the storage from changing and recommend steps for a resolution.
>> [!div class="nextstepaction"]
>> [Run Tests: Check OneDrive Storage Quota](https://aka.ms/PillarOneDriveQuota)

> [!NOTE]
> This diagnostic isn’t supported for GCC High, DoD, Microsoft 365 operated by 21Vianet, or Microsoft 365 Education.

> To disable OneDrive creation for specific users, see [Manage user profiles in the SharePoint admin center](/sharepoint/manage-user-profiles).
