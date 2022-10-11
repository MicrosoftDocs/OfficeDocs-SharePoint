---
title: "Manage restricted access control for SharePoint site"
ms.reviewer: 
manager: serdars
recommendations: true 
ms.author: mactra
author: its-mactra
ms.date: 10/12/2022
audience: Admin
f1.keywords: 
- NOCSH 
ms.topic: article
ms.service: sharepoint-online
ms.localizationpriority: medium
ms.collection:
- M365-collaboration
- Strat_SP_admin
search.appverid:
ms.assetid: TBD
description: "Enable restricted access control for SharePoint sites through Microsoft 365 Group Membership"
---
# Manage restricted access control for SharePoint sites

With restricted access control (preview), you can manage the access of a SharePoint site and its content. As a [SharePoint administrator](sharepoint-admin-role.md), you can grant access to users of the Microsoft 365 Group associated with a SharePoint site. Users who are not added to the group membership won’t have access even if they previously had site access permissions to a file. Restricted access control policy also applies to Microsoft 365 group memberships associated with Microsoft Teams.

Restricting access to sites based on group membership lets you reduce the risk of oversharing within your organization and provides an additional layer of security to safeguard site content. By enabling restricted site access, you apply a policy that retroactively addresses the concern of overshared site content. Use and consult [data access governance reports](data-access-governance-reports.md) to learn how to govern access to SharePoint data.

For example, the research department has a Microsoft 365 group that contains all of their department members. They don’t want anyone outside of the department to have access to the research department site or its contents. As their SharePoint admin, you can restrict site access to only members of the Microsoft 365 group by enabling restricted access control in PowerShell.

[PowerShell](/powershell/sharepoint/sharepoint-online/introduction-sharepoint-online-management-shell) is required to enable restricted access control.

## Enable restricted access control for your organization

To enable restricted access control in SharePoint, run the following command:

```Powershell
Set-SPOTenant -EnableRestrictedAccessControl $true
```

Then, wait for approximately 1 hour before managing restricted access control for that site.

> [!NOTE]
> If you have Microsoft 365 Multi-Geo, you must run this command for each geo-location you want to use restricted access control.

## Enable restricted access control for your SharePoint site

You can enable restricted access control on a group-connected or Teams-connected site by running the following command:

```Powershell
Set-SPOSite -Identity <siteurl> -RestrictedAccessControl $true
```

**For example:**

`Set-SPOSite -Identity <https://contoso.sharepoint.com/sites/ResearchTeamSite> -RestrictedAccessControl $true`

## View restricted access control for site

To view the restricted access control configuration for a site, run the following command:

```Powershell
Get-SPOSite -Identity <siteurl> | Select RestrictedAccessControl
```

## Remove restricted access control for site

To remove restricted access control from a site, run the following command:

```Powershell
Set-SPOSite -Identity <siteurl> -RestrictedAccessControl $false
```

**For example:**

`Set-SPOSite -Identity <https://contoso.sharepoint.com/sites/ResearchTeamSite-RestrictedAccessControl> $false`

## Related topics

[Manage site access based on sensitivity label](authentication-context-example.md)

[Data Access Governance reports](data-access-governance-reports.md)
