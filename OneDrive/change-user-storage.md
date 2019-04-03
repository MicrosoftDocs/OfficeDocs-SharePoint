---
title: "Change a specific user's OneDrive storage space"
ms.author: kaarins
author: kaarins
manager: pamgreen
ms.audience: Admin
ms.topic: article
ms.service: one-drive
localization_priority: Normal
search.appverid:
- ODB160
- ODB150
- MET150
ms.collection: 
- Strat_OD_admin
- M365-collaboration
ms.assetid: 7448173d-a38c-48cf-acbb-09ac1b6237d4
description: "Learn how to change a user's OneDrive for Business storage space by using PowerShell"
---

# Change a specific user's OneDrive storage space

As a global or SharePoint admin in Office 365, you can set the OneDrive storage space for a specific user by using Microsoft PowerShell.
  
> [!NOTE]
> For info about setting the default storage space, see [Set the default storage space for OneDrive users](set-default-storage-space.md). For info about the storage available for your Office 365 plan, see the [OneDrive for Business service description](https://go.microsoft.com/fwlink/?linkid=826071). 
  
## Change the storage space for a specific user's OneDrive

1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).

    > [!NOTE]
    > If you installed a previous version of the SharePoint Online Management Shell, go to Add or remove programs and uninstall “SharePoint Online Management Shell.” <br>On the Download Center page, select your language and then click the Download button. You’ll be asked to choose between downloading a x64 and x86 .msi file. Download the x64 file if you’re running the 64-bit version of Windows or the x86 file if you’re running the 32-bit version. If you don’t know, see https://support.microsoft.com/help/13443/windows-which-operating-system. After the file downloads, run it and follow the steps in the Setup Wizard. 

2. Connect to SharePoint Online as a global admin or SharePoint admin in Office 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).
    
3. Run the following command:
    
      ```PowerShell
      Set-SPOSite -Identity <user's OneDrive URL> -StorageQuota <quota>
      ```

      (Where  _\<user's OneDrive URL\>_ is the URL of the user's OneDrive and  _\<quota\>_ is the value in gigabytes for the storage space. 
      
      A user’s OneDrive URL is based on their username. For example,     
      https://microsoft-my.sharepoint.com/personal/user1_contoso_com. You can find their username on the Active users (or Deleted users) page in the Microsoft 365 admin center. 

      For storage space, you would enter 1000 for 1 TB or 5000 for 5 TB. You can specify any value 1 GB or greater, however, if you specify a value bigger than that allowed by a given user's license, that user's storage space will be rounded down to the maximum value allowed by their license. 
    
    > [!NOTE]
    > If you want to change the storage space for multiple users, you can use PowerShell to [Display a list of OneDrive accounts by using PowerShell](list-onedrive-urls.md). To disable OneDrive creation for specific users, see [Manage user profiles in the SharePoint admin center](/sharepoint/manage-user-profiles). 
  

