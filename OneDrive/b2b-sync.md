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

## Controlling external sharing

When you enable your users to share content from your organization externally, you can use several features in Office 365 to manage who has access to thecontent. Office 365 admins and site owners can review permissions and audit access to sites. For info, see [Searching for site content shared with external users](/office365/securitycompliance/keyword-queries-and-search-conditions) and [Turn on external sharing notifications](turn-on-external-sharing-notifications.md).You can enable external sharing with only specific internet domains, or you can block specific domains. You can also The right to create external user guest accounts may be restricted to specific members of an organization if desired. 
 
Microsoft encourages SharePoint users to create separate team sites, one per project, for content being shared externally. Sites can be clearly annotated to indicate that external users have access to avoid unintentional disclosure of information. For individual user's sharing content from their OneDrive for Business site, Microsoft recommends creating separate folders for different projects or collaboration groups. 
  
External user's permissions can be removed at any time per site or folder, or from all of the organization’s content by deleting the guest account. Please remember that any synced content will remain on the user's computer after permissions have been removed. 
 


## The external sharing process

When external sharing is enabled in your organization, and for a site, users can share the site externally. 

[Learn how to share a site](https://support.office.com/article/958771a8-d041-4eb8-b51c-afea2eae3658)

[Learn how to share a folder](https://support.office.com/article/1fe37332-0f9a-4719-970e-d2578da4941c) 

When users share an item with someone outside of your organization, the recipient receives an email. 

When the recipient clicks the link in the email to go to the shared item, they need to click "Organizational account" to sign in with their work or school account. Behind the scenes, this creates the guest account in Azure AD.

The recipient may need to enter their username or password, and then they can view the shared item. If they don't want to sync everything that was shared, they can browse to the library or folder they want to sync. To set up syncing, they need to click the Sync button. 



