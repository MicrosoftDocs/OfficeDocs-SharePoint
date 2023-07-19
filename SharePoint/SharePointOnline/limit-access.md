---
ms.date: 07/18/2023
title: "Restrict OneDrive access"
ms.author: mactra
author: MachelleTranMSFT
manager: serdars
audience: Admin
f1.keywords:
- CSH
ms.topic: article
ms.service: one-drive
ms.localizationpriority: medium
ms.collection: 
- Strat_OD_admin
- M365-collaboration
- Highpri
- Tier1
search.appverid:
ms.assetid: 
ms.custom:
- admindeeplinkSPO
- onedrive-toc
description: "In this article, you'll learn how to allow only users in specified security groups to access OneDrive."
---

# Restrict OneDrive access

[!INCLUDE[Advanced Management](includes/advanced-management.md)]

You can use the restricted access control policy for OneDrive to allow only users in specified security groups to access OneDrive. Even if other users outside of these security groups are licensed for OneDrive, they won’t have access to their own OneDrive or any shared OneDrive content.

You can use this to prevent oversharing of OneDrive content. For example, you can restrict OneDrive access to your users, preventing guests from accessing any OneDrive content even if it's shared with them.

## Requirements

To access and use this feature, your organization must have one of the following subscriptions:

- Office 365 E5/A5
- Microsoft 365 E5/A5
- Microsoft Syntex - SharePoint Advanced Management
  - To enable restricted access control from your Microsoft Syntex - SharePoint Advanced Management subscription:

  1. Download the latest **[SharePoint PowerShell module](/powershell/sharepoint/sharepoint-online/introduction-sharepoint-online-management-shell)**
  2. Run the following command in PowerShell:

    ```Powershell
    Set-SPOTenant -EnableRestrictedAccessControl $true
    ```

  3. Wait for approximately 1 hour.

    > [!NOTE]
    >
> If you have Microsoft 365 Multi-Geo, you must run this command for each geo-location you want to use restricted access control.

## Enablement

### Office 365 and Microsoft 365 subscribers

To enable this feature as an Office 365 or Microsoft 365 subscriber:

1. Go to <a href="https://go.microsoft.com/fwlink/?linkid=2185071" target="_blank">Access control in the SharePoint admin center</a>, and sign in with an account that has [admin permissions](sharepoint-admin-role.md) for your organization.

2. Select **Restrict OneDrive access**.

3. Select **Restrict OneDrive access to only users in specified security groups**.

    :::image type="content" source="media/restrictonedriveaccess.png" alt-text="Restrict OneDrive access on the Access control page in the SharePoint admin center":::

4. Add the security groups (maximum of 10) you want to be able to use OneDrive.

5. Select **Save**.

> [!NOTE]
> Users who aren't included in the security groups you added will lose access to their own OneDrive and any shared OneDrive content.

### Microsoft Syntex - SharePoint Advanced Management subscribers

#### Enable restricted access control for a OneDrive account

To enable restricted access control for a OneDrive account, run the following commands:

```powershell
Set-SPOSite -Identity <siteurl> -RestrictedAccessControl $true
```

```powershell
Set-SPOSite -Identity <siteurl> -AddRestrictedAccessControlGroups <comma separated group GUIDS>
```

> [!NOTE]
> For restricted access control to be enforced on the site, you must add at least one security group whose members are allowed site access. You can add up to 10 Security Groups for a given site. Once users are added to a security group, access to the site is automatically applied.

**For example:**

```powershell
Set-SPOSite -Identity <https://contoso-my.sharepoint.com/personal/user_contoso_onmicrosoft_com> -RestrictedAccessControl $true
```

```powershell
Set-SPOSite -Identity <https://contoso-my.sharepoint.com/personal/user_contoso_onmicrosoft_com> -AddRestrictedAccessControlGroups afd516b5-c350-4c2a-8339-600b93c56791
```

After running the commands, you have restricted site access to members of the specified security group (Employees_ResearchDepartment).

Note

To identify corresponding GUID for a given Security Group (say Employees_ResearchDepartment), run the following commands:

Install-Module -Name MSOnline
Import-Module -Name MSOnline  
Connect- MsolService

$group = Get-MsolGroup | Where-Object {$_.DisplayName -eq " Employees_ MarketingDepartment"}
$group.ObjectId

#### Manage restricted access control groups for a OneDrive account

You can add up to 10 Azure AD security groups whose members will be allowed access to the site. The specified security groups can be managed as restricted access control groups when the setting is applied. Restricted access control will now limit the site access to members of the specified security groups. Dynamic membership of security groups is also supported for restricted access control policy.

To edit a restricted access control group for a OneDrive site, run the following command:

```powershell
Set-SPOSite -Identity <siteurl> -RestrictedAccessControlGroups <comma separated group GUIDS>
```

**For example**:

```powershell
Set-SPOSite -Identity <https://contoso-my.sharepoint.com/personal/user_contoso_onmicrosoft_com> -RestrictedAccessControlGroups afd516b5-c350-4c2a-8339-600b93c56791,053e8286-f18a-40d6-a12a-a323b89c5d63
```

> [!NOTE]
> The Security Groups specified will automatically get access to the site permissions.
>
> The policy is enforced only when it is enabled on the site and has at least one security group added.

#### Remove restricted access control groups for a OneDrive account

To limit access control on user OneDrive account, remove security groups by running the following command:

```powershell
Set-SPOSite -Identity <siteurl> -RemoveRestrictedAccessControlGroups <comma separated group GUIDS>
```

**For example**:

```powershell
Set-SPOSite -Identity <https://contoso-my.sharepoint.com/personal/user_contoso_onmicrosoft_com> -RemoveRestrictedAccessControlGroups afd516b5-c350-4c2a-8339-600b93c56791
```

### View restricted access control for a OneDrive account

To view the restricted access control configuration for a OneDrive account, run the following command:

```powershell
Get-SPOSite -Identity <siteurl> | Select RestrictedAccessControl, RestrictedAccessControlGroups
```

To view the complete list of security groups added in the restricted access control configuration for a OneDrive account, run the following command:

```powershell
Get-SPOSite -Identity <siteurl> | Select -EXPAND RestrictedAccessControlGroups
```

#### Disable restricted access control for a OneDrive account

To disable restricted access control for a OneDrive account, run the following command:

```powershell
Set-SPOSite -Identity <siteurl> -RestrictedAccessControl $false
```

**For example**:

```powershell
Set-SPOSite -Identity <https://contoso-my.sharepoint.com/personal/user_contoso_onmicrosoft_com> -RestrictedAccessControl $false
```

#### Remove restricted access control for a OneDrive account

To remove restricted access control configuration for a OneDrive account, run the following command:

```powershell
Set-SPOSite -Identity <siteurl> -ClearRestrictedAccessControl
```

**For example**:

```powershell
Set-SPOSite -Identity <https://contoso-my.sharepoint.com/personal/user_contoso_onmicrosoft_com> -ClearRestrictedAccessControl
```

This command will reset the restricted access control configuration for the given site by clearing both attributes: RestrictedAccessControl, RestrictedAccessControlGroups.

### Known experiences

Restricted access control policy is enforced only when the user is trying to access the OneDrive account or the content in in. This behavior is like any other conditional access policies configured for a site.

Unified Search connected experiences don't enforce restricted access control policy. Users see search results if they have existing access permissions to the content or the site. When the user selects a search result item to open the content, they're denied access if they aren't part of the policy.

## Auditing

Audit events are available in [Microsoft Purview compliance portal](/microsoft-365/compliance/microsoft-365-compliance-center) to help you monitor restricted access control activities. Audit events are logged for the following activities:

1. Applying restricted access control for site
2. Removing restricted access control for site
3. Changing restricted access control groups for site

## Related topics

[Restrict access control for SharePoint sites](restricted-access-control.md)

[Data access governance insights for SharePoint sites](data-access-governance-reports.md)
