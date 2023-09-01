---
ms.date: 05/26/2020
title: Mover migration - setting up the Google Cloud storage connector
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
- m365initiative-migratetom365
search.appverid: MET150
description: "Using the Mover migration service to set up the Google Cloud storage connector"
---
# Setting up your source: Google Cloud Storage Connector

>[!Important]
>**Mover is now retired for all Admin led migrations**. The ability to migrate from Google Drive, Box, Dropbox, and Egnyte has been fully integrated into Migration Manager. For full details see: [Mover retirement timeline](mover-retirement-timeline.md).  Migration Manager does not support the migration of Amazon S3 or Azure blob storage.
>
>All FastTrack-led migrations have transitioned to Migration Manager.
>
>**Tenant to tenant migration**. Cross-tenant OneDrive migration is now available outside of Migration Manager. Learn more here: [Cross-tenant OneDrive migration](/microsoft-365/enterprise/cross-tenant-onedrive-migration).  
>
>A cross tenant migration solution for SharePoint is currently being developed and in private preview.  To learn more, see [How to participate in the Cross-tenant SharePoint migration preview](/microsoft-365/enterprise/cross-tenant-sharepoint-migration).


Authorizing Google Cloud Storage is straightforward. To authorize or add a Google Cloud Storage account as a Connector, follow these simple steps:

- First, you'll need to log in to your Google Cloud Platform Dashboard/Console.
- From there, go to Storage and then Settings and Interoperability. From here, you can see your storage buckets, and which one is set to default.
- Click on Create a new key. These are the credentials you'll use in the app in the next steps.

## Enabling Interoperability in Google Cloud

1. In the Transfer Wizard click **Authorize New Connector**.

![Auth New Connector](media/clear_auth.png)

2. Find Google Cloud Storage in the Connector list.
3. Click **Authorize**.

![Google Cloud Connector List](media/mover-auth-source-connector-google.png)

4. A new window (tab) will open. Name your Connector (Optional).
5. Enter your Access Key & Secret Key (which you created in the previous steps), as well as your Project ID (if different from the default).

![Google Cloud Name Connector](media/name-connector-google-cloud.png)

6. Click Authorize again.


## Troubleshooting

**Google Cloud Nearline:** Once you've authorized a Google Cloud Storage Connector, you simply have to create a Nearline bucket the same way you would a regular storage bucket. [Click here to read more in Google's support docs](https://cloud.google.com/storage/docs/storage-classes#nearline).


