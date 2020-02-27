---
title: "Migration Assessment Scan Alerts"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.date: 9/12/2017
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
localization_priority: Priority
ms.collection:
- IT_SharePoint_Hybrid_Top
- IT_Sharepoint_Server_Top
- SPMigration
ms.custom: 
ms.assetid: 11fa99a3-9e65-48f6-b460-31c8cf8d30e5
description: "Learn how to fix issues with alerts during migration."
---

# Migration Assessment Scan: Alerts

Learn how to fix issues with alerts during migration.
  
## Overview

Most migration tools do not migrate alerts. Alerts are created on items, lists, and libraries to notify a user of when content changed. This report provides visibility into the alerts that are currently configured in the source environment. If users would like to be notified of content changes after the migration, they will need to configure the alerts on the new environment.   As a result of alerts not migrating, we provide a lot of raw data associated with the alerts should the need arise to recreate the alerts post migration.
  
## Data Migration

Basic migration tools do not migrate alerts.
  
> [!IMPORTANT]
> Any site that is configured as "No Access" (locked), in SharePoint will be skipped. To see a list of locked site collections see the Locked Sites scan output. 
  
## Preparing for Migration

Provide communication with users to avoid confusion post migration.
  
## Post Migration

Provide communication with users to avoid confusion post migration.
  
## Scan Result Reports

The following table describes the columns in the **Alerts-detail.csv** report. 
  
This scan report provides a list of all the alerts installed in the environment.
  
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
|WebURL  <br/> |Web URL.  <br/> |
|Title  <br/> |Title of the alert.  <br/> |
|AlertTemplateName  <br/> |Name of the alert.  <br/> |
|Filter  <br/> |The CAML query filter applicaed to the alert.  <br/> |
|ID  <br/> |ID assigned to the alert.  <br/> |
|MatchID  <br/> |Per-filtering ID for an externally matched alert.  <br/> |
|ItemID  <br/> |ID of the item an alert is assocatiated with. IF this is empty, the alert is associated with the list instead.  <br/> |
|ListURL  <br/> |Time the add-in was installed.  <br/> |
|ListID  <br/> |ID of the list the alert is associated with.  <br/> |
|List  <br/> |ID or the web hosting the add-in  <br/> |
|AlwaysNotify  <br/> |URL of the webhosting the add-in.  <br/> |
|DeliveryChannels  <br/> |Title of the web hosting the add-in.  <br/> |
|AlertType  <br/> |The type of object to which the alert applies, which can be a list or document library, a list item or document, or a custom object.  <br/> |
|EventType  <br/> |The type of event to which the alert applies.  <br/> |
|EventTypeBitmask  <br/> |This can be ignored.  <br/> |
|AlertFrequency  <br/> |Gets or sets the time interval for sending the alert.  <br/> |
|AlertTime  <br/> |The date and time for sending the alert.  <br/> |
|Status  <br/> |Determines if the alert is enabled or not.  <br/> |
|User  <br/> |User the alert is associated with.  <br/> |
|DynamicRecipient  <br/> |If the alert is dynamically generated, this determines how the recipient is defined.  <br/> |
|ScanID  <br/> |Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool.  <br/> |
|||
   

