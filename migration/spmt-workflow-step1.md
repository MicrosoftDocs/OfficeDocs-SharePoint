---
title: "Overview Migrating workflows with the SharePoint Migration Tool (SPMT)"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: serdars
recommendations: true
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.localizationpriority: high
ms.collection:
- SPMigration
- M365-collaboration
ms.custom: 
ms.assetid: 
description: "Overview Migrate your SharePoint Server workflows to Microsoft 365 using the SharePoint Migration Tool (SPMT)"
---

# Step 1 - Configure endpoints and Power Automate

Before you begin your workflow migration, configure the following endpoints.

## Configure endpoints

The following endpoints are required by workflow migration.

|Endpoint|Description|
|:-----|:-----|
|https://service.powerapps.com ||
|https://api.bap.microsoft.com||
|https://gov.service.powerapps.us||
|https://gov.api.bap.microsoft.us||
|https://high.service.powerapps.us||
|https://high.api.bap.microsoft.us||
|https://service.apps.appsplatform.us||
|https://api.bap.appsplatform.us||



## Configure Power Automate 

If your tenant has never used Power Automate before, you must configure it before you begin migration. We recommend using Edge or Internet Explorer.

1.	Sign in to https://admin.powerplatform.microsoft.com/ using an admin account.
2.	Select **Add database** to your default environment.

![Add powerautomate database](media/spmt-add-powerautomate-db.png)

3.	Wait for "State" status to change to **Ready**.
4.	To sync AAD user to CDS, sign in to **Microsoft Power Automate | Microsoft Power Platform** with the account you’d like to set as the default flow owner.