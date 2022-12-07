---
title: "Migration Manager File Share migration reports"
ms.reviewer:
ms.author: jhendr
author: JoanneHendrickson
manager: serdars
recommendations: true
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.subservice: sharepoint-migration
ms.localizationpriority: medium
mscollection:
- SPMigration
- M365-collaboration
- m365initiative-migratetom365
search.appverid: MET150
description: "Learn about the reports available when using Migration Manager to migrate on-premises file shares to Microsoft 365."
---

# Migration Manager: File share migration reports

When migrating your on-premises file shares to Microsoft 365, Migration Manager generates log files, summary and task-level reports, and a performance report.  Use these reports to help manage, audit, and troubleshoot your migration process.

>[!Note]
>These reports are for file share migration only. For cloud migrations, learn more at: [Cloud migration reports and errors in Migration Manager](mm-cloud-reports.md)

|Type|Report|
|:-----|:-----|:-----|
|Task level|[Item Summary](#item-summary)|
|Task level|[Item Failure Report](#item-failure-report)|
|Task level|[Item Report](#item-report)|
|Task level|[Scan Summary](#scan-summary)|
|Task level|[Structure Report](#structure-report)|
|Task level|[Structure Failure Report](#structure-failure-report)|
|Task level|[Structure Failure Summary](#structure-failure-summary)|
|Performance report|[Performance Report](#performance-report)|

## How to view the reports

These reports can be viewed while the migration is taking place or after the jobs are complete.

**Viewing task level reports:**

1. To see the report on a task, select the task name from the list. A panel will appear to the right.
2. Select **Download task report**. The report will download after the task is complete.

**Viewing summary reports:**

1. Select one or more completed tasks from the list. Click **Summary report**.
2. An aggregate summary report will be downloaded to your computer.

## Download detailed task level reports via Powershell

To download task level reports, run the following Powershell cmdlet.

1. [Download the powershell script](https://spmt.sharepointonline.com/download/ReportAggregator.zip) and extract the files.
2. **Run** *aggregatereports.ps1*.
3. Enter your tenant credentials.
4. From the Task Filter pane, select how you want to filter your reports:

   ![Screen to choose how to filter Migratino Manager reports](media/mm-reports-powershell-filter.png).

5. The aggregated report zip file will be found in the same folder as the PowerShell cmdlet.

## Summary Report

The summary report is an aggregate report that lists all successfully completed, failed, and in-progress tasks.

- **Aggregate Summary Report.csv.** This report contains a single row of data that gives the total picture; including total size, number of files migrated, duration.

When assessing your migration jobs, we recommend that you first look at these summary reports.

|Column|Description|
|---|---|
|Task name|Friendly name of the migration task|
|Status|Status of each task (success, failure, in progress, not started)|
|Source|File path or URL of the location of the data being migrated.|
|Destination|The URL of the Site and library to where the data will be migrated.|
|Total scanned items|Total number of files and list items, including those that will be filtered out because of settings or potential scan issues.|
|Total to be migrated items|The total number of files and list items that were expected to migrate excluding those filtered out based on settings or potential scan issues.|
|Migrated items|The total number of files migrated.|
|Items not migrated|Number of files that did not migrate.|
|Total bytes|Total number of bytes scanned in source destination.|
|Total GB|Total number of gigabytes scanned in source destination.|
|Migrated bytes|The total number of bytes of data migrated.|
|Migrated GB|The total size of the files migrated, expressed in gigabytes.|
|Agent|The address of the migration agent (VM or computer) that is running the migration task.|
|Duration|Length of time in minutes that the migration task took to complete.|
|TaskID|Unique ID of the task.|
|Task failure reason|Explanation of task failure.|
|Agent group|Name of agent group the task was assigned to.|

## Task Reports

When you need to do a more in-depth investigation or a thorough verification of your migration task, the task level reports help you drill down into the specific details.  We recommend using these reports to help you accomplish this.

- **ItemSummary.csv:** This is similar to the overall summary report except that it aggregates the data just for a single task.

- **ItemFailureReport.csv:** This is the failure report at the item level. This is a filtered version of the files report, showing only failures.

- **ItemReport.csv:**  A list of all the items this task attempted to do

- **ScanSummary.csv:** This report gives statistical totals.

- **StructureReport.csv:**  Structure report at the task level.

- **StructureFailureReport.csv:**  Structure failure report at the task level.

- **StructureFailureSummary.csv:**  This is an aggregate of all the structural task failure reports. This will only be generated if there are failures.

### Item Summary

The **ItemSummary.csv** report is a summary report at the task level.

|Column|Description|
|---|---|
|Incremental round|The round number added to the end of the report name (RO, R1, etc.) indicates if the scan or job has been rerun.|
|Scanned|Total number of files scanned before migration.|
|Item scan failures|Number of files that failed the scan and doesn't qualify for the migration.|
|Filtered out items|Number of files not included in migration.|
|Expected migrated file count|The total number of files that were expected to migrate excluding those filtered out based settings or scanned potential issues. The total number of files that were expected to migrate.|
|Read|Total number of files read.|
|Packaged|Total number of files packaged and ready to upload to the destination.|
|Uploaded|Total number of files attempted to upload.|
|ReUploaded|The total number of files that were re-uploaded.|
|Submitted|Total number of files submitted.|
|ReSubmitted|Total number of files resubmitted.|
|Migrated|Total number of files migrated.|
|Failed reading|Number of files that encountered an error or failure while being read.|
|Failed packing|Number of files that encountered an error or failure while being packaged.|
|Failed uploading|Number of files that encountered an error or failure while being uploaded.|
|Failed submitting|Number of files that encountered an error or failure while being submitted.|
|Failed querying|Number of files that encountered an error or failure while being queried.|
|Device name|Name of the device or computer that is running the migration job.|

### Item Failure Report

The **ItemFailureReport.csv**, is only generated if an error resulting in a file being unable or failing to migrate.

|Column|Description|
|---|---|
|Source|File path or URL of the location of the data being migrated.|
|Destination|the URL of the tenant and library to where the data will be migrated.|
|Item name|The name of the file migrated.|
|Extension|The extension, indicating the file type.|
|Item size|The size of the individual file.|
|Content type|The file type.|
|Status|Status indicating at what stage the file is.|
|Result category|General code associated with the item to indicate what happened with that item.|
|Message|Detailed error or informational message.|
|Error code|Failed reason error code.|
|Source item ID|ID of the item at the source.|
|Destination item ID|ID of the item at the destination.|
|Package number|ID generated for the package number during the transition.|
|Migration job ID|The ID number of the job (which could contain one or more tasks).|
|Incremental Round|The round number added to the end of the report name (RO, R1, etc.) indicates if the scan or job has been rerun.|
|Task ID|The ID number of the Task.|
|Device name|Name of the device or computer that is running the migration job.|

### Item Report

The **ItemReport.csv** is a detailed report that provides data on each file within the task.

|Column|Description|
|---|---|
|Source|File path or URL of the location of the data being migrated.|
|Destination|the URL of the tenant and library to where the data will be migrated.|
|File name|The name of the file migrated.|
|Extension|The extension, indicating the file type.|
|File size|The size of the individual file.|
|Content type|The file type.|
|Status|Status indicating at what stage the file is.|
|Result category|General code associated with the item to indicate what happened with that item.|
|Message|more detailed Error or informational message generated.|
|Source item ID|ID of the item at the source.|
|Destination item ID|ID of the item at the destination.|
|Package number|ID generated for the package number during the transition.|
|Migration job ID|The ID number of the job (which could contain one or more tasks).|
|Incremental round|The round number added to the end of the report name (RO, R1, etc.) indicates if the scan or job has been rerun.|
|Task ID|The ID number of the Task.|
|Device name|Name of the device or computer that is running the migration job.|

### Scan Summary

The **ScanSummary.csv** report provides the total stats for the scan -- a process that takes place before the actual migration begins.

|Column|Description|
|---|---|
|Incremental round|The round number added to the end of the report name (RO, R1, etc.) indicates if the scan or job has been rerun.|
|Total scanned items|Total number of folders, list items and files that have been scanned.|
|Total scanned folders|Total number of folders scanned.|
|Total scanned list items|Total number of list items scanned.|
|Total scanned files|Total number of files scanned.|
|Folders with issues|The number of folders with potential issues for the migration.|
|Items with issues|The number of files with potential issues for migration.|
|Items filtered out|Number of files that were filtered out based on settings in the tool.|
|Folders to be migrated|Number of folders that will be migrated.|
|Items to be migrated|Number of files that will be migrated.|
|Total items to be migrated|Total number of folders and files that will be migrated.|
|Device name|Name of the device or computer that is running the migration job.|

### Structure report

Structure report at the task level.

|Column|Description|
|---|---|
|Structure type|Site collection, site, list, field, content type, view|
|Structure title|Display name of the object|
|Operation|Skipped, created or updated.|
|Status|Success, partial success, failure|
|Details|Reason for failure.|
|Source structure URL|Display the source URL. Site collection, site, and list will list the URL. Fields, content type. and view will display its container's URL.|
|Destination structure URL|Display the source URL. Site collection, site, and list will list the URL. Fields, content type, and view will display its container's URL.|
|Source structure ID|ID when available.|
|Destination structure ID|ID when available.|
|Time stamp|The time at which the action occurred.|

### Structure failure report

This is a failure report at the task level. This report will only be generated if there is a failure.

|Column|Description|
|---|---|
|Structure type|Site collection, site, list, field, content type, view|
|Structure title|Display name of the object|
|Operation|Skipped, created or updated.|
|Status|Success, partial success, failure|
|Details|Reason for failure.|
|Source structure URL|Display the source URL. Site collection, site, and list will list the URL. Fields, content type. and view will display its container's URL.|
|Destination structure URL|Display the source URL. Site collection, site, and list will list the URL. Fields, content type, and view will display its container's URL.|
|Source structure ID|ID when available.|
|Destination structure ID|ID when available.|
|Time stamp|The time at which the action occurred.|

### Structure failure summary

This is an aggregate of all the task failure reports. This will only be generated if there are failures.

|Column|Description|
|---|---|
|Structure type|Site collection, site, list, field, content type, view|
|Structure title|Display name of the object|
|Operation|Skipped, created or updated.|
|Status|Success, partial success, failure|
|Details|Reason for failure.|
|Source structure URL|Display the source URL. Site collection, site, and list will list the URL. Fields, content type. and view will display its container's URL.|
|Destination structure URL|Display the source URL. Site collection, site, and list will list the URL. Fields, content type, and view will display its container's URL.|
|Source structure ID|ID when available.|
|Destination structure ID|ID when available.|
|Time stamp|The time at which the action occurred.|

## Performance report

This report provides scores ranging from 1 to 100. The greater the number, the higher the speed. While these scores cannot predict how fast the migration will perform, they can help identify areas that could be impacting your migration performance.

|Column|Recommendation|
|---|---|---|
|Reading source speed score|[Improving the speed at which the source can be read](./mm-performance.md#improving-the-speed-at-which-the-source-can-be-read)|
|Local disk performance score|[Improving the migration computer speed](./mm-performance.md#improving-the-migration-computer-speed)|
|Uploading speed score|[Improving your connectivity to Office 365 and Azure](./mm-performance.md#improving-your-connectivity-to-office-365-and-azure)|
|SharePoint throughput score|[Improving your migration performance](./sharepoint-online-and-onedrive-migration-speed.md)|
