---
title: "Migration Assessment Scan Workflow Associations 2010"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.date: 9/13/2017
audience: ITPro
ms.topic: article
ms.service: sharepoint-online
localization_priority: Priority
ms.collection:
- IT_SharePoint_Hybrid_Top
- IT_Sharepoint_Server_Top
- SPMigration
- M365-collaboration
ms.custom:
ms.assetid: ebf375f6-588f-4d5e-9126-e945aa31f7e2

---

# Migration Assessment Scan: Workflow Associations 2010

## Overview

The migration tooling is typically able to migrate the Workflow Definitions from the SharePoint source to the target environment. However, any in progress workflow instances are not migrated. As a result, in progress workflows are reset to appear as if they were never started on the destination.
  
## Data Migration

Workflow Data is divided into the following two parts:
  
- **Workflow Definition:** The definition describes the overall workflow process, e.g. a three stage approval workflow with custom routing rules for each stage. This data will typically be migrated with the rest of the site collection data and will be available in your target environment. 
    
- **Workflow Instances:** Each running instance of a workflow definition maintains the state of the in progress workflow, e.g. this document is in Stage Two of the approval process and is assigned to John Doe. Unfortunately, this information cannot be migrated to the new platform. The result of this will be the loss of all running workflow instances. For example, a document that was in Stage Two of a workflow in the source environment will be back at Stage Zero (workflow not started) post migration to the target environment. 
    
> [!IMPORTANT]
> Any site that is configured as "No Access" (locked), in SharePoint will be skipped. To see a list of locked site collections see the Locked Sites scan output. 
  
## Preparing for Migration

To avoid unnecessary workflow restarts it is best to complete in-flight workflows before the migration event when your content is moved to the target environment.
  
## Post Migration

Once the migration to the target environment is complete, users will need to restart any workflows that were still in flight. If the workflow contained identities, it may be necessary to republish the workflow using SharePoint Designer.
  
## Scan Result Reports

 **WorkflowAssociations2010-detail.csv** This scan report provides a list of all the 2010 workflow associations in the environment along with how many running instances at the time the scan was executed. 
  
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
|Scope  <br/> |Either List, ContentType, or Site. This is the level that the workflow is associated with.  <br/> |
|RunningInstances  <br/> |Number of workflows actively running at that scope.  <br/> |
|WebURL  <br/> |URL to the web that the workflow is associated with.  <br/> |
|ListTitle  <br/> |Title of the list the workflow is associated with. If the scope is Site, the value will be N/A.  <br/> |
|ListUrl  <br/> |Url to the list with the workflow association.  <br/> |
|ContentTypeName  <br/> |Name of the content type if the scope is ContentType.  <br/> |
|IsReusable  <br/> |True if the workflow association was published as a reusable workflow.  <br/> |
|ReusableScope  <br/> |Specifies the scope of the reusable workflow. Reusable or GlobalReusable.  <br/> |
|WorkflowName  <br/> |Name of the workflow association. This is the text that displays in SharePoint when starting the workflow.  <br/> |
|WorkflowDescription  <br/> |Description of the workflow association.  <br/> |
|HasCustomWorkflowActivity  <br/> |True if the workflow is using a custom workflow activity that was deployed via full trust solutions.  <br/> |
|WorkflowReferencedAssemblies  <br/> |Name of the assembly associated with a custom activity. Populated if HasCustomWorkflowActivity is True.  <br/> |
|SolutionNames  <br/> |Name of the full trust solution package the custom activity is associated with. Populated if HasCustomWorkflowActivity is True.  <br/> |
|WorkflowPublishedBy  <br/> |Name of the person that published the workflow.  <br/> |
|WorkflowID  <br/> |Unique identifier associated with the workflow.  <br/> |
|AddListItemPermissionsExist  <br/> |True if the workflow contains an action that adds list permissions. The activity embeds a users identity and may not function post migration without manual republish of the workflow.  <br/> |
|RemoveListItemPermissionsExists  <br/> |True if the workflow contains an action that removes list permissions. The activity embeds a users identity and may not function post migration without manual republish of the workflow.  <br/> |
|ReplaceListItemPermissionsExists  <br/> |True if the workflow contains an action that replaces list permissions. The activity embeds a users identity and may not function post migration without manual republish of the workflow.  <br/> |
|EmailActivityExists  <br/> |True if the workflow contains an action that sends email. The activity embeds a users identity and may not function post migration without manual republish of the workflow.  <br/> |
|ImpersonationExists  <br/> |True if the workflow contains an action that impersonates an account to perform an action. The activity embeds a users identity and may not function post migration without manual republish of the workflow.  <br/> |
|RulesFileExists  <br/> |True if the workflow contains conditional rules that contain identities. The activity embeds a users identity and may not function post migration without manual republish of the workflow.  <br/> |
|ContentAppovalExists  <br/> |True if the workflow contains content approval activities. The activity embeds a users identity and may not function post migration without manual republish of the workflow.  <br/> |
|WorkflowFileCheckedOut  <br/> |If the workflow file is checked out it will not migrate as expected.  <br/> |
|ScanID  <br/> |Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool.  <br/> |
   

