---
title: "Manage Version history limits for a site using PowerShell"
ms.reviewer: 
ms.author: serdars
author: serdars
manager: serdars
recommendations: true
ms.date: 12/22/2023
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
description: "This article provides guidance on how to manage version history limits for a site using PowerShell."

---

# Manage Version history limits for a Site using PowerShell 

## Environment Setup

To manage **Version history limits** for a Site using PowerShell, install the latest PnP Powershell. For details, see [Installing PnP PowerShell | PnP PowerShell](https://pnp.github.io/powershell/articles/installation.html).

## Set Site Level Version Limits for both new and existing document libraries

### Apply Automatic settings

`Set-PnPSite -EnableAutoExpirationVersionTrim $true`
<br> Check version policy setting on the site using `Get-PnPSiteVersionPolicy`

> [!NOTE]
> Run `Get-PnPSiteVersionPolicy` in a new PS7 window if the values are not refreshed after set.  

:::image type="content" source="media/automatic-setting-pnp-site.PNG" alt-text="automatic set pnp":::

### Apply Manual Setting with versions count and Time limits

`Set-PnPSite -EnableAutoExpirationVersionTrim $false -MajorVersions 100 -MinorVersions 10 -ExpireVersionsAfterDays 200`

:::image type="content" source="media/manual-setting-pnp-site-time-limit.PNG" alt-text="manual set pnp time limit":::

### Apply Manual Setting with versions count and No Time limits

`Set-PnPSite -EnableAutoExpirationVersionTrim $false -MajorVersions 300 -MinorVersions 20 -ExpireVersionsAfterDays 0`

:::image type="content" source="media/manual-setting-pnp-site-no-time-limit.PNG" alt-text="manual set pnp no time limit":::

## Set site version policy for new document libraries only

### Apply Automatic settings 

`Set-PnPSite -EnableAutoExpirationVersionTrim $true -ApplyForNewLibs`

:::image type="content" source="media/automatic-setting-new-libs.PNG" alt-text="automatic set for new libs":::

### Apply Manual Setting with Major Version Count and Time limits

`Set-PnPSite -EnableAutoExpirationVersionTrim $false -MajorVersions 100 -ExpireVersionsAfterDays 200 -ApplyForNewLibs`

:::image type="content" source="media/automatic-setting-new-libs-time-limit.PNG" alt-text="automatic setting new libs with time limit":::

### Apply Manual Setting with Major Version Count and No Time limits  

`Set-PnPSite -EnableAutoExpirationVersionTrim $false -MajorVersions 300 -ExpireVersionsAfterDays 0 -ApplyForNewLibs`

:::image type="content" source="media/automatic-setting-new-libs-no-time-limit.PNG" alt-text="automatic setting new libs with no time limit":::

### Clear Site Level Version history limits  

If the setting on the site is cleared, the new document libraries use the tenant level settings.  
> [!NOTE]
> Clearing a setting on a Site will only apply to New Document Libraries created on the site and will not impact the settings on existing doc libraries.  

`Set-PnPSite -InheritTenantVPForNewDocLibs`

:::image type="content" source="media/inherit-tenant-new-doc-libs.PNG" alt-text="inherit tenant new doc libs":::

## Set site version policy for existing document libraries only

### Apply Automatic settings

`Set-PnPSite -EnableAutoExpirationVersionTrim $true -ApplyForExistingLibs`  

:::image type="content" source="media/automatic-setting-existing-libs.PNG" alt-text="automatic setting existing libs":::

### Apply Manual Setting with Versions count and Time limits

`Set-PnPSite -EnableAutoExpirationVersionTrim $false -MajorVersions 100 -MinorVersions 5 -ExpireVersionsAfterDays 200 -ApplyForExistingLibs`

:::image type="content" source="media/manual-setting-existing-libs-time-limit.PNG" alt-text="manual setting existing libs time limit":::

### Apply Manual Setting with Versions count and NO Time limits

`Set-PnPSite -EnableAutoExpirationVersionTrim $false -MajorVersions 100 -MinorVersions 5 -ExpireVersionsAfterDays 0 -ApplyForExistingLib`s 

:::image type="content" source="media/manual-setting-existing-libs-no-time-limit.PNG" alt-text="manual setting existing libs no time limit":::

### Cancel the request  

Cancel the request that isn't processed. Can't revert the change for the processed document libraries.  

`Set-PnPSite -CancelVPForExistingLibs`  

:::image type="content" source="media/cancel-existing-libs.PNG" alt-text="cancel existing libs":::
