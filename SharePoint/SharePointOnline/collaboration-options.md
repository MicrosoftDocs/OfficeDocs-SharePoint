---
ms.date: 06/10/2022
title: Plan sharing and collaboration options in SharePoint and OneDrive
ms.reviewer: srice
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

# Plan sharing and collaboration options in SharePoint and OneDrive

SharePoint and OneDrive provide a platform for collaboration through file and folder storage and sharing.

As you plan your SharePoint and OneDrive rollout, these are the primary decision areas around collaboration:

- **Site creation** - do you want to allow your users to create SharePoint sites or do you want to manage this through IT or a business process?
- **External sharing** - do you want to allow users to share files, folders, or sites with people outside your organization?
- **File and folder sharing defaults** - what sharing defaults do you want to use to make sharing easy while you help protect sensitive information?

For details about collaboration governance in Microsoft 365, see [What is collaboration governance?](/microsoft-365/solutions/collaboration-governance-overview).

For an in-depth look at file collaboration in SharePoint, see [Intro to file collaboration in Microsoft 365, powered by SharePoint](/sharepoint/intro-to-file-collaboration) and [File collaboration in SharePoint with Microsoft 365](/sharepoint/deploy-file-collaboration).

Keep in mind that the settings you choose for collaboration in SharePoint can also affect Teams. For more information, see [Overview of Teams and SharePoint integration](teams-connected-sites.md).

## Site creation and lifecycle

By default, users can create new team sites and communication sites in SharePoint and shared libraries in OneDrive. We recommend keeping this setting and using [expiration policies](/microsoft-365/solutions/microsoft-365-groups-expiration-policy) to manage the number of unused sites.

If you don't want to allow users to create sites directly, you can disable user site creation. For details, see [Manage site creation in SharePoint](/sharepoint/manage-site-creation).

Even if you turn off sites creation for users in SharePoint, they can still create Microsoft 365 group-connected team sites by creating a Microsoft 365 group or any of its related services, such as a team in Microsoft Teams. If you don't want to allow users to create Microsoft 365 Groups or related services, including group-connected team sites, see [Manage who can create Microsoft 365 Groups](/microsoft-365/solutions/manage-creation-of-groups).

As part of your SharePoint rollout, we recommend that you create your own custom guidance for SharePoint site owners on how sites are set up and managed in your organization. See [Create guidelines for site usage](sites-usage-guidelines.md) for more information.

## External sharing

External sharing in SharePoint and OneDrive uses [Microsoft Entra B2B collaboration](/azure/active-directory/external-identities/what-is-b2b) to create guest accounts for people outside the organization. Guests can be given access to SharePoint sites or to individual files and folders in SharePoint and OneDrive.

External sharing is enabled by default in Microsoft 365, including SharePoint and OneDrive. We recommend leaving external sharing enabled. Microsoft 365 external sharing options can provide a more secure and governable sharing environment than sending attachments though email or using consumer sharing services.

Use the <a href="https://go.microsoft.com/fwlink/?linkid=2185222" target="_blank">Sharing page in the SharePoint admin center</a> to configure your sharing options. For details, see [Manage sharing settings](/sharepoint/turn-external-sharing-on-or-off).

For details about how to configure guest collaboration in SharePoint sites, see [Collaborate with guests in a site](/microsoft-365/solutions/collaborate-in-site).

### Organization level sharing settings

The organization level sharing settings for SharePoint and OneDrive provide a default setting for sites and OneDrive libraries. Individual sites can be locked down further, but cannot be made more permissive than, the organizational settings.

A key decision for your SharePoint and OneDrive rollout is who content can be shared with:

- **Anyone** - Users can share files and folders using links that don't require sign-in.
- **New and existing guests** - Guests are added to the directory when an item is shared and must sign in or provide a verification code to access the content.
- **Existing guests** - Users can only share with guests already in your organization's directory. (This setting is not recommended because guests can be added to the directory in various ways outside of SharePoint and OneDrive.)
- **Only people in your organization** - No external sharing is allowed.

These settings can be set separately for SharePoint and OneDrive, though the OneDrive setting cannot be more permissive than the SharePoint setting.

Important decisions:
- Do you want to allow external sharing? If not, choose the **Only people in your organization** option.
- Do you want to allow users to create sharing links that allow unauthenticated (anonymous) people to access files or folders? If so, choose **Anyone**.

### External sharing restrictions

You can restrict external sharing with these options:

- Restrict which domains users can share with.
- Limit external sharing to people in a specific security group.
- Expire guest access after a specified period.
- Require reauthentication after a specified period for users using a verification code.

If you want to restrict which domains users can share with, you can choose the **Limit external sharing by domain** setting. For details, see [Restrict sharing of SharePoint and OneDrive content by domain](/sharepoint/restricted-domains-sharing). Note that this setting only affects SharePoint and OneDrive. If you want to set this for all the services in Microsoft 365, you can configure the restriction in Microsoft Entra ID. See [Allow or block invitations to B2B users from specific organizations](/azure/active-directory/external-identities/allow-deny-list) for details.

If you don't want all of your users to be able to share externally, you can restrict external sharing to specific security groups. Choose the **Allow only users in specific security groups to share externally** option and choose the groups you want to allow.

If you want guest access to expire after a given period, use the **Guest access to a site or OneDrive will expire automatically after this many days** setting. The users who shared the content will have the option to extend the expiration by the period you specify before guests lose access. For more information see, [Manage guest expiration for a site](https://support.microsoft.com/office/25bee24f-42ad-4ee8-8402-4186eed74dea).

Guests with non-Microsoft email addresses, such as Gmail, are sent a verification code when they attempt to access shared content. You can require that these guests reauthenticate after a specified period. Use the **People who use a verification code must reauthenticate after this many days** setting to configure this.

## File and folder sharing

To create an easy sharing experience for your users while reducing the risk of oversharing, you can choose from these options for file and folder sharing links:

- Choose the default link type that users see when they share a file or folder.
- Choose if the default sharing link allows recipients to edit the files.
- Choose if *Anyone* links expire after a given period.
- Choose if *Anyone* links allow recipients to edit the files.

When users share a file or folder, they can choose from several types of sharing links that offer different levels of permissions. You can choose which link type is shown by default:
- *Specific people* links require the user to specify a list of people who will have access to the file or folder.
- *Only people in your organization* links provide access to the file or folder to anyone in your organization who has the link.
- *Anyone* links (if you've enabled them in your organization level sharing settings) provide anonymous access to anyone who has the link, including people outside your organization.

You can also choose the default permission level - view or edit - for sharing links.

These options can also be configured for individual sites. See [Change the sharing settings for a site](/sharepoint/change-external-sharing-site) for details.

If you've enabled *Anyone* links, you can choose if these links should expire after a given period and if they should allow edit access or just view access.

## Next steps

> [!div class="nextstepaction"]
> [Training and change management](training-change-management.md)

## Related topics

[Plan for SharePoint and OneDrive in Microsoft 365](plan-for-sharepoint-onedrive.md)

[Set up secure file sharing and collaboration with Microsoft Teams](/microsoft-365/solutions/setup-secure-collaboration-with-teams)

[Overview of external collaboration options in Microsoft 365](/microsoft-365/enterprise/external-guest-access)

[SharePoint and OneDrive file sync](/sharepoint/sharepoint-sync)

[Create a more secure guest sharing environment](/microsoft-365/solutions/create-secure-guest-sharing-environment)
