---
title: "How Version History Limits for Document Libraries Work"
ms.reviewer: 
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
description: "This article provides guidance on how Version History settings work."

---

# How Version History Limits for Document Libraries Work

You can control the version history in SharePoint at different levels—organization, site, individual library, or list level. This helps admins and site owners manage content recovery and auditing more effectively. Global and SharePoint admins in Microsoft 365 can set **Version history limits** at the organization level. These settings apply universally to all new libraries, whether on existing or new SharePoint sites, and on default libraries on new OneDrive sites. Site Owners can overwrite organization-level version settings by [configuring versions settings for sites](https://support.microsoft.com/en-us/office/enable-and-configure-versioning-for-a-list-or-library-1555d642-23ee-446a-990a-bcab618c7a37) they own. Site owners can overwrite organization or site settings by [configuring version settings for libraries and lists](/office/enable-and-configure-versioning-for-a-list-or-library-1555d642-23ee-446a-990a-bcab618c7a37) they own.

The following table summarizes the various ways of managing **Version history limits** on your document libraries:

| Area | How does it work? |
|:-----|:-----|
| **Set Default **Version history limits** for new document libraries created in your organization** | Default Organization **Version history limits** is set on all new document libraries created across existing and new SPO sites. |
| **Set Site or Library Level **Version history limits** | If needed, Site Admins can break inheritance from the default Organization limits for an individual Site or Library. |
| **Report on Version Storage on a site** | Run a report to analyze version storage use of existing versions, understand how a version limit works before configuring limits or analyze the impact of trimming existing versions prior to scheduling trim job. |
| **Trim Existing Versions** | Site Admins can choose to trim existing version history storage by running ‘What-If’ reports to understand the impact and then scheduling a timer job to execute the trimming. |

By default, Organization level settings are applied to all new libraries created in the organization. If **Version history limits** are configured on a site, the site settings are applied to all new libraries created on the site.

:::image type="content" source="media/version-history/version-limits-new-libraries-flow.png" alt-text="version limits for new libraries":::

## Types of Version limits

There are two Version history settings that admins can use to configure version limits for all new libraries created in their organization:

### **Automatic Setting:**

Automatic setting is recommended for optimized version storage. It combines the data recovery benefits that Version History offers while optimizing for its storage. For admins, this setting offers the most optimal storage option without having to estimate the version count or age limits needed to meet the diversified need of their end users.

### **Manual setting:**

The manual setting allows admins to set count limits on the number of major versions or to set expiration and count limits. When this option is selected, the admins can configure it in the following ways:

- **Major version limit with expiration period**: Versions are deleted after exceeding either the set number of major versions or after the set period of time. For example, if you configure a library to store 500 major versions with a 365-day expiration, the system stores no more than 500 versions, and automatically deletes any version older than 365 days.

- **Major version limits with no expiration period**: Versions are deleted after they exceed the set number of major versions. For example, if a library is configured to store 500 major versions, no more than 500 versions is stored for each file or item.
 
For more information on setting types of Version history limits, see [Planning Version Storage for your Organization](sharePoint/versionHistory/planning-version-storage-for-your-organization.md).

## Set Default Version limits for your Organization

Organization-level version settings define the default version storage limits set on all new document libraries created across all existing or newly created SharePoint sites allowing you to set global default **Version history limits** across your organization.  

> [!IMPORTANT]
> When organizational-level version settings are updated, the new settings will be updated to all new document libraries (Base Type = 1). However, it will not update the history limits on the existing document libraries or result in the trimming of existing versions to meet the new limits. You'll need to take additional steps to [[update the settings on existing libraries on a site](#setting-version-history-limits-for-a-site)] or to [[trim existing versions](#trimming-existing-versions-from-sites-or-libraries)].

Take an example of Contoso with an existing Marketing site with a set of libraries set to 500 major version limits. When the admin updates the organization version limits to ‘Automatic’ library, version limits for document libraries will be set in the following ways:

- **Library version limits on existing Marketing Site**: Version limits on all new libraries created in the Marketing site will be set to the organization limits of Automatic. Version limits on existing libraries remain unchanged that is, limits won't be updated to Automatic.  

- **Library version limits on new Legal Site**: When a new Legal site is created, version limits on all libraries created in the legal site set to the organization version limits.

:::image type="content" source="media/version-history/break-inheritance-at-site-level.png" alt-text="tenant version history":::

## Set Version limits for a Site

By default, site-level **Version history limits** aren't set on individual sites as the Organization level settings define the limit that is applied to all new document libraries created in a site. However, to meet site-specific content needs, site admins can choose to set distinct site-level **Version history limits** on individual sites. This way, users can break the inheritance from organization limits on an individual site.

Site-level **Version history limits** for sites can be managed in the following ways:

| **Version history limits option** | Description |
|:-----|:-----|
|**Apply site-level Version history limits to all new and existing document libraries in a Site:** |Using this option, the **Version history limit** set on site-level is applied to all the new document libraries created in the site and creates a background request to asynchronously process the update on existing document libraries.|
|**Apply site-level Version history limits to only new document libraries created in a Site:**|Using this option, the **Version history limits** set on site-level are only applied to new document libraries created in the site. There will be no changes made to the limits on the existing document libraries or on libraries that aren't enabled for versioning in the site.|
|**Apply limits to existing document libraries only in a Site:**|Using this option allows you to update the existing document libraries on a site while allowing the new document libraries to inherit the organization-level **Version history limits**.|
|**Clear limits set on a Site:** |Existing limits on a site can be cleared to allow new document libraries created in the site to follow organization level limits. NOTE: Clearing a setting on a Site will only apply to New Document Libraries created on the site and won't impact the settings on existing doc libraries.|

Take an example of Contoso where organizational version limits are set to Automatic, no version limits set for Marketing Site and Legal Site. Suppose Site Administrator of Legal site sets the site version history limit to 500 major version count limit for new and existing libraries. Library version limits for Contoso will be set in the following ways:

- **Library version limits on Marketing Site**: Since there's no site level version limit set for Marketing site, organization limit of Automatic will be set on all new libraries created in marketing site.  

- **Library version limits on Legal Site**: Since version limits are set for Legal site, all new libraries are set to store 500 major versions.

:::image type="content" source="media/version-history/set-version-limits-for-a-site.png" alt-text="break inheritance at site level":::

> [!IMPORTANT]
>
> - Setting site-level **Version history limits** is available using PowerShell cmdlets only.
> - Updating the Site-level settings of existing document libraries of the site **will not** trim existing versions to meet the newly set limits. Additional steps will need to be taken to trim existing versions.
> - Requests to update limits on existing libraries are processed asynchronously. If a new request is issued but the old one isn't yet completed yet, it returns the message "Set-PnPSite: Can't start to set version policy for document libraries on the site because it's already in progress. Wait for it to finish or cancel it."
> - MinorVersions count only applies to the document libraries that enabled minor versioning.

## Set Version limits for Individual Document Library

The default **Version history limits** for new document libraries are set by either the organization-level limits or the site-level limits. If the site has its own version history limit, it means the site has broken inheritance from the organization. However, to meet specific content requirements, site admins can decide to overwrite the setting of a document library.

Here's a summary of the expected behavior when Document Libraries version expiration or count limits are updated:  

- **When Library level version expiration setting is updated**, the new expiration limit is applied to newly created versions only. Take an example of a Library with version expiration settings updated from **Never Expire** to **Expire after six months**. New version created is set to expire after six months with no impact on versions that had already been created.  

- **When Library level count limits are updated**, if existing versions exceed the new count limit, then those versions are gradually trimmed when the file is updated. Consider a library where the version count limit is initially set to 500 versions but is later reduced to 300 versions. In this scenario, if there's a file with 500 versions, each time a user updates the file, the system will gradually purge the oldest 20 versions with each new version creation until the total number of versions aligns with the updated limit of 300. It's crucial to note that when count limits are lowered, the process of version deletion occurs gradually, with up to 20 versions being removed for every new version created.  

:::image type="content" source="media/version-history/overright-version-history-limits-document-library.png" alt-text="overwrite version history":::

> [!CAUTION]
> Versions deleted either under the automatic setting or due to versions' age or count exceeded the limits set by the admin are marked for permanent deletion. These will not be available to restore from the recycle bin.

The important points to note are as follows:

- Default Workflow: The following is the default workflows for document library **Version history limits**:
    - Default organization Level Limits: The default **Version history limits** for your organization will be set to Manual mode with **500 Major Version Limit** set to **Never Expire**.
    - Default Site or Library Level Limits: By default, there will be no **Version history limits** set on individual sites as new document libraries inherit the organization level limits.

- Organizational-level version limit settings can be used to configure version settings on libraries only. List version settings, creation of major and minor versions or content approval workflows need to be [configured at individual library or list level](/office/enable-and-configure-versioning-for-a-list-or-library-1555d642-23ee-446a-990a-bcab618c7a37).

- Changes made to organization-level settings apply to new libraries created since the change was made. The ability to apply the setting to existing document libraries at the organization-level isn't yet released. The new settings won't be applied to existing libraries or to versions that were already created.

- A version's expiration date is determined from library version settings and is stamped on the version when a version is created. If expiration settings at the library are modified, the expiration date on the existing versions of a file won't change.

- When a document with versions is subject to retention settings, the retention of versions is determined by the configured retention setting. In other words, the retention setting always wins, whether that be a deletion or hold policy. [Learn about retention for SharePoint and OneDrive - Microsoft 365 Compliance | Microsoft Docs](/microsoft-365/compliance/retention-policies-sharepoint).
 
## Trim Existing Versions from Sites or Libraries

As a SharePoint Site Administrator, you can schedule a job to trim existing versions on your sites to reduce the version storage footprint of your site or align existing version storage with updated version history limits by scheduling a job to trim existing versions. There are several things you need to consider before you decide to trim existing version history on a site or library. Version availability is critical for recovery scenarios like undoing unwanted changes. Versions deleted using scheduled jobs are permanently deleted. This deletion bypasses the normal recycle bin and deleted versions can't be recovered.

SharePoint supports two ways to trim existing versions on a site or library. Use the following information to help you choose which trim method is best for your use case.

| **Use Case** | **Recommended approach** | **Description** |
|:-----|:-----|:-----|
| Review impact before scheduling version trim job.<br> <br> Compare different trimming modes for desired savings and acceptable impact. | Analyze and Trim (2-Step Trimming Workflow)  | The 2-step trim workflow allows you to assess the impact of version trimming prior to scheduling the trim job. <br> <br> You'll be able to generate a version storage use report, compare the storage savings and user impact of different trimming modes like Manual Count or Expiration limits, Automatic or other custom trimming logic, apply a desired trimming mode on the report and finally queue the job to trim versions. <br> <br> **Trimming Modes supported:** <br> <br> <li> Manual Expiration <br> <li> Manual Count <br> <li> Automatic <br> <li> Custom  |
| Trim versions without analyzing impact. | Batch Trim (1-Step Trimming Workflow) |Batch trim workflow allows you purge versions older than specified period. Use the 1-step trim workflow only if you're comfortable with directly applying the trimming and don't need to review impact before committing to the trim job. <br> <br> **Trimming Modes supported:** <br> <br> <li> Manual Expiration |

:::image type="content" source="media/version-history/trimming-workflows.png" alt-text="trimming workflows":::

The following sections describe the different trimming methods:  

### Analyze and trim (2-step version trimming method)

Trimming existing versions is performed in the following sequence of steps:  

**Step 1: Generate a Version Storage Use report for a Site or Library** to create an input file needed for scheduling the version trim job. This report can also be applied to gain key insights on the impact of applying different trimming settings. For trimming workflow, this report serves the purpose of an input file needed to schedule version trim job.

**Step 2: Run ‘What-If’ analysis** to preview the changes and analyze the user and storage savings impact of applying one of the trimming modes to the version storage report csv file.  

> [!IMPORTANT]
> - You need to be a Site Administrator of the site to generate reports and trim versions from document libraries in a site.
> - Depending on the size of the Site or Library, the job can take a few days to complete. Check the progress of the job until the status shows "completed".

**Step 3: Set the desired trimming mode and Schedule a job** to trim versions for your Sites or Libraries.

### Batch trim older versions (1-step trimming method)

The 1-step batch trim method skips the analysis phase allowing you to directly schedule a trim job to delete versions matching the specified criteria. This trimming workflow only supports the ‘Manual Expiration’ trim mode that allows you to store versions created within a specified period by scheduling a job to asynchronously delete versions older than the specified number of days.

Here's the sequence of steps for this method:

1. **Prepare to trim:** Determine the desired scope for version deletion - You can delete old file versions for all document libraries in a site or for a specific document library.  Determine the minimum age (in days) for the file versions you want to delete. For example, on May 1, 2023, if you choose to delete file versions that are at least 30 days old, then the versions snapshotted before April 1, 2023 (your target date), will be deleted.

1. **Schedule batch delete of Versions:** Schedule a job to asynchronously delete versions older than the specified number of days.

The following are the known limitations.

- The API doesn't delete versions created in the last 30 days. This means your input to the API can't be less than 30 days.

- The API always deletes all versions that were created before January 1, 2023. If you want to trim versions, you can't keep any older than that. This means the value you use for the `DeleteBeforeDays` parameter should result in date after January 1, 2023.

### Trim Modes

Version trimming workflows allow you to select and apply one of the trimming modes for scheduling a trim job on a site or library.

- **Manual Expiration:** The manual expiration mode sets the target expiration date on matching versions with the specified value.
    - With the 2-step trim workflow, the ‘TargetExpirationDate’ of matching versions is set to the specified value.
    - With the 1-step trim workflow, the trim job is scheduled to delete matching versions.

:::image type="content" source="media/version-history/manual-expiration-trim-table.png" alt-text="manual expiration":::

- **Manual Count Limit:** The manual count limit trim mode sets the target expiration date on oldest versions exceeding specified count limit to be deleted right away.

:::image type="content" source="media/version-history/manual-count-limit-trim-table.png" alt-text="manual count limit":::

- **Automatic:** The automatic trim mode sets the target expiration date based on the Automatic logic.

- **Custom:** The 2-step trim mode allows you to update the target expiration date by manually editing the report file and scheduling the trim job.

## Learn More

For more information, check out the following resources:

- [Tutorial: Generate and Analyze Version Usage Report for SharePoint Site]()
- [Tutorial: Run ‘What-If’ analysis on Version Storage Report File]()
- [Tutorial: Perform a 2-Step Trim by analyzing impact & scheduling trim]()
- [Tutorial: Perform a 1-Step trim by scheduling batch trim job]()
