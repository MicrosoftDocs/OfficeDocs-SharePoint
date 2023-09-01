---
ms.date: 12/05/2022
title: Migration Manager cloud migration reports
ms.reviewer: JoanneHendrickson
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
description: "Learn about reports, errors, and status codes for cloud to cloud migrations using Migration Manager in Microsoft 365."
---
# Migration Manager: Reports, errors & status codes for cloud migrations

Migration Manager generates a series of logs and reports for cloud migration scenarios. There are two sets of reports: Those generated during the scan stage and those during the actual migration. 

A scan/migration task presents as a row in the Migration Manager scan/migration list. The task equals to: 

- **Google Drive:** Personal or Shared Drive
- **Dropbox:** Member or Team folder
- **Box:** User, Admin, or Co-admin
- **Egnyte:** Private or Shared folder

## Reports

Use these reports to help manage, audit, and troubleshoot your migration process.

|Report type|Scan report|Description|
|:-----|:-----|:-----|
|Detailed|[TransactionItem.csv](#scan-transactionitemcsv)|Details of the last scan for all items.|
|Summary|[FileExtension.csv](#fileextensioncsv)|Provides the statistics of extension types existing in each task.|
|Summary|[LargeFileSize.csv](#largefilesizecsv)|Lists all items larger than 15 GB that **can't** be migrated.|
|Summary|[LongPath.csv](#longpathcsv)|Lists all items with path lengths larger than 300 characters and that **can't** be migrated.|
|Summary|[ProjectError.csv](#scan-projecterrorcsv)|Lists all item level errors that occurred during the scan process of all tasks.|
|Summary|[ScanSummary.csv](#scansummarycsv)|Task level summary of all scan tasks. You can find the scan results based on the scan status code listed.|


|Report type|Migration report|Description|
|:-----|:-----|:-----|
|Detailed|[TransactionItem.csv](#migration-transactionitemcsv)|Lists the final migration status of all items of the selected task.|
|Summary|[ProjectError.csv](#migration-projecterrorcsv)|Lists all item level errors that ever occurred during the migration process of all tasks.|
|Summary|[Migration summary.csv](#migration-summarycsv)|Task level summary of all migration tasks. |

>[!Important]
>These reports are for cloud migrations only. For file share migrations, learn more at: [**Reports and errors for file share migrations**](mm-reports.md).
>
>These reports expire in 90 days. Microsoft doesn't retain the raw data (the log files).

## Failure and status codes 

Your reports may reference a failure or status code to provide specific details as to the nature of the issue. 
  
- [Failure codes](#failure-codes): Result codes or "failure codes" represent item level errors during both the scan and migration process.  
- [Status codes](#status-codes): Status codes provide the final status of the scan and migration tasks.  

## How to download reports

Detailed and summary reports of your scan and migration tasks can be downloaded individually or in bulk. 

There are limits on the number of tasks can be selected for bulk download for each report type: 

|Report type|Number of tasks allowed per download|
|:-----|:-----|
|Scan summary report|1000| 
|Scan detailed report|100 |
|Migration summary report|1000|
|Migration detailed report|100|

>[!Note]
>For each report type, only one can be processed at a time. For example, there can’t be two scan summary reports running simultaneously.
>
>The option to download all summary reports when no drives are selected is disabled. To download multiple summary reports efficiently, use the multi-select or select-all function on tasks.


### Download Scan reports

1. On the **Scan** tab, select one or more rows listed in the table. Each row in the table represents a scan task.
2. From the action bar, select **Download reports**. Then select either **Detailed** or **Summary** depending on the type of report you need.

:::image type="content" source="media/mm-cloud-reports-download-dropdown.png" alt-text="Dropdown menu for downloading either detailed or summary reports":::

3. After the reports have been created, a message appears with a link to download the .zip file containing the reports. For example:  

:::image type="content" source="media/mm-cloud-reports-download-ready-linkbox.png" alt-text="link for download ready":::

4. You can also access reports that you have requested by selecting **Recent actions** from the menu bar at the top of the screen.  Reports can be accessed for up to 30 days.

:::image type="content" source="media/mm-cloud-recent-actions-button-on-menu.png" alt-text="recent actions button on menu bar":::

:::image type="content" source="media/mm-cloud-recent-actions-reports.png" alt-text="recent actions action panel":::


### Download Migration reports

1. On the **Migration** tab, select one or more rows from the list of migration tasks. Each row in the table represents a migration task.
2. From the action bar, select **Download reports**. Then select either **Detailed** or **Summary** depending on the type of report you need.
3. After the reports have been created, a message appears with a link to download the .zip file containing the reports. 
4. You can also access reports that you have requested by selecting **Recent actions** from the menu bar at the top of the screen.  Reports can be accessed for up to 30 days.

## Scan reports

The following reports are downloaded from the **Scans** tab in Migration Manager. 

### Scan TransactionItem.csv 

The TransactionItem.csv report details the last scan for all items. Each row in the .csv file represents an item of the selected task. 

|Column|Description|
|:-----|:-----|
|TaskId |ID of the selected task, used for debugging. |
|TransactionId |Whenever a task is run, it becomes a transaction. The transaction ID is used for debugging.|
|Name |Display name of the source account. |
|SourcePath |Source path of the selected source account. |
|OperationStep |Operation step of the item. |
|Status |Final scan status of the item. “Skipped” indicates the scan has completed, and the item is ready to be migrated. |
|ResultCode|Failure code of the item. A value of "None" will show in this column when the item status is "Success". For a listing of all result codes, see [Failure codes](#failure-codes). |
|FailureReason|Description of the failed item. This column is blank if the item status has a value of "Success". For a listing of all result codes, see [Failure codes](#failure-codes). |
|FullPath |Full path of the item in the source. |
|SourcePathDepth |Path depth of the item in the source.  |
|SourceBasename |Base name of the item in the source. If the item is a root folder, this column is blank. |
|SourceExtension |File extension of the item in the source. If the item is a root folder, this column is blank. |
|SourceType |Type of folder in the source. |
|SourceSize |Data size of the item in the source. |
|SourceAclsTotal |The number of users and groups with whom the item is shared. |
|SourceAclsUnique |The number of users and groups with whom the item is shared and that is different from its parent. |
|DestinationPath |Full path of the item in the destination. |
|DestinationPathDepth |Path depth of the item in the destination.  |
|DestinationBasename |Base name of the item in the destination. If the item is a root folder, this column is blank. |
|DestinationExtension |File extension of the item in the destination. If the item is a root folder, this column is blank. |
|DestinationLocation |The web URI of the item in destination. |
|DestinationType |File or folder in the destination. |
|DestinationSize |Data size of the item in the destination. |

### FileExtension.csv 

The FileExtension.csv report details the extension types in each task. 

|Column |Description| 
|:-----	|:------|
|TaskId|ID of the selected task, used for debugging. |
|Name|Display name of the selected task in the source. |
|SourcePath|Source path of the selected task. |
|FullPath|	Full path of the item in the source. |
|SourceExtension|Extension type exists in the task. |
|TotalSize|Total data size of the extension type in the task. |

### LargeFileSize.csv

The LargeFileSize.csv report details all items larger than 15 GB that can't be migrated. 

|Column |Description |
|:------|:-----|
|TaskId |ID of the selected task, used for debugging. |
|Name |Display name of the selected task in the source. |
|SourcePath |Source path of the selected task. |
|FullPath |Full path of the item in the source. |
|SourceSize |Data size in Byte of the item in the source. |
|SourceSizeInGB |Data size in GB of the item in the source. |

### LongPath.csv

The LongPath.csv report details all items with path lengths larger than 300 and that can't be migrated. 

|Column |Description |
|:-----|:-----|
|TaskId |ID of the selected task, used for debugging. |
|Name |Display name of the selected task in the source. |
|SourcePath |Source path of the selected task. |
|FullPath |Full path of the item in the source. |
|SourcePathLength |Path length of the item in the source. |

### Scan ProjectError.csv 

The ProjectError.csv report details all item level scan errors that have occurred. 

|Column|Description
|:-----|:-----| 
|TaskId|ID of the selected task, used for debugging. 
|Name|Display name of the selected task in the source. 
|SourcePath|Source path of the selected task. 
|FullPath|Full path of the item in the source. 
|Action|Operation step of the item that goes wrong during the scan process. 
|ResultCode|Failure code of the item. It shows "null" when item status is "Success". To learn more, see [Failure codes](#failure-codes). |
|FailureReason|Primary reason for the task failing the scan.|


### ScanSummary.csv 

The ScanSummary.csv report is a task level summary of all scan tasks.

|Column |Description |
|:-----|:-----|
|TaskId |ID of the selected task, used for debugging. |
|StartTime|	Start time of the latest scan, expressed in UTC.|
|EndTime	|End time of the latest scan, expressed in UTC.|
|TransactionId |Every time when task is run, it's a transaction. Transaction ID is used for debugging. |
|Name |Display name of the selected task in the source. |
|SourcePath |Source path of the selected task. |
|Tags |Predefined tags of the task. |
|FoldersReadyToBeMigrated|Number of folders that are ready to be migrated.|
|FilesReadyToBeMigrated|Number of files that are ready to be migrated.|
|DataReadyToBeMigrated|Data size in Byte that is ready to be migrated.|
|UniquePermissions |Number of users and groups with whom the item is shared and that is different from its parent. |
|MaximumPathLength |The max path length among all the items in the source. |
|FoldersScanned|Number of folders scanned in the source.|
|FilesScanned|Number of files scanned in the source.|
|DataScanned|Data size in Byte that scanned in the source.|
|ScanStatusCode |Scan status code of the scanned task. To learn more, see [Status codes](#status-codes).  |
|MostRecentScan |The most recent scan time in UTC of the task. |



## Migration reports

### Migration TransactionItem.csv 

The TransactionItem.csv report details the final migration status for all items of the selected task. Each row in the .csv file represents an item of the selected task. 

|Column |Description |
|:-----|:-----|
|TaskId |ID of the selected task, used for debugging. |
|TransactionId |Every time when task is run, it becomes a transaction. Transaction ID is used for debugging. |
|Name |Display name of the source account. |
|SourcePath |Source path of the selected source account. |
|OperationStep |Operation step of the item. |
|Status |Final migration status of the item. |
|ResultCode|Failure code of the item. It shows "none" when item status is "Success". To learn more, see [Failure codes](#failure-codes).  |
|FailureReason |Failure description of the failed item. If the item status value is "Success", this column is left blank. To learn more, see [Failure codes](#failure-codes). |
|FullPath |Full path of the item in the source. |
|SourcePathDepth |Path depth of the item in the source.  |
|SourceBasename |Base name of the item in the source. If the item is a root folder, this column is blank. |
|SourceExtension |File extension of the item in the source. If the item is a root folder, this column is blank. |
|SourceType |Type of folder in the source. |
|SourceSize |Data size of the item in the source. |
|SourceAclsTotal |The number of users and groups with whom the item is shared. |
|SourceAclsUnique |The number of users and groups with whom the item is shared and that is different from its parent. |
|DestinationPath |Full path of the item in the destination. |
|DestinationPathDepth |Path depth of the item in the destination.  |
|DestinationBasename |Base name of the item in the destination. If the item is a root folder, this column is blank. |
|DestinationExtension |File extension of the item in the destination. If the item is a root folder, this column is blank. |
|DestinationLocation |The web URI of the item in destination. |
|DestinationType |File or folder in the destination. |
|DestinationSize |Data size of the item in the destination. |


### Migration ProjectError.csv 

The Projecterror.csv report details all item level errors that ever occurred during the migration process of all tasks. 

|Column |Description |
|:-----|:-----|
|TaskId|ID of the selected task, used for debugging. |
|Name|Display name of the selected task in the source. |
|SourcePath |Source path of the selected task. |
|FullPath|Full path of the item in the source. |
|Action|Operation step of the item that goes wrong during the migration process. |
|ResultCode|Failure code of the item. It shows "null" when item status is "Success". To learn more, see [Failure codes](#failure-codes). |
|FailureReason|Failure description of the failed item. If the item status is "Success", this column is blank.To learn more, see [Failure codes](#failure-codes). |


### Migration Summary.csv 

The Migration Summary.csv report is a task level summary of all migration tasks.

|Column |Description |
|:-----|:-----|
|TaskId |ID of the selected task, used for debugging. |
|TransactionId |Every time when task is run, it's a transaction. Transaction ID is used for debugging. |
|StartTime|Start time of the latest migration, expressed in UTC.|
|EndTime|End time of the latest migration, expressed in UTC.|
|Name |Display name of the selected task in the source. |
|SourcePath |Source path of the selected task. |
|Tags |Predefined tags of the task. |
|StatusCode |Status code of the migration task. To learn more, see [Status codes](#status-codes).   |
|FoldersCreated |Folder created in the destination for the migration. |
|FilesTotalCopied|To date, the total files that have been migrated to the destination from all migrations ever initiated.|
|FilesLatestCopied|Files that migrated to the destination in the latest migration.|
|FilesAlreadyCopied|Files already migrated to the destination from previous migrations or already exist in the destination.|
|FilesFiltered|Files not migrated due to migration filter setting.|
|FilesFailed|Files that failed in the migrating process.|
|DataTotalCopied|Total data size (in bytes) that has been migrated to the destination from all migrations ever initiated.|
|DataLatestCopied|Data size (in bytes) migrated to the destination in the latest migration.|
|DataAlreadyCopied|Data size (in bytes) already migrated to the destination from previous migrations or already exists in the destination.|
|DataFiltered|Data size (in bytes) not migrated due to migration filter setting.|
|DataFailed|Data size (in bytes) that failed in the migrating process.|
|FilePermissions| File-level permission migration is set to be on or off. The default setting is **Off**. |


## Failure codes

Result codes or "failure codes" represent item level errors during both the scan and migration process.

|Failure code|Description |User action|
|:-----|:-----|:-----|
|MACCESSDENIED|User denied access.|Check permissions and Try again...|
|MACCESSTOKENNULL|Failed to execute request as connector authorization failed.|Unexpected error. Try again.|
|MAUTHACCESSTOKEN|Connector authorization failure. Failed to get access token.|Unexpected error. Try again.|
|MAUTHACCESSTOKENINVALID|Connector authorization failure. The API request failed because the access token is invalid or expired.|Retry.|
|MAUTHCALLERNOTAUTHENTICATED|Connector authorization failed. The service isn't allowing to connect as it doesn't recognize the caller.|Try again.|
|MAUTHMOVERAPP|Microsoft 365 migration app needs to be authorized in source account.|Sign in to the source account and grant permission to the Microsoft 365 migration app. Try again.|
|MAUTHNOCODE|Connector authorization failed as auth code isn't provided.|Try again.|
|MAUTHNOEMAIL|Connector authorization failure. Failed to get email from claim.|Unexpected error. Try again.|
|MAUTHNOIDTOKEN|Connector authorization failure. Failed to get ID token from access token.|Unexpected error. Try again.|
|MAUTHNOTENANT|Connector authorization failed; no tenant/enterprise ID found. Tenant = Enterprise. Tenant is the term in MS/Azure and Enterprise is used by Box and others.|Try again.|
|MAUTHREFRESHTOKEN|Connector authorization failure. Failed to get refresh token.|Try again.|
|MAUTHUSERNOTADMIN|Connector authorization failed; user doesn't have admin role.|Check permissions and Try again...|
|MAZUREUPLOAD|Failed to submit the migration job to Migration API after the files were uploaded to the Azure blob.| Try again.|
|MBADREQUEST|Bad request when operating on source or destination item.|Unexpected error.  Try again.|
|MCONNECTORNOTFOUND|Connector not found in database.|Check connector settings.  Try again.|
|MCORRELATE|Collection correlates missing source listing.|Confirm source location, Try again...|
|MDESTINATIONNOTWRITABLE|You don't have write access to the destination. |Check permissions and Try again...|
|MDUPLICATE|Duplicate. This file already exists in your destination location.|Confirm file is in destination already.|
|MEMPTYMETADATA|Unable to find metadata. |Try again.|
|MEXPORTFILERESTRICTED|This file is restricted, and can’t be migrated from the source.|Check to see if this file has legal restrictions such as copyright claims.|
|MEXPORTFILEUNSUPPORTED|Unsupported file type. |You can't migrate this file from the source.|
|MEXPORTFILEUNSUPPORTEDMIMETYPE|Unsupported file type.|You can't migrate this file from the source. Check file at source.|
|MFAILEDGETROOTITEM|Failed to get root folder listing. This is set in both Google and Office365 connector.|Try again.|
|MFILEIMPORT|This file type isn't supported in the destination location. |Check source file.|
|MFILELOCKED|"File is locked, and can't download or get metadata. |Unlock file.  Try again.|
|MFILENAMELENGTH|Filename exceeds maximum allowable length. |Rename file and Try again...|
|MFILESIZEINCORRECT|Downloaded file is smaller than expected.|Check file for size and compare.  Try again.|
|MGETFOLDERACLS|Failure to get shared folder membership. |Check folder permissions and Try again...|
|MHTTPCONNECTION|Connection failure.|Check your network and Try again...|
|MINVALIDEMAIL|Invalid user email; unable to find user with that email. |Check user name and Try again...|
|MINVALIDPAGESIZE|The page size for connector pagination must be greater than zero.|Try again.
|MINVALIDPARENTID|Item has no parent ID. Id-based connectors require the item to have a parent ID.|Check file and Try again...|
|MINVALIDPATH|Path is invalid.|Check path and Try again...|
|MINVALIDRESPONSE|Invalid response from API call. |Try again.|
|MITEMPATHLENGTH|Item path exceeds length restrictions.|Check file path for length and Try again...|
|MLARGEFILESIZEEXPORT|File exceeds maximum size for export from the source.|Check file size.|
|MLARGEFILESIZEIMPORT|File exceeds maximum allowed size for import into destination. |Check file size. |
|MLISTGROUP|API request to list groups for connector failed.| This request may be caused by an invalid or throttling. Try again. |
|MLISTING|Folder listing failed.|Try again.|
|MLISTUSER|Failure to get user listing. This may be caused by an invalid requestor throttling. | Try again. |
|MLOCKACQ|Failed to acquire lock within timeout period and obtain new access token.|Try again.|
|MNONDESTRUCTIVEOPTIONENABLED| Unable to delete file or folder.|Try again.|
|MNOPARENT|Item doesn't have a parent item.|Check file and Try again...|
|MNOTAFILE|The path refers to something that isn't a file.|Check the path and correct as necessary. Try again.|
|MNOTAFOLDER|The path refers to something that isn't a folder.|Check the path and correct as necessary.  Try again.|
|MNOTFOUND|Item not found.|Check file and Try again...|
|MNOTIMPLEMENTED|Method not implemented for connector. |Try again.|
|MNOTPERMITTED|Can't traverse to the folder level; can't perform actions outside a users folder.|Check permissions and Try again...|
|MNOTUSERORTEAMDRIVE|Confirm that the name of the item in the source service matches what you have in the task's source path. Note: Google Suite allows invisible characters to be added to item names. We advise that your rename the item in the source service to ensure there's no invisible characters and then use that same name in the task source path.|
|MOWNERNOTFOUND|The original owner was removed or its information wasn't found.|Reassign ownership of the file.|
|MPATHMALFORMED|Invalid path format. | Check your source and Try again...|
|MSERVICENOTAVAILABLE|Service unavailable.|Try again.|
|MSETITEMPERMISSION|Failed to set permission. Failure may be caused by throttling.|Try again.|
|MSOURCENOTREADABLE|Unable to read the source directory. |Confirm source location. Try again.|
|MSTORAGEQUOTAREACHED|Storage quota exceeded for connector.|Increase storage limit and Try again...|
|MTHROTTLE|API requests made by connector are getting throttled.|Try again.|
|MUNVERIFIEDPARENT|Item doesn't have a verified parent item. |Check file and Try again...|
|MUPDATEITEMPERMISSION|Failed to remove permissions. |Try again.|
|MUSERCOUNT|Unexpected failure to get user count. |Try again.|
|MUSERFORBIDDEN|The current user doesn't have permission to access the file or folder.|Check permissions and Try again...|
|MUSERINFONOTFOUND|User account info not found.|Check user info and Try again...|
|MUSERNOTFOUND|User isn't found; either it's disabled or deleted.|Check user and correct as necessary. Try again.|
|MUSERQUOTAREACHED|User quota limit reached.|Learn more: [Microsoft Graph error responses and resource types](/graph/errors) |
|MZEROBYTEFILESIZEIMPORT|You can't import a 0-byte file to a connector.|Check file and Try again...|
|PFAIL|Failed to set permission|Check permissions and Try again...|
|PFAILUNSUP|Unsupported file permissions not set.|Check permissions and Try again...|
|PSUCCESS|Set permission successfully|
|PUNSUP|Unable to set permissions.|Check permission settings and Try again...|
|MJOBNOTCOMPLETED |Migration job (upload package) isn't submitted or hasn't finished uploading yet. |Try again.| 
|MJOBERROR |Item level failure when processing the migration job (upload package). |Check file name and content. Try again.| 
|MJOBFATALERROR|Failed to process the migration job (upload package). All items in the package will be marked as failure. |Try again. |


## Status codes

Status codes provide the final status of the scan and migration tasks. 

|Status Code |Message |
|:-----|:-----|
|100 |Success |
|101 |Success. No files needed copying |
|102 |Success. Some files aren't supported by Destination name and weren't transferred. |
|120 |Success. Some files aren't supported by Source name and weren't transferred. |
|122 |Success. Some unsupported files not transferred. |
|201 |Some upload errors. Try again.|
|202 |No files copied. Some upload errors. Try again.|
|210 |Some download errors. Try again.|
|220 |No files copied. Some download errors. Try again.|
|211 |Some download and upload errors. Try again.|
|222 |No files copied. Some download and upload errors. Try again.|
|227 |Some files aren't supported on the source or destination |
|230 |Canceled|
|250 |Already running |
|260 |Storage Quota Exceeded on Destination name |
|261 |Quota API Exceeded on Destination name |
|300 |Running |
|302 |Waiting for Microsoft batch processing |
|400 |General failure. Try again.|
|401 |Couldn't upload anything. Try again.|
|402 |Connector authorization failed. Try reauthorizing Source name or Destination name |
|403 |No status. Try again.|
|404 |Crashed. Try again.|
|405 |Crashed. Try again.|
|410 |Couldn't connect to Source name. Try reauthorizing. |
|411 |Invalid root path |
|422 |User for schedule not found |
|423 |Connector not found |
|490 |Ended by company name Admin. Try again.|
|491 |Microsoft migration reporting communication failure. Try again.|
|500 |Unknown, contact support |
|600 |Queued to start. |
|601 |Queued to start. |
|620 |Running pre-checks |

