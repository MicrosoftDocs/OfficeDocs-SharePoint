---
ms.date: 08/29/2023
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

Restricted access control enables SharePoint site and content management via [SharePoint Online PowerShell](../SharePointServer/sharepoint-powershell.md) or [SharePoint admin center](https://learn.microsoft.com/sharepoint/restricted-access-control). As a [SharePoint administrator](sharepoint-admin-role.md), you grant access to all users in the site's group. Others not in the group can't access the site or its content, even if they had prior permissions. This policy applies to Microsoft 365 group-connected, Teams-connected, and non-group connected sites

Restricting site access via group membership minimizes internal oversharing risk. For insights into data sharing, see [Data access governance reports](data-access-governance-reports.md). This extra security layer from restricted access control safeguards content during site access and opening. Enabling restricted access control enforces a policy to block non-group members from accessing content.

As an example, consider Contoso's research department in Microsoft 365. They have a group comprising department members and aim to limit access to their research site and its content. By activating restricted access control, they ensure only members of the department's Microsoft 365 group can access the site and its content.

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

You can restrict access to non-group connected sites by specifying [Azure AD security groups](/windows-server/identity/ad-ds/manage/understand-security-groups) in the SharePoint admin center or PowerShell. Each non-group connected site can be assigned up to 10 security groups. Once a security group is added, all users in the group will have access to the site.

> [!NOTE]
> Dynamic membership of security groups is also supported for restricted access control policy.

To enable, view, or disable site access to a non-group connected site:

1. In SharePoint admin center, expand **Sites** and select **Active sites**.
2. Select the site you want to manage and the site details panel appears.
3. In **Settings** tab, select **Edit** in the **Restricted site access** section.
4. Enter the name of the security group in the **Add security group** field and select **Save**.

For restricted access control to work on a non-group connected site, you must add at least one security group. :::image type="content" source="media/rac-spac/non-group-connected-sites/4-RAC-SPAC-non-group-connected-sites-enabled-added-security-groups.png" alt-text="screenshot showing restricted access control security groups being added to non-group connected sites." lightbox="media/rac-spac/non-group-connected-sites/3-RAC-SPAC-Teams-non-group-connected-sites-enabled.png":::

> [!IMPORTANT]
> When you remove a security group from restricted access control, users of the security group will continue to have site access permissions. We recommend manually reviewing site permissions in SharePoint admin center and remove users who no longer require access.

To enable restricted access control for a non-group connected site, run the following command:

```Powershell
Set-SPOSite -Identity <siteurl> -RestrictedAccessControl $true
```

To add a security group to a non-group connected site, run the following command:

```Powershell
Set-SPOSite -Identity <siteurl> -AddRestrictedAccessControlGroups <comma separated group GUIDS>
```

For example:

`Set-SPOSite -Identity https://contoso.sharepoint.com/sites/marketingdepartment -RestrictedAccessControl $true`

`Set-SPOSite -Identity https://contoso.sharepoint.com/sites/marketingdepartment -AddRestrictedAccessControlGroups AFD516B5-C350-4C2A-8339-600B93C56791`

> [!TIP]
> To identify corresponding GUID for a given security group (say Employees_MarketingDepartment), run the following commands:
>
> ```Powershell
> Install-Module -Name MSOnline
> Import-Module -Name MSOnline 
> Connect- MsolService
> $group = Get-MsolGroup | Where-Object {$_.DisplayName -eq " Employees_MarketingDepartment "}
> $group.ObjectId
> ```

#### Manage restricted access control groups for a non-group site using PowerShell

You can add up to 10 Azure AD security groups whose members are allowed access to the site. The specified security groups can be managed as restricted access control groups when the setting is applied. Restricted access control limits the site access to members of the specified security groups.

To edit a restricted access control group for a non-group site, run the following command:

```Powershell
Set-SPOSite -Identity <siteurl> -RestrictedAccessControlGroups <comma separated group GUIDS>
```

For example:

`Set-SPOSite -Identity https://contoso.sharepoint.com/sites/LegalDepartmentSite -RestrictedAccessControlGroups afd516b5-c350-4c2a-8339-600b93c56791,053e8286-f18a-40d6-a12a-a323b89c5d63`

> [!NOTE]
>
> - The security groups specified will automatically get access to the site permissions.
> - The policy is enforced only when it is enabled on the site and has at least one security group added.

#### Remove restricted access control groups for a non-group site using PowerShell

You can remove the specified security group from restricted access control configuration. Members of
the security group are no longer be able to access site content while the policy is enforced on the site.

To remove a security group from a restricted access control configuration for the non-group site, run the following command:

```Powershell
Set-SPOSite -Identity <siteurl> -RemoveRestrictedAccessControlGroups <comma separated group GUIDS>
```

For example:

`Set-SPOSite -Identity https://contoso.sharepoint.com/sites/LegalDepartmentSite -RemoveRestrictedAccessControlGroups afd516b5-c350-4c2a-8339-600b93c56791`

To reset restricted access control configuration for a site, run the following command:

```powershell
Set-SPOSite -Identity <siteurl> -ClearRestrictedAccessControl
```

For example:

`Set-SPOSite -Identity https://contoso.sharepoint.com/sites/LegalDepartmentSite -ClearRestrictedAccessControl`

This command resets the restricted access control configuration for the given site by setting RestrictedAccessControl flag to false and clearing RestrictedAccessControlGroups for the given site.

> [!TIP]
> The security groups removed from the restricted access control list will continue to have site permissions. We recommend SPO admin to review site permissions and remove users who should no longer have site access permissions.

#### View restricted access control for a non-group site using PowerShell

To view the restricted access control configuration for a site, run the following command:

```Powershell
Get-SPOSite -Identity <siteurl> | Select RestrictedAccessControl, RestrictedAccessControlGroups
```

To view the complete list of security groups added in the restricted access control configuration for a site, run the following command:

```Powershell
Get-SPOSite -Identity <siteurl> | Select -EXPAND RestrictedAccessControlGroups
```

> [!NOTE]
> The security groups added for this setting are also added to the SharePoint members group for the site. When disabling the setting, it is recommended to review site permissions and remove users who no longer need access to the site.

## Restricted access control using SharePoint admin center

### Sites not connected to Teams or Microsoft 365 groups (SharePoint admin center)

With restricted access control, you can restrict site access to members of specified Azure AD security groups. Users who aren't members of the specified security groups can't open the site or its content even if they previously had site access permissions. You can apply restricted access control on a site with up to 10 security groups. Dynamic membership of security groups is also supported for restricted access control policy.

## Shared channel sites

For [shared channel sites](/microsoftteams/shared-channels), only internal users in the resource tenant are subject to restricted access control. External users are excluded from restricted access control policy and only evaluated per the site’s existing [site permissions](/microsoftteams/shared-channels).

For example:

The Contoso tenant has set up a manual trust relation with another Azure AD organization Fabrikam, via [B2B direct connect](/microsoftteams/shared-channels).  When restricted access control is enabled for a shared channel site in Contoso tenant, only users in Contoso are now subjected to restricted access control policy. Fabrikam users continue to be evaluated for site permissions only.  

> [!IMPORTANT]
> Site permissions for a shared channel site can’t be managed independently through SharePoint and must be done in Microsoft Teams.

## Known experiences

1. Restricted access control policy is enforced only when the user is opening the SharePoint site or opening the content in the SharePoint site. This behavior is like any other conditional access policies configured for a site.
2. Unified Search connected experiences don't enforce restricted access control policy. Users see search results if they have existing access permissions to the content or the site. When the user selects a search result item to open the site content, they're denied access if they aren't part of the policy.

## Auditing

Audit events are available in [Microsoft Purview compliance portal](/microsoft-365/compliance/microsoft-365-compliance-center) to help you monitor restricted access control activities. Audit events are logged for the following activities:

1. Applying restricted access control for site
2. Removing restricted access control for site
3. Changing restricted access control groups for site

## Related articles

[Microsoft Syntex - SharePoint Advanced Management overview](advanced-management.md)

[Restrict OneDrive access by security group](limit-access.md)

[Conditional access policy for SharePoint sites and OneDrive](authentication-context-example.md)

[Data Access Governance reports](data-access-governance-reports.md)
