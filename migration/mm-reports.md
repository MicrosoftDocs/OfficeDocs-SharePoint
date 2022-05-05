---
title: "Migration Manager Reports"
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
search.appverid: MET150
description: "Learn about the reports available when using Migration Manager in Microsoft 365."
---

# Migration Manager reports

Migration Manager generates log files, summary and task level reports, and a performance report.  These will help you manage, audit and troubleshoot your migration process.

Summary report: 
- [Summary Report](#summary-report)

Task level reports:
- [Item Summary](#item-summary)
- [Item Failure Report](#item-failure-report)
- [Item Report](#item-report)
- [Scan Summary](#scan-summary)
- [Structure Report](#structure-report)
- [Structure Failure Report](#structure-failure-report)
- [Structure Failure Summary](#structure-failure-summary)

Performance report
- [Performance Report](#performance-report)
  
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
  
### Summary Report

|**Column**|**Description**|
|:-----|:-----|
|Task name  <br/>|Friendly name of the migration task|
|Status  <br/> |Status of each task (success, failure, in progress, not started)  <br/> |
|Source  <br/> |File path or URL of the location of the data being migrated.  <br/> |
|Destination  <br/> |The URL of the Site and library to where the data will be migrated.  <br/> |
|Total scanned items  <br/> |Total number of files and list items, including those that will be filtered out because of settings or potential scan issues.  <br/> 
|Total to be migrated items <br/> |The total number of files and list items that were expected to migrate excluding those filtered out based on settings or potential scan issues.  <br/> |
|Migrated items <br/> |The total number of files migrated.  <br/> |
|Items not migrated <br/> |Number of files that did not migrate.  <br/> |
|Total bytes  <br/> |Total number of bytes scanned in source destination.  <br/> |
|Total GB  <br/> |Total number of gigabytes scanned in source destination.  <br/> |
|Migrated bytes  <br/> |The total number of bytes of data migrated.  <br/> |
|Migrated GB <br/> |The total size of the files migrated, expressed in gigabytes.  <br/> |
|Agent|The address of the migration agent (VM or computer) that is running the migration task.|	
|Duration  <br/> |Length of time in minutes that the migration task took to complete.  <br/> |
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
  
|**Column**|**Description**|
|:-----|:-----|
|Incremental round  <br/> |The round number added to the end of the report name (RO, R1, etc.) indicates if the scan or job has been rerun.  <br/> |
|Scanned  <br/> |Total number of files scanned before migration.  <br/> |
|Item scan failures  <br/> |Number of files that failed the scan and doesn't qualify for the migration.  <br/> |
|Filtered out items  <br/> |Number of files not included in migration.  <br/> |
|Expected migrated file count  <br/> |The total number of files that were expected to migrate excluding those filtered out based settings or scanned potential issues. The total number of files that were expected to migrate.  <br/> |
|Read  <br/> |Total number of files read.  <br/> |
|Packaged  <br/> |Total number of files packaged and ready to upload to the destination.  <br/> |
|Uploaded  <br/> |Total number of files attempted to upload.  <br/> |
|ReUploaded  <br/> |The total number of files that were re-uploaded.  <br/> |
|Submitted  <br/> |Total number of files submitted.  <br/> |
|ReSubmitted  <br/> |Total number of files resubmitted.  <br/> |
|Migrated  <br/> |Total number of files migrated.  <br/> |
|Failed reading  <br/> |Number of files that encountered an error or failure while being read.  <br/> |
|Failed packing  <br/> |Number of files that encountered an error or failure while being packaged.  <br/> |
|Failed uploading  <br/> |Number of files that encountered an error or failure while being uploaded.  <br/> |
|Failed submitting  <br/> |Number of files that encountered an error or failure while being submitted.  <br/> |
|Failed querying  <br/> |Number of files that encountered an error or failure while being queried.  <br/> |
|Device name  <br/> |Name of the device or computer that is running the migration job.  <br/> |
   
### Item Failure Report

The **ItemFailureReport.csv**, is only generated if an error resulting in a file being unable or failing to migrate. 
  
|**Column**|**Description**|
|:-----|:-----|
|Source  <br/> |File path or URL of the location of the data being migrated.  <br/> |
|Destination  <br/> |the URL of the tenant and library to where the data will be migrated.  <br/> |
|Item name  <br/> |The name of the file migrated.  <br/> |
|Extension  <br/> |The extension, indicating the file type.  <br/> |
|Item size  <br/> |The size of the individual file.  <br/> |
|Content type  <br/> |The file type.  <br/> |
|Status  <br/> |Status indicating at what stage the file is.  <br/> |
|Result category  <br/> |General code associated with the item to indicate what happened with that item.  <br/> |
|Message  <br/> |Detailed error or informational message .  <br/> |
|Error code  <br/> |Failed reason error code.  <br/> |
|Source item ID  <br/> |ID of the item at the source.  <br/> |
|Destination item ID  <br/> |ID of the item at the destination.  <br/> |
|Package number  <br/> |ID generated for the package number during the transition.  <br/> |
|Migration job ID  <br/> |The ID number of the job (which could contain one or more tasks).  <br/> |
|Incremental Round  <br/> |The round number added to the end of the report name (RO, R1, etc.) indicates if the scan or job has been rerun.  <br/> |
|Task ID  <br/> |The ID number of the Task.  <br/> |
|Device name  <br/> |Name of the device or computer that is running the migration job.  <br/> |
   
### Item Report

The **ItemReport.csv** is a detailed report that provides data on each file within the task. 
  
|**Column**|**Description**|
|:-----|:-----|
|Source  <br/> |File path or URL of the location of the data being migrated.  <br/> |
|Destination  <br/> |the URL of the tenant and library to where the data will be migrated.  <br/> |
|File name  <br/> |The name of the file migrated.  <br/> |
|Extension  <br/> |The extension, indicating the file type.  <br/> |
|File size  <br/> |The size of the individual file.  <br/> |
|Content type  <br/> |The file type.  <br/> |
|Status  <br/> |Status indicating at what stage the file is.  <br/> |
|Result category  <br/> |General code associated with the item to indicate what happened with that item.  <br/> |
|Message  <br/> |more detailed Error or informational message generated.  <br/> |
|Source item ID  <br/> |ID of the item at the source.  <br/> |
|Destination item ID  <br/> |ID of the item at the destination.  <br/> |
|Package number  <br/> |ID generated for the package number during the transition.  <br/> |
|Migration job ID  <br/> |The ID number of the job (which could contain one or more tasks).  <br/> |
|Incremental round  <br/> |The round number added to the end of the report name (RO, R1, etc.) indicates if the scan or job has been rerun.  <br/> |
|Task ID  <br/> |The ID number of the Task.  <br/> |
|Device name  <br/> |Name of the device or computer that is running the migration job.  <br/> |
   
### Scan Summary

The **ScanSummary.csv** report provides the total stats for the scan -- a process that takes place before the actual migration begins. 
  
|**Column**|**Description**|
|:-----|:-----|
|Incremental round  <br/> |The round number added to the end of the report name (RO, R1, etc.) indicates if the scan or job has been rerun.  <br/> |
|Total scanned items  <br/> |Total number of folders, list items and files that have been scanned.  <br/> |
|Total scanned folders  <br/> |Total number of folders scanned.  <br/> |
|Total scanned list items  <br/> |Total number of list items scanned.  <br/> |
|Total scanned files  <br/> |Total number of files scanned.  <br/> |
|Folders with issues  <br/> |The number of folders with potential issues for the migration.  <br/> |
|Items with issues  <br/> |The number of files with potential issues for migration.  <br/> |
|Items filtered out  <br/> |Number of files that where filtered out based on settings in the tool.  <br/> |
|Folders to be migrated  <br/> |Number of folders that will be migrated.  <br/> |
|Items to be migrated  <br/> |Number of files that will be migrated.  <br/> |
|Total items to be migrated  <br/> |Total number of folder and files that will be migrated.  <br/> |
|Device name  <br/> |Name of the device or computer that is running the migration job.  <br/> |
   
### Structure report

Structure report at the task level.
  
|**Column**|**Description**|
|:-----|:-----|
|Structure type  <br/> |Site collection, site, list, field, content type, view  <br/> |
|Structure title  <br/> |Display name of the object  <br/> |
|Operation  <br/> |Skipped, created or updated.  <br/> |
|Status  <br/> |Success, partial success, failure  <br/> |
|Details  <br/> |Reason for failure.  <br/> |
|Source structure URL  <br/> |Display the source URL. Site collection, site, and list will list the URL. Fields, content type. and view will display its container's URL.  <br/> |
|Destination structure URL  <br/> |Display the source URL. Site collection, site, and list will list the URL. Fields, content type, and view will display its container's URL.  <br/> |
|Source structure ID  <br/> |ID when available.  <br/> |
|Destination structure ID  <br/> |ID when available.  <br/> |
|Time stamp  <br/> |The time at which the action occurred.  <br/> |
   
### Structure failure report

This is a failure report at the task level. This report will only be generated if there is a failure.
  
|**Column**|**Description**|
|:-----|:-----|
|Structure type  <br/> |Site collection, site, list, field, content type, view  <br/> |
|Structure title  <br/> |Display name of the object  <br/> |
|Operation  <br/> |Skipped, created or updated.  <br/> |
|Status  <br/> |Success, partial success, failure  <br/> |
|Details  <br/> |Reason for failure.  <br/> |
|Source structure URL  <br/> |Display the source URL. Site collection, site, and list will list the URL. Fields, content type. and view will display its container's URL.  <br/> |
|Destination structure URL  <br/> |Display the source URL. Site collection, site, and list will list the URL. Fields, content type, and view will display its container's URL.  <br/> |
|Source structure ID  <br/> |ID when available.  <br/> |
|Destination structure ID  <br/> |ID when available.  <br/> |
|Time stamp  <br/> |The time at which the action occurred.  <br/> |
   
### Structure failure summary

This is an aggregate of all the task failure reports. This will only be generated if there are failures.
  
|**Column**|**Description**|
|:-----|:-----|
|Structure type  <br/> |Site collection, site, list, field, content type, view  <br/> |
|Structure title  <br/> |Display name of the object  <br/> |
|Operation  <br/> |Skipped, created or updated.  <br/> |
|Status  <br/> |Success, partial success, failure  <br/> |
|Details  <br/> |Reason for failure.  <br/> |
|Source structure URL  <br/> |Display the source URL. Site collection, site, and list will list the URL. Fields, content type. and view will display its container's URL.  <br/> |
|Destination structure URL  <br/> |Display the source URL. Site collection, site, and list will list the URL. Fields, content type, and view will display its container's URL.  <br/> |
|Source structure ID  <br/> |ID when available.  <br/> |
|Destination structure ID  <br/> |ID when available.  <br/> |
|Time stamp  <br/> |The time at which the action occurred.  <br/> |
   

## Performance report

This report provides scores ranging from 1 to 100. The greater the number, the higher the speed. While these scores cannot predict how fast the migration will perform, they can help identify areas that could be impacting your migration performance.

|**Column**|**Recommendation**|
|:-----|:-----|:-----|
|Reading source speed score<br/> |[Improving the speed at which the source can be read](./mm-performance.md#improving-the-speed-at-which-the-source-can-be-read)<br/> |
|Local disk performance score<br/> |[Improving the migration computer speed](./mm-performance.md#improving-the-migration-computer-speed) <br/> |
|Uploading speed score  <br/> |[Improving your connectivity to Office 365 and Azure](./mm-performance.md#improving-your-connectivity-to-office-365-and-azure)<br/> |
|SharePoint throughput score <br/> |[Improving your migration performance](./sharepoint-online-and-onedrive-migration-speed.md) <br/> |