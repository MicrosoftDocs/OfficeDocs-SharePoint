---
title: "Migrate SharePoint workflows in Microsoft 365 using the SharePoint Migration tool"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: serdars
recommendations: true
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.localizationpriority: high
ms.collection: 
- IT_Sharepoint_Server_Top
- Strat_SP_gtc
- SPMigration
- M365-collaboration
- m365initiative-migratetom365
ms.custom:
- seo-marvel-mar2020
description: Learn how to migrate SharePoint workflows into Microsoft 365 using the SharePoint Migration tool (PSMT).
---
# Migrate SharePoint workflows using the SharePoint Migration Tool (SPMT)

 

## Prerequisites and endpoints

The following endpoints are required for workflow migration. 

|Required endpoint|For|
|:-----|:-----|:-----|
|https://service.powerapps.com |Workflow migration |
|https://api.bap.microsoft.com |Workflow migration|
|https://gov.service.powerapps.us |Workflow migration|
|https://gov.api.bap.microsoft.us |Workflow migration|
|https://high.service.powerapps.us|Workflow migration |
|https://high.api.bap.microsoft.us |Workflow migration|
|https://service.apps.appsplatform.us |Workflow migration|
|https://api.bap.appsplatform.us |Workflow migration|

## Prepare your environment
If PowerAutomate has never been used on the tenant to which you migrating your workflows, you must prepare it in advance.

1. Sign in to https://admin.powerplatform.microsoft.com/ using an admin account.
2. Select **Add database** to add a database to your default environment.
3. Wait for state to change to **Ready**.
4. To sync AAD users to CDS, sign in to Microsoft Power Automatehttps://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Fus.flow.microsoft.com%2Fen-us%2F&data=04%7C01%7CZhaoyang.Sun%40microsoft.com%7C8e043b2f15e84ca3144f08d93bb7661d%7C72f988bf86f141af91ab2d7cd011db47%7C0%7C0%7C637606481152589482%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C1000&sdata=qDDGFkHFE2hjKAuibZ4PbN1gbghoTDFM2gIuEdNdztw%3D&reserved=0 | Microsoft Power Platform with the account you’d like to set as the default flow owner


Install

