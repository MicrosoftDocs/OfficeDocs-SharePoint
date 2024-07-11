---
ms.date: 07/10/2024
title: "Restrict SharePoint site access with Microsoft 365 groups and Entra security groups"
ms.reviewer: nibandyo
manager: jtremper
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
- M365-SAM
- Highpri
- Tier2
- ContentEngagementFY24
search.appverid:
description: "Learn how to restrict access to SharePoint sites to members of a Microsoft 365 or Entra security group."
---

# Restrict SharePoint site access with Microsoft 365 groups and Entra security groups

[!INCLUDE[Advanced Management](includes/advanced-management.md)]

You can restrict access to SharePoint sites and content to users in a specific group by using a site access restriction policy. Users not in the specified group can't access the site or its content, even if they had prior permissions or a shared link. This policy can be used with Microsoft 365 group-connected, Teams-connected, and non-group connected sites.

Site access restriction policies are applied when a user attempts to open a site or access a file. Users with direct permissions to the file can still view files in search results. However, they can't access the files if they're not part of the specified group.

Restricting site access via group membership can minimize the risk of oversharing content. For insights into data sharing, see [Data access governance reports](data-access-governance-reports.md).

## Prerequisites

The site access restriction policy requires [Microsoft SharePoint Premium - SharePoint Advanced Management](advanced-management.md).

## Enable site-level access restriction for your organization

You must enable site-level access restriction for your organization before you can configure it for individual sites.

To enable site-level access restriction for your organization in SharePoint admin center:

1. Expand **Policies** and select **Access control**.
2. Select **Site-level access restriction**.
3. Select **Allow access restriction** and then select **Save**.

   :::image type="content" source="media/rac-spac/1-RAC-SPAC-dashboard-feb-2024.png" alt-text="screenshot of site access restriction in sharepoint admin center dashboard." lightbox="media/rac-spac/1-RAC-SPAC-dashboard-feb-2024.png":::

To enable site-level access restriction for your organization using PowerShell, run the following command:

```Powershell
Set-SPOTenant -EnableRestrictedAccessControl $true
```

It might take up to one hour for command to take effect

> [!NOTE]
> For Microsoft 365 Multi-Geo users, run this command separately for each desired geo-location.

## Restrict access to group-connected sites (Microsoft 365 Groups and Teams)

Site access restriction policy for group-connected sites restricts SharePoint site access to members of the Microsoft 365 group or team associated with the site.

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

You can restrict access to non-group connected sites by specifying [Entra security groups](/azure/active-directory/fundamentals/how-to-manage-groups) or Microsoft 365 groups that contain the people who should be allowed access to the site. You can configure up to 10 Entra security groups or Microsoft 365 groups. Once the policy is applied, users in the specified group who have site access permissions are granted access to the site and its content. You can use [dynamic security groups](/azure/active-directory/enterprise-users/groups-create-rule) if you want to base group membership on user properties.

To manage site access to a non-group connected site:

1. In SharePoint admin center, expand **Sites** and select **Active sites**.
1. Select the site you want to manage and the site details panel appears.
1. In **Settings** tab, select **Edit** in the **Restricted site access** section.
1. Select the **Restrict SharePoint site access to only users in specified groups** check box.
1. Add or remove your security groups or Microsoft 365 groups and select **Save**.

In order for site access restriction to be applied to the site, you must add at least one group to the site access restriction policy.

:::image type="content" source="media/rac-spac/non-group-connected-sites/restricted-access-control-non-group-connected-site-page.png" alt-text="screenshot showing site access restriction security groups being added to non-group connected sites." lightbox="media/rac-spac/non-group-connected-sites/restricted-access-control-non-group-connected-site-page.png":::

To manage site access restriction for non-group connected sites using PowerShell, use the following commands:

| Action  | PowerShell command |
|---------|---------|
|Enable site access restriction     |`Set-SPOSite -Identity <siteurl> -RestrictedAccessControl $true`|
|Add group |`Set-SPOSite -Identity <siteurl> -AddRestrictedAccessControlGroups <comma separated group GUIDS>`         |
|Edit group     |`Set-SPOSite -Identity <siteurl> -RestrictedAccessControlGroups <comma separated group GUIDS>`         |
|View group     |`Get-SPOSite -Identity <siteurl> Select RestrictedAccessControl, RestrictedAccessControlGroups`         |
|Remove group     |`Set-SPOSite -Identity <siteurl> -RemoveRestrictedAccessControlGroups <comma separated group GUIDS>`         |  
|Reset site access restriction  |`Set-SPOSite -Identity <siteurl> -ClearRestrictedAccessControl`         |

## Shared and private channel sites

Shared and private channel sites [are separate from the Microsoft 365 group-connected site that standard channels use](teams-connected-sites.md). Because shared and private channel sites aren't connected to the Microsoft 365 group, site access restriction policies applied to the team don't affect them. You must enable site access restriction for each shared or private channel site separately as non-group connected sites.

For shared channel sites, only internal users in the resource tenant are subject to site access restriction. External channel participants are excluded from site access restriction policy and only evaluated per the site's existing site permissions.

> [!IMPORTANT]
> Adding people to the security group or Microsoft 365 group won't give users access to the channel in Teams. It is recommended to add or remove the same users of the teams channel in Teams and the security group or Microsoft 365 group so users have access to both Teams and SharePoint.

## Configure learn more link for access denial error page

Configure your learn more link to inform users who were denied access to a SharePoint site due to the restricted site access control policy. With this customizable error link, you can provide more information and guidance to your users.

> [!NOTE]
> The learn more link is a tenant-level setting that applies to all sites that have restricted access control policy enabled.  

To configure the link, run the following command in SharePoint PowerShell:

```powershell
Set-SPOTenant -RestrictedAccessControlForSitesErrorHelpLink “<Learn more URL>” 
```

To fetch the value of the link, run the following command:

```powershell
Get-SPOTenant | select RestrictedAccessControlForSitesErrorHelpLink 
```

The configured learn more link is launched when the user selects the **Know more about your organization’s policies here** link.

![Screenshot that shows learn more link for restricted access control.](../SharePointOnline/media/rac-spac/2-rac-learn-more-link.png)

## Reporting

As an IT administrator, you can view the following reports to gain more insight on SharePoint and OneDrive sites protected with restricted site access policy:

- Sites protected by restricted site access policy (RACProtectedSites)
- Details of access denials due to restricted site access (ActionsBlockedByPolicy)

> [!NOTE]
> It can take a few hours to generate each report.

### Sites protected by restricted site access policy report (preview)

You can run the following commands in SharePoint PowerShell to generate, view, and download the report:

#### Generate report

To generate a new report, run the following command:

```powershell
Start-SPORestrictedAccessForSitesInsights -RACProtectedSites 
```

#### View report

To fetch and view the generated report, run the following command:

```powershell
Get-SPORestrictedAccessForSitesInsights -RACProtectedSites -ReportId <Report GUID>
```

The report shows the top 100 sites with the highest page views that are protected with the policy.

#### Download report

To download the generated report, run the following command:

```powershell
Get-SPORestrictedAccessForSitesInsights -RACProtectedSites -ReportId <Report GUID> -Action Download 
```

The downloaded report is located on the path where the command was run.

> [!IMPORTANT]
> You must run the command as an administrator in order to download the report.

### Percentage of sites protected with restricted site access report

You can also view the percentage of sites that are protected with restricted site access out of total number of sites, using the following command:

```powershell
Get-SPORestrictedAccessForSitesInsights -RACProtectedSites -ReportId <Report GUID> -InsightsSummary
```

### Access denials due to restricted site access report

#### Create report

To create a new report for fetching access denial details, run the following command in PowerShell:

```powershell
Start-SPORestrictedAccessForSitesInsights -ActionsBlockedByPolicy
```

#### Fetch report status

To fetch the status of the generated report, run the following command:

```powershell
Get-SPORestrictedAccessForSitesInsights -ActionsBlockedByPolicy
```

#### View all access denials in the last 28 days report

To get the list of all access denials in the last 28 days, run the following command:

```powershell
Get-SPORestrictedAccessForSitesInsights -ActionsBlockedByPolicy -ReportId <Report ID> -Content AllDenials
```

The PowerShell output contains most recent 100 access denials. To view the complete list, you can download the report.

#### View list of top users who were denied access

To get the list of top users who were denied access, run the following command:

```powershell
Get-SPORestrictedAccessForSitesInsights -ActionsBlockedByPolicy -ReportId <Report ID> -Content TopUsers
```

The PowerShell output contains the top 100 users who faced the highest access denials. To view the complete list, download the report.

#### View list of top sites that received maximum access denials

To get the list of top sites that received maximum access denials, run the following command:

```powershell
Get-SPORestrictedAccessForSitesInsights -ActionsBlockedByPolicy -ReportId <Report ID> -Content TopSites
```

The PowerShell output contains the top 100 sites that had the highest access denials. To view the complete list, download the report.

#### View distribution of access denials across different types of sites report

To view the distribution of access denials across different types of sites, run the following command:

```powershell
Get-SPORestrictedAccessForSitesInsights -ActionsBlockedByPolicy -ReportId <Report ID> -Content SiteDistribution
```

> [!IMPORTANT]
> You must run the command as an administrator to download the report.

> [!NOTE]
> The downloaded report will be located on the path from where command has been run.

## Auditing

[Audit events](/office/office-365-management-api/office-365-management-activity-api-schema) are available in the Purview compliance portal to help you monitor site access restriction activities. Audit events are logged for the following activities:

- Applying site access restriction for site
- Removing site access restriction for site
- Changing site access restriction groups for site

## Related articles

[Conditional access policy for SharePoint sites and OneDrive](authentication-context-example.md)

[Data Access Governance reports](data-access-governance-reports.md)
