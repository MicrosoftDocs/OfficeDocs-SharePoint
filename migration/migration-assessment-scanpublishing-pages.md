---
title: "Migration Assessment Scan Publishing Pages"
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
ms.custom:
ms.assetid: 7f8e8ee7-c400-4530-a550-598c9bf33c44

---

# Migration Assessment Scan: Publishing Pages

## Overview

Publishing sites are typically customized intranet sites that rely on page layouts to allow end users to quickly create articles that are published to end users. Due to the high level of customization that is involved with publishing sites, they may be difficult to migrate to SharePoint Online without an extensive amount of remediation effort.
  
## Data Migration

The files can migrate however the pages may not function correctly on the new platform. The common causes are changes to SharePoint provided master pages, JavaScript, and CSS files.
  
> [!IMPORTANT]
> Any site that is configured as "No Access" (locked), in SharePoint will be skipped. To see a list of locked site collections see the Locked Sites scan output. 
  
## Preparing for Migration

Catalog the pages that leverage page layouts. Perform test migrations and plan for post migration remediation. You may find it's easier to start a new portal on SharePoint Online and archiving your on premises portal once that site is up and running.
  
## Post Migration

Apply the fixes to your page layouts and publishing pages post migration.
  
## Scan Result Reports

The following table describes the columns in the **PublishingPages-detail.csv** report. This scan report provides a list of all the add-ins installed in the environment. 
  
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
|PublishingPageURL  <br/> |Url to the publishing page.  <br/> |
|PageLayoutName  <br/> |Name of the page layout associated with the publishing page.  <br/> |
|PageLayoutURL  <br/> |Url to the page layout associated with the publishing page.  <br/> |
|ScanID  <br/> |Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool.  <br/> |
   