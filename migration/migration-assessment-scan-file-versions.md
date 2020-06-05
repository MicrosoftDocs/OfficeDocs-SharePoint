---
title: "Migration Assessment Scan File Versions"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.date: 9/12/2017
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
ms.assetid: e847ee5e-342b-45a1-94c1-89244f81bef4
description: "Learn how to fix issues with file versions during migration."
---

# Migration Assessment Scan: File Versions

Learn how to fix issues with file versions during migration.
  
## Overview

Versions have historically impacted the length of a migration for a given site in a linear fashion. The more versions you have, the longer it will take to migrate a given site.
  
## Data Migration

By default, versioning is enabled for all lists and libraries on the target platform. In the destination SPO site, there is no limit when versioning is enabled.
  
> [!IMPORTANT]
> Any site that is configured as "No Access" (locked), in SharePoint will be skipped. To see a list of locked site collections see the Locked Sites scan output. 
  
## Preparing for Migration

Examine the report and determine if preserving versions is needed or not for your business.
  
## Post Migration

Site owners should validate their version information was migrated as expected.
  
## Scan Result Reports

The following table describes the columns in the **FileVersions-detail.csv** report. 
  
This scan report provides a list of all the files in the environment that have versions.
  
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
|SiteURL  <br/> |URL to the site collection.  <br/> |
|SiteOwner  <br/> |Site collection owner.  <br/> |
|VersionCount  <br/> |Number of versions the items have.  <br/> |
|File  <br/> |File that the versions are associated with.  <br/> |
|ScanID  <br/> |Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool.  <br/> |
   

