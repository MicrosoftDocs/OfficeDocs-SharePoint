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

Most migrations fall into regular phases as follows. Proven success factors for migration include planning, assessing and remediating, preparing your target environment, migrating, and onboarding your users.



> [!NOTE]
> The Mover Migration tool is a Microsoft owned migration tool available at no cost to subscribers of Microsoft 365.


>[!Tip]
>Before starting a managed migration, we highly recommend reading and reviewing the current Mover documentation. This content provides valuable knowledge on how to understand the Mover tool for running migrations from various cloud storage platforms.
> See [Mover migration content](https://docs.microsoft.com/en-us/sharepointmigration/mover-plan-migration)


## Planning
Before beginning your migration, it is important that you plan your outcome by performing an assessment of your current source environment. What you discover will influence your overall strategy and timing, including:

•	The design of the target environment and the mapping between source and destination.
•	The amount of content you migrate. Determine if content is redundant, out of date, or still relevant.
•	Understand the scope of your project, any time restrictions, or deadlines
•	Build your user onboarding into your upfront planning. Communicate early and often with your users about the migration and how it will impact them. Don't wait until the very end to start preparing them for the change.

### Scope and timeline
The most common question from customers is “how long will the migration take?.”  This is something that is hard to provide an accurate answer to. While the Mover app is one of the fastest ways to migrate data, the speed of the migration may still be affected by bottlenecks.  These include, but aren’t limited to:

•	Number of files and folders being moved.
•	File size 
•	Total amount of data being moved
•	Server connections with the source or destination
•	Both Source and Destination connectors have rate limits and we  constrained to to how fast they allow us to download, upload and process data between the two.
•	Complexity of permissions or sharing of data
•	Applying permissions as part of the migration is another factor that can influence speed.  To apply permissions we are again making numerous API calls which will increase the time it takes to migrate the data.


## Assess and remediate

Before beginning your migration, it is important that you perform an analysis of your current environment. Only you know your data and how and who uses it. 

You or your customer might have a relative idea of how many users are in their source domain and how many they might want to migrate. However, it is important to get an accurate count of the user base by running an Inventory Scan.  This lest you know not only how many users are in the domain but also help determine who owns the data. 


| |**Assess**|**Remediate**|
|:-----|:-----|:-----|
|**Data ownership**|Find all files in the Folders and Files report whose Path ends in one of the extensions defined here: [Types of files that cannot be added to a list or library](https://support.office.com/article/30BE234D-E551-4C2A-8DE8-F8546FFBF5B3)|Within most customers user base, much of the data will be shared data.  When using the Mover for migrating only owned folders and the root files for each user is copied. If a user is not the owner of the data, we do not copy it.  Content can be automatically re-shared after it is migrated so that each user has access to their content exactly as before.

We also use the Inventory Scan to help determine who owns what. |
|**Data distribution**|Find all accounts that exceed 5TB or 400,000 files or items.|Split these accounts into into smaller service accounts|
|**File and folder path length**|Find all items in the *Folders and Files* report whose Path exceeds the file path length described here: [SharePoint limits](/office365/servicedescriptions/sharepoint-online-service-description/sharepoint-online-limits)|Work with your migration vendor to reorganize your file and folder structure such that it does not exceed this limit. Splitting large drives that serve several scenarios into multiple smaller, more focused drives may help here.|



Size Amount of files/data to Migrate ando how its distrbuted

Run an inventory scan. The number of files/data to migrate ties in closely with how the data is distributed.  Customers may have an idea of many files or how much data they have in their Source.  But some of the cloud storage providers' reporting on the exact numbers can be misleading, as some may count items in the trash and/or external shared data.
To obtain accurate totals for files/data owned then carrying out the Inventory Scan is essential.

It should be noted that Mover app only copies files/folders/data owned by users within the Source tenant.  The Tool does NOT migrate External Shared data, Email or items residing in the trash.


## Prepare your environment



## Migrate

### Process

Below is a typical migration process that follows Microsoft's best practices guidance.

1. Select a small set of users for a pilot migration. The goal of the pilot is to validate the process, including performance, user communication, and to get a sample of user feedback.</br></br>
2. Perform the pilot migration. This should use an incremental migration method, in which migration happens in the background with no user impact, followed by a cutover event in which network file shares and local file shares are disabled and they are directed to use the Microsoft 365 environment. This method is preferred as it reduces user impact.
3. Understand the data from the pilot migration to determine the remainder of your migration schedule and make any changes. For example, you may update your user communication template to address a question you received from a pilot user.
4. Perform the remainder of the migration. This should also follow an incremental migration method, just like the pilot. Microsoft recommends a single cutover event for all users to switch to using their OneDrive accounts and SharePoint sites. This helps eliminate users from updating duplicate copies of content.



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







