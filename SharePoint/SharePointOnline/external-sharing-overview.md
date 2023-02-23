---
ms.date: 07/11/2018
title: "External sharing overview"
ms.reviewer: srice
ms.author: mikeplum
author: MikePlumleyMSFT
manager: serdars
recommendations: true
audience: Admin
f1.keywords:
- CSH
ms.topic: article
ms.custom:
- 'quickshare'
- 'o365p_enablespextluser'
- 'O365P_AddSPExtlUser'
- 'O365M_EnableSPExtlUser'
- 'O365E_EnableSPExtlUser'
-  seo-marvel-apr2020
-  Adm_O365
ms.service: sharepoint-online
ms.localizationpriority: high
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
description: "Learn about the external sharing options in SharePoint in Microsoft 365. These options allow users in your organization to share content with people outside the organization."
---

# External sharing overview

The external sharing features of Microsoft SharePoint let users in your organization share content with people outside the organization (such as partners, vendors, clients, or customers). You can also use external sharing to share between licensed users on multiple Microsoft 365 subscriptions if your organization has more than one subscription. External sharing in SharePoint is part of [secure collaboration with Microsoft 365](/microsoft-365/solutions/setup-secure-collaboration-with-teams).

Planning for external sharing should be included as part of your overall permissions planning for SharePoint in Microsoft 365. This article describes what happens when users share, depending on what they're sharing and with whom. 

If you want to get straight to setting up sharing, choose the scenario you want to enable:

- [Collaborate with guests on a document](/Office365/Enterprise/collaborate-on-documents)
- [Collaborate with guests in a site](/Office365/Enterprise/collaborate-in-a-site)
- [Collaborate with guests in a team](/Office365/Enterprise/collaborate-as-a-team)

(If you're trying to share a file or folder, see [Share OneDrive files and folders](https://support.office.com/article/9fcc2f7d-de0c-4cec-93b0-a82024800c07) or [Share SharePoint files or folders in Microsoft 365](https://support.office.com/article/1fe37332-0f9a-4719-970e-d2578da4941c).)
  
> [!NOTE]
> External sharing is turned on by default for your entire SharePoint environment and the sites in it. You may want to [turn it off globally](turn-external-sharing-on-or-off.md) before people start using sites or until you know exactly how you want to use the feature. 
  
## How the external sharing settings work

SharePoint has external sharing settings at both the organization level and the site level (previously called the "site collection" level). To allow external sharing on any site, you must allow it at the organization level. You can then restrict external sharing for other sites. If a site's external sharing option and the organization-level sharing option don't match, the most restrictive value will always be applied.
  
Whichever option you choose at the organization or site level, the more restrictive functionality is still available. For example, if you choose to allow unauthenticated sharing using "Anyone" links (previously called "shareable" links or "anonymous access" links), users can still share with guests, who sign in, and with internal users. 

> [!IMPORTANT]
> Even if your organization-level setting allows external sharing, not all new sites allow it by default. The default sharing setting for Microsoft 365 group-connected team sites is "New and existing guests." The default for communication sites and classic sites is "Only people in your organization." 
  
**Security and privacy**
  
If you have confidential information that should never be shared externally, we recommend storing the information in a site that has external sharing turned off. Create additional sites as needed to use for external sharing. This helps you to manage security risk by preventing external access to sensitive information.

> [!NOTE]
> To limit *internal* sharing of contents on a site, you can prevent site members from sharing, and enable access requests. For info, see [Set up and manage access requests](https://support.office.com/article/94B26E0B-2822-49D4-929A-8455698654B3). 
> 
> When users share a folder with multiple guests, the guests will be able to see each other's names in the Manage Access panel for the folder (and any items within it).
  
## Sharing Microsoft 365 group-connected team sites

When you or your users create Microsoft 365 groups (for example in Outlook, or by creating a team in Microsoft Teams), a SharePoint team site is created. Admins and users can also create team sites in SharePoint, which creates a Microsoft 365 group. For group-connected team sites, the group owners are added as site owners, and the group members are added as site members. In most cases, you'll want to share these sites by adding people to the Microsoft 365 group. However, you can share only the site. 

> [!IMPORTANT]
> It's important that all group members have permission to access the team site. If you remove the group's permission, many collaboration tasks (such as sharing files in Teams chats) won't work. Only add guests to the group if you want them to be able to access the site. For info about guest access to Microsoft 365 groups, see [Manage guest access in Groups](/office365/admin/create-groups/manage-guest-access-in-groups).  

## What happens when users share

When users share with people outside the organization, an invitation is sent to the person in email, which contains a link to the shared item.
  
 **Recipients who sign in**
  
When users share *sites*, recipients will be prompted to sign in with:
- A Microsoft account
- A work or school account in Azure AD from another organization

![Sign-in screen](media/sign-in-msa-org.png)

When users share *files and folders*, recipients will also be prompted to sign in if they have:
- A Microsoft account

These recipients will typically be added to your directory as guests, and then permissions and groups work the same for these guests as they do for internal users. (To ensure that all guests are added to your directory, use the [SharePoint and OneDrive integration with Azure AD B2B](./sharepoint-azureb2b-integration.md).)
  
Because these guests do not have a license in your organization, they are limited to basic collaboration tasks:
  
- They can use Office.com for viewing and editing documents. If your plan includes Office Professional Plus, they can't install the desktop version of Office on their own computers unless you assign them a license. 

- They can perform tasks on a site based on the permission level that they've been given. For example, if you add a guest as a site member, they will have Edit permissions and they will be able to add, edit and delete lists; they will also be able to view, add, update and delete list items and files.
    
- They will be able to see other types of content on sites, depending on the permissions they've been given. For example, they can navigate to different subsites within a shared site. They will also be able to do things like view site feeds.
    
If your authenticated guests need greater capability such as OneDrive storage or creating a Power Automate flow, you must assign them an appropriate license. To do this, sign in to the [Microsoft 365 admin center](https://admin.microsoft.com) as a Global Administrator, make sure the Preview is off, go to the **Active users** page, select the guest, click **More**, and then click **Edit product licenses**.

 **Recipients who provide a verification code**

When users share files or folders, recipients will be asked to enter a verification code if they have:

- A work or school account in Azure AD from another organization
- An email address that isn't a Microsoft account or a work or school account in Azure AD

![Enter Verification Code screen](media/verification-code.png)

If Azure AD B2B integration is not enabled, recipients will enter the code each time they access the file or folder and are not added to your directory.

If Azure AD B2B integration is enabled, recipients may be prompted to sign in or use a one-time passcode, depending on your organization's Azure AD B2B settings.

More information about Azure AD B2B integration can be found at [SharePoint and OneDrive integration with Azure AD B2B](sharepoint-azureb2b-integration.md).

> [!NOTE]
> Sites can't be shared with people unless they have a Microsoft account or a work or school account in Azure AD.
  
 **Recipients who don't need to authenticate**
  
Anyone with the link (inside or outside your organization) can access files and folders without having to sign in or provide a code. These links can be freely passed around and are valid until the link is deleted or expires (if you've set an expiration date). You cannot verify the identity of the people using these links, but their IP address is recorded in audit logs when they access or edit shared content.
  
![Sharing a folder by using an "Anyone" link](media/anyone-link.png)

People who access files and folders through "Anyone" links aren't added to your organization's directory, and you can't assign them licenses. They also can't access sites using an "Anyone" link. They can only view or edit the specific file or folder for which they have an "Anyone" link. 
  
## Stopping sharing

You can stop sharing with guests by removing their permissions from the shared item, or by removing them as a guest in your directory.
  
You can stop sharing with people who have an "Anyone" link by going to the file or folder that you shared and deleting the link.

 [Learn how to stop sharing an item](https://support.office.com/article/0a36470f-d7fe-40a0-bd74-0ac6c1e13323) 
  
## Need more help?

[!INCLUDE[discussionforums.md](includes/discussionforums.md)]

## See also

[How Microsoft manages and enables external sharing and collaboration with SharePoint (Microsoft Ignite)](https://www.youtube.com/watch?v=dK5uky1bJ1Y)

[Coaching your guests through the external sharing experience](https://techcommunity.microsoft.com/t5/SharePoint-Support-Blog/Coaching-your-guest-users-through-the-External-Sharing/ba-p/182739)
  
[Set up and manage access requests](https://support.office.com/article/94b26e0b-2822-49d4-929a-8455698654b3)
  
[Searching for site content shared externally](/office365/securitycompliance/keyword-queries-and-search-conditions)

[Configure Teams with three tiers of protection](/microsoft-365/solutions/configure-teams-three-tiers-protection)

[Create a secure guest sharing environment](/Office365/Enterprise/create-a-secure-guest-sharing-environment)

[Settings interactions between Microsoft 365 Groups, Teams and SharePoint](/microsoft-365/solutions/groups-sharepoint-teams-governance)

[Pricing - Active Directory External Identities](https://azure.microsoft.com/pricing/details/active-directory/external-identities/)

