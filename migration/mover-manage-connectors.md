---
title: Mover Migration Connectors
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
search.appverid: MET150
description: "Mover Migration Connectors"
---
# Connectors

>[!Important]
>We have retired the legacy [Mover](https://app.mover.io) tool's ability for admin-led migrations from [Google Drive](mm-google-overview.md), [Dropbox](mm-dropbox-overview.md), [Box](mm-box-overview.md), and [Egnyte](mm-egnyte-overview.md). Please use [Migration Manager](https://aka.ms/ODSP-MM), located in the SharePoint admin center.
>
>*Ongoing migrations are not impacted by this change. However, you cannot create new connectors.* If you are currently in the middle of a Mover migration, you may continue using Mover until you finish your migration using your existing connectors. FastTrack led migrations are not impacted at this time.
>
>[**Individuals or students**: You may continue to use Mover, learn how!](https://support.microsoft.com/en-us/office/move-your-school-files-when-you-graduate-7dbda93c-71e6-483f-8914-ad445554cd31)
>
>[Learn more about the Mover.io retirement](mover-retirement-timeline.md)

### What is a connector?

A **Connector** is what we call our link to your cloud storage accounts.

To set up a transfer, you must grant us access to your cloud storage accounts. Without this link, we are unable to communicate with them.

Creating a **Connector** may involve authenticating via OAuth or with normal username/password credentials. You only need to authenticate once per account.

Our authorization is lost when you delete the **Connector**, delete your account with us, or revoke our access through your cloud service's security settings.

### Which connector to use for each Microsoft service

|Microsoft service|Which Mover connector to use|
|---|---|
|Azure Blob Storage|Azure Blob Storage Connector|
|OneDrive Consumer|OneDrive Consumer Connector|
|OneDrive for Business (Administrator)|Office 365 Connector|
|OneDrive for Business (User)|OneDrive for Business (User) Connector|
|SharePoint Online|Office 365 Connector|

## Deleting connectors

Deleting a **Connector** revokes our access to your cloud storage accounts. To confirm that we have been deauthorized, visit the security settings in your respective cloud service and check for our app.

Using our app to remove our authorization with a particular cloud service is simple:

1. From the **Transfer Wizard**, for the **Connector** type you want to delete, select **Manage ▼**.
2. To the right of **Connect**, select arrow ▼.
3. Select **Delete**.
4. Confirm you want to delete, and you're done!

![Delete connector](media/delete-connector.png)

> [!NOTE]
> Deleting a **Connector** is permanent and cannot be reversed. The **Connector** type disappears from the **Transfer Wizard**. To add a new **Connector**, select **Authorize New Connector**.

## Reauthorizing connectors

Reauthorizing a **Connector** is sometimes necessary if we lose authorization or access to your cloud storage accounts or web servers. It is also a good first step in trying to resolve most issues with your **Connectors**.

The process to authorize a Connector again is very simple:

1. Find the **Connector** type you want to reauthorize.
2. Select **Manage ▼**.
3. For other **Connector** options, next to **Connect**, select ▼.
4. Select **Reauthorize**.
5. Follow the same steps you performed when you first created the **Connector** to renew the authorization tokens/permissions.

> [!NOTE]
> You are unable to change the display name of the **Connector**. If you want to rename it, you must delete and re-add the **Connector**.

**Connectors** are automatically deauthorized if they haven't transferred any data in the last 90 days. If you try to load a deauthorized **Connector** in the **Transfer Wizard**, an error message appears, along with a prompt to reauthorize the **Connector**.
