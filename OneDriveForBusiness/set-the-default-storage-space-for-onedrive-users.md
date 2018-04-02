---
title: "Set the default storage space for OneDrive users"
ms.author: kaarins
author: kaarins
manager: pamgreen
ms.date: 2/27/2018
ms.audience: Admin
ms.topic: article
ms.prod: office-online-server
localization_priority: Normal
ms.collection: Strat_OD_admin
ms.assetid: cec51d07-d7e0-42a3-b794-9c00ad0f0083
description: "Learn how to change the default storage space for OneDrive users in the OneDrive admin center. "
---

# Set the default storage space for OneDrive users

The default storage space for each user's OneDrive user is 1 TB. If you have one of the following Office 365 plans, you can increase the storage up to 5 TB:
  
- Office 365 Enterprise E3 and E5
    
- Office 365 Government E3 and E5
    
- Office 365 Education and Office 365 Education E5
    
- OneDrive for Business Plan 2 and SharePoint Online Plan 2
    
> [!NOTE]
>  If your organization has more than 5 users, you can change the storage space to more than 5 TB. Contact Microsoft support to discuss your needs. For more information about the storage space that comes with each plan, see [OneDrive for Business service description](https://go.microsoft.com/fwlink/?linkid=826071)>  You must assign at least one license to a user before you can increase the default OneDrive storage space. 
  
## To set the default OneDrive storage space

1. Open the [OneDrive admin center](https://admin.onedrive.com/?v=StorageSettings) and click the **Storage** tab. 
    
     ![The Storage tab of the OneDrive admin center](media/15942b88-2f71-4c85-87ec-eb14b88f8f93.png)
  
2. Enter the default storage amount (in GB) in the **Default storage** box, and then click **Save**.
    
This storage space setting applies to all new and existing users for whom you haven't set specific storage limits. To change the storage space for specific users, you need to use Microsoft PowerShell. To check if you've set specific storage limits for a user, run this PowerShell command:
  
```
$r=Get-SPOSite -Identity https://superdomain-my.sharepoint.com/personal/noadmin_superdomain_onmicrosoft_com -Detailed
$r.StorageQuotaType
Default
```

If the storage type is set to UserSpecific instead of Default, you'll need to use PowerShell to change the storage space manually. 
  
For info about using PowerShell, see [Set up the SharePoint Online Management Shell Windows PowerShell environment](https://go.microsoft.com/fwlink/p/?LinkID=286318). For info about changing user storage space using PowerShell, see [Set your OneDrive for Business storage quota](change-your-users-onedrive-storage-space-using-powershell).
  
## See also

#### Other Resources

[OneDrive admin center](https://support.office.com/article/b5665060-530f-40a3-b34a-9e935169b2e0)

