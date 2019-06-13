---
title: "Migration Assessment Scan Unsupported Site Templates"
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
ms.assetid: 7cd48080-1e02-443b-9e3d-8361b2903959
description: "Learn how to fix issues with Unsupported Site Templates during migration."
---

# Migration Assessment Scan: Unsupported Site Templates

Learn how to fix issues with Unsupported Site Templates during migration.
  
## Overview

Every SharePoint site is based on a site template. In the SharePoint source environment, it was possible to create site collections using a variety of default templates as well as templates deployed via Full Trust Code (FTC). However, site collections that are supported for migration are the Team Site and Personal Site templates. The Personal Site Template is used for creating OneDrive for Business sites.
  
Supported Site Templates:
  
|**Template Friendly Name**|**Template**|**ID**|
|:-----|:-----|:-----|
|TeamSite  <br/> |STS  <br/> |1  <br/> |
|Personal Site  <br/> |SPSPERS  <br/> |21  <br/> |
   
## Data Migration

Any site that is not using a Team Site or Personal Site template should be mapped to the Team Site template during migration. The content from the source environment is then copied into the new Team Site on the target.
  
> [!IMPORTANT]
> Any site that is configured as "No Access" (locked), in SharePoint would be skipped. To see a list of locked site collections see the Locked Sites scan output. 
  
## Preparing for Migration

Leverage the scan report for Unsupported Site Templates to identify site collections that are impacted. The impacted site's content will be copied into a Team Site template during migration, but it is possible the Team Site template does not include the features/functionality of the source site.
  
## Post Migration

Validate that your sites work post migration.
  
## Scan Result Reports

 **UnsupportedWebTemplate-detail.csv** This scan report contains a list of sites that are currently using a site template that is not supported on the target platform. 
  
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
|FullURL  <br/> |URL to the impacted site.  <br/> |
|WebID  <br/> |ID for the site that is linked to the invalid site template.  <br/> |
|WebTitle  <br/> |Title for the impacted site.  <br/> |
|WebTemplateID  <br/> |ID for the site template that is not supported in the source environment.  <br/> |
|WebTemplate  <br/> |Friendly name for the site template. If this is empty, it indicates that the site template is no longer registered on the source environment.  <br/> |
|ScanID  <br/> |Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool.  <br/> |
   

