---
ms.date: 07/31/2023
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

With restricted access control, you can manage access of a SharePoint site and its content using **SharePoint PowerShell** or **SharePoint admin center**. As a [SharePoint administrator](sharepoint-admin-role.md), you can grant access to specified users in the group associated with a SharePoint site. Users not added to the specified group can't open the site at access time or open the site content even if they previously had access permissions to the site or the file. **The restricted access control policy applies to Microsoft 365 group-connected sites, non-group connected sites and Microsoft Teams.**

Restricting site access based on group membership reduces the risk of site oversharing within your organization. To view how data is shared in your organization, use [data access governance reports](data-access-governance-reports.md). Restricted access control provides an extra layer of security to safeguard site content at site access time or when opening the content. By enabling restricted site access, you apply a policy that prevents access of content by users who aren't a member of the specified group.

For example, the Contoso tenant's research department has a Microsoft 365 group containing all their department members. The department doesn't want anyone outside of the department to access the research team site or its content. They enable restricted access control on the site to restrict site access to the research department's Microsoft 365 group. Only users who are members of the Microsoft 365 group can visit the site or open its content.

## Restricted access control using PowerShell

### Requirements for PowerShell method

To access and use this feature, your organization must do the following in **PowerShell**:

- Subscribe to **[Microsoft Syntex - SharePoint Advanced Management](advanced-management.md)** before following these instructions:
- Download the latest **[SharePoint PowerShell module](/powershell/sharepoint/sharepoint-online/introduction-sharepoint-online-management-shell)**
- Enable **restricted access control for your organization**:

  1. Run the following command in PowerShell:
  
        ```Powershell
      Set-SPOTenant -EnableRestrictedAccessControl $true
      ```

  2. Wait for approximately 1 hour.
  
  3. Manage restricted access control for that site.

> [!NOTE]
> If you have Microsoft 365 Multi-Geo, you must run this command for each geo-location you want to use restricted access control.

### Teams and Microsoft 365 group-connected sites (PowerShell)

You can enable restricted access control for your group-connected or Teams-connected sites using Microsoft 365 group membership. Restricted access control grants access to members of the Microsoft 365 group connected to the site when accessing the site or opening its content. Users who aren't ***members of the Microsoft 365 group*** can't access the site and its content.

#### Enable restricted access control for group-connected sites using PowerShell

To apply restricted access control to a group-connected or Teams-connected site, use the following command:

```PowerShell
Set-SPOSite -Identity <siteurl> -RestrictedAccessControl $true
```

**For example:**

`Set-SPOSite -Identity https://contoso.sharepoint.com/sites/ResearchTeamSite -RestrictedAccessControl $true`

#### View restricted access control for group-connected sites using PowerShell

To view the restricted access control configuration for a site, run the following command:

```PowerShell
Get-SPOSite -Identity <siteurl> | Select RestrictedAccessControl
```

#### Remove restricted access control for group-connected sites using PowerShell

To remove restricted access control from a site, run the following command:

```PowerShell
Set-SPOSite -Identity <siteurl> -RestrictedAccessControl $false
```

**For example:**

`Set-SPOSite -Identity https://contoso.sharepoint.com/sites/ResearchTeamSite -RestrictedAccessControl $false`

### Sites not connected to Teams or Microsoft 365 groups (PowerShell)

With restricted access control, you can ***restrict site access to members of specified [Azure AD security groups](/windows-server/identity/ad-ds/manage/understand-security-groups)*** using [SharePoint PowerShell](/powershell/sharepoint/sharepoint-online/introduction-sharepoint-online-management-shell). Users who aren't members of the specified security groups can't open the site or its content even if they previously had site access permissions. **You can apply restricted access control on a site with up to 10 security groups.** [Dynamic membership](/azure/active-directory/enterprise-users/groups-create-rule) of security groups is also supported for restricted access control policy.

#### Enable restricted access control for non-group connected sites using PowerShell

To enable restricted access control for a non-group connected site, run the following command:

```Powershell
Set-SPOSite -Identity <siteurl> -RestrictedAccessControl $true
```

```Powershell
Set-SPOSite -Identity <siteurl> -AddRestrictedAccessControlGroups <comma separated group GUIDS>
```

> [!NOTE]
>
> - For restricted access control to be enforced on the site, you must add at least one security group whose members are allowed site access.
> - You can add up to 10 security Groups for a given site.
> - The users in the security group will automatically have access to the site.

**For example:**

`Set-SPOSite -Identity https://contoso.sharepoint.com/sites/marketingdepartment -RestrictedAccessControl $true`

`Set-SPOSite -Identity https://contoso.sharepoint.com/sites/marketingdepartment -AddRestrictedAccessControlGroups AFD516B5-C350-4C2A-8339-600B93C56791`

After running the commands, you have restricted site access to members of the specified security group (Employees_MarketingDepartment).

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

You can add up to 10 Azure AD security groups whose members are allowed access to the site. The specified security groups can be managed as **restricted access control groups** when the setting is applied. Restricted access control limits the site access to members of the specified security groups.

To edit a restricted access control group for a non-group site, run the following command:

```Powershell
Set-SPOSite -Identity <siteurl> -RestrictedAccessControlGroups <comma separated group GUIDS>
```

**For example:**

`Set-SPOSite -Identity https://contoso.sharepoint.com/sites/LegalDepartmentSite -RestrictedAccessControlGroups afd516b5-c350-4c2a-8339-600b93c56791,053e8286-f18a-40d6-a12a-a323b89c5d63`

> [!NOTE]
>
> - The security groups specified will automatically get access to the site permissions.
> - The policy is enforced only when it is enabled on the site and has at least one security group added.

#### Remove restricted access control groups for a non-group site using PowerShell

You can remove the specified security group from restricted access control configuration. Members of
the security group are no longer be able to access site content while the policy is enforced on the site.

**To remove a security group from a restricted access control configuration for the non-group site, run the following command:**

```Powershell
Set-SPOSite -Identity <siteurl> -RemoveRestrictedAccessControlGroups <comma separated group GUIDS>
```

**For example:**

`Set-SPOSite -Identity https://contoso.sharepoint.com/sites/LegalDepartmentSite -RemoveRestrictedAccessControlGroups afd516b5-c350-4c2a-8339-600b93c56791`

**To reset restricted access control configuration for a site, run the following command:**

```powershell
Set-SPOSite -Identity <siteurl> -ClearRestrictedAccessControl
```

**For example:**

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
> The security groups added for this setting are also added to the ***SharePoint members group*** for the site. When disabling the setting, it is recommended to review site permissions and remove users who no longer need access to the site.

## Restricted access control using SharePoint admin center

### Requirements for SharePoint admin center method

To access and use this feature, your organization must:

- Subscribe to Microsoft Syntex - SharePoint Advanced Management.
- Enable restricted access control for your organization in SharePoint admin center:
  1. Expand **Policies** and select **Access control**.
  2. Select **Site access restriction**.
  3. Select **Allow access restriction** box.

Now you can manage restricted access control for SharePoint sites from the SharePoint admin center. :::image type="content" source="media/rac-spac/1-RAC-SPAC-dashboard.png" alt-text="screenshot of restricted access control in sharepoint admin center dashboard." lightbox="media/rac-spac/1-RAC-SPAC-dashboard.png":::

### Teams and Microsoft 365 group-connected site (SharePoint admin center)

You can enable restricted access control for your group-connected or Teams-connected sites using Microsoft 365 group membership. Members of the Microsoft 365 group connected to the site are granted access to the site and its content. Users who aren't members of the Microsoft 365 group can't access the site and its content. :::image type="content" source="media/rac-spac/teams-M365-connected-sites/2-RAC-SPAC-Teams-M365-connected-sites.png" alt-text="screenshot of restricted site access on group-connected sites." lightbox="media/rac-spac/teams-m365-connected-sites/2-RAC-SPAC-Teams-M365-connected-sites.png":::

#### Enable restricted access control for group-connected sites using SharePoint admin center

To enable restricted access control for a group-connected site:

1. Go to SharePoint admin center, expand **Sites** and select **Active sites**.
2. Select the site you want to manage and the site details panel appears.
3. In **Settings** tab, select **Edit** in the **Restricted site access** section.
4. Select the **Restrict access to this site** box.
5. Select **Save**.

#### View restricted access control for group-connected sites using SharePoint admin center

To view the restricted access control configuration for a site:

1. Go to SharePoint admin center, expand **Sites** and select **Active sites**.
2. Select the site you want to manage to view restricted access control on the site details panel.

#### Remove restricted access control for group-connected sites using SharePoint admin center

To remove restricted access control policy from a group-connected or Teams-connected site:

1. Go to SharePoint admin center, expand **Sites** and select **Active sites**.
2. Select the site you want to manage and the site details panel appears.
3. In **Settings** tab, select **Edit** in the **Restricted site access** section.
4. Deselect the **Restrict access to this site** box.
5. Select **Save**.

Restricted access control is disabled for the site.

### Sites not connected to Teams or Microsoft 365 groups (SharePoint admin center)

With restricted access control, you can restrict site access to members of specified Azure AD security groups. Users who aren't members of the specified security groups can't open the site or its content even if they previously had site access permissions. You can apply restricted access control on a site with up to 10 security groups. Dynamic membership of security groups is also supported for restricted access control policy.

#### Enable restricted access control for a non-group site using SharePoint admin center

To apply restricted access control policy to a non-group connected site:

1. Go to SharePoint admin center, expand **Sites** and select **Active sites**.
2. Select the site you want to manage and the site details panel appears.
3. In **Settings** tab, select **Edit** in the **Restricted site access** section.
4. Enter the security group you want to add in the **Add security group** field and select **Save**.

For restricted access control to be enforced on the site, you must add at least one security group. You can add up to 10 security groups for a given site. All users in the security group will automatically have access to the site. :::image type="content" source="media/rac-spac/non-group-connected-sites/3-RAC-SPAC-Teams-non-group-connected-sites-enabled.png" alt-text="screenshot on how to enable rac on non-group connected site." lightbox="media/rac-spac/teams-m365-connected-sites/3-RAC-SPAC-Teams-M365-connected-sites-enabled.png"::: :::image type="content" source="media/rac-spac/non-group-connected-sites/4-RAC-SPAC-non-group-connected-sites-enabled-added-security-groups.png" alt-text="screenshot showing restricted access control security groups being added to non-group connected sites." lightbox="media/rac-spac/non-group-connected-sites/3-RAC-SPAC-Teams-non-group-connected-sites-enabled.png":::

#### Remove security groups from a non-group site using SharePoint admin center

To remove restricted access control security groups from a non-group site:

1. In SharePoint admin center, expand **Sites** and select **Active sites**.
2. Select the site you want to manage and the site details panel appears.
3. In **Settings** tab, select **Edit** in the **Restricted site access** section.  
4. Select **X** to remove a specific security group and select **Save**.

> [!TIP]
> Security groups removed from restricted access control will continue to have site permissions. We recommend using SharePoint admin center to review site permissions and remove users who no longer require site access permissions.

#### Remove restricted access control for a non-group site using SharePoint admin center

To remove restricted access control policy from a non-group connected site:

1. In SharePoint admin center, expand **Sites** and select **Active sites**.
2. Select the site and select the **Settings** tab in the site details panel.
3. Under **Restricted site access**, select **Edit**.
4. Deselect the **Restrict SharePoint site access to only users in specified security groups** box.
5. Select **Save**.

The security groups added to this setting are also added to the ***SharePoint members group*** for the site. When disabling the setting, it is recommended to review site permissions and remove users who no longer need access to the site.

## Shared channel sites

For [shared channel sites](/microsoftteams/shared-channels), only internal users in the resource tenant are subject to restricted access control. External users are excluded from restricted access control policy and only evaluated per the site’s existing [site permissions](/microsoftteams/shared-channels).

**For example:**

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
