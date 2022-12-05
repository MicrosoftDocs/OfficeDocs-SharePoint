---
title: "Migration Manager Cloud migration reports"
ms.reviewer:
ms.author: jhendr
author: JoanneHendrickson
manager: serdars
recommendations: true
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: articlems.service: sharepoint-online
ms.subservice: sharepoint-migration
ms.localizationpriority: medium
mscollection:
- SPMigration
- M365-collaboration
- m365initiative-migratetom365
search.appverid: MET150
description: "Learn about reports for cloud to cloud migration using Migration Manager in Microsoft 365."
---
# Migration Manager:  Cloud migration reports 

Migration Manager generates a series of scan log and reports for cloud migration scenarios.

## How to download 

**Scan log:** Select a scan task (each row in the Scans UI table represents a scan task) in the Scans UI, select “Download scan log” in the action bar. 

**Scan reports:** Select “Download reports” in the action bar directly in the Scans UI. Don't select any individual scan task. Scan reports are overall reports for all scan tasks. 

## Scan reports

**Scan log**

- ScanLog.csv 

**Scan reports**

- FileExtensions.csv 
- LargeFileSizes.csv 
- LongPaths.csv 
- ScanErrors.csv 
- ScanSummary.csv 

### ScanLog.csv 

ScanLog.csv contains the final scan status of all items of the task selected. Each row in the .csv file represents an item of the selected task. 

|Column|Description|
|:-----|:-----|
|TaskId |ID of the selected task, used for debugging. |
|TransactionId |Whenever a task is run, it becomes a transaction. The transaction ID is used for debugging.|
|Name |Display name of the source account. |
|SourcePath |Source path of the selected source account. |
|OperationStep |Operation step of the item. |
|Status |Final scan status of the item. “Skipped” indicates the scan has completed, and the item is ready to be migrated. |
|FailureCode |Failure code of the item. It shows "none" when the item status is "Success". Check the link to find out more. |
|FailureDescription |Description of the failed item. This column is blank if the item status has a value of "Success". Check the link to find out more. |
|FullPath |Full path of the item in the source. |
|SourcePathDepth |Path depth of the item in the source.  |
|SourceBasename |Base name of the item in the source. If the item is a root folder, this field is blank. |
|SourceExtension |File extension of the item in the source. If the item is a root folder, this field is blank. |
|SourceType |Type of folder in the source. |
|SourceSize |Data size of the item in the source. |
|SourceAclsTotal |The number of users and groups with whom the item is shared. |
|SourceAclsUnique |The number of users and groups with whom the item is shared and that are different from its parent. |
|DestinationPath |Full path of the item in the destination. |
|DestinationPathDepth |Path depth of the item in the destination.  |
|DestinationBasename |Base name of the item in the destination. If the item is a root folder, this field is blank. |
|DestinationExtension |File extension of the item in the destination. If the item is a root folder, this field is blank. |
|DestinationLocation |The web URI of the item in destination. |
|DestinationType |File of folder in the destination. |
|DestinationSize |Data size of the item in the destination. |

### FileExtensions.csv 

FileExtensions.csv provides the statistics of extension types existing in each task. 

|Column |	Description| 
|:-----	|:------|
|TaskId|ID of the selected task, used for debugging. |
|Name|Display name of the selected task in the source. |
|SourcePath|Source path of the selected task. |
|FullPath|	Full path of the item in the source. |
|SourceExtension|Extension type exists in the task. |
|TotalSize|Total data size of the extension type in the task. |

### LargeFileSizes.csv

LargeFileSizes.csv is a list of all items larger than 15 GB that can NOT be migrated. 

|Column |Description |
|:------|:-----|
|TaskId |ID of the selected task, used for debugging. |
|Name |Display name of the selected task in the source. |
|SourcePath |Source path of the selected task. |
|FullPath |Full path of the item in the source. |
|SourceSize |Data size in Byte of the item in the source. |
|SourceSizeInGB |Data size in GB of the item in the source. |

### LongPaths.csv

LongPaths.csv file contains a list of all items with path lengths larger than 300 and that can't be migrated. 

|Column |Description |
|:-----|:-----|
|TaskId |ID of the selected task, used for debugging. |
|Name |Display name of the selected task in the source. |
|SourcePath |Source path of the selected task. |
|FullPath |Full path of the item in the source. |
|SourcePathLength |Path length of the item in the source. |

### ScanErrors.csv 

ScanErrors.csv is a collection of all item level errors that ever occurred during the scan process of all tasks. 

|Column|Description
|:-----|:-----| 
|TaskId|ID of the selected task, used for debugging. 
|Name|Display name of the selected task in the source. 
|SourcePath|Source path of the selected task. 
|FullPath|Full path of the item in the source. 
|Action|Operation step of the item that goes wrong during the scan process. 
|FailureCode|Failure code of the item. It shows "null" when item status is "Success". Check the link to find out more. 


### ScanSummary.csv 

ScanSummary.csv is a task level summary of all scan tasks. You can find the scan results based on the scan status code revealed. 

|Column |Description |
|:-----|:-----|
|TaskId |ID of the selected task, used for debugging. |
|TransactionId |Every time when task is run, it's a transaction. Transaction ID is used for debugging. |
|StartTime |Starting time in UTC of the scan task. |
|EndTime |Ending time in UTC of the scan task. |
|Name |Display name of the selected task in the source. |
|SourcePath |Source path of the selected task. |
|Tags |Predefined tags of the task. |
|ScannedData-Byte |Data size in Byte scanned in the source. |
|ScannedFolders |Number of folders scanned in the source. |
|ScannedFiles |Number of files scanned in the source. |
|UniquePermissions |Number of users and groups with whom the item is shared and that are different from its parent. |
|MaximumPathLength |The max path length among all the items in the source. |
|DataReadyToBeMigrated-Byte |Data size in Byte that is ready to be migrated. |
|FoldersReadyToBeMigrated |Number of Folders that are ready to be migrated. |
|FilesReadyToBeMigrated |Number of files that are ready to be migrated. |
|ScanStatusCode |Scan status code of the scanned task, find out more on status code. |
|ScanStatus |Scan status of the scanned task. |
|MostRecentScan |The most recent scan time in UTC of the task. |


## Migration Reports 

Migration Manager generates a series of migration log and reports for cloud migration scenarios: 

Migration log 

- MigrationLog.csv 

Migration reports 

- Migration errors.csv 
- Migration summary.csv 

**How to download** 

**Migration log:** Select on a migration task (each row in the Migrations UI table represents a migration task) in the Migrations UI, select “View logs” in the side page popped up to view the log online, you can also select “Download CSV” in the subsequent page to download the MigrationLog.csv. 

**Migration reports:** Select “Download reports” in the action bar directly in the Migrations UI. Do NOT select any migration task, as migration reports are overall reports of all migration tasks. 



### MigrationLog.csv 

MigrationLog.csv reveals the final migration status of all items of the task selected. Each row in the csv file represents an item of the selected task. 

|Column |Description |
|:-----|:-----|
|TaskId |ID of the selected task, used for debugging. |
|TransactionId |Every time when task is run, it becomes a transaction. Transaction ID is used for debugging. |
|Name |Display name of the source account. |
|SourcePath |Source path of the selected source account. |
|OperationStep |Operation step of the item. |
|Status |Final migration status of the item. |
|FailureCode |Failure code of the item. It shows "none" when item status is "Success". Check the link to find out more. |
|FailureDescription |Failure description of the failed item. If the item status value is "Success", this field is left blank. Check the link to find out more. |
|FullPath |Full path of the item in the source. |
|SourcePathDepth |Path depth of the item in the source.  |
|SourceBasename |Base name of the item in the source. If the item is a root folder, this field is blank. |
|SourceExtension |File extension of the item in the source. If the item is a root folder, this field is blank. |
|SourceType |Type of folder in the source. |
|SourceSize |Data size of the item in the source. |
|SourceAclsTotal |The number of users and groups with whom the item is shared. |
|SourceAclsUnique |The number of users and groups with whom the item is shared and that are different from its parent. |
|DestinationPath |Full path of the item in the destination. |
|DestinationPathDepth |Path depth of the item in the destination.  |
|DestinationBasename |Base name of the item in the destination. If the item is a root folder, this field is blank. |
|DestinationExtension |File extension of the item in the destination. If the item is a root folder, this field is blank. |
|DestinationLocation |The web URI of the item in destination. |
|DestinationType |File of folder in the destination. |
|DestinationSize |Data size of the item in the destination. |


### Migration errors.csv 

Migration errors.csv is a collection of all item level errors that ever occurred during the migration process of all tasks. 

|Column |Description |
|:-----|:-----|
|TaskId|ID of the selected task, used for debugging. |
|Name|Display name of the selected task in the source. |
|SourcePath |Source path of the selected task. |
|FullPath|Full path of the item in the source. |
|Action|Operation step of the item that goes wrong during the migration process. |
|FailureCode|Failure code of the item. It shows "null" when item status is "Success". Check the link to find out more. |
|FailureDescription |Failure description of the failed item. If the item status is "Success", this field will be blank. Check the link to find out more.|


### Migration summary.csv 

Migration summary.csv is a task level summary of all migration tasks. You can find the migration results based on the status code revealed. 

|Column |Description |
|:-----|:-----|
|TaskId |ID of the selected task, used for debugging. |
|TransactionId |Every time when task is run, it's a transaction. Transaction ID is used for debugging. |
|StartTime |Starting time in UTC of the migration task. |
|EndTime |Ending time in UTC of the migration task. |
|Name |Display name of the selected task in the source. |
|SourcePath |Source path of the selected task. |
|Tags |Predefined tags of the task. |
|StatusCode |Status code of the migration task, find out more on status code. |
|FoldersCreated |Folder created in the destination for the migration. |
|LatestCopiedFiles |Number of files copied to destination during the latest transaction. |
|AlreadyCopiedFiles |Number of files copied to destination in the transaction ran before. |
|TotalCopiedFiles |Total number of files ever copied to destination. |
|FilesFailed |Number of files that failed to copy to destination during the latest transaction. |
|LatestCopiedData |Data size copied to destination during the latest transaction. |
|AlreadyCopiedData |Data copied to destination in the transaction ran before. |
|TotalCopiedData |Total data size ever copied to destination. |
|DataFailed |Data size that failed to copy to destination during the latest transaction. |
|Filters |Filter rules that applied during the latest transaction. |
|FilteredFiles |Number of files NOT copied to destination during the latest transaction due to the filter rules. |
|FilteredData |Data NOT copied to destination during the latest transaction due to the filter rules. |


## Failure codes

Failure codes demonstrate item level errors during both the scan and migration process.

|Failure code|Description |User action|
|:-----|:-----|:-----|
|MACCESSDENIED|User denied access.|Check permissions and try again.|
|MACCESSTOKENNULL|Failed to execute request as connector authorization failed.|Unexpected error. Try again.|
|MAUTHACCESSTOKEN|Connector authorization failure. Failed to get access token.|Unexpected error. Try again.|
|MAUTHACCESSTOKENINVALID|Connector authorization failure. The API request failed because the access token is invalid or expired.|Retry.|
|MAUTHCALLERNOTAUTHENTICATED|Connector authorization failed. The service isn't allowing to connect as it doesn't recognize the caller.|Try again.|
|MAUTHMOVERAPP|Mover Application in Users Admin Account/tenant needs to be authorized.|To authorize this connector, you need to grant permissions to the Mover application. Try again.|
|MAUTHNOCODE|Connector authorization failed as auth code isn't provided.|Try again.|
|MAUTHNOEMAIL|Connector authorization failure. Failed to get email from claim.|Unexpected error. Try again.|
|MAUTHNOIDTOKEN|Connector authorization failure. Failed to get ID token from access token.|Unexpected error. Try again.|
|MAUTHNOTENANT|Connector authorization failed; no tenant/enterprise ID found. Tenant = Enterprise. Tenant is the term in MS/Azure and Enterprise is used by Box and others.|Try again.|
|MAUTHREFRESHTOKEN|Connector authorization failure. Failed to get refresh token.|Try again.|
|MAUTHUSERNOTADMIN|Connector authorization failed; user doesn't have admin role.|Check permissions and try again.|
|MAZUREUPLOAD|Failed to submit the migration job to Migration API after the files were uploaded to the Azure blob.| Try again.|
|MBADREQUEST|Bad request when operating on source or destination item.|Unexpected error.  Try again.|
|MCONNECTORNOTFOUND|Connector not found in database.|Check connector settings.  Try again.|
|MCORRELATE|Collection correlates missing source listing.|Confirm source location, try again.|
|MDESTINATIONNOTWRITABLE|You don't have write access to the destination. |Check permissions and try again.|
|MDUPLICATE|Duplicate. This file already exists in your destination location.|Confirm file is in destination already.|
|MEMPTYMETADATA|Unable to find metadata. |Try again.|
|MEXPORTFILERESTRICTED|This file is restricted, and can’t be migrated from the source.|Check to see if this file has legal restrictions such as copyright claims.|
|MEXPORTFILEUNSUPPORTED|Unsupported file type. |You can't migrate this file from the source.|
|MEXPORTFILEUNSUPPORTEDMIMETYPE|Unsupported file type.|You can't migrate this file from the source. Check file at source.|
|MFAILEDGETROOTITEM|Failed to get root folder listing. This is set in both Google and Office365 connector|Try again.|
|MFILEIMPORT|This file type isn't supported in the destination location. |Check source file.|
|MFILELOCKED|"File is locked, and can't download or get metadata. |Unlock file.  Try again.|
|MFILENAMELENGTH|Filename exceeds maximum allowable length. |Rename file and try again.|
|MFILESIZEINCORRECT|Downloaded file is smaller than expected.|Check file for size and compare.  Try again.|
|MGETFOLDERACLS|Failure to get shared folder membership. |Check folder permissions and try again.|
|MHTTPCONNECTION|Connection failure.|Check your network and try again.|
|MINVALIDEMAIL|Invalid user email; unable to find user with that email. |Check user name and try again.|
|MINVALIDPAGESIZE|The page size for connector pagination must be greater than zero.|Try again.
|MINVALIDPARENTID|Item has no parent ID. Id-based connectors require the item to have a parent ID.|Check file and try again.|
|MINVALIDPATH|Path is invalid.|Check path and try again.|
|MINVALIDRESPONSE|Invalid response from API call. |Try again.|
|MITEMPATHLENGTH|Item path exceeds length restrictions.|Check file path for length and try again.|
|MLARGEFILESIZEEXPORT|File exceeds maximum size for export from the source.|Check file size.|
|MLARGEFILESIZEIMPORT|File exceeds maximum allowed size for import into destination. |Check file size. |
|MLISTGROUP|API request to list groups for connector failed.| This may be caused by an invalid or throttling. Try again. |
|MLISTING|Folder listing failed.|Try again.|
|MLISTUSER|Failure to get user listing. This may be caused by an invalid requestor throttling. | Try again. |
|MLOCKACQ|Failed to acquire lock within timeout period and obtain new access token.|Try again.|
|MNONDESTRUCTIVEOPTIONENABLED| Unable to delete file or folder.|Try again.|
|MNOPARENT|Item doesn't have a parent item.|Check file and try again.|
|MNOTAFILE|The path refers to something that isn't a file.|Check the path and correct as necessary. Try again.|
|MNOTAFOLDER|The path refers to something that isn't a folder.|Check the path and correct as necessary.  Try again.|
|MNOTFOUND|Item not found.|Check file and try again.|
|MNOTIMPLEMENTED|Method not implemented for connector. |Try again.|
|MNOTPERMITTED|Can't traverse to the folder level; can't perform actions outside a users folder.|Check permissions and try again.|
|MNOTUSERORTEAMDRIVE|Confirm that the name of the item in the source service matches what you have in the task's source path. Note: Google Suite allows invisible characters to be added to item names. We advise that your rename the item in the source service to ensure there's no invisible characters and then use that same name in the task source path.|
|MOWNERNOTFOUND|The original owner was removed or its information wasn't found.|Reassign ownership of the file.|
|MPATHMALFORMED|Invalid path format. | Check your source and try again.|
|MSERVICENOTAVAILABLE|Service unavailable.|Try again.|
|MSETITEMPERMISSION|Failed to set permission. Failure may be caused by throttling.|Try again.|
|MSOURCENOTREADABLE|Unable to read the source directory. |Confirm source location. Try again.|
|MSTORAGEQUOTAREACHED|Storage quota exceeded for connector.|Increase storage limit and try again.|
|MTHROTTLE|API requests made by connector are getting throttled.|Try again.|
|MUNVERIFIEDPARENT|Item doesn't have a verified parent item. |Check file and try again.|
|MUPDATEITEMPERMISSION|Failed to remove permissions. |Try again.|
|MUSERCOUNT|Unexpected failure to get user count. |Try again.|
|MUSERFORBIDDEN|The current user doesn't have permission to access the file or folder.|Check permissions and try again.|
|MUSERINFONOTFOUND|User account info not found.|Check user info and try again.|
|MUSERNOTFOUND|User isn't found; either it's disabled or deleted.|Check user and correct as necessary. Try again.|
|MUSERQUOTAREACHED|User quota limit reached.|Learn more: [Microsoft Graph error responses and resource types](/graph/errors) |
|MZEROBYTEFILESIZEIMPORT|You can't import a 0-byte file to a connector.|Check file and try again.|
|PFAIL|Failed to set permission|Check permissions and try again.|
|PFAILUNSUP|Unsupported file permissions not set.|Check permissions and try again.|
|PSUCCESS|Set permission successfully|
|PUNSUP|Unable to set permissions.|Check permission settings and try again.|
|MJOBNOTCOMPLETED |Migration job (upload package) isn't submitted or hasn't finished uploading yet. |Try again.| 
|MJOBERROR |Item level failure when processing the migration job (upload package). |Check file name and content. Try again.| 
|MJOBFATALERROR|Failed to process the migration job (upload package). All items in the package will be marked as failure. |Try again. |


## Status codes

Status codes demonstrate the final status of the scan/migration tasks. 

|Status Code |Message |
|:-----|:-----|
|100 |Success |
|101 |Success. No files needed copying |
|102 |Success. Some files aren't supported by Destination name and weren't transferred |
|120 |Success. Some files aren't supported by Source name and weren't transferred |
|122 |Success. Some unsupported files not transferred |
|201 |Some upload errors, please retry |
|202 |No files copied. Some upload errors, please retry |
|210 |Some download errors, please retry |
|220 |No files copied. Some download errors, please retry |
|211 |Some download and upload errors, please retry |
|222 |No files copied. Some download and upload errors, please retry |
|227 |Some files aren't supported on the source or destination |
|230 |Canceled |
|250 |Already running |
|260 |Storage Quota Exceeded on Destination name |
|261 |Quota API Exceeded on Destination name |
|300 |Running |
|302 |Waiting for Microsoft batch processing |
|400 |General failure, please retry |
|401 |Couldn't upload anything, please retry |
|402 |Connector authorization failed. Try reauthorizing Source name or Destination name |
|403 |No status, please retry |
|404 |Crashed, please retry |
|405 |Crashed, please retry |
|410 |Couldn't connect to Source name. Try reauthorizing |
|411 |Invalid root path |
|422 |User for schedule not found |
|423 |Connector not found |
|490 |Ended by company name Admin, please retry |
|491 |Microsoft migration reporting communication failure, please retry |
|500 |Unknown, contact support |
|600 |Queued to start, please be patient |
|601 |Queued to start, please be patient |
|620 |Running pre-checks |
