---
title: "Migration Assessment Scan Site Template Language"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.date: 9/20/2017
audience: ITPro
ms.topic: article
ms.service: sharepoint-online
localization_priority: Priority
ms.collection:
- IT_SharePoint_Hybrid_Top
- IT_Sharepoint_Server_Top
- SPMigration
- M365-collaboration
---

# Migration Assessment Scan: Site Template Language

## Overview

In SharePoint it is possible to install language packs and create sites leveraging multiple languages. During a migration, additional planning is required to validate sites that are not using a language familiar to the migration team.
  
## Data Migration

Site content will migrate, but validation of the content will require someone that speaks the language the content is in to confirm everything migrated correctly.
  
> [!IMPORTANT]
> Any site that is configured as "No Access" (locked), in SharePoint will be skipped. To see a list of locked site collections see the Locked Sites scan output. 
  
## Preparing for Migration

Plan to have appropriate resources available to perform user acceptance testing on the migrated content.
  
## Post Migration

Content experts will need to validate the migrated content.
  
## Scan Result Reports

The following table describes the columns in the SiteTemplateLanguage-detail.csv report. This scan report provides a list of all the add-ins installed in the environment. 
  
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
|WebURL  <br/> |Url to the site.  <br/> |
|Template  <br/> |Name of the template. This will show a number if SharePoint is unable to determine name of the site template.  <br/> |
|TemplateID  <br/> |ID associated with the site template. For example, 1 is associated with STS [Team Site].  <br/> |
|Locale  <br/> |Language associated with the site template. If you installed English SharePoint and created a Team Site, the Locale would show 1033.  <br/> |
|ScanID  <br/> |Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool.  <br/> |
   

