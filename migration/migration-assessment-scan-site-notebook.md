---
title: "Migration Assessment Scan Site Notebook"
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
- SPMigration
- M365-collaboration
ms.custom:

---

# Migration Assessment Scan: Site Notebook

## Overview

SharePoint 2013 and later support a feature called Site Notebook. This SharePoint feature is activated on the site and will generate a OneNote in the Site Assets library of the web. The file will be named with the title of the site.
Depending on the migration tools being used, your Site Notebook will migrate. However, the name of the Site Notebook in SharePoint for Microsoft 365 is different from the name of the file in the on-premises environment. As a result, links referencing the original file name will be broken. This report will provide a list of OneNote files that match the following scenario:
	• OneNote Notebook files
	• Exist in the Site Assets library
	• Have a name that ends in Notebook
	• OneNote is not empty
	• Is not flagged as deleted


  
## Data Migration

Depending on the migration tools being used, the Site Notebook will migrate but the file will have a different name resulting in broken links.

  
> [!IMPORTANT]
> Any site that is configured as "No Access" (locked), in SharePoint will be skipped. To see a list of locked site collections see the Locked Sites scan output. 
  
## Preparing for Migration

Prepare for questions about missing Site Notebooks and provide guidance to impacted users.
  
## Post Migration

Educate users on the change related to Site Notebooks.


  
## Scan Result Reports

The following table describes the columns in the **Apps-detail.csv** report.
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
|DaysOfUsageData |Number of days the usage logging service retains data. This provides context for Hits and DistinctUsers. For example, if this is 14 days,the Hits and DistinctUsers data is for the last 14 days.|
|File|Path to the Site Notebook.|
|TimeCreated|Date/Time the file was created.|
|TimeModified|Date/Time the file was last modified.|
|ModifiedBy|Person that last modified the file.|
|ScanId|Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool. |


   

