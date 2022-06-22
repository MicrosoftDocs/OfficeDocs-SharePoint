---
title: 
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
description: 
---

# 

	migration requirements gathering
	Systems integration that needs to be migrated

## Migrating data

A key task in deploying OneDrive for your organization is a plan to migrate your users existing files to OneDrive. Depending on where these files are kept, there are several options, discussed below. You can choose one or more of these options depending on the number and location of files that you need to migrate.

Another planning consideration is who will be migrating the data. Normally, a user's OneDrive is created the first time they access OneDrive. If you will be migrating your users' files on their behalf before they begin using OneDrive, you may need to pre-provision OneDrive for each of them. (This can be done with a PowerShell script.)

Keep in mind that any of the migration options listed below may result in a surge of network activity as large numbers of files are migrated to OneDrive.

Key decisions:

- Which of the following migration methods do you want to use?

- Are you configuring hybrid OneDrive? (See the hybrid section of this article for the considerations around this option.)

- Do you need to pre-provision OneDrive for your users? (Are you migrating files before users have started using OneDrive?)

### Files in on-premises OneDrive or MySites libraries

If users' existing files are in on-premises SharePoint, OneDrive, or MySites, you can use the SharePoint Migration Tool to migrate the files to Microsoft 365. For info, see [Overview of the SharePoint Migration Tool (SPMT)](/sharepointmigration/introducing-the-sharepoint-migration-tool).

The SharePoint Migration Tool can be used by your IT department to migrate files for users. This is the recommended method of migration for files in an on-premises SharePoint farm.

### Files on users' local known folders

If user files are located in Windows known folders such as their Desktop, Documents, or Pictures folders, you can use Known Folder Move to move and redirect these locations. You can enable this feature during the initial rollout of OneDrive or sometime later. For more info, see [Redirect and move Windows known folders to OneDrive](redirect-known-folders.md).

### Files in other local disk folders

If users have other work files in various locations on their computers, it's often easiest for them to manually move the files to OneDrive. After you deploy the OneDrive sync app to your users' computers, you can instruct them to move their work files to the OneDrive folder on their computer.

### Files in file shares or other cloud providers

You can use Migration Manager to migrate these files to OneDrive. [Migrate files shares to Microsoft 365 with Migration Manager](/sharepointmigration/mm-get-started)

[Migrate your content to Microsoft 365](/sharepointmigration/migrate-to-sharepoint-online)

You can:
- [Migrate from file shares](/sharepointmigration/mm-get-started)
- [Migrate from Box](/sharepointmigration/mm-box-overview)
- [Migrate from Google Workspace](/sharepointmigration/mm-google-overview)
- [Migrate from Dropbox](/sharepointmigration/mm-dropbox-overview)
- [Migrate from Egnyte](/sharepointmigration/mm-egnyte-overview)
- [Migrate SharePoint Server sites and content](/sharepointmigration/introducing-the-sharepoint-migration-tool)
- [Migrate SharePoint Server workflows](/sharepointmigration/spmt-workflow-overview)

