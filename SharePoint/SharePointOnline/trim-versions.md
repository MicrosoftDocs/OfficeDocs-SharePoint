---
title: "Trim existing versions on site, library, or OneDrive"
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
description: "This article provides guidance on how to trim existing versions from site, library, or OneDrive account."

---


# Trim existing versions from site, library, or OneDrive

> [!CAUTION]
> Versions deleted using trimming jobs are permanently deleted. This deletion workflow bypasses the normal recycle bin retention and deleted versions cannot be recovered. 

As a SharePoint admin in Microsoft 365, you can queue a job to trim existing versions on a site, library, or OneDrive user account to reduce the version storage footprint of your site. You can also align existing version storage with updated version history limits by scheduling a job to trim existing versions or align existing version storage with updated Version history limits.<br> There are several things you need to consider before you decide to trim existing Version history on a site or library. Version availability is critical for recovery scenarios like undoing unwanted changes. Versions deleted using trimming jobs are permanently deleted and can't be recovered from recycle bin. 

| **Phase** | **Recommended Actions** |
| --- | --- |
| Prepare | **Evaluate your recovery objectives and target version storage use:** Determine the right trim mode and trim scope that you need to meet your organization’s recovery objectives.<br><br>**Review Impact:** Before committing to trim existing versions, you have the option to review the impact of the purge action by running a ‘What-if’ analysis operation of the selected trim mode on the specified scope. |
| Queue Job | Once you're ready to commit to a trim job, you can queue a version trimming job to asynchronously delete versions matching the criteria specified in the trim mode within a site, library, or OneDrive user account. |
| Track Progress | You can track the progress of all queued jobs to review the progress made in trimming versions.  |



:::image type="content" source="media/version-history/trimming-workflows.png" lightbox="media/version-history/trimming-workflows.png" alt-text="Diagram of trimming workflows.":::

## Review impact by running ‘What-if’ analysis 

Before committing to trim existing versions, you can review the impact of the purge action by running a ‘What-if’ analysis operation.  Running a ‘What-if’ operation will follow these steps: 

- **Generate a Version Storage usage report for a site or library**: This report can support multiple uses including, version storage use analytics or to gain key insights on the impact of applying different trimming settings. 

- **Run ‘What-If’ analysis** by setting different trimming modes to preview the changes and analyze the user and storage savings impact of applying one of the trimming modes to the version storage report csv file. 

> [!IMPORTANT]
> Depending on the size of the site or library, the job can take a few days to complete. Check the progress of the job until the status returns as “completed”.

## Version trim modes

Version trimming workflows allow you to select and apply one of the trimming modes for queuing a trim job on a site, document library, or OneDrive account.

**Manual expiration trim mode:** Evaluates the age of versions and deletes versions matching the expiration criteria. 

**Example:** In the following example, a trim job is queued to trim versions older than 60 days. On August 31, the job is picked up and it starts permanently deleting versions older than 60 days as of August 31.


  :::image type="content" source="media/version-history/manual-expiration-trim-table.png" lightbox="media/version-history/manual-expiration-trim-table.png" alt-text="Diagram of manual expiration.":::

> [!IMPORTANT]
> Known limitations of manual expiration mode
> 1. The expire trim mode doesn't delete versions created in the last 30 days. This means your input can't be less than 30 days.
> 1. The expire trim mode always deletes all versions that were created before January 1, 2023. If you want to trim versions, you can't keep any older than that. This means the value you use for the `DeleteBeforeDays` parameter should result in date after January 1, 2023.


**Manual count limit trim mode:** Deletes the oldest versions exceeding the specified count limit.

**Example:** In the example below, a trim job is queued to delete versions that exceed 50 major version counts. On August 31, the job starts permanently deleting older versions that exceed the 50 major version count limit as of August 31.

   :::image type="content" source="media/version-history/manual-count-limit-trim-table.png" lightbox="media/version-history/manual-count-limit-trim-table.png" alt-text="Diagram of manual count limit.":::


**Automatic trim mode:** Applies Automatic algorithm to delete existing versions. Depending on the version age, the job will permanently delete versions or set expiration time according to the automatic version storage algorithm.

> [!TIP]
> You can run the impact analysis of either applying the Manual Count, Expire, or Automatic trim mode to understand the version delete impact under each mode. 

## Queue trim job and track progress

The version trimming workflow uses a job to asynchronously delete versions matching the criteria specified in the trim mode.

To queue the trim job, you need to determine the scope for version deletion and the trim mode to set the criteria for existing version deletion. You can delete old file versions based on version age, count limits, or automatic algorithm for all document libraries in a site or for a specific document library.  

Once you're ready to commit to the trim, you can queue the job to asynchronously delete versions matching the trim mode criteria. You'll be able to monitor the progress of committed trim jobs to keep track of the deletion progress. 

## Trim existing versions using PowerShell

Follow these steps to trim existing versions using PowerShell.

1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).

    > [!NOTE]
    > If you installed a previous version of the SharePoint Online Management Shell, go to Add or Remove programs and uninstall **SharePoint Online Management Shell**.

1. Connect to SharePoint as a [Administrator or SharePoint Administrator](/sharepoint/sharepoint-admin-role) in Microsoft 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).
2. Run one of the following commands to trim the existing versions:

   | **Action** | **PowerShell Command** |
   | --- | --- |
   | Queue a trim job to expire versions | **Expire versions on a site:**<br><br>`New-SPOSiteFileVersionBatchDeleteJob -Identity $siteUrl -DeleteBeforeDays <days>`<br><br>**Expire versions on a library:**<br><br>`New-SPOListFileVersionBatchDeleteJob -Site $siteUrl -list $libName -DeleteBeforeDays <days>` |
   | Queue a trim job to delete versions exceeding the specified count limit | **Delete versions exceeding count limits from a site:**<br><br>`New-SPOSiteFileVersionBatchDeleteJob -Identity $siteUrl -MajorVersionLimit <delete major versions exceeding limit> -MajorWithMinorVersionsLimit <number of major versions for which all minor versions will be kept>`<br><br>**Delete versions exceeding count limits from a library:**<br><br>`New-SPOListFileVersionBatchDeleteJob -Site $siteUrl -list $libName -MajorVersionLimit <delete major versions exceeding limit> -MajorWithMinorVersionsLimit <number of major versions for which all minor versions will be kept>` |
   | Queue trim job to delete versions using the estimated automatic trimming algorithm | **Apply automatic logic to trim existing versions from a Site:**<br><br>`New-SPOSiteFileVersionBatchDeleteJob -Identity $siteUrl -Automatic`<br><br>**Apply automatic logic to trim existing versions from a library:**<br><br>`New-SPOListFileVersionBatchDeleteJob -Site $siteUrl -List $libName -Automatic` |
   | Stop further processing of an in-progress trim job<br><br>**Note:** Once the cmdlet executes successfully, all new asynchronous version deletion is stopped. Stopping a trim job doesn't impact versions that are permanently deleted when the job was in progress. | **To stop processing an in-progress site level trim     job:**<br><br>`Remove-SPOSiteFileVersionBatchDeleteJob -Identity $siteUrl`<br><br>**To stop processing an in-progress library level trim job:**<br><br>`Remove-SPOListFileVersionBatchDeleteJob -Site $siteUrl -List $libName` |
   | Get the status for a file version trimming job | **To get status of a site level trimming job:**<br><br>`Get-SPOSiteFileVersionBatchDeleteJobProgress -Identity $siteUrl`<br><br>**To get status of a library level trimming job:**<br><br>`Get-SPOListFileVersionBatchDeleteJobProgress -Site $siteUrl -List $libName` |


## Learn More

For more information, check out the following resources:

- [Tutorial: Generate Version Usage Report](tutorial-generate-version-usage-report.md).
- [Tutorial: Run 'What-If' analysis](tutorial-run-what-if-analysis.md).
- [Tutorial: Queue Trim Job](tutorial-queue-a-trim-job.md).
