---
title: "Migration Assessment Scan Customized Pages"
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
ms.assetid: 55004bf2-5b96-4272-8f8f-970672fc84d4
description: "Learn how to mitigate issues with Customized Pages during migration."
---

# Migration Assessment Scan: Customized Pages

Learn how to mitigate issues with Customized Pages during migration.
  
## Overview

Customized files are out of the box SharePoint files that have been modified by a user. A common example is using a tool like SharePoint Designer to open a site and modify the default.aspx file of a site. During migration, these pages will be reverted to their uncustomized state.
  
Any file modified by the SharePoint System Account is excluded from the scan report.
  
For more information on customized files and how to reset a file back to the default, read the following article:
  
- [Customize a SharePoint page by using remote provisioning and CSS](https://msdn.microsoft.com/pnp_articles/customize-a-sharepoint-page-by-using-remote-provisioning-and-css)
    
## Data Migration

Customized files are reverted to their uncustomized state during migration.
  
> [!IMPORTANT]
> Any site that is configured as "No Access" (locked), in SharePoint will be skipped. To see a list of locked site collections see the Locked Sites scan output.
  
## Preparing for Migration

Notify the site collection owners of sites that contain customized pages that they will need to reapply any customizations made to impacted files post migration. Page owners should look for out of the box behavior to replace customization where possible.
  
## Post Migration

Site owners will need to reapply any customizations post migration.
  
## Scan Result Reports

The following table describes the columns in the **CustomizedPages-detail.csv** report. 
  
This scan report provides a list of all the customized files and who last modified them.
  
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
|ModifiedBy  <br/> |User that modified the file  <br/> |
|File  <br/> |File that was customized.  <br/> |
|ScanID  <br/> |Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool.  <br/> |
   

