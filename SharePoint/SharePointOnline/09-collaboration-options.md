---
title: Sharing and collaboration options in SharePoint and OneDrive
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: serdars
recommendations: true
audience: Admin
f1.keywords: NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.localizationpriority: medium
ms.collection:  
ms.custom: intro-get-started
search.appverid: MET150
description: Plan the sharing and collaboration options that you want to implement as part of rolling out SharePoint and OneDrive.
---

# Sharing and collaboration options in SharePoint and OneDrive

SharePoint and OneDrive provide a platform for collaboration through file and folder sharing.

As you plan your SharePoint and OneDrive rollout, these are the primary decision areas around collaboration:

- **Site creation** - do you want to allow your users to create SharePoint sites or do you want to manage this through IT or a business process?
- **External sharing** - do you want to allow users to share files, folders, or sites with people outside your organization?
- **File and folder sharing defaults** - what sharing defaults do you want to use to make sharing easy but protect sensitive information?

For more details around collaboration governance in Microsoft 365, see [What is collaboration governance?](/microsoft-365/solutions/collaboration-governance-overview).

## Site creation

By default, users can create new team sites and communication sites and shared libraries in OneDrive. We recommend keeping this setting and using [expiration policies](/microsoft-365/solutions/microsoft-365-groups-expiration-policy) to manage the number of unused sites.

If you don't want to allow users to create sites directly, you can disable user site creation. For details, see [Manage site creation in SharePoint](/sharepoint/manage-site-creation).

Even if you turn off sites creation for users in SharePoint, they can still create Microsoft 365 group-connected team sites by creating a Microsoft 365 group or any of its related services, such as a team in Microsoft teams. If you don't want to allow users to create Microsoft 365 Groups or related services, including group-connected team sites, see [Manage who can create Microsoft 365 Groups](/microsoft-365/solutions/manage-creation-of-groups).

## External sharing

External sharing in SharePoint and OneDrive uses [Azure Active Directory B2B collaboration](/azure/active-directory/external-identities/what-is-b2b) to create guest accounts for people outside the organization. Guests can be given access to SharePoint sites or to individual files and folders in SharePoint and OneDrive.

External sharing is enabled by default in Microsoft 365, including SharePoint and OneDrive. We recommend leaving external sharing enabled. Microsoft 365 external sharing options can provide a more secure and governable sharing environment than sending attachments though email or using consumer sharing services.

### Organization level sharing settings

The organization level sharing settings for SharePoint and OneDrive provide a default setting for sites and OneDrive libraries. Individual sites can be locked down further, but cannot be made more permissive than the organizational settings.

A key decision for your SharePoint and OneDrive rollout is who content can be shared with:

- **Anyone** - Users can share files and folders using links that don't require sign-in.
- **New and existing guests** - Guests are added to the directory when an item is shared and must sign in or provide a verification code to access the content.
- **Existing guests** - Only guests already in your organization's directory. (This setting is not recommended because guests can be added to the directory in various ways outside of SharePoint and OneDrive.)
- **Only people in your organization** - No external sharing is allowed.

These settings can be set separately for SharePoint and OneDrive, though the OneDrive setting cannot be more permissive than the SharePoint setting.



OneDrive vs. SharePoint settings

Note that the OneDrive sharing settings are a subset of the SharePoint sharing settings. If you want to allow external sharing in OneDrive, it must be enabled for SharePoint. For more info, see [File collaboration in SharePoint with Microsoft 365](/sharepoint/deploy-file-collaboration).


- Specify settings for sharing links and control external sharing: [Manage sharing](manage-sharing.md)

- **Sharing** - Use the <a href="https://go.microsoft.com/fwlink/?linkid=2185222" target="_blank">Sharing page in the SharePoint admin center</a> to configure your sharing options based on the decisions you made earlier in this guide. To learn more, see [Manage sharing settings](/sharepoint/turn-external-sharing-on-or-off).


- **Do you want to allow external sharing?** If you enable external sharing for OneDrive, your users will be able to share files and folders with people outside your organization.

- **If you allow external sharing, do you want to allow unauthenticated users?** If you enable sharing with **Anyone**, users can create sharable links that don't require sign-in.

- **Do you want to restrict external sharing by domain?** You can restrict external sharing to specific domains or prevent sharing with specific domains.
limit sharing by domain
[Restrict sharing of SharePoint and OneDrive content by domain](/sharepoint/restricted-domains-sharing)

Limit external sharing by security group

[Manage sharing settings](/sharepoint/turn-external-sharing-on-or-off)

Guest access to a site or OneDrive will expire automatically after this many days

If your administrator has set an expiration time for guest access, each guest that you invite to the site or with whom you share individual files and folders will be given access for a certain number of days. For more information visit, Manage guest expiration for a site

People who use a verification code must reauthenticate after this many days

If people who use a verification code have selected to "stay signed in" in the browser, they must prove they can still access the account they used to redeem the sharing invitation.

Anyone link expiration

[Collaborate with guests in a site](/microsoft-365/solutions/collaborate-in-site)

[Create a more secure guest sharing environment](/microsoft-365/solutions/create-secure-guest-sharing-environment)

## File and folder sharing


- **What do you want the default sharing link to be?** Users can choose which type of link to send (Anyone, People in your organization, or Specific people), but you can choose the default option that is presented to users.

Default sharing link permissions








## Related topics

[Set up secure file sharing and collaboration with Microsoft Teams](/microsoft-365/solutions/setup-secure-collaboration-with-teams)

[Overview of external collaboration options in Microsoft 365](/microsoft-365/enterprise/external-guest-access)

[Intro to file collaboration in Microsoft 365, powered by SharePoint](/sharepoint/intro-to-file-collaboration)

[File collaboration in SharePoint with Microsoft 365](/sharepoint/deploy-file-collaboration)

[SharePoint and OneDrive file sync](/sharepoint/sharepoint-sync)