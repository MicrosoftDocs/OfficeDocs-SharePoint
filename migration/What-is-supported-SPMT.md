---
title: "What does SPMT support?"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
localization_priority: Priority
ms.collection: 
- IT_Sharepoint_Server_Top
- SPMigration
- M365-collaboration
ms.custom:
- seo-marvel-apr2020
- seo-marvel-jun2020
description: In this article, learn about the supported features and locations of the SharePoint Migration Tool (SPMT).
---

# SPMT supported features


## Features
The SharePoint Migration Tool (SPMT) supports the migration of the following locations and features:

**On-premises fileshares**
- Local and network fileshares

**SharePoint Server 2010 & 2013**

|**Supported**|**Description**|**Additional info**|
|:-----|:-----|:-----|
|File, folder, list items|Supports migration of files, folders and lists.|[Supported list templates](sharepoint-migration-supported-list-templates.md)|
|Permissions|Separate settings are available to set file share permissions and the SharePoint on-premises permissions. |[File & Folder Permissions](understanding-permissions-when-migrating.md)|
|Versions|We will preserve your file history, as determined by you.|[SPMT Settings](spmt-settings.md)|
|Managed Metadata & Taxonomy|SPMT supports the migration of content types and term stores. Global term store migration requires global tenant admin permissions.||
|Navigation & icons|Site navigation for out of box sites is preserved and migrated||
|Site features|We support an extensive number of site features|[SPMT supported SharePoint site features](spmt-supported-site-features.md)|
|SharePoint web parts|SPMT supports the migration of SharePoint web parts| [Full list of SPMT supported SharePoint web parts](spmt-supported-webparts.md)|
|Site migration|SharePoint sites that are "out of the box"; sites that do not use any coding or 3rd party tools can be migrated||
|Site description|Site descriptions can be migrated||
|Incremental|Tasks can also be saved to be rerun at a later date, allowing you to move only those new or updated files in the source location.||
|Pages|Pages in the site asset library||
|Microsoft Teams|Users can select Teams and channels directly from the destination selection page.||
|Taxonomy migration|By default, managed metadata migration is turned off, and taxonomy is updated in incremental rounds.||

> [!Note]
> Do you have a suggestion or feature request to improve the SPMT? Share it with us at [User Voice](https://sharepoint.uservoice.com/forums/282887-sharepoint-hybrid-or-migration-to-office365)

> [!Note]
> For a detailed list of features available in each release of SPMT, please read [Release Notes: SharePoint Migration Tool (SPMT)](new-and-improved-features-in-the-sharepoint-migration-tool.md)
