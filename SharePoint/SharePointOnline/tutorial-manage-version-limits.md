---
title: "Tutorial: Manage Version history limits on a Site, Library, or OneDrive account"
ms.reviewer: rekamath
ms.author: serdars
author: serdars
manager: serdars
recommendations: true
ms.date: 04/30/2024
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
description: "This article provides guidance on how to manage Version history limits for a site, library, or OneDrive account."

---


# Tutorial: Manage Version history limits for a Site, Library, or OneDrive account

In this tutorial, you will learn how to manage the version history limits for a site, document library, or OneDrive account. You will learn how to:

- Set site level settings for all libraries on the site.
- Check progress of your settings update job.
- Stop an in-progress settings update job.

Before you begin:

1. Review your **organization’s recovery objectives** and **version storage use quota targets** along with the **site-specific version storage needs** to evaluate if a break of inheritance of version settings at site, library, or OneDrive account level is needed.
2. If needed **run an impact analysis** with the desired setting, to understand the impact the new setting would have using current version storage usage patterns.
3. For site version settings, evaluate the scope of document libraries that should be updated. Depending on business need, you can choose one of the following:

- Update new libraries only without impacting existing library settings.
- Update existing libraries only and inherit organization default settings for new libraries.
- Update both existing and all new libraries for consistent version storage at the site level.

## Set version limits to for a Site  

You can set version limits on a site by running the [**Set-SPOSite**](/powershell/module/sharepoint-online/set-sposite) command. Once you run the command, you can review progress of the settings update background job or optionally cancel the update job that are `<InProgress>`.

Consider the following example to apply Automatic version history limits on a site.

Run the following commands to **apply Automatic setting** to all document libraries on a site.

```PowerShell

```

Consider the following example to apply manual setting with Count and Time version history limits on a site.

Run the following commands to **apply manual setting with count and time limits.**

In this example count limits are set to 100 major versions with 10 minor versions and versions are set to expire after 200 days.

```PowerShell

```

> [!NOTE]
> ‘MajorWithMinorVersions’ count only applies to the document libraries that enabled minor versioning.

Consider the following example to apply manual setting with Count only version history limits on a site.

Run the following commands to **apply manual setting with count limits** and check policy setting applied.

In this example count limits are set to 300 major versions with 20 minor versions.

```PowerShell
Set-PnPSiteVersionPolicy -EnableAutoExpirationVersionTrim $false -MajorVersions 300 -MajorWithMinorVersions 20 -ExpireVersionsAfterDays 0
# Check version policy setting on site
Get-PnPSiteVersionPolicy
```

## Cancel an in-progress request to update version history limits on existing libraries

Run the following commands to cancel an `<InProgress>` settings update request.Cancelling the job doesn't revert the change for document libraries where the update was already processed.

```
PowerShell

```

## Set version history limits on new document libraries created on a site

Run the following commands to **apply Automatic setting** and check policy setting applied.

```PowerShell

Set-PnPSiteVersionPolicy -EnableAutoExpirationVersionTrim $true -ApplyToNewDocumentLibraries 
# Check version policy setting on site
Get-PnPSiteVersionPolicy
```

Run the following commands to **apply manual setting with count and time limits** and check policy setting applied.

In this example count limits are set to 100 major versions and versions are set to expire after 200 days.

```PowerShell

Set-PnPSiteVersionPolicy -EnableAutoExpirationVersionTrim $false -MajorVersions 100 -ExpireVersionsAfterDays 200 -ApplyToNewDocumentLibraries
# Check version policy setting on site
Get-PnPSiteVersionPolicy
```

Run the following commands to **apply manual setting with count limits** and check policy setting applied.

In this example count limits are set to 300 major versions with 20 minor versions.

```PowerShell

Set-PnPSiteVersionPolicy -EnableAutoExpirationVersionTrim $false -MajorVersions 300 -ExpireVersionsAfterDays 0 -ApplyToNewDocumentLibraries
# Check version policy setting on site
Get-PnPSiteVersionPolicy
```

## Set version history policy for existing document libraries only

Run the following commands to **apply Automatic setting** and check policy setting applied.

```PowerShell

Set-PnPSiteVersionPolicy -EnableAutoExpirationVersionTrim $true -ApplyToExistingDocumentLibraries
```

## Apply manual settings with versions count and time limits

```PowerShell

Set-PnPSiteVersionPolicy -EnableAutoExpirationVersionTrim $false -MajorVersions 100 -MajorWithMinorVersions 5 -ExpireVersionsAfterDays 200 -ApplyToExistingDocumentLibraries
```

## Apply Manual settings with versions count and no time limits  

```
PowerShell

Set-PnPSiteVersionPolicy -EnableAutoExpirationVersionTrim $false -MajorVersions 100 -MajorWithMinorVersions 5 -ExpireVersionsAfterDays 0 -ApplyToExistingDocumentLibraries
```

## Learn More

- Get Version History Limits on a Site: [Get-PnPSiteVersionPolicy](https://pnp.github.io/powershell/cmdlets/Get-PnPSiteVersionPolicy.html)
- Set Version History Limits on a Site: [Set-PnPSiteVersionPolicy](https://pnp.github.io/powershell/cmdlets/Set-PnPSiteVersionPolicy.html)
- Get progress of Version History Limits update on a Site: [Get-PnPSiteVersionPolicyProgress](https://pnp.github.io/powershell/cmdlets/Get-PnPSiteVersionPolicyProgress.html)