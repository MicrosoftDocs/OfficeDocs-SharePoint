---
ms.date: 08/07/2023
title: Plan and deploy a file collaboration environment - SharePoint
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
recommendations: true
audience: Admin
f1.keywords: NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.localizationpriority: medium
ms.collection:  
- Strat_SP_admin
- M365-collaboration
- essentials-security
ms.custom:
- seo-marvel-apr2020
- admindeeplinkSPO
search.appverid: MET150
description: In this article, you'll learn about planning and deploying a secure and productive file collaboration environment in SharePoint in Microsoft 365.
---
# Plan and deploy a file collaboration environment - SharePoint

With Microsoft 365 services, you can create a secure and productive file collaboration environment for your users. SharePoint powers much of this, but the capabilities of file collaboration in Microsoft 365 reach beyond the traditional SharePoint site. Teams, OneDrive, and a variety of governance and security options all play a role in creating a rich environment where users can collaborate easily and where your organization's sensitive content remains secure.

In the sections below, we call out the options and decisions that you as an administrator should consider when setting up a collaboration environment:

- How SharePoint relates to other collaboration services in Microsoft 365, including OneDrive, Microsoft 365 Groups, and Teams.

- How you can create an intuitive and productive collaboration environment for your users.

- How you can protect your organization's data by managing access through permissions, data classifications, governance rules, and monitoring.

This is part of the broader Microsoft 365 collaboration story:

- [Secure collaboration with Microsoft 365](/microsoft-365/solutions/setup-secure-collaboration-with-teams)

- [Collaboration governance](/microsoft-365/solutions/collaboration-governance-overview)

- [Meetings, webinars, and live events](/microsoftteams/quick-start-meetings-live-events)

We recommend that you download the [Microsoft Teams and related productivity services in Microsoft 365 for IT architects](/microsoft-365/solutions/productivity-illustrations) poster and refer to it while you read this article. This poster provides detailed illustrations of how the collaboration services in Microsoft 365 relate to each other and interact.

## Creating a successful collaboration experience

The technical implementation options that you choose for file collaboration in Microsoft 365 should balance what can seem to be contradictory requirements:

- Protecting your intellectual property

- Enabling self-service

- Creating a smooth user experience

**Protecting your intellectual property**

There are several options discussed later in this article for protecting your intellectual property. These include limiting who files can be shared with, applying governance policies by using sensitivity labels, and managing the devices that users use to access content.

In considering which options to choose, we recommend a balanced approach:

A configuration that allows users to share content freely can lead to accidental sharing of confidential data. However, a user experience that is difficult to use or too restrictive can lead to users finding alternative collaboration options that circumvent your governance policies, ultimately leading to even greater risk.

By using a combination of features – depending on the sensitivity of your data – you can create a collaboration environment that's easy to use and provides the security and auditing controls that you need.

**Enabling self-service**

In Microsoft 365, we recommend allowing users to create Teams, Microsoft 365 Groups, and SharePoint sites as needed. You can use sensitivity labels to enforce permissions governance, take advantage of compliance features that protect your content, and use expiration and renewal policies to make sure unused sites don't accumulate.

By choosing options that favor user self-service, you can minimize the impact on your IT staff while creating an easier experience for your users.

**Creating a smooth user experience**

The key to creating a smooth user experience is to avoid creating barriers for your users that they don't understand or that they must escalate to your help desk. For example, turning external sharing off for a site might cause user confusion or frustration; whereas labeling the site and its contents as confidential and using data loss prevention policy tips and emails to educate your users in your governance policies, can lead to a much smoother experience for them.

## SharePoint, Microsoft 365 Groups, and Teams

In SharePoint in Microsoft 365, each SharePoint team site is part of a Microsoft 365 group. A Microsoft 365 group is a single permissions group that is associated with a variety of Microsoft 365 services, including a SharePoint site, an instance of Planner, a mailbox, a shared calendar, and others. When you add owners or members to the Microsoft 365 group, they are given access to the SharePoint site along with the other connected services.

While you can continue to manage SharePoint site permissions separately by using SharePoint groups, we recommend managing permissions for SharePoint by adding people to or removing them from the associated Microsoft 365 group. This provides easier administration as well as giving users access to a host of related services that they can use for better collaboration.

Microsoft Teams provides a hub for collaboration by bringing together all the Microsoft 365 group-related services, plus a variety of Teams-specific services, in a single user experience with persistent chat. Teams uses the associated Microsoft 365 group to manage its permissions. Within the Teams experience, users can directly access SharePoint along with the other services without having to switch applications. This provides a centralized collaboration space with a single place to manage permissions. Teams uses the SharePoint site that is connected to the Microsoft 365 group for files in standard channels and creates separate SharePoint sites for each private or shared channel. For collaboration scenarios in your organization, we highly recommend using Teams rather than using services such as SharePoint independently.

For details about how SharePoint and Teams interact, see [Overview of Teams and SharePoint integration](/sharepoint/teams-connected-sites) and [Manage settings and permissions when SharePoint and Teams are integrated](/sharepoint/manage-teams-sharepoint-experiences).

## Collaboration in client applications

Office applications such as Word, Excel, and PowerPoint provide a wide variety of collaboration features, including coauthoring and @mentions, and are also integrated with sensitivity labels and data loss prevention (discussed below).

We highly recommend deploying Microsoft 365 Apps for enterprise. Microsoft 365 Apps for enterprise provides an always up-to-date experience for your users, with the latest features and updates delivered on a schedule that you can control.

For details about deploying Microsoft 365 Apps for enterprise, see [Deployment guide for Microsoft 365 Apps](/deployoffice/deployment-guide-microsoft-365-apps).

## OneDrive libraries

While SharePoint provides shared libraries for shared files that teams can collaborate on, users also have an individual library in OneDrive where they can store files that they own.

When a user adds a file to OneDrive, that file is not shared with anyone else. OneDrive provides the same sharing capabilities as SharePoint, so users can share files in OneDrive as needed.

A user's individual library can be accessed from Teams, as well as from the OneDrive web interface and mobile application.

On devices running Windows or macOS, users can install the OneDrive sync app to sync files from both OneDrive and SharePoint to their local disk. This allows them to work on files offline and also provides the convenience of opening files in their native application (such as Word or Excel) without the need of going to the web interface.

The two main decisions to consider for using OneDrive in collaboration scenarios are:

- Do you want to [allow Microsoft 365 users to share files in OneDrive with people outside your organization](turn-external-sharing-on-or-off.md)?

- Do you want to [restrict file sync](plan-file-sync.md) in any way – such as only to managed devices?

These settings are available in the <a href="https://go.microsoft.com/fwlink/?linkid=2185219" target="_blank">SharePoint admin center</a>.

## Securing your data

A big part of a successful collaboration solution is making sure your organization's data remains secure. Microsoft 365 provides a variety of features to help you keep your data secure while enabling a seamless collaboration experience for your users.

To help protect your organization's information, you can:

- **Control sharing** – by configuring sharing settings for each site that are appropriate to the type of information in the site, you can create a collaboration space for users while securing your intellectual property.

- **Classify and protect information** – by classifying the types of information in your organization, you can create governance policies that provide higher levels of security to information that is confidential compared to information that is meant to be shared freely.

- **Manage devices** – with device management, you can control access to information based on device, location, and other parameters.

- **Monitor activity** – by monitoring the collaboration activity happening in Teams and SharePoint, you can gain insights into how your organization's information is being used. You can also set alerts to flag suspicious activity.

- **Protect against threats** – by using policies to detect malicious files in SharePoint, OneDrive, and Teams, you can help ensure the safety of your organization's data and network.

These are each discussed in more detail below. There are many options to choose from. Depending on the needs of your organization, you can choose the options that give you the best balance of security and usability. If you are in a highly regulated industry or work with highly confidential data, you may want to put more of these controls in place; whereas if your organization's information is not sensitive you may want to rely on basic sharing settings and malicious file alerts.

### Control sharing

The sharing settings that you configure for SharePoint and OneDrive determine who your users can collaborate with, both inside and outside your organization. Depending on your business needs and the sensitivity of your data, you can:

- Disallow sharing with people outside your organization.

- Require people outside your organization to authenticate.

- Restrict sharing to specified domains.

You can configure these settings for the entire organization, or for each site independently (except private or shared channel sites). For detailed information, see [Turn sharing on or off](turn-external-sharing-on-or-off.md) and [Turn sharing on or off for a site](change-external-sharing-site.md).

See [Limit accidental exposure to files when sharing with guests](/microsoft-365/solutions/share-limit-accidental-exposure) for additional guidance around sharing with people outside your organization.

When users share files and folders, a shareable link is created which has permissions to the item. There are three primary link types:

- *Anyone* - links that work for anyone and don't require sign-in
- *People in your organization* - links that work for users in your organization
- *Specific people* - links that work for the people specified when the link is created

For more information about these link types, see [How shareable links work in OneDrive and SharePoint in Microsoft 365](shareable-links-anyone-specific-people-organization.md).

**Unauthenticated access with *Anyone* links**

*Anyone* links are a great way to easily share files and folders with people outside your organization. However, if you're sharing sensitive information, this may not be the best option.

If you require people outside your organization to authenticate, *Anyone* links will not be available to users and you'll be able to audit guest activity on shared files and folders.

Though *Anyone* links do not require people outside your organization to authenticate, you can track the usage of *Anyone* links and revoke access if needed.

If you want to allow *Anyone* links, there are several options for a more secure sharing experience.

You can restrict *Anyone* links to read-only. You can also set an expiration time limit, after which the link will stop working.

Another option is to configure a different link type to be displayed to the user by default. This can help minimize the chances of inappropriate sharing. For example, if you want to allow *Anyone* links but are concerned that they only be used for specific purposes, you can [set the default link type](change-default-sharing-link.md) to *Specific people* links or *People in your organization* links instead of *Anyone* links. Users would then have to explicitly select *Anyone* links when they share a file or folder.

You can also use data loss prevention to restrict *Anyone* link access to files that contain sensitive information.

***People in your organization* links**

*People in your organization* links are a great way to share information within your organization. *People in your organization* links work for anyone in your organization, so users can share files and folders with people who aren't part of a team or members of a site. The link when redeemed, gives access to the particular file or folder and can be passed around inside the organization. This allows for easy collaboration with stakeholders from groups that may have separate teams or sites – such as design, marketing, and support groups.

Creating a *People in your organization* link will not make the associated file or folder appear in search results, be accessible via Copilot, or grant access to everyone within the organization. Simply creating this link does not provide organizational-wide access to the content. For individuals to access the file or folder, they must possess the link and it needs to be activated through redemption. A user can redeem the link by clicking on it, or, in some instances, the link may be automatically redeemed when sent to someone via email, chat, or other communication methods. The link does not work for guests or other people outside your organization.

***Specific people* links**

*Specific people* links are best for circumstances where users want to limit access to a file or folder. The link only works for the person specified and they must authenticate in order to use it. These links can be internal or external (if you've enabled guest sharing).

### Classify and protect information

Microsoft Purview Data Loss Prevention provides a way to classify your teams, groups, sites, and documents, and to create a series of conditions, actions, and exceptions to govern how they're used and shared.

By classifying your information and creating governance rules around them, you can create a collaboration environment where users can easily work with each other without accidentally or intentionally sharing sensitive information inappropriately.

With data loss prevention policies in place, you can be relatively liberal with your sharing settings for a given site and rely on data loss prevention to enforce your governance requirements. This provides a friendlier user experience and avoids unnecessary restrictions that users might try to work around.

For detailed information about data loss prevention, see [Learn about data loss prevention](/purview/dlp-learn-about-dlp).

**Sensitivity labels**

Sensitivity labels provide a way to classify teams, groups, sites, and documents with descriptive labels that can then be used to enforce a governance workflow.

Using sensitivity labels helps your users to share information safely and to maintain your governance policies without the need for users to become experts in those policies.

For example, you could configure a policy that requires Microsoft 365 groups classified as confidential to be private rather than public. In such a case, a user creating a group, team, or SharePoint site would only see the "private" option when they choose a classification of confidential. For information about using sensitivity labels with teams, groups, and sites, see [Use sensitivity labels to protect content in Microsoft Teams, Microsoft 365 groups, and SharePoint sites](/purview/sensitivity-labels-teams-groups-sites)

**Conditions and actions**

With data loss protection conditions and actions, you can enforce a governance workflow when a given condition is met.

Examples include:

- If customer information is detected in a document, then users cannot share that document with guests.

- If a document contains the name of a confidential project, then guests cannot open the document even if it has been shared with them.

For more information, see [Learn about data loss prevention](/purview/dlp-learn-about-dlp)

### Conditional access

Microsoft Entra Conditional Access provides additional controls to prevent users from accessing your organization's resources in risky situations, such as from untrusted location or from devices that aren't up to date.

Examples include:

- Block guests from signing in from risky locations

- Require multi-factor authentication for mobile devices

You can create access policies that are specifically for guests, allowing risk mitigation for people who most likely have unmanaged devices.

For detailed information, see [What is Conditional Access?](/azure/active-directory/conditional-access/overview).

## Monitoring with reports

A variety of reports are available in Microsoft 365 to help you monitor site usage, document sharing, governance compliance, and a host of other events.

For info about how to view reports on SharePoint site usage, see [Microsoft 365 Reports in the Admin Center - SharePoint site usage](/microsoft-365/admin/activity-reports/sharepoint-site-usage-ww).

For info about how to view data loss prevention reports, see [View the reports for data loss prevention](/purview/dlp-learn-about-dlp#dlp-activity-explorer-and-reports).

For info on reports that can help you monitor content sharing, see [Data access governance reports for SharePoint sites](data-access-governance-reports.md).

## Related topics

[Create a secure guest sharing environment](/microsoft-365/solutions/create-secure-guest-sharing-environment)

[Best practices for sharing files and folders with unauthenticated users](/microsoft-365/solutions/best-practices-anonymous-sharing)

[Microsoft Syntex - SharePoint Advanced Management overview](advanced-management.md)
