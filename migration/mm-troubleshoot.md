---
title: "Troubleshooting Migration Manager"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
localization_priority: Priority
ms.collection: 
- IT_Sharepoint_Server_Top
- SPMigration
- M365-collaboration
search.appverid: MET150
ms.custom: 
description: "Troubleshoot common errors in Migration Manager."
---
# Troubleshoot Migration Manager issues and errors

This article describes some issues and errors that you may encounter when using Migration Manager, and how to help you resolve them.

## Check prerequisites and settings

Make sure you have met the prerequisites for agent installation, and have reviewed the required endpoints. Government cloud customers should confirm they have set their configuration properly.

- [Agent installation prerequisites](https://docs.microsoft.com/sharepointmigration/mm-setup-clients#prerequisites)

- [Required endpoints](https://docs.microsoft.com/sharepointmigration/mm-setup-clients#required-endpoints)

- [Government cloud settings](https://docs.microsoft.com/sharepointmigration/mm-setup-clients#government-cloud-support)


### Migration Mananger agent error messages
|Message|Do this|
|-----|-----|
|*Current user does not have access to source file share*|Make sure the source file share is a netowrk file share and is shared with the current user.|
|*The source file share does not exist*|Make sure the source file share is an existing network file share and is shared with current user.|

## Destination site URL issues

For an individual task:  You can only specify the site URL, but not the document and the folder.  The site always defaults to the documents library.

For bulk task upload:  You can specify both the site URL and the document library folder.



## Frequently seen error messages

|Message|Do this|
|-----|-----|
|*Invalid source folder*|Confirm the path you entered is correct and follows the proper format</br></br>Confirm your have read access to the folder.|
|*The site cannot be created or updated*|Confirm that you have permissions to create the site and that the URL is valid</br></br>If the site exists, confirm you are the site collection administrator</br></br>If it still fails, create the site manually and point the migration tool to this newly created site.|
|*Scan file failure: The folder name is invalid*|See [Invalid file names and file types in OneDrive and SharePoint](https://support.office.com/article/64883a5d-228e-48f5-b3d2-eb39e07630fa)|
|*Scan file failure: Target path is too long*|See [Invalid file names and file types in OneDrive and SharePoint](https://support.office.com/article/64883a5d-228e-48f5-b3d2-eb39e07630fa)   </br></br></br>The entire path, including the file name, must contain fewer than 400 characters for OneDrive, OneDrive for Business and SharePoint Online.|
|*Scan File Failure: Not enough disk space to pack the file*|The disk space available for the migration working folder is too small for the size of your source file.  Enlarge your size of your working folder try again.
|*Packaging failure: Cannot open file*|Packaging failed due to non-existing source.  Check if you can access the source root folder.|
|*A duplicate task has already been created.*|The CSV file used to do bulk migration cannot have duplicate entries.  Remove the duplicate line(s) and try again.|
|*The parent folder was not migrated*|The parent folder was not migrated, therefore all items under the folder will fail to migrate. Check your parent folder and retry your migration.|



## Error codes 
|**Error Code**|**Recommended action**|
|:-----|:-----|
|0x0201000D|Check if the list exists or if you can access it in the source site and target site.|
|0x02050008|Unable to access your local storage.  Restart your migration.|
|0x02010023|Your source list template is not supported.  Please try another.|
|0x0201000C|Check your credentials and then re-enter your username and password.|
|0x02010017|You must be a site collection admin.|
|0x02060009| 1 - The site collection cannot be created because the URL is already in use or an invalid URL.|
|| 2 -  The site collection cannot be created because the URL contains invalid character.|
|| 3 -  The site collection cannot be created or updated.|
|0x02060007| 1 - The site collection cannot be created because the URL is already in use or an invalid URL.|
|| 2 -  The site collection cannot be created because the URL contains invalid character.|
|0x02010018| 1 - Check your credentials and then try again.|
|| 2 -  A problem occurred accessing SharePoint.  Check your credentials and try again.|
|| 3 - A problem occurred accessing SharePoint.  Check your credentials and your network connection and try again.|
|| 4 - A problem occurred accessing SharePoint.  Check your credentials and your site URL for accuracy and try again.|
|| 5 - A problem occurred accessing SharePoint.  Check your credentials and the format of your URL. Retry.|
|| 6 - A problem occurred accessing SharePoint.  Check your credentials and try again.  If the problem continues, please create a support case.|
|| 7 - A problem occurred accessing SharePoint.  Check your credentials and try opening your site in a browser.|
|0x0204000A|Cannot create package file. All files and folders in the Migration Manager working folder, *%appdata%\Microsoft\MigrationToolStorage*, must be closed. Restart your migration.|
|0x02030001|1 - Check your credentials.  Restart your migration. 
|| 2 - Check your credentials. Restart your migration.
|| 3 - Check your credentials and your network connection. Restart your migration. 
|| 4 - Check your credentials and your site URL. Restart your migration.
|| 5 - Check your credentials and the format of your URL.  Restart your migration.
|| 6 - Check your credentials and restart your migration.  If this continues, please a support case.
|| 7 - Check your credentials and try opening your site in a browser. Restart your migration.|
|0x02010008|Confirm the path and format of the user mapping file and that you have permission to access it.|
|0x02050001|All files and folders in the Migration Manager working folder, *%appdata%\Microsoft\MigrationToolStorage*, must be closed. Restart your migration.|
|0x02010002|Check your network status.  If you can access the source sites from a browser, then create a support case.|
|0x02010010|Make sure the source list and target list have the same template. |
|0x0204000D|All files and folders in the Migration Manager working folder, *%appdata%\Microsoft\MigrationToolStorage*, must be closed during migration. Restart your migration.|
|0x02040012|The temporary storage on your local computer is too low.  Migration Manager caches the package on the working folder. Expand your temporary storage and retry.|
|0x02030003|There are too many items with unique permissions. Simplify your permissions list by reducing the number of unique permissions. aRetry your migration.|
|0x02050001|Local storage file is corrupted.  The working folder was touched or modified during the migration.  Retry your migration.|
|0x02080001|The file in the package has been changed or deleted while uploading. All files and folders in the Migration Manager working folder, %appdata%\Microsoft\MigrationToolStorage, must be closed. Restart your migration.|
|0x02040009|The package can’t be created because the directory cannot be found.  All files and folders in the Migration Manager working folder, %appdata%\Microsoft\MigrationToolStorage, must be closed. Restart your migration.|
|0x02010020|Disable migrating version history in Migration Manager settings or enable versioning in SPO.|
|0x0201000E|Check if the global setting has filtered out special characters in the target path or if the path has unsupported characters.|
|0X0201000F|Invalid site URL. Check if the site URL is valid. Try to access the URL via a browser.|
|0x0207001|You do not have access to the task folder. Check if you can access  %appdata%\Microsoft\MigrationToolStorage.|
|0x01410010|A failure occurred because of missing dependencies on list items. Check the FailureSummaryReport.csv for details. Check if the dependencies have been included in your migration scope.|
|0x01510001|Packages failed to upload. 	If you have customized Azure storage, check if you can access the Azure storage and check if you can access the target site. Try migrating again.
|0x01510001|Failed to Upload the Job to Server: Upload file failed during migration.|
|0x02070009|Several packages failed to upload. Pause the task and check your network connection.|
|0x01710009|A failure occured due to job end failures; some items failed in the package. Restart migration.|
|0x01710009|Errors or timeout for Server Processing the file: Not all the items in the package have been migrated.|
|0x01610001|The Azure container is expired. Retry migration task.|   
|0x01710006|Errors or timeout for server processing the file: Job Fatal Error.|
|0x01710004|Errors or timeout for server processing the file. Fail to lookup folder name. The item may exist in other list or site in the same site collection. Or the item is in the recycle bin.|
|0x0131000F|Failed to Read the file. File is checked out.|
