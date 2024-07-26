---
title: "Permission settings in Migration Manager"
ms.date: 11/15/2023
ms.reviewer: 
ms.author: heidip
author: MicrosoftHeidi
manager: jtremper
recommendations: true
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: microsoft-365-migration
ms.localizationpriority: high
ms.collection: 
- M365-collaboration
- SPMigration
- m365initiative-migratetom365
search.appverid: MET150
description: Learn about configuring project permissions in Migration Manager.
---
# Permission settings in Migration Manager

Review your settings to ensure that the same users with access to files, folders, and metadata will continue to have access after migration.

## Migrate permissions
By default, Migration Manager migrates folders permissions.  File permissions aren't migrated, and destination files inherit parent folder permissions.

File permissions migration can be enabled by Project settings:
 
:::image type="content" source="media/mm-project-settings-toolbar.png" alt-text="project settings":::

Once enabled, the destination file permissions will be the same as they are in source.  This ensures that migrated files are shared with the same users as before migration.  

> [!Note]
> - Migrating file permissions may slow down your migration process.
> - While permissions are migrated, 'Share With Me' information in OneDrive can't be surfaced for now. 
## Map identities

Identity Mapping is when you match the user and group identities that have access to your source environment and map those identities to Microsoft 365 user and group identities. This process is important to migration. If identities aren't properly set up prior to migration, it can result in users losing access to content. It can also result in information being incorrect at the destination.

Learn more about identity mapping for different cloud scenarios:

- [Google Drive](mm-google-step5-map-identities.md)

- [Dropbox](mm-dropbox-step5-map-identities.md)

- [Box](mm-box-step5-map-identities.md)

- [Egnyte](mm-egnyte-step5-map-identities.md)

> [!Note]
> When migrating Google shared drive permissions, we recommend you do the following:
> - Recreate a Microsoft 365 group that has the same memberships as the Google Drive group. You can either create a new group, or edit the group linked to the Team site which you designate as the migration destination of the Google shared drive.
> - In the "Map identites" setting, map the original Google Drive group of the shared Drive to the Microsoft 365 group recreated above.
