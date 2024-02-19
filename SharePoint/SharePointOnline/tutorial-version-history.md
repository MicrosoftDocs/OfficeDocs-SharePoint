---
title: "Tutorial - Version Usage, What-If Analysis, and Trim Techniques"
ms.reviewer: 
ms.author: serdars
author: serdars
manager: serdars
recommendations: true
ms.date: 01/31/2023
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
description: "This article provides guidance on Version Usage, What-If Analysis, and Trim Techniques."

---

# Tutorials

## Tutorial: Generate and Analyze Version Usage Report for SharePoint Site

By understanding version storage on a site, you can better optimize the version history settings to meet your organization’s recovery objectives and manage storage costs.

This tutorial shows you how to generate a version storage use report and analyze it to better understand the version storage footprint of the site. The report can also be used to perform ‘What-if’ analysis of applying different version limits or trimming existing versions.  

In this tutorial we'll cover how to:

- Generate Version storage use report file for Site or Library.
- Check progress of report generation.
- Understand the report file.
- Analyze version storage use using Excel or PowerShell.

### Generate Version Use Report for Sites or Library

Before you begin, determine the **Report Scope** (Site or Document Library); **Report Location** (a location within a SharePoint document library that you want to save the report to). The Report Location tells us where to generate a report file, and it should be a link to a file and there can't be a file with the same name.

- Here’s an example of the PowerShell script that generates a **site-scoped** report at the [report location](https://contoso.sharepoint.com/SharedDocuments/SiteReport.csv).  

> [!NOTE]
> The report location is within a SharePoint document library.

:::image type="content" source="media/version-history/powershell-site-scoped.png" alt-text="powershell site scoped":::

:::image type="content" source="media/version-history/powershell-site-scoped-1.png" alt-text="powershell site scoped 1":::

- Here’s a PowerShell script that generates a **library-scoped** report at the **report location**, `https://contoso.sharepoint.com/Shared Documents/SiteReport.csv.` Ensure that the report location is within a SharePoint document library.

:::image type="content" source="media/version-history/library-scoped-report-powershell.png" alt-text="library scoped report powershell":::

> [!IMPORTANT]
> The file version report generation job is complete asynchronously over the next few days. The completion time of the report depends on the size of your library or site.
>
> While the job is processing, you will see the report file being gradually populated. Do not update the file during this time, as it may lead to job failure. Check the progress of the report generation to ensure that the report is fully populated and ready to process.
>
> If you want to cancel a report generation in progress, you can simply delete the report file.

### Check Report Generation Progress

- Here’s a PowerShell script that allows you to check if your **site scoped report** is fully populated and ready to be analyzed.

:::image type="content" source="media/version-history/site-scoped-report.png" alt-text="site scoped report":::

- Here’s a PowerShell script that allows you to check if your **library scoped report** is fully populated and ready to be analyzed.

:::image type="content" source="media/version-history/library-scoped-report-analysed.png" alt-text="library scoped report analysed":::

- The cmdlet returns in JSON format, and the value will look like one of the following values:

:::image type="content" source="media/version-history/json-powershell.png" alt-text="json powershell":::

### Understand Version Report File

- Here’s an example of file version expiration report and its column breakdown.

:::image type="content" source="media/version-history/file-version-expiration-report.png" alt-text="file version expiration report":::

There are 12 rows in this table. The first row is the header row. The compact columns are denoted with *.Compact* post-fix. The other 11 rows represent file versions, where each row represents 1 version.

Let’s go through the first file version displayed in this report.  

- `WebId`, `DocId`, `MajorVersion`, and `MinorVersion` uniquely identify this version in your SharePoint site.  

- `WebUrl` indicates the version in the [web](https://contoso.sharepoint.com), and `FileUrl` indicates that the file for this version is located at DocLib/MyDocument.docx. In other words, it is in a Document Library called `DocLib`, while the file is in the root folder of `DocLib` and is named MyDocument.docx.  

- `Size` indicates that the version takes 92,246 bytes of storage.  

- The next two columns, `ModifiedBy_UserId` and `ModifiedBy_DisplayName` indicate that the user, Michelle Harris (with user ID 6), has created this version.  

- `LastModifiedDate` indicates that the version’s content was last modified on March 13, 2023, at 22:36:09 UTC. `SnapshotDate` displays that the version became a historical version on March 20, 2023, at 16:56:51 UTC. `IsSnapshotDateEstimated` shows that `SnapshotDate` is the actual snapshot date.  

- `CurrentExpirationDate` indicates that this version is currently set to never expire. `AutomaticPolicyExpirationDate` shows that under the automatically expire policy, this version is also set to never expire. `TargetExpirationDate` indicates that if we follow this schedule for trimming, we would set this version to never expire.  

Let’s look at the third version.  

The `WebId` and `DocId` values are empty because these columns are compact columns, denoted by *.Compact* post-fix, it means they should have values. If we look for the last nonempty above that row, we find `WebId` as `4c7a58c1-01f2-4fa3-a730-44081a44f689`, and `DocId` as `18c3e09c-b5be-48e7-a754-7a2ce53e0999`.

We can also see that the `TargetExpirationDate` is set for April 19, 2023, at 18:08:53 UTC. It means if we trim based on this schedule, we would be setting the expiration date for this version to that time. However, at the time of this documentation is written, it has passed April 19, 2023. Instead of setting the version to expire, it's deleted right away.

> [!NOTE]
> All date times are represented in the round-trip format. For more information, see [Standard date and time format strings - .NET | Microsoft Learn](/dotnet/standard/base-types/standard-date-and-time-format-strings)

### Analyze Version Storage for Sites

After configuring the `TargetExpirationDate` values for your report, you can choose to perform deeper analysis to see the impact of the trimming before running an actual trim. You can perform this analysis independently, or alternatively, we provide two recommended options for your analysis.  

## Option one: Analyze the report using Excel

Open the shared Excel workbook **AnalyzeReportFile_Template.xlsx**. You can find the following worksheets in it.  

- **Configuration**: Use this worksheet to set the date range for generating the different report views.
- **Dataset**: This is the raw dataset imported from the report file. Various reporting summary views are constructed from this dataset.
- **Preset Reports**: The following is a list of preset views that can be used to understand the impact of applying the selected setting on versions stored in the site:
    - **Summary**: Analyze the current state of version storage for this site and deleted version distribution under the new settings.
    - **Impacted Users**: Review the users whose versions would be impacted under the new settings.
    - **Version Count**: A table and graph showing the numbers of versions that will be available over time under the current schedule and the number of versions that will be available under the new schedule.
    - **Size of Versions Expired**: Compare the size of versions that will be deleted over time under the current schedule and the number of versions that will be available under the new schedule.
    - **File Level Analysis**: Review file level version deletions under the new settings.  

Follow these steps to populate the workbook:

1. On the **Configuration** worksheet, enter the full path to the What-If report file in **Cell B3**.

:::image type="content" source="media/version-history/analyze-version-step1.png" alt-text="configuration worksheet":::

2. If you want to change the date range of graphs in **Number of Versions Available** worksheet, or **Size of Versions Expired** worksheet, change the corresponding values in Cells B6, B7, B10, and/or B11. This is optional.  

:::image type="content" source="media/version-history/analyze-version-step2.png" alt-text="analyze version configuration":::

3. At the top of Excel, select **Data** tab, and in the Ribbon, select **Refresh All** button.

:::image type="content" source="media/version-history/analyze-version-step3.png" alt-text="analyze version data tab":::

4. On the **Calculations** worksheet, autofill the **Number of Versions** and **Number of Versions Remaining After Deletion** columns.

:::image type="content" source="media/version-history/analyze-version-step4-a.png" alt-text="Calculations worksheet 1":::

:::image type="content" source="media/version-history/analyze-version-step4-b.png" alt-text="Calculations worksheet 2":::

5. On the **Impacted Users** worksheet, autofill the **Number of Versions Will be Deleted** column.

:::image type="content" source="media/version-history/analyze-version-step5.png" alt-text="Impacted Users worksheet":::

All worksheets should now be up to date. You can check the information you're interested in.

## Option two: Analyze the report using PowerShell

1. Save the script as a file named **AnalyzeReportFile.ps1.**

:::image type="content" source="media/version-history/analyse-report-file.png" alt-text="AnalyzeReportFile":::

2. Open PowerShell 7 and run the following command, replacing the placeholder values with the appropriate values.  

:::image type="content" source="media/version-history/analyze-report-powershell-command.png" alt-text="analyze report powershell command":::

3. The output displays four tables:

- **Current Expiration Schedule:** this table contains a time-series summary for your versions as they are. It has the following columns:
    1. Date: the first column represents the date.
    1. NumberOfVersionsAvailable: the number of versions available on that date under the current schedule.  
    1. NumberOfVersionsExpired: the number of versions expired on that date under the current schedule.  
    1. SizeOfVersionsExpiredMB: the size of versions expired on that date under the current schedule.  

:::image type="content" source="media/version-history/current-expiration-schedule.png" alt-text="Current Expiration Schedule":::

- **Target Expiration Schedule:** this table is the same as Current Expiration Schedule but reflects the updated schedule instead. This is only helpful if you want to test out different expiration scenarios by changing the **TargetExpirationDate** column in the file version expiration report.  

:::image type="content" source="media/version-history/target-expiration-schedule.png" alt-text="Target Expiration Schedule":::

- **Files with Fewer Than 10 Versions:** a list of the URLs, and the number of versions before and after the deletion for those files whose number of versions is fewer than 10 after immediate deletion (but was more than 10 before the immediate deletion).  

:::image type="content" source="media/version-history/files-with-fewer-than-10-versions.png" alt-text="Files with Fewer Than 10 Versions":::

- **Users Impacted:** the users whose versions would be immediately deleted.

:::image type="content" source="media/version-history/users-impacted.png" alt-text="Users Impacted":::

Optionally, you can adjust the parameters:

- `TimelineStartDate`: the starting date for Table 1 and 2 above.
- `TimelineStepDays`: the number of days in between rows for Table 1 and 2 above.  
- `TimelineNumSteps`: the number of rows to calculate for Table 1 and 2 above.  
- `ShowFilesWithFewerThanNVersions`: the threshold for the number of versions in Table 3 above.

## Tutorial: Run ‘What-If’ analysis on Version Storage Report File

In this tutorial, we'll cover how to:

- Run impact analysis of Automatic setting.
- Run impact analysis of Manual Expiration.
- Run impact analysis of Manual Count limits.

Download the report file to your local computer and leverage the provided scripts to apply the desired setting to the file - Automatic, Manual Expiration Limits or Manual with Count Limits Only. If needed, you could leverage PowerShell and Excel examples to understand the impact of the selected setting on version storage or impacted users.

- Here's an example of PowerShell script you could apply to generate a What-If Report file that applies the **Automatic Expiration**  policy on the report file `C:\Report.csv`.  

:::image type="content" source="media/version-history/expiration-automation.png" alt-text="expiration automation":::

- Here's an example of PowerShell script to generate a What-If Report file. It applies **Manual Expiration** with expire-after days set to 30 on the report file `C:\Report.csv`.  

:::image type="content" source="media/version-history/manual-expiration.png" alt-text="manual expiration":::

- Here's an example of PowerShell script to generate a What-If Report file, It applies a **Manual with Count Limits** policy with major version limit set to 50 on the report file `C:\Report.csv`.

:::image type="content" source="media/version-history/manual-with-count-limits-a.png" alt-text="manual with count limits-a":::

:::image type="content" source="media/version-history/manual-with-count-limits-b.png" alt-text="manual with count limits-b":::

## Tutorial: Queue a Trim Job for a Site or Document Library

In this tutorial we will cover:

- Schedule a batch trim job from a site or library.
- Stop an in-progress batch deletion job.
- Check progress of your batch deletion job.

### Prerequisites

1. Determine the **Scope [Site, Library]** for version deletion - You can delete old file versions for all document libraries in a site or for a specific document library.
1. Determine the minimum **age (in days)** for the file versions you want to delete. For example, on May 1, 2023, if you choose to delete file versions that are at least 30 days old, then the versions snapshotted before April 1, 2023 (your target date), will be deleted.

### Queue Trim Job

Follow the PowerShell examples below to start deleting old file versions. Make sure you're a site administrator.

**Example 1. Queue trim job to delete versions on all libraries on a Site.**

To delete versions that are older than 180 days old for all document libraries in the [site collection](https://contoso.sharepoint.com).

:::image type="content" source="media/version-history/batch-trim-all-lib.png" alt-text="batch trim all library":::

**Example 2. Batch trim versions on a single library on a site.**

To delete versions that are older than 30 days in document library ‘Documents’ in the [site collection](https://contoso.sharepoint.com).

:::image type="content" source="media/version-history/batch-trim-single-lib.png" alt-text="batch trim single library":::

Once the cmdlet executes successfully, versions that match your criteria is deleted asynchronously in batches in the upcoming days.

### Cancel an in-progress Batch Trim Job

If needed, you can cancel an in-progress batch trim job. Once the cmdlet executes successfully, asynchronous version deletion is stopped, but versions that have already been deleted will still be gone.

**Example 1. Stop additional batch deletion on site scoped trim job.**

To stop the more batch deletion for the [site collection](https://contoso.sharepoint.com).

:::image type="content" source="media/version-history/batch-deletion-site-scoped.png" alt-text="batch deletion site scoped":::

**Example 2. Stop additional batch deletion on library scoped trim job.**

To stop the more batch deletion for the document library Documents in [site collection](https://contoso.sharepoint.com).

:::image type="content" source="media/version-history/batch-deletion-lib-scoped.png" alt-text="batch trim library scoped":::

