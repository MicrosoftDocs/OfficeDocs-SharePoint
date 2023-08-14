---
ms.date: 08/11/2023
title: "Setting Google Sheets permissions for Migration Manager sheet scans"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: serdars
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.subservice: sharepoint-migration
ms.localizationpriority: high
ms.collection: 
- m365solution-migratetom365
- m365solution-scenario
- M365-collaboration
- SPMigration
- highpri
ms.custom: admindeeplinkSPO
search.appverid: MET150
description: Migrate Google spreadsheet requirements Migration Manager sheet scan of Google spreadsheet
---
# Setting Google Sheets permissions for Migration Manager sheet scan

>[!Note]
>The "sheet scan" feature mentioned in this article is currently in **private preview** and not generally available.

You must grant Google Spreadsheet permissions before Migration Manager can run a **sheet scan** on Google Sheets.

## Set permissions

To confirm you have granted this permission: 

1. Sign in with your Google admin credentials to the Google Marketplace.
2. Under Drive, verify that "See all your Google Sheets spreadsheets” permission shows **Granted**.  

:::image type="content" source="media/mm-google-permission-gsheet.png" alt-text="google permissions granting for gsheet":::

3. If it hasn't been granted, select **Grant access** at the top of the screen to grant permission.
4. Once permission has been granted, Migration Manager can run seep scans for Google Sheets spreadsheet files.

