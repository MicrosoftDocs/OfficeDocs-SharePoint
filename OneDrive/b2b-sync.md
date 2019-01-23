---
title: "B2B Sync"
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
description: "Learn how the OneDrive sync client allows users to sync libraries and folders shared by users in other organizations. "
---

# B2B Sync (preview)

The OneDrive sync client now lets users sync libraries or folders in SharePoint or OneDrive that have been shared from other organizations. This scenario is often referred to as Business-to-Business (B2B) Collaboration. We’re calling this new feature in the OneDrive sync client "B2B Sync". 
  
Azure Active Directory (AAD) guest accounts play a key role in making B2B Collaboration possible. A guest account at one organization links to a member account at another organization. Once created, a guest account allows Office 365 services like OneDrive and SharePoint to grant a guest permission to sites and folders the same way a member within the organization is granted permission. Since the accounts at two organizations are linked, the user only needs to remember the username and password for the account at their organization. As a result, a single sign in to their account enables access to content from their own organization and from any other organization that have created guest accounts for them. 
 
## Sharing requirements

Users share sites, libraries, and folders in different ways in SharePoint and OneDrive:

- If users are syncing a library or folder, they can right-click it in File Explorer to share it. 
- Users can go to the SharePoint site, library, or folder and click the Share button to share the it. 
- Admins can create guest accounts and use the admin center or PowerShell to add them to sites.

B2B Sync works with all these methods of sharing. It has only the following requirements:

- For guests to sync shared content, the content must be shared at the site, library, or folder level. Guests can't sync files that are shared individually. 
- B2B sync works only when guest accounts are created in the organization, and when the recipient has an Azure AD account. It doesn't work when users share by creating an anonymous access link (also known as "anyone" link or "shareable" link), or when they share with people who have a Microsoft account or other personal account. 

## Known issues with this preview release

- On PCs, the Azure AD Authentication Library (ADAL) is not currently supported for B2BSync. If your organization has enabled ADAL with OneDrive.exe or a user was configured using the OneDrive [silent account configuration](use-silent-account-configuration.md) feature (which enables ADAL), you'll need to disable ADAL to preview B2B Sync. 
 
    The following command will disable ADAL. OneDrive.exe will need to be restarted after you run this command. The user may need to enter their password after OneDrive restarts. 

    REG ADD HKCU\Software\Microsoft\OneDrive /v EnableADAL /t REG_DWORD /d 0 /f 
 
- On the Mac, Files On-Demand thumbnails will not display from external organization's sites. Thumbnails will display correctly for files from the user's own organization. 

## Overview of the B2B Sync experience

When external sharing is enabled in your organization, and for a site, users can share the site externally. 

[Learn how to share a site](https://support.office.com/article/958771a8-d041-4eb8-b51c-afea2eae3658)

[Learn how to share a folder](https://support.office.com/article/1fe37332-0f9a-4719-970e-d2578da4941c) 

After the item shared, this happens:

1. The recipient receives an email like the following. 

2. When the recipient clicks the link in the email to go to the shared item, they need to click "Organizational account" to sign in with their work or school account. Behind the scenes, this creates the guest account in Azure AD.

3. The recipient may need to enter their username or password, and then they can view the shared item. If they don't want to sync everything that was shared, they can browse to the library or folder they want to sync. To set up syncing, they need to click the Sync button. 

4. The guest’s browser will display up a message asking if they want to open "Microsoft OneDrive," and they will need to allow this. 

5. If this is the first time the guest has used the sync client with this email address, they'll need to sign in. The email address will be automatically set to the account used in the previous steps. Click Sign in.

6. The sync client may be able to sign them in without entering password if they are signed into Windows with the same account. Otherwise they'll enter their password and proceed.
 
7. They'll next confirm the location to place the sync files from the shared site. Note the content is placed in an organization name folder matching the organization owning the content. If the user is syncing content from their own organization’s SharePoint and this content from another organization, they'll have two folders matching the two organization’s names. Click Next to proceed.

8.	The next page will differ based on whether the user's computer has Files On-Demand enabled or not. But after proceeding they'll see the final page of the wizard confirming the site is ready to sync.

9.	After closing the wizard, the site will begin syncing. The user can click the blue cloud icon in the tray to open the OneDrive sync activity center to see the files syncing, open the local folder with the files, or open the SharePoint site in a web browser.

For more info, see [External sharing overview](/sharepoint/external-sharing-overview)
 
## Enable external sharing for your organization 
 
SharePoint admins may configure both global settings affecting all sites of the organization and per site settings.  Per site settings can be used to restrict sharing further than the global setting but cannot be used to enable broader sharing than global allows.

You can change your organization-wide sharing settings in three different places (all three control the same thing):

•	In the Microsoft 365 admin center, under Settings > Services & add-ins> Sites, in the OneDrive admin center. 
•	On the Sharing page in the OneDrive admin center (https://docs.microsoft.com/en-us/onedrive/manage-sharing#externalsharing)
•	On the sharing page in the in the classic SharePoint admin center.

Note: If you allow “anyone” links (sometimes referred to as “anonymous access” or “shareable”), these links do not create guest accounts and therefore don’t enable B2B Sync.

For more information please see:
•	https://docs.microsoft.com/en-us/sharepoint/turn-external-sharing-on-or-off 

## Controlling external sharing

When you allow users to share content from your organization externally, you can use several features in Office 365 to manage who has access to the content. Office 365 admins and site owners can review permissions and audit access to sites. For info, see [Searching for site content shared with external users](/office365/securitycompliance/keyword-queries-and-search-conditions) and [Turn on external sharing notifications](turn-on-external-sharing-notifications.md). You can enable external sharing with only specific internet domains, or you can block specific domains. For info, see [Restricted domains sharing](/sharepoint/restricted-domains-sharing). You can also allow only members of specific security groups to share externally. For info, see [Turn external sharing on or off](/sharepoint/turn-external-sharing-on-or-off)
 
Microsoft encourages SharePoint users to create separate team sites, one per project, for content being shared externally. Sites can be clearly annotated to indicate that external users have access to avoid unintentional disclosure of information. For individual user's sharing content from their OneDrive for Business site, Microsoft recommends creating separate folders for different projects or collaboration groups. 
  
External user's permissions can be removed at any time per site or folder, or from all of the organization’s content by deleting the guest account. Please remember that any synced content will remain on the user's computer after permissions have been removed. 
 
## Enable external sharing for a site
To view or change the sharing setting for any site, use the new SharePoint admin center.
1.	Sign in to https://admin.microsoft.com as a global or SharePoint admin.
Note: If you have Office 365 Germany, sign in at https://portal.office.de. If you have Office 365 operated by 21Vianet (China), sign in at https://login.partner.microsoftonline.cn/. Then use the app launcher to go to the admin center. 
2.	In the left pane, choose Admin centers > SharePoint.
3.	If the classic SharePoint admin center appears, click Try it now to open the new SharePoint admin center preview.
4.	Under Sites, click Active sites, and customize the view as necessary to see the External sharing column.


If you need to, change the external sharing setting for a site (https://docs.microsoft.com/en-us/sharepoint/manage-sites-in-new-admin-center#change-the-external-sharing-setting-for-a-site)
 
 
For more information please see:
•	https://docs.microsoft.com/en-us/sharepoint/turn-external-sharing-on-or-off
•	https://docs.microsoft.com/en-us/onedrive/manage-sharing
•	https://docs.microsoft.com/en-us/sharepoint/change-default-sharing-link
 
 
Use the Azure AD admin center to create guest users
To create guest users individually in the Azure AD admin center, see https://docs.microsoft.com/en-us/azure/active-directory/b2b/b2b-quickstart-add-guest-users-portal. 
8.	Once you've created your Guest accounts you can add them to a SharePoint team site via the site settings permissions dialog or by adding them to a security group that already has permissions to the site you want to share.  You'll need to take care of informing your invited guest by emailing them a link to the site you gave them permission to.

You can also use the SharePoint share flow to share to these existing guest accounts by simply entering the same email address used to create the account.  In this case the share flow has an option to send an email to the share recipient.
 
 
Use PowerShell to bulk create guest accounts for external users and add them to a SharePoint site's group
You may find you need to create and grant permissions to many external users.  Below is a PowerShell script which creates guess accounts and grants them permissions to a site.  The script takes an Excel CSV (comma separated value) file as input which contains a list of user display names and email addresses.  For each name and email address, a guest account is created and that account is added a security group to grant it permission.  The script is designed so that you can feed the resulting output CSV as input to the script on a subsequent run.  This enables you to add more users to your CSV file or to reattempt creating any failed account.
 
Once you've run the script, you'll need to email the users with a direct link to the SharePoint site you gave them permissions to.  When they click the link, they'll be presented with the below UI to accept the terms of the invitation.  Once they accept, they will be taken to the site you shared with them.  At that point they can click the sync button to begin syncing the sites files to their PC or Mac.
 
 
 
PowerShell InviteGuests.ps1
# requires latest AzureADPreview
# Get-Module -ListAvailable AzureAD*
# Uninstall-Module AzureAD 
# Uninstall-Module AzureADPreview 
# Install-Module AzureADPreview
 
 
# customizable properties for this script
 
$csvDir = ''
$csvInput = $csvDir + 'BulkInvite.csv'
$csvOutput = $csvDir + 'BulkInviteResults.csv'
 
$domain = 'YourTenantOrganization.onmicrosoft.com'
$admin = "admin@$domain"
$redirectUrl = 'https://YourTenantOrganization.sharepoint.com/sites/SiteName/'
$groupName = 'SiteName'
 
 
# CSV file expected format (with the header row):
# Name,Email
# Jane Doe,jane@contoso.com
 
$csv = import-csv $csvInput
 
# will prompt for credentials for the tenantorganization admin account (who has permissions to send invites and add to groups)
Connect-AzureAD -TenantDomain $domain -AccountId $admin
 
$group = (Get-AzureADGroup -SearchString $groupName)
 
foreach ($row in $csv)
{
    Try
    {
        if ((Get-Member -inputobject $row -name 'error') -and `
            ($row.error -eq 'success'))
        {
            $out = $row  #nothing to do, user already invited and added to group
        }
        else
        {
            echo ("name='$($row.Name)' email='$($row.Email)'")
 
            $inv = (New-AzureADMSInvitation -InvitedUserEmailAddress $row.Email -InvitedUserDisplayName $row.Name `
                        -InviteRedirectUrl $redirectUrl -SendInvitationMessage $false)
 
            $out = $row
            $out|Add-Member -MemberType ScriptProperty -force -name 'time' -Value {$(Get-Date -Format u)}
            $out|Add-Member -MemberType ScriptProperty -force -name 'status' -Value {$inv.Status}
            $out|Add-Member -MemberType ScriptProperty -force -name 'userId' -Value {$inv.InvitedUser.Id}
            $out|Add-Member -MemberType ScriptProperty -force -name 'redeemUrl' -Value {$inv.inviteRedeemUrl}
            $out|Add-Member -MemberType ScriptProperty -force -name 'inviteId' -Value {$inv.Id}
 
            # this will send a welcome to the group email
            Add-AzureADGroupMember -ObjectId $group.ObjectId -RefObjectId $inv.InvitedUser.Id
 
            $out|Add-Member -MemberType ScriptProperty -force -name 'error' -Value {'success'}
        }
    }
    Catch
    {
        $err = $PSItem.Exception.Message
        $out|Add-Member -MemberType ScriptProperty -force -name 'error' -Value {$err}
    }
    Finally
    {
        $out | export-csv -Path $csvOutput -Append
    }
}
 
# for more information please see
# https://docs.microsoft.com/ azure/active-directory/b2b/b2b-tutorial-bulk-invite
# end of InviteGuests.ps1 powershell script
 
For more information see:
•	https://docs.microsoft.com/ azure/active-directory/b2b/redemption-experience
•	https://docs.microsoft.com/ azure/active-directory/b2b/add-user-without-invite

When a guest loses access to a shared library
 
If a person’s guest account is deleted or their permission to a library being synced is removed, the sync client will indicate there is a problem with the library.
 
•	A notification will appear indicating that the library can’t be synced.
 
 
•	The OneDrive icon in the notification area will show an error.
 
 
When the guest clicks the icon, they will see an error banner in the activity center.
 
 
When they click the “One or more libraries could not be synced” banner, they can learn how to resolve the issue.
