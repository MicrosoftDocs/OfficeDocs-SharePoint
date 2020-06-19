---
title: Mover Release Notes
author: JoanneHendrickson
manager: pamgreen
audience: ITPro
ms.topic: article
ms.service: sharepoint-online
localization_priority: Priority
ms.collection: 
- SPMigration
- M365-collaboration
search.appverid: MET150
description: "Mover Release Notes"
---

# Mover release notes

This article discusses cumulative features and enhancements in the Mover migration tool.

## Frontend v1.16.2 (June 12, 2020)

### Impact:
- The Migration Manager table now includes an "information" icon in each row to make it more intuitive for users to know that additional information on the row can be viewed by clicking on that icon. This action will open the Transfer Summary side panel.
- In the Migration Manager, when opening the Transfer Summary side panel for a given entry in the table, the Transfer Logs table within the side panel would empty itself about 10 seconds after its initial load. This has been fixed now and the Transfer Logs table should remain visible and will be updated with new data as it becomes available.
- Fixing a Migration Manager screen issue. When the user no longer has the mouse focus on the side panel, the panel will close.
- Fixing the incorrect display of "Connectors don't exist anymore!" when in fact the connectors do exist.

## Backend v1.16.4 (June 3, 2020)

A new backend release with some stability improvements. We are setting FTP, SFTP, and WebDAV connectors as private due to lack of usage and to focus our product.

### Impact

- Some users were having problems viewing transfers user logs and scan reports. The files were sometimes being delivered in an intermediate format. This has been fixed by ensuring the files are completely processed before being delivered to users. 
- The FTP, SFTP and WebDAV connectors are marked as private. So users will no longer be able to authorize new connectors of those types. Existing FTP, SFTP and WebDav connectors will continue to work until July 1, 2020. Current users have been notified regarding this via email. 
- API Consumers: When using the POST transactions/?type=transfer or POST transactions/?type=scan endpoints, if one of the schedules were already running, it will not return the error object in the response, and as a result the other response items were shifted in order. This has been fixed by ensuring that an error object is properly returned for schedules that are already running. 

## Frontend v1.16.1.1 (June 1, 2020)

This frontend release focuses on improving accessibility to our application for keyboard and screenreader users.

### Impact

- The option to create a (legacy) Mover account has been removed from the UI. That is, users will now be required to use the "Sign In with Microsoft Account" feature instead. In the future, legacy Mover accounts will not be supported anymore. 
- Improved accessibility in the app for keyboard and screenreader users. 
- Keyboard users will be able to navigate through all Migration Actions dropdown menu Items in the Migration Manager using the tab key, and the up, down, left and right arrow keys. They will be able to navigate to previously not keyboard-accessible menu items such as the Customize and Reorder columns submenus which allows them to select which columns to display on the table and in what order. In addition to this, screenreader users will get better prompts when interacting with the Migration Actions dropdown menu. 
- Keyboard users will now be able to navigate the Migration Manager table. They will be able to sort the table, open the Transfer Summary side panel for rows, and apply tag filters. Screenreader users will have a much improved experience when interacting with the table, including proper ARIA labels and descriptions for actions they can take on elements on the table. 
- In the Transfer Wizard, when selecting Authorize New Connector (either source or destination), the Connector Type Picker is now accessible using the keyboard. In addition to this, the Authorize buttons on each connector type now have enhanced ARIA labels that will better inform screen-reader users what the button does. 
- In the Transfer Wizard screen, the connector picker (both source and destination) would show some connector types or connector names truncated on some screen sizes. Tool tips have been added on these items so now users will be able to view the names in full and not just the truncated version. 
- In the Transfer Wizard screen, the Manage/Connect drop down has been improved so the Narrator says the proper text for the correct  button. 
- In the Migration Manager screen, the helper tool tip for Filters will now be automatically be shown when focusing into the "information" icon, which is now accessibile by tabbing into it. 
- End users will be able to navigate into and out of the File Picker both in the Transfer Wizard (when connecting to a single user connector) and in the Migration Manager (when editing source or destination on a specific schedule). 

### Customer Workflow Impact
- Legacy user account creation has been made inaccessible using links in the UI.
- In the Migration Manager's Migration Actions dropdown menu, the Reorder columns and Customize columns menu items will appear visually different as changes were made to make them accessible for keyboard and screenreader users. 
- In the Migration Manager's Migration Actions dropdown menu, the Stats menu item will no longer have on and off options, but the menu item can be toggled and the toggle status will be displayed as a check instead. 
- In the Migration Manager table, users would be able to open the Transfer Summary panel by clicking on a row. This behavious has changed and users will now need to either double click on the row or click on the status of the row. Also, the entire Migration Manager table appear visually different as changes were made to make it accessible for screenreader users. 

## Backend v1.16.3.1 (May 29, 2020)

A backend release deploy that should have no impact on customers. This  moves the storage location of pre-rendered user logs and scan reports into Azure Blob Storage.

## Backend v1.16.2 (May 28, 2020)

New release of our Mover backend that includes an exciting new feature for preview (Box Notes to OneNote notebooks conversion) as well as a fix to a customer issue and stability fixes.

### Impact

- Support added for converting Box Notes to OneNote notebooks. Migrations from Box to OneDrive Consumer, OneDrive for Business (Single User) or Office 365 will be able to convert Box Notes to OneNote notebooks. This feature is now in public preview and will require support assistance to enable it for customers. 
- Support: In order to enable Box Notes to OneNote notebooks conversion for a migration, the following options will need to be set on the schedules: src_convert_boxnotes_onenotes=true and src_skip_boxnotes=false. src_convert_boxnotes_onenotes cannot be set to true if src_convert_boxnotes is already set to true. The latter enables Box Notes to Word Document conversion instead. 
- During a transfer, if an update of an item that already existed in the destination (and was changed in the source) failed on its first attempt, subsequent attmpts will always fail with unpredictable errors. This has been addressed and subsequent (internal) attempts on these cases are done properly now and will have a chance of completing successfully. 
- Some users were experiencing an issue in which the Migration Manager table would show some schedules with status Not Run when they were indeed run, sometimes multiple times. This has been corrected and will not happend going forward. Problematic schedules have been fixed to reflec the proper status. 

## Backend v1.16.1 (May 25, 2020)

Backend release with stability improvements. There are no customer facing changes. But this will help clear some backlogs in our migration job monitoring service.

## Backend v1.15.11 (May 14, 2020)
Backend release improving experience to some of our users.

### Impact

- The Migration Manager table will get populated a bit faster for the average migration, whil every large migrations (1000s of users) will see a considerable speed improvement. 
- In the Migration Manager overview, some migrations with many users that have been scanned/migrated a large number o times would sometimes fail to populate the table. This has been ixed by optimizing how migrations get populated in order to increase performance.

## Frontend v1.15.4 (May 13, 2020)

A large frontend release, with little UX impact, but library upgrades. 

### Impact

- Minor UI changes from updating Fabric UI. 

## Backend v1.15.10 (May 12, 2020)

Backend release to improve experience to some of our users.

### Impact

- When Downloading User Logs in zip format, the file name for each log includes a reference to the source and destination directories, but not of more relevant information to the user. This is now improved by changing the structure of individual file names to be: {endDate}_{sourcePath}_{txid}.moverlog.{extension}. This makes the files behave better when sorting them as they are prefixed by the transaction end date. As well, the source path is now cleaned up to only show more relevant parts. Reference to the destination directory is not included anymore as it tends to be irrelevant when the source directory is already included. 
- When duplicating a schedule in the Migration Manager view, certain schedules were failing with "Failed to duplicate N schedules", where N is the number of failed schedules. This is now fixed and the user is able to duplicate all schedules. 


## Backend v1.15.9 (May 7, 2020)

A backend release went out addressing a customer concern about 0-byte files into Office 365, and with many more enhancements that don't currently have a direct user impact but will enable future improvements for our end users.

### Impact

- Migrations going into Office 365 will not skip 0-byte file anymore and will be successfully transferred to the destination. However, migrations going into OneDrive Consumer or OneDrive for Business (Single User) will still skip 0-byte files as those services still restrict non-administrator transfers from creating zero-byte files.

## Frontend v1.15.3 (May 1, 2020)

A frontend deployment to speed up bulk operation. 

### Impact

- Doing bulk operations on users in the Migration Manager would be slow when a lot of users were selected. Speed improvements to these operations have been introduced by using a new version of the Mover API. 


## Frontend v1.15.2.1 (April 29, 2020)
A small deploy fixing a frontend issue. But also testing part of our infrastructure move to Azure.

### Impact

- When trying to create a folder from the File Picker view for a connector, "Unknown error" is displayed to the user. This is now fixed and folder creation is working properly again.

## Backend v1.15.8.1 (April 28, 2020)

Deploy to production: Backend release to address a customer migration. 

### Impact

- When Downloading User Logs in zip format, if the source and destination directories are too long (their) system cannot open the (downloaded) zip file because there is a filename length limitation of 255 characters (in zip files). This is now fixed, they can download and open zip file (even when source and destination directories are very long). 
- When scanning is done on a migration/schedule the scanner reports are generated and available for download in the Migration Manager UI. The generated reports include a Common Path report which was missing a new line character at the end of the headers, causing a malformed row formatting with the first common path record in the same row as the header. A fix has been implemented to ensure the report is presented in proper CSV format and is readable. 
 
### Customer Workflow Impact
- When downloading Common Path reports, customers will not need to manually fix the first line in the report anymore. The report will be a valid CSV file from the beginning. 

## Backend v1.15.7 (April 23, 2020)

Backend release to address a customer migration.

### Impact

- In Dropbox, Team Folders that are no longer shared with anyone would make a transfer fail when listing the containing folder. This has now been fixed and unshared Team Folders are handled properly. 

## Backend v1.15.6 (April 23,2020)

Backend release with customer fixes.

### Impact

- Managers are now able to delete the account of a managed user by entering their own password instead of the managed user's password. 
- Add support to traverse and transfer archived Team Folders out of the Dropbox (Administrator) connector.

## Frontend v1.15.1 (April 21, 2020)

### Impact
- Connector Authorization window where the user selects what connector to authorize now displays the full connector names without truncating them (on mobile phones, tablets and desktop).

## Backend 1.15.5.1 (April 21, 2020)

A backend release that includes customer fixes, expanding support for Dropbox and Google Drive (G Suite) scenarios.
   
### Impact

- In Dropbox, shared folders without an owner were making transfers fail at the containing folder. This is now fixed by letting the transfers traverse everything except those problematic folders (as opposed to their containing folders). Shared folders can have no owner because the original owner is no longer part of the Dropbox business account. Users are properly informed of this through the corresponding entry in the user log. 
- In Dropbox, archived Team Folders would make a transfer fail when listing the containing folder. This has now been fixed and archived Team Folders are handled properly. 
- Transferring Google Documents out of Google Drive or G Suite (Admin) was previously restricted to documents at most 10MB in size. This restriction is no longer in place and users should be able to export larger Google Documents into their Office 365 counterparts. 
- There was an issue where users could not create folders at the root of a Single User connector. This has been fixed and users should be able to create folders at the root of Single User connectors now. 
- Connectors were not being deleted immediately when the user deleted their account. Instead, connectors would get deleted when the account retention policy monitor would clean them up. This has been changed so that connectors are deleted right away. 

## Backend v1.15.4 (April 9, 2020)

Backend release to fix to address handling of of Dropbox Team folders. This is a work in progress to catch up with the latest about Team Folders, but it fixes urgent issues to unblock customers.

### Impact

- Fixed handling of Dropbox Team Folders and unique permissions within subfolders. Team Folders will be listed on the root of the Dropbox (Admin) connector, as well as under each user that has access to them. However, to prevent data duplication, Team Folders will NOT be transferred if they are listed under a user. Team Folders are only transferred when traversing them directly from the root of the Dropbox (Admin) connector. Also, permissions for Team Folders and its subfolders are properly exported now, including restrictive permissions.  

## Backend v1.15.3 (April 8, 2020)

Small but critical backend release for migrations out of G Suite (Admin). Please read the impact statement carefully.

### Impact
- Fixes a specific case in migrations from G Suite (Admin) that would end up in data duplication. The case relates to folders in an "owner" root that were shared with other users ("guest") and "guest" mounted the folder not in their root folder but somewhere deeper in their tree. In this case, the transfer would not obey the user priority list resulting in the folder being transferred for both "owner" and "guest". This regression was introduced on March 1, 2019 (June 2019 for FTC) and fixed now. Full impact is still being assessed. There is no need to re-run Google Prescans for affected migrations; instead, re-running the transfers will now skip the folder in question appropriately. Remediation for affected customers is to manually removed the duplicated data (upon identification). 

## Backend v1.15.1 (April 2, 2020)

A backend release that includes bug fix and stability improvements.

### Impact

- Users creating a new Mover account using the Sign in with Microsoft account feature will have appropriate access to running all types of transfers (some transfers appeared as not allowed to some new users). 

## Backend & Frontend v1.15.0 (April 1, 2020)

### Impact
- A new "Support" link will be displayed in the top navigation bar in the app. This link will point users to the new support system. The intercom widget will be disabled in the application. 
- Brand new users and current users with a Microsoft account will be able to sign into the Mover app with their Microsoft account. This includes work/school and personal accounts. Existing Mover accounts will continue to be supported. 

### Special Customer Impact

- OneDrive Consumer: Added ODC's domain to allowed origins for CORS validation. This enables future integration (currently as POC) with the OneDrive Consumer Web UI. 

## Backend v1.14.1.1 (March 31, 2020)

### Impact

- Fixed an issue with very old migrations with permission mappings that would prevent the app from loading. Support for these old migrations have been fixed.
- Users: For legacy transfers that convert Box Notes to Word Documents only. Box notes images that are not supported by Word Docx will now be converted to a format acceptable by Word Docx and will be displayed properly in the document. 
- When the Mover app is loaded, the Migration Manager will default to the latest Migration instead of oldest Migration (this was a regression from a previous release). 
- This adds an extra column for schedule tags in all migration and scan reports that aggregate by user/schedule. 

## Backend & Frontend v1.14.0 (March 26,2020)

A combined backend/frontend deploy with some fixes to reports and disabling the Intercom widget.

### Impact

- Accurate stats for files and bytes (success, failure, skipped, unsupported) will be displayed in the Migration Report. There will be no discrepancy for the stats shown in the report versus what's displayed in the Migration Manager UI. 
- The Migration Manager UI will not be stuck for users that have migrations with very large permission mappings. Instead, the app will load permission mappings as needed (when editing them). If a migration has an excessively large permission mapping, the app will not display the editor. Instead, the user will be able to download the permission mapping as CSV, edit and then re-upload the CSV. 
- The intercom widget will be disabled in the application. 

## Backend v1.13.10 (March 24, 2020)

A backend release with a new feature and potential performance fix. 

### Impact
- Unique permissions from items within a Dropbox Team Folder will now be moved to the destination.

## Backend v1.13.9 (March 20, 2020)

Backend release to assist with the increased loads.
 
### Impact
-  There were cases in which transfer cancellations were taking a long time to take effect. This fixes the issue by ensuring they happen faster. 

## Backend v1.13.7 (March 17, 2020)

Backend release with changes to help us determine the root cause for customer issues.

### Impact

- Transfers from Egnyte's root directory or the Private directory will not incur in a validation error and the user will be allowed to migrate out of those folders. 

## Backend v1.13.5 (March 11, 2020)

### Impact

- After a user runs a scan on a schedule, the scan reports (Long Paths, Common Paths, Large Files, Files Extension, Migration Scan Summary Report) were being generated sometimes with a pretty long delay. This is being fixed now. Also, the Migration Actions menu in the Migration Manager will update in real time when the scan reports finish generating and the proper count will be shown for the Scan Reports (zip file) menu item. 

## Backend v1.13.4 (March 9, 2020)

### Impact

- User will see improved speeds both when initially loading the schedules table in the Migration Manager, and when refreshing the data in it. The table should load in under 60 seconds now for huge migrations (100K+ schedules with multiple runs per schedule). Most importantly, users should not see the table failing to load in the UI due to size (may fail due to other normal issues like network problems). Average migrations will load instantaneously. Ultimate goal is to improve UX so that the table would load instantaneously for migrations of all sizes. 
