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

As part of Microsoft 365, MMP is mandated to be covered by the EUDB promise. This is due to the complexity of the migration business, and the architecture of MMP, the original deadline of Dec 31, 2022 has been extended to Mar 23, 2023.
 
Before the EUDB initiative, MMP has had 1 instance based in the US farm, serving all global migration traffic.


## Terms 
- Migration: the business supported by the MMP product and refers to the migration of customer data from external platforms to Microsoft 365.
- Move: the actual transfer of data from the US region to EU region.
- Migration data: the data (e.g., files) customers migrated from external platforms to Microsoft 365. 
- MMP only store Customer data for a very short period, no longer than 24 hours.
- Application data: 
- Task definitions: the user-created definitions of migration jobs. 
- Transient data: logs, reports and other data generated at the runtime of the application.
- Transient data has a retention window of 90 days.
Transition plan


## Timeline

|Customer|Description|Deadline|
|:-----|:-----|:-----|
|EU-N:| brand new EU customers who don’t have a single EU migration||
|EU-A: |EU customers with active migrations aka - migration task run in the last 90 days||
|EU-AP:| Pilot EU-A customers. Criteria: 10-20 customers who have active migrations. ||Hand pick tenants based on size and ensuring we are including all scenarios – FS, Google, Dropbox, Box, Egnyte and Stream. ||
|EU-E:| EU customers with expired migrations aka – zero migration tasks run in the last 90 days||
