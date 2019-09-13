---
title: "Troubleshooting SharePoint Migration Tool"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Priority
ms.collection: 
- IT_Sharepoint_Server_Top
- Strat_SP_gtc
- SPMigration
- M365-collaboration
search.appverid: MET150
ms.custom: 
description: "How to troubleshoot common errors in the SharePoint Migration Tool."
---
# Troubleshooting common SPMT issues and errors

This article describes some common issues and errors that you may encounter when using the SharePoint Migration Tool (SPMT), and how to help you resolve them.

>[!Note]
> For help on SPMT installation issues, see: [Troubleshooting SPMT installation issues](https://docs.microsoft.com/en-us/sharepointmigration/spmt-install-issues)

## Common error messages

|Message|Do this|
|-----|-----|
|*We are unable to connect to the site you provided*|Check if the list exists or if you can access it in the source site and target site from your computer.</br></br>Confirm you have signed into SPMT with an account that has access to the site.</br></br>Confirm the URL you entered is correct and follows the proper format. </br>Example:  <spam><spam>https://<spam><spam>contoso.sharepoint.com/teams/SiteTitle<spam><spam>| 
|*Invalid source folder*|Confirm the path you entered is correct and follows the proper format</br></br>Confirm the user of SPMT has read access to the folder|
|*The site cannot be created or updated*|Confirm that you have permissions to create the site and that the URL is valid</br></br>If the site exists, confirm you are the site collection administrator</br></br>If it still fails, create the site manually and point the migration tool to this newly created site.|
|*Scan file failure: The folder name is invalid*|See [Invalid file names and file types in OneDrive and SharePoint](https://support.office.com/en-us/article/Invalid-file-names-and-file-types-in-OneDrive-OneDrive-for-Business-and-SharePoint-64883a5d-228e-48f5-b3d2-eb39e07630fa)|
|*Scan file failure: Target path is too long*|See [Invalid file names and file types in OneDrive and SharePoint](https://support.office.com/en-us/article/Invalid-file-names-and-file-types-in-OneDrive-OneDrive-for-Business-and-SharePoint-64883a5d-228e-48f5-b3d2-eb39e07630fa)   </br></br></br>The entire path, including the file name, must contain fewer than 400 characters for OneDrive, OneDrive for Business and SharePoint Online.|




## SPMT error codes 
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
|0x02010018| 1 - Check your credentials and then try again.|
|| 2 -  A problem occurred accessing SharePoint.  Check your credentials and try again.|
|| 3 - A problem occurred accessing SharePoint.  Check your credentials and your network connection and try again.|
|| 4 - A problem occurred accessing SharePoint.  Check your credentials and your site URL for accuracy and try again.|
|| 5 - A problem occurred accessing SharePoint.  Check your credentials and the format of your URL. Retry.|
|| 6 - A problem occurred accessing SharePoint.  Check your credentials and try again.  If the problem continues, please create a support case.|
|| 7 - A problem occurred accessing SharePoint.  Check your credentials and try opening your site in a browser.|
|0x0204000A|Cannot create package file. All files and folders in the SPMT working folder, *%appdata%\Microsoft\MigrationToolStorage*, must be closed. Restart your migration.|
|0x02030001|1 - Check your credentials.  Restart your migration. 
|| 2 - Check your credentials. Restart your migration.
|| 3 - Check your credentials and your network connection. Restart your migration. 
|| 4 - Check your credentials and your site URL. Restart your migration.
|| 5 - Check your credentials and the format of your URL.  Restart your migration.
|| 6 - Check your credentials and restart your migration.  If this continues, please a support case.
|| 7 - Check your credentials and try opening your site in a browser. Restart your migration.|
|0x02010008|Confirm the path and format of the user mapping file and that you have permission to access it.|
|0x02050001|All files and folders in the SPMT working folder, *%appdata%\Microsoft\MigrationToolStorage*, must be closed. Restart your migration.|
|0x02010002|Check your network status.  If you can access the source sites from a browser, then create a support case.|
|0x02010010|Make sure the source list and target list have the same template. |
|0x0204000D|All files and folders in the SPMT working folder, *%appdata%\Microsoft\MigrationToolStorage*, must be closed during migration. Restart your migration.|
|0x02080001|The file in the package has been changed or deleted while uploading. All files and folders in the SPMT working folder, %appdata%\Microsoft\MigrationToolStorage, must be closed. Restart your migration.|
|0x02010006|The source SharePoint site does not have any defined role definitions. Check to see if your role exists when accessing source site.|
|0x02040009|The package can’t be created because the directory cannot be found.  All files and folders in the SPMT working folder, %appdata%\Microsoft\MigrationToolStorage, must be closed. Restart your migration.|
|0x02010020|Disable migrating version history in SPMT settings or enable versioning in SPO.|
|0x0201000E|Check if the global setting has filtered out special characters in the target path or if the path has unsupported characters.|
|0x02010016|We are unable to find your SharePoint Server user.  Make sure you are a site collection admin.|


## Navigation errors

|**Error**|**Reason**|**Action**|
|:-----|:-----|:-----|
|This navigation node contains an invalid URL: cannot find the object this URL points to. |SharePoint Online will validate the URL before it creates the navigation node. If the URL represents a SharePoint object and the object cannot be found. SPO will reject the node creation query with this error. This can happen if the target of the URL was deleted, moved, not migrated yet, migrated in previous task where the URL mapping cannot be recognized in current job.|Use the same URL mapping between multiple tasks. For example:  </br></br> Task 1:  http:<span><span>//domain/original_path/site -> http://<span><span>domain/new_path/site<span><span> </br></br>Task 2: http://<span><span>domain/original_path/site2 -> http://<span><span>domain/new_path/site2<span><span>.  </br></br> Run another task to migrate Navigation nodes pointing to objects that were not migrated previously. Manually created the node in target site.|
|The navigation settings are highly customized. Currently it's not supported. |Global and current site navigation can only be migrated if its value matches a predefined template. Otherwise,the value will be recognized as *highly customized* and won’t get migrated.|Change the global and current navigation to use one of the predefined templates.  See *Site settings -> Look and Feel -> Navigation*. Manually edit the setting on target site.|
|Could not get target Term Store ID. The taxonomy provider of web navigation settings cannot be updated. |As the global and/or current site navigation settings is set to  “Managed Navigation”, the term store scanner was unable to get the target term store ID. This can happen if Managed Metadata Services are not properly configured.|Learn more at [SPMT Managed Metadata Migration](managed-metadata-migration.md).|
|The taxonomy provider term set ID of web navigation settings is invalid. |As the global and/or current site navigation settings is set to “Managed Navigation”, the term store scanner was unable to map the term set ID. |Confirm that the setting on the source site is valid and the term set was successfully migrated.|
|To update web navigation settings, you need following permissions: Add and Customize Pages.|The SPO account used for migration doesn’t have permission to edit site navigation settings.|Grant “Add and Customize Pages” permission to this account. |

## Taxonomy errors
|**Error**|**Reason**|**Action**|
|:-----|:-----|:-----|
|Migrate term store failed due to permission issue. |Current user is not a term store admin. |In the SharePoint Admin Center, select *Classic features*, and then under *Term store* click **Open**. Select the term store you want to migrate, then add the current user as a Term Store admininistrator.|
|Migrate term store failed due to lack of working languages. |Not all working languages of source term store exist in the target term store. |Go to SharePoint Online site setting. Under Site Administration, click Term store management. Choose the term store you want to update, select and add all the languages existing in source term store to the target working language panel.|
|Migrate term store failed due to default term store does not exist. |There is no default site collection term store at SP on-prem. |Go to SharePoint Server (on-premises) Central Administration, manage service application under Application Management, edit the properties of Managed Metadata Service Connection. Select the **This service application is the default storage location for column specific term sets**.|
|Migrate term store failed due to several default term stores exist. |There are several default site collection term stores existing at SP on-prem. |Go to SharePoint OnPrem Central Administration, manage service application under Application Management, choose one Managed Metadata Service Connection as default term store. Deselect **This service application is the default storage location for column specific term sets** of other Managed Metadata Service Connections.|
|Migrate pinned term failed due to its source term does not exist. |In some cases, the pinned term is in global term set (available for all sites connecting to this Managed Metadata Service Application), and the source term is in local term set (available for users of this site collection). Because SPMT will migrate the global terms first, then migrate the local ones, when trying to create the pinned term,  the source term has not been migrated yet.|Migrate again, and the pinned term will be created for the second time,  as the source term has been migrated before.|


## Web part errors
|**Error**|**Reason**|**Action**|
|:-----|:-----|:-----|
|Migration not supported web part | Currently, SPMT does not support this web part.| Check the list of currently supported web parts:  [SPMT supported web parts](spmt-supported-webparts.md) |
|Migration failed due to referring list is missing |The list has not been added to the task list. |Check your web part and the referring list to ensure it is in your migration scope.|
|Migration failed due to page being customized | SPMT currently does not support customized page migration. |Restore the page’s template page by using SharePoint Designer and restart your migration.|
|Migration failed due to page migration failed |Migration of the page failed, and all the web parts on that page.| Retry migrating the failed page. If the page succeeds, then all the web parts on that page will successfully migrate.|
|Migration failed due to it is an unsafe web part and the server setting ‘NoScript’| When the setting **NoScript** is turned on in the target SharePoint Online site, the web parts are considered to be unsafe as they could have the ability to execute JavaScript scripts or other code. Web parts will be blocked from migrating. |Turn off the  **NoScript** setting on the target SharePoint Online site so that these web parts will be unblocked. Important: Your site may be at risk if you turn off the settings. See this link for more info. |
| Migration failed due to invalid XML definition |The XsltListView web part and ListView web part contain an XML definition which is critical for the migration of these web parts.  Sometimes the XML definition is invalid due to upgrading issues or server errors.|Delete the failed web part from the SharePoint Server  source page.  Re-add it and try the migration again.|
| Migration failed due to invalid assembly name |The assembly name of the web part is critical for SPMT to migrate the web part. If the assembly of the web part cannot be parsed from its SOAP response the migration fails. |Check whether this web part is a supported “out-of-the box” (OOTB) web part. If it is supported, please file a bug and we will investigate.  However, if is a 3rd party web part, it is not supported. |
|Migration failed due to web part connection failure. |The web part is connected to another web part that failed to migrate, causing both to fail. |Make sure the connected web part is migrated successfully. Re-try your migration.|
|Migration failed due to unable to map user |If User field is a property of the web part, SPMT will attempt to map the user on the source web part (usually an on-premises user) to a user on the target SharePoint Online site. This error occurs when SPMT cannot map to the user. |Confirm that Azure Active Directory is used to sync all on-premises users to SharePoint Online. See this link for more info.|
