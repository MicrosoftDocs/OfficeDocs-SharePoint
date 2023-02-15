---
title: "Migrated Flow structure when using SPMT"
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
description: "Learn about how workflows will be structured when migrating from SharePoint Server to Power Automate using SPMT."
---

# Migrated flow structure for SharePoint 2010 OOTB workflows

When the Sharepoint Migration Tool (SPMT) migrates a workflow to Power Automate, it finds the Power Automate built-in actions that best match the functions in the original SharePoint workflow. Because of the feature gaps between SharePoint workflow and Power Automate, a converted flow may not carry the exact same behavior as the original one.

SPMT will generate one or two Power Automate flows for one SharePoint workflow depending on its start options. 

- If a workflow can be manually started, a list flow is generated with manual trigger. 
- If a workflow can be auto started on create or update, a list flow is generated with auto-trigger. 

The chart below shows the first action in a flow migrated from an **out-of-the-box (OOTB)** approval workflow (manual start) and the UI form when a user starts the flow. It lists the mapping of five user inputs between original workflow and converted flow.

![out of the box workflows](media/spmt-workflow-ootb-options.png)

## Migrated approval workflow

The approval workflow is migrated with this structure:

:::image type="content" source="media/spmt-approval-workflow-steps.png" alt-text="Approval workflow migrated structure":::

For an auto or manually triggered Power Automate flow, the following workflow configurations are migrated to the destination flow:

|Type|Options|
|---|---|
|Manual approval PA flow|Four user inputs are supported in the migrated flow. They are: </br>- Approval type Options: First to respond, Wait until all approve.<br>- Approvers. Emails<br>- Request. Text<br>- CC. Emails<br>- Enable Content Approval. On/Off|
| Auto triggered PA flow|The following configurations in workflow are migrated to destination flow. </br>- The approval type, **Everyone must approve** is used in the destination flow.</br>- Approvers. Emails</br>- Request. Text</br>- CC. Emails</br>- Enable Content Approval. On/Off|

## Migrated collect feedback workflow

The collect feedback workflow is migrated with this structure:

:::image type="content" source="media/spmt-collect-signature-workflow-steps.png" alt-text="Collect feedback workflow migrated structure":::

For an auto or manually triggered Power Automate flow, the following workflow configurations are migrated to the destination flow:

|Type|Options|
|---|---|
|Manual approval PA flow|Three user inputs are supported in the migrated flow. They are: </br><br>- Reviewers. Emails<br>- Request. Text<br>- CC. Emails|
| Auto triggered PA flow|The following configurations in workflow are migrated to destination flow. They are: </br><br>- Reviewers. Emails<br>- Request. Text<br>- CC. Emails|

## Migrated collect signature workflow

The collect signature workflow is migrated with this structure:

:::image type="content" source="media/spmt-collect-signature-workflow-steps.png" alt-text="Collect signature migrated structure":::

For an auto or manually triggered Power Automate flow, the following workflow configurations are migrated to the destination flow:

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
