---
title: "Change your users' OneDrive storage space using PowerShell"
ms.author: kaarins
author: kaarins
manager: pamgreen
ms.date: 9/18/2017
ms.audience: Admin
ms.topic: article
ms.prod: office-online-server
localization_priority: Normal
ms.assetid: 7448173d-a38c-48cf-acbb-09ac1b6237d4
description: "Learn how to change your users' OneDrive for Business storage space using PowerShell."
---

# Change your users' OneDrive storage space using PowerShell

The default storage space for each user's OneDrive user is 1 TB. If you have one of the following Office 365 plans, you can increase the storage up to 5 TB:
  
- Office 365 Enterprise E3 and E5
    
- Office 365 Government E3 and E5
    
- Office 365 Education and Office 365 Education E5
    
- OneDrive for Business Plan 2 and SharePoint Online Plan 2
    
> [!NOTE]
>  If your organization has more than 5 users, you can change the storage space to more than 5 TB. Contact Microsoft support to discuss your needs. For more information about the storage space that comes with each plan, see [OneDrive for Business service description](https://go.microsoft.com/fwlink/?linkid=826071)>  You must assign at least one license to a user before you can increase the default OneDrive storage space. 
  
## Change the default storage for OneDrive users

To set the default storage space in the new OneDrive admin center, see [Set the default storage space](set-the-default-storage-space-for-onedrive-users). To set the default storage space using Windows PowerShell, use the Set-SPOTenant Windows PowerShell cmdlet.
  
[Connect to SharePoint Online by using Windows PowerShell](https://go.microsoft.com/fwlink/p/?LinkID=829954) and then use the following syntax. 
  
```
Set-SPOTenant -OneDriveStorageQuota <quota>
```

For  _\<quota\>_, specify the value in megabytes for the storage space. For example, 1048576 for 1 TB or 5242880 for 5 TB. You can specify any value that you want, however, if you specify a value greater than that allowed by a given user's license, that user's storage space will be rounded down to the maximum value allowed by their license.
  
If you want to reset an existing user's OneDrive to the new default storage space, you can use the following Windows PowerShell syntax:
  
```
Set-SPOSite -Identity <siteURL> -StorageQuotaReset
```

## Change the storage space for a specific user's OneDrive

You can set the storage space for a specific user by using the Set-SPOSite Windows PowerShell cmdlet.
  
[Connect to SharePoint Online by using Windows PowerShell](https://go.microsoft.com/fwlink/p/?LinkID=829954) and then use the following syntax. 
  
```
Set-SPOSite -Identity <siteURL> -StorageQuota <quota>
```

For  _\<quota\>_, specify the value in megabytes for the storage space. For example, 1048576 for 1 TB or 5242880 for 5 TB. You can specify any value that you want, however, if you specify a value greater than that allowed by a given user's license, that user's storage space will be rounded down to the maximum value allowed by their license.
  
(You can [display a list of OneDrive for Business site collections](https://go.microsoft.com/fwlink/p/?LinkId=786840) if you want to change the storage space on more than one.) 
  

