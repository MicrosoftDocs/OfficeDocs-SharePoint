---
title: "Migrate SharePoint workflows with the SharePoint Migration Tool (SPMT) to Power Automate"
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
ms.custom: admindeeplinkSPO
ms.assetid: 
description: "Overview of how to migrate your SharePoint Server workflows to Power Automate using the SharePoint Migration Tool (SPMT)."
---
# Overview: Migrate SharePoint Server 2010 workflows to Power Automate

>[!Note]
>This feature is currently in public preview, and subject to change.

Microsoft removed **SharePoint Server 2010** workflow services from existing tenants on November 1, 2020. We recommend that you move your classic SharePoint Server workflows to Power Automate flows. 

Using the SharePoint Migration Tool (SPMT), you can now migrate these workflows to Power Automate

**SharePoint Server 2010 out of the box (OOTB) workflows:**
- Approval workflow
- Collect feedback workflow
- Collect signature workflow
- Three-state workflow
- List library workflows and content-type workflows (not site workflows)
- Workflow definitions and associations (not workflow history data)

>[!Note]
> Workflows created with  SharePoint Server Designer 2013 or SharePoint Server 2013 are currently not supported.


## How does it work?

|Step|What happens|
|:-----|:-----|
|[Step 1: Configure endpoints and Power Automate](spmt-workflow-step1.md)|Configure required endpoints.  If your tenant has never used Power Automate, configure it before you begin migration.|
|[Step 2: Migrate workflows](spmt-workflow-step2.md)|Using SPMT, migrate your SharePoint Server workflows.|
|[Step 3: Activate workflows](spmt-workflow-step2.md)|Sign in to Power Automate to activate the newly migrated workflows.|


## Get started

To get started:

Go to the <a href="https://go.microsoft.com/fwlink/?linkid=2185075" target="_blank">Migration center</a> in the SharePoint admin center, and sign in with an account that has [admin permissions](/sharepoint/sharepoint-admin-role) for your organization.

Make sure that you have:

- **Access to the destination**: You must either be a global admin or OneDrive/SharePoint admin to the Microsoft 365 tenant where you want to migrate your content. 
- **Access to the source**: Have SharePoint Server account credentials that have read access to any workflow you plan to migrate.
- **Prerequisites installed:** Make sure you have the necessary prerequisites installed.

## Re-run migration 

SPMT will skip a workflow if it has already been successfully migrated. If you want to run a new migration to override the migrated flow, delete it from the destination before starting the migration.