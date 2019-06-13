---
title: "Migration Assessment Scan Large Excel Files"
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
ms.assetid: 359d684a-65bf-4345-8b98-b169a2474ed2
description: "Learn how to mitigate issues with large Excel files during migration."
---

# Migration Assessment Scan: Large Excel Files

Learn how to mitigate issues with large Excel files during migration.
  
## Overview

The maximum limit for opening XLSX files in the browser is 10MB in the target environment. This setting is configurable in the source environment which may result in a change in behavior for your users. If you attempt to open a file larger than 10MB from a SharePoint site, it will prompt you to open the file in the Excel client application.
  
## Data Migration

XLSX files will be migrated.
  
> [!IMPORTANT]
> Any site that is configured as "No Access" (locked), in SharePoint will be skipped. To see a list of locked site collections see the Locked Sites scan output. 
  
## Preparing for Migration

Notify users of the expected behavior.
  
## Post Migration

Attempting to open an XLSX file larger than 10MB will prompt you to open the file in the Excel client. You will be prompted with a dialog.
  
## Scan Result Reports

 **LargeExcelFiles-detail.csv** This scan report contains all the XLSX files that are over 10MB in size. 
  
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
|File  <br/> |URL to the XLSX file.  <br/> |
|FileSizeinMB  <br/> |Size of the XLSX file in MB.  <br/> |
|ScanID  <br/> |Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool.  <br/> |
   

