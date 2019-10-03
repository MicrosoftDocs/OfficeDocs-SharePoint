---
title: "Migration Assessment Scan Large List Views"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.date: 9/13/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Priority
ms.collection:
- IT_SharePoint_Hybrid_Top
- IT_Sharepoint_Server_Top
- Strat_SP_gtc
- SPMigration
- M365-collaboration
ms.custom:
ms.assetid: e94a941a-b171-41fc-8685-f2fd74bf8487
description: "Learn how to mitigate issues with Large List Views during migration."
---

# Migration Assessment Scan: Large List Views

Learn how to mitigate issues with Large List Views during migration.
  
## Overview

On the source environment it is possible to configure list view throttling so there are a set number of hours per day where the throttle on views is lifted. On the target platform, the stated product list limits is in place continuously (24x7). This may result in some of your list views being throttled.
  
## Data Migration

The lists and their data will be migrated. However, the list views called out in the scan report may not be viewable post migration without performing the remediation documented in the following section, Preparing for Migration. Any list views containing over 12 lookup columns may also be throttled and require remediation. For more information, see [Designing large lists and maximizing list performance.](/previous-versions/office/sharepoint-server-2010/cc262813(v=office.14)).
  
> [!IMPORTANT]
> Any site that is configured as "No Access" (locked), in SharePoint will be skipped. To see a list of locked site collections see the Locked Sites scan output. 
  
## Preparing for Migration

Review the provided report and remediate the large list views prior to migration. For information on how to optimize list views, see [Manage large lists and libraries in Office 365](https://support.office.com/en-us/article/Manage-large-lists-and-libraries-in-Office-365-b4038448-ec0e-49b7-b853-679d3d8fb784?ui=en-US&amp;rs=en-US&amp;ad=US).
  
## Post Migration

Ensure the lists that you remediated are rendering correctly.
  
## Scan Result Reports

 **FileName: LargeListViews-detail.csv** This scan report contains list views that were either throttled, or will potentially be throttled in the near future once you migrate to the new platform. The report contains list views that meet one of the following criteria: 
  
- Returned greater than 3,000 items.
    
- Actively throttled on the scanned environment.
    
- Contains greater than 12 lookup columns.
    
- Configured as an aggregate view.
    
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
|LookupColumnCount  <br/> ||
|ListViewTitle  <br/> |The title of the impacted list view.  <br/> |
|DefaultView  <br/> |True/False. Determines if the view is the default view for the list.  <br/> |
|AggregateView  <br/> |True/False. Determines if the view is an aggregate view. For example, the view is configured to display a Total.  <br/> |
|ListViewThrottled  <br/> |True/False. Specifies whether the list view was actively throttled on the scanned environment.  <br/> |
|ViewItemCount  <br/> |Number of items returned when the list view was executed. This field is empty if ListViewThrottled is True.  <br/> |
|Hidden  <br/> |True/False. Specifies if the list view is configured to be hidden from end users.  <br/> |
|ReadOnlyView  <br/> |True/False. Specifies if the list view is configured to be read only.  <br/> |
|WebURL  <br/> |Url to the subsite that contains the list view.  <br/> |
|ListTitle  <br/> |Title of the list the list view is associated with  <br/> |
|ListURL  <br/> |Url to the root folder of the list.  <br/> |
|ListItemCount  <br/> |Number of items in the list.  <br/> |
|ListTemplate  <br/> |Template used when creating the list.  <br/> |
|ListType  <br/> |The type of list configured.  <br/> |
|ListCreator  <br/> |User that created the list.  <br/> |
|ItemLastModifiedDate  <br/> |Date/Time an item was last modified on the list.  <br/> |
|ScanID  <br/> |Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool.  <br/> |
   

