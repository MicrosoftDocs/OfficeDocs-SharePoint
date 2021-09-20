---
title: Importing tags with Migration Manager 
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
ms.localizationpriority: high
ms.collection: 
- M365-collaboration
- SPMigration
search.appverid: MET150
description: "Importing tags with Migration Manager".
---
# Importing and using tags with Microsoft Manager

Use tags manage your tasks, and your overall migration project. Tags allow you to filter your tasks and more easily navigate through quantity of sources and users to find what you need.

If you have a large migration project, you will likely migrate the content in phases or need to identify them by groupings.  Applying tags to indicate department, region, wave, or any other collection relevant to your organization helps organize and manage your migration project. With tags, you can filter, group, and keep organized.
 
Examples of tags names include the migration phase, such as Wave 1, Wave 2, etc.  Typical tag names are often the name of a department or what phase or "wave" a grouping of migrations will be done.  

The tags can be continually updated.  If, for example,  you scan a group of sources and they are ready to migrate, you can update the tags so you can identify them quickly. If a group of tasks need to be,  run again, you may tag them with "Incremental run" to identify more clearly the issue.

You can enter one or more tags per source, separating them with a semi-colon in the .csv file.
 
>[!Note]
>Only the tag field can be updated using this .csv file.  The ID, source name, and source path are included for reference only.


## Import and update tags

1. Connect to source
2. Select **Import tags** from the menu bar.

![Import tags option on the menu bar](media/mm-tagging.png)

3. Select **Download current source paths**.  The download .csv file will contain the Task ID, Source Name, Source Path, and Tags.  If no tags were associated with the source, the value will be blank.

3. Enter the name of the tag associated with each source.  If you want to apply more than one tag to a single source, separate the values using a semi-colon. Save the revised file.
4. Browse for the updated CSV file and then select **Apply**.


![Import tags entering CSV file name](media/mm-import-tag-csv.png)


5.  View the tags on the scan list and filter as needed.



![Results from import tags](media/mm-import-tag-results.png)