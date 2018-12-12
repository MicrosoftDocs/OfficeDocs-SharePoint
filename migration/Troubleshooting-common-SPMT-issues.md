---
title: "Troubleshooting SharePoint Migration Tool"
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Priority
ms.collection: 
- IT_Sharepoint_Server_Top
- Strat_SP_gtc
ms.custom: 

description: "How to troubleshoot common errors in the SharePoint Migration Tool."
---
## Troubleshooting common SPMT errors
|**Error Code**|**Error description**|**Recommendations**|
|:-----|:-----|:-----|
|0x0201000D|The list does not exist or cannot be accessed.|Check if the list exists or if you can access the list in source site and target site.|
|0x02050008|Failed to access local storage.|Do not open, edit or delete the SPMT working folder %appdata%\Microsoft\MigrationToolStorage or its contents. Restart your migration.|
|0x02010023|Your source list template is not supported.  Please try another.|The source list is not supported or with unsupported dependencies, such as unsupported taxonomy,the source list template is not supported, or that the lookup field reference is broken. Please check StructureReport_XX.csv for more details.  The StructureReport_XX.csv report is is under "*C:\Users\%user name%\AppData\Roaming\Microsoft\MigrationTool\admin@XXXX.onmicrosoft.com\WF_XXXXX\Report*" folder.|
|0x0201000C|Invalid credentials.|Check if you can access the source sites and lists with your credentials. Make sure you are the site collection admin for source and target. Check if you can modify SPO target site.|
|0x02010017|You do not have sufficient permission. |Make sure the user is site collection admin.|
|0x02060009|1. The site collection cannot be created because the URL is already in use or an invalid URL.</br> 2. The site collection cannot be created because the URL contains invalid character.</br> 3. The site collection cannot be created or updated.|Make sure you are tenant admin. Check below items for potential failure reasons.</br> 1. The site collection cannot be created because the URL is already in use or an invalid URL.</br> 2. The site collection cannot be created because the URL contains invalid character.</br> 3. The site collection cannot be created or updated.|
|0x02010018|1. Check your credentials and try again.</br> 2. A problem occurred accessing SharePoint.  Check your credentials and try again SharePoint access failure - SharePoint library was not found</br> 3. A problem occurred accessing SharePoint.  Check your credentials and try again SharePoint access failure - Server cannot be connected </br> 4. A problem occurred accessing SharePoint.  Check your credentials and try again SharePoint access failure - Web issue</br> 5. A problem occurred accessing SharePoint.  Check your credentials and try again SharePoint access failure - Invalid URL format</br> 6. A problem occurred accessing SharePoint.  Check your credentials and try again SharePoint access failure - Unexpected failure</br> 7. A problem occurred accessing SharePoint.  Check your credentials and try again SharePoint access failure - DNS resolving failure|Error occurs during data source scanning.  Check below for potential failure reasons.</br> 1. Invalid credentials</br> 2.The list doesn't exist</br> 3. Network connection issue</br> 4. Invalid site URL</br> 5. Wrong URL format</br> 6. An unexpected error occurs. Please create a support case.</br> 7. Check network for potential DNS resolving issue. Open the site in browser.|
|0x0204000A|Cannot create package file due to file being locked|Check %appdata%\Microsoft\MigrationToolStorage and make sure all the files/folders are not opened during migration.|
|0x02030001|1. Query job status SharePoint access failure - Invalid credentials</br>2. Query job status SharePoint access failure - SharePoint library is not found</br>3. Query job status SharePoint access failure - Server cannot be connected</br>4. Query job status SharePoint access failure - Web issue</br>5. Query job status SharePoint access failure - Invalid URL format</br>6. Query job status SharePoint access failure - Unexpected failure</br>7. Query job status SharePoint access failure - DNS resolving failure|This error occurs when submitting migration job to SPO.  </br>1. Invalid credentials</br>2.The list doesn't exist-</br>3.Network connection issue</br>4.Invalid site URL-</br>5.Wrong URL format. </br> 6.An unexpected error occurred. Please create a support case.</br>7.Check network for potential DNS resolving issue. Open the site in browser.|
|0x02010008|Invalid user mapping. Check your user mapping file for correct formatting and access.|Check to see if you have permission to access the user mapping .csv file and if the path and format of the  user mapping file is correct.|
|0x02050001|Local storage file is corrupted|Do not open, edit or delete the SPMT working folder %appdata%\Microsoft\MigrationToolStorage or its contents. Restart your migration.|
|0x02010002|Unable to access the source SharePoint site. |Check your network status.  If you can access the source sites from a browser, then create a support case.|
|0x02010010|The selected source list has a different template than the target one. |Make sure the source list and target list have the same template. For file share migration, the target must be a document library or my site.|
|0x0204000D|An unexcepted exception occurred when saving the Prime package.|Do not open, edit or delete the SPMT working folder %appdata%\Microsoft\MigrationToolStorage or its contents. Restart your migration.|
|0x02080001|The file in the package has been changed or deleted while uploading|Do not open, edit or delete the SPMT working folder %appdata%\Microsoft\MigrationToolStorage or its contents. Restart your migration.|
|0x02010006|The source SharePoint site does not have any defined role definitions.|Access to websites,lists, folders, and list items are controlled through a role-based membership system.  Users are assigned to roles that authorize their access to SharePoint objects. Check to see if your role exists when accessing source site.|
|0x02040009|The package file can't be created because the directory can't be found.|Check %appdata%\Microsoft\MigrationToolStorage.  Make sure this folder is not touched during migration.|
|0x02010020|Versioning is disabled on SPO, but the source data might have version history. Please turn off version support in SPMT or enable version in SPO.|Turn off migrate version history in SPMT settings or enable version in SPO.|
|0x0201000E|Invalid SharePoint path|Check if the global setting has filtered out some special characters in the target path or if the path has unsupported characters like |
|0x02010016|We are unable to find your SharePoint Server user.  Make sure you are a site collection admin|Check the SharePoint user on the source web. This happens if SPMT cannot read user info from the web. Make sure you are the site collection admin for source.|
