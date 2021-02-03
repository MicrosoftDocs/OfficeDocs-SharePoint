---
title: Mover transfer status codes 
author: JoanneHendrickson
ms.author: jhendr
manager: serdars
audience: ITPro
ms.topic: article
ms.service: sharepoint-online
localization_priority: Priority
ms.collection:
- SPMigration
- M365-collaboration
search.appverid: MET150
description: "Mover transfer status codes"
---
# Mover transfer status codes


When a run ends, an automatic re-run may occur if it meets the conditions listed under each scenario are met.

**The task is being scanned OR migrated for the first time:**
- When a task is first scanned or migrated, it may trigger reruns. 
- When a task scan is started and then canceled. If that task is scanned again, it will NOT trigger reruns,  because it was not the first time the task was scanned.


**More automatic reruns are still available.** 
- A task will be automatically rerun a maximum of three times. 
- A first task scan/migrate action can result in triggering a total of four transactions: the original transaction (run), and the three additional attempts (reruns). Six reruns can be triggered at the most: 3 for the initial scan, and 3 for the initial migration.

**Canceling the transfer**
- If a task is in "Queued" state, status code 600, 601 can be canceled.
- If the task is in "Running" state, status code 620, 300 can be canceled

**The last transaction ended in any of these status codes:**

 - 201
 - 202
 - 210
 - 220
 - 211
 - 401
 - 403
 - 404
 - 405
 - 406
 - 491

An automatic re-run may occur when: 

|Scenario|Conditions|
|:-----|:-----|
|The task is being scanned OR migrated for the first time|- When a task is first scanned or migrated, it may trigger reruns. </br>- When a task scan is started and then canceled. If that task is scanned again, it will NOT trigger reruns,  because it was not the first time the task was scanned.|
|More automatic reruns are still available| </br>- A task will be automatically rerun a maximum of three times. </br>- A first task scan/migrate action can result in triggering a total of four transactions: the original transaction (run), and the three additional attempts (reruns). Six reruns can be triggered at the most: 3 for the initial scan, and 3 for the initial migration.|
|Canceling the transfer|- The task is "Queued", and has a status code 600, or 601. </br>- The task is "Running", and has a status code 620, or 300.|
|The last transaction ended in any of these status codes|201, 202, 210, 220, 211, 401, 403,404, 405, 406, 491.|
<br>


|Mover status code|Message|
|:-----|:-----|
|100| Success|
|101| Success. No files needed copying|
|102| Success. Some files are not supported by *Destination name* and were not transferred|
|120| Success. Some files are not supported by *Source name* and were not transferred|
|122| Success. Some unsupported files not transferred|
|201| Some upload errors, please retry|
|202| No files copied. Some upload errors, please retry|
|210| Some download errors, please retry|
|220| No files copied. Some download errors, please retry|
|211| Some download and upload errors, please retry|
|222| No files copied. Some download and upload errors, please retry|
|227| Some files are not supported on the source or destination|
|230| Canceled|
|250| Already running|
|260| Storage Quota Exceeded on *Destination name*|
|261| Quota API Exceeded on *Destination name*|
|300| Running|
|302| Waiting for Microsoft batch processing|
|400| General failure, please retry|
|401| Could not upload anything, please retry|
|402| Connector authorization failed. Try reauthorizing *Source name* or *Destination name*|
|403| No status, please retry|
|404| Crashed, please retry|
|405| Crashed, please retry|
|410| Could not connect to *Source name*. Try reauthorizing|
|411| Invalid root path|
|422| User for schedule not found|
|423| Connector not found|
|490| Ended by *company name* Admin, please retry|
|491| Microsoft migration reporting communication failure, please retry|
|500| Unknown, contact support|
|600| Queued to start, please be patient|
|601| Queued to start, please be patient|
|620| Running pre-checks|