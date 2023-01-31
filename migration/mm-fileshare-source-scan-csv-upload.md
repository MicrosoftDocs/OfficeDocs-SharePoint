---
title: "Upload file share sources to Migration Manager using a CSV file."
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: serdars
recommendations: true
audience: ITPro
f1.keywords:
- CSH
ms.topic: article
ms.service: sharepoint-online
ms.subservice: sharepoint-migration
ms.localizationpriority: high
ms.collection: 
- SPMigration
- M365-collaboration
search.appverid: MET150
description: "Bulk upload file share sources to scan in Migration Manager."
---

# Upload file share sources using a CSV file

Migration Manager lets you use a comma-separated (CSV) file to bulk upload your file share sources to scan. Use any text editor, or an application like Excel, to create the CSV file. You can also download the blank CSV template from Migration Manager file share workflow.

:::image type="content" source="media/mm-fileshare-upload-csv.png" alt-text="mm-fileshare-source-choice":::

- **Column heading**.  You can optionally use the column headings in your CSV file to make your file easier to read.
- **UTF-8**.  The encoding of the CSV file must be UTF-8.


## Using a comma-separated value (CSV) file for bulk upload

Create a single column CSV file. There is only 1 column, source path.

 :::image type="content" source="media/mm-fileshare-addsource-upload.png" alt-text="upload a file share csv file":::

 **To create a CSV file for data migration**
  
The following example uses Excel to create the CSV file.
  
1. Start Excel. 
2. Enter source paths. Enter one source path per row. *Required.* 
3. Close and save as a Comma delimited (\*.csv) file.