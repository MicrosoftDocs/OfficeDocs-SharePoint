---
title: "Migration Assessment Scan List Items with Audience Targeting"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.date: 7/23/2018
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

---

# Migration Assessment Scan: List Items with Audience Targeting

## Overview

In SharePoint it is possible to enable Audience Targeting on a list or library. After this feature is enabled users are able to target audiences on a given list item. Unfortunately during a migration from On-Premises SharePoint to SharePoint Online, the list and list item audience data will not migrate. This report will contain all the list items in the environment that are targeting audiences.

  
## Data Migration

The audience targeting data will not migrate.
  
> [!IMPORTANT]
> Any site that is configured as "No Access" (locked), in SharePoint will be skipped. To see a list of locked site collections see the Locked Sites scan output. 
  
## Preparing for Migration

Leverage the report to understand the audiences that are being used to target list content to users. If this functionality is needed after migration to SharePoint Online, plan for the remediation of impacted content. This will involve creating new audiences in SharePoint Online environment and fixing the impacted list items post migration.
  
## Post Migration

Implement your remediation plan for the impacted content that was decided during Preparing for Migration.

  
## Scan Result Reports

The following table describes the columns in the **ListItemsWithAudienceTargeting-detail.csv** report.
This scan report provides a list of all the add-ins installed in the environment.

  |**Column**|**Description**|
|:-----|:-----|
|SiteId |Unique identifier of the impacted site collection. |
|SiteURL |URL to the impacted site collection. |
|SiteOwner |Owner of the site collection. |
|SiteAdmins |List of people listed as site collection administrators. |
|SiteSizeInMB |Size of the size collection in megabytes [MB] |
|NumOfWebs |Number of webs that exist in the site collection. |
|ContentDBName |Name of the content database hosting the site collection. |
|ContentDBServerName |SQL Server hosting the content database. |
|ContentDBSizeInMB |Size of the content database hosting the site collection. |
|LastContentModifiedDate|Date/Time the site collection had content modified. |
|TotalItemCount |Total number of items found in the site collection. |
|Hits |Number of requests logged for the site collection. Relies on data from the usage logging service. If the usage logging service is disabled this row will show N/A. |
|DistinctUsers |Number of distinct users that have accessed the site collection. Relies on data from the usage logging service. If the usage logging service is disabled this row will show N/A. |
|DaysOfUsageData |Number of days the usage logging service retains data. This provides context for Hits and DistinctUsers. For example, if this is 14 days, the Hits and DistinctUsers data is for the last 14 days.|
|WebUrl|Url to the web hosting the list.|
|ListTitle|Title of the list that contains list items that target audiences.|
|ListUrl|Url to the root of the list.|
|ListItemUrl|URL to the list item's display form.|
|TargetAudienceNames|List of audience names that this list item targets. If an audience name could not be resolved, the audience ID will be displayed. This can occur if the audience was deleted after it was used on the list item.|
|ScanId|Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool. |

   

