---
title: "Review the destination paths for your Box migration with Migration Manager"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: serdars
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
localization_priority: Priority
ms.collection: 
- M365-collaboration
- SPMigration
search.appverid: MET150
description: Review your destination paths for your Box migration while using Migration Manager.
---
# Step 4:   Review destination paths

In this step, you are reviewing the destination paths, and making sure they are correct. An account cannot be migrated without a destination indicated.  Once you migrate content to a destination it cannot be modifed.

## Single destination edit

If a destination is missing, highlight the row. A panel will appear to the right. Under **Destination**, click **Edit.**  you will be given the option of selecting a OneDrive, SharePoint, or Teams path as a destination.


### OneDrive

1. Highlight the row. Under **Destination**, click **Edit.**
2. Select **OneDrive** as a destination.

![edit OD destination path](media/mm-box-select-od-destination.png)

3. Select a folder (optional).

![select OneDrive folder path](media/mm-box-destination-folder-onedrive.png)

4. Click **Save path**.


###  SharePoint

1. Highlight the row. Under **Destination**, click **Edit.**
2. Select **OneDrive** as a destination.

![edit SP destination path](media/mm-box-sp-destination-path.png)

3. Select a location where you want to move the content.

![select SP library path](media/mm-box-sharepoint-destination-folder.png)
4. Click **Save path**.



### Teams


1. Highlight the row. Under **Destination**, click **Edit.**
2. Select **OneDrive** as a destination.

![select teams destination](media/mm-box-teams-destination-path.png)

3. Select a channel.

![select teams channel](media/mm-box-teams-destination-channel.png)

4. Click **Save path**.


## Upload destinations using a CSV file

If you have many destinations to edit, you can choose to upload a bulk destinations CSV file. 


![upload destinations for Box accounts bulk](media/mm-box-bulk-upload-destination-panel.png)

1. Download the MigrationDestinations.csv file template and enter your destinations. Save your file using any name you wish.
2. Select the file with your destinations.
3. Click **Save**.  

>[!Important]
>Review your destination CSV file before you upload it to make sure you have entered the values in correctly.  The destination file is not validated, and once you have migrated to these destinations it cannot be undone.
