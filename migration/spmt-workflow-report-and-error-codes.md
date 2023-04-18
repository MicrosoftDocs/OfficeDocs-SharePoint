---
ms.date: 12/02/2021
title: "SPMT Workflow migration report and error codes"
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
description: "Learn about the report generated when migrating SharePoint Server workflows using SPMT and the error codes that may surface."
---

# Migration workflow report and error codes


## Workflow migration reports

The work migration task generates two reports, one for scans and the other for the migration.  These reports will saved to the  *WF_xxx/Report/TaskReport_xxx/*  folder. 

- Workflow scans: **WorkflowScanReport.csv**
- Workflow migrations: **WorkflowMigrationReport.csv**



|Report column name|Notes|
:-----|:-----|
|Source association URL|Source SharePoint object URL that is associated with the workflow. It can be URL of list, library, site |
|Destination association URL|Destination SharePoint object URL that is associated with the migrated Power Automate flow. It can be the URL of a list or library.|
|Source workflow URL|Location of the source workflow.|
|Destination workflow URL|The location where the workflow will be migrated.|
|Source workflow ID ||
|Destination flow ID||
|Source workflow name||
|Destination flow name ||
|Solution name|The name of Power Automate solution that contains migrated flows. Flow owner can find migrated flows in the solution. |
|Source workflow owner|The creator of source workflow instance|
|Destination flow owner|The owner(s) of migrated Power Automate flow|
|Association type|Possible values: List, Site, or Content type|
|Workflow version|Possible values: Workflow2010, Workflow2013|
|Workflow template name||
|Workflow accessed date|Latest execution/modification date of the workflow|
|Total action count|The count of actions for SPD workflow|
|Unsupported actions|List of actions which are not supported by migration tool|
|Status|Possible values: Migrated, Failed, or Skipped, Scan Finished.|
|Result category |Possible values: Migrated, Scan Finished, SCAN FILTER, MIGRATION SKIP, SCAN FAILURE, FLOW CREATE FAILURE|
|Message|Error message|
|Error code||


## Workflow migration errors

When a scan or migration fails with either a *SCAN FAILURE* or *FLOW CREATE FAILURE*, the error message and code are provided in the report. 

|Error message|Error code|Suggested action|
|:-----|:-----|:-----|
|SharePoint workflow scan unknown error.|0x02110001||
|SharePoint workflow subscription found without a workflow definition.|0x02110002|Confirm the workflow has valid definition|
|SharePoint workflow parse unknown error.|0x02110011||
|SharePoint workflow parse initial variables failed.|0x02110012||
|SharePoint workflow parse activities failed.|0x02110013||
|SharePoint workflow definition cannot be loaded.|0x02110014|Confirm the workflow has valid definition|
|SharePoint workflow association data cannot be loaded.|0x02110015|Check your workflow and associate it with a list or library|
|SharePoint workflow parse initial operator failed.|0x02110016||
|SharePoint workflow template is not supported.|0x02110021||
|SharePoint workflow associated with a site or site level content type is not supported.|0x02110022||
|SharePoint workflow cannot convert to cloud flow because some variables are not supported.|0x02110023||
|SharePoint workflow cannot convert to cloud flow because some actions are not supported.|0x02110024||
|Workflow migration failed because of unsupported variables or activities.|0x02110024||
|Workflow stage is not supported. It may contain circle stage dependency in the flow definition.|0x02110025||
|SharePoint Workflow definition contains unsupported actions.|0x02110026|You can select "Convert to compose action" in settings, and try migration again to convert unsupported action to compose.|
|Not all dependencies used in SharePoint workflow are resolved.|0x02110041|Resolve dependencies (user or list), then retry migration.|
|Lookup list used in SharePoint workflow cannot be mapped to target list.|0x02110042|Migrate the lookup list to SPO, then retry migration.|
|Cannot get flow owner's AAD id.|0x02110044|Map flow owner to a valid AAD user, then retry migration.|
|SharePoint workflow is filtered out because its association list or content type is out of migration scope.|0x02210031|If you migrate workflows of a single list, try to perform workflow migration of its site. If the workflow is associated to a content type, manually create the content type on SPO list or library and try workflow migration again.|
|SharePoint workflow is filtered out because no new instances are allowed.|0x02210032|Confirm the workflow is still in use. If you want to continue the migration, reactivate the workflow.|
|SharePoint workflow is filtered out because no SharePoint object is associated.|0x02210033|Check your workflow and associate it with a list or library|
|SharePoint workflow is filtered out because no triggers are configured.|0x02210034|Confirm the workflow is still in use. If you want to continue the migration, please reactivate the workflow.|
|SharePoint workflow is filtered out because it is a draft, please publish it and try to migrate it again.|0x02210035|Please publish your workflow and try migration again.|
|Workflow migration failed.|0x02810051||
|Workflow migration failed because flow owner is not found.|0x02810052|Check the user mapping file or AAD lookup to make workflow owner can be mapped to a AAD user.|
|Workflow migration failed because flow approvers are not found.|0x02810053|Check the user mapping file or AAD lookup to make sure the approver in Workflow can be mapped to a AAD user.|
|Workflow migration failed because association data is missing.|0x02810054|Check your workflow and associate it with a list or library and check OOTB workflow include necessary data.|
|SharePoint workflow is skipped because it has been migrated before.|0x02810055||
|Unable to create flow.|0x02810061||
|Cannot find the Flow owner in CDS|0x02810062|Please make sure flow owner existed in Power Platform.|
|Invalid parameters to create flows. Please contact with Microsoft for details.|0x02810063||
|No flow is going to be created. Please contact with Microsoft for details.|0x02810064||
|Fails to detect the endpoints of the BAP environment|0x02810065|Please make sure your custom endpoint file is valid.|
|Cannot access BAP environment|0x02810066|Please make migrator user can access Business Applications Platform.|
|Unable to get Power Platform's default environment.|0x02810067|Check if tenant has power automate license and if database is created|
|Cannot access CDS|0x02810068|Please make migrator user can access Common Data Service.|
|Unable to create CDS user because cannot fetch the business unit in CDS|0x02810070|You can create flow owner user manually in power platform admin center. Assign Basic User and Environment Maker security role to this user. Then migrate the workflow again.|
|Unable to create CDS user because cannot detect the built-in roles in CDS|0x02810071|Retry migration|
|Unable to fetch existing flows from the environment|0x02810072|You can create flow owner user manually in power platform admin center. Assign Basic User and Environment Maker security role to this user. Then migrate the workflow again.|
|Unable to create user in Power Platform's default environment.|0x02810073|You can create flow owner user manually in power platform admin center. Assign Basic User and Environment Maker security role to this user. Then migrate the workflow again.|
|Unable to get the publisher|0x02810074|Retry migration|
|Unable to publish solution.|0x02810075|Retry migration|
Workflow migration failed possibly because flow owner missing environment maker role.|0x02810076|Flow owner did not meet the role prerequisite, please make sure flow owner have Basic User and Environment Make role.|

