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

The Migration Manager Platform (MMP) is the platform for migration tools to SharePoint Online. It enables migrations from cloud storage platform sources to Microsoft 365. 

The European Union Data Boundary (EUDB) is a geographically defined boundary within which Microsoft has committed to store and process customer data for our major commercial enterprise online services, including Azure, Dynamics 365, Power Platform, and Microsoft 365, subject to limited circumstances where customer data will continue to be transferred outside the EU Data Boundary.

As part of Microsoft 365, MMP is mandated to be covered by the EUDB promise. Due to the complexity of the migration business, and the architecture of MMP, the original deadline of Dec 31, 2022 has been extended to Mar 23, 2023.
 
Before the EUDB initiative, MMP has had one instance based in the United States (US) farm, serving all global migration traffic. A second instance based in the European Union (EU) will be available starting April 1, 2023 with a phased implementation schedule for existing customers with active migration projects.



## Timeline for EU 

|Date|Change|
|:-----|:-----|
|February 24, 2023|Announcement made regarding EU Data Boundary changes|
|April 1, 2023|New migration projects will initiate and be processed in the EU. All existing migration projects will automatically be recreated in the the EU instance.  Users can choose to restart their projects in the EU instance or continue with their migration in the US instance.|
|October 31, 2023|EU users no longer can access file share scans and cloud migration projects initiated in the US instance.|
|December 31, 2023|All existing migrations in the US instance must be completed.|
|June 1, 2024|Access to Stream migrations in the US instance expire.|

## What does that mean for me?

|If you are...|Impact|Recommendation|
|:-----|:-----|:-----|
|An EU customer, no existing migrations|No impact to you|No action required.|
|An EU customer with active migrations|If you are an EU customer with active migrations in the US instance, you have a choice. Continue to complete your migration projects in the US instance, or restart them in the EU instance.  We have recreated any existing migration projects in the EU, if you need to run them there. You will have until December 31, 2023 to complete active migrations.  However, starting January 1, 2024, you will no longer have access to projects process in the US or the reports that were generated.  An "active project" must have been run in the last 90 days. |We recommend completing any existing US initiated migrations in the US.|
|An EU customer with an active Stream migration|You have until May 301 2024 to access your US initiated Stream migration.  After that date, the migrations will be removed.|
