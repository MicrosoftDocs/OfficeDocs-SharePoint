---
title: "Migrate SharePoint workflows with the SharePoint Migration Tool (SPMT)"
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
description: "Overview of how to migrate your SharePoint Server workflows to Microsoft 365 using the SharePoint Migration Tool (SPMT)."
---
# Overview: Migrate SharePoint Server workflows to Microsoft 365

>[!Note]
>This feature is currently in public preview, and subject to change.

Microsoft removed SharePoint Server 2010 workflow services from existing tenants on November 1, 2020. We recommend that you move your classic SharePoint Server workflows to Power Automate flows. 

Using the SharePoint Migration Tool (SPMT), you can now migrate your SharePoint Server flows to Microsoft 365.
Workflow migration is limited to:

- List and library "out-of-box" (OOTB) approval workflows
- Workflow definitions and associations

## How does it work?
|Step|What happens|
|:-----|:-----|
|[Step 1: Configure endpoints and Power Automate](spmt-workflow-step1.md)|Configure required endpoints.  If your tenant has never used Power Automate, configure it before you begin migration.|
|[Step 2: Migrate workflows](spmt-workflow-step2.md)|Using SPMT, migrate your SharePoint Server workflows.|
|[Step 3: Activate workflows](spmt-workflow-step2.md)|Sign in to Power Automate to activate the newly migrated workflows.|


## Get started

To get started:

Go to the [Migration Manager page of the new SharePoint admin center](https://aka.ms/ODSP-MM-BOX), and sign in with an account that has [admin permissions](/sharepoint/sharepoint-admin-role) for your organization.

Make sure that you have:

- **Access to the destination**: You must either be a global admin or OneDrive/SharePoint admin to the Microsoft 365 tenant where you want to migrate your content. 

- **Access to the source**: Have SharePoint Server account credentials that have read access to any workflow you plan to migrate.

- **Prerequisites installed:** Make sure you have the necessary prerequisites installed.