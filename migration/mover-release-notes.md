---
title: Mover Release Notes
author: JoanneHendrickson
ms.author: jhendr
manager: serdars
recommendations: true
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


## Frontend v1.19.8 (April 27, 2021
- Accessibility. We have removed the option to close a "successful notification" message. It will now auto close in 5 seconds. 

## Backend - v1.20.7 (April 27, 2021)
- New. Six new columns have been added to the Migration Report. See the documentation at: https://docs.microsoft.com/sharepointmigration/mover-reports#migration-report. These new columns start with the following prefixes:
  - *Completed Successfully* will get the statistics for the last metrics completed transfer (green, status code 1xx). Three available statistics: Files, Bytes, MB.
  - *Completed* will get the statistics for the last completed transfer, either successfully or with some errors (green OR yellow, status code 1xx OR 2xx). Three available metrics: Files, Bytes, MB.
Reduces resolution times for customers who need to ensure their transactions (scans or transfers) are run in a specific region due to compliance requirements.
- New. GoogleWorkspace connector has been enabled in SharePoint Migration Manager.


## Backend v1.20.3 (March 11, 2021)

This release contains jolt command updates along with features and fixes for customers.

- Fix.  Some customers had trouble loading their G Suite connector in the Transfer Wizard. This usually happened for customers that had a very large number of Shared Drives in their G Suite account. The connectors should load, although for customers with a large number of Shared Drives, the count will be an approximate only.
- Feature. File permissions option is turned on by default if the source connector is a Microsoft connector.

## Frontend v1.19.6 (March 11, 2021)
This release contains accessibility fixes.
- Accessibility: In the Migration Manager table, an aria label is added to the Info button so the information is rendered correctly.
- Accessibility: Remove the role "menu" in the Migration Manager page because there are no children.


## Backend v1.20.1 (February 24, 2021) 
- Fix.  Customers were still able to delete a connector. The stop gap was only added to the UX. Measures have been added to check if a connector is associated to a migration. If it is, the connector cannot be deleted.


## Backend v1.20.0 (February 16, 2021) 
- Fix.  Users that only signed in using their Microsoft account were unable to delete their account because the form would prompt them for their password. Users are now able to delete their accounts safely.
- Feature. Account managers are able to delete managed users' accounts without being prompted for a password.
- Improvement. Customers running migrations from Egnyte would sometimes get "Could not get folder ACLs" error messages in their user logs. This is not very descriptive. Messaging has been improved to show the cause of the problem (usually, exceeding API quotas in Egnyte).

## Backend v1.19.25 (February 9, 2021) 
- Fix.  Users encountered an issue transferring folders with special characters (such as #) that are still valid in SharePoint Online. This has now been fixed and the system ensures that all special characters that are valid in SharePoint Online are handled properly.

## Backend v1.19.24 (February 8, 2021) 
- Fix. Broken Agent transfers for destinations that are not Office 365 has now been fixed.



## Backend v1.19.22 (December 16, 2020)

- Fix.  Users could not authorize new Box (Single User) connectors after Box restricted some features from Mover's client. This issue is fixed.
- Fix. Some users received the error "document library could not be found" when attempting transfers to certain SharePoint Online Document Libraries. This issue is fixed.
- Fix.  Transfers from or into OneDrive Consumer that were throttled had issues when re-trying the affected operations. An authorization related error message would appear on the User Log for these transfers. Re-tries now have proper authorization in place. This issue is fixed.

## Backend v1.19.21.5 (December 10, 2020)
This release fixes an issue with Egnyte Connector retrieving groups.

- Fix. While trying to retrieve groups for Egnyte, migration would fail as it created an infinite loop. Retrieval of groups is now successful.

## Backend v1.19.21.1 (December 4, 2020)
This release fixes an issue with Box connector authorization.

- Fix.  Some users reported issues authorizing new Box connectors or re-authorizing existing Box connectors. This is due to Box blocking our authorization attempts for our current Box client. New Box clients have been created to bypass this issue and authorization of Box connectors should be working again.

## Backend v1.19.20 (December 1, 2020)

- Accessibility: The User Log view now uses a different ID for all elements in the page.


## Frontend v1.19.2 (December 1, 2020)

- Fix.  Accessibility: 'Start copy' button was getting activated before loading of folders in 'Select Source' step in the Transfer Wizard. If the user invoked 'Start Copy', the transfer would get triggered by copying all items from the root of the source and destination. A fix has been made to wait for folders to be fully loaded before activating the Start Copy button.
- Fix.  Accessibility: Navigating through the list of folders in the Transfer Wizard using multiple tab stops was making navigation harder for users with motor impairments. Fix has been added to navigate the list using the keyboard arrow keys.
- Accessibility: The Transfer Summary panel will now display a tooltip for every value in the top details table containing the transaction information.
- Accessibility: The Migration Manager "Active filters" auto-suggestions are now accessible with the keyboard by pressing the down and up arrow keys from the filter search box.
- Accessibility: In the Migration Manager, Active Filters section, the info button had a tooltip with filtering instructions. However, the narrator would not read the content, even if the tooltip was in focus. To make the content accessible, the tooltip was eliminated and, instead, a proper link to the documentation page was added: https://aka.ms/MoverMigrationManagerFilters.



## Backend v1.19.19 (November 26, 2020)
- During a transfer there might be a failure that is unrecoverable. It means the transfer completely failed and any rerun would not fix it, such as, Storage Quota Exceeded.
However, when this happens during our 302 processing, the status of this processing take precedence. 
Unfortunately, this means that the original unrecoverable state is now lost. This has been fixed. 
If the transfer failed and it is an unrecoverable state, this state will now be preserved and displayed appropriately to the user.


## Backend v1.19.18 (November 10, 2020)

- Fix. Images included in Box notes are now correctly transferred and rendered in Microsoft Word.  
- Fix. The metadata "Created time" is now correctly getting migrated when running a transfer from Google to Office 365.
- Retrieval attempts of SharePoint Online sites for an Office 365 connector have been enhanced and expanded.
- Migration job limits have been adjusted, resulting in improved reliability for transfers going into Office 365.


## Backend v1.19.17 (November 3, 2020)

- Fix.  When destinations did not support direct upload, transfers from the Agent to the destination would fail. Direct Upload destinations are now detected and handling has been corrected when the destination does not support direct upload.

- Fix.  Added direct uploads to user log filters, both on success and failure. This fixes a defect in logging where Agents using the Direct Upload feature (which is now the default) would not have their log entries included in the user logs. This will enable correct feedback for users of the Agent.

## Frontend v1.19.1 (October 28, 2020)

This release fixes these customer issues:

- Fix. When editing a source or destination path in Migration Manager with lots of items, the side panel would only render up to 100 items and the rest would appear blank. The file picker now displays all content.

- Fix.  When a customer entered a certain format for an email account as an admin, the email validation could fail even with a valid email addresses. This has been fixed.


## Backend v1.19.10 (October 15, 2020)

- When authorizing an Office 365 connector, the links on the authorization page will now point to the new Mover docs at https://docs.microsoft.com/SharepointMigration/mover-plan-migration

## Frontend v1.19.0 (October 15, 2020) 

- All links to Mover documentation will now point to the Microsoft documentation site: https://docs.microsoft.com/SharepointMigration/mover-plan-migration


## Backend v1.19.15 (October 14, 2020)

- Improvement to ratelimit provider. In general, large migrations should now move faster.
- Email auth removed. This is no longer supported.


## Backend v1.19.14 (October 8, 2020)

- Fix.  Fixed sign up emails to not request a "reply" action since Mover emails are now being sent from a "no-reply" address. Users are now being directed to the public documentation.
- Fix.  Decreased and in some cases eliminated "failed to load migration" job errors.


## Backend v1.19.13 (October 1, 2020)

- Improve stability of the overall system by improving the reliability of our caching systems.
- Right after creating a migration from Office 365 and into Office 365, if the user tried to autodiscover migration tasks and if it failed to retrieve the source tenant's users and SPO sites, the app would report a strange error.  This has been fixed with a proper error being reported instead.

## Backend v1.19.11 (September 24, 2020)

- Fix.  Some customers were having issues autodiscovering tasks in newly created migrations into Office 365. Customers should now be able to autodiscover tasks. 


## Agent v1.3.5 (September 22, 2020)

- A new Agent has been released for all install types. Version 1.3.5 is a required update for all customers. This release updates the pinned certificates used for connecting to Bifrost. As of September 26, 2020, any older Agents will not connect to Bifrost and not be able to transfer files.


## Backend v1.19.9 (September 15,2020)

- Fix.  Previously, authorship information such as "Modified By" was not sent to the destination. Metadata from Google sources is now included in the transfer and displayed at the Office 365 destination.


- Fix. During transfers, items skipped as failures (unsupported items for export in the source or import in the destination) were showing as failures only in the user logs but not in reports, such as the Migration Error Report. These failures also now appear in the reports.

  
- Fix. When a user cancels a job, the job goes through a process to be cancelled. Previously, if the job finished before the cancel process completed, the rerun transfer was automatically initiated. This has been fixed. An automatic rerun transfer is not triggered if a job is in the process of being cancelled. 

- Improvement has been made in the overall system's stability through enhancements to the reliability of our caching systems.

- Fix. During a G Suite transfer from a shared drive some users received a "File is restricted" error. This has been fixed by allowing the transfer to move those files over to the destination.


## Backend v1.19.8 (September 9, 2020)
-	Enforce that authorizing user is Office365 Global Admin or SharePoint Admin when authorizing a connector

## Backend v1.19.7 (September 1, 2020)
-	Improved data transfer speeds from the Agent connector (file shares) into an Office 365 connector. Customers will need to update the Agent to version v1.3.4.0.
-	Transfers going into some Office 365 sites may fail to move certain folders if the sites have the SharePoint Online option `ThicketSupportDisabled` set to `false`. To correct this issue, customers can set `ThicketSupportDisabled` to `true` in the SharePoint Online sites experiencing the issues. Alternatively, they can contact Mover support to apply a workaround to their transfers. The workaround consists in automatically appending an underscore (_) to the folder names. The folders that may fail due to this SharePoint Online option have names ending in:

    - .files
    - _files
     - -Dateien
    - _fichiers
    - _bestanden
    - _file
    - _archivos
    - -filer
    - _tiedostot
    - _pliki
    - _soubory
    - _elemei
    - _ficheiros
    - _arquivos
    - _dosyalar
    - _datoteke
    - _fitxers
    - _failid
    - _fails
    - _bylos
    - _fajlovi
    - _fitxategiak



>[!Note]
>The workaround should NOT be requested if the SPO option `ThicketSupportDisabled` has been set to `true` as this may cause data duplication.

- When a transfer into Office 365 fails on items due to path length limitations, the items would show up yellow in the user logs and as errors in the migration error report. However, the messages related to these failed entries were blank. This has been fixed by ensuring that a proper error message has been added to these failures.


## Backend v1.19.6 (August 31, 2020)

- Improved stability for transfers going into Office 365.
- Improved sign-up experience into the Mover app for customer having issues.

## Backend v1.19.5 (August 26, 2020)

- Improved telemetry to tackle customer issues.

## Backend v1.19.4 (August 20, 2020)

- Improved stability for transfers going into Office 365.

## Frontend v1.18.2  (August 6, 2020)

- While using the App, notifications are sent to let you know if your request has been successful or if an error has occurred. The height and text size of notifications have been increased to improve visibility and awareness.

- A message will display if you are trying to authorize Office 365 with a tenant that lacks SharePoint Online licenses.

- You will not see Google pre-scan warnings when connecting to a G Suite source connector in the Transfer Wizard.

- All non-success notifications will stay open for the user to read. Success notifications will automatically close after 5 seconds.

## Backend v1.19.3 (August 6, 2020)

End of life notification and bug fix.

- The connectors for Amazon WorkDocs and NetDocuments have reached end of life. The connectors were deprecated July 1, 2020, and existing users notified. These connectors are no longer available.

- When a migration job failed to submit during a migration into Office 365, error entries were not being added to the user log or migration error report. This has now been fixed.  All files contained in the failed migration job now have an error entry in the user log and the migration error report.

## Backend v1.19.2 (July 31, 2020)

Migration Report improvements and bug fixes.

- When authorizing the G Suite Admin source connector, the template showed the prescan warning. As prescan is no longer needed due to its integration into the regular scan and transfer process, the warning from the connector authorization template in the UI has been removed.

- When authorizing or reauthorizing an Office 365 connector, a picker will show accounts that are currently signed into Microsoft. This improves the user experience as it prevents them from manually entering their credentials if they are already logged into Microsoft.

- A fix has been made to distinguish OneNote notebooks and folders with ".one" extension. Previously, when running a transfer from an Office 365 source, folder names with .one extension would fail to transfer the folders' content to the destination as the app would consider it as OneNote notebook.

- A fix has been made to correct an issue when signing into Mover. Some users were unable to sign in with their Microsoft account even though authorization seems to have gone fine. The application would redirect them back to the Mover login page after trying to load the UI, without any error messages. This behavior has been fixed; these users can now sign in with their Microsoft accounts.

- A fix has been made to correct discrepancies in the migration reports metrics.  In the future, more fields will be added to this report to give users a better understanding of ongoing migrations.

- When the user tries to authorize the Office 365 connector, and if the tenant lacks M365 licenses, the connector authorization will fail, and the error message "Couldn't retrieve SharePoint Online site list. We suspect your tenant lacks SharePoint Online licenses" will be displayed in the UI.

- When a transfer gets automatically re-queued, its status will now show as "Re-Queued" as opposed to "Queued". When it is running from an automatic re-queue, it will show as "Rerunning".

- Saving the permission map for a migration via the web UI that had a job_limit set or auto_job_limit set (migration scaler) caused those fields to set back to null, and the settings were lost. This issue is now fixed.

- Google Drive now lets users create shortcuts to their drive files as part of migrating the Google Drive app from multi-parenting to single-parenting behavioral models. Shortcuts are files that link to other files on the user's drive. The Mover app currently does not support moving those files to a destination.  When completed, the transfer status row will display yellow, indicating that some files are unsupported and that rerunning won't fix it.

## Backend v1.19.0 (July 14, 2020)

Exciting new features for migrations out of G Suite and Box.

- For migrations out of G Suite, requesting a "Google Pre-scan" was required before running the regular scans or transfers in order to prevent data duplication. The Google Pre-scan process has now been integrated into our regular migration scan and transfer processes, eliminating the need to request a Google Pre-scan from our support team. For more information, please refer to: https://aka.ms/MoverGSuite
- For migrations out of Box, all Box Notes will now be automatically converted to Microsoft Word documents in the destination. For more information, please refer to: https://aka.ms/MoverBox

## Backend v1.18.1 (July 8, 2020)

- Deprecation notices
  - Starting July 1, 2020, Amazon WorkDocs and NetDocuments connectors have been deprecated. This means that users will not be able to authorize new Amazon WorkDocs or NetDocuments connectors. However, users will still be able to use existing Amazon WorkDocs and NetDocuments connectors until their end-of-life date of August 1, 2020. Users are encouraged to wrap up existing migrations involving these two connectors as soon as possible.
- Error reporting improvements
  - Improved error messages displayed in the User Log coming from the Agent connector.
- Stability fixes
  - Large transfers into Office 365 are now less likely to fail completely (red row in the Migration Manager), as a result of performance optimizations.

## Frontend v1.18.1 (July 1, 2020)

- Accessibility fixes
  - Removed double tab stops in Authorize New Connector links in the Transfer Wizard.
  - Fixed Migration Manager stats to display properly in all zoom levels, and in devices of all screen sizes.
  - Enabled outlines on all links throughout the application when they have focus. This will help users locate the current element in focus when navigating the application using the keyboard.
  - Removed "Coming Soon" video in the Migration Manager when the user has no migrations.
  - Removed prompt to provide feedback when users close their accounts. It's natural for users to delete their accounts when their migrations are done. Alternatively, they can contact support to provide feedback.
  - Added a light version for the "Sign in with Microsoft" button for users browsing the application using a high-contrast browser mode.
  - Fixed the Mover logo for users browsing the application using a high-contrast browser mode.
  - Navigation bars will now show a marker on the active and focused items in high-contrast browser mode.

## Frontend & Backend v1.18.0 (June 25, 2020)

- Error reporting improvements
  - During a migration into Office 365, we would skip processing of source files over 15 GB and mark them as successfully skipped. This changed for a while to instead process them and report on the processing errors. While Office 365 supports 100 GB files now, migration of files over 15 GB is not yet supported. So we have reverted back to the previous approach of skipping files larger than 15 GB. Support for 100 GB files will be announced once they are fully supported for migrations into Office 365.
  - When running a migration from a non-existent source directory, the transfer would fail appropriately and the user log would have a yellow row in it. However, this row in the user log would sometimes contain no error message. This has been fixed so that a proper error message is included detailing that the source directory does not exist.
  - During a migration into Office 365, while a file may be uploaded properly, its batch may fail to be submitted for processing. In these cases, the UI would show the file as failed, but the user log would not contain any entries showing that the file failed. This has been fixed by ensuring that there always exists a user log entry per file when a migration job (batch) within a transfer fails to submit.
  - In the Migration Manager table, if there are skips because the file is unsupported on the source or destination, or if we are not allowed to download the file, then it will now show up as a failure and not as a regular incremental skip. Transactions that were mostly successful but only had these unsupported file issues, will end with status code 227 "Some files are unsupported" and the row will appear yellow in the Migration Manager.
- New features
  - On the Account Page, in the Admin Panel, a user is now able to add managers to their account in bulk. The user can enter a list of comma-separated email addresses to be added as account managers.

## Frontend v1.16.2 (June 12, 2020)

- The Migration Manager table now includes an "information" icon in each row to make it more intuitive for users to know that additional information on the row can be viewed by clicking on that icon. This action will open the Transfer Summary side panel.
- In the Migration Manager, when opening the Transfer Summary side panel for a given entry in the table, the Transfer Logs table within the side panel would empty itself about 10 seconds after its initial load. This has been fixed now and the Transfer Logs table should remain visible and will be updated with new data as it becomes available.
- Fixing a Migration Manager screen issue. When the user no longer has the mouse focus on the side panel, the panel will close.
- Fixing the incorrect display of "Connectors don't exist anymore!" when in fact the connectors do exist.

## Backend v1.16.4 (June 3, 2020)

A new backend release with some stability improvements. We are setting FTP, SFTP, and WebDAV connectors as private due to lack of usage and to focus our product.

- Some users were having problems viewing transfers user logs and scan reports. The files were sometimes being delivered in an intermediate format. This has been fixed by ensuring the files are completely processed before being delivered to users.
- The FTP, SFTP, and WebDAV connectors are marked as private. So users will no longer be able to authorize new connectors of those types. Existing FTP, SFTP and WebDav connectors will continue to work until July 1, 2020. Current users have been notified regarding this via email.

## Frontend v1.16.1.1 (June 1, 2020)

This frontend release focuses on improving accessibility to our application for keyboard and screen reader users.

- The option to create a (legacy) Mover account has been removed from the UI. That is, users will now be required to use the "Sign In with Microsoft Account" feature instead. In the future, legacy Mover accounts will not be supported anymore.
- Improved accessibility in the app for keyboard and screen reader users.
  - Keyboard users will be able to navigate through all Migration Actions dropdown menu Items in the Migration Manager using the tab key, and the up, down, left and right arrow keys. They will be able to navigate to previously not keyboard-accessible menu items such as the Customize and Reorder columns submenus that allows them to select which columns to display on the table and in what order. In addition to this, screen reader users will get better prompts when interacting with the Migration Actions dropdown menu.
  - Keyboard users will now be able to navigate the Migration Manager table. They will be able to sort the table, open the Transfer Summary side panel for rows, and apply tag filters. Screen reader users will have a much improved experience when interacting with the table, including proper ARIA labels and descriptions for actions they can take on elements on the table.
  - In the Transfer Wizard, when selecting Authorize New Connector (either source or destination), the Connector Type Picker is now accessible using the keyboard. The Authorize buttons on each connector type now have enhanced ARIA labels that will better inform screen-reader users what the button does.
  - In the Transfer Wizard screen, the connector picker (both source and destination) would show some connector types or connector names truncated on some screen sizes. Tool tips have been added on these items so now users will be able to view the names in full and not just the truncated version.
  - In the Transfer Wizard screen, the Manage/Connect drop down has been improved so the Narrator says the proper text for the correct  button.
  - In the Migration Manager screen, the helper tool tip for Filters will now be automatically be shown when focusing into the "information" icon, which is now accessible by tabbing into it.
  - End users will be able to navigate into and out of the File Picker both in the Transfer Wizard (when connecting to a single user connector) and in the Migration Manager (when editing source or destination on a specific schedule).

## Backend v1.16.3.1 (May 29, 2020)

A backend release deploy that should have no impact on customers.

## Backend v1.16.2 (May 28, 2020)

New release of our Mover backend that includes an exciting new feature for preview (Box Notes to OneNote notebooks conversion) as well as a fix to a customer issue and stability fixes.

- Support added for converting Box Notes to OneNote notebooks. Migrations from Box to OneDrive Consumer, OneDrive for Business (Single User) or Office 365 will be able to convert Box Notes to OneNote notebooks. This feature is now in public preview and will require support assistance to enable it for customers.
- During a transfer, if an update of an item that already existed in the destination (and was changed in the source) failed on its first attempt, subsequent attempts will always fail with unpredictable errors. This has been addressed and subsequent (internal) attempts on these cases are done properly now and will have a chance of completing successfully.
- Some users were experiencing an issue in which the Migration Manager table would show some schedules with status "Not Run" when they were indeed run, sometimes multiple times. This has been corrected and will not happen going forward. Problematic schedules have been fixed to reflect the proper status.

## Backend v1.16.1 (May 25, 2020)

Backend release with stability improvements. There are no customer facing changes. But this will help clear some backlogs in our migration job monitoring service.

## Backend v1.15.11 (May 14, 2020)

Backend release improving experience to some of our users.

- The Migration Manager table will get populated a bit faster for the average migration, while large migrations (1000s of users) will see a considerable speed improvement.
- In the Migration Manager overview, some migrations with many users that have been scanned/migrated a large number o times would sometimes fail to populate the table. This has been fixed by optimizing how migrations get populated in order to increase performance.

## Frontend v1.15.4 (May 13, 2020)

A large frontend release, with little UX impact, but library upgrades.

- Minor UI changes from updating Fabric UI.

## Backend v1.15.10 (May 12, 2020)

Backend release to improve experience to some of our users.

- When Downloading User Logs in zip format, the file name for each log includes a reference to the source and destination directories, but not of more relevant information to the user. This is now improved by changing the structure of individual file names to be: `{endDate}_{sourcePath}_{txid}.moverlog.{extension}`. This makes the files behave better when sorting them as they are prefixed by the transaction end date. As well, the source path is now cleaned up to only show more relevant parts. Reference to the destination directory is not included anymore as it tends to be irrelevant when the source directory is already included.
- When duplicating a schedule in the Migration Manager view, certain schedules were failing with "Failed to duplicate `N` schedules", where `N` is the number of failed schedules. This is now fixed and the user is able to duplicate all schedules.

## Backend v1.15.9 (May 7, 2020)

A backend release went out addressing a customer concern about 0-byte files into Office 365, and with many more enhancements that don't currently have a direct user impact but will enable future improvements for our end users.

- Migrations going into Office 365 will not skip 0-byte file anymore and will be successfully transferred to the destination. However, migrations going into OneDrive Consumer or OneDrive for Business (Single User) will still skip 0-byte files as those services still restrict non-administrator transfers from creating zero-byte files.

## Frontend v1.15.3 (May 1, 2020)

A frontend deployment to speed up bulk operation.

- Doing bulk operations on users in the Migration Manager would be slow when a lot of users were selected. Speed improvements to these operations have been introduced by using a new version of the Mover API.

## Frontend v1.15.2.1 (April 29, 2020)

A small deploy fixing a frontend issue. But also testing part of our infrastructure move to Azure.

- When trying to create a folder from the File Picker view for a connector, "Unknown error" is displayed to the user. This is now fixed and folder creation is working properly again.

## Backend v1.15.8.1 (April 28, 2020)

Release to address customer issues with migrations.

- When Downloading User Logs in zip format, if the source and destination directories are too long (their) system cannot open the (downloaded) zip file because there is a filename length limitation of 255 characters (in zip files). This is now fixed, they can download and open zip file (even when source and destination directories are very long).
- When scanning is done on a migration/schedule the scanner reports are generated and available for download in the Migration Manager UI. The generated reports include a Common Path report which was missing a new line character at the end of the headers, causing a malformed row formatting with the first common path record in the same row as the header. A fix has been implemented to ensure the report is presented in proper CSV format and is readable.

## Backend v1.15.7 (April 23, 2020)

Backend release to address a customer migration.

- In Dropbox, Team Folders that are no longer shared with anyone would make a transfer fail when listing the containing folder. This has now been fixed and unshared Team Folders are handled properly.

## Backend v1.15.6 (April 23,2020)

Backend release with customer fixes.

- Managers are now able to delete the account of a managed user by entering their own password instead of the managed user's password.
- Add support to traverse and transfer archived Team Folders out of the Dropbox (Administrator) connector.

## Frontend v1.15.1 (April 21, 2020)

- Connector Authorization window where the user selects what connector to authorize now displays the full connector names without truncating them (on mobile phones, tablets and desktop).

## Backend 1.15.5.1 (April 21, 2020)

A backend release that includes customer fixes, expanding support for Dropbox and Google Drive (G Suite) scenarios.

- In Dropbox, shared folders without an owner were making transfers fail at the containing folder. This is now fixed by letting the transfers traverse everything except those problematic folders (as opposed to their containing folders). Shared folders can have no owner because the original owner is no longer part of the Dropbox business account. Users are properly informed of this through the corresponding entry in the user log.
- In Dropbox, archived Team Folders would make a transfer fail when listing the containing folder. This has now been fixed and archived Team Folders are handled properly.
- Transferring Google Documents out of Google Drive or G Suite (Admin) was previously restricted to documents at most 10MB in size. This restriction is no longer in place and users should be able to export larger Google Documents into their Office 365 counterparts.
- There was an issue where users could not create folders at the root of a Single User connector. This has been fixed and users should be able to create folders at the root of Single User connectors now.
- Connectors were not being deleted immediately when the user deleted their account. Instead, connectors would get deleted when the account retention policy monitor would clean them up. This has been changed so that connectors are deleted right away.

## Backend v1.15.4 (April 9, 2020)

Backend release to address handling of Dropbox Team folders. This is a work in progress to catch up with the latest features related to Team Folders, but it fixes urgent issues to unblock customers.

- Fixed handling of Dropbox Team Folders and unique permissions within subfolders. Team Folders will be listed on the root of the Dropbox (Admin) connector, as well as under each user that has access to them. However, to prevent data duplication, Team Folders will NOT be transferred if they are listed under a user. Team Folders are only transferred when traversing them directly from the root of the Dropbox (Admin) connector. Also, permissions for Team Folders and its subfolders are properly exported now, including restrictive permissions.

## Backend v1.15.3 (April 8, 2020)

Small but critical backend release for migrations out of G Suite (Admin). Please read the impact statement carefully.

- Fixes a specific case in migrations from G Suite (Admin) that would end up in data duplication. The case relates to folders in an "owner" root that were shared with other users ("guest") and "guest" mounted the folder not in their root folder but somewhere deeper in their tree. In this case, the transfer would not obey the user priority list resulting in the folder being transferred for both "owner" and "guest". This regression was introduced on March 1, 2019 and is fixed now. Full impact is still being assessed. There is no need to re-run Google Prescans for affected migrations; instead, re-running the transfers will now skip the folder in question appropriately. Remediation for affected customers is to manually removed the duplicated data (upon identification).

## Backend v1.15.1 (April 2, 2020)

A backend release that includes bug fix and stability improvements.

- Users creating a new Mover account using the Sign in with Microsoft account feature will have appropriate access to running all types of transfers (some transfers appeared as not allowed to some new users).

## Backend & Frontend v1.15.0 (April 1, 2020)

- A new "Support" link will be displayed in the top navigation bar in the app. This link will point users to the new support system. The intercom widget will be disabled in the application.
- Brand new users and current users with a Microsoft account will be able to sign into the Mover app with their Microsoft account. This includes work/school and personal accounts. Existing Mover accounts will continue to be supported.

## Backend v1.14.1.1 (March 31, 2020)

- Fixed an issue with very old migrations with permission mappings that would prevent the app from loading. Support for these old migrations have been fixed.
- For transfers that convert Box Notes to Word Documents only. Box notes images that are not supported by Word Docx will now be converted to a format acceptable by Word Docx and will be displayed properly in the document.
- When the Mover app is loaded, the Migration Manager will default to the latest Migration instead of oldest Migration (this was a regression from a previous release).
- This adds an extra column for schedule tags in all migration and scan reports that aggregate by user/schedule.

## Backend & Frontend v1.14.0 (March 26,2020)

A combined backend/frontend deploy with some fixes to reports and disabling the Intercom widget.

- Accurate stats for files and bytes (success, failure, skipped, unsupported) will be displayed in the Migration Report. There will be no discrepancy for the stats shown in the report versus what's displayed in the Migration Manager UI.
- The Migration Manager UI will not be stuck for users that have migrations with very large permission mappings. Instead, the app will load permission mappings as needed (when editing them). If a migration has an excessively large permission mapping, the app will not display the editor. Instead, the user will be able to download the permission mapping as CSV, edit and then re-upload the CSV.
- The intercom widget will be disabled in the application.

## Backend v1.13.10 (March 24, 2020)

A backend release with a new feature and potential performance fix.

- Unique permissions from items within a Dropbox Team Folder will now be moved to the destination.

## Backend v1.13.9 (March 20, 2020)

Backend release to assist with the increased loads.

- There were cases in which transfer cancellations were taking a long time to take effect. This fixes the issue by ensuring they happen faster.

## Backend v1.13.7 (March 17, 2020)

Backend release with changes to help us determine the root cause for customer issues.

- Transfers from the Egnyte root directory or the Private directory will not incur in a validation error and the user will be allowed to migrate out of those folders.

## Backend v1.13.5 (March 11, 2020)

- After a user runs a scan on a schedule, the scan reports (Long Paths, Common Paths, Large Files, Files Extension, Migration Scan Summary Report) were being generated sometimes with a pretty long delay. This is being fixed now. Also, the Migration Actions menu in the Migration Manager will update in real time when the scan reports finish generating and the proper count will be shown for the Scan Reports (zip file) menu item.

## Backend v1.13.4 (March 9, 2020)

- User will see improved speeds both when initially loading the schedules table in the Migration Manager, and when refreshing the data in it. The table should load in under 60 seconds now for huge migrations (100K+ schedules with multiple runs per schedule). Most importantly, users should not see the table failing to load in the UI due to size (may fail due to other normal issues like network problems). Average migrations will load instantaneously. Ultimate goal is to improve UX so that the table would load instantaneously for migrations of all sizes.
