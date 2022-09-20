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

The approval workflow is migrated with this structure:

:::image type="content" source="media/spmt-approval-workflow-steps.png" alt-text="Approval workflow migrated structure":::

|Type|Options|
|---|---|
|List workflow|Manual start on selected item will have a new list flow with manual trigger, also known as *LIST_MANUAL_APPROVAL*.</br>Trigger by new item and update item will have a new list flow with auto trigger, also known as *LIST_AUTO_APPROVAL*.|
|Document library|Manual start on selected file will have a new file flow with manual trigger, also known as *FILE_MANUAL_APPROVAL*<br/>Trigger by new file and update file will have a new file flow with auto trigger, also known as *FILE_AUTO_APPROVAL*.|
|Manual approval PA flow|Four user inputs are supported in the migrated flow. They are: </br>- Approval type Options: First to respond, Wait until all approve.<br>- Approvers. Emails<br>- Request. Text<br>- CC. Emails<br>- Enable Content Approval. On/Off|
| Auto triggered PA flow|The following configurations in workflow are migrated to destination flow. </br>- The approval type, **Everyone must approve** is used in the destination flow.</br>- Approvers. Emails</br>- Request. Text</br>- CC. Emails</br>- Enable Content Approval. On/Off|

### Migrated collect feedback workflow

The collect feedback workflow is migrated with this structure:

:::image type="content" source="media/spmt-collect-signature-workflow-steps.png" alt-text="Collect feedback workflow migrated structure":::

|Type|Options|
|---|---|
|List workflow|Manual start on selected item will have a new list flow with manual trigger, also known as *LIST_MANUAL_COLLECTFEEDBACK*.</br>Trigger by new item and update item will have a new list flow with auto trigger, also known as *LIST_AUTO_COLLECTFEEDBACK*.|
|Document library|Manual start on selected file will have a new file flow with manual trigger, also known as *FILE_MANUAL_COLLECTFEEDBACK*<br/>Trigger by new file and update file will have a new file flow with auto trigger, also known as *FILE_AUTO_COLLECTFEEDBACK*.|
|Manual approval PA flow|Three user inputs are supported in the migrated flow. They are: </br><br>- Reviewers. Emails<br>- Request. Text<br>- CC. Emails|
| Auto triggered PA flow|The following configurations in workflow are migrated to destination flow. They are: </br><br>- Reviewers. Emails<br>- Request. Text<br>- CC. Emails|

## Migrated collect signature workflow

The collect signature workflow is migrated with this structure:

:::image type="content" source="media/spmt-collect-signature-workflow-steps.png" alt-text="Collect signature migrated structure":::

|Type|Options|
|:-----|:-----|
|Manually triggered collect feedback| Before starting a workflow, three user inputs are supported in the migrated flow. They are:</br>- Signer order maps to Signer type. Options: First to respond, Wait until all approve</br>-Signers maps to Signers. Emails</br>-Request maps to Message. Text</br>- CC maps to CC. Emails|
|Auto triggered collect feedback|Signer order maps to Signer type. “Everyone must approve” is used in migrated flow.</br>- Signers maps to Signers. Emails</br>- Request maps to Message. Text</br>- CC maps to CC. Emails|
|

## Migrated three-state workflow

The three state workflow is migrated with this structure:

:::image type="content" source="media/spmt-three-state-workflow-steps.png" alt-text="Three state workflow structure":::

For auto or manual triggered three state Power Automate flow, the following configurations in workflow are migrated to destination flow.  The workflow states are:

- StatusField (Status field name)
- InitialState (Initial state value)
- MiddleState (Middle state value)
- FinalState (Final state value)


|Type|State|Details|
|:-----|:-----|:-----|
|Task |Initial|**Task Title**</br>-CustomMessageText (custom message)</br>-CustomMessageField (Field included in task title)</br></br>**Task Description**</br>CustomMessageTextBody (Task description/custom message)</br>CustomMessageBodyField (Field included in task body)</br></br>**Task Assign To**</br>- TaskAssignedToCustom (Task assigners is the value of an item field, or Task assigners are customized)</br>-AssignedToField (Task assigner field)</br>-CustomAssignedTo (Customized task assigners)|
|Email message|Initial|- SendEmail (Whether to send email)</br>- IncludeTaskAssignedTo (Whether to include task assigner in to-list)</br>- ToList (Email to-list)</br>- SubjectTextIncludeTitle (Whether to include task title in email subject text)</br>- SubjectText (Email subject text)</br>- BodyTextIncludeLink (Whether to include item link in email message)</br>- BodyText (Email body text)</br>|
|Task|Middle|**Task Title**</br>- CustomMessageText2 (custom message)</br>- CustomMessageField2 (Field included in task title)</br>**Task Description**</br>- CustomMessageTextBody2 (Task description/custom message)</br>- CustomMessageBodyField2 (Field included in task body)</br>**Task Assign To**</br>- TaskAssignedToCustom2 (Task assigners is the value of an item field, or Task assigners are customized)</br>- AssignedToField2 (Task assigner field)</br>- CustomAssignedTo2 (Customized task assigners)|
|E-mail message| Middle|- SendEmail2 (Whether to send email)</br> - IncludeTaskAssignedTo2 (Whether to include task assigner in to-list) </br>- ToList2 (Email to-list) </br>- SubjectTextIncludeTitle2 (Whether to include task title in email subject text)</br> - SubjectText2 (Email subject text)</br> - BodyTextIncludeLink2 (Whether to include item link in email message)</br>- BodyText2 (Email body text)|
