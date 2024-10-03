---
title: "Tutorial: Manage version history limits on a site, library, or OneDrive account"
ms.reviewer: rekamath
ms.author: ruihu
author: maggierui
manager: jtemper
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
description: "This article provides guidance on how to manage Version history limits for a site, library, or OneDrive account."

---


# Tutorial: Manage version history limits for a site, library, or OneDrive account

In this tutorial, you will learn how to manage the version history limits for a site, document library, or OneDrive account. You will learn how to:

- Set Version history limits settings on the site. 
- Stop an in-progress settings update job. 

## Before you begin

- Review your **organization’s recovery objectives** and **version storage use quota targets** along with the **site-specific version storage needs** to evaluate if a break of inheritance of version settings at site, library, or OneDrive account level is needed.

- If needed **run an impact analysis** with the desired setting, to understand the impact the new setting would have using current version storage usage patterns.
- For setting site level version limits, evaluate the scope of document libraries that should be updated. Depending on business need, you can choose one of the following:
    - Update new libraries only without impacting existing library settings.
    - Update existing libraries only and inherit organization default settings for new libraries.
    - Update both existing and all new libraries for consistent version storage at the site level.

## Set version limits for a site  

You can set version limits on a site by running the [**Set-SPOSite**](/powershell/module/sharepoint-online/set-sposite) command to break inheritance from the organization version history limits.  

- Use the `–ApplyToNewDocumentLibraries` parameter to apply the changes only to new libraries created in the site. 

- Use the `–ApplyToExistingDocumentLibraries` to only update the Version history limits on existing libraries on a site. Any new library created inherits the default organization limits. 

### Example: Apply automatic version history limits to all document libraries on a site

Run the following commands to **apply Automatic setting** to all document libraries on a site.

```PowerShell
Set-SPOSite -Identity https://contoso.sharepoint.com/sites/site1 -EnableAutoExpirationVersionTrim $true  
```

### Example: Apply automatic version history limits to new document libraries on a site

In the following example, Automatic Version history limits are applied to all new document libraries created on the site. The settings on existing libraries will not be impacted.
  
```PowerShell
 Set-SPOSite -Identity https://contoso.sharepoint.com/sites/site1 -EnableAutoExpirationVersionTrim $true -ApplyToNewDocumentLibraries
```

### Example: Apply manual setting with count and time version history limits to existing libraries only on a site

In the following example, Version history limits of all existing libraries on a site are updated to Manual Version history limits.

```PowerShell
Set-SPOSite -Identity https://contoso.sharepoint.com/sites/site1 -EnableAutoExpirationVersionTrim $false -MajorVersionLimit 500 -ExpireVersionsAfterDays 30 -ApplyToExistingDocumentLibraries
```

## Cancel an in-progress request to update version history limits on existing libraries

If required, you can cancel the update job that is currently `<InProgress>` using the `Remove-SPOSiteVersionPolicyJob`. 

> [!NOTE]
> Cancelling the job doesn't revert the change for document libraries where the update is already processed.  

In the example below, the in-progress job to update settings on site will be stopped. 

```PowerShell
Remove-SPOSiteVersionPolicyJob -Identity https://contoso.sharepoint.com/sites/site1
```

## Learn More

- Track progress of version settings update request for existing document libraries on a site using [Get-SPOSiteVersionPolicyJobProgress](/powershell/module/sharepoint-online/get-spositeversionpolicyjobprogress).
- Cancel further processing of version settings update on existing document libraries on the site collection using [Remove-SPOSiteVersionPolicyJob](/powershell/module/sharepoint-online/remove-spositeversionpolicyjob).
