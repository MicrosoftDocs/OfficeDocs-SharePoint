---
title: "Project settings in Migration Manager"
ms.date: 11/13/2023
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
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
- m365initiative-migratetom365
search.appverid: MET150
description: Learn about about configuring project settings in Migration Manager.
---

# Project settings in Migration Manager

Project settings in Migration Manager are easily accessed from the menu bar at the top of your screen.

:::image type="content" source="media/mm-project-settings-toolbar.png" alt-text="menu bar with project settings option":::

The settings are designed to support each cloud provider. Depending on what cloud provider you are migrating from, you may see different options.

:::image type="content" source="media/mm-project-settings-tab-names.png" alt-text="just the tab names of the settings categories":::

|Setting tab|Description|
|:-----|:-----|
|File & folder filters|You can limit what is migrated by customizing the settings on this page. Specify if invalid characters are allowed in a file or folder name, or choose to exclude specific file types or folder names., or by when they date create, and date modified.|
|Permissions|These settings ensure that the same users with access to files, folders, and metadata will continue to have access after migration. </br>Learn more: [**Permission settings**](mm-project-settings-permissions.md)|
|Project details|Edit your project, find your Proejct ID, or disconnect from your source.|
|Advanced|If you are migrating Google Sheets, this setting allows a scan to identify imcompatible formulas and embedded links which may affect the converted Excel files.  Learn more: [**Scan Google Sheet spreadsheets**](mm-google-sheet-scan.md).  Note: Advanced features will continue to be developed to include other cloud migrations.|

>[!Note]
>It's important to note that these settings are applied to all migrations unless you have customized individually. Changes won't be applied to migrations in progress.
