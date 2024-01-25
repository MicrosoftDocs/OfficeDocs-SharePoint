---
title: "Migration time estimator tool in Migration Manager"
ms.date: 09/26/2023
ms.reviewer: 
ms.author: heidip
author: MicrosoftHeidi
manager: jtremper
recommendations: true
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: microsoft-365-migration
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
2. If you are **not** connected to the source, select the Migration time estimator from the overview page.  If you are connected to the source, select the Migration Time Estimator from the tool bar on the top right of the screen.

:::image type="content" source="media/mm-time-estimator.png" alt-text="time estimator":::



3. Enter the values:
  - Number of drives/users (required)
  - Total data size in GB (required)
  - Total file count (optional)

4. After entering your information, select **Estimate**. A migration time estimate is generated within moments.

>[!Important]
>It is important to recognize that the generated estimations are **preliminary** and based on big date fitting. They may vary due to individual factors, including, but not limited to:
>
>- Adverse network conditions
>- Large average file size
>- Source rate limiting, reaching request quotas, or other performance impediments at the source
>- Activation of File Level Permission (FLP), which could potentially decelerate the migration process
>- Migrations occurring during peak hours
>- Elevated-cost transfers (for example, Google Docs exports)
>- SharePoint Job Processing throughput

## Best Practices

- We advise using the Migration Time Estimator as an initial approximation before you connect to the source.
- After connecting to the source, run an overall scan to attain a more precise estimate, which will be displayed in the Migrations section.

>[!Note]
> Currently, the more accurate scanning estimations is available only for Google Drive migrations.

