---
title: "Migration Assessment Scan Workflow Running Solutions 2010"
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
ms.assetid: 479f89dc-f6ba-4252-a72e-5cf1d02946ac
description: "Learn about issues migrating workflows that are in progress."
---

# Migration Assessment Scan: Workflow Running Solutions 2010

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

The following table describes the columns in the **WorkflowRunning2010-detail.csv** report.

|Column|Description|
|---|---|
|SiteID|Unique identifier of the impacted site collection.|
|SiteURL|URL to the impacted site collection.|
|SiteOwner|Owner of the site collection.|
|SiteAdmins|List of people listed as site collection administrators.|
|SiteSizeInMB|Size of the size collection in megabytes [MB]|
|NumOfWebs|Number of webs that exist in the site collection.|
|ContentDBName|Name of the content database hosting the site collection|
|ContentDBServerName|SQL Server hosting the content database.|
|ContentDBSizeInMB|Size of the content database hosting the site collection.|
|LastContentModifiedDate|Date/Time the site collection had content modified.|
|TotalItemCount|Total number of items found in the site collection.|
|Hits|Number of requests logged for the site collection. Relies on data from the usage logging service. If the usage logging service is disabled this row will show N/A.|
|DistinctUsers|Number of distinct users that have accessed the site collection. Relies on data from the usage logging service. If the usage logging service is disabled this row will show N/A.|
|DaysOfUsageData|Number of days the usage logging service retains data. This provides context for Hits and DistinctUsers. For example, if this is 14 days, the Hits and DistinctUsers data is for the last 14 days.|
|WorkflowName|Name of the workflow|
|ItemURL|URL to the item the workflow was started against. <br/> If this is a **site workflow**, the URL will point to the site. <br/> If this is a **list item workflow**, the URL will point to the list item.|
|Scope|Either Site or List.|
|WorkflowInitiator|User that started the workflow.|
|ScanID|Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool.|
