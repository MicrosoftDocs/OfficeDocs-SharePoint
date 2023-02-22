---
ms.date: 07/11/2018
title: "Restore a deleted OneDrive"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
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
ms.custom:
- admindeeplinkSPO
- onedrive-toc
search.appverid:
- ODB160
- MET150
ms.assetid: e487f40d-5321-46a8-9504-92b600b65cb9
description: Learn how to restore a deleted user's OneDrive when the deleted user no longer appears in the Microsoft 365 admin center.
---

# Restore a deleted OneDrive

When you delete a user in the Microsoft 365 admin center (or when a user is removed through Active Directory synchronization), the user's OneDrive will be retained for the number of days you specify in the <a href="https://go.microsoft.com/fwlink/?linkid=2185219" target="_blank">SharePoint admin center</a>. (For info, see [Set the default file retention for deleted OneDrive users](set-retention.md).) The default is 30 days. During this time, shared content can still be accessed by other users. At the end of the time, the OneDrive will be in a deleted state for 93 days and can only be restored by a global or SharePoint admin.

For info about using Files Restore to restore a OneDrive to a previous point in time, see [Restore your OneDrive](https://support.office.com/article/fa231298-759d-41cf-bcd0-25ac53eb8a15).

For info about restoring items from the recycle bin in OneDrive, see [Restore deleted files or folders](https://support.office.com/article/949ada80-0026-4db3-a953-c99083e6a84f).
  
## Restore a deleted OneDrive when the deleted user no longer appears in the Microsoft 365 admin center

If the user was deleted within 30 days, you can restore the user and all their data from the Microsoft 365 admin center. To learn how, see [Restore a user in Microsoft 365](/office365/admin/add-users/restore-user). If you deleted the user more than 30 days ago, the user will no longer appear in the Microsoft 365 admin center, and you'll need to use PowerShell to restore the OneDrive.
  
1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).

    > [!NOTE]
    > If you installed a previous version of the SharePoint Online Management Shell, go to Add or remove programs and uninstall "SharePoint Online Management Shell." 

2. Connect to SharePoint as a [global admin or SharePoint admin](/sharepoint/sharepoint-admin-role) in Microsoft 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).

3. Determine if the OneDrive is available for restore.

   - If you know the URL of the OneDrive, run the following command:

     ```PowerShell
     Get-SPODeletedSite -Identity <URL>
     ```

     A user's OneDrive URL is based on their username. For example, 
     `https://contoso-my.sharepoint.com/personal/user1_contoso_com`. You can find their username on the Active users (or Deleted users) page in the Microsoft 365 admin center. 

   - If you don't know the URL of the deleted OneDrive, run the following command:

     ```PowerShell
     Get-SPODeletedSite -IncludeOnlyPersonalSite | FT url
     ```

   - If the OneDrive appears in the results, it can be restored.

4. Restore the OneDrive to an active state:

   ```PowerShell
   Restore-SPODeletedSite -Identity <URL>
   ```

5. Assign an administrator to the OneDrive to access the needed data:

   ```PowerShell
   Set-SPOUser -Site <URL> -LoginName <UPNofDesiredAdmin> -IsSiteCollectionAdmin $True
   ```

For more info about these cmdlets, see [Get-SPODeletedSite](/powershell/module/sharepoint-online/get-spodeletedsite) and [Restore-SPODeletedSite](/powershell/module/sharepoint-online/restore-spodeletedsite).

> [!NOTE]
> When a OneDrive is restored, it will continue to remain available until it's explicitly deleted.
  
## Permanently delete a OneDrive

After you recover the data you need from the OneDrive, we recommend that you permanently delete the OneDrive by running the following command:
  
```PowerShell
Remove-SPOSite -Identity <URL>
Remove-SPODeletedSite -Identity <URL>
```

> [!CAUTION]
> When you permanently delete a OneDrive, you will not be able to restore it.
  
## See also

[OneDrive retention and deletion](retention-and-deletion.md)

