---
ms.date: 02/08/2023
title: "Migrate SharePoint Designer workflows with SPMT"
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
description: Overview Migrate your SharePoint Designer 2010 & 2013 created workflows to Microsoft 365 using the SharePoint Migration Tool (SPMT)"
---
# SharePoint Designer 2010 & 2013 workflow migrations to Power Automate

The SharePoint Migration Tool (SPMT) 4.1 now supports the migration of SharePoint Designer (SPD) 2010 & 2013 workflows.

**Actions** are the main elements that form a workflow definition. The current release of SPMT can migrate some commonly used actions, but not all are currently supported. Future releases of SPMT will support more SPD actions.

## Actions 

|Workflow action category|Workflow action |Workflow version|Flow action in Power Automate|
|:-----|:-----|:-----|:-----|
|Core action|Send an Email|2010, 2013|Send an email |
|Core action|Set workflow variable|2010, 2013|Set variable|
|Core action|Do Calculation|2010, 2013|Set variable|
|Core action|Log to History List*|2010, 2013|Compose|
|Core action|Set Workflow Status*|2010, 2013|Compose|
|Core action|Go to stage**|2010, 2013||
|Core action|Add a Comment|2010, 2013|Compose|
|Core action|Add Time to Date|2010, 2013|Set variable|
|Core action|Pause for Duration|2010, 2013|Delay|
|Core action|Pause Until Date|2010, 2013|Delay until|
|Utility action|Extract Substring from End of String|2010, 2013|Set variable|
|Utility action|Extract Substring from Index of String|2010, 2013|Set variable|
|Utility action|Extract Substring from Start of String|2010, 2013|Set variable|
|Utility action|Extract Substring of String from index with Length|2010, 2013|Set variable|
|Utility action|Fin Substring in String|2013|Set variable|
|Utility action|Replace Substring in String|2013|Set variable|
|Utility action|Trim String|2013|Set variable|
|Utility action|Find Interval Between Dates|2010, 2013|Set variable|
|List action|Create New List Item|2010, 2013|Create item|
|List action|Set field value in the current item|2010, 2013|Send an HTTP request to SharePoint|
|List action|Update List Item|2010, 2013|Send an HTTP request to SharePoint|
|List action|Check in item|2010, 2013|Check in file|
|List action|Check out item|2010, 2013|Check out file|
|List action|Discard check out item|2010, 2013|Discard check out|
|List action|Delete item|2010, 2013|Delete item or Delete file|
|Task action|Assign a task |2013|Start, wait for an approval|
|Task action|Start a task process |2013|Start, wait for an approval|
|Task action|Start Approval Process|2010|Start, wait for an approval|
|Task action|Start Feedback Process|2010|Start, wait for an approval|
|Task action|Start Custom Task Process|2010|Start, wait for an approval|
|Task action|Assign a To-do Item|2010|Start, wait for an approval|
|Condition|If/else|2010, 2013|If/else|
|Condition|Created by a specific person|2010, 2013|If/else|
|Condition|Created in a specific date span|2010, 2013|If/else|
|Condition|Modified by a specific person|2010, 2013|If/else|
|Condition|Modified in a specific date span|2010, 2013|If/else|
|Condition|Title field contains keywords|2010, 2013|If/else|
|Condition|If current item field equals value|2010|If/else|
|Condition|The file size in a specific range kilobyte|2010|If/else|
|Condition|The file type is a specific type|2010|If/else|


>[!Note]
>"*" There is no direct matching action in Power Automate for workflow actions like “Log to History List” and “Set Workflow Status”, “Compose” action is used as a placeholder action in migrated flow.
>
>"**" A workflow with multiple stage forms a directed graph. A general directed graph cannot be supported in Power Automate. The migration tool will only convert workflow with stage format of Directed Rooted Tree (or Arborescence), and report error otherwise.



## Designer workflow actions not migrated


|Workflow action category|Workflow action|Workflow version|
|:-----|:-----|:-----|
|Core action|Call HTTP Web Service|2013|
|Core action|Build dictionary|2013|
|Core action|Count items in a dictionary|2013|
|Core action|Get an item from a dictionary|2013|
|Core action|Set time portion of date/time field|2010, 2013|
|Core action|Stop workflow|2010|
|List action|Copy document|2010, 2013|
|List action|Wait for event in list item|2010, 2013|
|List action|Wait for field change in current item|2010, 2013|
|List action|Translate document|2013|
|List action|Declare record|2010|
|List action|Undeclare record|2010|
|List action|Set content approval Status|2010|
|List action|Delete drafts|2010|
|List action|Delete Previous Versions |2010|
|List action|Wait for the change in Document Check-out status|2010|
|Task action|Assign a form to a group |2010|
|Task action|Collect Data from a User |2010|
|Condition action|Person is a valid SharePoint user|2010, 2013|
|Coordination action|Start a List workflow |2013|
|Coordination action|Start a Site workflow |2013|
|Loop|Loop in time|2013|
|Loop|Loop with Condition|2013|
|Parallel|Parallel block|2010, 2013|
|Relational|Lookup manager of a user|2010|
|Document Set|Capture a version of the Document Set|2010|
|Document Set|Send document set to repository|2010|
|Document Set|Set content approval status for doc set|2010|
|Document Set|Start document set approval process|2010|


By default, the migration tool stops workflow migration and reports errors if there are one or more unsupported actions in the source workflow. You can let the tool continue the migration process by selecting “Convert to Compose action” option in the migration settings, “Handle Unsupported Action”. 


## Lookups

Lookups are used in many workflow actions. Lookup types include

- Lookup for string. It's used in text field, such as email “body” field, task “request” field.
- Lookup for user. It's used in user field, such as email “to” field, task “participant” field.

In Power Automate, “Dynamic content” is used to provide dynamic value, similar with lookup in workflow. 

### Lookup for string 

Supported lookups for string include:

- Get field value of current item
- Get value of a variable
- Get value of context
- Get field value of current list
- Get field value of another list
- Parameter collects data when this workflow is started manually

Unsupported lookups for string include:

- Get field value of associated task list
- Get field value of associated history list

### Lookup for user

Supported lookups for user include:

- User name. An Active Directory (AD) user in the workflow will be mapped to a Microsoft Entra user in migration Power Automate flow.

Unsupported lookups for user include:

- SharePoint group name
- Hierarchy manager

## Initiation Form Parameters

In the SharePoint Designer workflow, initiation form parameters can be configured for a manually started workflow. When workflows are run, these parameters are provided by the user, and their values are set as variables. After migration, initiation form parameters are converted to the inputs of the manual-triggered Power Automate flow.
