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

>[!Note]
>Attention businesses or those with EDU plans: We have retired the legacy [Mover](https://app.mover.io) tool's ability for admin-led migrations from [Google Drive](mm-google-overview.md), [Dropbox](mm-dropbox-overview.md), [Box](mm-box-overview.md), and [Egnyte](mm-egnyte-overview.md). Please use [Migration Manager](https://aka.ms/ODSP-MM), located in the SharePoint admin center.
>
>[**Individuals or students**: You may continue to use Mover, learn how!](https://support.microsoft.com/en-us/office/move-your-school-files-when-you-graduate-7dbda93c-71e6-483f-8914-ad445554cd31)


>[!Important]
>
>All FastTrack-led migrations will transition to Migration Manager except those with multi-parent folders who have reached velocity migrations. These exceptions will need to finish their migrations by December 31, 2022.

Mover's cloud migration scenarios are fully available in Migration Manager and have set the timeline to retire Mover. Unifying the migration experience within Migration Manager simplifies the tool decision for you and allows us to focus our development and support resources to help you meet your migration goals.

|Date|What|
|:-----|:-----|
|July 1, 2022|You'll no longer be able to create **new** Mover connectors to Box admin or Dropbox admin. Google Drive admin and Egnyte admin connectors were disabled earlier this year.|
|August 1, 2022|All FastTrack-led migrations will transition to Migration Manager except those with multi-parent folders who have reached velocity migrations. These exceptions will need to finish their migrations by December 31, 2022.|
|September 1, 2022|Mover email notifications will be disabled. All emails sent from the Mover.io tool will be disabled. Scans and transfers will continue to work normally.|
|October 1, 2022|You'll no longer be able to create **new** Azure Blob Storage or **new** Amazon S3 connectors.| 
|December 31, 2022|You'll no longer be able to continue **existing** Mover admin migrations from Box admin, Dropbox admin, Google Drive admin, and Egnyte. You must complete your migration or transition to Migration Manager before this date.  This also applies to all **FastTrack-led** migrations.|
|January 31, 2023|Migrations between two Microsoft 365 tenants will be no longer supported.|
|Early 2023|Individual and end-user migrations will no longer be supported.|


## FAQs

**Question:**  Why are we retiring Mover.io?</br>
**Answer:**    Mover's cloud migration functionality is now fully integrated into Migration Manager, Microsoft'ts recommended tool for file migrations. This simplifies the experience for you and helps us support you more effectively.

**Question:** Why are we starting the retirement now?</br>
**Answer:**   Until now, we have been integrating the Mover’s cloud migration functionality into Migration Manager. Migration Manager now offers the full functionality of Mover along with an improved experience within the Microsoft admin center. 


**Question:**  Will my current Mover migrations stop working?</br>
**Answer:**    No. Microsoft is retiring the ability to create **new** connectors. Existing migrations will continue to operate on Mover until December 31, 2022.  See the timeline above. 

**Question:**  I'm migrating using Mover. If my existing connector gets disconnected, can I still reauthorize it to continue?</br>
**Answer:**    Yes. You can reauthorize an existing connector until December 31, 2022.

**Question:** Will individual or consumer migrations continue to work on Mover?</br>
**Answer:**   We'll continue to support individual, consumer, or student migrations from Mover for some time. Refer back to this page for updates on these migration scenarios. 

**Question:** Is tenant-to-tenant migration supported in Migration Manager?</br>
**Answer:**  No. Microsoft will be offering a solution that will be available sometime in 2023. This will be a premium feature distinct from legacy Mover. In the interim, we recommend using a third-party solution for your Microsoft 365 tenant-to-tenant migration needs.
