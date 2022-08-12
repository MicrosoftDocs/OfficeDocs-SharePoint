---
title: Plan for SharePoint and OneDrive in Microsoft 365
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
description: 
---

# Plan for SharePoint and OneDrive in Microsoft 365

This article and the other articles in this section include the core planning considerations for rolling out OneDrive and SharePoint in a medium to large organization.

SharePoint is deeply integrated with Microsoft Teams. As part of your SharePoint and OneDrive rollout, we recommend that you review [Microsoft Teams deployment overview](/microsoftteams/deploy-overview).

As you plan your rollout, in addition to the technical planning considerations provided here, consider theses questions:

- What are your high-level goals for rolling out OneDrive and SharePoint?
- What are the file storage and collaboration needs of your organization?
- How do you want to transition from your current tools to OneDrive and SharePoint?
- How important is migration of content as part of your rollout?
- Should your administrators specialize in a particular area of OneDrive or SharePoint or should they work from a shared queue of tasks?

After you review this article, see these article for additional planning information:

- [Identify business requirements for SharePoint and OneDrive](business-requirements.md)

- [Hybrid OneDrive and SharePoint in Microsoft 365](hybrid.md)

- [Migration planning for SharePoint and OneDrive rollout](plan-rollout-migration.md)

- [Create a compliant SharePoint and OneDrive environment](compliant-environment.md)

- [Plan sharing and collaboration options in SharePoint and OneDrive](collaboration-options.md)

- [Plan file sync for SharePoint and OneDrive in Microsoft 365](plan-file-sync.md)

- [Training and change management for rolling out SharePoint and OneDrive](training-change-management.md)

- [Migrate content as part of your SharePoint and OneDrive rollout](rollout-migration.md)

- [Roll out SharePoint and OneDrive](roll-out-sharepoint-onedrive.md)

## Migrating with FastTrack

FastTrack is a Microsoft benefit that is included in your subscription. FastTrack provides you with a set of best practices, tools, resources, and experts committed to helping you deploy Microsoft 365. Guidance around SharePoint and OneDrive onboarding, migration, and adoption are included in the benefit offering. This guidance includes: help to discover what's possible, creating a plan for success, and onboarding new users, providing guidance on migrating content from file share, Box, or Google Drive source environments, and introducing capabilities at a flexible pace. 

FastTrack guidance provides enablement of both SharePoint and OneDrive as well as getting the source environment ready for your transition. For more details, see [FastTrack Center Benefit Overview](/fasttrack/data-migration/). Interested in getting started? Visit the [FastTrack web site](https://www.microsoft.com/fasttrack/), review resources, and submit a Request for Assistance.

## Site lifecycle

You can let your users create and administer their own SharePoint sites, determine what kind of sites they can create, and specify the location of the sites. By default, users can create communication sites and Microsoft 365 group-connected team sites.

You can prevent your users from creating their own sites if you want to manage this process through IT. See [Manage site creation in SharePoint](manage-site-creation.md) for more information.

Disabling site creation for users does not remove their ability to create Microsoft 365 groups or resources, such as Microsoft Teams, which rely on a group. When a Microsoft 365 group is created, a SharePoint site is also created. To restrict creation of Microsoft 365 groups and the resources that rely on groups see [Manage who can create Microsoft 365 Groups](/microsoft-365/solutions/manage-creation-of-groups).

We recommend that you allow users to create their own groups and sites and use [Microsoft 365 group expiration policies](/microsoft-365/solutions/microsoft-365-groups-expiration-policy) to help manage the deletion of sites and groups that aren't in use.

As part of your SharePoint rollout, we recommend that you create your own custom guidance for SharePoint site owners on how sites are set up and managed in your organization. See [Create guidelines for site usage](sites-usage-guidelines.md) for more information.

## Hubs and architecture

SharePoint uses hub sites to help you organize sites in a hierarchy that matches your organization or business processes. While it's not critical to plan your hub site layout as part of your SharePoint rollout, we recommend reviewing [Planning your SharePoint hub sites](planning-hub-sites.md) to understand how hub sites work.

We recommend including planning for hub sites as part of your process for rolling out an [intelligent intranet](/sharepoint/intelligent-internet-overview).

## Pre-provision OneDrive libraries

By default, the first time that a user browses to their OneDrive it's automatically created (provisioned) for them. In some cases, such as the following, you might want your users' OneDrive locations to be ready beforehand, or pre-provisioned:

- Your organization has a custom process for adding new employees, and you want to create a OneDrive when you add a new employee.
- Your organization plans to migrate from SharePoint Server on-premises to Microsoft 365.
- Your organization plans to migrate from another online storage service.

If you're planning to migrate content to OneDrive as part of your SharePoint and OneDrive rollout, you may need to pre-provision OneDrive for the users in your pilot or rollout program. See [Pre-provision OneDrive for users in your organization](pre-provision-accounts.md) for more information.

## Network utilization

Various factors can impact the amount of network bandwidth used by OneDrive. For the best experience, we recommend that you assess this impact before doing a full OneDrive deployment across your organization. The article [Network utilization planning for the OneDrive sync app](network-utilization-planning.md) includes the recommended process for determining your network bandwidth needs for OneDrive. Be sure to include this as part of your deployment plan

[Networking roadmap for Microsoft 365](/microsoft-365/enterprise/networking-roadmap-microsoft-365)

[Office 365 URLs and IP address ranges](/enterprise/urls-and-ip-address-ranges)

[Use the Office 365 Content Delivery Network (CDN) with SharePoint Online](/microsoft-365/enterprise/use-microsoft-365-cdn-with-spo)

## Change management

Rolling out SharePoint and OneDrive means new processes and procedures for the users in your organization. An important part of the rollout is making sure users are trained in the new ways of doing tasks as well as entirely new tasks that SharePoint and OneDrive enable. See [Training and change management for rolling out SharePoint and OneDrive](training-change-management.md) for considerations around change management and resources that you can share with your users on how to work with SharePoint and OneDrive.

## Customizing SharePoint

SharePoint offers many customization options, including:
- Branding SharePoint sites
- Navigation between sites
- Custom page layouts
- Custom apps
- Workflows

We recommend that you review [Customizing SharePoint](/sharepoint/extend-and-develop) to determine if you want to include any of these customizations as part of your SharePoint rollout.

## Next steps

   > [!div class="nextstepaction"]
   > [Identify business requirements](04-business-requirements.md)
