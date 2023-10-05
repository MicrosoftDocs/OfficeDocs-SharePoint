---
ms.date: 12/04/2020
title: Mover - Deleting a migration
ms.author: jhendr
author: JoanneHendrickson
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
- m365initiative-migratetom365
search.appverid: MET150
description: "How to delete a migration using the Mover migration tool."
---
# Deleting a Mover migration

>[!Important]
>**Mover is now retired for all Admin led migrations**. The ability to migrate from Google Drive, Box, Dropbox, and Egnyte has been fully integrated into Migration Manager. For full details see: [Mover retirement timeline](mover-retirement-timeline.md).  Migration Manager does not support the migration of Amazon S3 or Azure blob storage.
>
>All FastTrack-led migrations have transitioned to Migration Manager.
>
>**Tenant to tenant migration**. Cross-tenant OneDrive migration is now available outside of Migration Manager. Learn more here: [Cross-tenant OneDrive migration](/microsoft-365/enterprise/cross-tenant-onedrive-migration).  
>
>A cross tenant migration solution for SharePoint is currently being developed and in private preview.  To learn more, see [How to participate in the Cross-tenant SharePoint migration preview](/microsoft-365/enterprise/cross-tenant-sharepoint-migration).



To delete a migration created using Mover, do the following:

1. Click **Migration actions**.
2. From the dropdown menu, select **Delete migration**.
3. Type **DELETE** in the pop-up window.
4. Click **OK**.

![Delete a migration](media/delete-migration.png)

>[!Warning]
> Deleting the migration will delete ALL logging information.  It will NOT delete any data in the source or destination paths.
> Do not delete a migration during an ongoing troubleshooting process as it is unrecoverable.
