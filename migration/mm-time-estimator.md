---
title: "Migration time estimator tool in Migration Manager"
ms.date: 08/30/2023
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
ms.localizationpriority: high
ms.collection: 
- M365-collaboration
- SPMigration
search.appverid: MET150
description: Learn about how Migration Manager estimates the length of time your migration project will take to complete.
---
# Migration time estimator tool in Migration Manager

The Migration Time Estimator acts  as a rapid estimation tool to gauge the anticipated duration of migration before it starts. This tool can be used for cloud migration scenarios including Google Drive, Dropbox, Box, and Egnyte.

## Run the time estimator

This tool can be used before or after you connect to the source. A connection to the source isn't required to run the estimator.

1. Select **Migration** in the SharePoint admin center, choose your source location, and then **Get started**.
2. From the top right tool bar, choose the Migration Time Estimator.
3. Enter the required details, as shown here:

  |Fields|Requirement type|Formats|Input upper limit|
  |:-----|:-----|:-----|:-----|
  |Number of drives/users|Mandatory|Positive integer|10^6|
  |Total data size in gigabytes|Mandatory|Positive number|10^9|
  |Total file count|Optional|Positive integer|3*10^9|

4. After entering your information, select **Estimate**. A migration time estimate is generated within moments.


>[!Important]
>It is important to recognize that the Migration Time Estimator's estimations are **preliminary** and based on big date fitting. They may vary due to individual factors, including, but not limited to:

- Adverse network conditions
- Large average file size
- Source rate limiting, reaching request quotas, or other performance impediments at the source
- Activation of File Level Permission (FLP), which could potentially decelerate the migration process
- Migrations occurring during peak hours
- Elevated-cost transfers (for example, Google Docs exports)
- SharePoint Job Processing throughput

## Best Practices

- We advise using the Migration Time Estimator as an initial approximation before you connect to the source.
- After connecting to the source, run an overall scan to attain a more precise estimate, which will be displayed in the Migrations section.

>[!Note]
> Currently the most accurate scanning estimations are for Google Drive migrations.

