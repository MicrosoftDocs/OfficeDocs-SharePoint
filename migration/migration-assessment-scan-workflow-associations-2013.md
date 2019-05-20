---
title: "Migration Assessment Scan Workflow Associations 2013"
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.date: 9/13/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Priority
ms.collection:
- IT_SharePoint_Hybrid_Top
- IT_Sharepoint_Server_Top
- Strat_SP_gtc
ms.custom:
ms.assetid: 59e80c9a-2543-43b4-9d4d-d758465c2e71
description: "Learn how to fix issues with that occur with Workflow Associations 2013 during migration."
---

# Migration Assessment Scan: Workflow Associations 2013

Learn how to fix issues with that occur with Workflow Associations 2013 during migration.
  
## Overview

When content is migrated from the SharePoint source environment to the new target environment there are two types of workflows that could be involved, depending on their use in the current farm.
  
Workflows that were created using the workflow service that was available in SharePoint 2010 and are still in use on the source environment will be migrated to the new farm and will continue to work as expected.
  
SharePoint source farms may run Workflow 2013 using a version of the Workflow Manager. As a result, when content is moved from the source environment to the target environment, there is a process to migrate Workflow 2013 over to the Azure instance of the Workflow Manager.
  
## Data Migration

Workflow Data is divided into two parts:
  
- **Workflow Definition:** The definition describes the overall workflow process, e.g. a three stage approval workflow with custom routing rules for each stage. This data lives in O365 and will be migrated with the rest of the O365 data and will be available in your target environment. 
    
- **Workflow Instances:** Each running instance of a workflow definition maintains the state of the workflow, e.g. this document is in Stage Two of the approval process and is assigned to John Doe. This data lives in the Azure Workflow Manager. Unfortunately, the Azure team does not have the technology to migrate Workflow Manager data from the current source environments to Azure instances. The result of this will be the loss of all running workflow instances. For example, a document that was in Stage Two of a workflow in the source environment will be back to Stage Zero (workflow not started) post migration to the target environment. 
    
> [!IMPORTANT]
> Any site that is configured as "No Access" (locked), in SharePoint will be skipped. To see a list of locked site collections see the Locked Sites scan output. 
  
## Preparing for Migration

To avoid unnecessary workflow restarts it is best to complete in-flight workflows before the migration event when your content is moved to the target environment. If the feature is in use in the source environment today you can receive a list of running instances of workflows prior to the migration event, so that you can communicate this status to your site owners.
  
## Post Migration

Once the migration is complete, all users will need to restart any workflows that were still in flight. In some extreme cases, it may be necessary to recreate a workflow if the tooling is unable to migrate it.
  
## Scan Result Report

 **WorkflowAssociations2013-detail.csv** This scan report contains source workflow definitions and where they are associated in the site. Workflow definitions come across in the migration, so this gives some visibility into the workflow footprint in the farm. 
  
|**Column**|**Description**|
|:-----|:-----|
|SiteId  <br/> |Unique identifier of the impacted site collection.  <br/> |
|SiteURL  <br/> |URL to the impacted site collection.  <br/> |
|SiteOwner  <br/> |Owner of the site collection.  <br/> |
|SiteAdmins  <br/> |List of people listed as site collection administrators.  <br/> |
|SiteSizeInMB  <br/> |Size of the size collection in megabytes [MB]  <br/> |
|NumOfWebs  <br/> |Number of webs that exist in the site collection.  <br/> |
|ContentDBName  <br/> |Name of the content database hosting the site collection.  <br/> |
|ContentDBServerName  <br/> |SQL Server hosting the content database.  <br/> |
|ContentDBSizeInMB  <br/> |Size of the content database hosting the site collection.  <br/> |
|LastContentModifiedDate  <br/> |Date/Time the site collection had content modified.  <br/> |
|TotalItemCount  <br/> |Total number of items found in the site collection.  <br/> |
|Hits  <br/> |Number of requests logged for the site collection. Relies on data from the usage logging service. If the usage logging service is disabled this row will show N/A.  <br/> |
|DistinctUsers  <br/> |Number of distinct users that have accessed the site collection. Relies on data from the usage logging service. If the usage logging service is disabled this row will show N/A.  <br/> |
|DaysOfUsageData  <br/> |Number of days the usage logging service retains data. This provides context for Hits and DistinctUsers. For example, if this is 14 days, the Hits and DistinctUsers data is for the last 14 days.  <br/> |
|Scope  <br/> |Either List or Site. This is the level that the workflow will run at. It should help the site owner locate the impacted workflow definitions.  <br/> |
|RunningInstances  <br/> |Number of running instances linked to this workflow association.  <br/> |
|WebUrl  <br/> |Url to the subsite.  <br/> |
|ListTitle  <br/> |If the workflow is associated with a list, this will display the title of that list.  <br/> |
|ListUrl  <br/> |If the workflow is associated with a list, this will display the url to the root of the list.  <br/> |
|IsReusable  <br/> |True/False. Identifies which workflows were published as reusable workflows.  <br/> |
|WorkflowAssociationName  <br/> |Display name given to the workflow association.  <br/> |
|WorkflowDescription  <br/> |Description given to the workflow association.  <br/> |
|WorkflowPublishedBy  <br/> |Identity of the account used to publish the workflow.  <br/> |
|WorkflowAssociationID  <br/> |Unique identifier for the workflow association.  <br/> |
|EmailActivityExists  <br/> |True if there are email activities contained in the workflow. It may be necessary to fix up the identities in the email activities post migration.  <br/> |
|ConditionalRuleExists  <br/> |True if there are conditional rules contained in the workflow. It may be necessary to fix up the identities in the conditional rules post migration.  <br/> |
|WorkflowFileCheckedOut  <br/> |True if the workflow files are checked out. Checked out files will not migrate.  <br/> |
|ScanID  <br/> |Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool.  <br/> |
   

