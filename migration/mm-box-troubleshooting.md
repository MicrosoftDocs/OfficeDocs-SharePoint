---
title: "Troubleshooting Migration Manager Box"
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
localization_priority: Priority
ms.collection: 
- M365-collaboration
- SPMigration
search.appverid: MET150
description: "Troubleshooting the Migration Manager Box feature."
---

# Troubleshooting after your Box migration

Review these areas if you are experiencing issue with your Box migration.


## Automatic reruns

When a run ends, an automatic rerun may occur if the conditions listed under each scenario are met.

|Scenario|Conditions|
|:-----|:-----|
|The task is being scanned OR migrated for the first time|When a task is first scanned or migrated, it may trigger reruns. </br>When a task scan is started and then canceled. If that task is scanned again, it will NOT trigger reruns, because it was not the first time the task was scanned.|
|More automatic reruns are still available|A task will be automatically rerun a maximum of three times. </br>A first task scan/migrate action can result in triggering a total of four transactions: the original transaction (run), and three additional attempts (reruns). Six reruns can be triggered at the most: 3 for the initial scan, and 3 for the initial migration.|
|Last transaction status codes|An automatic rerun may occur if the last transaction ends with any of the following status codes: 201, 202, 210, 220, 211, 401, 403,404, 405, 406, or 491.|

## Canceling a transfer
A transfer can be canceled under the following conditions:
- The task is "Queued", and has a status code 600 or 601.
OR
- The task is "Running", and has a status code 620 or 300.



## Incremental feature

Our incrementals are delta operations which compare files in your source to files in Microsoft 365. Using this comparison, we copy anything that is new or has changed. This lets us to keep Microsoft 365 data up to date when the very final cut-over of users occurs. These incremental passes are an important part of our process.

**Technical clarification**: We compare what you have in your source to what is in Microsoft 365 and we only transfer anything that doesn't already exist, or has a newer timestamp.

## 'Lost files'

During a transition where sharing paradigms change, there are many users who claim, “My files are lost!”

This is common if they are not in clear communication about how the sharing structure changes when they log in to Microsoft 365. This can be mitigated with a clear communication strategy.