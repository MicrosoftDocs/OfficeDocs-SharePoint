---
ms.date: 10/11/2023
title: "Restrict SharePoint site access to members of a group"
ms.reviewer: nibandyo
manager: serdars
recommendations: true 
ms.author: mactra
author: MachelleTranMSFT
audience: Admin
f1.keywords: 
- NOCSH 
ms.topic: article
ms.service: sharepoint-online
ms.localizationpriority: medium
ms.custom:
  - has-azure-ad-ps-ref
ms.collection: 
- M365-collaboration
- Highpri
- Tier1
search.appverid:
description: "Learn how to restrict access to SharePoint sites to members of a group."
---
# Restrict SharePoint site access to members of a group

[!INCLUDE[Advanced Management](includes/advanced-management.md)]

You can restrict access to SharePoint sites to users in a specific group by using a site access restriction policy. Users not in the specified group can't access the site or its content, even if they had prior permissions or a shared link. This policy can be used with Microsoft 365 group-connected, Teams-connected, and non-group connected sites.

Site access restriction policies are applied when a user attempts to open a site or access a file. Users can still see files in search results if they have direct permissions to the file, but they won't be able to access the file if they're not part of the specified group.

Restricting site access via group membership can minimize the risk of oversharing content. For insights into data sharing, see [Data access governance reports](data-access-governance-reports.md).

## Prerequisites

The site access restriction policy requires [Microsoft Syntex - SharePoint Advanced Management](advanced-management.md).

## Enable site access restriction for your organization

You must enable site access restriction for your organization before you can configure it for individual sites.

To enable site access restriction for your organization in SharePoint admin center:

1. Expand **Policies** and select **Access control**.
1. Select **Site access restriction**.
1. Select **Allow access restriction** and then select **Save**.:::image type="content" source="media/rac-spac/1-RAC-SPAC-dashboard.png" alt-text="screenshot of site access restriction in sharepoint admin center dashboard." lightbox="media/rac-spac/1-RAC-SPAC-dashboard.png":::

To enable site access restriction for your organization using PowerShell, run the following command:

```Powershell
Set-SPOTenant -EnableRestrictedAccessControl $true
```

It may take up to one hour for command to take effect

> [!NOTE]
> For Microsoft 365 Multi-Geo users, run this command separately for each desired geo-location.

## Restrict access to group-connected sites (Microsoft 365 Groups and Teams)

Site access restriction policy for group-connected sites restricts SharePoint site access to members of the Microsoft 365 group or team associated with the site. When the policy is active, access to the site or its content can't be granted directly through SharePoint or sharing links.

To manage site access restriction for a group-connected site in SharePoint admin center

1. In SharePoint admin center, expand **Sites** and select **Active sites**.
1. Select the site you want to manage and the site details panel appears.
1. In the **Settings** tab, select **Edit** in the **Restricted site access** section.
1. Select the **Restrict access to this site** box and select **Save**.

To enable site access restriction for a group-connected site, run the following command:

```PowerShell
Set-SPOSite -Identity <siteurl> -RestrictedAccessControl $true
```

To view site access restriction for a group-connected site, run the following command:

```PowerShell
Get-SPOSite -Identity <siteurl> | Select RestrictedAccessControl
```

To disable site access restriction for a group-connected site, run the following command:

```PowerShell
Set-SPOSite -Identity <siteurl> -RestrictedAccessControl $false
```

## Restrict site access to non-group connected sites

You can restrict access to non-group connected sites by specifying [Microsoft Entra security groups](/azure/active-directory/fundamentals/how-to-manage-groups) that contain the people who should have access. Each non-group connected site can be assigned up to 10 Microsoft Entra security groups. Once a security group is added, only users in the groups have access to the site. You can use [dynamic security groups](/azure/active-directory/enterprise-users/groups-create-rule) if you want to base group membership on user properties.

When you add a security group to a site access restriction policy, the security group is also added to the site members group automatically. If you remove a security group from the policy, it isn't removed from the site members group. Members of the security group won't have access to the site because the group is no longer specified in the policy. However, if you turn the policy off entirely (uncheck the **Restrict SharePoint site access to only users in specified security groups** check box), members of any security groups that you had specified in the policy will have access to the site. Be sure to review the site members group for appropriate permissions if you turn off a site access restriction policy.

To manage site access to a non-group connected site:

1. In SharePoint admin center, expand **Sites** and select **Active sites**.
1. Select the site you want to manage and the site details panel appears.
1. In **Settings** tab, select **Edit** in the **Restricted site access** section.
1. Select the **Restrict SharePoint site access to only users in specified security groups** check box.
1. Add or remove your security groups and select **Save**.

In order for site access restriction to work on a non-group connected site, you must add at least one security group.

:::image type="content" source="media/rac-spac/non-group-connected-sites/4-RAC-SPAC-non-group-connected-sites-enabled-added-security-groups.png" alt-text="screenshot showing site access restriction security groups being added to non-group connected sites." lightbox="media/rac-spac/non-group-connected-sites/3-RAC-SPAC-Teams-non-group-connected-sites-enabled.png":::

To manage site access restriction for non-group connected sites using PowerShell, use the following commands:

| Action  | PowerShell command |
|---------|---------|
|Enable site access restriction     |`Set-SPOSite -Identity <siteurl> -RestrictedAccessControl $true`|
|Add security group |`Set-SPOSite -Identity <siteurl> -AddRestrictedAccessControlGroups <comma separated group GUIDS>`         |
|Edit security group     |`Set-SPOSite -Identity <siteurl> -RestrictedAccessControlGroups <comma separated group GUIDS>`         |
|View security group     |`Get-SPOSite -Identity <siteurl>, Select RestrictedAccessControl, RestrictedAccessControlGroups`         |
|Remove security group     |`Set-SPOSite -Identity <siteurl> -RemoveRestrictedAccessControlGroups <comma separated group GUIDS>`         |  
|Reset site access restriction  |`Set-SPOSite -Identity <siteurl> -ClearRestrictedAccessControl`         |

## Shared and private channel sites

Shared and private channel sites [are separate from top-level sites and are not connected to any Microsoft 365 groups](teams-connected-sites.md). When you enable site access restriction for a team containing private and/or shared channel sites, only the parent site is affected. You must enable site access restriction for shared or private channel sites separately from the group-connected sites.

For shared channel sites, only internal users in the resource tenant are subject to site access restriction. External users are excluded from site access restriction policy and only evaluated per the site's existing site permissions.

> [!IMPORTANT]
> Be sure to add or remove the same users to the teams channel in Microsoft Teams and the security group so users have access to both Teams and SharePoint.

## Auditing

[Audit events](/office/office-365-management-api/office-365-management-activity-api-schema) are available in the Microsoft Purview compliance portal to help you monitor site access restriction activities. Audit events are logged for the following activities:

- Applying site access restriction for site
- Removing site access restriction for site
- Changing site access restriction groups for site

## Related articles

[Conditional access policy for SharePoint sites and OneDrive](authentication-context-example.md)

[Data Access Governance reports](data-access-governance-reports.md)
