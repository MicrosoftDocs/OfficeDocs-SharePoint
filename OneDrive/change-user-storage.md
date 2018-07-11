---
title: "Change a specific user's OneDrive storage space"
ms.author: kaarins
author: kaarins
manager: pamgreen
ms.date: 4/27/2018
ms.audience: Admin
ms.topic: article
ms.prod: office-online-server
localization_priority: Normal
search.appverid:
- ODB160
- ODB150
ms.assetid: 7448173d-a38c-48cf-acbb-09ac1b6237d4
description: "Learn how to change a user's OneDrive for Business storage space by using PowerShell"
---

# Change a specific user's OneDrive storage space

As a global or SharePoint admin in Office 365, you can set the OneDrive storage space for a specific user by using Microsoft PowerShell.
  
> [!NOTE]
> For info about setting the default storage space, see [Set the default storage space for OneDrive users](set-default-storage-space.md). For info about the storage available for your Office 365 plan, see the [OneDrive for Business service description](https://go.microsoft.com/fwlink/?linkid=826071). 
  
## Change the storage space for a specific user's OneDrive

1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).
    
2. Connect to SharePoint Online as a global admin or SharePoint admin in Office 365. To learn how, see [Getting started with SharePoint Online Management Shell](https://go.microsoft.com/fwlink/?linkid=869066).
    
3. Run the following command:
    
      ```
      Set-SPOSite -Identity <user's OneDrive URL> -StorageQuota <quota>
      ```

      (Where  _\<user's OneDrive URL\>_ is the URL of the user's OneDrive and  _\<quota\>_ is the value in megabytes for the storage space. For example, 1048576 for 1 TB or 5242880 for 5 TB. You can specify any value that you want, however, if you specify a value greater than that allowed by a given user's license, that user's storage space will be rounded down to the maximum value allowed by their license.) 
    
    > [!NOTE]
    > If you want to change the storage space for multiple users, you can use PowerShell to [Display a list of OneDrive accounts by using PowerShell](list-onedrive-urls.md). To disable OneDrive creation for specific users, see [Manage user profiles in the SharePoint admin center](https://support.office.com/article/494bec9c-6654-41f0-920f-f7f937ea9723#disableonedrivecreation). 
  

