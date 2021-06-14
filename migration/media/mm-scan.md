---
title: "Migrate Manager Scan preview"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: serdars
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
localization_priority: Priority
ms.collection: 
- m365solution-migratetom365
- m365solution-scenario
- M365-collaboration
- SPMigration
search.appverid: MET150
description: Preview of the scans feature in Migration Manager.
---
# Migration Manager scan (preview)


![Scan dashboard preview](/media/mm-scan-dashboard.png)

What are the readiness checks that are being performed during the scan?



Columns for File share scans:

|Column|Description|
|:-----|:-----|:-----|
|Source path|File path or URL of the location of the data being migrated.|
|Scan status|Status of each task (success, failure, in progress, not started)|
|Data size||
|File count|The total number of files, excluding files filtered out based settings or scanned potential issues.|
|Folder count|The total number of folders in the source path.|
|Max path length|The longest path length for an item in this account.  The path length is calculated to include the tenant URL, user site, path, and any character encoding. Microsoft 365 allows a maximum of 400 characters.|
|Root permissions||
|Last accessed||
|Created on|This is the date the scan was created|
|Migration Readiness|Status of readiness checks. A value of "Warning" indicates that one or more issues  need to be addressed before moving the task to migration.|
|Task ID|Unique identifier for a migration task.|