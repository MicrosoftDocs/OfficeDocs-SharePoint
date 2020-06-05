---
title: "Migration Assessment Scan Custom Permission Level"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.date: 12/14/2017
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
ms.assetid: 617ba8f7-eff1-4fcb-b9b8-ee5ef459a18c
ms.collection:
- SPMigration
- M365-collaboration
---

# Migration Assessment Scan: Custom Permission Level

## Overview

In SharePoint, it is possible to create a custom permission level and then assign that permission level to users and groups. Some migration tools will have problems moving this information to SharePoint Online. As a result, permissions will not be the same for impacted users and groups post migration.
  
For more information on permission levels, see [Understanding permission levels in SharePoint](/sharepoint/understanding-permission-levels).
  
## Data Migration

With some tooling, this data is not migrated. It is recommended to use the permission levels provided by SharePoint. However, if custom permission levels are required, the permission levels would need to be manually recreated on the SharePoint Online sites.
  
> [!IMPORTANT]
> Any site that is configured as "No Access" (locked), in SharePoint will be skipped. To see a list of locked site collections see the Locked Sites scan output. 
  
## Preparing for Migration

Understand the custom permission levels in use in your source environment and determine the plan to move forward. Either move users and groups to the default SharePoint permission levels, or build out a plan for creating the custom permission levels and fixing permissions post migration.
  
## Post Migration

Validate the users and groups have the correct permission levels. If you needed to create custom permission levels, ensure those are functioning as expected.
  
## Scan Result Reports

The following table describes the columns in the **CustomPermissionLevel-detail.cs** v report. This scan report provides a list of all the custom permission levels in the environment. 
  
|**Column**|**Description**|
|:-----|:-----|
|SiteId  <br/> |Unique identifier of the impacted site collection.  <br/> |
|SiteURL  <br/> |URL to the impacted site collection.  <br/> |
|WebApplicationURL  <br/> |URL of the Web Application hosting the site collection.  <br/> |
|SiteOwner  <br/> |Owner of the site collection.  <br/> |
|SiteAdmins  <br/> |List of people listed as site collection administrators  <br/> |
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
|WebURL  <br/> |Url to the site that has publishing features enabled.  <br/> |
|PermissionLevelName  <br/> |Name of the custom permission level.  <br/> |
|PermissionLevelDescription  <br/> |Description of the custom permission level.  <br/> |
|Permission LevelURL  <br/> |Url to the custom permission level.  <br/> |
|ScanID  <br/> |Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool.  <br/> |
   

