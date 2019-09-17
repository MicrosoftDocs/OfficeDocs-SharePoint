---
title: Sharing and permissions in the SharePoint modern experience
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
audience: Admin
ms.topic: article
ms.service: sharepoint-online
ms.collection:  
- Strat_SP_modern
- M365-collaboration
search.appverid:
- SPO160
- MET150
localization_priority: Priority
description: "Learn about sharing and permissions in the SharePoint modern experience"
---

# Sharing and permissions in the SharePoint modern experience

Traditionally, SharePoint permissions have been managed through a set of permissions groups within a site (Owners, Members, Visitors, etc.). In SharePoint Online, this remains true for some types of sites, but additional options are available.

The three main types of sites in SharePoint are:

- Team sites - Team sites provide a collaboration environment for your teams and projects. Each team site, by default, is part of an Office 365 group, which includes a mailbox, shared calendar, and other collaboration tools. Team sites may also be part of a team in Microsoft Teams. Permissions for team sites are best managed through the associated Office 365 group or Teams team.
- Communication sites - Communication sites are for broadcasting news and status across the organization. Communication site permissions are managed by using the SharePoint Owners, Members, and Visitors groups for the site.
- Hub sites - Hub sites are team sites or communication sites that the administrator has designated as a hub. They are designed to provide connection through shared navigation between related sites. Permissions for hub sites can be managed through the Owners, Members, and Visitors groups, or through the associated Office 365 group if there is one. Special permissions are needed to associate sites to a hub site.

## Hub site permissions

Hub site owners define the shared experiences for hub navigation and theme. Hub site members create content on the hub site as with any other SharePoint site. Owners and members of the sites associated with the parent hub create content on individual sites.

admin must specify users who can add sites to hub

connected site perms are managed separately

perms to hub site depend on whether group-connected or not



## Communication site permissions

Communication sites use the standard SharePoint permissions groups:

- Owners
- Members
- Visitors



## Team site permissions and Office 365 Groups

In SharePoint Online, each SharePoint team site is part of an Office 365 group. An Office 365 group is a single permissions group that is associated with a variety of Office 365 services, including a SharePoint site, an instance of Planner, a mailbox, a shared calendar, and others. When you add owners or members to the Office 365 group, they are given access to the SharePoint site along with the other connected services.

While you can continue to manage SharePoint site permissions separately by using SharePoint groups, we recommend managing permissions for SharePoint by adding people to or removing them from the associated Office 365 group. This provides easier administration as well as giving users access to a host of related services that they can use for better collaboration.

### Using team sites with Teams

Microsoft Teams provides a hub for collaboration by bringing together a variety of services including a SharePoint team site. Teams uses the associated Office 365 group to manage its permissions.

Within the Teams experience, users can directly access SharePoint along with the other services without having to switch applications. This provides a centralized collaboration space with a single place to manage permissions. For collaboration scenarios in your organization, we highly recommend using Teams rather than using services such as SharePoint independently.

For details about how SharePoint and Teams interact, see [How SharePoint Online and OneDrive for Business interact with Microsoft Teams](https://docs.microsoft.com/microsoftteams/sharepoint-onedrive-interact).

## Managing site permissions with security groups




## Sharable links

When users share files and folders, a shareable link is created which has permissions to the item. There are three primary link types:

  - *Anyone* links give access to the item to anyone who has the link. People using an *Anyone* link do not have to authenticate, and their access cannot be audited.
  
    ![Diagram showing how anyone links can be passed from user to user](media/DMC_SharePointSharingLinks_Anyone.png)
      
    An *anyone* link is a transferrable, revocable secret key. It's transferrable because it can be forwarded to others. It's revocable because by deleting the link, you can revoke the access of everyone who got it through the link. It's secret because it can't be guessed or derived. The only way to get access is to get the link, and the only way to get the link is for somebody to give it to you.  

  - *People in your organization* links work for only people inside your Office 365 organization. (They do not work for guests in the directory, only members).  

    ![Diagram showing how people in my organization links can be passed from user to user inside the company](media/DMC_SharePointSharingLinks_PeopleInYourOrganization.png)
      
    Like an *anyone* link, a *people in my organization* link is a transferrable, revocable secret key. Unlike an *anyone* link, these links only work for people inside your Office 365 organization. When somebody opens a *people in my organization* link, they need to be authenticated as a member in your directory. If they're not currently signed-in, they'll be prompted to sign-in.  

  - *Specific people* links only work for the people that users specify when they share the item.  

    ![Diagram showing how specific people links only work for the people specified](media/DMC_SharePointSharingLinks_Specific.png)
      
    A *specific people* link is a non-transferable, revocable secret key. Unlike *anyone* and *people in my organization* links, a *specific people* link will not work if it's opened by anybody except for the person specified by the sender.  
      
    *Specific people* links can be used to share with internal or external users. In both cases, the recipient will need to authenticate as the user specified in the link.  

It's important to educate your users in how these sharing links work and which they should use to best maintain the security of your data. Send your users links to [Share OneDrive files and folders](https://support.office.com/article/9fcc2f7d-de0c-4cec-93b0-a82024800c07) and [Share SharePoint files or folders](https://support.office.com/article/1fe37332-0f9a-4719-970e-d2578da4941c), and include information about your organization's policies for sharing information.




## Guest sharing

The external sharing features of SharePoint Online let users in your organization share content with people outside the organization (such as partners, vendors, clients, or customers). You can also use external sharing to share between licensed users on multiple Office 365 subscriptions if your organization has more than one subscription. Planning for external sharing should be included as part of your overall permissions planning for SharePoint Online. This article describes what happens when users share, depending on what they're sharing and with whom. 
  
(If you want to get straight to setting up sharing, see [Turn external sharing on or off for SharePoint Online](turn-external-sharing-on-or-off.md). If you're trying to share a file or folder, see [Share OneDrive files and folders](https://support.office.com/article/9fcc2f7d-de0c-4cec-93b0-a82024800c07) or [Share SharePoint files or folders in Office 365](https://support.office.com/article/1fe37332-0f9a-4719-970e-d2578da4941c).)
  
> [!NOTE]
> External sharing is turned on by default for your entire SharePoint Online environment and the sites in it. You may want to [turn it off globally](turn-external-sharing-on-or-off.md) before people start using sites or until you know exactly how you want to use the feature. 
  
SharePoint Online has external sharing settings at both the organization level and the site level (previously called the "site collection" level). To allow external sharing on any site, you must allow it at the organization level. You can then restrict external sharing for other sites. If a site's external sharing option and the organization-level sharing option don't match, the most restrictive value will always be applied.
  
Whichever option you choose at the organization or site level, the more restrictive functionality is still available. For example, if you choose to allow sharing using "Anyone" links (previously called "shareable" links or "anonymous access" links), users can still share with guests who sign in, and with internal users. 

> [!IMPORTANT]
> Even if your organization-level setting allows external sharing, not all new sites allow it by default. The default sharing setting for Office 365 group-connected team sites is "New and existing guests." The default for communication sites and classic sites is "Only people in your organization." 
  
**Security and privacy**
  
If you have confidential information that should never be shared externally, we recommend storing the information in a site that has external sharing turned off. Create additional sites as needed to use for external sharing. This helps you to manage security risk by preventing external access to sensitive information.

> [!NOTE]
> To limit *internal* sharing of contents on a site, you can prevent site members from sharing, and enable access requests. For info, see [Set up and manage access requests](https://support.office.com/article/94B26E0B-2822-49D4-929A-8455698654B3). <br>When users share a folder with multiple guests, the guests will be able to see each other's names in the Manage Access panel for the folder (and any items within it).




## SharePoint and OneDrive integration with Azure AD B2B (Preview)


Azure AD B2B provides authentication and management of guest users. Authentication happens via one-time passcode when they don't already have a work or school account or a Microsoft account (MSA).

With SharePoint and OneDrive integration, the Azure B2B one-time passcode feature is used for external sharing of files, folders, list items, document libraries and sites. This feature provides an upgraded experience from the existing [secure external sharing recipient experience](https://docs.microsoft.com/sharepoint/what-s-new-in-sharing-in-targeted-release). 

Enabling the preview does not change your sharing settings. For example, if you have site collections where external sharing is turned off, it will remain off.

SharePoint and OneDrive integration with the Azure AD B2B one-time passcode feature is currently in preview. After preview, this feature will replace the ad-hoc external sharing experience used in OneDrive and SharePoint today for all tenants.

Advantages of Azure AD B2B include:
- Invited external users are each given an account in the directory and are subject to Azure AD access policies such as multi-factor authentication.
- Invitations to a SharePoint site use Azure AD B2B and no longer require users to have or create a Microsoft account.
- If you have configured Google federation in Azure AD, federated users can now access SharePoint and OneDrive resources that you have shared with them.
- SharePoint and OneDrive sharing is subject to the Azure AD organizational relationships settings, such as **Members can invite** and **Guests can invite**.


[SharePoint and OneDrive integration with Azure AD B2B (Preview)](sharepoint-azureb2b-integration-preview.md)

## See also

[External sharing overview](external-sharing-overview.md)

[Turn external sharing on or off for SharePoint Online](turn-external-sharing-on-or-off.md)

[Share SharePoint files or folders](https://support.office.com/article/1fe37332-0f9a-4719-970e-d2578da4941c)
