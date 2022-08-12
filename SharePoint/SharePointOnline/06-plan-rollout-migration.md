---
title: Migration planning for SharePoint and OneDrive rollout
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: serdars
recommendations: true
audience: Admin
f1.keywords: NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.localizationpriority: medium
ms.collection:  
ms.custom: intro-get-started
search.appverid: MET150
description: Plan your migration of sites and files as part of your OneDrive and SharePoint rollout.
---

# Migration planning for SharePoint and OneDrive rollout

A key task in deploying SharePoint and OneDrive for your organization is a plan to migrate your users' existing files. Depending on where these files are kept, there are several options, discussed below. You can choose one or more of these options depending on the number and location of files that you need to migrate.

The following types of data can be migrated with Microsoft tools:
- Files and folders (from on-premises or other cloud providers)
- SharePoint Server sites
- SharePoint Server 2010 workflows

Keep in mind that migrating content may result in a surge of network activity as large amounts of data is moved to SharePoint and OneDrive.

For complete information on migrating content to SharePoint and OneDrive, see [Migrate your content to Microsoft 365](/sharepointmigration/migrate-to-sharepoint-online).

#### Automation and workflows

If you have automated processes or workflows around files or other content, you may need to consider how to integrate those processes with Microsoft 365 or migrate them as well. Consider using [SharePoint Framework solutions](/sharepoint/dev/) or [Microsoft Power Platform](/power-platform).

If you have SharePoint Server 2010 workflows, you can migrate them to Power Automate by using the SharePoint Migration Tool. See [Overview: Migrate SharePoint Server 2010 workflows to Power Automate](/sharepointmigration/spmt-workflow-overview) for more information.

#### Hybrid

If you use SharePoint Server on-premises, you may want to set up a hybrid environment with SharePoint in Microsoft 365 while you migrate or as a long term solution. See [Hybrid OneDrive and SharePoint in Microsoft 365](hybrid.md)
for more information.

## Migrating users' personal work files to OneDrive

As part of your OneDrive rollout, 

Normally, a user's OneDrive is created the first time they access OneDrive. If you will be migrating your users' files on their behalf before they begin using OneDrive, you may need to pre-provision OneDrive for each of them. See [Pre-provision OneDrive for users in your organization](pre-provision-accounts.md) for details.

### Files in on-premises OneDrive or MySites libraries

If users' existing files are in on-premises SharePoint Server, OneDrive, or MySites, you can use the SharePoint Migration Tool to migrate the files to Microsoft 365. For info, see [Overview of the SharePoint Migration Tool (SPMT)](/sharepointmigration/introducing-the-sharepoint-migration-tool).

### Files on users' local known folders

If user files are located in their Windows or Mac  Desktop or Documents folders, you can use Known Folder Move to move and redirect these locations to OneDrive. You can enable this feature during the initial rollout of OneDrive or sometime later. For more info, see [Redirect and move Windows known folders to OneDrive](redirect-known-folders.md) and [Redirect and move macOS Desktop and Documents folders to OneDrive](redirect-known-folders-macos).

### Files in other local disk folders

If users have other work files in various locations on their computers, it's often easiest for them to manually move the files to OneDrive. After you deploy the OneDrive sync app to your users' computers, you can instruct them to move their work files to the OneDrive folder on their computer. For more information, see [Move files from OneDrive to OneDrive for work or school](https://support.microsoft.com/office/7fb28cad-7e25-451f-8b4b-2d1a71e5c0e9).

## Migrating sites from SharePoint Server to SharePoint in Microsoft 365

If you have sites in SharePoint Server, you can migrate them to SharePoint in Microsoft 365 by using the SharePoint Migration Tool. You can do this as part of your SharePoint and OneDrive rollout, or you can do it later. For details, see [Overview of the SharePoint Migration Tool (SPMT)](/sharepointmigration/introducing-the-sharepoint-migration-tool).

## Migrating files in file shares or hosted on other cloud providers

For files located in file shares or other cloud providers, you can use Migration Manager to migrate them to SharePoint and OneDrive. For details, see [Migrate files shares to Microsoft 365 with Migration Manager](/sharepointmigration/mm-get-started).

See these references for specific instructions on how to migrate from different locations:

- [Migrate from file shares](/sharepointmigration/mm-get-started)
- [Migrate from Box](/sharepointmigration/mm-box-overview)
- [Migrate from Google Workspace](/sharepointmigration/mm-google-overview)
- [Migrate from Dropbox](/sharepointmigration/mm-dropbox-overview)
- [Migrate from Egnyte](/sharepointmigration/mm-egnyte-overview)
- [Migrate SharePoint Server sites and content](/sharepointmigration/introducing-the-sharepoint-migration-tool)
- [Migrate SharePoint Server workflows](/sharepointmigration/spmt-workflow-overview)

