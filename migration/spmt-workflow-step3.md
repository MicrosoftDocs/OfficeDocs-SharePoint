---
title: "Step 3: Activate workflows after migration"
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

The chart below shows the first action in a flow migrated from an out-of-the-box (OOTB) approval workflow (manual start) and the UI form when a user starts the flow. It lists the mapping of five user inputs between original workflow and converted flow.

![out of the box workflows](media/spmt-workflow-ootb-options.png)

### Migrated approval workflow

|Type|Options|
|---|---|
|List workflow|Manual start on selected item will have a new list flow with manual trigger, also known as *LIST_MANUAL_APPROVAL*.</br>Trigger by new item and update item will have a new list flow with auto trigger, also known as *LIST_AUTO_APPROVAL*.|
|Document library|Manual start on selected file will have a new file flow with manual trigger, also known as *FILE_MANUAL_APPROVAL*<br/>Trigger by new file and update file will have a new file flow with auto trigger, also known as *FILE_AUTO_APPROVAL*.|
|Manual approval PA flow|Four user inputs are supported in the migrated flow. They are: </br>- Approval type Options: First to respond, Wait until all approve.<br>- Approvers. Emails<br>- Request. Text<br>- CC. Emails<br>- Enable Content Approval. On/Off|
| Auto triggered PA flow|The following configurations in workflow are migrated to destination flow. </br>- The approval type, **Everyone must approve** is used in the destination flow.</br>- Approvers. Emails</br>- Request. Text</br>- CC. Emails</br>- Enable Content Approval. On/Off|

### Migrated collect feedback workflow

|Type|Options|
|---|---|
|List workflow|Manual start on selected item will have a new list flow with manual trigger, also known as *LIST_MANUAL_COLLECTFEEDBACK*.</br>Trigger by new item and update item will have a new list flow with auto trigger, also known as *LIST_AUTO_COLLECTFEEDBACK*.|
|Document library|Manual start on selected file will have a new file flow with manual trigger, also known as *FILE_MANUAL_COLLECTFEEDBACK*<br/>Trigger by new file and update file will have a new file flow with auto trigger, also known as *FILE_AUTO_COLLECTFEEDBACK*.|
|Manual approval PA flow|Three user inputs are supported in the migrated flow. They are: </br><br>- Reviewers. Emails<br>- Request. Text<br>- CC. Emails|
| Auto triggered PA flow|The following configurations in workflow are migrated to destination flow. They are: </br><br>- Reviewers. Emails<br>- Request. Text<br>- CC. Emails|
