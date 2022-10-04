---
title: "Restricted access control"
ms.reviewer: 
manager: serdars
recommendations: 
ms.author: mactra
author: its-mactra
ms.date: 10/10/2022
audience: Admin
f1.keywords:
- NOCSH 
ms.topic: conceptual
ms.service: sharepoint-online
ms.localizationpriority: 
ms.collection:  
search.appverid:
ms.assetid: TBD
description: "Enable restricted access control for SharePoint sites through Microsoft 365 Group Membership"
---
# Restricted access control for SharePoint sites

![green check mark](media/yes.png) **Requires SharePoint Advanced Management**

Manage SharePoint site access and sharing privileges with restricted access control.

As a [SharePoint administrator](sharepoint-admin-role.md), you can grant access to users of the Microsoft 365 Group associated with the SharePoint site. Users who are not added to the group membership won’t have access even if they previously had site access permissions to a file. Restricted access control policy also applies to Microsoft 365 group memberships associated with Microsoft Teams.

Restricting access to sites based on group membership lets you reduce the risk of oversharing within your organization and provides an additional layer of security to safeguard confidential site content.

**For example:**

The research department in your organization realizes users from another department accessed and created share links to the research department's SharePoint team site. The research department now wants only current members of their department to have access to the site so none of their data is leaked to others. As their SharePoint admin, you can audit the Microsoft 365 group membership associated with the research department before removing users who’ve left the research department, and adding new users who’ve recently joined the research department. Once you enable restricted access control in PowerShell, users outside of the research department’s group membership are unable to access the site.

[PowerShell](https://learn.microsoft.com/powershell/sharepoint/sharepoint-online/connect-sharepoint-online) is required to enable restricted access control.

## Enable restricted access control for your organization

To enable restricted access control in SharePoint, run the following command:

```Powershell
Set-SPOTenant -EnableRestrictedAccessControl $true
```

Then, wait for approximately 1 hour before managing restricted access control for that site.

> [!NOTE]
> If you have Microsoft 365 Multi-Geo, you must run this command for each geo-location you want to use restricted access control.

## Enable restricted access control for SharePoint site

You can enable restricted access control on a Microsoft 365 group-connected site or Teams-connected site by running the following command:

```Powershell
Set-SPOSite -Identity <siteurl> -RestrictedAccessControl $true
```

**For example:**

`Set-SPOSite -Identity <https://contoso.sharepoint.com/sites/ResearchTeamSite> -RestrictedAccessControl $true`

## View restricted access control for site

To view restricted access control configuration for a site, run the following command:

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
