---
title: "Manage Version history limits for your Organization"
ms.reviewer: rekamath
ms.author: serdars
author: serdars
manager: serdars
recommendations: true
ms.date: 12/13/2023
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
description: "This article describes how global and SharePoint admins in Microsoft 365 can change their organization-level Version History Limit settings."
---

# Manage Version history limits for your Organization

This article describes how global and SharePoint admins in Microsoft 365 can change their organization-level Version History Limit settings for Microsoft SharePoint and Microsoft OneDrive.

:::image type="content" source="media/version-history/sharepoint-admin-settings.png" lightbox="media/version-history/sharepoint-admin-settings.png" alt-text="diagram of sharepoint admin settings":::

On the Version History Limits, SharePoint Admin Setting page uses the Organization Level Version History Limits to set global default version history limits that are universally applied to all newly created document libraries in the organization.

:::image type="content" source="media/version-history/set-version-history-limits.png" lightbox="media/version-history/set-version-history-limits.png" alt-text="diagram of set version history limits":::

The Set version history limits has two setting options:

- Automatically – Versions are deleted overtime based on the activity and how long ago the file was first created.

- Manually – When versions exceed a set number or time limit, the oldest versions are deleted.

**Automatically**

- Automatic is a recommended option providing the most optimal storage option without having to estimate the version count or age limits.

- Deploys an algorithm to preserve a sufficient high-value version, prioritizing more recent versions over ones farther back in time, to ensure availability in case restores are required.
 
**Manually**

There are two modes of manual configuration.

- Major version count and time limits: versions are deleted after exceeding the specified number of major versions or after the set time period.

- Major version count limits only: versions are deleted after they exceed the set number of major versions. There are no time limits set on versions.

## Set Automatic Version Storage limits

1. Go to **Settings** in the [SharePoint admin center](/sharepoint/sharepoint-admin-role), and sign in with an account that has [administrator permissions](/sharepoint/sharepoint-admin-role) for your organization.
1. Select **Version History limits**.
1. Select **Automatically**.
1. Select **Save** and **Confirm** to apply the changes to all new libraries created.

:::image type="content" source="media/version-history/version-history-limits-automatic.png" lightbox="media/version-history/version-history-limits-automatic.png" alt-text="automatic":::

To set Automatic version history limits for all new document libraries created in your organization using PowerShell, run the following command:

```PowerShell
Set-SPOTenant-EnableAutoExpirationVersionTrim $true
```

## Set Manual Version Count Limits with No Expiration

1. Go to **Settings** in the [SharePoint admin center](/sharepoint/sharepoint-admin-role), and sign in with an account that has [administrator permissions](/sharepoint/sharepoint-admin-role) for your organization.
1. Select **Version history limits**.
1. Select **Manually**.
1. Enter a value between 100 and 50,000 in the **Number of major versions** box.
1. Set the **Delete versions after this period of time** drop-down option to '**Never**.' This setting ensures that no expiration is stamped on versions.
1. Select **Save** and **Confirm** to apply the changes to all new libraries created.

:::image type="content" source="media/version-history/version-history-limits-manual.png" lightbox="media/version-history/version-history-limits-manual.png" alt-text="custom":::

## Set Manual Version Count and Expiration Storage Limits

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

## Review Organization Version Storage Limits

1. Go to **Settings** in the [SharePoint admin center](/sharepoint/sharepoint-admin-role), and sign in with an account that has [administrator permissions](/sharepoint/sharepoint-admin-role) for your organization.
1. Select **Version history limits**.

To review the default version history limits for all new document libraries using PowerShell, run the following command:

```PowerShell
Get-SPOTenant | select EnableAutoExpirationVersionTrim, ExpireVersionsAfterDays,MajorVersionLimit
```
