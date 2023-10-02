---
ms.date: 09/27/2023
title: "Restrict SharePoint site access"
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
description: "Learn how to enable restricted access control for SharePoint sites."
---
# Restrict SharePoint site access

[!INCLUDE[Advanced Management](includes/advanced-management.md)]

Restricted access control enables SharePoint site and content management via [SharePoint admin center](https://learn.microsoft.com/sharepoint/restricted-access-control) or[SharePoint Online PowerShell](../SharePointServer/sharepoint-powershell.md).

As a [SharePoint administrator](sharepoint-admin-role.md), you can apply site access restriction to your organization and then manage the feature for individual sites by specifying the group containing users who will have access. Users not in the group can't access the site or its content, even if they had prior permissions. This policy applies to Microsoft 365 group-connected, Teams-connected, and non-group connected sites.

> [!NOTE]
> Once you enforce a restricted access control policy, shared links to the site or content will no longer work. Users will be redirected to a webpage informing them they lack sufficient site access permissions to view the site and content. Users will need to be added to the group to access the site or content.

Restricted access control policy is enforced only when the user is opening the SharePoint site or opening the content in the SharePoint site. This behavior is like any other conditional access policies configured for a site.

Unified Search connected experiences do not enforce restricted access control policy. Users can see search results if they have existing access permissions to the content or the site. When the user selects a search result item to open the site content, they're denied access if they aren't part of the policy.

Restricting site access via group membership can minimize the risk of oversharing content. For insights into data sharing, see [Data access governance reports](data-access-governance-reports.md). This extra security layer from restricted access control safeguards content during site access and opening.

## Requirements

To access and use this feature, your organization must do the following:

- Subscribe to [Microsoft Syntex - SharePoint Advanced Management](advanced-management.md).
- Download the latest [SharePoint PowerShell module](https://www.microsoft.com/download/details.aspx?id=35588).

## Enable restricted access control for your organization

There are two ways to enable restricted access control for your organization using either SharePoint admin center or PowerShell.

To enable restricted access control for your organization in SharePoint admin center:

  1. Expand **Policies** and select **Access control**.
  2. Select **Site access restriction**.
  3. Select **Allow access restriction** and then select **Save**.:::image type="content" source="media/rac-spac/1-RAC-SPAC-dashboard.png" alt-text="screenshot of restricted access control in sharepoint admin center dashboard." lightbox="media/rac-spac/1-RAC-SPAC-dashboard.png":::

To enable restricted access control for your organization using PowerShell:

1. Run the following command:

      ```Powershell
    Set-SPOTenant -EnableRestrictedAccessControl $true
    ```

2. Wait for approximately 1 hour.

> [!NOTE]
> For Microsoft 365 Multi-Geo users, run this command separately for each desired geo-location to implement restricted access control.

## Restrict access to group-connected sites (Microsoft 365 groups and Teams)

Once restricted access control is enabled for your organization, you can manage access for your group-connected sites using either SharePoint admin center or PowerShell.

To enable, view, or disable restricted access control for a group-connected site in SharePoint admin center:

1. In SharePoint admin center, expand **Sites** and select **Active sites**.
2. Select the site you want to manage and the site details panel appears.
3. In the **Settings** tab, select **Edit** in the **Restricted site access** section.
4. Select the **Restrict access to this site** box.
5. Select **Save**.

To enable restricted access control for a group-connected site in PowerShell, run the following command:

```PowerShell
Set-SPOSite -Identity <siteurl> -RestrictedAccessControl $true
```

To view restricted access control for a group-connected site in PowerShell, run the following command:

```PowerShell
Get-SPOSite -Identity <siteurl> | Select RestrictedAccessControl
```

To disable restricted access control for a group-connected site in PowerShell, run the following command:

```PowerShell
Set-SPOSite -Identity <siteurl> -RestrictedAccessControl $false
```

## Restrict site access to non-group connected sites

You can restrict access to non-group connected sites by specifying [Azure AD security groups](/azure/active-directory/fundamentals/how-to-manage-groups) in the SharePoint admin center or PowerShell. Each non-group connected site may be assigned up to 10 security groups. Once a security group is added, all users in the group will have access to the site.

> [!NOTE]
> Dynamic membership of security groups is also supported for restricted access control policy.

To enable, view, or disable site access to a non-group connected site:

1. In SharePoint admin center, expand **Sites** and select **Active sites**.
2. Select the site you want to manage and the site details panel appears.
3. In **Settings** tab, select **Edit** in the **Restricted site access** section.
4. Enter the name of the security group in the **Add security group** field and select **Save**.

For restricted access control to work on a non-group connected site, you must add at least one security group. :::image type="content" source="media/rac-spac/non-group-connected-sites/4-RAC-SPAC-non-group-connected-sites-enabled-added-security-groups.png" alt-text="screenshot showing restricted access control security groups being added to non-group connected sites." lightbox="media/rac-spac/non-group-connected-sites/3-RAC-SPAC-Teams-non-group-connected-sites-enabled.png":::

> [!IMPORTANT]
> When you remove a security group from restricted access control, users of the security group will continue to have site access permissions. We recommend you review site permissions for the affected site in SharePoint admin center and remove users who no longer require access.

See the following table for more information on how to manage restricted access control for non-group connected sites using PowerShell:

|Action  |PowerShell command|
|---------|---------|
|Enable restricted access control     |`Set-SPOSite -Identity <siteurl> -RestrictedAccessControl $true`|
|Add security group |`Set-SPOSite -Identity <siteurl> -AddRestrictedAccessControlGroups <comma separated group GUIDS>`         |
|Edit security group     |`Set-SPOSite -Identity <siteurl> -RestrictedAccessControlGroups <comma separated group GUIDS>`         |
|View security group     |`Get-SPOSite -Identity <siteurl> | Select RestrictedAccessControl, RestrictedAccessControlGroups`         |
|Remove security group     |`Set-SPOSite -Identity <siteurl> -RemoveRestrictedAccessControlGroups <comma separated group GUIDS>`         |  
|Reset restricted access control  |`Set-SPOSite -Identity <siteurl> -ClearRestrictedAccessControl`         |

> [!NOTE]
> Resetting the restricted access control configuration for a given site using the command will set RestrictedAccessControl flag to false and clear RestrictedAccessControlGroups for the given site.

## Shared channel sites

For [shared channel sites](/microsoftteams/shared-channels), only internal users in the resource tenant are subject to restricted access control. External users are excluded from restricted access control policy and only evaluated per the site’s existing [site permissions](/microsoftteams/shared-channels).

For example:

The Contoso tenant has set up a manual trust relation with another Azure AD organization Fabrikam, via [B2B direct connect](/microsoftteams/shared-channels).  When restricted access control is enabled for a shared channel site in Contoso tenant, only users in Contoso are now subjected to restricted access control policy. Fabrikam users continue to be evaluated for site permissions only.  

> [!IMPORTANT]
> Site permissions for a shared channel site can’t be managed independently through SharePoint and must be done in Microsoft Teams.

## Auditing

Audit events are available in Microsoft Purview compliance portal to help you monitor restricted access control activities. Audit events are logged for the following activities:

- Applying restricted access control for site
- Removing restricted access control for site
- Changing restricted access control groups for site

## Related articles

[Microsoft Syntex - SharePoint Advanced Management overview](advanced-management.md)

[Restrict OneDrive access by security group](limit-access.md)

[Conditional access policy for SharePoint sites and OneDrive](authentication-context-example.md)

[Data Access Governance reports](data-access-governance-reports.md)
