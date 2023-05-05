---
ms.date: 10/11/2019
title: "Migrate your files to Microsoft 365 with Migration Manager"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: serdars
recommendations: true
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.subservice: sharepoint-migration
ms.localizationpriority: high
ms.collection: 
- M365-collaboration
- SPMigration
- m365solution-migratetom365
- m365solution-scenario
- highpri
ms.custom:
- seo-marvel-apr2020
- admindeeplinkSPO
search.appverid: MET150
description: "Learn about how the Migration Manager tool in the modern SharePoint Admin Center works and how to get started with it."
---

# Overview: Migrate your file shares to Microsoft 365

Migrating your on-premises file share content to Microsoft 365 lets you collaborate with innovative Office apps, intelligent cloud services, world-class security, and the rich features offered in Microsoft SharePoint, Teams, and OneDrive. Migration Manager helps you get there.

With the ability to set up multiple servers as "agents", Migration Manager lets you scale your migration project as much as you need. Located in the modern SharePoint Admin Center, Migration Manager guides you through the setup of your agents and the creation of your tasks. You can specify global or task level settings, view all-up task progress, and download aggregated summary and task-level reports. Migration Manager also provides advanced features such as grouping agents to optimize performance, conduct pre-scans, and implement file exclusion metrics.

## How does it work?


![Set up migration agents](media/mm-flow-3box.png)

- **Setup migration agents.** Download and install a lightweight agent on each computer or virtual machine you want to connect to Migration Manager. The agent runs as a service and authenticates to both your Microsoft 365 destination and your on-premises source.

- **Create tasks & migrate.** Create a task by entering the URL of the network file share that you want to migrate (your source) and the URL of the SharePoint site where you are migrating your content (your destination), or upload a CSV file for multiple user migrations. Your tasks will be automatically assigned to the next available agent in the assigned agent group.

- **Monitor and report.** Monitor progress across all agents, download summaries of migration jobs, and download detailed data on each individual migration.

## File size migration limit

We support files up to 250 GB in size for file share to Microsoft 365 migrations.


## Prerequisites & permissions


|Requirement|Notes|
|:-----|:-----|
|System requirements| [Migration Manager system requirements](mm-prerequisites.md#prerequisites)|
|Endpoints| [Migration Manager required endpoints](mm-prerequisites.md#required-endpoints). Make sure your computer or VM has the required endpoints open.|
|SMB 2.0|For file share migration, the server hosting the source data must support SMB 2.0 or higher|
|Access to the destination|You must either be a **Global admin** or a **OneDrive/SharePoint admin** on the Microsoft 365 tenant where you want to migrate your content. |
|Access to the source|Windows credentials that have read access to any of the network file shares you plan to migrate. |

>[!Note]
>When using Migration Manager to migrate content to non-English SharePoint sites, make sure the site title does not include non-English characters.


## User Onboarding

Develop a plan to prepare your users for the upcoming change. Consideration factors to include in your plan:

- **Evangelize the move**. Underscore the benefits, the collaborative capabilities, and the reasons for making the move.
- **End user training**.  Provide training to your users on the features in OneDrive.
- **Train your helpdesk**.  Before the cut-over event, train your helpdesk in key features and common user questions.
- **Prepare for any possible downtime**. Plan for possible downtime during the migration.

Develop a plan for sending communications to your user base, providing clear statements of timing, and expectations and impact to the individual, including:

- The migration timeline and how it will impact them. Include any user calls to action.
- Assure them that if they already have content in OneDrive, their content is safe and won't be overwritten.
- Let them know whether individuals can opt out of the migration process.

### Onboarding related resources

- [Microsoft 365 end user adoption guide](/office365/customlearning/champ_o365guide): Outlining methodology and resources for implementing proven adoption success factors
- [Engage your org](https://adoption.microsoft.com/sharepoint/#engage): Customizable templates to generate internal awareness and excitement
- [OneDrive](https://support.office.com/article/1f608184-b7e6-43ca-8753-2ff679203132) and [team library](https://support.office.com/article/551e190a-8fbe-47ae-a88a-798b443c46b1): Video training
- [OneDrive](https://support.office.com/article/a1397e56-61ec-4ed2-9dac-727bf8ac3357) and [team library](https://support.office.com/article/324a89ec-e77b-4475-b64a-13a0c14c45ec): Quick start training guides; get up and running quickly with the basic info you need to be productive right away
- [SharePoint video training](https://support.office.com/article/cb8ef501-84db-4427-ac77-ec2009fb8e23)
- [Work together with OneDrive](https://support.office.com/article/626cff9f-9a56-472b-a77d-b019d97eec8d)
- [Learn more about OneDrive](https://support.office.com/article/38acc14b-fd86-466e-b802-baece8107c86)

## [Step 1: Set up Migration Manager agents](mm-setup-clients.md)
