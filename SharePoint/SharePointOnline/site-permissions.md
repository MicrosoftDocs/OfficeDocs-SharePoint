---
ms.date: 11/26/2019
title: "Admin center site permissions reference"
ms.reviewer: srice
ms.author: mikeplum
author: MikePlumleyMSFT
manager: serdars
recommendations: true
audience: Admin
ROBOTS: NOINDEX
f1.keywords:
- CSH
ms.topic: article
ms.service: sharepoint-online
ms.localizationpriority: high
ms.custom: admindeeplinkSPO
layout: ContentPage
ms.collection:  
- Strat_OD_share
- M365-collaboration
search.appverid:
- SPO160
- MET150
description: "Learn about site permissions that you can configure in the SharePoint admin center."
---

# Admin center site permissions reference

On the **Membership** tab, you can manage permissions for the site and also for any associated Microsoft 365 group or Microsoft Teams team. These roles are specific to the selected site or group and don't give users access to the <a href="https://go.microsoft.com/fwlink/?linkid=2185219" target="_blank">SharePoint admin center</a>.

## Site admins

Site admins (formerly called site collection administrators) have the highest level of SharePoint permissions. They have the same Full Control permissions of a site owner, plus they can do more things, such as managing search, the recycle bin, and site collection features. They also have access to any items in the site, including in subsites, even if permissions inheritance has been broken.

If there's a Microsoft 365 group or team connected to the site, then group or team owners are automatically included as site admins and group or team members are automatically included as site members. Managing site permissions through group or team membership is recommended over giving people permissions directly to the site. This method allows for easier administration and consistent access for users across group and team resources.

### Microsoft 365 group owners

Microsoft 365 group owners can manage group membership, privacy, and classification, as well as the associated SharePoint site. If the Microsoft 365 group is associated with a team, then the group owners are also team owners.

### Additional admins

Additional admins are site admins only and can only manage the SharePoint site. They have no access to the associated Microsoft 365 group or team unless they have also been directly added to the group or team.

## Site owners

Site owners have full control of the SharePoint site. If the site has an associated Microsoft 365 group or team, then group or team owners are automatically included as site owners. However, people added directly to the site owners group don't have access to the Microsoft 365 group or team unless they are added there directly.

## Site members

Site members have edit permissions to the SharePoint site and can add and remove files, lists, and libraries. If the site has an associated Microsoft 365 group or team, then group or team members are automatically included as site members. However, people added directly to the site members group don't have access to the Microsoft 365 group or team unless they are added there directly.

## Site visitors

Site visitors have view-only permissions to the SharePoint site. This permission level is only used by SharePoint and isn't related to permissions in an associated Microsoft 365 group or team.

> [!NOTE]
> For information on how to manage Site owners, Site  members and Site visitors permission groups, see [Sharing and permissions in the SharePoint modern experience](modern-experience-sharing-permissions.md).

## Additional permissions

There are additional [permission levels](understanding-permission-levels.md) in SharePoint beyond those shown on this panel. Users may have access to the site or its contents through those roles. Users may also have access to files or folders in the site through sharing links.

## See also

[External sharing overview](external-sharing-overview.md)

[Overview of Microsoft 365 Groups for administrators](/office365/admin/create-groups/office-365-groups)

