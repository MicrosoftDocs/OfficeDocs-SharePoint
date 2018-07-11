---
title: "Restore a deleted OneDrive"
ms.author: kaarins
author: kaarins
manager: scotv
ms.date: 5/15/2018
ms.audience: Admin
ms.topic: article
ms.prod: office-online-server
localization_priority: Normal
search.appverid: ODB160
ms.assetid: e487f40d-5321-46a8-9504-92b600b65cb9
description: "Learn how to restore a deleted user's OneDrive when the deleted user no longer appears in the Office 365 admin center."
---

# Restore a deleted OneDrive

When you delete a user in the Office 365 admin center (or when a user is removed through Active Directory synchronization), the user's OneDrive will be retained for the number of days you specify in the OneDrive admin center. (For info, see [Set the default file retention for deleted OneDrive users](set-retention.md).) The default is 30 days. During this time, shared content can still be accessed by other users. At the end of the time, the OneDrive will be in a deleted state for 93 days and can only be restored by a global or SharePoint admin.
  
## Restore a deleted OneDrive when the deleted user no longer appears in the Office 365 admin center

If the user was deleted within 30 days, you can restore the user and all their data from the Office 365 admin center. To learn how, see [Restore a user in Office 365](https://support.office.com/article/2c261e42-5dd1-48b0-845f-2a016d29cfc1). If you deleted the user more than 30 days ago, the user will no longer appear in the Office 365 admin center, and you'll need to use PowerShell to restore the OneDrive. 
  
1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).
    
2. Connect to SharePoint Online as a global admin or SharePoint admin in Office 365. To learn how, see [Getting started with SharePoint Online Management Shell](https://go.microsoft.com/fwlink/?linkid=869066).
    
3. Determine if the OneDrive is available for restore
    
  - If you know the URL of the OneDrive, run the following command: 
    
  ```
  Get-SPODeletedSite -Identity <URL>
  ```

  - If you don't know the URL of the deleted OneDrive, run the following command:
    
  ```
  Get-SPODeletedSite -IncludeOnlyPersonalSite | FT url
  ```

  - If the OneDrive appears in the results, it can be restored.
    
4. Restore the OneDrive to an active state:
    
  ```
  Restore-SPODeletedSite -Identity <URL>
  ```

5. Assign a site collection administrator to the OneDrive to access the needed data:
    
  ```
  Set-SPOUser -Site <URL> -LoginName <UPNofDesiredAdmin> -IsSiteCollectionAdmin $True
  ```

For more info about these cmdlets, see [Get-SPODeletedSite](https://go.microsoft.com/fwlink/?linkid=874326) and [Restore-SPODeletedSite](https://go.microsoft.com/fwlink/?linkid=874327).
  
## Permanently delete a OneDrive

After you recover the data you need from the OneDrive, we recommend that you permanently delete the OneDrive by running the following command:
  
```
Remove-SPOSite -Identity <URL>
```

> [!CAUTION]
> When you permanently delete a OneDrive, you will not be able to restore it. 
  
## See also

[OneDrive retention and deletion](retention-and-deletion.md)

