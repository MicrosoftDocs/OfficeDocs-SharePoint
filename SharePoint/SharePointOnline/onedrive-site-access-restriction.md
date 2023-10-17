---
ms.date: 10/17/2023
title: Restrict access to a user's OneDrive content to people in a security group
ms.author: mactra
author: MachelleTranMSFT
manager: serdars
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: one-drive
ms.localizationpriority: medium
ms.collection: 
- Strat_OD_admin
- Highpri
- Tier1
- M365-sam
- M365-collaboration
search.appverid:
ms.assetid: 
ms.custom:
- admindeeplinkSPO
description: "Learn how to allow only users in specified security groups to access a user's OneDrive content."
---

# Restrict access to a user's OneDrive content to people in a security group

[!INCLUDE[Advanced Management](includes/advanced-management.md)]

You can restrict access to a user's OneDrive content by using a OneDrive access restriction policy and specifying [Microsoft Entra security groups](/azure/active-directory/fundamentals/how-to-manage-groups) that contain the people who should be able to access files in that OneDrive.

When the policy is applied, the people in the security group are not granted access to any files directly. The OneDrive owner must share the content as they normally would. The OneDrive access restriction policy prevents anyone who is not in the security group from accessing the OneDrive content even if it's shared with them.

## Prerequisites

The OneDrive access restriction policy requires [Microsoft Syntex - SharePoint Advanced Management](advanced-management.md).

## Enable site access restriction for your organization

You must enable site access restriction for your organization before you can configure it for a user's OneDrive.

To enable site access restriction for your organization in SharePoint admin center:

1. Expand **Policies** and select **Access control**.
1. Select **Site access restriction**.
1. Select **Allow access restriction** and then select **Save**.:::image type="content" source="media/rac-spac/1-RAC-SPAC-dashboard.png" alt-text="screenshot of site access restriction in sharepoint admin center dashboard." lightbox="media/rac-spac/1-RAC-SPAC-dashboard.png":::

To enable site access restriction for your organization using PowerShell, run the following command:

```Powershell
Set-SPOTenant -EnableRestrictedAccessControl $true
```

It might take up to one hour for command to take effect

> [!NOTE]
> For Microsoft 365 Multi-Geo users, run this command separately for each desired geo-location.

## Restrict site access to a user's OneDrive content

Each OneDrive can be assigned up to 10 Microsoft Entra security groups. Once a security group is added, only users in the groups have access to content in that OneDrive that has been shared with them. You can use [dynamic security groups](/azure/active-directory/enterprise-users/groups-create-rule) if you want to base group membership on user properties.

To manage access restriction for OneDrive, use the following commands:

| Action  | PowerShell command |
|---------|---------|
|Enable site access restriction     |`Set-SPOSite -Identity <siteurl> -RestrictedAccessControl $true`|
|Add security group |`Set-SPOSite -Identity <siteurl> -AddRestrictedAccessControlGroups <comma separated group GUIDS>`         |
|Edit security group     |`Set-SPOSite -Identity <siteurl> -RestrictedAccessControlGroups <comma separated group GUIDS>`         |
|View security group     |`Get-SPOSite -Identity <siteurl>, Select RestrictedAccessControl, RestrictedAccessControlGroups`         |
|Remove security group     |`Set-SPOSite -Identity <siteurl> -RemoveRestrictedAccessControlGroups <comma separated group GUIDS>`         |  
|Reset site access restriction  |`Set-SPOSite -Identity <siteurl> -ClearRestrictedAccessControl`         |

## Related topics

[Restrict access control for SharePoint sites](restricted-access-control.md)

[Data access governance insights for SharePoint sites](data-access-governance-reports.md)
