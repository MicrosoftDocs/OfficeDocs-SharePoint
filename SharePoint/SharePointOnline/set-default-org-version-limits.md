---
title: "Set default organization version limits"
ms.reviewer: rekamath
ms.author: ruihu
author: maggierui
manager: jtremper
recommendations: true
ms.date: 10/03/2024
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint
ms.localizationpriority: medium
search.appverid:
- SPO160
- SPS150
- MET150
description: "This article provides guidance on how admins can set default organization version limits for new document libraries and OneDrive accounts."

---

# Set default organization version limits for new document libraries and OneDrive accounts

Organization-level version settings define the default version storage limits that apply on all new document libraries created across all existing or newly created SharePoint sites and new OneDrive Accounts. This setting allows admins to define the global default version history limits that apply across the organization to ensure consistent version storage use and restore options.  

**Example Scenario**

Take an example of Contoso with an existing marketing site with a set of libraries set to 500 major version limits. When the admin updates the organization version limits to 'Automatic' library, version limits for document libraries are set in the following ways:

- **Library version limits on existing marketing site**: Version limits on all new libraries created in the marketing site are set to the organization limits of Automatic. Version limits on existing libraries remain unchanged that is, limits aren't updated to Automatic.  

- **Library version limits on new legal site**: When a new legal site is created, version limits on all libraries created on the legal site are set to the organization version limits.

:::image type="content" source="media/version-history/break-inheritance-at-site-level.png" lightbox="media/version-history/break-inheritance-at-site-level.png" alt-text="Diagram of break inheritance.":::

> [!IMPORTANT]
> - Changes made to organization-level version history limits apply to new SharePoint libraries and OneDrive user accounts created since the change was made. The changes can take upto 24 hours to be reflected on new libraries created. 
> - Changes made to organization-level version history limits will not update the limits applied to existing document libraries. To update the existing library settings, you can [set version limits for existing libraries on a site](site-version-limits.md) or [set version limits on a library](library-version-limits.md). The ability to apply version history limits to existing document libraries at the organization level is not supported.
> - Changes made to the organization-level version history limits will not trim existing version history to the new limits. To delete existing versions, you can [trim existing versions from a site, library or OneDrive](library-version-limits.md#manage-version-history-limits-for-a-library-using-powershell). The ability to trim existing versions at the organization level is not supported.
> - Default Version History limits for your organization is set to Manual version history limits with 500 major version count limit and no expiration.
> - Organization-level Document Library version limit settings can be used to configure version settings on libraries only ([List template Base Type = 1](/openspecs/sharepoint_protocols/ms-wssts/8bf797af-288c-4a1d-a14b-cf5394e636cf)). List version settings, creation of major and minor versions, or content approval workflows need to be [configured at individual library or list level](https://support.microsoft.com/en-us/office/enable-and-configure-versioning-for-a-list-or-library-1555d642-23ee-446a-990a-bcab618c7a37).
> - If your organization is configured for multi-geo, the Organization level version history levels can be set for each geo. 

## Manage version history limits for your organization

This article describes how global and SharePoint admins in Microsoft 365 can change the default version history limits for all new SharePoint document libraries and OneDrive accounts created in the organization. 

:::image type="content" source="media/version-history/sharepoint-admin-settings-2.png" lightbox="media/version-history/sharepoint-admin-settings-2.png" alt-text="Diagram of sharepoint admin settings.":::

On the version history limits, SharePoint Admin Setting page uses the Organization Level Version History Limits to set global default version history limits that are universally applied to all newly created document libraries in the organization.

:::image type="content" source="media/version-history/set-version-his-lim-2.png" lightbox="media/version-history/set-version-his-lim-2.png" alt-text="Diagram of set version history limits.":::


## Set automatic version history limits for the organization

1. Go to **Settings** in the [SharePoint admin center](/sharepoint/sharepoint-admin-role), and sign in with an account that has [administrator permissions](/sharepoint/sharepoint-admin-role) for your organization.
1. Select **Version History limits**.
1. Select **Automatically**.
1. Select **Save** and **Confirm** to apply the changes to all new libraries created.

:::image type="content" source="media/version-history/version-history-limits-automatic.png" lightbox="media/version-history/version-history-limits-automatic.png" alt-text="Diagram of automatic version history limits.":::

To set Automatic version history limits for all new document libraries created in your organization using PowerShell, run the following command:

```PowerShell
Set-SPOTenant-EnableAutoExpirationVersionTrim $true
```

## Set manual version count limits with no expiration

1. Go to **Settings** in the [SharePoint admin center](/sharepoint/sharepoint-admin-role), and sign in with an account that has [administrator permissions](/sharepoint/sharepoint-admin-role) for your organization.
1. Select **Version history limits**.
1. Select **Manually**.
1. Enter a value between 100 and 50,000 in the **Number of major versions** box.
1. Set the **Delete versions after this period of time** drop-down option to '**Never**.' This setting ensures that no expiration is stamped on versions.
1. Select **Save** and **Confirm** to apply the changes to all new libraries created.

:::image type="content" source="media/version-history/version-history-limits-manual.png" lightbox="media/version-history/version-history-limits-manual.png" alt-text="Screenshot of manual version count limits with no expiration.":::

## Set manual version count and expiration storage limits

To set count and expiration limits for all new document libraries created in your organization using SharePoint admin center:
1. Go to **Settings** in the [SharePoint admin center](/sharepoint/sharepoint-admin-role), and sign in with an account that has [administrator permissions](/sharepoint/sharepoint-admin-role) for your organization.
1. Select **Version history limits**.
1. Select **Manually**.
1. Enter a value between 100 and 50,000 in the **Number of major versions** box.
1. Select one of the preset values for **Delete versions after this period of time** drop-down option. or
1. To enter a custom value for **Delete versions after**, select the custom value from the dropbox and enter value greater than 30 days in the **Days** box and **Save**.
1. Select **Save** and **Confirm** to apply the changes to all new libraries created.

To set count and expiration limits for all new document libraries created in your organization using PowerShell, run the following command:

```PowerShell
Set-SPOTenant 
-EnableAutoExpirationVersionTrim $false
-MajorVersionLimit<int>
-ExpireVersionsAfterDays<0>
```

## Review organization version storage limits

To review the default version history limits for all new document libraries using SharePoint admin center:
1. Go to **Settings** in the [SharePoint admin center](/sharepoint/sharepoint-admin-role), and sign in with an account that has [administrator permissions](/sharepoint/sharepoint-admin-role) for your organization.
1. Select **Version history limits**.

To review the default version history limits for all new document libraries using PowerShell, run the following command:

```PowerShell
Get-SPOTenant | select EnableAutoExpirationVersionTrim, ExpireVersionsAfterDays,MajorVersionLimit
```

## Learn More

For more information, check out the following resources:

- [Manage Version History Limits for your Organization using Set-SPOTenant](/powershell/module/sharepoint-online/set-spotenant)
