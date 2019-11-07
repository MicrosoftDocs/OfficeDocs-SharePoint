---
title: "Migration Assessment Scan Email Enabled Lists"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.date: 9/12/2017
audience: ITPro
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
ms.assetid: a15bae85-86b3-4098-9bbd-631638d377b2
description: "Learn how to mitigate issues with Email Enabled Lists during migration."
---

# Migration Assessment Scan: Email Enabled Lists

Learn how to mitigate issues with Email Enabled Lists during migration.
  
## Overview

On the source environment it is possible to configure lists that can accept incoming email. This feature is not available on the target environment.
  
## Data Migration

The contents in the libraries listed in the report will migrate, but new emails sent to the library will no longer automatically show up as the library will no longer accept incoming emails.
  
> [!IMPORTANT]
> Any site that is configured as "No Access" (locked), in SharePoint will be skipped. To see a list of locked site collections, see the Locked Sites scan output. 
  
## Preparing for Migration

Communicate with end users that email will no longer show up in the target environment.
  
## Post Migration

Communicate with end users that email will no longer show up in the target environment.
  
## Scan Result Reports

The following table describes the columns in the **EmailEnabledLists-detail.csv** report.﻿ 
  
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
|WebURL  <br/> |Url to the web hosting the email enabled list  <br/> |
|ListTitle  <br/> |Title of the email enabled lists  <br/> |
|ListURL  <br/> |URL to the root of the email enabled list  <br/> |
|ListItemCount  <br/> |Number of items in the list  <br/> |
|ListTemplate  <br/> |Template used when creating the list  <br/> |
|ListType  <br/> |Type associated with the list  <br/> |
|ListCreator  <br/> |User that created the list  <br/> |
|ItemLastModifiedDate  <br/> |Date that an item in the list was modified  <br/> |
|ScanID  <br/> |Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool.  <br/> |
   

