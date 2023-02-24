---
title: "Migration Manager and the European Union database (EUDB)"
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
search.appverid: MET150
description: Learn about the changes to Migration Manager for the European Union and how data is processed.
---

# Migration Manager and the European Union Data Boundary (EUDB)

>[!Important]
>Beginning April 1, 2023, all new European Union (EU) scans and migrations, except for Stream, will be processed in the EU. 
>You may continue to run existing migrations until September 30, 2023. Starting October 1, 2023, you will no longer have access to migration projects created in the United States (US).
>
>Stream migrations created before April 1, 2023 may continue to run in the US project until February 15, 2024.

The Migration Manager Platform (MMP) is the platform for the Migration Manager migration tool that enables migrations from file share and cloud storage platform sources to Microsoft 365. 

The European Union Data Boundary (EUDB) is a geographically defined boundary within which Microsoft has committed to store and process customer data for our major commercial enterprise online services, including Azure, Dynamics 365, Power Platform, and Microsoft 365, subject to limited circumstances where customer data will continue to be transferred outside the EU Data Boundary.

MMP currently has one instance based in the United States (US) farm, serving all global migration traffic. A second instance based in the European Union (EU) will be available starting April 1, 2023 with a phased implementation schedule for existing customers with active migration projects.


## Timeline overview

|Date|Change|
|:-----|:-----|
|April 1, 2023|The Scans tab becomes read only.|
|April 1, 2023|All new migrations will be processed in the EU. All existing migration projects will automatically be recreated in the EU instance.  Users can choose to restart their projects in the EU project or continue with their migration in the US project.|
|September 30, 2023|All existing migrations in the US instance must be completed.|
|October 1, 2023|EU users no longer can access scans or cloud migration projects initiated in the US instance.|
|February 15, 2024|Stream migrations must be completed. Migrations will be removed after this date.| 

## What does that mean for me?


|If you have...|Impact to you|Recommendation|
|:-----|:-----|:-----|
|Have no existing migrations|None|No action required.||
|Have active migrations|If you're an EU customer with active migrations in the US instance, you have a choice. Continue to complete your migration projects in the US instance, or restart them in the EU instance.  We've recreated any existing migration projects in the EU, if you need to run them there. You'll have until September 30, 2023 to complete active migrations. After October 1, 2023, you'll no longer have access to US migrations or the reports that were generated.  An "active project" must have been run in the last 90 days. |We recommend completing any existing US initiated migrations in the US.|
|An active file share migration|You can access any existing US scan reports until April 1, 2023 after which the become read only.|Create new scans starting April 1, 2023 |
|File share scans|File share scans will be until April 1, 2023, when they change to read only. |
|An active Stream migration|Stream migrations created before April 1, 2023 may continue to run in the US project until February 15, 2024. After that date, the migrations will be removed. |Complete your Stream migration before February 15, 2024.|