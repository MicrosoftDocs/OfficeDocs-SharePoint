---
title: "Migration Assessment Scan Master Pages"
ms.reviewer: 
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
ms.assetid: 487c6ff4-d087-4743-a786-e6b86c2a1223
description: "Learn how to mitigate issues with Master pages during migration."
---

# Migration Assessment Scan: Master Pages

Learn how to mitigate issues with Master pages during migration.
  
## Overview

During migration, the default master page shouldbe set on all sites that are migrated. This ensures that the site will render once the migration is complete as the content migration will not have a dependency on any custom master pages. If you have custom master pages assigned to sites, you will need to set the Master Page property on the new site after the migration has completed.
  
## Data Migration

> [!IMPORTANT]
> Custom master page files (\*.master) shouldn't be migrated to the new platform. The setting on the destination site will be set to the default master page. This process ensures the site will render after the migration. 
  
## Preparing for Migration

Review the report and determine where you can move away from custom master pages before you migrate. Plan and understand what post migration work will be necessary to use the customized file moving forward.
  
## Post Migration

If you decide to continue using the customized master page on the new platform, you will need to apply the master page setting and validate your customizations work on the new platform.
  
## Scan Result Reports

 **NonDefaultMasterPages-detail.csv** This scan report contains all the sites that have a custom master page applied. 
  
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
|WebUrl  <br/> |Url to the subsite that has the master page setting configured.  <br/> |
|WebTitle  <br/> |Title of the impacted subsite.  <br/> |
|MasterPageUrl  <br/> |Server relative path to the master page referenced by the MasterPageUrl property.  <br/> |
|CustomMasterPageUrl  <br/> |Server relative path to the master page referenced by the CustomMasterPageUrl property.  <br/> |
|ScanID  <br/> |Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool.  <br/> |
   

