---
title: Mover - Create a new migration with a CSV file
ms.author: jhendr
author: JoanneHendrickson
manager: serdars
audience: ITPro
ms.topic: article
ms.service: sharepoint-online
localization_priority: Priority
ms.collection: 
- SPMigration
- M365-collaboration
search.appverid: MET150
description: "Mover - Create a new migration with a CSV file"
---
# Creating a new migration from a CSV (optional)

Sometimes you have thousands of users and a complicated directory schema that you want to import. In these cases, it's desirable to plan out your migration in a spreadsheet.

In these cases, we trust the CSV upload option is useful. This lets you lay out all your users and directories, and then provide it to us in a .csv format for us to create your migration.

## Users to migrate

Your CSV file must follow this format:

A heading for the source and destination, followed by the paths, and optional tags on each line.

`Source Path,Destination Path,Tags`</br>
`user1@example.com,user__1@corp.example.com,"Pilot, IT"`</br>
`user2@example.com,user__2@corp.example.com,"Pilot, Sales"`</br>
`user3@example.com/src dir,user3@example.com/migrated,"Pilot, IT"`</br>
`Source Shared Drive,user4@example.com/Team Folder,"Pilot, Sales"`</br>
`https://TENANT02.sharepoint.com/sites/SiteName/Shared%20Documents,user5@example.com,"Marketing, Sales"`</br>

>[!Note]
>Ensure your CSV has no spaces after each comma separated value. Values that require commas must be wrapped in quotation marks.

Sample CSV file format:

|Source Path|Destination Path|Tags|
|:-----	|:-----	|:-----	|
|user01@domain<span><span>.com|user_01@domain.<span><span>com|
|Team Folder|user_02@domain.<span><span>com|
|Shared Drive|user_03@domain.<span><span>com|
|/C:/folder|user_04@domain.<span><span>com|
|user01@domain<span><span>.<span><span>com|https<span><span>://TENANT01.<span><span>sharepoint.<span><span>com/sites/SiteName/Shared%20Documents|
|https<span><span>://<span><span>TENANT01.sharepoint.<span><span>com/sites/SiteName/Shared%20Documents|https<span><span>://TENANT02.<span><span>sharepoint.<span><span>com/sites/SiteName/Shared%20Documents|

>[!Note]
>When URL mapping to SharePoint, you must remove everything after /Shared Documents; otherwise,the URL fails.

For example, this full URL won't work:
`https://TENANT01.sharepoint.com/sites/SiteName/Shared Documents/Forms/AllItems.aspx`

Change it to:
`https://TENANT01.sharepoint.com/sites/SiteName/Shared Documents`

## Creating your CSV in Excel

To use an Excel spreadsheet to create your CSV:

1. Ensure you have two columns, one titled `Source Path`, and one `Destination Path`.
2. List the relative paths, domains, and usernames on the subsequent rows.
3. Export your spreadsheet as a CSV:
  a. Select **File**.
  b. Select **Save As**.
  c. From the **File Format** options, select **CSV**.
