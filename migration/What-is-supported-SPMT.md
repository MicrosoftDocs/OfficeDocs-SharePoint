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

# What features does SPMT support?


## Features
The SharePoint Migration Tool (SPMT) supports the migration of the following locations and features:

**On-premises fileshares**
- Local and network fileshares

**SharePoint Server 2013**
- File, folder, list items:  [Supported list templates](sharepoint-migration-supported-list-templates.md)
- Permissions:  [Permissions](understanding-permissions-when-migrating.md)
- Versions:  We will preserve your file history, as determined by you. To learn more: [SPMT Settings](spmt-settings.md)
- Metadata & Taxonomy:  SPMT supports the migration of content types and term stores. Global term store migration requires global tenant admin permissions.
- Sites structure: 
- Navigation:  Site navigation for out of box sites is preserved and migrated
- Site features
- SharePoint web parts [(see supported list here)](spmt-supported-webparts.md) 
- "Out of the Box" SharePoint sites - sites that do not use any coding or 3rd party tools **
- Navigation and icons **
- Site description ** 
- Incremental:  Tasks can also be saved to be rerun at a later date, allowing you to move only those new or updated files in the source location. 

- Pages, including any pages in site asset library 
- Managed metadata, including content types and term stores. Migration of global term store requires Global Tenant Admin permissions.
