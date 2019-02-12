---
title: "Set the default storage space for OneDrive users"
ms.author: kaarins
author: kaarins
manager: pamgreen
ms.audience: Admin
ms.topic: article
ms.service: one-drive
localization_priority: Normal
ms.collection: Strat_OD_admin
search.appverid:
- ODB160
- ODB150
- MET150
ms.assetid: cec51d07-d7e0-42a3-b794-9c00ad0f0083
description: "Learn how to change the default storage space for OneDrive users in the OneDrive admin center. "
---

# Set the default storage space for OneDrive users

The default storage space for each user's OneDrive user is 1 TB. Depending on your Office 365 plan (see the [OneDrive for Business service description](https://go.microsoft.com/fwlink/?linkid=826071) for info), you can increase the storage up to 5 TB. 
  
> [!NOTE]
> For help finding out which subscription you have, see [What Office 365 for business subscription do I have?](/office365/admin/admin-overview/what-subscription-do-i-have)<br> If your organization has 5 or more users, you can change the storage space to more than 5 TB. Contact Microsoft support to discuss your needs. You must assign at least one license to a user before you can increase the default OneDrive storage space. 
  
## Set the default OneDrive storage space in the OneDrive admin center

1. Open the [OneDrive admin center](https://admin.onedrive.com/?v=StorageSettings) and click **Storage** in the left pane. 
    
    ![The Storage page of the OneDrive admin center](media/15942b88-2f71-4c85-87ec-eb14b88f8f93.png)
  
2. Enter the default storage amount (in GB) in the **Default storage** box, and then click **Save**.

> [!NOTE]
> The minimum storage is 1 GB. 
    
This storage space setting applies to all new and existing users for whom you haven't set specific storage limits. (To check if a user has a specific storage limit, see the next section.) To change the storage space for specific users, you need to use Microsoft PowerShell. For info on how to do this, see [Change your users' OneDrive storage space using PowerShell](change-user-storage.md). 
  
## Check if a user has the default storage limit or a specific limit

1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).

    > [!NOTE]
    > If you installed a previous version of the SharePoint Online Management Shell, go to Add or remove programs and uninstall “SharePoint Online Management Shell.” <br>On the Download Center page, select your language and then click the Download button. You’ll be asked to choose between downloading a x64 and x86 .msi file. Download the x64 file if you’re running the 64-bit version of Windows or the x86 file if you’re running the 32-bit version. If you don’t know, see https://support.microsoft.com/help/13443/windows-which-operating-system. After the file downloads, run it and follow the steps in the Setup Wizard.
    
2. Connect to SharePoint Online as a global admin or SharePoint admin in Office 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).
    
3. Run the following command:
    
    ```PowerShell
    $r=Get-SPOSite -Identity <user's OneDrive URL> -Detailed
    $r.StorageQuotaType
    ```

    (Where  _\<user's OneDrive URL\>_ is the URL of the user's OneDrive). A user’s OneDrive URL is based on their username. You can find their username on the Active users (or Deleted users) page in the Microsoft 365 admin center. For example, https://microsoft-my.sharepoint.com/personal/user1_contoso_com
      
    The command will return "Default" if the user has the default storage limit or "UserSpecific" if the user has a specific limit. 
    
## Set the default OneDrive storage space using PowerShell

1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).
    
2. Connect to SharePoint Online as a global admin or SharePoint admin in Office 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).
    
3. Run the following command:
    
      ```PowerShell
      Set-SPOTenant -OneDriveStorageQuota <quota>
      ```

     Where  _\<quota\>_ is the value in megabytes for the storage space. For example, 1048576 for 1 TB or 5242880 for 5 TB. You can specify any value that you want, however, if you specify a value greater than that allowed by a given user's license, that user's storage space will be rounded down to the maximum value allowed by their license. 
    
    To reset an existing user's OneDrive to the new default storage space, run the following command:
    
      ```PowerShell
      Set-SPOSite -Identity <user's OneDrive URL> -StorageQuotaReset
      ```

## See also
 
[More info about using Set-SPOTenant](/powershell/module/sharepoint-online/set-spotenant)

