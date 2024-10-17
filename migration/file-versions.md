---
ms.date: 10/11/2024
title: File Versions
ms.reviewer: heidip
ms.author: kbchen
author: MetMS2023
manager: DAPODEAN
recommendations: true
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: microsoft-365-migration
ms.localizationpriority: medium
mscollection:
- SPMigration
- M365-collaboration
- m365initiative-migratetom365
search.appverid: MET150
description: "How to configure file version migration setting in Migration Manager."
---

# File Versions

Migration Manager now supports migrating version histories along with each of the files. Customers can now transfer either a specific number of versions or all versions from cloud sources to Microsoft 365.

>[!NOTE]
> Currently, file version migration is supported only for a Google scenario.

## Version settings 

To configure file versions setting in a cloud migration project:

1. Select **Project Settings** in the top-right toolbar.

2. Select the **Advanced** tab.

3. Configure the **File versions** settings as listed.

    - **Do not migrate file version** (default setting): Migrate only the most recent version of each file.

    - **Migrate a specific number of file versions**: Specify a fixed number of versions to migrate for each file.

    - **Migrate all existing file versions**: Migrate all available versions (up to 50,000) of each file.

>[!NOTE]
> Version settings can also be customized at the task level in **Task settings**.

## Performance impact 

File version migration can significantly increase the load on the source API quota, transmission network, and destination storage. To ensure optimal performance, it's strongly recommended to choose **Migrate a specific number of file versions** and set the number to **no more than 10**.

>[!NOTE]
> Laboratory testing indicates that native Google format files may experience throttling when migrating more than 10 versions. This performance restriction doesn't apply to other file types.

## Reporting 

Each file corresponds to a row in the **Migration detailed report**. If version migration is enabled, a file is marked as successful only when all its versions are successfully migrated.
