---
title: "Migration Assessment Scan Checked-out files"
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
ms.assetid: 43ca2e32-1ed7-4a4b-a575-7573b435594b
description: "Learn about issues with checked-out files during data migration."
---

# Migration Assessment Scan: Checked-out files

Learn about issues with checked-out files during data migration.
  
## Overview

Migration reads the source SharePoint farm using an account that has Full Read access to the environment. If a file is checked out by a user, the migration tooling is not able to read the checked out file. However, the migration tooling will see the last checked in version of the file instead. To avoid losing data, users should check-in their files prior to their site migrating.
  
## Data Migration

Only checked-in content will be migrated. To avoid any potential data loss, encourage users to check in their files prior to migration. A site administrator can check-in a file for a user, however only the content that was saved to SharePoint by the user would be migrated - if a user downloaded the file and was working on it outside of SharePoint, those changes would not appear post check-in.
  
> [!IMPORTANT]
> Any site that is configured as "No Access" (locked), in SharePoint will be skipped. To see a list of locked site collections see the Locked Sites scan output. 
  
## Preparing for Migration

Users should ensure that their content is checked-in prior to the migration date provided.
  
## Post Migration

Site owners performing user acceptance testing (UAT) on their content should validate that their sites migrated correctly.
  
## Scan Result Reports

The following table describes the columns in the **CheckedOutFiles-detail.csv** report. 
  
This scan report provides a view of the files that are checked out and which user has the files checked out at the time the scan was executed.
  
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
|File  <br/> |File that is chekced out.  <br/> |
|CheckedOutUser  <br/> |User that has the file checked out.  <br/> |
|ScanID  <br/> |Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool.  <br/> |
   

