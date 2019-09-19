---
title: "Migration Assessment Scan Apps"
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
- SPMigration
ms.custom: 
ms.assetid: 2e57511d-07f0-4395-a795-11be19417c1a
description: "Learn how to mitigate issues with SharePoint add-ins during migration."
---

# Migration Assessment Scan: Apps

Learn how to mitigate issues with SharePoint add-ins during migration.
  
## Overview

Migrating SharePoint add-ins (formerly called apps) isn't supported in the target environment. The site content will be migrated, but the add-ins will not. As a result, once the site is migrated, the add-ins will need to be reinstalled. If you purchased the add-in, you will need to reclaim the license from the Add-in store.
  
## Data Migration

Site content will be migrated, but add-ins will need to be installed on the destination environment. If any add-ins stored data in the SharePoint App-web, that data will be orphaned and the add-in will be reinstalled cleanly.
  
> [!IMPORTANT]
> Any site that is configured as "No Access" (locked), in SharePoint will be skipped. To see a list of locked site collections see the Locked Sites scan output. 
  
## Preparing for Migration

Read through the provided report.
  
## Post Migration

Site owners will need to reinstall the add-in during the user acceptance testing (UAT) process. If there was an add-in that was purchased, the user who purchased the add-in will need to recover the license.
  
## Scan Result Reports

The following table describes the columns in the **Apps-detail.csv** report. 
  
This scan report provides a list of all the add-ins installed in the environment.
  
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
|OwnerLogin  <br/> |Owner of the site collection. [duplicate of Site Owner column]  <br/> |
|OwnerTitle  <br/> |Display name for the owner.  <br/> |
|AppTitle  <br/> |Title of the add-in.  <br/> |
|AppSource  <br/> |This is the location the application was installed from.  <br/> |
|AppID  <br/> |ID assigned to the add-in.  <br/> |
|WebID  <br/> |ID or the web hosting the add-in.  <br/> |
|LaunchURL  <br/> |URL used to launch the add-in. If this URL is ~appWebUrl, then the add-in runs on the SharePoint environment. If the URL is not associated with the SharePoint environment, then the add-in is a provider-hosted add-in that runs outside of the environment.  <br/> |
|CreationTime  <br/> |Time the add-in was installed.  <br/> |
|RemoteAppURL  <br/> |If the add-in is a provider-hosted add-in, this will contain the URL for the add-in.  <br/> |
|SettingsPageURL  <br/> |URL for the settings page associated with an add-in.  <br/> |
|WebSiteTitle  <br/> |Title of the web hosting the add-in.  <br/> |
|WebURL  <br/> |URL of the webhosting the add-in.  <br/> |
|PageURL  <br/> |If the add-in is an app part that sites on a page, this will be the URL to the page.  <br/> |
|ScanID  <br/> |Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool.  <br/> |
   

