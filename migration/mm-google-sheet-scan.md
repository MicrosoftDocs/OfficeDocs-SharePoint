---
ms.date: 11/14/2023
title: "Scan Google Sheet spreadsheets with Migration Manager"
ms.reviewer: 
ms.author: heidip
author: MicrosoftHeidi
manager: jtremper
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: microsoft-365-migration
ms.localizationpriority: high
ms.collection: 
- m365solution-migratetom365
- m365solution-scenario
- M365-collaboration
- SPMigration
- highpri
- m365initiative-migratetom365
ms.custom: admindeeplinkSPO
search.appverid: MET150
description: Migrate Google Sheet spreadsheets with Migration Manager.
---
# Scan Google Sheet spreadsheets with Migration Manager

>[!Important]
>Due to the limitations of the Google API quota, Sheet Scan operates with a restricted scope on each sheet file. Specifically, the sheet scan examines only the top 1,000 cells or the first 100 errors identified, whichever condition is met first, then the scan process for that sheet file will conclude.

A sheet scan is a scanning feature that exposes issues such as incompatible formulas and invalid embedded links in Google Sheets when exported and transferred to Microsoft Excel files. Migration Manager generates sheet reports listing issues discovered in the sheet scan process.
The sheet scan is turned off by default. Once you enable it in project settings, it's automatically run as part of the general scan process.

Learn more:

- [How to run a general scan process in Migration Manager](mm-google-step2-scan-assess.md)
- [How to start a Google Drive migration project in Migration Manager](mm-google-overview.md)

## Prerequisites

You must grant the **Microsoft 365 Migration** app access to all your Google Sheets spreadsheets in  Google Marketplace. Spreadsheet access must be granted before Migration Manager can run a **sheet scan** on your Google Sheets. 

### Grant access to Google Sheets

1. Sign in with your Google admin credentials to [Google Marketplace](https://admin.google.com/ac/apps/gmail/marketplace/appdetails/888375727339).
2. Under **Drive**, verify that "See all your Google Sheets spreadsheets” status shows **Granted**.  

  :::image type="content" source="media/mm-google-permission-gsheet.png" alt-text="google permissions granting for gsheet":::

3. If it hasn't been granted, select **Grant access** at the top of the page to grant access.
4. Once access has been granted, Migration Manager can run sheet scans for Google Sheets spreadsheet files.

## Enable Sheet scan

To enable a Google Sheet scan in a Google Drive migration project:

1. Select **Project Settings** in the top-right toolbar.
2. Select the **Advanced** tab.
3. Select **Enable Google Sheet scan** setting. Once enabled, the sheet scan is automatically included as part of the general scan.


## Sheet scan reports

Once a general scan is done, it may take a while for the Sheet Scan reports to be generated. 
To download Sheet Scan reports, select one or multiple scan tasks, and then select “Download reports – Sheet summary/Sheet detailed” from the action bar.
 
|Report type|Download menu|Tasks selection limit|Report name|Report Description|
|:-----|:-----|:-----|:-----|:-----|
|Sheet Summary|Download report – Sheet summary|Can select up to 1000 tasks|SheetSummary.csv|A summary of Google Sheets of each selected task|
|Sheet detailed|Download report – Sheet detailed|Can select up to 100 tasks|- SheetItem.csv</br>-  SheetIssue.csv|**SheetItem.csv**: Lists all the Google Sheets files scanned and whether they have issues or not</br>**SheetIssue.csv**: Lists issue details of selected tasks


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
|SheetScanStatus|Status of the sheet scan process.|


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
|IssueType|Type of issue found.|
|IssueDetail|Details of the issue found.|
|CellLocation|Location of the cell with issue found.|
|CellContent|Original content of the cell with issue found.|
