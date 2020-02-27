---
title: "Migration Assessment Scan Managed Metadata Columns"
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
localization_priority: Priority
ms.collection:
- IT_SharePoint_Hybrid_Top
- IT_Sharepoint_Server_Top
- Strat_SP_gtc
- SPMigration
- M365-collaboration
ms.custom:
ms.assetid: 787812c2-8742-40c3-bd74-c7df9846c0b0

---

# Migration Assessment Scan: Managed Metadata Columns

## Overview

In SharePoint it is possible to add a Managed Metadata column to a list and populate the list field with values from the Managed Metadata Service Application. Migration of these columns requires coordination with migration of the Managed Metadata Service Application data.
  
## Data Migration

Managed metadata columns are typically migrated, but support will depend on the migration tooling you select.
  
> [!IMPORTANT]
> Any site that is configured as "No Access" (locked), in SharePoint will be skipped. To see a list of locked site collections see the Locked Sites scan output. 
  
## Preparing for Migration

Prior to migration, you want to understand how many lists leverage Managed Metadata and you will want to try to migrate these as close to the time you migrate your Managed Metadata Service Application data to the cloud.
  
## Post Migration

If migrating managed metadata columns is supported in the migration tooling you have chosen, you will want to ensure that the lists using the columns migrated and is properly configured to create and edit list items.
  
## Scan Result Reports

The following table describes the columns in the **ManagedMetadataLists-detail.csv** report. This scan report includes all lists that contain Managed Metadata columns. 
  
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
|DaysOfUsageData  <br/> |Number of days the usage logging service retains data. This provides context for Hits and DistinctUsers. For example, if this is 14 days, the Hits and DistinctUsers data is for the last 14 day  <br/> |
|ManagedMetadataColumns  <br/> |Semicolon delimited list of Managed Metadata columns associated with the list.  <br/> |
|WebURL  <br/> |Url to the web hosting the list.  <br/> |
|ListTitle  <br/> |Title of the list that contains managed metadata columns.  <br/> |
|ListURL  <br/> |URL to the list that contains managed metadata columns.  <br/> |
|ListItemCount  <br/> |Number of items in the impacted list.  <br/> |
|ListTemplate  <br/> |List template associated with the impacted list.  <br/> |
|ListType  <br/> |List type of the impacted list.  <br/> |
|ListCreator  <br/> |Account that created the list.  <br/> |
|ItemLastModifiedDate  <br/> |Date/Time the list had an item modified.  <br/> |
|ScanID  <br/> |Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool.  <br/> |
   

