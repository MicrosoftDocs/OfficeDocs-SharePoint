---
title: "Managed migration process guide for use with Mover"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: serdars
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
localization_priority: Priority
ms.collection: 
- SPMigration
- M365-collaboration
ms.custom:
- seo-marvel-apr2020
search.appverid: MET150
description: A guide to help partners managing a customers migration project.
---
# Managed migration guide for use with Microsoft Mover 

This guide was created to share the process and best practices of managing a cloud to cloud migration project using the Microsoft Mover application. 

Most migrations fall into regular phases. Proven success factors for migration include planning, assessing and remediating, preparing your destination environment, migrating, and onboarding your users.


> [!NOTE]
> The Mover Migration tool is a Microsoft owned migration tool available at no cost to subscribers of Microsoft 365.


>[!Tip]
>We highly recommend reading and reviewing the current Mover documentation. This content provides valuable knowledge on how to understand the Mover tool for running migrations from various cloud storage platforms.
> See [Mover migration content](https://docs.microsoft.com/en-us/sharepointmigration/mover-plan-migration)


## Planning
Before beginning your migration, it is important that you plan your outcome by performing an assessment of your current source environment. What you discover will influence your overall strategy and timing, including:

- The design of the target environment and the mapping between source and destination.
- The amount of content you migrate. Determine if content is redundant, out of date, or still relevant.
- Understand the scope of your project, any time restrictions, or deadlines
- Build your user onboarding into your upfront planning. Communicate early and often with your users about the migration and how it will impact them. Don't wait until the very end to start preparing them for the change.

### Scope and timeline
The most common question from customers is “How long will the migration take?”. While the Mover app is one of the fastest ways to migrate data, the migration speed can be impacted by many factors, including: 

- Number of files and folders being moved
- File size 
- Total amount of data being moved
- Server connections with the source or destination
- Both Source and destination connectors have rate limits and we  constrained to to how fast they allow us to download, upload and process data between the two.
- Complexity of permissions or sharing of data:  Applying permissions as part of the migration is another factor that can influence speed.  To apply permissions we are again making numerous API calls which will increase the time it takes to migrate the data.

Mapping out timelines and setting expectations of what can be achieved with those timelines is essential to managing a successful migration project.

Usually, the more time you have to complete the project the smoother the migration will be. One of the benefits of migrating via the Mover app is that we only take a copy of the source data and upload that to the Destination. This allows the users to continue to work in their source files while we copy their data for them, allowing the migration to run in parallel with minimal distribution of the customers' daily activities.

The only time users need to refrain from creating new content is during the final delta.


### Communication

A migration is a significant undertaking for any customer. Trying to grasp the entire extent of all data and communicating with the users within the organization is complicated.

Before, during, and after a migration, it is critical to communicate clearly and effectively with your user base. 

**Management** — Management needs succinct information about the how’s and why’s of the migration, including the benefits, and expectations. Clearly communicate what a successful migration looks like 

**Users** — They need to know when changes are taking place and who to go to with questions or issues, and in turn whoever we are working with for that customer we will be available to provide answers to those questions when they occur.

**IT Helpdesk/Support staff** — If your organization is large enough to have specific support staff for other employees, they must understand each step of the migration and how to help troubleshoot many of the questions that might arise.


## Assess and remediate

Before beginning your migration, it is important that you perform an analysis of your current environment. Only you know your data and how and who uses it. 

### Inventory scan

You or your customer might have a relative idea of how many users are in their source domain and how many they might want to migrate. However, it is important to get an accurate count of the user base by running an **Inventory Scan.**  This scan will let you know how many users are in the domain and help determine who owns the data. To learn more, see [Running a migration inventory scan with Mover.](mover-scan.md) 

Your scan will help you assess who will be included, the timeline, :

| |**Assess**|**Remediate**|
|:-----|:-----|:-----|
|**Data ownership**|How many users are in the domain and who owns the data|Most data will be shared data.  Only owned folders and the root files for each user is copied. If a user is not the owner of the data, is is not copied. Content can be automatically re-shared after it is migrated so that each user has access to their content exactly as before. |
|**Data distribution**|Find all accounts that exceed 5TB or 400,000 files or items.|Split these accounts into into smaller service accounts. **We highly recommend that users with very large data sets be broken into smaller accounts to facilitate faster transfers.**|
|**File and folder path length**|Find all items in the *Folders and Files* report whose Path exceeds the file path length described here: [SharePoint limits](/office365/servicedescriptions/sharepoint-online-service-description/sharepoint-online-limits)|Work with your migration vendor to reorganize your file and folder structure such that it does not exceed this limit. Splitting large drives that serve several scenarios into multiple smaller, more focused drives may help here.|
|**Size and amount of files/data** |Get an accurate count of the number of files and the size.|This number will be the most accurate, as it will not included items in the trash, or externally shared data.  Do not rely on your cloud provider's reporting to give you an accurate picture.  Use this information to more clearly define migration timeline and length of time required for the migration.|

 
>[Important]
>The Mover app only copies files/folders/data owned by users within the source tenant.  Mover does NOT migrate external shared data, email or items residing in the trash.


## Prepare your environment

We recommend the following best practices as you prepare your environment.

|What|Action notes|
|:------|:-----|
|**Source connector factors**|Each source has a specific process and caveats to be aware of when authoring and creating your connector. Learn more about your source connector here: [Setup your source](https://docs.microsoft.com/sharepointmigration/mover-box) |
|**Account setup** |This ensures that only those running the migration have control of the migration.  This ensures that there is a designated team that is running, monitoring and maintaining the migration. |
|**Disable mail notifications**|Disable all migration notification emails to avoid getting spammed.  Otherwise, you and your customers will receive test emails regarding transfers, failures, progress, etc.|
|**Destination upload folder**|Map an upload/destination folder for uploading the migrated data.|


## Migrate process

Below is a typical migration process that follows Microsoft's best practices guidance.

1. Select a small set of users for a pilot migration. The goal of the pilot is to validate the process, including performance, user communication, and to get a sample of user feedback.

2. Perform the pilot migration. This should use an incremental migration method, in which migration happens in the background with no user impact, followed by a cutover event in which network file shares and local file shares are disabled and they are directed to use the Microsoft 365 environment. This method is preferred as it reduces user impact.

3. Understand the data from the pilot migration to determine the remainder of your migration schedule and make any changes. For example, you may update your user communication template to address a question you received from a pilot user.

4. Perform the remainder of the migration. This should also follow an incremental migration method, just like the pilot. Microsoft recommends a single cutover event for all users to switch to using their OneDrive accounts and SharePoint sites. This helps eliminate users from updating duplicate copies of content.

5. Provide regular (daily) reporting to key stakeholders with a migration report that captures all transfers and their current status.




## User Onboarding

Develop a plan to prepare your users for the upcoming change. Consideration factors to include in your plan:
- **Evangelize the move.** Underscore the benefits, the collaborative capabilities, and the reasons for making the move.
- **End user training.**  Provide training to your users on the features in OneDrive.
- **Train your helpdesk.**  Before the cutover, train your helpdesk in key features and common user questions.
- **Prepare for any possible downtime** the migration may incur.

Develop a plan for sending communications to your user base, providing clear statements of timing, and expectations and impact to the individual, including:
- The migration timeline and how it will impact them. Include any user calls to action.
- Assure them that their content is safe and won't be overwritten.
- Let them know whether individuals can opt out of the migration process.

### Onboarding related resources

- [Microsoft 365 end user adoption guide](https://docs.microsoft.com/office365/customlearning/champ_o365guide): Outlining methodology and resources for implementing proven adoption success factors
- [Posters, email templates](https://fasttrack.microsoft.com/office365/resourcehub): customizable templates to generate internal awareness and excitement
- [OneDrive](https://support.office.com/article/1f608184-b7e6-43ca-8753-2ff679203132) and [team library](https://support.office.com/article/551e190a-8fbe-47ae-a88a-798b443c46b1) video training
- [OneDrive](https://support.office.com/article/a1397e56-61ec-4ed2-9dac-727bf8ac3357) and [team library](https://support.office.com/article/324a89ec-e77b-4475-b64a-13a0c14c45ec) Quick start training guides: get up and running quickly with the basic info you need to be productive right away
- [SharePoint video training](https://support.office.com/article/cb8ef501-84db-4427-ac77-ec2009fb8e23)







