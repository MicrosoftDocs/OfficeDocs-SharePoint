---
title: "Migration Assessment Scan Publishing Sites"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.date: 9/12/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Priority
ms.collection:
- IT_SharePoint_Hybrid_Top
- IT_Sharepoint_Server_Top
- Strat_SP_gtc
- SPMigration
- M365-collaboration
ms.custom:
ms.assetid: 33af6b99-4b90-4edd-8ff7-e8fe2f288d3d

---

# Migration Assessment Scan: Publishing Sites

## Overview

Publishing sites are typically customized intranet sites that rely on page layouts to allow end users to quickly create articles that are published to end users. Due to the high level of customizations that are involved with publishing sites, they may be difficult to migrate to SPO without a lot of remediation.
  
## Data Migration

The content in the publishing site may migrate, but any customization typically requires an extensive amount of remediation effort.
  
> [!IMPORTANT]
> Any site that is configured as "No Access" (locked), in SharePoint will be skipped. To see a list of locked site collections see the Locked Sites scan output. 
  
## Preparing for Migration

Test migration of the sites with the publishing features enabled. Understand what will need to be corrected post migration.
  
## Post Migration

Apply the fixes to your customized content post migration.
  
## Scan Result Reports

The following table describes the columns in the **P-detail.csv** report. This scan report provides a list of all the add-ins installed in the environment. 
  
|**Column**|**Description**|
|:-----|:-----|
|SiteId  <br/> |Unique identifier of the impacted site collection.  <br/> |
|SiteURL  <br/> |URL to the impacted site collection.  <br/> |
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
|PublishingInfrastructureEnabled  <br/> |True if the site collection level Publishing Infrastructure feature is enabled. This will only be True if the site is the root site in the site collection.  <br/> |
|PublishingEnabled  <br/> |True if the site level Publishing Feature is enabled.  <br/> |
|ScanID  <br/> |Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool.  <br/> |
   

