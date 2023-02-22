---
ms.date: 05/16/2019
title: "What does SPMT support?"
audience: ITPro
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: serdars
recommendations: true
ms.audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.subservice: sharepoint-migration
ms.localizationpriority: high
ms.collection: 
- IT_Sharepoint_Server_Top
- SPMigration
- M365-collaboration
ms.custom:
- seo-marvel-apr2020
description: "This article contains a list of features that are supported in the SharePoint Migration Tool (SPMT)."
---

# SPMT-supported features


## Features
SharePoint Migration Tool (SPMT) supports migration of the following locations and features:

**On-premises fileshares**
- Local and network fileshares

**SharePoint Server 2010, 2013, and 2016**

| Supported | Description | More info |
|:-----|:-----|:-----|
|File, folder, list items|Supports migration of files, folders, and lists.|[Supported list templates](sharepoint-migration-supported-list-templates.md)|
|Permissions|Separate settings are available to set file share permissions and SharePoint on-premises permissions. |[File and folder permissions](understanding-permissions-when-migrating.md)|
|Versions|You determine what file history is preserved.|[SPMT settings](spmt-settings.md)|
|Managed metadata and taxonomy|SPMT supports the migration of content types and term stores. Global term store migration requires global tenant admin permissions.||
|Navigation and icons|Site navigation for out-of-box sites is preserved and migrated.||
|Site features|An extensive set of site features are supported.|[SPMT-supported SharePoint site features](spmt-supported-site-features.md)|
|SharePoint web parts|SPMT supports migration of SharePoint web parts.| [SPMT-supported SharePoint web parts](spmt-supported-webparts.md)|
|Site migration|"Out-of-the-box" SharePoint sites that don't use any coding or third-party tools can be migrated.||
|Site description|Site descriptions can be migrated.||
|Incremental|Tasks can also be saved to rerun at a later date, allowing you to move only those new or updated files in the source location.||
|Pages|Pages in the site asset library.||
|Microsoft Teams|Users can select Teams and channels directly from the destination selection page.||
|Taxonomy migration|By default, managed metadata migration is turned off, and taxonomy is updated in incremental rounds.||

> [!Note]
> Do you have a suggestion or feature request to improve the SPMT? Share it with us at [Migration Feedback](https://feedbackportal.microsoft.com/feedback/forum/06735c62-321c-ec11-b6e7-0022481f8472).

> [!Note]
> For a detailed list of features available in each release of SPMT, please read [Release Notes: SharePoint Migration Tool (SPMT)](new-and-improved-features-in-the-sharepoint-migration-tool.md).

