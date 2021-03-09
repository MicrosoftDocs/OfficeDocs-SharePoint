---
title: "What's new in Migration Manager"
recommendations: true
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: serdars
audience: ITPro
f1.keywords:
- NOCSH
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

You can help us improve Migration Manager by sending us your suggestions and reporting bugs you encounter. At the bottom of this page, click the Feedback button.

## Coming soon


- **Auto site provisioning.** When migrating to SharePoint sites, if the site doesn't exist, it will be automatically provisioned before we start the migration.
- **Summary report enhancements.** The TaskID and reason for task failure will be added to the task summary report.
- **CSV optional header.**  Soon users will have the options of including optional headers in the bulk upload file.
- **Agent targeting.** If you want to target migration tasks to a group of agents, you will be able to do so. 

  
## Current features and improvements through February 2021

- **Support replacing invalid characters**. To help migrate files with invalid characters in the file name, users can now specify pre-defined characters to replace invalid characters. 
- **Configure working folder for agents**. Through the Migration Manager UI, you can configure the physical location of the folder where logs and reports are stored on the agent's machine. You can also see the available disc space so you can choose a drive that has enough storage before starting your migration.
- **Filters for report aggregator script**.  You can now apply rich filters when downloading the detailed task level reports via the PowerShell cmdlet.  See [Download detailed task reports](https://docs.microsoft.com/sharepointmigration/mm-reports#download-detailed-task-reports).
-  **Fix for zero durations in Summary Reports.** We recently introduced an issue where the duration field was showing zero values in the *SummaryReport.csv*. This has been fixed.
- **Fix for large file upload.**  Report files larger than 250 MB can now be uploaded.
- **Fix for non-English sites.**  Fixed the issue where Documents1 library was getting created for non-English sites.



## December 2020

- **Process multiple tasks per agent.** Each agent can now process 5-10 migration tasks, simultaneously so that you can finish your migrations faster.
- **Select a team as a destination.** Users will be able to select a Teams team and the channel as the migration destination. This is in addition to the existing ability to specify a Teams location by the URL.
- **Select a OneDrive email as a destination.** Users will be able to input a OneDrive email address as the migration destination. This is in addition to the existing ability to specify a OneDrive location by the URL.


## October 2020 

- **Increased bulk task upload limits**. Users can create up to 50,000 separate migration tasks. This is an increase from the previous limit of 5,000 tasks in the bulk file.
- **Task management**. Users can filter, sort, and perform searches on their migration tasks.
- **Bulk task validation**. When using a CSV for bulk task creation, Migration Manager validates the first destination site URL to help users identify any potential issues.
- **Government cloud**. Migration Manager supports GCCHigh/DoD tenants.
- **Vanity URL**. Migration manager supports vanity URLs.
- **Installation issues**. Fixed issues that caused common agent installation failure.
- **Report aggregator**.  Detailed task level reports can be generated via a PowerShell cmdlet.  See [Download detailed task reports](https://docs.microsoft.com/sharepointmigration/mm-reports#download-detailed-task-reports).
- **General improvements**. Overall fit and finish to improve your experience.

