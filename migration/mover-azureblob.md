---
ms.date: 05/26/2020
title: Mover migration - setup your Azure Blob Storage Connector
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
description: "Using Mover migration service, set up your Azure blob storage connector."
---
# Authorizing the Azure Blob Storage Connector


>[!Important]
>**Mover is now retired for all Admin led migrations**. The ability to migrate from external cloud sources has been fully integrated into Migration Manager.
>
>All FastTrack-led migrations have transitioned to Migration Manager.
>
>**Tenant to tenant migration**. Cross-tenant OneDrive migration is now available outside of Migration Manager. Learn more here: [Cross-tenant OneDrive migration](/microsoft-365/enterprise/cross-tenant-onedrive-migration).  
>
>A cross tenant migration solution for SharePoint is currently being developed and scheduled for release in Spring 2023.



Authorizing Azure Blob Storage is straightforward. To authorize or add an Azure Blob Storage account as a Connector, follow these steps:

1. In the *Transfer Wizard*, click **Authorize New Connector**.

![Auth New Connector](media/clear_auth.png)

2. Find Azure Blob Storage in the Connector list.
3. Click **Authorize.**

![Azure blob connector](media/mover-auth-source-connector.png)

4. A new window (tab) will open. Name your Connector (Optional).
5. Enter your Account Name.
6. Enter your Account Key.
7. Click Authorize again, and voila!

![Azure connector name](media/name-connector-azure.png)

