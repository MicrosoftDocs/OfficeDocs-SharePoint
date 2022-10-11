---
title: "Restricted Access Control"
ms.reviewer: 
manager: serdars
recommendations: 
ms.author: mactra
author: its-mactra
ms.date: 10/12/2022
audience: Admin
f1.keywords:
- NOCSH 
ms.topic: conceptual
ms.service: sharepoint-online
ms.localizationpriority: 
ms.collection:  
search.appverid:
ms.assetid: TBD
description: "Enable Restricted Access Control for SharePoint sites through Microsoft 365 Group Membership"
---
# Restricted Access Control for SharePoint sites

With the Restricted Access Control policy, you can restrict the access of a SharePoint site and its content only to the members of Microsoft 365 group connected to the site. Users who are not added in the Microsoft 365 group, even if they previously had site access permissions will lose access.

As a [SharePoint Administrator](sharepoint-admin-role.md), Restricted Access Control allows you to reduce the oversharing of SharePoint site content within your organization.

For example, your research department decides content from a SharePoint site should only be accessed by users within the research Microsoft 365 group. They also want to prevent users outside of the Microsoft 365 group from receiving links for the site or its content. By enabling Restricted Access Control to connect a SharePoint site to a Microsoft 365 group, users who are not in the research Microsoft 365 group won’t have access to the content.

[PowerShell](https://learn.microsoft.com/powershell/sharepoint/sharepoint-online/connect-sharepoint-online) is required to enable Restricted Access Control.

## Enable Restricted Access Control for your organization

To enable Restricted Access Control in SharePoint, run the following command:

```Powershell
Set-SPOTenant -EnableRestrictedAccessControl $true
```

After you've enabled Restricted Access Control for SharePoint in your organization, wait for approximately 1 hour before managing restricted site access for a specific Microsoft 365 group connected site.

> [!NOTE]
> If you have Microsoft 365 Multi-Geo, you must run this command for each of your geo-locations.

## Enable Restricted Access Control for SharePoint site

Enable Restricted Access Control on a Microsoft 365 group connected site or team-site by running the following command:

```Powershell
Set-SPOSite -Identity,> -RestrictedAccessControl $true
```

**For example:**

Set-SPOSite -Identity <https://contoso.sharepoint.com/sites/ResearchTeamSite> -RestrictedAccessControl $true

## View Restricted Access Control for site

To view Restricted Access Control configuration for a site, run the following command:

```Powershell
Get-SPOSite –Identity <siteurl> | Select RestrictedAccessControl
```

## Remove Restricted Access Control for site

To remove Restricted Access Control from a Microsoft 365 group connected site, run the following command:

```Powershell
Set-SPOSite –Identify <siteurl> -RestrictedAccessControl $false
```

**For example:**

Set-SPOSite -Identity <https://contoso.sharepoint.com/sites/ResearchTeamSite-RestrictedAccessControl> $false
