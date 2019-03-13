---
title: "External sharing overview"
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.audience: Admin
ms.topic: article
f1_keywords:
- 'quickshare'
- 'o365p_enablespextluser'
- 'O365P_AddSPExtlUser'
- 'O365M_EnableSPExtlUser'
- 'O365E_EnableSPExtlUser'
ms.service: sharepoint-online
localization_priority: Priority
ms.custom: Adm_O365
ms.collection:  
- Strat_OD_share
- M365-collaboration
search.appverid:
- SPO160
- MOE150
- MED150
- MBS150
- BSA160
- BCS160
- GSP150
- MET150
ms.assetid: c8a462eb-0723-4b0b-8d0a-70feafe4be85
description: "Learn about the external sharing options in SharePoint Online."
---

# External sharing overview

If your organization performs work that involves sharing documents or collaborating directly with vendors, clients, or customers, then you can use the external sharing features of SharePoint Online to share content with people outside your organization. Or, if this is not the case, you may want to limit the use of external sharing in your organization. Planning for external sharing should be included as part of your overall permissions planning for SharePoint Online. In this article, we look at the SharePoint Online sharing options and how to plan for them.
  
(If you want to get straight to setting up sharing, see [Turn external sharing on or off for SharePoint Online](turn-external-sharing-on-or-off.md). If you're trying to share a file or folder, see [Share OneDrive files and folders](https://support.office.com/article/9fcc2f7d-de0c-4cec-93b0-a82024800c07) or [Share SharePoint files or folders in Office 365](https://support.office.com/article/1fe37332-0f9a-4719-970e-d2578da4941c).)
  
> [!NOTE]
> External sharing is turned on by default for your entire SharePoint Online environment and the sites in it. You may want to [turn it off globally](turn-external-sharing-on-or-off.md) before people start using sites or until you know exactly how you want to use the feature. 
  
## How do the external sharing settings work?

SharePoint Online has both global (organization-level) external sharing settings, and settings at the site level (previously called "site collection" level). The organization-level settings override any settings at the site level, and also affect OneDrive.
  
Whichever option you choose, the more restrictive functionality is still available. For example, if you choose to allow sharing using "Anyone" links (previously called "shareable" links or "anonymous access" links), users can still share with guests who sign in, and with internal users. 
  
 **Security and privacy**
  
If you have confidential information that should never be shared externally, consider storing the information in a site that has external sharing turned off. Create additional sites as needed to use for external sharing. This helps you to manage security risk by preventing external access to sensitive information.

> [!NOTE]
> When users share a folder with multiple guests, the guests will be able to see each other's names and email addresses in the sharing properties.
  
## What happens when users share

When users share with people outside the organization, an invitation is sent to the person in email, which contains a link to the shared item.
  
 **Recipients who sign in**
  
When users share *sites*, recipients will be prompted to sign in with:
- A Microsoft account
- A work or school account in Azure AD from another organization

When users share *files and folders*, recipients will also be prompted to sign in if they have:
- A Microsoft account

These recipients will typically be added to your directory as guests, and then permissions and groups work the same for these guests as they do for internal users.
  
Because these guests do not have a license in your organization, they are limited to basic collaboration tasks:
  
- They can use Office Online for viewing and editing documents. If your plan includes Office Professional Plus, they cannot install the desktop version of Office on their own computers unless you assign them a license. 

- They can perform tasks on a site consistent with the permission level that they are assigned. For example, if you add a guest as a site member, they will have Edit permissions and they will be able to add, edit and delete lists; they will also be able to view, add, update and delete list items and files.
    
- They will be able to see other types of content on sites, depending on the permissions you give them. For example, they can navigate to different subsites within a shared site. They will also be able to do things like view site feeds.
    
If your authenticated guests need greater capability such as OneDrive storage or creating a Microsoft Flow, you must assign them an appropriate license. To do this, go to the **Active users** page of the Microsoft 365 admin center, select the guest, click **More**, and then click **Edit product licenses**.

 **Recipients who provide a verification code**

When users share files or folders, recipients will be asked to enter a verification code if they have:

- A work or school account in Azure AD from another organization
- An email address that isn't a Microsoft account or a work or school account in Azure AD

If the recipient has a work or school account, they only need to enter the code the first time. Then they will be added as a guest and can sign in with their organization's user name and password.

If the recipient doesn't have a work or school account, they need to use a code each time they access the file or folder, and they are not added to your directory.

> [!NOTE]
> Sites can't be shared with people unless they have a Microsoft account or a work or school account in Azure AD.
  
 **Recipients who don't need to authenticate**
  
If you allow "Anyone" links, people inside or outside your organization can access files and folders without having to sign in or provide a code. These links can be freely passed around and are valid until the link is deleted or expires (if you've set an expiration date). You cannot verify the identity of the people using these links, but their IP address is recorded in audit logs when they access or edit shared content.
  
People who access files and folders anonymously through "Anyone" links aren't added to your organization's directory, and you can't assign them licenses. They also can't access sites anonymously. They can only view or edit the specific file or folder for which they have an "Anyone" link. 
  
## Stopping sharing

You can stop sharing with guests by removing their permissions from the shared item, or by removing them as a guest in your directory.
  
You can stop sharing with people who have an "Anyone" link by going to the file or folder that you shared and deleting the link.

 [Learn how to stop sharing an item](https://support.office.com/article/0a36470f-d7fe-40a0-bd74-0ac6c1e13323) 
  
## Collaborating with external business partners

If you have business partners or vendors with whom you need to collaborate or share documents, consider setting up a SharePoint Online extranet site. An extranet site is a dedicate site that you use for business-to-business collaboration guests and only guests from specific domains can be invited.
  
SharePoint Online extranet sites are very easy to set up and much easier and less expensive to maintain than on-premises extranet sites. For details, see [Use Office 365 SharePoint Online as a business-to-business (B2B) extranet solution](create-b2b-extranet.md).
  
## See also

[Coaching your guests through the external sharing experience](https://techcommunity.microsoft.com/t5/SharePoint-Support-Blog/Coaching-your-guest-users-through-the-External-Sharing/ba-p/182739)
  
[Set up and manage access requests](https://support.office.com/article/94b26e0b-2822-49d4-929a-8455698654b3)
  
[Searching for site content shared externally](/office365/securitycompliance/keyword-queries-and-search-conditions)

