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

# Manage Version history limits for a Site using PowerShell (Preview)

This article describes how Site Admins can choose to manage version history limits on individual sites. Using PnP PowerShell you can view any version history limits applied on a site, set a version limit for all, new or existing libraries, clear existing version limits on site to inherit from tenant level settings.

To manage version history limits for a site, use the following PowerShell commands:

| **Action:** | **PowerShell Command** |
|:-----|:-----|
| To view the version history limits set on a site | `Get-PnPSiteVersionPolicy`|
| To set version history limits for all libraries on a site. <br><br> Version history limits set on site level will be applied immediately to all new document libraries created in the site and will create a background request to asynchronously process the update on existing document libraries. | To set Automatic Version History Limits: <br><br> `Set-PnPSiteVersionPolicy` <br> `-EnableAutoExpirationVersionTrim $true` <br><br> To set Manual limits with Count and time parameters: <br><br> `Set-PnPSiteVersionPolicy` <br> `-EnableAutoExpirationVersionTrim $false` <br> `-MajorVersions <delete major versions exceeding limit>` <br> `-MajorWithMinorVersions <delete minor versions exceeding limit>` <br> `-ExpireVersionsAfterDays <delete versions exceeding time limit set in days>`<br><br> To set Manual limits with Count parameters only: <br><br> `Set-PnPSiteVersionPolicy` <br> `-EnableAutoExpirationVersionTrim $false` <br> `-MajorVersions <delete major versions exceeding limit>` <br> `-MajorWithMinorVersions <delete minor versions exceeding limit>` <br> `-ExpireVersionsAfterDays 0`  |
| To set version history limits to apply only to new document libraries created on a site without impacting the limits set on existing libraries. |To set Automatic Version History Limits for new libraries created on a site: <br><br> `Set-PnPSiteVersionPolicy` <br> `-EnableAutoExpirationVersionTrim $true -ApplyToNewDocumentLibraries` <br><br> To set Manual limits with Count and time parameters for new libraries created on a site: <br><br> `Set-PnPSiteVersionPolicy` <br> `-EnableAutoExpirationVersionTrim $false` <br> `-MajorVersions <delete major versions exceeding limit>` <br> `-MajorWithMinorVersions <delete minor versions exceeding limit>` <br> `-ExpireVersionsAfterDays 0`  <br><br> To set Manual limits with Count parameters only: <br><br> `Set-PnPSiteVersionPolicy` <br> `-EnableAutoExpirationVersionTrim $false` <br>  `-MajorVersions <delete major versions exceeding limit>` <br> `-ExpireVersionsAfterDays 0` <br> `-ApplyToNewDocumentLibraries` |
| To clear the existing version history limits set on a site and inherit Organization version limits on new document libraries created on the site. | `Set-PnPSiteVersionPolicy -InheritFromTenant` |

## Getting Started

1. Install the latest PnP PowerShell. For details, see [Installing PnP PowerShell | PnP PowerShell](https://pnp.github.io/powershell/articles/installation.html).
1. Connect to Site you want to apply the version history limits on.  
For example, <br> `Connect-PnPOnline -Url https://[tenant].sharepoint.com/sites/siteurl -Credentials $cred`

## Set version limits to apply to all document libraries in a site

You can set version limits to apply to all document libraries in a site by running the command to apply the selected setting. Once you run the command you will be able to review progress of settings update background job or optionally cancel the update job that are `<InProgress>`.  

### Apply desired version history limits to all document libraries on a site.

- Run the following commands to **apply Automatic setting** and check policy setting applied.

```PowerShell

   Set-PnPSiteVersionPolicy -EnableAutoExpirationVersionTrim $true
   # Check version policy setting on site
   Get-PnPSiteVersionPolicy 
``` 

- Run the following commands to **apply Manual Setting with count and time limits** and check policy setting applied.
 
In this example count limits are set to 100 major versions with 10 minor versions and versions are set to 
expire after 200 days.

```PowerShell

   Set-PnPSiteVersionPolicy -EnableAutoExpirationVersionTrim $false -MajorVersions 100 -
   MajorWithMinorVersions 10 -ExpireVersionsAfterDays 200
   # Check version policy setting on site
   Get-PnPSiteVersionPolicy 
```

- Run the following commands to **apply Manual Setting with count limits** and check policy setting applied. 

In this example count limits are set to 300 major versions with 20 minor versions.

```PowerShell

   Set-PnPSiteVersionPolicy -EnableAutoExpirationVersionTrim $false -MajorVersions 300 -
   MajorWithMinorVersions 20 -ExpireVersionsAfterDays 0
   # Check version policy setting on site
   Get-PnPSiteVersionPolicy 
```

### Get progress of an in-progress setting update request

Version limits on all new libraries created in the site will be immediately applied. Settings on existing libraries will be asynchronously updated using a background job. Run the following commands **to get the progress of the settings update job**. 

```PowerShell

   Get-PnPSiteVersionPolicyProgress
```
Here's the description of the status in response:

| **Status:** | **Description** |
|:-----|:-----|
| `NoRequestFound` | There's no request on the site to set version policy for existing document libraries. |
| `New`   | It's a new request and never processed. |
| `InProgress`  | The request was processed but not completed yet. |
| `CompleteSuccess` | The request was processed and completed successfully. |
| `CompleteWithFailure`  | It was processed and completed, but some document libraries failed to set the version policy. |

### Cancel an in-progress request to update version history limits on existing libraries. 

Run the following commands to cancel an `<InProgress>` settings update request. Cancels the settings update request on libraries that isn't processed. This won't revert the change for document libraries where the settings update was already processed.

```PowerShell

   Set-PnPSiteVersionPolicy -CancelForExistingDocumentLibraries
```

## Set version history limits to apply on new document libraries created on a site

- Run the following commands to **apply Automatic setting** and check policy setting applied.

```PowerShell

  Set-PnPSiteVersionPolicy -EnableAutoExpirationVersionTrim $true -
  ApplyToNewDocumentLibraries
  # Check version policy setting on site
  Get-PnPSiteVersionPolicy 
```

- Run the following commands to **apply Manual setting with count and time limits** and check policy setting applied. 

In this example count limits are set to 100 major versions and versions are set to expire after 200 days.

```PowerShell

   Set-PnPSiteVersionPolicy -EnableAutoExpirationVersionTrim $false -MajorVersions 100 -
   ExpireVersionsAfterDays 200 -ApplyToNewDocumentLibraries
   # Check version policy setting on site
   Get-PnPSiteVersionPolicy 
```

- Run the following commands to **apply Manual setting with count limits** and check policy setting applied.

In this example count limits are set to 300 major versions with 20 minor versions.

```PowerShell

   Set-PnPSiteVersionPolicy -EnableAutoExpirationVersionTrim $false -MajorVersions 300 -
   ExpireVersionsAfterDays 0 -ApplyToNewDocumentLibraries
   # Check version policy setting on site
   Get-PnPSiteVersionPolicy 
```

## Clear version history limits set on a site

Run the following command to **clear an existing version history limit applied on a site**. When the setting on the site is cleared, the tenant level version history limits will be applied on the new document libraries, but no changes will be made to the limits on existing libraries.

```PowerShell

   Set-PnPSiteVersionPolicy -InheritFromTenant
```

## Set version history policy for existing document libraries only

- Run the following commands to **apply Automatic setting** and check policy setting applied.

```PowerShell

   Set-PnPSiteVersionPolicy -EnableAutoExpirationVersionTrim $true -
   ApplyToExistingDocumentLibraries
```
:::image type="content" source="media/version-history/automatic-setting-existing-libs.png" alt-text="automatic setting existing libs":::

- Apply Manual Setting with Versions count and Time limits

```PowerShell

   Set-PnPSiteVersionPolicy -EnableAutoExpirationVersionTrim $false -MajorVersions 100 -
MajorWithMinorVersions 5 -ExpireVersionsAfterDays 200 -ApplyToExistingDocumentLibraries
```

- Apply Manual Setting with Versions count and NO Time limits

```PowerShell

   Set-PnPSiteVersionPolicy -EnableAutoExpirationVersionTrim $false -MajorVersions 100 -
MajorWithMinorVersions 5 -ExpireVersionsAfterDays 0 -ApplyToExistingDocumentLibraries
```
