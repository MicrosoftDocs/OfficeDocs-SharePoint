---
title: "Migration Assessment Scan Workflow Running Solutions 2013"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: serdars
recommendations: true
ms.date: 9/13/2017
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.subservice: sharepoint-migration
ms.localizationpriority: high
ms.collection:
- IT_SharePoint_Hybrid_Top
- IT_Sharepoint_Server_Top
- SPMigration
- M365-collaboration
ms.custom:
ms.assetid: 36fbe716-131a-4f50-a5e7-7846e504b912
description: "Learn how to fix Workflow Running Solutions 2013 issues that occur during migration."
---

# Migration Assessment Scan: Workflow Running Solutions 2013

Learn how to fix Workflow Running Solutions 2013 issues that occur during migration.
  
## Overview

The migration is unable to migrate workflows that are in progress. If a workflow on a site or item is In Progress, it will appear as if the workflow was never started on the item prior to migration. If you have business critical workflows that are in progress prior to migration, it is recommended to finish the workflow prior to migration.
  
## Data Migration

Workflow definitions will migrate, however in progress workflow information will not be migrated.
  
> [!IMPORTANT]
> Any site that is configured as "No Access" (locked), in SharePoint will be skipped. To see a list of locked site collections see the Locked Sites scan output. 
  
## Preparing for Migration

Communicate with end users that in progress workflows will need to be restarted after migration.
  
## Post Migration

Communicate with end users that in progress workflows will need to be restarted after migration.
  
## Scan Result Reports

 **WorkflowRunning2013-detail.csv** This report contains all the running SharePoint 2013 workflow instances. 
  
|Column|Description|
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
|WorkflowName  <br/> |Name of the workflow  <br/> |
|ItemURL  <br/> |URL to the item the workflow was started against.  <br/> If this is a **site workflow**, the URL will point to the site.  <br/> If this is a **list item workflow**, the URL will point to the list item.  <br/> |
|Scope  <br/> |Either Site or List.  <br/> |
|WorkflowInitiator  <br/> |User that started the workflow.  <br/> |
|ScanID  <br/> |Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool.  <br/> |
   

