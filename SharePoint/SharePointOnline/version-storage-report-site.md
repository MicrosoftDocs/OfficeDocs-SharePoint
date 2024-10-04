---
title: "Generate version storage usage report for a site"
ms.reviewer: rekamath
ms.author: ruihu
author: maggierui
manager: jtremper
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
description: "This article provides guidance on how to generate version storage use report for a site."
---


# Generate version storage usage report for a SharePoint site

As a SharePoint admin in Microsoft 365, you can request an inventory of the versions on a site, library, or file, which can be used for various scenarios:

- Review current version storage used by existing versions.

- Understand how a version limit impacts new versions by applying the desired limits on existing versions before configuring limits.  

- Analyze the impact of trimming existing versions before scheduling a trim job.

> [!NOTE]
> Additional reporting options are available with [Microsoft Graph Data Connect](/graph/data-connect-datasets#onedrive-and-sharepoint-online).

When you run the report, a background timer job is scheduled to generate a CSV file of every file version on a given SharePoint site. The CSV file is saved to the location of your choice on the site. If you don't want site members to see the report, consider creating a folder with different permissions where only site owners can access the report.

> [!IMPORTANT]
> The file version report generation job completes asynchronously over the next few days. The time it takes for the report to complete depends on the size of your library or site. For smaller sites or libraries, it takes over 24 hours to complete. For larger ones, it takes a few days to complete. 
>
> While the job is being processed, you can see the report file being gradually populated. Do not update the file during this time. It will cause the job to fail. Check the progress of the report generation to confirm that the report is fully populated and ready to process. 
>
> If you wish to cancel an in-progress report generation, you may simply delete the report file. 


## Report format

The file version expiration report is in Comma-Separated Values (CSV) format. Each row corresponds to a file version and it contains the following columns:

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
|`ModifiedBy_UserDisplayName`|The display name of the user who created this version and is a compact column.|
|`LastModifiedDate`|The time when the version was last modified.|
|`SnapshotDate`|The time when the version became a historical version.|
|`IsSnapshotDateEstimated`|If this identifier is set to true, then the `SnapshotDate` is a best-effort estimation. The `SnapshotDate` might be estimated if the version was snapshot before January 1, 2023.|

| **Expiration Schedule information:** | Description |
|:-----|:-----|
|`CurrentExpirationDate`|Time when the version will expire as it currently stands.|
|`AutomaticPolicyExpirationDate`|Time when the version would be expiring if an automatic expiration policy were to be retroactively applied, estimated on a best-effort basis.|
|`TargetExpirationDate`|Is populated to the same value as `CurrentExpirationDate`. This column is useful for any What-If analysis and batch-updating the expiration dates.|

<sup>1</sup> Compact columns are columns that won't repeat values if two consecutive rows have the same value. It puts empty string for the repeated records. The header for these columns have "Compact" postfix.

## How to generate site version storage usage report for site, OneDrive or library

Follow these steps to manage version history limits for a site by using PowerShell.

1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).

    > [!NOTE]
    > If you installed a previous version of the SharePoint Online Management Shell, go to Add or remove programs and uninstall **SharePoint Online Management Shell**.

1. Connect to SharePoint as a [SharePoint Administrator](/sharepoint/sharepoint-admin-role) in Microsoft 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).
2. Run one of the following commands to generate a version storage usage report:

| **Action** | **PowerShell Command** |
| --- | --- |
| Generate a version storage usage report for a site or OneDrive account | `New-SPOSiteFileVersionExpirationReportJob -Identity $siteUrl -ReportUrl $reportUrl` |
| Track progress of the job to generate report for a site or OneDrive account | `Get-SPOSiteFileVersionExpirationReportJobProgress -Identity $siteUrl -ReportUrl $reportUrl` |
| Generate a version storage usage report for a library | `New-SPOListFileVersionExpirationReportJob -Site $siteUrl -List $libName -ReportUrl $reportUrl` |
| Track progress of the job to generate report for a library | `Get-SPOListFileVersionExpirationReportJobProgress -Site $siteUrl -List $libName -ReportUrl $reportUrl` |

## Learn More

1. [Tutorial: Generate Version Usage Report](tutorial-generate-version-usage-report.md)
1. [Tutorial: Run 'What-If' Analysis](tutorial-run-what-if-analysis.md)