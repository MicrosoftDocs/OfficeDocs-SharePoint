---
ms.date: 09/09/2020
title: Mover transfer status codes 
author: JoanneHendrickson
ms.author: jhendr
manager: serdars
recommendations: true
audience: ITPro
ms.topic: article
ms.service: sharepoint-online
ms.subservice: sharepoint-migration
ms.localizationpriority: high
ms.collection:
- SPMigration
- M365-collaboration
- m365initiative-migratetom365
search.appverid: MET150
description: "Mover transfer status codes"
---
# Mover transfer status codes

>[!Important]
>**Mover is now retired for all Admin led migrations**. The ability to migrate from Google Drive, Box, Dropbox, and Egnyte has been fully integrated into Migration Manager. For full details see: [Mover retirement timeline](mover-retirement-timeline.md).  Migration Manager does not support the migration of Amazon S3 or Azure blob storage.
>
>All FastTrack-led migrations have transitioned to Migration Manager.
>
>**Tenant to tenant migration**. Cross-tenant OneDrive migration is now available outside of Migration Manager. Learn more here: [Cross-tenant OneDrive migration](/microsoft-365/enterprise/cross-tenant-onedrive-migration).  
>
>A cross tenant migration solution for SharePoint is currently being developed and in private preview.  To learn more, see [How to participate in the Cross-tenant SharePoint migration preview](/microsoft-365/enterprise/cross-tenant-sharepoint-migration).



## Automatic reruns

When a run ends, an automatic rerun may occur if the conditions listed under each scenario are met.

|Scenario|Conditions|
|:-----|:-----|
|The task is being scanned OR migrated for the first time|When a task is first scanned or migrated, it may trigger reruns. </br>When a task scan is started and then canceled. If that task is scanned again, it will NOT trigger reruns, because it wasn't the first time the task was scanned.|
|More automatic reruns are still available|A task will be automatically rerun a maximum of three times. </br>A first task scan/migrate action can result in triggering a total of four transactions: the original transaction (run), and three additional attempts (reruns). Six reruns can be triggered at the most: 3 for the initial scan, and 3 for the initial migration.|
|Last transaction status codes|An automatic rerun may occur if the last transaction ends with any of the following status codes: 201, 202, 210, 220, 211, 401, 403,404, 405, 406, or 491.|

## Canceling a transfer
A transfer can be canceled under the following conditions:
- The task is "Queued", and has a status code 600 or 601.
OR
- The task is "Running", and has a status code 620 or 300.

## Status codes

|Mover status code|Message|
|:-----|:-----|
|100| Success|
|101| Success. No files needed copying|
|102| Success. Some files aren't supported by *Destination name* and weren't transferred|
|120| Success. Some files aren't supported by *Source name* and weren't transferred|
|122| Success. Some unsupported files not transferred|
|201| Some upload errors, please retry|
|202| No files copied. Some upload errors, please retry|
|210| Some download errors, please retry|
|220| No files copied. Some download errors, please retry|
|211| Some download and upload errors, please retry|
|222| No files copied. Some download and upload errors, please retry|
|227| Some files aren't supported on the source or destination|
|230| Canceled|
|250| Already running|
|260| Storage Quota Exceeded on *Destination name*|
|261| Quota API Exceeded on *Destination name*|
|300| Running|
|302| Waiting for Microsoft batch processing|
|400| General failure, please retry|
|401| Couldn't upload anything, please retry|
|402| Connector authorization failed. Try reauthorizing *Source name* or *Destination name*|
|403| No status, please retry|
|404| Crashed, please retry|
|405| Crashed, please retry|
|410| Couldn't connect to *Source name*. Try reauthorizing|
|411| Invalid root path|
|422| User for schedule not found|
|423| Connector not found|
|490| Ended by *company name* Admin, please retry|
|491| Microsoft migration reporting communication failure, please retry|
|500| Unknown, contact support|
|600| Queued to start, please be patient|
|601| Queued to start, please be patient|
|620| Running prechecks|
