---
title: Mover retirement timeline
author: JoanneHendrickson
ms.author: jhendr
manager: serdars
recommendations: true
audience: ITPro
ms.topic: article
ms.service: sharepoint-online
ms.subservice: sharepoint-migration
ms.localizationpriority: high
ms.collection:
- SPMigration
- M365-collaboration
search.appverid: MET150
description: "Mover retirement timeline"
---
# Mover.io retirement timeline

>[!Important]
>**Attention businesses or those with EDU plans**: We will soon be retiring the legacy [Mover](https://app.mover.io) tool's ability to migrate from [Google Drive](mm-google-overview.md), [Dropbox](mm-dropbox-overview.md), [Box](mm-box-overview.md), and [Egnyte](mm-egnyte-overview.md). Please use [Migration Manager](https://aka.ms/ODSP-MM), located in the SharePoint admin center, going forward.
>
>If you are currently in the middle of a Mover migration, you may continue using Mover until you finish your migration. However, you will not be able to create new connectors.  FastTrack led migrations are not impacted at this time.
>
>[**Individuals or students**: You may continue to use Mover. Learn how!](https://support.microsoft.com/office/7dbda93c-71e6-483f-8914-ad445554cd31?OCID=Docs_MigrateContent_IndStudentLink)


Mover's cloud migration scenarios are fully available in Migration Manager and have set the timeline to retire Mover. Unifying the migration experience within Migration Manager simplifies the tool decision for you and allows us to focus our development and support resources to help you meet your migration goals.

|Date|What|
|:-----|:-----|
|July 1, 2022|You'll no longer be able to create **new** Mover connectors to Box admin or Dropbox admin. Google Drive admin and Egnyte admin connectors were disabled earlier this year.|
|Q4 2022|You'll no longer be able to create **new** Azure Blob Storage or **new** Amazon S3 connectors.| 
|TBA|Migrations between two Microsoft 365 tenants will be no longer supported.|
|TBA|Individual and end-user migrations will no longer be supported.|


## FAQs

**Question:**  Why are we retiring Mover.io?</br>
**Answer:**    Mover's cloud migration functionality is now fully integrated into Migration Manager, Microsoft'ts recommended tool for file migrations. This simplifies the experience for you and helps us support you more effectively.

**Question:** Why are we starting the retirement now?</br>
**Answer:**   Until now, we have been integrating the Mover’s cloud migration functionality into Migration Manager. Migration Manager now offers the full functionality of Mover along with an improved experience within the Microsoft admin center. 


**Question:**  Will my current Mover migrations stop working?</br>
**Answer:**    No. Microsoft is retiring the ability to create **new** connectors. Existing migrations will continue to operate on Mover. However, we recommend transitioning your migrations to Migration Manager at your earliest convenience to ensure to get the latest migration tooling. 

**Question:**  I'm migrating using Mover. If my existing connector gets disconnected, can I still reauthorize it to continue?</br>
**Answer:**    Yes. You can reauthorize an existing connector assuming the existing connector was operational before the retirement. 

**Question:** Will individual or consumer migrations continue to work on Mover?</br>
**Answer:**   We'll continue to support individual, consumer, or student migrations from Mover for some time. Refer back to this page for updates on these migration scenarios. 



