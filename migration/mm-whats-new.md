---
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
mscollection: 
- SPMigration
- M365-collaboration
localization_priority: Normal
search.appverid: MET150
description: "Learn about the new features and updates to existing features in Migration Manager."
---

# What's new in Migration Manager

We're continuously adding new features to Migration Manager and fixing issues we learn about. Here's a summary of what's included.   

#### We're listening!

Help us improve Migration Manager by sending your suggestions and reporting bugs you encounter. Just select the feedback button at the bottom of the page.  


## June 2021

- **Scan file shares (preview).**  Scan and view your sources for migration readiness. Learn more: [Migration Manager Scan (preview)](mm-scan.md)
- **Agent app mode**. Install agent on non-domain joined computers (app mode). You now haave the option of installing the Migration Manager agent on non-domain joined computers using an agent app.

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