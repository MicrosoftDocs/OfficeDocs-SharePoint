---
ms.date: 08/07/2023
title: "Step 5: Map Google identities with Migration Manager"
ms.reviewer: jhendr
author: MicrosoftHeidi
ms.author: heidip
manager: jtremper
audience: ITPro
f1.keywords:
- CSH
ms.topic: article
ms.service: microsoft-365-migration
ms.localizationpriority: high
ms.collection: 
- m365solution-migratefileshares
- m365solution-migratetom365
- m365solution-scenario
- M365-collaboration
- SPMigration
- highpri
- m365initiative-migratetom365
search.appverid: MET150
description: "Step 5:  Map Google identities with Migration Manager." 
---

# Step 5: Map identities of Google Drive to Microsoft 365 accounts

Map identities of your Google Drives to Microsoft 365 accounts while using Migration Manager.  

Identity Mapping is when you match the user and group identities that have access to your source environment (in this case Google) and map those identities to Microsoft 365 user and group identities. This process is important to migration. If identities are not properly set up prior to migration, it can result in users losing access to content. It can also result in information being incorrect at the destination.

Map your groups and users in Google to those in Microsoft 365 to migrate your Google sharing settings.

1. Select the Migrations tab.
2. Select **Map identities** from the menu bar.
3.  Select **Auto-map** to have Migration Manager map the identities for you or select **Import users and groups** to upload the values using a CSV file.


## Mapping individual identities

1. To edit a single mapping, highlight the row. Enter the mapping Microsoft 365 user account. 
2. Select **Save**.


## Import users and groups

If you have many mappings to edit, you can choose to upload a CSV file containing your users and groups mappings. Download the  file template to your computer and enter your destinations. Save your file as a .csv file using any name you wish. 

**Upload your own users and groups mappings**

1. Select **Import users and groups**.
2. Download the mapping.csv template file, inserting your own mappings. You can name the .csv any name you wish.
3. Choose **Select file**. Navigate to your mapping .csv file and select.
4. Select **Save**.
5. Select **Close**.


>[!Important]
>Make sure to verify your mappings before uploading the file.  The file will not be validated, and once migration cannot be changed.

### Migrating Google Shared Drives

Google Shared drives are now migrated by default. Google Shared Drive permissions are migrated according to what you have set in Project settings, under [general permission setting](/sharepointmigration/mm-project-settings-permissions#migrate-permissions). 

Folder permissions are migrated by default. File permissions are migrated on demand. 

We recommend the following steps when migrating permissions in your shared drive:

- Recreate a Microsoft 365 group with the same memberships as the Google Drive group. You can either create a new group or edit the group linked to the Team site designated as the migration destination for the Google Shared Drive.
- In the 'Map Identities' setting, map the original Google Drive group of the shared drive to the Microsoft 365 group.


## Go to [**Step 6: Migrate and monitor**](mm-Google-step6-migrate-monitor.md)

