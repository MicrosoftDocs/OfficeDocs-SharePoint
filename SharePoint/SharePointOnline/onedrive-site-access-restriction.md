---
ms.date: 05/20/2024
title: Restrict access to a user's OneDrive content to people in a group
ms.reviewer: nibandyo
ms.author: mactra
author: MachelleTranMSFT
manager: jtremper
audience: Admin
f1.keywords:
- NOCSH
ms.topic: how-to
ms.service: one-drive
ms.localizationpriority: medium
ms.collection: 
- Strat_OD_admin
- Highpri
- Tier2
- M365-sam
- M365-collaboration
- essentials-compliance
- essentials-security
search.appverid:
ms.assetid: 
ms.custom:
- admindeeplinkSPO
description: "Learn how to allow only users in specified security groups to access a user's OneDrive content."
---

# Restrict access to a user's OneDrive content to people in a group

[!INCLUDE[Advanced Management](includes/advanced-management.md)]

You can restrict access to an individual user's OneDrive content to users in a security group by using a OneDrive access restriction policy. Users not in the specified group can't access the content, even if they had prior permissions or shared link.

The policy is applied using [Microsoft Entra security groups](/azure/active-directory/fundamentals/how-to-manage-groups) that contain the people who should be able to access files in that OneDrive.

When the policy is applied, the people in the security group aren't granted permissions to any files directly. The OneDrive owner must share the content as they normally would. The OneDrive access restriction policy prevents anyone who isn't in the security group from accessing the OneDrive content even if it's shared with them.

Access restriction policies are applied when a user attempts to access a file. Users can still see files in search results if they have direct permissions to the file, but they won't be able to access the file if they're not part of the specified security group.

You can also restrict access to the OneDrive service itself to people in a security group. For more information, see [Restrict OneDrive access by security group](limit-access.md).

## Requirements

The OneDrive access restriction policy requires [Microsoft SharePoint Premium - SharePoint Advanced Management](advanced-management.md).

## Enable site access restriction for your organization

You must enable site access restriction for your organization before you can configure it for a user's OneDrive.

To enable site access restriction for your organization in SharePoint admin center:

1. Expand **Policies** and select **Access control**.
1. Select **Site access restriction**.
1. Select **Allow access restriction** and then select **Save**.

   :::image type="content" source="media/rac-spac/1-rac-spac-dashboard-feb-2024.png" alt-text="screenshot of site access restriction in sharepoint admin center dashboard." lightbox="media/rac-spac/1-rac-spac-dashboard-feb-2024.png":::

To enable site access restriction for your organization using PowerShell, run the following command:

```Powershell
Set-SPOTenant -EnableRestrictedAccessControl $true
```

It might take up to one hour for command to take effect.

> [!NOTE]
> For Microsoft 365 Multi-Geo users, run this command separately for each desired geo-location.

## Restrict access to a user's OneDrive content

Each OneDrive can be assigned up to 10 Microsoft Entra security groups. Once a security group is added, only users in the groups have access to content in that OneDrive that has been shared with them. You can use [dynamic security groups](/azure/active-directory/enterprise-users/groups-create-rule) if you want to base group membership on user properties.

> [!IMPORTANT]
> The owner of the OneDrive must be included in one of the security groups that you specify or they will lose access to their OneDrive and its contents.

To manage access restriction for OneDrive, use the following commands:

| Action  | PowerShell command |
|---------|---------|
|Enable access restriction for a given OneDrive. (Run this command before adding security groups.) |`Set-SPOSite -Identity <siteurl> -RestrictedAccessControl $true`|
|Add security group |`Set-SPOSite -Identity <siteurl> -AddRestrictedAccessControlGroups <comma separated group GUIDS>`         |
|Edit security group     |`Set-SPOSite -Identity <siteurl> -RestrictedAccessControlGroups <comma separated group GUIDS>`         |
|View security group     |`Get-SPOSite -Identity <siteurl> Select RestrictedAccessControl, RestrictedAccessControlGroups`         |
|Remove security group     |`Set-SPOSite -Identity <siteurl> -RemoveRestrictedAccessControlGroups <comma separated group GUIDS>`         |  
|Reset site access restriction  |`Set-SPOSite -Identity <siteurl> -ClearRestrictedAccessControl`         |

## Auditing

Audit events are available in the Microsoft Purview compliance portal to help you monitor site access restriction activities. Audit events are logged for the following activities:

- Applying site access restriction for site
- Removing site access restriction for site
- Changing site access restriction groups for site

## Related articles

[Restrict SharePoint site access to members of a group](restricted-access-control.md)

[Data access governance insights for SharePoint sites](data-access-governance-reports.md)
