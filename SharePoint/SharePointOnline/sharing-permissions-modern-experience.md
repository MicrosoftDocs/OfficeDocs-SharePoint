---
title: Sharing and permissions in the SharePoint modern experience
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.audience: Admin
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

The SharePoint Online security model includes the ability to control granular access to most aspects of SharePoint Online from the site level down to the item level. Access to the different items of SharePoint can be granted to specific users as well as to groups of users. For example, you might have a marketing department that wants to create a new modern team site as the collaboration space for a new marketing campaign. This team site needs to be restricted to a limited group of employees while the campaign is being built. When the new campaign is created, the team may wish to communicate the new messaging via a communication site with a more open set of permissions.

To further the marketing collaboration space scenario, say the team site needs to include an outside vendor that will be providing input on the new marketing campaign and thus will need access to the collaboration space. As documents are being created, quite possibly a library or an individual document needs to be shared with an internal or external person that may need rights to only view a specific document, or possibly the person should have full authoring permissions to just one library.

Traditional SharePoint includes three primary groupings of permissions, that being permission granted to individual users, permissions granted to a group of users where the group membership is maintained by Active Directory, or permissions granted to a group of users where the group membership is maintained by SharePoint directly. Each of the traditional SharePoint site templates, including team sites and publishing sites, provides the same permission model.

With modern SharePoint experiences, team sites and communication sites may also have unique, granular permissions, although each site template provides different options for both permissions as well as sharing. Modern team sites in particular are connected to Office 365 Groups, providing a richer communication and collaboration approach, as well as providing a group email and connection to a team within Microsoft Teams, among other benefits. Permission and sharing management in both modern SharePoint experiences are also more streamlined and intuitive within the modern experience.

Key points to consider regarding permissions and sharing in modern SharePoint sites include:

-   Modern SharePoint permission grouping

-   Providing a user direct access to a site vs adding a user to a group

-   Sharing permissions across sites

-   Permission differentiation between Team sites and Communication sites

-   External sharing and sharing options

## User grouping options and best practices 

Traditional SharePoint provided two primary forms of granting permissions to collections of users. With SharePoint groups, SharePoint maintains a list of groups on a site by site basis, and within each group, a list of assigned users. By default, traditional team and publishing sites [includes a set of SharePoint groups](/sharepoint/default-sharepoint-groups) that includes the following common groups: owners, members, and visitors. Publishing sites include additional groups such as approvers, designers, and more. Each SharePoint group is assigned specific permissions to the site hosting the group and thus any user assigned to a particular group also inherits that group’s permissions.

The second form of user grouping within traditional SharePoint includes security, or Active Directory, based groups. With security groups, a group of users is stored within Active Directory without any specific access to SharePoint. The security group may then be granted targeted access to specific aspects of SharePoint, such as owner access to one site collection, and only read access to a library in another site collection.

A common use case for SharePoint groups include an ad hoc grouping of users for a team site that need common access such as editing permissions to a marketing campaign team site. Common use cases for security groups include a larger set of users that may need common access across many sites, such as a group of all employees within the marketing department, that need at least read access to all marketing sites within a group of marketing site collections.

### SharePoint Online grouping options

SharePoint Online continues to provide both SharePoint groups as well as security groups maintained by Azure Active Directory. Office 365 also provides a third grouping option for SharePoint, [Office 365 Groups](https://support.office.com/en-us/article/learn-about-office-365-groups-b565caa1-5c40-40ef-9915-60fdb2d97fa2?ui=en-US&rs=en-US&ad=US). Office 365 Groups are similar to security groups, although Office 365 Groups include many additional benefits. Office 365 groups are provided a group email address as well as additional tools such as a group calendar, notebook, Planner, and a SharePoint team site. Users assigned to an Office 365 Group may also be classified as either a group owner or a group member, in comparison to security groups where all group members have equal access under the group.

Office 365 Groups may be added in Office 365, Outlook, Azure Active Directory, as well as may be added via custom applications or by IT admins using PowerShell. When creating a new modern team site or a Microsoft Teams team, an Office 365 Group is also created. Office 365 Groups may be public or private, where public groups are groups that may be discovered by anyone within the tenant while private groups are invite only. Additionally, Office 365 Groups may include internal and external users.

SharePoint groups and security groups do not have associated group email addresses, nor do they include group calendars, notebooks, Planner, or a default SharePoint site as is the case with Office 365 Groups.

## When and why to add users to a type of group or directly to a Site 

A given user may be provided access to a SharePoint site by granting specific access to a given user account, or by adding the given user account to an Office 365 Group, a security group, or a SharePoint group. It is considered best practice to add users to one of the three available group types when a user requires access to a SharePoint site to increase general performance and data responsiveness.

### Office 365 Groups

As already stated, Office 365 Groups are special types of groups stored in Azure Active Directory that offer two types of user classifications, Owners and Members. All modern team sites are tied to an Office 365 Group, and by default, when an Office 365 Group is created, a corresponding modern team site is created at the same time. IT admins and developers may create custom applications or use PowerShell to create Office 365 Groups and link them to existing SharePoint sites instead of having the Office 365 Group creation process create a new team site. Further, classic SharePoint team sites may be [connected to an Office 365 Group](/sharepoint/dev/transform/modernize-connect-to-office365-group) through a process that will create a new Office 365 Group for the classic site and link them together.

Office 365 Groups are the recommended choice when a collection of people want to communicate and collaborate together, that being, more than just a collection of people that need common access level to a particular resource. Office 365 Groups do not make sense when simple security trimming is required, although Office 365 Groups do allow for a common group of members to have common access to assets across the tenant.

### Security groups

Security groups are similar to Office 365 Groups as security groups are stored within Azure Active Directory and do provide a method to groups users to provide common access to assets across the tenant. Security groups do not provide the additional communication and collaboration benefits found in Office 365 Groups such as a shared email address, a shared calendar, and more.

Security groups are a recommended solution when a collection of people need common access to multiple sites, libraries, or other SharePoint assets, yet do not need the collaboration components available to Office 365 Groups. Note that Security groups are configured by tenant administrators that have access to Azure Active Directory. For this reason, Office 365 Groups may be necessary for some scenarios when group creation must be handled by non-tenant admins as Office 365 tenants may be configured to allow Office 365 Group creation by a larger set of users.

### SharePoint groups

SharePoint groups are groupings of users tied to specific SharePoint sites. SharePoint groups are not shared across the site collection boundary although SharePoint groups are inherited by default by sub sites.

SharePoint groups are provided by default by all SharePoint sites including modern team sites and communication sites. SharePoint groups may include specific users and security groups, and may also include both internal and external users as well, depending on tenant and site level configuration. Since SharePoint groups are not shared across site collections, they cannot be used to provide unified access to groups of users across sites.

With modern team sites, the underlying Office 365 Group should be favored for providing access to a given site. Communication sites may utilize Office 365 Groups although the underlying grouping is handled by SharePoint groups.

## Sharing permissions across a group of sites – sites within a Hub 

SharePoint hub sites offer an important mechanism to provide cohesion with a SharePoint implementation strategy. [Learn more about hub sites](/sharepoint/dev/features/hub-site/hub-site-overview).

Associating a site to a hub site does not change or unify the permissions of either the hub site or the associated site. It is important that users who can associate a site to a hub site have permission to the hub site, while you might also want to consider that members of a site that is associate to a hub also have permission to the hub although this is not a requirement.

In a scenario where common permissions may want to be applied across all or a sub-section of sites associated with a hub site, an Office 365 Group or security group could be created and then added as a member of each joined site.

## Permission comparison between team sites and communication sites 

Modern SharePoint Team sites and Communication sites are built on the same foundation yet have important differences that should be considered.

Each Team site is associated with an Office 365 Group. Office 365 Groups allow for two types of users, Owners and Members. As such, there are two primary types of users that are given access to a team site, those that are owners and have full control of the site, and members, which are users that only have editing capabilities, but not general configuration permissions.

Team site permissions are driven by SharePoint groups and may be administered by the group owners. The advanced permission settings allow for more granular control of permissions but is not recommended for general team use cases as the permissions will not extend back into the Office 365 Group or its related services.

Communication sites look to “Share” a site, sharing a given site to individual users or security groups. When sharing, the particular user or group may be granted full control, edit, or read only access.

Communication sites are not tied to an Office 365 Group. Advanced permissions options are also available to communication sites via the Sharing or Site permissions panels. It is important to note that underlying sharing and general permissions of communication sites also driven by SharePoint groups. Communication sites include three default SharePoint groups, Owners, Members, and Visitors, just as provided by traditional SharePoint sites.

## Internal and external sharing within SharePoint Online 

Sharing a site or asset within a site such as a library or document is essentially the same a granting permission for a particular person, user, or group to the shared asset. When sharing within SharePoint, you are also provided the ability to email the user directly with the UI as well.

There are two primary forms for sharing within SharePoint, internal sharing and external sharing. Internal sharing includes sharing with users or security groups within your tenant. External sharing includes sharing with anyone else.

External sharing is controlled at two levels, both at the tenant wide level as well as at the site collection level. A common use case is allowing sharing at the tenant level so that some sites may be shared externally, while limiting external sharing with the HR or another internal only site. [Learn more about external sharing](/sharepoint/external-sharing-overview).

By default, external sharing is enabled at both the tenant level and site collection level, although anonymous sharing is not allowed by default. If external sharing is blocked at the tenant level then no external sharing will be allowed on any site.

When sharing a team site, you may invite users and security groups to be a member of the site. When shared via the site permissions interface on the site itself, be aware that inviting a new member will not join that member to the connected Office 365 Group. You can invite new members to the Office 365 Group, which will automatically provide that member the proper access to the team site.

## Configuration options for sharing within SharePoint Online

By default, internal sharing is available on all SharePoint sites including team sites and communication sites. By default, external sharing is also allowed.

The availability of external sharing is controlled at different levels within SharePoint Online. At the tenant level, external sharing may be enabled or disabled for all sites. When disabling sharing at the tenant admin level, all sites will not allow any sharing of content with external users.

When external sharing is enabled at the tenant level, this enables the ability for sites within the tenant to allow for external sharing on a site by site basis. By default, with external sharing enabled at the tenant level, each modern site will by default have external sharing enabled as well. [Learn how to configure external sharing in SharePoint](/sharepoint/external-sharing-overview).

Changing external sharing on a site by site basis requires a tenant administrator.

When sharing a document such as a Microsoft Word, Microsoft Excel, or Microsoft PowerPoint document, the shared asset may be opened within the browser for a rich viewing or authoring experience.

## Different types of sharing links

When sharing a SharePoint file or folder, different types of links may be generated and either automatically or manually sent to the end user(s).

**Anyone**

If anonymous sharing is enabled at both the tenant level and site collection level, the link may be generated that would allow anyone access to anyone who has the link. By default anonymous sharing is not enabled and requires a tenant administrator to configure.

**People in your organization**

You may quickly create a link to share document or folder with anyone in your organization. This will grant access to your site or document to everyone in your organization who has the link.

**People with existing access**

A SharePoint document or folder may be shared with a group or user that already has existing access to the shared item in question. The primary purpose of this type of sharing is to generate the direct link to the item in question. The link generated by this option is a direct link without any expiration date, nor with any additional security trimming. This means that a user that utilizes such a link will only have their already granted permissions to the item in question.

**Specific people**

When sharing a document or folder, if enabled, you may share with specific people that you specify. This allows for both internal and external sharing, as well as sharing with specific people and security groups. A secure link may be generated that will provide read only or authoring access to the given shared item to one or more selected external users. Note that the external users will be granted restricted access to your tenant and may be added as an external user to your Azure Active Directory. They will only have access to the items that are explicitly shared with them.

### Expiration Date and enabled editing

Links can provide specific access to the shared asset including the ability for both internal or external users the right to edit the shared asset.

Anyone links can be configured to expire after a certain date or to never expire.

**Principal author: Eric Overfield, MVP<br>Website: [ericoverfield.com](http://ericoverfield.com)<br>LinkedIn: [https://linkedin.com/in/ericoverfield](https://linkedin.com/in/ericoverfield)<br>Twitter: @ericoverfield<br>**

## See also

[External sharing overview](external-sharing-overview.md)

[Turn external sharing on or off for SharePoint Online](turn-external-sharing-on-or-off.md)

[Share SharePoint files or folders](https://support.office.com/article/1fe37332-0f9a-4719-970e-d2578da4941c)
