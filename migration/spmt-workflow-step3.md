---
ms.date: 12/02/2021
title: "Step 3: Activate workflows after migration"
ms.reviewer:
ms.author: mactra
author: MachelleTranMSFT
manager: serdars
recommendations: true
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: microsoft-365-migration
ms.localizationpriority: high
ms.collection:
- SPMigration
- M365-collaboration
- m365initiative-migratetom365
ms.custom:
ms.assetid:
description: "The third step in migrating SharePoint Server workflows to Microsoft 365, activating the migrating flows."
---

# Step 3 - Activate migrated workflows Power Automate

> [!NOTE]
> This feature is currently in public preview, and subject to change.

After the migration has completed, the flow owner must sign in to Power Automate to turn on the migrated flows.

1. Sign in to Power Automate.
2. Navigate to **Solutions**, choose the latest one matching "Solution" in migration report.
3. Edit connection references. Select **New connection** if no existing connection found. If so, we recommend you pick an existing connection.

   ![Select a new workflow connection](media/spmt-workflow-automate-connection.png)

4. Turn on flow after all connection references are configured.

![Turn on workflow after connection references are configured](media/spmt-workflow-turn-on-flow-after-connection.png)

After the migrated flows are turned on, testing is suggested to verify the behavior of the flows.

## The migrated flows

When SPMT migrates the workflow to Power Automate, it finds the Power Automate built-in actions that best match the functions in the original SharePoint workflow. Because of the feature gaps between SharePoint workflow and Power Automate, a converted flow may not carry the exact same behavior as the original one.

The tool generates one or two Power Automate flows for one SharePoint workflow depending on its start options.

- If a workflow can be manually started, a list flow is generated with manual trigger
- If a workflow can be auto started on create or update, a list flow is generated with auto trigger.

###  SharePoint Server 2010 workflows (OOTB)

For full details on what SharePoint Server 2010 out-of-the-box (OOTB) workflows are supported including the structure, see:

- [SharePoint Server 2010 workflow migrations (OOTB)](spmt-workflow-migrated-flows.md) 

###  SharePoint Designer 2010 & 2013 workflows

For full details on what workflow actions and lookups are supported, and what is not, see:

- [SharePoint Designer 2010 & 2013 Workflow migrations](spmt-workflow-migration-spd.md)

## What to check after migration

**Review your nesting levels.** </br>Power Automate allows a maximum of eight "nesting levels". If your migrated workflow exceeds that level, an error message will display when you select **Save** on the flow edit page. Review the migrated flow and modify them as needed. [Learn more in Limits and configuration - Power Automate](/power-automate/limits-and-config#flow-definition-limits)

- *Error message example*. "The power flow's logic app flow template was invalid. The template actions action_name are nested at level '9' which exceeds the maximum nesting limit of '8'.

**Review the workflow migration report for unsupported actions.** </br>Look for any entry with the status value of "migrated" and with more than one unsupported action. These values indicate that the "unsupported actions" have been converted to **compose actions** in the migrated workflow. Review the migrated flow, locate the **compose actions**, and update accordingly. [Learn more about unsupported workflow actions](/sharepointmigration/spmt-workflow-migration-spd#designer-workflow-actions-not-migrated)

>[!Note]
>[Learn more here: SPMT Workflow reports and error codes](spmt-workflow-report-and-error-codes.md)