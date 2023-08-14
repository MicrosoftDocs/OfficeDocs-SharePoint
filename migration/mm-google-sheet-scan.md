---
ms.date: 08/14/2023
title: "Migrate Google spreadsheets with Migration Manager"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: serdars
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.subservice: sharepoint-migration
ms.localizationpriority: high
ms.collection: 
- m365solution-migratetom365
- m365solution-scenario
- M365-collaboration
- SPMigration
- highpri
ms.custom: admindeeplinkSPO
search.appverid: MET150
description: Migrate Google spreadsheets with Migration Manager.
---
# Migrate Google Sheets with Migration Manager

A sheet Scan is a scanning feature that exposes issues such as incompatible formulas, and invalid embedded links in Google Sheets when they are exported and transferred to Microsoft Excel files. Migration Manager generates sheet reports are listing any issues discovered in the  Sheet Scan process.
 Sheet Scan is disabled by default. Once enabled, it’ll automatically run with the general scan process. Learn more:
- [How to trigger a general scan process in Migration Manager](mm-google-step2-scan-assess.md)
- [How to start a Google Drive migration project in Migration Manager](mm-google-overview.md)

## Enable Sheet Scan

To enable a Google Sheet scan in a Google Drive migration project:

1. Select “Project Settings” in the top-right toolbar.
2. Find “Advanced” tab.
3. Select **Enable Google Sheet scan** setting. Once enabled, sheet scan will trigger as part of the general scan.
4. Upon enabling, a Google Spreadsheet permissions check will be triggered, make sure Google Sheets spreadsheets permission is granted.  
 
 
Once enabled, sheet scan will trigger as part of the general scan.

 Sheet Scan Report
Once a general scan is done, it may take a while for the  Sheet Scan reports to be generated. 
To download Sheet Scan reports, select one or multiple scan tasks, and then click “Download reports – Sheet summary/Sheet detailed” from the action bar. 
 

|Report type|Download menu|Tasks selection limit|Report name|Report Description|
|:-----|:-----|:-----|:-----|:-----|
|Sheet Summary|Download report – Sheet summary|Can select up to 1000 tasks|SheetSummary.csv|A summary of Google Sheets of each selected task|
|Sheet detailed|Download report – Sheet detailed|Can select up to 100 tasks|-SheetItem.csv</br>- - SheetIssue.csv|-List all the Google Sheets files scanned and whether they have issues or not</br>- Issue details of selected tasks


### SheetSummary.csv

A summary of Google Sheets of each selected task. Each line represents a summary of each task selected.


|Column name|Description|
|:-----|:-----|
|TaskId|ID of the selected task, used for troubleshooting.|
|Name|Display name of the selected task in the source.|
|SourcePath|Source path of the selected task.|
|TotalGSheet|The number of Google Sheets found in the task.|
|GSheetWithIssue|The number of Google Sheets in the task with issues found.|
|Issues|Total number of issues found in the task.|


### SheetItem.csv

List all the Google Sheets files scanned and whether they have issues or not.

|Column name|Description|
|:-----|:-----|
|TaskId|ID of the selected task, used for troubleshooting.|
|TransactionID|Every time when task is run, it's a transaction. Transaction ID is used for troubleshooting.|
|Name|Display name of the selected task in the source.|
|SourcePath|Source path of the selected task.|
|FullPath|Full path of the item in the source.|
|LastModified|Last modified time of the Google Sheets file.|
|IssueCount|Total number of issues found in the Google Sheets file.|

### SheetIssue.csv

Issue details of selected tasks.

|Column name|Description|
|:-----|:-----|
|TaskId|ID of the selected task, used for troubleshooting.|
|TransactionID|Every time when task is run, it's a transaction. Transaction ID is used for   troubleshooting.|
|Name|Display name of the selected task in the source.|
|SourcePath|Source path of the selected task.|
|FullPath|Full path of the item in the source.|
|LastModified|Last modified time of the Google Sheets file.|
|SheetName|The name of the Google Sheets file.|
|IssueType|Type of issue found. Presently, only incompatible formula detection is supported.|
|IssueDetail|Details of the issue found.|
|CellLocation|Location of the cell with issue found.|
|CellContent|Original content of the cell with issue found.|
