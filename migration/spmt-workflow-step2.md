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
3. Select **SharePoint Server**.
4. Select the **Workflow migration** type.


![Select workflow migration](media/spmt-workflow-select.png)

5. Enter the URL of the SharePoint Server workflow you want to migrate.
6. Enter your username and password to the SharePoint Server site; it can be UserID or user email. Select **Sign in**. 
7. Select which workflows to include in the migration. If you select the option for a specific list, you will be prompted for the list name.  Select **Next**.


![spmt workflow source](media/spmt-workflow-select-source.png)

8. Enter your destination; the SharePoint site and list where you want to migrate your workflow.  If the site or the list doesn't currently exist, they will be created for you. Select **Next**. 
9. This task is added to the list of migration tasks.  If you want to select another set of data files to migrate, select **Add a source**.  Otherwise, select **Next** to go to the next step.
10. On the settings page, turn on **Only perform scanning** to run workflow scanning.
11. In the **Power Automate flow owner** box, enter the email address of the new flow owner.  

![Set your workflow settings](media/spmt-workflow-settings.png)

12. Review your migrations.  Select **Add another task** to select another set of files to migrate, or Next to submit migration.

![Review workflow migrations](media/spmt-workflow-review-workflow-migrations.png)

## Step 3:  [Activate workflows](spmt-workflow-step3.md)