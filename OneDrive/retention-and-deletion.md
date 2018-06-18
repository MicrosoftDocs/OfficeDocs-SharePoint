---
title: "OneDrive retention and deletion"
ms.author: v-thehay
author: SteyerTHaynie
manager: scotv
ms.date: 5/21/2018
ms.audience: Admin
ms.topic: article
ms.prod: office-online-server
localization_priority: Normal
search.appverid: ODB160
ms.assetid: ef883c48-332c-42f5-8aea-f0e2366c15f9
description: "Learn what happens to a user's OneDrive when the user's Office 365 account for the organization is deleted"
---

# OneDrive retention and deletion

This article describes what happens to a user's OneDrive when you delete the user's Office 365 account for your organization. 
  
## Give another user access to a deleted user's OneDrive

When you delete a user in the Office 365 admin center, you can choose what you want to do with the user's product licenses, email, and OneDrive. If you give another user access to the OneDrive, that user will have 30 days by default to access and download the files they want to keep. (To change the retention time, see [Set the OneDrive retention for deleted users](set-retention.md).) They'll receive an email with a link to these instructions for accessing the deleted user's OneDrive: [Copy files from another user's OneDrive](https://support.office.com/article/7eb33f7d-6540-488f-afaf-56043828e47b.aspx).
  
## Configure automatic access delegation

By default, when you delete a user, ownership of the OneDrive is transferred to the user's manager. Follow these steps to check if access delegation is turned on and set a secondary admin in case a user doesn't have a specified manager:
  
1. Sign in to Office 365 as a global admin or SharePoint admin.
    
2. Select the app launcher icon ![The icon that looks like a waffle and represents a button click that will reveal multiple application tiles for selection.](media/3b8a317e-13ba-4bd4-864e-1ccd47af39ee.png) in the upper-left and choose **Admin** to open the Office 365 admin center. (If you don't see the Admin tile, you don't have Office 365 administrator permissions in your organization.) 
    
3. In the left pane, choose **Admin centers** \> **SharePoint**.
    
4. Click **user profiles** in the left pane. 
    
5. Under **My Site Settings**, click **Setup My Sites**.
    
6. Next to **My Site Cleanup**, make sure **Enable access delegation** is selected. 
    
7. We recommend that you also specify a secondary owner account in the **My Site Cleanup** section. This account will be the appointed owner of the OneDrive if the user's manager isn't set in Azure AD. Email notifications will also be sent to the secondary owner account when the value is populated. 
    
8. Click **OK**.
    
If a manager or secondary owner isn't set for the user, or if access delegation is disabled, OneDrive will follow the deletion process described in the next section. However, email messages won't be sent automatically.
  
## The OneDrive deletion process

1. A user is deleted from the Office 365 admin center or is removed through Active Directory synchronization.
    
2. The account deletion is synchronized to SharePoint Online.
    
3. The OneDrive Clean Up Job runs, and the OneDrive is marked for deletion. The deleted user will appear in the Office 365 admin center for 30 days. The default retention period for OneDrive is also 30 days, but you can change this in the OneDrive admin center (see [Set the OneDrive retention for deleted users](set-retention.md)) or by using the **-OrphanedPersonalSitesRetentionPeriod** parameter for the **Set-SPOTenant** cmdlet in the SharePoint Online Management Shell. For more information about using this cmdlet, see [Set-SPOTenant](https://go.microsoft.com/fwlink/?linkid=872571).
    
4. If a manager is specified for the deleted account, the manager will receive an email telling them they have access to the OneDrive, and that the OneDrive will be deleted at the end of the retention period.
    
5. If a manager isn't specified for the user account, but a secondary owner was entered in the SharePoint admin center, the secondary owner will receive an email telling them they have access to the OneDrive, and that the OneDrive will be deleted at the end of the retention period.
    
6. Seven days before the retention period expires, a second email will be sent to the manager or secondary owner as a reminder that the OneDrive will be deleted in seven days.
    
7. After seven days, the OneDrive for the deleted user is sent to the site collection recycle bin, where it is kept for 93 days. During this time, users will no longer be able to access any shared content in the OneDrive. To restore the OneDrive, you need to use PowerShell. For info, see [Restore a deleted OneDrive](restore-a-deleted-onedrive.md).
    
    > [!NOTE]
    > The Recycle Bin is not indexed and therefore searches do not find content there. This means that an eDiscovery hold can't locate any content in the Recycle Bin in order to hold it. 
  
> [!NOTE]
> Retention policies always take precedence to the standard OneDrive deletion process, so content included in a policy could be deleted before 30 days or retained for longer than the OneDrive retention. For more info, see [Overview of retention policies](https://support.office.com/article/5e377752-700d-4870-9b6d-12bfc12d2423). Likewise, if a OneDrive is put on hold as part of an eDiscovery case, managers and secondary owners will be sent email about the pending deletion, but the OneDrive won't be deleted until the hold is removed. > The retention period for cleanup of OneDrive begins when a user account is deleted from Azure Active Directory. No other action will cause the cleanup process to occur including disablement of a user account or removal of a user's license. For more information, see [Remove licenses from users in Office 365 for business](https://support.office.com/article/9b497c85-d0a4-4735-80fa-d3565bc05bd1). 
  

