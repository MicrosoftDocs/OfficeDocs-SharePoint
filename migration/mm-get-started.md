---
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
localization_priority: Priority
ms.collection: 
- M365-collaboration
- SPMigration
- m365solution-migratetom365
- m365solution-scenario
ms.custom:
- seo-marvel-apr2020
search.appverid: MET150
description: "Learn about how the Migration Manager tool in the modern SharePoint Admin Center works and how to get started with it."
---

# Overview:  Migrate your file shares to Microsoft 365 with Migration Manager

>[!NOTE]
>Migration Manager currently supports only the migration of **file shares**.  This release does not support the migration of content from SharePoint Server.

Migrating your on-premises file share content to Microsoft 365 lets you collaborate with innovative Office apps, intelligent cloud services, and world-class security.  Migration Manager helps you get there.

With the ability to set up multiple computers as "agents", Migration Manager lets you scale your migration project as much as you need. Located in the modern SharePoint Admin Center, Migration Manager guides you through the setup of your agents and the creation of your tasks. You can specify global or task level settings, view all-up task progress, and download aggregated summary and task-level reports.

## How does it work?


![Set up migration agents](media/mm-flow-3box.png)

- **Setup migration agents.** Download and install a setup file on each computer or virtual machine you want to connect to Migration Manager.

- **Create tasks & migrate.** Create a task by entering the URL of the network file share that you want to migrate (your source) and the URL of the SharePoint site where you are migrating your content (your destination). Your tasks will be automatically assigned to the next available agent.

- **Monitor and report.** Monitor progress across all agents and access reports from one central location. 

## Get started

Go to the [Migration Manager page of the new SharePoint admin center](https://aka.ms/ODSP-MM-FS), and sign in with an account that has [admin permissions](/sharepoint/sharepoint-admin-role) for your organization.

Make sure that you have:

- **Access to the destination**: You must either be a global admin or OneDrive/SharePoint admin to the Microsoft 365 tenant where you want to migrate your content. 

- **Access to the source**: Windows credentials that have read access to any of the network file shares you plan to migrate.

- **Prerequisites installed:** Make sure your computer or VM has the necessary prerequisites installed:  See here for the [List of prerequisites](mm-setup-clients.md).

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
- [Posters, email templates](https://support.microsoft.com/office/create-and-use-site-templates-in-sharepoint-server-versions-60371b0f-00e0-4c49-a844-34759ebdd989): Customizable templates to generate internal awareness and excitement.
- [OneDrive](https://support.office.com/article/1f608184-b7e6-43ca-8753-2ff679203132) and [team library](https://support.office.com/article/551e190a-8fbe-47ae-a88a-798b443c46b1): Video training
- [OneDrive](https://support.office.com/article/a1397e56-61ec-4ed2-9dac-727bf8ac3357) and [team library](https://support.office.com/article/324a89ec-e77b-4475-b64a-13a0c14c45ec): Quick start training guides; get up and running quickly with the basic info you need to be productive right away
- [SharePoint video training](https://support.office.com/article/cb8ef501-84db-4427-ac77-ec2009fb8e23)
- [Work together with OneDrive](https://support.office.com/article/626cff9f-9a56-472b-a77d-b019d97eec8d)
- [Learn more about OneDrive](https://support.office.com/article/38acc14b-fd86-466e-b802-baece8107c86)

### Related links

[How to set up agents in Migration Manager](mm-setup-clients.md)</br>
[Migration Manager settings](mm-settings.md)</br>
[How to format your CSV or JSON file for bulk upload into the Migration Manager](mm-bulk-upload-format-csv-json.md)</br>
[Migration Manager FAQs](mm-faqs.md)</br>