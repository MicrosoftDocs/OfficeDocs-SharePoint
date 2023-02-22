---
ms.date: 01/07/2019
title: "Remove users from SharePoint"
ms.reviewer: waynewin
ms.author: serdars
author: SerdarSoysal
manager: serdars
recommendations: true
audience: Admin
f1.keywords:
- CSH
ms.topic: article
ms.custom:
- 'ViewUserProfiles'
- 'SPOTAMgUserProfiles'
- 'seo-marvel-apr2020'
ms.service: sharepoint-online
ms.collection: M365-collaboration
ms.localizationpriority: medium
search.appverid:
- SPO160
- MOE150
- BSA160
- GSP150
- MET150
ms.assetid: 494bec9c-6654-41f0-920f-f7f937ea9723
description: "In this article, you'll learn how to remove users from SharePoint in different scenarios."
---

# How to remove users from SharePoint

This article describes how to remove users so they no longer appear in SharePoint. It should be used to troubleshoot Profile Property synchronization or mismatched ID issues only as advised by Microsoft Customer Support Services.

- **Scenario 1: Someone is deleted from the Microsoft 365 admin center but still appears in SharePoint.**
 
    When a user or guest browses to a SharePoint site, their user information is cached in the UserInfo list. When the user or guest is deleted, their related UserInfo information is not removed. Their profile still appears, which may cause confusion when people view the people picker.

- **Scenario 2: Site User ID Mismatch.**
 
    This issue most frequently occurs when a user is deleted and the account is then re-created with the same user name. The account in the Microsoft 365 admin center or Active Directory (in directory synchronization scenarios) is deleted and re-created with the same user principal name (UPN). The new account is created by using a different ID value. When the user tries to access a site collection or their OneDrive, the user has an incorrect ID. A second scenario involves directory synchronization with an Active Directory organizational unit (OU). If users have already signed in to SharePoint, and then are moved to a different OU and resynced with SharePoint, they may experience this problem.
 
## Delete a user from the Microsoft 365 admin center

For the steps to delete a user in the Microsoft 365 admin center, see [Delete a user from your organization](/office365/admin/add-users/delete-a-user).
 
> [!NOTE]
>   If you're using directory synchronization, you must remove the user from the on-premises Active Directory environment.

 After you delete a user, a series of jobs will remove the user from SharePoint. After the next incremental profile import job, the user (or users) will be marked as deleted, the user's profile page will be deleted, and the user's OneDrive will be marked for deletion by the MySite cleanup job.

## Delete a guest from the Microsoft 365 admin center

1. Sign in to https://admin.microsoft.com as a Global Administrator or SharePoint Administrator. (If you see a message that you don't have permission to access the page, you don't have Microsoft 365 admin permissions in your organization.)
    
    > [!NOTE]
    > If you have Office 365 operated by 21Vianet (China), sign in at https://login.partner.microsoftonline.cn/. Then select the Admin tile to open the admin center.  
    
2. In the left pane, select **Users** \> **Guest users**.

3. Select **Delete a user**.

4. Select the user, click **Select**, and then click **Delete**.
 
## Delete a guest by using the SharePoint Online Management Shell

1. [Install the SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).

2. Connect to SharePoint as a [Global Administrator or SharePoint Administrator](./sharepoint-admin-role.md) in Microsoft 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).
    
3. Run the following command:
 
   ```PowerShell
   Connect-SPOService -Url https://fabrikam-admin.sharepoint.com -Credential $cred
   ```
4. Remove the guest from each site collection by using the following command:
 
   ```PowerShell
   $ExtUser = Get-SPOExternalUser -filter jondoe@fabrikam.com
   ```
   > [!NOTE]
   >  Replace the **jondoe\@fabrikam.com** placeholder with the account for your scenario.

5. Enter the following command:
 
   ```PowerShell
   Remove-SPOExternalUser -UniqueIDs @($ExtUser.UniqueId)
    ```

## Remove people from the UserInfo list

The preceding steps removed access to Microsoft 365 and SharePoint. However, the user or guest still appears in people searches and in the SharePoint Online Management Shell when you use the Get-SPOUser cmdlet. To completely remove people from SharePoint, you must remove them from the UserInfo list. There are two ways to do this:

### Site by site in SharePoint 

You'll have to browse to each site collection that the user or guest visited, and then follow these steps:
 
> [!NOTE]
> This option is available only if the user previously browsed to the site collection. They won't be listed if they were granted access but never visited the site. 

1. Browse to the site and edit the URL by adding the following string to the end of it: **/_layouts/15/people.aspx?MembershipGroupId=0**
 
     For example, the full URL will resemble the following: **`https://fabrikam.sharepoint.com/_layouts/15/people.aspx?membershipGroupId=0`**

2. Select the person from the list, and then on the **Actions** menu, select **Delete Users from Site Collection**.
 
### Using the SharePoint Online Management Shell

1. [Install the SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).

2. Connect to SharePoint as a [Global Administrator or SharePoint Administrator](./sharepoint-admin-role.md) in Microsoft 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).
    
3. Run the following command:

   ```PowerShell
   Remove-SPOUser -Site https://fabrikam.sharepoint.com -LoginName jondoe@fabrikam.com
   ```
   > [!NOTE]
   >  Replace the _jondoe@fabrikam.com_ placeholder with the person in question.  

## Clear browser history

SharePoint uses browser caching in several scenarios, including in the people picker. Even when a user is fully removed, he or she may still remain in the browser cache. Clearing the browser history resolves this issue. For info about doing this in Edge, see [View and delete browser history in Microsoft Edge](https://support.microsoft.com/help/10607).

When you clear the browser history, make sure that you also select to clear cookies and website data.

