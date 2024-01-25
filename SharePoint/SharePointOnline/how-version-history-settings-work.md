---
title: "How Version History settings work"
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

# How Version History settings work

You can control the version history in SharePoint at different levels—organization, site, individual library, or list level. This helps admins and site owners manage content recovery and auditing more effectively. Global and SharePoint admins in Microsoft 365 can set **Version history limits** at the organization level. These settings apply universally to all new libraries, whether on existing or new SharePoint sites, and on default libraries on new OneDrive sites. Site Owners can overwrite organization-level version settings by [configuring versions settings for sites](https://support.microsoft.com/en-us/office/enable-and-configure-versioning-for-a-list-or-library-1555d642-23ee-446a-990a-bcab618c7a37) they own. Site owners can overwrite organization or site settings by [configuring version settings for libraries and lists](/office/enable-and-configure-versioning-for-a-list-or-library-1555d642-23ee-446a-990a-bcab618c7a37) they own.

The following table summarizes the various ways of managing **Version history limits** on your document libraries:

| Area | How does it work? |
|:-----|:-----|
| Set Default **Version history limits** for new document libraries created in your organization | Default Organization **Version history limits** is set on all new document libraries created across existing and new SPO sites. |
| Set Site or Library Level **Version history limits** | If needed, Site Admins can break inheritance from the default Organization limits for an individual Site or Library. |
| Trim Existing Versions | Site Admins can choose to trim existing version history storage by running ‘What-If’ reports to understand the impact and then scheduling a timer job to execute the trimming. |

By default, Organization level settings are applied to all new libraries created in the organization. If **Version history limits** are configured on a site, the site settings will be applied to all new libraries created on the site.

:::image type="content" source="media/version-history/version-limits-new-libraries-flow.PNG" alt-text="version limits for new libraries":::

## Setting types of Version history limits

There are two Version history settings that admins can use to configure version limits for all new libraries created in their organization:

### **Automatic Setting:**

Automatic setting is recommended for optimized version storage. It combines the data recovery benefits that Version History offers while optimizing for its storage. For admins, this setting offers the most optimal storage option without having to estimate the version count or age limits needed to meet the diversified need of their end users.

### **Manual setting:**

The manual setting allows admins to set count limits on the number of major versions or to set expiration and count limits. When this option is selected, the admins can configure it in the following ways:

- **Major version limit with expiration period**: Versions are deleted after exceeding either the set number of major versions or after the set period of time. For example, if you configure a library to store 500 major versions with a 365-day expiration, the system stores no more than 500 versions, and automatically deletes any version older than 365 days.

- **Major version limits with no expiration period**: Versions are deleted after they exceed the set number of major versions. For example, if a library is configured to store 500 major versions, no more than 500 versions is stored for each file or item.
 
For more information on setting types of Version history limits see [Planning Version Storage for your Organization](sharePoint/versionHistory/planning-version-storage-for-your-organization.md).

## Setting Default Version history limits for your Organization

Organization-level version settings define the default version storage limits set on all new document libraries created across all existing or newly created SharePoint sites allowing you to set global default **Version history limits** across your organization.  

> [!IMPORTANT]
> When organizational-level version settings are updated, the new settings will be updated to all new document libraries (Base Type = 1). However, it will not update the history limits on the existing document libraries or result in the trimming of existing versions to meet the new limits. You'll need to take additional steps to [[update the settings on existing libraries on a site](#setting-version-history-limits-for-a-site)] or to [[trim existing versions](#trimming-existing-versions-from-sites-or-libraries)].

:::image type="content" source="media/version-history/tenant-version-history-limit.PNG" alt-text="tenant version history":::

## Setting Version history limits for a Site

By default, site-level **Version history limits** aren't set on individual sites as the Organization level settings define the limit that is applied to all new document libraries created in a site. However, to meet site-specific content needs, site admins can choose to set distinct site-level **Version history limits** on individual sites. This way, users can break the inheritance from organization limits on an individual site.

Site-level **Version history limits** for sites can be managed in the following ways:

| **Version history limits option** | Description |
|:-----|:-----|
|**Apply site-level Version history limits to all new and existing document libraries in a Site:** |Using this option, the **Version history limit** set on site-level is applied to all the new document libraries created in the site and creates a background request to asynchronously process the update on existing document libraries.|
|**Apply site-level Version history limits to only new document libraries created in a Site:**|Using this option, the **Version history limits** set on site-level are only applied to new document libraries created in the site. There will be no changes made to the limits on the existing document libraries or on libraries that aren't enabled for versioning in the site.|
|**Apply limits to existing document libraries only in a Site:**|Using this option allows you to update the existing document libraries on a site while allowing the new document libraries to inherit the organization-level **Version history limits**.|
|**Clear limits set on a Site:** |Existing limits on a site can be cleared to allow new document libraries created in the site to follow organization level limits. NOTE: Clearing a setting on a Site will only apply to New Document Libraries created on the site and won't impact the settings on existing doc libraries.|

> [!IMPORTANT]
>
> - Setting site-level **Version history limits** is available using PowerShell cmdlets only.
> - Updating the Site-level settings of existing document libraries of the site **will not** trim existing versions to meet the newly set limits. Additional steps will need to be taken to trim existing versions.
> - Requests to update limits on existing libraries are processed asynchronously. If a new request is issued but the old one isn't yet completed yet, it returns the message "Set-PnPSite: Can't start to set version policy for document libraries on the site because it's already in progress. Wait for it to finish or cancel it."
> - MinorVersions count only applies to the document libraries that enabled minor versioning.

:::image type="content" source="media/version-history/break-inheritance-at-site-level.PNG" alt-text="break inheritance at site level":::

## Setting Version history limits for Individual Document Library

The default **Version history limits** for new document libraries are set by either the organization-level limits or the site-level limits. If the site has its own version history limit, it means the site has broken inheritance from the organization. However, to meet specific content requirements, site admins can decide to overwrite the setting of a document library.

Here's a summary of the expected behavior when Document Libraries version expiration or count limits are updated:  

- **When Library level version expiration setting is updated**, the new expiration limit is applied to newly created versions only. Take an example of a Library with version expiration settings updated from **Never Expire** to **Expire after six months**. New version created is set to expire after six months with no impact on versions that had already been created.  

- **When Library level count limits are updated**, if existing versions exceed the new count limit, then those versions are gradually trimmed when the file is updated. Consider a library where the version count limit is initially set to 500 versions but is later reduced to 300 versions. In this scenario, if there is a file with 500 versions, each time a user updates the file, the system will gradually purge the oldest 20 versions with each new version creation until the total number of versions aligns with the updated limit of 300. It's crucial to note that when count limits are lowered, the process of version deletion occurs gradually, with up to 20 versions being removed for every new version created.  

:::image type="content" source="media/version-history/overright-version-history-limits-document-library.PNG" alt-text="overwrite version history":::

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

## Analyzing Version Storage Usage for your Site

As a SharePoint Site Administrator, you can create a CSV file of every file version on a given SharePoint Site. This report provides a deeper analysis of the current version storage usage or to see the effect of applying one of the three trimming modes before running an actual trim. The three different trimming modes are:
- Automatic
- Manual Expiration Limits
- Manual with Count Limits Only

### Understanding the file version expiration report file

The file version expiration report is in Comma-Separated Values (CSV) format. Each row corresponds to a file version, and it contains the following columns:

| **File Version Identifiers:** | Description |
|:-----|:-----|
|`WebId`|The unique identifier of the web and is a compact column <sup>1</sup>.|
|`DocId`|The unique identifier of the document and is a compact column.|
|`MajorVersion`|The major version number of the file version.|
|`MinorVersion`|The minor version number of the file version.|

| **File Version Information:** | Description |
|:-----|:-----|
|`WebUrl`|The SharePoint Url to the web and is a compact column.|
|`FileUrl`|The web relative Url to the file and is a compact column.|
|`Size`|The size of the version in bytes.|
|`ModifiedBy_UserId`|The identifier of the user who created this version and is a compact column.|
|`ModifiedBy_UserDisplayName`|The display name of the user who created this version and is a compact column'.|
|`LastModifiedDate`|The time when the version was last modified.|
|`SnapshotDate`|The time when the version became a historical version.|
|`IsSnapshotDateEstimated`|If this is set to true, then the `SnapshotDate` is a best-effort estimation. The `SnapshotDate` might be estimated if the version was snapshot before January 1, 2023.|

| **Expiration Schedule information:** | Description |
|:-----|:-----|
|`CurrentExpirationDate`|Time when the version is going to expire as it currently stands.|
|`AutomaticPolicyExpirationDate`|Time when the version would be expiring if an automatic expiration policy were to be retroactively applied, estimated on a best-effort basis.|
|`TargetExpirationDate`|Is populated to the same value as `CurrentExpirationDate`. This column is useful for any What-If analysis and batch-updating the expiration dates.|

<sup>1</sup> Compact columns are columns that won't repeat values if two consecutive rows have the same value. It will simply put empty string for the repeated records. The header for these columns will have "Compact" postfix.

You can download the report file from SharePoint and do any analysis to learn about the dataset.

There are 12 rows in this table. The first row is the header row. The compact columns are denoted with *.Compact* post-fix. The other 11 rows represent file versions, where each row represents 1 version.

:::image type="content" source="media/version-history/file-version-expiration-report.PNG" alt-text="An example file version expiration report and its column breakdown":::

Let’s go through the first file version displayed in this report.  

- `WebId`, `DocId`, `MajorVersion`, and `MinorVersion` uniquely identify this version in your SharePoint site.  

- `WebUrl` indicates the version in the [web](https://contoso.sharepoint.com), and `FileUrl` indicates that the file for this version is located at DocLib/MyDocument.docx. In other words, it is in a Document Library called `DocLib`, while the file is in the root folder of `DocLib` and is named MyDocument.docx.  

- `Size` indicates that the version takes 92,246 bytes of storage.  

- The next two columns, `ModifiedBy_UserId` and `ModifiedBy_DisplayName` indicate that the user, Michelle Harris (with user ID 6), has created this version.  

- `LastModifiedDate` indicates that the version’s content was last modified on March 13, 2023, at 22:36:09 UTC. `SnapshotDate` displays that the version became a historical version on March 20, 2023, at 16:56:51 UTC. `IsSnapshotDateEstimated` shows that `SnapshotDate` is the actual snapshot date.  

- `CurrentExpirationDate` indicates that this version is currently set to never expire. `AutomaticPolicyExpirationDate` shows that under the automatically expire policy, this version is also set to never expire. `TargetExpirationDate` indicates that if we follow this schedule for trimming, we would set this version to never expire.  

Let’s look at the third version.  

The `WebId` and `DocId` values are empty because these columns are compact columns, denoted by *.Compact* post-fix, it means they should have values. If we look for the last nonempty above that row, we find `WebId` as `4c7a58c1-01f2-4fa3-a730-44081a44f689`, and `DocId` as `18c3e09c-b5be-48e7-a754-7a2ce53e0999`.

> [!NOTE]
> All date times are represented in the round-trip format. For more information, see [Standard date and time format strings - .NET | Microsoft Learn](/dotnet/standard/base-types/standard-date-and-time-format-strings)

We can also see that the `TargetExpirationDate` is set for April 19, 2023, at 18:08:53 UTC. It means if we trim based on this schedule, we would be setting the expiration date for this version to that time. However, at the time of this documentation is written, it has passed April 19, 2023. Instead of setting the version to expire, it's deleted right away.

## Trimming Existing Versions from Sites or Libraries

As a SharePoint Site Administrator, you can trim existing versions on your sites to reduce the version storage footprint of your site or align existing version storage with updated **Version history limits** by scheduling a job to trim existing versions.

Trimming existing versions is performed in the following sequence of steps:  

**Step 1: Generate a ‘What-If File Version Expiration report’ for a Site or Library** to create an input file needed for scheduling the version trim job. This report can also be applied to gain key insights on the impact of applying different trimming settings.

**Step 2: Set trimming mode on ‘What-If File Expiration report’** by applying one of the 3 different trimming modes - Automatic, Manual Expiration Limits or Manual with Count Limits Only. You need to download the report file to your local computer and apply the provided scripts to apply one of the desired settings to the file. This step converts the ‘What-If File Expiration report’ into the ‘Schedule input file’ needed to schedule the job to trim versions.  

Optionally, apply Excel or PowerShell examples to understand the impact of the selected setting on version storage or impacted users from the selected change.

**Step 3: Schedule a job** to trim versions for your Sites or Libraries. Before scheduling the trim, you can optimize the size of ‘Schedule Input File’ generated in step by applying the scripts provided. Upload the ‘Schedule Input file’ to SharePoint on document library in the same site as the site you're deleting versions from. Lastly, schedule the trimming job. Once the job is queued, you'll be able to check the status of your trimming job. When the status shows *completed*, the version trimming task has completed.  

> [!IMPORTANT]
> - You need to be a Site Administrator of the site to generate reports and trim versions from document libraries in a site.
> - Depending on the size of the Site or Library, the job can take a few days to complete. Check the progress of the job until the status shows "completed".
