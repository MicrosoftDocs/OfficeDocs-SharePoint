---
ms.date: 10/19/2020
title: "What's new in Migration Manager"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: serdars
recommendations: true
audience: ITPro
f1.keywords:
- CSH
ms.topic: article
ms.service: sharepoint-online
ms.subservice: sharepoint-migration
mscollection: 
- SPMigration
- M365-collaboration
- m365initiative-migratetom365
ms.localizationpriority: medium
search.appverid: MET150
description: "Learn about the new features and updates to existing features in Migration Manager."
---

# What's new in Migration Manager

We're continuously adding new features to Migration Manager and fixing issues we learn about. Here's a summary of what's included.  

#### We're listening!

Help us improve Migration Manager by sending your suggestions and reporting bugs you encounter. Just select the feedback button at the bottom of the page.  

## Coming soon

- Several enhancements are coming to Google Workspace migrations. New features include:
  -  Filtering by factors such as dates, file types, and invalid characters
  -  Downloading bulk reports


## March 2023

- **Change**. Downloading your migration reports has been consolidated in the action menu bar. The *View logs* link has been removed to improve resource consumption and align with how Scan logs are downloaded.
- 
## February 2023

- **Fixed. Summary report timeout.** Extremely large reports would occasionally exceed database memory, leading to report download timeout. This has been fixed.
- **Display of the estimated time**. There is now display of the estimated time it will take for your Google Drive migration to complete.

## January 2023
- **Fixed:  Report aggregator script**. The Report aggregator script was incorrectly converting bytes to gigabytes. This has now been fixed. [Learn more: Download detailed task reports.](/sharepointmigration/mm-reports#download-detailed-task-level-reports-via-powershell) 


## December 2022
- **Fixed: Upload failures logs**. Items that failed in SPO upload process weren't listed in the migration log, and was inconsistent with the final migration result. This has been fixed. 
- **Report fields refined**. The fields of downloaded reports have been improved for clarity and readability.


## October 2022
- **Change - Box Notes**. We're no longer able to convert Box notes to a .docx file during migration.

## June 2022
- **Fix: Google proprietary file formats failed to migrate**. Some Google files (mainly  Google slides) failed to migrate showing the error code, "MFILESIZEINCORRECT". This has been fixed. Rerun any failed tasks to migrate these files.
- **Tag support for File share migrations**.  The tags feature File Share migrations lets you sort, organize, and navigate through a large quantity of sources and users.

## May 2022
- **Fixed: Box connection**. A recent change from Box makes the Microsoft 365 Migration app  a server auth app that later fails to authorize the user's account and connect. This has been fixed.

## April 2022

- **Task increase**.  We now support up to 50,000 tasks per tenant for cloud migrations (GoogleDrive, Box, Dropbox and Egnyte). File share migrations already support 50,000 tasks.

## March 2022
- **Egnyte migrations**.  Migrate your Egnyte content to Microsoft 365.

## February 2022

- **Workaround for Geo admins**. Migration currently doesn't fully support the Geo admin role. See [Workaround for Geo admins using Migration Manager](mm-troubleshoot.md)
- **Workaround for Azured-acquired SharePoint admins**. SharePoint admins created via groups can't access Migration Manager scan and migration tabs.  See [Workaround for Group-inherited SharePoint Admins using Migration Manager](mm-troubleshoot.md)

## January 2022

- **Add source path fix**. Previously, when doing a file share migration, the "Add source Path" button wasn't active on the Scan page, even if the agent was installed and connected. Fixed.
- **Tag support - cloud migrations**.  A new tag feature lets you sort, organize, and navigate through a large quantity of sources and users. Available for cloud migrations only.


## November 2021

- **Bulk upload Google drives.**  You can now bulk upload your Google drives using a comma-separated (CSV) file. 
- **Report creation failure fixed.** Mover API failed to create reports on scans and migrations involving more than 40,000 records. This has been fixed. 

## September 2021


- **Support for files up to 100 GB.** File share migration now supports migrating individual files of up to 100 GB.
- **Improved agent installation messages.**  The error messages during agent installation have been improved.
- **Reinstall recommended message.** A "Reinstall recommended" message displays detailed information as to why it's needed. 
- **Cross-geo site fix.**  If the destination cross-geo site didn't exist, the migration would fail. This has been fixed.
- **Agent service and Agent app on same computer upgrader issue fix.**  When the agent app and agent service were both installed on the same computer, the upgrader would always start the agent app after the agent service was updated. Fixed.
- **Agent service and Agent app on same computer file share fix.** When the agent service and the agent app were installed on the same computer, file share migration tasks would fail. Fixed.
- **Selected task reports deprecated.** Several task reports have been deprecated, including the *performance recommendation.csv* report, as they contained inaccurate or unnecessary information. Users should use the customer-facing dashboard in Migration Manager for performance analysis and improvement recommendations.



## August 2021

- **Task scheduling**.  Schedule your migration tasks in advance to run at the optimum time your organization.
- **Migrations during high load issues fixed.**  Some transfers from Box, Google, and Dropbox saw many failures when moving files during high load periods. The errors would appear in the migration error report as "Failed to load migration job, please retry." The issues causing these errors has been fixed and the reliability of transfers has increased.



## July 2021
- **Box migrations (GA).**  You can now migrate Box content to Microsoft 365 using Migration Manager.
- **Google migrations (GA).**  Migrate your Google Drives to Microsoft 365.
- **Dropbox migrations (GA).**  You now can migrate your Dropbox content to Microsoft 365.
 
## June 2021

- **Scan file shares (preview).**  Scan and view your sources for migration readiness. Learn more: [Migration Manager Scan (preview)](mm-scan.md)
- **Agent app mode**. Install agent on non-domain joined computers (app mode). You now have the option of installing the Migration Manager agent on non-domain joined computers using an agent app.

## May 2021

- **Auto site provisioning.** When migrating to SharePoint sites, if the site doesn't exist, it will be automatically provisioned before the migration starts.
- **Performance dashboard for file shares.**  View your performance history, and if needed, be provided prescriptive guidance on how to improve in impacted areas. *Requires latest version of agent.*
- **Google migrations (preview).**  Migrate your Google Drives to Microsoft 365.
- **Dropbox migrations (preview).**  You now can migrate your Dropbox content to Microsoft 365.

## April 2021

- **Box migrations (preview).**.  You can now migrate Box content to Microsoft 365 using Migration Manager (preview).
- **CSV optional header.**  Users have the option of including optional headers in the bulk upload file.

## March 2021

- **Agent groups and agent targeting.** You can now create an "agent group" and assign one or more agents to it. A group may represent a particular geographical location or other targeted purpose. After creating an agent group(s), you can target your tasks to be run by only that group of agents. To learn more, see: [Agent groups in Migration Manager](mm-agent-targeting.md).
- **Summary report enhancements.** *TaskID*, *Task failure reason*, and *Agent group* have been added to the task summary report.
- **Date completed column**.  A date completed column has been added so customers know the exact date when the task completed processing.

## February 2021

- **Support replacing invalid characters**. To help migrate files with invalid characters in the file name, users can now specify pre-defined characters to replace invalid characters. *Requires latest version of agent.*
- **Configure working folder for agents**. Through the Migration Manager UI, you can configure the physical location of the folder where logs and reports are stored on the agent's machine. You can also see the available disc space so you can choose a drive that has enough storage before starting your migration. *Requires latest version of agent.*
- **Filters for report aggregator script**.  You can now apply rich filters when downloading the detailed task level reports via the PowerShell cmdlet. To learn more, see: [Download detailed task reports](mm-reports.md#download-detailed-task-level-reports-via-powershell).
-  **Fix for zero durations in Summary Reports.** We recently introduced an issue where the duration field was showing zero values in the *SummaryReport.csv*. This has been fixed. *Requires latest version of agent.*
- **Fix for large file upload.**  Report files larger than 250 MB can now be uploaded. *Requires latest version of agent.*
- **Fix for non-English sites.**  Fixed the issue where Documents1 library was getting created for non-English sites. *Requires latest version of agent.*



## December 2020

- **Process multiple tasks per agent.** Each agent can now process 5-10 migration tasks, simultaneously so that you can finish your migrations faster. *Requires latest version of agent.*
- **Select a team as a destination.** Users will be able to select a Teams team and the channel as the migration destination. This is in addition to the existing ability to specify a Teams location by the URL.
- **Select a OneDrive email as a destination.** Users will be able to input a OneDrive email address as the migration destination. This is in addition to the existing ability to specify a OneDrive location by the URL.


## October 2020 

- **Increased bulk task upload limits**. Users can create up to 50,000 separate migration tasks. This is an increase from the previous limit of 5,000 tasks in the bulk file.
- **Task management**. Users can filter, sort, and perform searches on their migration tasks.
- **Bulk task validation**. When using a CSV for bulk task creation, Migration Manager validates the first destination site URL to help users identify any potential issues.
- **Government cloud**. Migration Manager supports GCCHigh/DoD tenants.
- **Vanity URL**. Migration manager supports vanity URLs.
- **Installation issues**. Fixed issues that caused common agent installation failure.
- **Report aggregator**.  Detailed task level reports can be generated via a PowerShell cmdlet.  See [Download detailed task reports](mm-reports.md#download-detailed-task-level-reports-via-powershell).
- **General improvements**. Overall fit and finish to improve your experience.

