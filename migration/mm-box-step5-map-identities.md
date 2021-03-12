---
title: "Step 5: Map Box identities with Migration Manager"
ms.reviewer: jhendr
author: JoanneHendrickson
ms.author: jhendr
manager: serdars
audience: ITPro
f1.keywords:
- CSH
ms.topic: article
ms.service: sharepoint-online
localization_priority: Priority
ms.collection: 
- M365-collaboration
- SPMigration
search.appverid: MET150
description: "Step 5:  Map Box identities with Migration Manager." 
---

# Step 5:  Preview - Map identities of Box accounts to Microsoft 365 accounts

>[!Important]
> This feature is currently in private preview and subject to change without notice.

Identity Mapping is matching--or "mapping" the user and group identities that have access to your source environment (in this case Box) and map those identities to Microsoft 365 user and group identities. This process is important to migration. If identities are not properly set up prior to migration, it can result in users losing access to content. It can also result in information being incorrect at the destination.


Map your groups and users in Box to those in Microsoft 365 to migrate your Box sharing settings.

1. Select the Migrations tab.
2. Select **Map identities** on the menu bar.

![Map box identities](media/mm-box-upload-destinations-bulk.png)
</br>
3.  Select **Auto-map** to have Migration Manager map the identities for you or select **Import users and groups** to upload the values using a CSV file.

![Map box identities toolbar](media/mm-box-map-identities-toolbar.png)

</br>

## Mapping individual identities

1. To edit a single mapping, highlight the row. Enter the mapping Microsoft 365 user account. 
2. Select **Save**.

![Map box identities single](media/mm-box-map-identity-single.png)

## Import users and groups

If you have many mappings to edit, you can choose to upload a CSV file containing your users and groups mappings. Download the  file template to your computer and enter your destinations. Save your file as a .csv file using any name you wish. 

Upload your own users and groups mappings using the M
1. Select **Import users and groups**.
2. Download the mapping.csv template file, inserting your own mappings. You can name the .csv any name you wish.
3. Click **Select file**.  Navigate to your mapping .csv file and select.
4. Select **Save**.
5. Select **Close**.


>[!Important]
>Make sure to verify your mappings before uploading the file.  The file will not be validated, and once migration cannot be changed.


[**Step 6: Migrate and monitor**](mm-box-step6-migrate-monitor.md)