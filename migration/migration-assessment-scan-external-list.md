---
title: "Migration Assessment Scan External List"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.date: 12/6/2017
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
ms.assetid: de809b30-8e4d-4223-b47e-81912d617dd1
ms.collection:
- SPMigration
- M365-collaboration
---

# Migration Assessment Scan: External List

## Overview

External lists are those lists that were created from a Business Catalogs Services [BCS] application. These are lists that appear to be SharePoint Lists, but are actually backed by an external datasource. For example, you could have a list that is showing data from an external SQL Server or Web Service.
  
## Data Migration

BCS applications are not migrated to the target environment. As a result, External Lists are not migrated.
  
See [Migration Assessment Scan: BCS](migration-assessment-scan-bcs.md) for more information about BCS. 
  
> [!IMPORTANT]
> Any site that is configured as "No Access" (locked), in SharePoint will be skipped. To see a list of locked site collections see the Locked Sites scan output. 
  
## Preparing for Migration

Build out a plan for the external lists. It is possible to configure Hybrid BCS to access on-premises data from SharePoint in Microsoft 365, but this will require some planning. 
  
See [Migration Assessment Scan: BCS](migration-assessment-scan-bcs.md) for more information about BCS 
  
## Post Migration

Ensure that your solutions, which rely on the BCS applications, function with the newly deployed BCS applications.
  
## Scan Result Reports

The following table describes the columns in the **ExternalLists-detail.csv** report. This scan report provides a list of all the external lists in the environment. 
  
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
|ListTitle  <br/> |Title of the list.  <br/> |
|ListURL  <br/> |Url to the root folder of the list.  <br/> |
|ListItemCount  <br/> |Number of items in the list.  <br/> |
|ListTemplate  <br/> |Template used when creating the list.  <br/> |
|ListType  <br/> |The type of list configured.  <br/> |
|ListCreator  <br/> |User that created the list.  <br/> |
|ItemLastModifiedDate  <br/> |Date/Time an item was last modified on the list.  <br/> |
|ScanID  <br/> | Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool.  <br/> |
   

