---
title: "Migration Manager reports for cloud migrations"
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
description: "Learn about the reports available when migrating from another cloud provider using Migration Manager in Microsoft 365."
---

# Migration Manager reports for cloud migrations

## Project level reports

### Project summary report

|**Column**|**Description**|
|:-----|:-----|
|taskId|task id|
| transactionId|transaction id|
| sourceName|task name|
| sourcePath|source path|
| tags|tags|
| transactionSize|sum of source file size|
| folderCount|source folder count|
| fileCount|source file count|
| uniquePermissions|sum of SourceAclsUnique in ItemMetadata, |SourceAclsUnique means Number of unique ACLs in the source item|
| maximumPathLength|sum of SourcePathLength in ItemMetadata|
| totalDataBytes|Total skipped source files|
| totalDataMB| Total skipped source file data in MB|
| totalFiles|Total skipped source file|
| scanStatusCode|transaction status code|
| scanStatus| transaction status text|
| mostRecentScan |most recent scan time|



### ScanSummary.csv


|**Column**|**Description**|
|:-----|:-----|


### Longpaths.csv


|**Column**|**Description**|
|:-----|:-----|



### FileExtension.csv


|**Column**|**Description**|
|:-----|:-----|



### LargeFileSizes.csv


|**Column**|**Description**|
|:-----|:-----|


### MigrationSummary.csv


|**Column**|**Description**|
|:-----|:-----|



### Migration errors.csv


|**Column**|**Description**|
|:-----|:-----|




## Task level reports

### ScanLog.csv


|**Column**|**Description**|
|:-----|:-----|
|SourceSize|The size of the source item in bytes|
|SourceAclsTotal|The number of ACLs in the source item|
|SourceAclsUnique |The number of unique ACLs in the source item|
|TransactionSize | The sum of SourceSize, in bytes|



Operation step

|||
|:-----|:-----|
|item/skip |the file was already migrated on a previous pass and is being skipped on this incremental run.|
|item/listPermissions|permissions were applied to this file on this pass.|
|transfer/complete |transfer has now finished Successfully|
|collection/postList |an action is being taken on a folder (usually the folder being created in the Dest)|


### MigrationLogs.csv


|**Column**|**Description**|
|:-----|:-----|


