---
title: "What does SPMT support?"
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Priority
ms.collection: 
- IT_Sharepoint_Server_Top
- Strat_SP_gtc
- SPMigration
- M365-collaboration
description: "List of features that are supported in the SharePoint Migration Tool (SPMT)"
---

# SPMT supported features


## Features
The SharePoint Migration Tool (SPMT) supports the migration of the following locations and features:

**On-premises fileshares**
- Local and network fileshares

**SharePoint Server 2010 & 2013**

|**Supported**|**Description**|**Additional info**|
|:-----|:-----|:-----|
|File, folder, list items||[Supported list templates](sharepoint-migration-supported-list-templates.md)|
|Permissions||[File & Folder Permissions](understanding-permissions-when-migrating.md)|
|Versions|We will preserve your file history, as determined by you.|[SPMT Settings](spmt-settings.md)|
|Managed Metadata & Taxonomy|SPMT supports the migration of content types and term stores. Global term store migration requires global tenant admin permissions.||
|Navigation & icons|Site navigation for out of box sites is preserved and migrated||
|Site features|We support an extensive number of site features|[SPMT supported SharePoint site features](spmt-supported-site-features.md)|
|SharePoint web parts|SPMT supports the migration of SharePoint webparts| [Full list of SPMT Supported SharePoint Webparts](spmt-supported-webparts.md)|
|Site migration|SharePoint sites that are "out of the box"; sites that do not use any coding or 3rd party tools can be migrated||
|Site description|Site descriptions can be migrated||
|Incremental|Tasks can also be saved to be rerun at a later date, allowing you to move only those new or updated files in the source location.||
|Pages|Pages in the site asset library||


> [!Note]
> Do you have a suggestion or feature request to improve the SPMT? Share it with us at [User Voice](https://sharepoint.uservoice.com/forums/282887-sharepoint-hybrid-or-migration-to-office365)