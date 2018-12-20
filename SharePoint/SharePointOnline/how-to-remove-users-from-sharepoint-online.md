---
title: "How to remove users from SharePoint Online"
ms.author: kaarins
author: kaarins
manager: pamgreen
ms.date: 12/19/2018
ms.audience: Admin
ms.topic: article
f1_keywords:
- 'ViewUserProfiles'
- 'SPOTAMgUserProfiles'
ms.service: sharepoint-online
localization_priority: Normal
search.appverid:
- SPO160
- MOE150
- BSA160
- GSP150
- MET150
ms.assetid: 494bec9c-6654-41f0-920f-f7f937ea9723
description: "Learn how to remove users from SharePoint Online in different scenarios."
---

# How to remove users from SharePoint Online

This article describes how to remove users from SharePoint Online in the following scenarios:

- **Scenario 1: A user is removed from the Office 365 admin center but is still present in SharePoint Online.**
 
   When a user account is deactivated or deleted, the user's profile remains in the UserInfo list for any site collections that the user previously browsed to. This may cause confusion, primarily when you use People Picker. This includes external users.

- **Scenario 2: A mismatched Passport Unique ID (PUID).**
 
    This issue most frequently occurs when a user is deleted and the account is then re-created with the same user name. The account in the Office 365 admin center or Active Directory (in directory synchronization scenarios) is deleted and re-created with the same user principal name (UPN). The new account is created by using a different PUID value. When the user tries to access a site collection in this situation (for example, a personal site), the user has an incorrect PUID. A second scenario involves directory synchronization with an Active Directory organizational unit (OU). If the user has already logged in to SharePoint and created personal sites, and then she is later moved to a different OU and resynced with SharePoint, she may experience this problem.

## More Information

In some scenarios, you may have to remove the user account. This article describes how to do this for the various account types.

**NOTES:**

- This article shouldn't to be used for troubleshooting Profile Property synchronization or PUID issues unless otherwise advised by Microsoft Customer Support Services.
 
- Many scenarios in this article use &lt;**contoso**&gt; as a placeholder. In your scenario, replace &lt;**contoso**&gt; with the domain that you use for your organization.
 
## Standard users

### Remove a user from the Office 365 admin center

> [!NOTE]
>   If you're using directory synchronization, the user must be removed from the on-premises Active Directory environment.

To remove a standard user, first remove the user from the Office 365 admin center. To do this, follow these steps:

1.  Browse to [https://portal.office.com](https://portal.office.com/), and then sign in with your administrator account.
 
2.  In the navigation pane (on the left side), click  **Users**, and then click **Active Users**.
 
3.  Select the check box next to the user whom you want to remove, and then click **DELETE**.
 
 After you delete a user from the admin center, a series of jobs will remove the user from SharePoint Online. After the next incremental profile import job, the user (or users) will be marked as deleted, the user’s profile page will be deleted, and the user's personal site will be marked for deletion by the MySite cleanup job.

### Remove a user from the UserInfo list

The preceding steps removed the user’s access to Office 365 and SharePoint Online. However, the user still appears in people searches and in the SharePoint Online Management Shell when you use the Get-SPOUser cmdlet. To completely remove the user from SharePoint, you must remove him or her from the UserInfo list. There are two ways to do this:

**Use the SharePoint Online user interface** 

You'll have to browse to each site collection that the user had access to, and then follow these steps:
 
> [!NOTE]
>  This option will only be visible to the user if they're active in the site collection. The user must have previously browsed to the site collection. Visitors who were granted access through domain groups only won't be listed here. 


1. After you're at the site collection, edit the URL by adding the following string to the end of it: **_layouts/15/people.aspx/membershipGroupId=0**
 
 	For example, the full URL will resemble the following: **https://&lt;contoso.sharepoint.com&gt;/_layouts/15/people.aspx/membershipGroupId=0**

2. Select the user from the list, and then click **Remove User Permissions** on the ribbon.
 
**Use the SharePoint Online Management Shell**

 > [!NOTE]
 >  This option doesn't apply to Small Business subscriptions.

For more information about how to use the SharePoint Online Management Shell, see [Introduction to the SharePoint Online Management Shell](https://support.office.com/en-us/article/introduction-to-the-sharepoint-online-management-shell-c16941c3-19b4-4710-8056-34c034493429).

1. Start the SharePoint Online Management Shell.
 
2. Enter the **$cred = Get-Credential** cmdlet and in the **Windows PowerShell Credential required** dialog box, type your site collection admin account and password, and then click **OK**.
 
3. Connect to SharePoint Online, and then enter the following command:

   ```
   Connect-SPOService -Url https://<contoso>.-admin.sharepoint.com -Credential $cred
   ```
   > [!NOTE]
   >  In this scenario, replace &lt;**contoso**&gt; with the domain for your organization.

## Clear the browser cache

SharePoint Online uses browser caching in several scenarios, including the in the People Picker. Even though a user was fully removed from the system, he or she may still remain in the browser cache. Clearing the browser cache resolves this issue. To do this for Internet Explorer, follow the steps given at [Viewing and deleting your browsing history](https://support.microsoft.com/en-us/help/17438/windows-internet-explorer-view-delete-browsing-history).

When you clear the cache, make sure that you also select the **Cookies and website data** option.

## External users

### Remove the external user from SharePoint Online

External users are managed from a site-collection–by–site-collection basis. An external user account must be removed from each site collection that the user was granted access to. There are two ways to do this, depending on your subscription type: by using the Office 365 admin center or by using the SharePoint Online Management Shell.

**For Small Business subscriptions, use the Office 365 admin center:**

 > [!NOTE]
 >  This option doesn't apply to Office 365 Enterprise (E) organizations, because it will remove the user and their permissions only from the selected SharePoint site (UserInfo list) and not from the directory.

1. Browse to the Office 365 admin center at [https://portal.office.com](https://portal.office.com).
 
2. Under **service settings** click **Manage Organization-wide settings**.
 
3. On the menu on the left side, click **sites and document sharing**, and then click **Remove individual external users**.
 
4. Select the external user who must be removed, and then click the **Delete** icon.
 
**All other subscriptions must use the SharePoint Online Management Shell**

  > [!NOTE]
 >  This option doesn't apply to Office 365 Small Business (P) organizations.

For more information about how to use the SharePoint Online Management Shell, go to [Introduction to the SharePoint Online Management Shell](https://support.office.com/en-us/article/introduction-to-the-sharepoint-online-management-shell-c16941c3-19b4-4710-8056-34c034493429).

1. Start the SharePoint Online Management Shell.
 
2. Enter the **$cred = Get-Credential** cmdlet and in the **Windows PowerShell Credential** required window, type your site collection admin account and password, and then click **OK**.

3. Connect to SharePoint Online, and then enter the following command:
 
   ```
   Connect-SPOService -Url https://<contoso>.-admin.sharepoint.com -Credential $cred
   ```
4. Remove the user from each site collection by using the following command:
 
   ```
   $ExtUser = Get-SPOExternalUser -filter someone@example.com
   ```
   > [!NOTE]
   >  Replace the **someone@example.com** placeholder with the account for your scenario.

5. Emter the following command:
 
   ```
   Remove-SPOExternalUser -UniqueIDs @($ExtUser.UniqueId)
   ```
 ## Remove the external user from the UserInfo list

The preceding steps removed the external user’s access SharePoint Online. However, the user will still be returned by any people searches and by the SharePoint Online Management Shell **Get-SPOUser** cmdlet. To completely remove the user from SharePoint, he or she must be removed from the UserInfo list. There are two ways to do this:

**Use the SharePoint user interface** Browse to each site collection that the user previously had access to, and then follow these steps:

1. Browse to each site collection that the user previously had access to, and then follow these steps: **_layouts/15/people.aspx/membershipGroupId=0**

 	For example, the full URL will resemble the following: **https://&lt;contoso.sharepoint.com&gt;/_layouts/15/people.aspx/membershipGroupId=0**

2. Select the user from the lias and click **Remove User Permissions** on the ribbon.

**Use the SharePoint Online Management Shell**

  > [!NOTE]
 >  This option doesn't apply to Small Business organizations.

For more information about how to use the SharePoint Online Management Shell, go to [Introduction to the SharePoint Online Management Shell](https://support.office.com/en-us/article/introduction-to-the-sharepoint-online-management-shell-c16941c3-19b4-4710-8056-34c034493429).

1. Start the SharePoint Online Management Shell.
 
2. Enter the **$cred = Get-Credential** cmdlet and in the **Windows PowerShell Credential** required window, type your admin account and password, and then click **OK**.
 
3. Connect to SharePoint Online, and then enter the following command:
 
   ```
   Connect-SPOService -Url https://<contoso>.-admin.sharepoint.com -Credential $cred
   ```
4. Remove the user from each site collection with the following command:
 
   ```
   Get-SPOUser -Site https://<contoso>.sharepoint.com | FT –a
   ``` 
   > [!NOTE]
   >  The external user's Login Name in the returned results will have a **live.com** prefix.

   Enter the following command:

   ```
   Remove-SPOUser -Site https://&lt;contoso&gt;.sharepoint.com -LoginName live.com#jondoe@company.com
   ```
   > [!NOTE]
   >  Replace the live.com#jondoe@company.com placeholder with the user in question.

## Clear the browser cache

SharePoint Online uses browser caching in several scenarios, including the in the People Picker. Even though a user was fully removed from the system, he or she may still remain in the browser cache. Clearing the browser cache resolves this issue. To do this for Internet Explorer, follow the steps given at [Viewing and deleting your browsing history](https://support.microsoft.com/en-us/help/17438/windows-internet-explorer-view-delete-browsing-history).

When you clear the cache, make sure that you also select the **Cookies and website data** option.

Whereas Exchange Online, Skype for Business Online (formerly Lync Online), and SharePoint Online all share user management at the Office 365 admin center level, SharePoint Online maintains an additional layer of user management. The steps in this article describe how to remove both a standard user account and an external user account from the SharePoint Online environment. 

## Additional notes

- At the Office 365 admin center level, user management lets an administrator manage users (create, delete, license, and assign delegated admins) in the Azure Active Directory domain structure. The portal also allows for the management of external users for site collections, including personal sites.
 
- In the SharePoint admin center, you can manage Site Collection administrators and the User Profile accounts.
 
- When a user browses to a SharePoint Online site, their user information is cached in the UserInfo list. When the same user is removed from the Office 365 admin center, their related UserInfo information is not removed.
 
If you still need help, go to [Microsoft Community](https://answers.microsoft.com/). 