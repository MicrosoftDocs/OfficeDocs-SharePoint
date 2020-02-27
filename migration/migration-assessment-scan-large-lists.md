---
title: "Migration Assessment Scan Large Lists"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.date: 11/23/2017
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
localization_priority: Priority
ms.collection:
- IT_SharePoint_Hybrid_Top
- IT_Sharepoint_Server_Top
- Strat_SP_gtc
- SPMigration
- M365-collaboration
ms.custom:
ms.assetid: a10f6067-5cbe-4eb4-82f8-d57be628a3f6
description: "Learn how to mitigate issues with Large Lists during migration."
---

# Migration Assessment Scan: Large Lists

Learn how to mitigate issues with Large Lists during migration.
  
## Overview

Lists over 20,000 items have historically caused issues with the migration tooling, making the ability to predict the time it takes to migrate sites that contain a larger list to be problematic.
  
## Data Migration

List data is migrated. However, the larger the list the more unpredictable the migration process has proven. Extremely large lists can result in an extended migration.
  
> [!NOTE]
> Any site that is configured as "No Access" (locked), in SharePoint will be skipped. To see a list of locked site collections see the Locked Sites scan output. 
  
## Preparing for Migration

Investigate the large lists and determine the need for this content to be migrated to the target environment.
  
## Post Migration

The migration tooling has built-in validation to ensure all the list items are migrated. You will want to validate the large lists migrated as expected.
  
## Scan Result Reports

 **LargeLists-detail.csv** This scan report provides all lists that have over 20,000 items. 
  
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
|WebURL  <br/> |Url to the subsite that contains the list.  <br/> |
|ListTitle  <br/> |Title of the list.  <br/> |
|ListURL  <br/> |Url to the root folder of the list.  <br/> |
|ListItemCount  <br/> |Number of items in the list.  <br/> |
|ListTemplate  <br/> |Template used when creating the list.  <br/> |
|ListType  <br/> |The type of list configured.  <br/> |
|ListCreator  <br/> |User that created the list.  <br/> |
|ItemLastModifiedDate  <br/> |Date/Time an item was last modified on the list.  <br/> |
|ScanID  <br/> |Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool.  <br/> |
   

