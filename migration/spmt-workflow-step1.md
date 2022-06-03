---
title: "Step 1: Configure endpoints and Power Automate for SharePoint workflow migration"
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
ms.subservice: sharepoint-migration
ms.localizationpriority: high
ms.collection:
- SPMigration
- M365-collaboration
ms.custom: 
ms.assetid: 
description: "The first step in migrating SharePoint Server workflows to Microsoft 365."
---
# Step 1 - Configure endpoints and Power Automate

>[!Note]
>This feature is currently in public preview, and subject to change.

Before you begin your workflow migration, configure the required endpoints

## Configure endpoints

The following endpoints are required by workflow migration.

|Endpoint|
|:-----|
|https://service.powerapps.com |
|https://api.bap.microsoft.com|
|https://gov.service.powerapps.us|
|https://gov.api.bap.microsoft.us|
|https://high.service.powerapps.us|
|https://high.api.bap.microsoft.us|
|https://service.apps.appsplatform.us|
|https://api.bap.appsplatform.us|



## Configure Power Automate 

If you have never used Power Automate with this tenant before, you must configure it before you begin migration. We recommend using Edge or Internet Explorer.

1.	Sign in to https://admin.powerplatform.microsoft.com/ using an admin account.
2.	Select **Add database** to your default environment.

![Add powerautomate database](media/spmt-add-powerautomate-db.png)

3.	Wait for "State" status to change to **Ready**.
4.	To sync AAD user to CDS, sign in to **Microsoft Power Automate | Microsoft Power Platform** with the account you’d like to set as the default flow owner.


## Step 2:  [Migrate Workflows](spmt-workflow-step2.md)