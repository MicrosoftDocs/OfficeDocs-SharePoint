---
title: "Change Version history limits for a Site (Preview)"
ms.reviewer: rekamath
ms.author: serdars
author: serdars
manager: serdars
recommendations: true
ms.date: 12/12/2023
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
description: "This article provides guidance on how admins can set version history limits on individual sites."

---

# Set Version limits for a Site (Preview)

By default, Organization level settings define the Version history limits that are applied to all new document libraries created in a site. However, to meet specific content needs, admins can choose to set distinct **Version history limits** on individual sites. This way, users can break the inheritance from organization limits on an individual site.

**Version history limits** for an individaul site can be managed in the following ways:

| Version history limits option | Description |
|:-----|:-----|
|**Apply site-level Version history limits to all new and existing document libraries in a Site:** |To achieve a consistent version storage policy for a site, you can choose to **set a limit to universally apply to all libraries** in the site. Using this option, the **Version history limit** set on site-level is applied to all the new document libraries created in the site and creates a background request to asynchronously process the update on existing document libraries.|
|**Apply site-level Version history limits to only new document libraries created in a Site:**|To avoid impacting the settings on existing libraries, you can **set a version history limit only for new libraries**. Using this option, the **Version history limits** set on site-level are only applied to new document libraries created in the site. There are no changes made to the limits on the existing document libraries or on libraries that aren't enabled for versioning in the site.|
|**Apply version history limits to existing document libraries only in a Site:**|You can update the limits **only on existing document libraries** on a site without setting a site level version history setting for new document libraries. Using this option creates a background request to asynchronously process the update on existing document libraries while allowing the new document libraries created in the site to inherit the organization level version history limits.|
|**Clear existing limits set on a Site:** |You can **clear the existing limits on a site** to allow new document libraries created in the site to follow organization level limits. **NOTE:** Clearing a setting on a Site applies only to New Document Libraries created on the site and doesn't impact the settings on existing doc libraries or trim existing versions.|

**Example Scenario**

Take an example of Contoso where organizational version limits are set to Automatic, no version limits set for Marketing Site and Legal Site. Suppose Site Administrator of Legal site sets the site version history limit to 500 major version count limit for new and existing libraries. Library version limits for Contoso are set in the following ways:

- **Library version limits on Marketing Site**: Since there's no site level version limit set for Marketing site, organization limit of Automatic is set on all new libraries created in marketing site.  

- **Library version limits on Legal Site**: Since version limits are set for Legal site, all new libraries are set to store 500 major versions.

:::image type="content" source="media/version-history/set-version-limits-for-a-site.png" lightbox="media/version-history/set-version-limits-for-a-site.png" alt-text="Diagram of set version limits for a site level":::

> [!IMPORTANT]
> - Site level Version history limits can be set using PowerShell cmdlets only.
> - Setting site level Version history limits doesn't trim existing versions to meet the new limits. Additional steps are needed to [trim existing versions on a site or library.](library-version-limits.md#manage-version-history-limits-for-a-library-using-powershell)
> - Requests to update the limits on existing libraries are processed asynchronously which can take up to 24 hours to process. You can review the progress of settings to update background job of all jobs that are in progress.
> - Cancelling an in-progress job stops the update on libraries that were not processed. This action doesn't revert the change for document libraries where the settings update was already processed.


## Manage Version history limits for a Site using PowerShell

Follow these steps to manage Version history limits for a site by using PowerShell.

1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).

> [!NOTE]
> If you installed a previous version of the SharePoint Online Management Shell, go to Add or remove programs and uninstall **SharePoint Online Management Shell**.

1. Connect to SharePoint as a [Global Administrator or SharePoint Administrator](/sharepoint/sharepoint-admin-role) in Microsoft 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).
2. Run one of the following commands to manage version history limits on your site:

| **Action** | **PowerShell Command** |
| --- | --- |
| View the version history limits set on a site | `Get-SPOSite -Identity $siteUrl \| fl Url, EnableAutoExpirationVersionTrim, ExpireVersionsAfterDays, MajorVersionLimit` |
| Set Automatic version history limits on a site. | To set Automatic Version History Limits for all libraries on a site:<br><br>`Set-SPOSite -Identity $siteUrl`<br>`-EnableAutoExpirationVersionTrim $true`<br><br>Append `-ApplyToNewDocumentLibraries` parameter to apply only to new document libraries on the site:<br><br>`Set-SPOSite -Identity $siteUrl`<br>`-EnableAutoExpirationVersionTrim $true`<br>`-ApplyToNewDocumentLibraries` <br><br>Append `-ApplyToExistingDocumentLibraries` to apply only to existing document libraries on a site:<br><br>`Set-SPOSite -Identity $siteUrl`<br>`-EnableAutoExpirationVersionTrim $true`<br>`-ApplyToExistingDocumentLibraries` |
| Set Manual limits with Count and time parameters on a site. | To set Manual limits with Count and time parameters for all libraries on a site:<br><br>`Set-SPOSite -Identity $siteUrl`<br>`-EnableAutoExpirationVersionTrim $false`<br>`-MajorVersions     <delete major versions exceeding limit>`<br>`-MajorWithMinorVersions <delete minor versions exceeding limit>`<br>`-ExpireVersionsAfterDays <delete versions exceeding time limit set in days>`<br><br>Append `-ApplyToNewDocumentLibraries` parameter to apply only to new document libraries on the site:<br><br>`Set-SPOSite -Identity $siteUrl`<br>`-EnableAutoExpirationVersionTrim $false`<br>`-MajorVersions <delete major versions exceeding limit>`<br>`-MajorWithMinorVersions <delete minor versions exceeding limit>`<br>`-ExpireVersionsAfterDays <delete versions exceeding time limit set in days>`<br>`-ApplyToNewDocumentLibraries` <br><br>Append `-ApplyToExistingDocumentLibraries` to apply only to existing document libraries on a site:<br><br>`Set-SPOSite -Identity $siteUrl`<br>`-EnableAutoExpirationVersionTrim $false`<br>`-MajorVersions <delete major versions exceeding limit>`<br>`-MajorWithMinorVersions <delete minor versions exceeding limit>`<br>`-ExpireVersionsAfterDays <delete versions exceeding time limit set in days>`<br>`-ApplyToExistingDocumentLibraries` |
| Set Manual count with no expiration limit on a site. | To set Manual limits with Count limits set the `-ExpireVersionsAfterDays` parameter to `0:`<br><br>`Set-SPOSite -Identity $siteUrl`<br>`-EnableAutoExpirationVersionTrim $false`<br>`-MajorVersions <delete major versions exceeding limit>`<br>`-MajorWithMinorVersions <delete minor versions exceeding limit>`<br>`-ExpireVersionsAfterDays 0` <br><br>Append `-ApplyToNewDocumentLibraries` parameter to apply only to new document libraries on the site:<br><br>`Set-SPOSite -Identity $siteUrl`<br>`-EnableAutoExpirationVersionTrim $false`<br>`-MajorVersions <delete major versions exceeding limit>`<br>`-ExpireVersionsAfterDays 0`<br>`-ApplyToNewDocumentLibraries` <br><br>Append `-ApplyToExistingDocumentLibraries` to apply only to existing document libraries on a site:<br><br>`Set-SPOSite -Identity $siteUrl`<br>`-EnableAutoExpirationVersionTrim $false`<br>`-MajorVersions <delete major versions exceeding limit>`<br>`-ExpireVersionsAfterDays 0`<br>`-ApplyToExistingDocumentLibraries` |
| Clear the existing version history limits set on a site and inherit Organization version limits on new document libraries created on the site. | `Set-SPOSite -Identity $siteUrl -InheritVersionPolicyFromTenant` |
| Cancel in progress update job|`Remove-SPOSiteVersionPolicyJob -Identity $siteUrl`     |

## Get progress of an in-progress settings update request

Version limits on all new libraries created in the site are immediately applied. Settings on existing libraries are asynchronously updated using a background job. 
Run the following command **to get progress of the settings update job**.

```PowerShell
Get-SPOSiteVersionPolicyJobProgress -Identity $siteUrl
```

The following table enumerates the various progress status that can be reported when attempting to update the version settings for existing libraries in a site collection:

| **Status** | **Description** |
| --- | --- |
| NoRequestFound | There are no requests on the site to set or update version settings on existing document libraries.  |
| New | The update request is New and is not processed yet. |
| InProgress | The update request is processed and the settings update request is in progress.  |
| CompleteSuccess | The update request is completed successfully.  |
| CompleteWithFailure | The update request is completed, but setting update on some document libraries has failed.  |


## Learn More:

- [Tutorial: Manage Version history limits for a Site, Library, or OneDrive account (Preview)](tutorial-manage-version-limits.md)
- Manage Version history limits for a Site using [**Set-SPOSite**](/powershell/module/sharepoint-online/set-sposite)
- Review progress of settings update on existing libraries in a Site using Get-SPOSiteVersionPolicyJobProgress
- Cancel an in-progress settings update job using Remove-SPOSiteVersionPolicyJob 



