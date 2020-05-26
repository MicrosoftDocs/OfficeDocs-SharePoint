---
title: Mover Migration Tools overview and planning
author: JoanneHendrickson
manager: pamgreen
audience: ITPro
ms.topic: article
ms.service: sharepoint-online
localization_priority: Priority
ms.collection: 
- SPMigration
- M365-collaboration
search.appverid: MET150
description: "Overview and planning to the Mover Migration tools"
---
## Connectors

### What is a connector?

A **Connector** is what we call our link to your cloud storage accounts.

To set up a transfer, you must grant us access to your cloud storage accounts. Without this link, we are unable to communicate with them.

Creating a **Connector** may involve authenticating via OAuth or with normal username/password credentials. You only need to authenticate once per account.

Our authorization is lost when you delete the **Connector**, delete your account with us, or revoke our access through your cloud service's security settings.

### Which connector to use for each Microsoft service

|**Microsoft service**|**Which Mover connector to use**|
|:-----|:-----|
|Azure Blob Storage|Azure Blob Storage Connector|
|OneDrive Consumer|	OneDrive Consumer Connector|
|OneDrive for Business (Administrator)|	Office 365 Connector|
|OneDrive for Business (User)|	OneDrive for Business (User) Connector|
|SharePoint Online|Office 365 Connector|

## Deleting connectors

Deleting a **Connector** revokes our access to your cloud storage accounts. To confirm that we have been deauthorized, visit the security settings in your respective cloud service and check for our app.

Using our app to remove our authorization with a particular cloud service is simple:

1. From the **Transfer Wizard**, for the **Connector** type you want to delete, select **Manage ▼**.
2. To the right of **Connect**, select arrow ▼.
3. Select **Delete**.
4. Confirm you want to delete, and you're done!

![Delete connector](media/delete-connector.png)

>[!Note]
>Deleting a **Connector** is permanent and cannot be reversed. The **Connector** type disappears from the **Transfer Wizard**. To add a new **Connector**, select **Authorize New Connector**.

### Reauthorizing connectors

Reauthorizing a **Connector** is sometimes necessary if we lose authorization or access to your cloud storage accounts or web servers. It is also a good first step in trying to resolve most issues with your **Connectors**.

The process to authorize a Connector again is very simple:

1. Find the **Connector** type you want to reauthorize.
2. Select **Manage ▼**.
3. For other **Connector** options, next to **Connect**, select ▼.
4. Select **Reauthorize**.
5. Follow the same steps you performed when you first created the **Connector** to renew the authorization tokens/permissions.

>[!Note]
>You are unable to change the display name of the **Connector**. If you want to rename it, you must delete and re-add the **Connector**.

**Connectors** are automatically deauthorized if they haven't transferred any data in the last 90 days. If you try to load a deauthorized **Connector** in the **Transfer Wizard**, an error message appears, along with a prompt to reauthorize the **Connector**.