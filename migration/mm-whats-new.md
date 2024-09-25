---
ms.date: 09/17/2024
title: "What's new in Migration Manager"
ms.reviewer: 
ms.author: heidip
author: MicrosoftHeidi
manager: jtremper
recommendations: true
audience: ITPro
f1.keywords:
- CSH
ms.topic: article
ms.service: microsoft-365-migration
mscollection: 
- SPMigration
- M365-collaboration
- m365initiative-migratetom365
ms.localizationpriority: medium
search.appverid: MET150
description: "Learn about the new features and updates to existing features in Migration Manager."
---

# What's new in Migration Manager

We're continuously adding new features to Migration Manager and fixing issues we learn about. Here's a summary of what's to come and new features that are now available.

## We're listening!

Help us improve Migration Manager by sending your suggestions and reporting bugs you encounter. Just select the feedback button at the bottom of the page.  


## Coming soon
- **Larger file support.** The size limit of a single file that can be migrated will be increased to improve migration fidelity.
- **File version migration.** Support for migrating file version histories in cloud scenarios.

## Sep 2024
- **New Migration transition.** Migration Manager is undergoing a transition to provide a more scalable migration service. Tenants with ongoing migration projects will experience transition UI elements. [Learn more about the transition](new-migration-transition.md).
- **Improved connection wizard.** Customers now have access to quick migration settings immediately upon connecting to cloud sources.

## Aug 2024
- **Revamped "Copy to Migrations" panel.** The panel has been redesigned, enabling destination uploads and task-level customization while sending scanned tasks to the Migrations tab, improving migration flow efficiency.
- **Unified Filter experience.** Filter functionality has been standardized across the Scans and Migrations tabs for a consistent user experience.

## July 2024

- **Migration Manager Agent v2.3 (for File Share migration).** Enhanced throttling handling mechanism, which reduces task failures caused by throttling. The v2.3 build is now in public preview: [Download link](https://spmtreleasescus.blob.core.windows.net/download/697b3ea6-1f82-4185-9e69-5111a6a90d75/agentsetup.exe)

## May 2024
- **Identity mapping flow refinement.** First selection of the "Migrate" button triggers the identity mapping setting that is a key prerequisite to a successful migration.
- **Identity mapping capacity.** The entry limit for identity mapping is increasing from 50K to 500K to better support large migrations. Additionally, single entry addition, identity exporting, and identity clearing features are enabled to help you better organize identity mapping.

## April 2024

- **Forms migration.** You can now migrate Google Forms by default. "Forms destination" is required during Forms migration. [Learn more about Forms destination](/sharepointmigration/mm-google-step4-review-destinations).

## March 2024

- **Skip scan.** You can now skip scan process in Box migration scenario. Once the users (tasks) are added to the Scan list, they can be send to Migrations tab instantly for migration operations.

## February 2024
- **Download limit increase.** Now download up to 5,000 tasks for summary reports and 500 tasks for detailed reports. [Learn more about report types and download limits](mm-cloud-reports.md).
- **Migration Manager Agent v2.0 (for File Share migration).** Enhanced multitasking and report uploading capabilities improve agent performance. The v2.0 build is now generally available: [Download link](https://spmtreleasescus.blob.core.windows.net/mmagent/agentsetup.exe).
- **Recent action panel redesign.** Redesigned for a smoother report downloading experience, with progress prompts for download job status updates.
- **Migration admin role.** New role to grant users only migration admin privileges for seamless migrations within Microsoft Admin Center. Applicable to cloud migrations from Google Drive, Dropbox, Box, and Egnyte.

## December 2023

- **Simplified permission setting**. The permission setting panel is revamped to provide a concise yet clear configuration experience. Access this setting through "Project settings - Permission" at the top right corner of the Migration Manager UI.

## November 2023
- **Destination validation.** Destination paths are now validated automatically during the bulk destination upload process. A validation report is provided to let fix issues that are discovered. Note: While the validation step is optional, we don’t recommend skipping it.
- **Shared drive permission.** Google Shared Drive permissions are now migrated by default according to what you set in permission settings.

## October 2023
- **Scan/Migration status update.** Improvements were made to let you organize the status of drives better. For guidance on different task statuses, see: [Migration Manager status codes](/sharepointmigration/mm-cloud-reports#status-codes)
- **Migration time estimator.** Get an estimated migration time before connecting to a migration source. The migration time estimator is located at the top right corner of the project page.
- **Report improvements.** Report fields and failure reasons are polished to provide a more readable and consistent reporting experience. 


## September 2023

- **New. File Level Permission for Dropbox and Box.** Support for File Level Permission (FLP) migration for Dropbox and Box. *This feature is already available for **Google Drive** (as of June 8, 2023.)*

- **Fixed. 'Share with me' support.** Some issues related to the migration of "Share with me" event are resolved.
- **Fixed. Task deletion.** Task deletion triggered in the UX is now consistently reflected in the backend, reducing deletion failures.


## August 2023

- **New. Box Notes conversion.** Migration Manager now supports converting Box notes to .docx format. Note: Certain elements such as File Preview, Table of Contents, and Annotations are omitted during the conversion process.


## July 2023

- **New. Multi-project support.** You can now create up to 5 separate projects per cloud source. For instance, you can create and simultaneously migrate up to 5 separate Box tenants. Multi-project feature makes acquisitions and mergers easier to consolidate into one M365 tenant.


## June 2023

- **New. File level permission migration.** For Google Drive migration, customers can now enable File Level Permission (FLP) migration in the "Settings - Sharing & metadata" section, located in the top right corner.
- **Change. Summary report bulk download optimization.** Streamlined the download process by disabling the option to download all summary report when no drives are selected. To download multiple summary reports efficiently, use the multi-select or select-all function on drives.

## May 2023

- **New. Overview page.** A new guided tour can be accessed from the overview page, to walk you through key migration steps and present general overviews of each core migration step. Links to relevant documentation are available at each stage.
- **New. Migration filter setting.**  You can now use factors such as dates, file types, and invalid characters to filter content for migration. Select filters from the migration setting panel that displays when scanned tasks are "copied to migration."
- **Change. Summary report limit increase.** When bulk-downloading a scan or migration summary report for selected tasks, you can select up to 1000 tasks. The previous limit was 100.


## April 2023

- **Important changes for European Union (EU) users.**  Beginning April 1, 2023, all new EU scans and migrations will be processed in the EU. For complete details, learn more at [Migration Manager and The European Union Data Boundary (EUDB)](mm-eudb.md)

## March 2023

- **Change. Report downloads in the action menu bar.** Downloading your reports is consolidated in the action menu bar. The View logs link is removed to improve resource consumption and align with how Scan logs are downloaded. [Learn more about downloading summary and detailed reports](mm-cloud-reports.md)

- **Fixed. Dropbox migrated permissions**. Customers were experiencing some Dropbox file and folder permissions not being migrated. This issue has been fixed.

## February 2023

- **Fixed. Summary report timeout.** Large reports would occasionally exceed database memory, leading to report download timeout. This has been fixed.
- **Display of the estimated time**. There's now display of the estimated time it takes for your Google Drive migration to complete.

## January 2023

- **Fixed:  Report aggregator script**. The Report aggregator script was incorrectly converting bytes to gigabytes. This has now been fixed. [Learn more: Download detailed task reports.](/sharepointmigration/mm-reports#download-detailed-task-level-reports-via-powershell) 


## Released in 2022

### December 2022

- **Fixed: Upload failures logs**. Items that failed in SPO (SharePoint Online) upload process weren't listed in the migration log, and was inconsistent with the final migration result. This has been fixed. 

- **Report fields refined**. The fields of downloaded reports are improved for clarity and readability.

### October 2022

- **Change - Box Notes**. We're no longer able to convert Box notes to a .docx file during migration.

### June 2022

- **Fix: Google proprietary file formats failed to migrate**. Some Google files (mainly  Google slides) failed to migrate showing the error code, "MFILESIZEINCORRECT". This has been fixed. Rerun any failed tasks to migrate these files.
- **Tag support for File share migrations**. The tags feature File Share migrations lets you sort, organize, and navigate through a large quantity of sources and users.

### May 2022

- **Fixed: Box connection**. A recent change from Box makes the Microsoft 365 Migration app  a server auth app that later fails to authorize the user's account and connect. This has been fixed.

### April 2022

- **Task increase**. We now support up to 50,000 tasks per tenant for cloud migrations (GoogleDrive, Box, Dropbox, and Egnyte). File share migrations already support 50,000 tasks.

### March 2022

- **Egnyte migrations**. Migrate your Egnyte content to Microsoft 365.

### February 2022

- **Workaround for Geo admins**. Migration currently doesn't fully support the Geo admin role. See [Workaround for Geo admins using Migration Manager](mm-troubleshoot.md)
- **Workaround for Azured-acquired SharePoint admins**. SharePoint admins created via groups can't access Migration Manager scan and migration tabs. See [Workaround for Group-inherited SharePoint Admins using Migration Manager](mm-troubleshoot.md)

### January 2022

- **Add source path fix**. Previously, when doing a file share migration, the "Add source Path" button wasn't active on the Scan page, even if the agent was installed and connected. Fixed.
- **Tag support - cloud migrations**.  A new tag feature lets you sort, organize, and navigate through a large quantity of sources and users. Available for cloud migrations only.

## Released in 2021

### November 2021

- **Bulk upload Google drives.**  You can now bulk upload your Google drives using a comma-separated (CSV) file. 
- **Report creation failure fixed.** Mover API failed to create reports on scans and migrations involving more than 40,000 records. This has been fixed. 

### September 2021


- **Support for files up to 100 GB.** File share migration now supports migrating individual files of up to 100 GB.
- **Improved agent installation messages.**  The error messages during agent installation are improved.

- **Reinstall recommended message.** A "Reinstall recommended" message displays detailed information as to why it is needed. 

- **Cross-geo site fix.**  If the destination cross-geo site didn't exist, the migration would fail. This has been fixed.
- **Agent service and Agent app on same computer upgrader issue fix.**  When the agent app and agent service were both installed on the same computer, the upgrader would always start the agent app after the agent service was updated. Fixed.
- **Agent service and Agent app on same computer file share fix.** When the agent service and the agent app were installed on the same computer, file share migration tasks would fail. Fixed.
- **Selected task reports deprecated.** Several task reports are deprecated, including the *performance recommendation.csv* report, as they contained inaccurate or unnecessary information. Users should use the customer-facing dashboard in Migration Manager for performance analysis and improvement recommendations.

### August 2021

- **Task scheduling**. Schedule your migration tasks in advance to run at the optimum time your organization.

- **Migrations during high load issues fixed.** Some transfers from Box, Google, and Dropbox saw many failures when moving files during high load periods. The errors would appear in the migration error report as "Failed to load migration job, please retry." The issues causing these errors are fixed and the reliability of transfers is increased.

### July 2021
- **Box migrations (GA).** You can now migrate Box content to Microsoft 365 using Migration Manager.
- **Google migrations (GA).** Migrate your Google Drives to Microsoft 365.
- **Dropbox migrations (GA).** You now can migrate your Dropbox content to Microsoft 365.

### June 2021

- **Scan file shares (preview).** Scan and view your sources for migration readiness. Learn more: [Migration Manager Scan (preview)](mm-scan.md)

- **Agent app mode**. Install agent on non-domain joined computers (app mode). You now have the option of installing the Migration Manager agent on non-domain joined computers using an agent app.

### May 2021

- **Auto site provisioning.** When migrating to SharePoint sites, if the site doesn't exist, it is automatically provisioned before the migration starts.

- **Performance dashboard for file shares.** View your performance history, and if needed, be provided prescriptive guidance on how to improve in impacted areas. *Requires latest version of agent.*

- **Google migrations (preview).** Migrate your Google Drives to Microsoft 365.
- **Dropbox migrations (preview).** You now can migrate your Dropbox content to Microsoft 365.

### April 2021

- **Box migrations (preview).** You can now migrate Box content to Microsoft 365 using Migration Manager (preview).
- **CSV optional header.** Users have the option of including optional headers in the bulk upload file.

### March 2021

- **Agent groups and agent targeting.** You can now create an "agent group" and assign one or more agents to it. A group may represent a particular geographical location or other targeted purpose. After creating an agent group, you can target only that group of agents to run your tasks. To learn more, see: [Agent groups in Migration Manager](mm-agent-targeting.md).
- **Summary report enhancements.** *TaskID*, *Task failure reason*, and *Agent group* is added to the task summary report.

- **Date completed column**. A date completed column has been added so customers know the exact date when the task completed processing.

### February 2021

- **Support replacing invalid characters**. To help migrate files with invalid characters in the file name, users can now specify predefined characters to replace invalid characters. *Requires latest version of agent.*
- **Configure working folder for agents**. Through the Migration Manager UI, you can configure the physical location of the folder where logs and reports are stored on the agent's machine. You can also see the available disk space so you can choose a drive that has enough storage before starting your migration. *Requires latest version of agent.*
- **Filters for report aggregator script**. You can now apply rich filters when downloading the detailed task level reports via the PowerShell cmdlet. To learn more, see: [Download detailed task reports](mm-reports.md#download-detailed-task-level-reports-via-powershell).
-  **Fix for zero durations in Summary Reports.** We recently introduced an issue where the duration field was showing zero values in the *SummaryReport.csv*. This has been fixed. *Requires latest version of agent.*
- **Fix for large file upload.**  Report files larger than 250 MB can now be uploaded. *Requires latest version of agent.*
- **Fix for non-English sites.**  Fixed the issue where Documents1 library was getting created for non-English sites. *Requires latest version of agent.*


## Earlier releases

### December 2020

- **Process multiple tasks per agent.** Each agent can now process 5-10 migration tasks, simultaneously so that you can finish your migrations faster. *Requires latest version of agent.*
- **Select a team as a destination.** Users are able to select a Teams team and the channel as the migration destination. This is in addition to the existing ability to specify a Teams location by the URL.
- **Select a OneDrive email as a destination.** Users are able to input a OneDrive email address as the migration destination. This is in addition to the existing ability to specify a OneDrive location by the URL.


### October 2020 

- **Increased bulk task upload limits**. Users can create up to 50,000 separate migration tasks. This is an increase from the previous limit of 5,000 tasks in the bulk file.
- **Task management**. Users can filter, sort, and perform searches on their migration tasks.
- **Bulk task validation**. When using a CSV for bulk task creation, Migration Manager validates the first destination site URL to help users identify any potential issues.
- **Government cloud**. Migration Manager supports GCCHigh/DoD tenants.
- **Vanity URL**. Migration manager supports vanity URLs.
- **Installation issues**. Fixed issues that caused common agent installation failure.
- **Report aggregator**.  Detailed task level reports can be generated via a PowerShell cmdlet.  See [Download detailed task reports](mm-reports.md#download-detailed-task-level-reports-via-powershell).
- **General improvements**. Overall fit and finish to improve your experience.

