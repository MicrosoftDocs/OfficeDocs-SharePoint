---
ms.date: 04/27/2023
title: "Restrict access to a SharePoint site by group membership"
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
ms.collection: 
- M365-collaboration
- Highpri
- Tier1
search.appverid:
description: "Learn how to enable restricted access control for SharePoint sites."
---
# Restrict access to a SharePoint site by Microsoft 365 group membership

[!INCLUDE[Advanced Management](includes/advanced-management.md)]

With restricted access control, you can manage the access of a SharePoint site and its content. As a [SharePoint administrator](sharepoint-admin-role.md), you'll grant access to specified users in the group associated with a SharePoint site. Users who aren't added to the specified group can't access even if they previously had site access permissions to a file. Restricted access control policy applies to Microsoft 365 group-connected sites, non-group connected sites and Microsoft Teams.

Restricting site access based on group membership reduces the risk of oversharing within your organization. Restricted access control provides an extra layer of security to safeguard site content. By enabling restricted site access, you apply a policy that stops sharing content with people who aren't a member of the group. Use and consult [data access governance reports](data-access-governance-reports.md) to see how data is currently being shared.

For example, the research department has a Microsoft 365 group containing all of their department members. They don’t want anyone outside of the department to have access to the research department site or its contents. To restrict site access to the research department's Microsoft 365 group, you enable restricted access control using PowerShell.

SharePoint [PowerShell](/powershell/sharepoint/sharepoint-online/introduction-sharepoint-online-management-shell) module is required to enable restricted access control.

## Requirements

To access and use this feature, your organization must have the following subscription:

- [Microsoft Syntex - SharePoint Advanced Management](advanced-management.md)

## Restricted access control for your organization

### Enable restricted access control for your organization

To enable restricted access control in SharePoint, run the following command:

```Powershell
Set-SPOTenant -EnableRestrictedAccessControl $true
```

Then, wait for approximately 1 hour before managing restricted access control for that site.

> [!NOTE]
> If you have Microsoft 365 Multi-Geo, you must run this command for each geo-location you want to use restricted access control.

## Restricted access control for group-connected or Teams-connected sites using Microsoft 365 group membership

You can enable restricted access control for your group-connected or Teams-connected sites using Microsoft 365 group membership. Restricted access control grants access to members of the Microsoft 365 group connected to the site. Users who aren't members of the Microsoft 365 group can't access the site and its content.

### Enable restricted access control for a group-connected site

To apply restricted access control to a group-connected or Teams-connected site, use the following command:

```Powershell
Set-SPOSite -Identity <siteurl> -RestrictedAccessControl $true
```

**For example:**

`Set-SPOSite -Identity https://contoso.sharepoint.com/sites/ResearchTeamSite -RestrictedAccessControl $true`

### View restricted access control for site for a group-connected site

To view the restricted access control configuration for a site, run the following command:

```Powershell
Get-SPOSite -Identity <siteurl> | Select RestrictedAccessControl
```

### Remove restricted access control for a group-connected site

To remove restricted access control from a site, run the following command:

```Powershell
Set-SPOSite -Identity <siteurl> -RestrictedAccessControl $false
```

**For example:**

`Set-SPOSite -Identity https://contoso.sharepoint.com/sites/ResearchTeamSite -RestrictedAccessControl $false`

## Restricted access control for non-group-connected sites using Azure AD security groups

As a SharePoint administrator, you can grant access to members of selected Azure AD security groups. **You can add up to 10 Azure AD security groups for a given site.** Users who aren't members of the added security groups can't access even if they previously had site access permissions to the site or the content.

### Enable restricted access control for a non-group-connected site

This will restrict the site access to members of the specified security group.

To apply restricted access control on a non-group connected site, run the following command:

```Powershell
Set-SPOSite -Identity <siteurl> -RestrictedAccessControl $true
```

```Powershell
```Set-SPOSite -Identity <siteurl> -AddRestrictedAccessControlGroups <comma separated group GUIDS>
```

> [!NOTE]
> 1. For restricted access control to be enforced on the site, you must add at least one security group whose members are allowed site access.
> 2. You can add up to 10 Security Groups for a given site.
> 3. The users in the security group will automatically have access to the site.

**For example:**

```Powershell
```Set-SPOSite -Identity https://contoso.sharepoint.com/sites/contosoteamsite -RestrictedAccessControl $true
```Set-SPOSite -Identity https://contoso.sharepoint.com/sites/contosoteamsite -AddRestrictedAccessControlGroups AFD516B5-C350-4C2A-8339-600B93C56791
```

> [!TIP]
> To identify corresponding GUID for a given security group (say Employees_FTE), run the following commands:
>
> ```Powershell
> Install-Module -Name MSOnline
> Import-Module -Name MSOnline 
> Connect- MsolService
> $group = Get-MsolGroup | Where-Object {$_.DisplayName -eq " Employees_FTE "}
> $group.ObjectId
> ```

### Manage Restricted access control groups for a non-group site

You can add up to 10 Azure AD security groups whose members will be allowed access to the site. These can be managed as **Restricted access control groups** when the setting is applied. This will limit the site access to members of the specified security groups.

### Add restricted access control to a security group

To enable restricted access control to a security group, run the following command:

```Powershell
```Set-SPOSite -Identity <siteurl> -RestrictedAccessControlGroups <comma separated group GUIDS>
```

**For example:**

```Powershell
```Set-SPOSite -Identity https://contoso.sharepoint.com/sites/HRPolicySite -RestrictedAccessControlGroups afd516b5-c350-4c2a-8339-600b93c56791,053e8286-f18a-40d6-a12a-a323b89c5d63
```

> [!NOTE]
> 1. The security groups specified will automatically get access to the site permissions.
>2. The policy is enforced only when it is enabled on the site and has at least one security group added.

### Remove restricted access control from a security group

You can remove the specified security group from restricted access control. Members of
the security group will no longer be able to access site contents while the policy is enforced on the site.

To remove restricted access control from a security group, run the following command:

```Powershell
```Set-SPOSite -Identity <siteurl> -RemoveRestrictedAccessControlGroups <comma separated group GUIDS>
```

**For example:**

```Powershell
```Set-SPOSite -Identity https://contoso.sharepoint.com/sites/HRPolicySite -RemoveRestrictedAccessControlGroups afd516b5-c350-4c2a-8339-600b93c56791
```

> [!NOTE]
> The Security Groups removed from the restricted access control list will continue to have site permissions. We recommend SPO admin to review site permissions and remove users who should no longer have site access permissions.

### View restricted access control for a non-group site

To view the restricted access control configuration for a site, run the following command:

```Powershell
```Get-SPOSite -Identity <siteurl> | Select RestrictedAccessControl, RestrictedAccessControlGroups
```

To view the complete list of security groups added in the restricted access control configuration for a site, run the following command:

```Powershell
```Get-SPOSite -Identity <siteurl> | Select -EXPAND RestrictedAccessControlGroups
```

> [!NOTE]
> The security groups added for this setting are also added to the **SharePoint members group** for the site. When disabling the setting, it is recommended to review site permissions and remove users who no longer need access to the site.

## Restricted access control for shared channel sites

For Shared Channel sites, only users in the resource tenant are subject to restricted access control. External users in the resource tenant will not be subjected to restricted access control policy and will be evaluated per the site’s existing site permissions only.

**For example:**

Consider a tenant Contoso which has set up a manual trust relation with another Azure AD organization Fabrikam, via B2B direct connect.  When restricted access control is enabled for a Shared channel site in Contoso tenant, only users in Contoso will be subjected to restricted access control policy. Fabrikam users will continue to be evaluated for site permissions only.  

> [!NOTE]
> Information the user should notice even if skimmingSite permissions for a shared channel site can’t be managed independently through SharePoint and must be done in Microsoft Teams.

## Auditing

Audit events are available in Microsoft Purview compliance portal to help you monitor restricted access control activities. Audit events are logged for the following activities:

1. Applying Restricted Access Control for site
2. Removing Restricted Access Control for site

## Related articles

[Microsoft Syntex - SharePoint Advanced Management overview](advanced-management.md)

[Conditional access policy for sites and OneDrives](authentication-context-example.md)

[Data Access Governance reports](data-access-governance-reports.md)
