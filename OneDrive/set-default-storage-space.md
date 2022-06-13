---
title: "Set the default storage space for OneDrive users"
ms.reviewer: waynewin
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
search.appverid:
- ODB160
- ODB150
- MET150
ms.custom:
- seo-marvel-apr2020
- admindeeplinkSPO
- onedrive-toc
ms.assetid: cec51d07-d7e0-42a3-b794-9c00ad0f0083
description: "In this article, you'll learn how to change the default storage space for OneDrive users."
---

# Set the default storage space for OneDrive users

For most subscription plans, the default storage space for each user's OneDrive is 1 TB. Depending on your plan and the number of licensed users, you can increase this storage up to 5 TB. For info, see the [OneDrive service description](/office365/servicedescriptions/onedrive-for-business-service-description). If you change a user's license, the available storage space is updated automatically within 24 hours after they access OneDrive.
  
If your organization has a qualifying Microsoft 365 subscription and five (5) or more users, you can change the storage space to more than 5 TB. To discuss your needs, contact Microsoft support. You must assign at least one license to a user before you can increase the default OneDrive storage space. The new storage limit is applied the next time a user accesses OneDrive.
  
> [!NOTE]
> For help finding out which subscription you have, see [What Microsoft 365 Apps for business subscription do I have?](/office365/admin/admin-overview/what-subscription-do-i-have)

## Set the default OneDrive storage space in the SharePoint admin center
This storage space setting applies to all new and existing users who are licensed for a qualifying plan and for whom you haven't set specific storage limits. (To check if a user has a specific storage limit, see the next section.) To change the storage space for specific users, see [Change a specific user's OneDrive storage space](change-user-storage.md).

> [!WARNING]
> If you decrease the storage limit and a user is over the new limit, their OneDrive will become read-only.

1. Go to <a href="https://go.microsoft.com/fwlink/?linkid=2185072" target="_blank">**Settings** in the new SharePoint admin center</a>, and sign in with an account that has [admin permissions](/sharepoint/sharepoint-admin-role) for your organization.
 
   > [!NOTE]
   > If you have Office 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the Settings page.

2. Select the OneDrive **Storage limit** setting.

    ![Default storage limit in the SharePoint admin center](media/storage-limit.png)
  
3. In the **Default storage limit** box, enter the default storage amount (in GB), and then select **Save**.

   > [!NOTE]
   > The minimum storage is 1 GB.

  
## Check if a user has the default storage limit or a specific limit

1. Sign in to https://admin.microsoft.com as a global or SharePoint admin. (If you see a message that you don't have permission to access the page, you don't have Microsoft 365 admin permissions in your organization.)
    
    > [!NOTE]
    > If you have Office 365 operated by 21Vianet (China), sign in at https://login.partner.microsoftonline.cn/. Then select the Admin tile to open the admin center.
    
2. In the left pane, select **Users** \> **Active users**.

3. Select the user.

4. Select the **OneDrive** tab.

5. Next to "Storage used," look at the max value (for example, 3 GB **of 1024 GB**).
    
    
## Set the default OneDrive storage space using PowerShell

1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).

    > [!NOTE]
    > If you installed a previous version of the SharePoint Online Management Shell, go to Add or remove programs and uninstall "SharePoint Online Management Shell." 

2. Connect to SharePoint as a [global admin or SharePoint admin](/sharepoint/sharepoint-admin-role) in Microsoft 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).
    
3. Run the following command:
    
      ```PowerShell
      Set-SPOTenant -OneDriveStorageQuota <quota>
      ```

     Where  _\<quota\>_ is the value in megabytes for the storage space. For example, 1048576 for 1 TB or 5242880 for 5 TB. You can specify any value that you want, however, if you specify a value greater than that allowed by a given user's license, that user's storage space will be rounded down to the maximum value allowed by their license. 
    
    To reset an existing user's OneDrive to the new default storage space, run the following command:
    
      ```PowerShell
      Set-SPOSite -Identity <user's OneDrive URL> -StorageQuotaReset
      ```
   
    > [!NOTE]
    > When you set site storage limits in PowerShell, you enter them in MB. The values are converted and rounded down to the nearest integer to appear in the admin centers in GB, so a value of 5000 MB becomes 4 GB. If you set a value of less than 1024 MB using PowerShell, it will be rounded up to 1 GB.

## See also

[More info about using Set-SPOTenant](/powershell/module/sharepoint-online/set-spotenant)
