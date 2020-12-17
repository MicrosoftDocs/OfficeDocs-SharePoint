---
title: "What's new in Migration Manager"
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
- **Support replacing invalid characters**. To help migrate files with invalid characters in the file name, users will be able to specify pre-defined characters to replace invalid characters. 
- **Auto site provisioning.** When migrating to SharePoint sites, if the site doesn't exist, it will be auto-provisioned before we start the migration.
- **Fix for zero durations in Summary Reports.** We recently introduced an issue where the duration field was showing zero values in the *SummaryReport.csv*. This has been fixed and will roll out to your tenants soon. 

  
## Current features through December 2020

- **Process multiple tasks per agent.** Each agent can now process 5-10 migration tasks, simulaneously so that you can finish your migrations faster.
- **Select a Teams as a destination.** Users will be able to select a Teams team and the channel as the migration destination. This is in addition to the existing ability to specify a Teams location by the URL.
- **Select a OneDrive email as a destination.** Users will be able to input a OneDrive email address as the migration destination. This is in addition to the existing ability to specify a OneDrive location by the URL.


## Features through October 2020 

- **Increased bulk task upload limits**. Users can create up to 50,000 separate migration tasks. This is an increase from the previous limit of 5,000 tasks in the bulk file.
- **Task management**. Users can filter, sort, and perform searches on their migration tasks.
- **Bulk task validation**. When using a CSV for bulk task creation, Migration Manager validates the first destination site URL to help users identify any potential issues.
- **Government cloud**. Migration Manager supports GCCHigh/DoD tenants.
- **Vanity URL**. Migration manager supports vanity URLs.
- **Installation issues**. Fixed issues which caused common agent installation failure.
- **Report aggregator**.  Detailed task level reports can be generated via a PowerShell cmdlet.  See [Download detailed task reports](https://docs.microsoft.com/sharepointmigration/mm-reports#download-detailed-task-reports).
- **General improvements**. Overall fit and finish to improve your experience.

