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

# Step 2 Migrate workflows

After configuring the required endpoints and configuring Power Automate, you are ready to start migrating your SharePoint Server workflows.

1. Start SPMT, and then enter your Microsoft 365 username and password.    
2. Select **Start your first migration**.
3. Select **Workflow migration**.

![Select workflow migration](media/spmt-workflow-select.png)

4. Enter the URL of the SharePoint Server workflow you want to migrate and select which workflows to include in the migration. If you select the option for a specific list, you will be prompted for the list name.  Select **Next**.

![select a workflow source](media/spmt-workflow-select-source.png)

5. Enter your destination; the SharePoint site and list where you want to migrate your content.  If the site or the list doesn't currently exist, they will be created for you. Select **Next**. 
6. Review your migrations.  Select **Add another task** to select another set of files to migrate.

![Review workflow migrations](media/spmt-workflow-review-workflow-migrations.png)

## Step 3:  [Activate workflows](spmt-workflow-step3.md)