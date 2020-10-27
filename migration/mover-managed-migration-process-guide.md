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


   ![Migration process](media/migrationprocess-fileshare.png)

|**Migration planning**|**Assess and remediate**|**Prepare your OneDrive and SharePoint environment**|**Migrate**|**User onboarding**|
|:-----|:-----|:-----|:-----|:-----|
|What content goes where<br><br>Understanding permissions vs sharing<br><br>What to expect before and after<br><br>Migration and network performance considerations<br><br>Change management and communications|Assess key areas<br><br>Remediate issues|Pre-provision Microsoft 365 and users|Review migration offerings<br><br>Microsoft FastTrack services<br><br>Migration service providers|Send regular emails to users<br><br>Provide training<br><br>Let users know how they are impacted|


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


## Assessment

Before beginning your migration, it is important that you perform an analysis of your current environment. Only you know your data and how and who uses it. 

You or your customer might have a relative idea of how many users are in their source domain and how many they might want to migrate. However, it is important to get an accurate count of the user base by running an Inventory Scan.  This lest you know not only how many users are in the domain but also help determine who owns the data. 

Data ownership

Within most customers userbase a lot of the data that is used will be shared data.  When using the Tool for migrating only owned folders and the root files for each user is copied.

If a user is not the owner of the data, we do not copy it.  Content can be automatically re-shared after it is migrated so that each user has access to their content exactly as before.

We also use the Inventory Scan to help determine who owns what. 

Data Distribution

Determining how a customer's data is distributed is also important. Usually in the initial discussion's customers might not have a clear picture of exactly how their data is distributed and again the Inventory Scan will aid in obtaining that information.

As a rule, if an account has over 400,000 files/items or their storage size exceeds 5 TB then we recommend that that user be split into smaller service accounts,  This impacts performance and speed.conThis aids with concurrency and speed during the Migration and will be discussed in a later topic.

Size Amount of files/data to Migrate ando how its distrbuted

Run an inventory scan. The number of files/data to migrate ties in closely with how the data is distributed.  Customers may have an idea of many files or how much data they have in their Source.  But some of the cloud storage providers' reporting on the exact numbers can be misleading, as some may count items in the trash and/or external shared data.
To obtain accurate totals for files/data owned then carrying out the Inventory Scan is essential.

It should be noted that Mover app only copies files/folders/data owned by users within the Source tenant.  The Tool does NOT migrate External Shared data, Email or items residing in the trash.



REMEDIATE
MIGRATE


CUSTOMER





