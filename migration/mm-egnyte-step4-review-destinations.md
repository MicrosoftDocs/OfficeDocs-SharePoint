---
ms.date: 09/06/2023
title: "Review the destination paths for your Egnyte migration with Migration Manager"
ms.reviewer: 
ms.author: heidip
author: MicrosoftHeidi
manager: jtremper
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: microsoft-365-migration
ms.localizationpriority: medium
ms.collection: 
- m365solutions-migratefileshares
- m365solution-migratetom365
- m365solution-scenario
- M365-collaboration
- SPMigration
- highpri
- m365initiative-migratetom365
search.appverid: MET150
ROBOTS: NOINDEX
description: Review your destination paths for your Egnyte migration while using Migration Manager.
---
# Step 4: Review destination paths in Migration Manager Egnyte

In this step, review the destination paths of the accounts you have moved to the migrations list, making sure they're correct. An account can't be migrated without a destination indicated. Once you start migrating content to a destination, it can't be modified.

## Single destination edit

If a destination is missing on a single user, highlight the row and update the value. 

1. Highlight the row, a panel will display. Under **Destination**, select **Edit.**
2. You have the choice of selecting a OneDrive, SharePoint, or Teams path as a destination. Depending on your selection:

    - For OneDrive, enter the OneDrive URL or email address and the location/folder name
    - For SharePoint, enter site URL and location
    - For Teams, select the team and the channel

3. Select **Save path**.
>[!Note]
> If the desired destination doesn’t appear in the dropdown list, please upload it using a CSV file as described below.


## Upload destinations using a CSV file

If you have many destinations to edit, you can choose to upload a bulk destinations CSV file.  Download the *MigrationDestinations.csv* file template to your computer and enter your destinations. The template lists all migration tasks that have never been run, and you can add to or modify the “destination path” column. Then save your file as a .csv file using any name you wish. 


![upload destinations for Google accounts bulk](media/mm-google-bulk-upload-destination-panel.png)

1. From the Migrations tab, select **Upload destinations** from the menu bar.
2. Select the file to upload with your destinations.
3. The destinations will be validated upon uploading. </br>

  >[!Note]
  >The validation process may take a while and can be skipped. However, we strongly recommend you complete the validation. You can always open another browser tab to continue Migration Manager operations.</br>

4. A validation report is generated if issues are found. Download the report to fix the issues based on the error message provided. Then reupload the fixed destinations to pass the validation.
5. Select **Save**.  

>[!Important]
>Rows with vacant destination paths will be skipped in the validation process.  

### Destination path format

|Type|Format|Example|
|:-----|:-----|:-----|
|SharePoint URL|https://<*tenant*>.sharepoint.com/sites/<*site name*>/<*library name*>/<*optional folder name*>|https://contoso.sharepoint.com/sites/sitecollection/Shared Documents </br>https://contoso.sharepoint.com/sites/sitecollection/Shared Documents/SubFolder|
|OneDrive UPN|name@example.com|user@contoso.onmicrosoft.com|
|OneDrive URL|https://<*tenant name*>-my.sharepoint.com/personal/<*user principal name*>/Documents/<*optional folder name*>|https://contoso-my.sharepoint.com/personal/user_contoso_onmicrosoft_com/Documents </br>https://contoso-my.sharepoint.com/personal/user_contoso_onmicrosoft_com/Documents/SubFolder |



## Go to [**Step 5: Map identities**](mm-google-step5-map-identities.md)


