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
  
## Who can access shared content

You can allow external sharing with only guests who authenticate, or you can allow users to share files and folders using links that let people outside the organization access the items anonymously. 
  
 **Guests who sign in**
  
When you share with people who have a Microsoft account or a work or school account in Azure AD from another organization, permissions and groups work the same for these guests as they do for internal users.
  
Because these guests do not have a license in your organization, they are limited to basic collaboration tasks:
  
- They can perform tasks on a site consistent with the permission level that they are assigned. For example, if you add a guest as a site member, they will have Edit permissions and they will be able to add, edit and delete lists; they will also be able to view, add, update and delete list items and files.
    
- They can use Office Online for viewing and editing documents. If your plan includes Office Professional Plus, they cannot install the desktop version of Office on their own computers unless you assign them a license. 
    
- They will be able to see other types of content on sites, depending on the permissions you give them. For example, they can navigate to different subsites within a shared site. They will also be able to do things like view site feeds.
    
If your authenticated guests need greater capability such as OneDrive storage or creating a Microsoft Flow, you must assign them an appropriate license. To do this, go to the **Active users** page of the Microsoft 365 admin center, select the guest, click **More**, and then click **Edit product licenses**.

 **Guests who have a code**

You can share files and folders with anyone who has an email address. If the person you're sharing with doesn't have a Microsoft account or a work or school account in Azure AD, they will be emailed a verification code to access the file or folder. You can't share sites with people unless they have a Microsoft account or a work or school account in Azure AD.
  
 **Anyone**
  
If you allow "Anyone" links, people inside or outside your organization can access files and folders without having to sign in or provide a code. These links can be freely passed around and are valid until the link is deleted or expires (if you've set an expiration date). You cannot verify the identity of the people using these links, but their IP address is recorded in audit logs when they access or edit shared content.
  
People who access files and folders anonymously through "Anyone" links aren't added to your organization's directory, and you can't assign them licenses. They also can't access sites anonymously. They can only view or edit the specific file or folder for which they have an "Anyone" link. 
  
## What happens when I share a site, folder, or file?

What happens behind the scenes depends on the account of the person with whom you've shared.
  
 **People who have a Microsoft account**
  
When you share a site, folder, or file with a specific person who has a Microsoft account, an invitation is sent to the person in email, which contains a link to the shared item. When the person clicks the link, they are asked to sign in using the user name and password of their Microsoft account. When they sign in, they are added as a guest in your organization's directory (you'll see them listed with **#EXT#** in their user name) and given access to the item. 
  
Once they are in your organization's directory, you can grant them access to other resources without sending them additional invitations. (You may need to send them a link to the shared item so they can find it.) You can also assign them licenses if you want.
  
You can discontinue sharing with a guest by removing their permissions from the shared item, or by removing them as a guest in your directory.
  
 **People who have a work or school account in Azure AD**
  
When you share a file or folder with a specific person who has an Office 365 work or school account in another organization, an email is sent to them which contains a link to the file or folder. The first time they access the file or folder using the link, they are sent a code to verify their identity. They must enter the code to access the file or folder. Once they have accessed the file or folder for the first time, these people are added as guests to your directory and thereafter they can access the file using thier work or school account.
  
**People who don't have a Microsoft account, or a work or school account**

When you share a file or folder with someone who doesn't have a Microsoft account, or a work or school account in another organization, an email is sent to them which contains a link to the file or folder. Each time they access the file or folder using the link, they are sent a code in email that they can use to verify their identity. They must enter the code to access the file or folder. These people are not added to your directory.
  
You can [stop sharing with someone](https://support.office.com/article/0a36470f-d7fe-40a0-bd74-0ac6c1e13323) by deleting the sharing link that was sent to them. 
  
 **Sharing using "Anyone" links**
  
When you share using an "Anyone" link, you can allow people to edit or view a file or upload to a folder. View and edit links are created separately and can be set to expire at a specified time. Once you have created these links, they can be reused and passed around freely. Anyone with the link can access the file or folder.
  
People who access files and folders using "Anyone" links aren't added to your directory. You can stop sharing with them by going to the file or folder that you shared and deleting the link.
  
## Collaborating with external business partners

If you have business partners or vendors with whom you need to collaborate or share documents, consider setting up a SharePoint Online extranet site. An extranet site is a dedicate site that you use for business-to-business collaboration guests and only guests from specific domains can be invited.
  
SharePoint Online extranet sites are very easy to set up and much easier and less expensive to maintain than on-premises extranet sites. For details, see [Use Office 365 SharePoint Online as a business-to-business (B2B) extranet solution](create-b2b-extranet.md).
  
## See also

[Coaching your guests through the external sharing experience](https://techcommunity.microsoft.com/t5/SharePoint-Support-Blog/Coaching-your-guest-users-through-the-External-Sharing/ba-p/182739)
  
[Set up and manage access requests](https://support.office.com/article/94b26e0b-2822-49d4-929a-8455698654b3)
  
[Searching for site content shared externally](/office365/securitycompliance/keyword-queries-and-search-conditions)

