---
title: "OneDrive retention and deletion"
ms.author: v-thehay
author: SteyerTHaynie
manager: scotv
ms.date: 4/24/2018
ms.audience: ITPro
ms.topic: article
ms.prod: office-online-server
localization_priority: Normal
ms.assetid: ef883c48-332c-42f5-8aea-f0e2366c15f9
description: "This article describes the process that occurs for OneDrive for Business when the user account that owns a OneDrive for Business site collection is deleted from Azure Active Directory."
---

# OneDrive retention and deletion

This article describes the process that occurs for OneDrive for Business when the user account that owns a OneDrive for Business site collection is deleted from Azure Active Directory.
  
## Retention and deletion overview (aka )

When a OneDrive for Business site collection is scheduled for deletion, the default action is to transfer ownership of the site to the manager of the original work account or school account that is being deleted. For this to occur, the user profile **Manager** property must be set for the original owner of the OneDrive for Business site. The **Access Delegation** setting is configured in the SharePoint admin center. This setting is located in **Setup My Sites** under the **User Profiles** section. By default, **Access Delegation** is enabled. We recommend that you also configure a secondary owner account in this section. This account will be the appointed owner of the site collection if the user profile **Manager** property isn't set for the original site owner. Email notifications will also be sent to the secondary owner account when the value is populated. When a manager or secondary owner isn't set for the user profile, or if the **Access Delegation** setting is disabled, the profile and OneDrive for Business site collection will follow the same deletion process that's described in the next section. However, no email messages will be sent. 
  
### The profile and OneDrive cleanup process in SharePoint Online

1. A work or school account is deleted from the Office 365 admin center or is removed through Active Directory synchronization.
    
2. The account deletion is synchronized to SharePoint Online.
    
3. The OneDrive Clean Up Job runs, and the user profile is marked for deletion. The profile will be preserved in the database in a deleted state. The default retention period is 30 days but this value can be modified by using the **-OrphanedPersonalSitesRetentionPeriod** parameter for the **Set-SPOTenant** cmdlet in the SharePoint Online Management Shell. For more information about the **Set-SPOTenant** cmdlet, go to the following Microsoft web site: 
    
    [Set-SPOTenant](https://technet.microsoft.com/en-us/library/fp161390.aspx)
    
4. If the **Manager** field is populated for the deleted account, the manager will receive an email message that states that the site will be removed after the retention period expires, and that access to the site is granted to the manager. 
    
5. If the **Manager** field isn't populated for the user account and a secondary owner was configured in **Setup My Sites** under the **User Profile** section of the SharePoint admin center, the secondary owner contact will receive an email message that states that the site will be removed after the retention period expires, and that access to the site is granted to the user. 
    
6. Seven days before the retention period expires, a second email message will be sent to the manager or secondary owner that states that the site will be deleted in seven days.
    
7. After seven days, the profile for the deleted account is deleted from the user profile service.
    
The personal site (that is, the OneDrive for Business site) for the deleted account is sent to the site collection recycle bin. The site is deleted from the recycle bin according to the site collection recycle bin retention policy, which is 90 days. The site isn't listed in the site collection recycle bin user interface (UI). You can however confirm its presence by using the **Get-SPODeletedSite** cmdlet for the SharePoint Online Management Shell. For more information about the **Get-SPODeletedSite** cmdlet, go to the following Microsoft web site: 
  
[Get-SPODeletedSite](https://technet.microsoft.com/library/fp161365.aspx)
  
For more information about the SharePoint Online admin center recycle bin, go to the following Microsoft website:
  
[Restore a deleted site collection](https://support.office.com/en-us/article/restore-a-deleted-site-collection-91c18651-c017-47d1-9c27-3a22f325d6f1)
  
### Notes

- If the user's profile is deleted from the SharePoint admin center at any time before the OneDrive Clean Up Job runs against the deleted user, the process won't run for that user profile because the profile no longer exists in the user profile service. No email messages will be sent. The OneDrive site won't be removed, and an orphaned site collection will result. You should never delete user profiles manually unless you are instructed to do this by Microsoft Customer Support Services.
    
- If the site is put on hold as part of an eDiscovery case, the site won't be deleted by using this process until the hold is removed. Although an email message is sent as part of the site deletion process (as described in steps 4 and 7), the site will remain on hold until the hold is removed.
    
- The retention period for cleanup of OneDrive begins when a user account is deleted from Azure Active Directory. No other action will cause the cleanup process to occur including disablement of a user account or removal of a user's license. For more information, go to the following Microsoft website:
    
    [Assign or unassign licenses for Office 365 for Business](https://support.office.com/en-us/article/assign-or-unassign-licenses-for-office-365-for-business-997596b5-4173-4627-b915-36abac6786dc?ui=en-us)
    
Still need help? Go to [Microsoft Community](https://answers.microsoft.com/)
  

