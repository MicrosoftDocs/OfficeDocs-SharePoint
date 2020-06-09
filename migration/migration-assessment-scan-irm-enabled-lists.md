---
title: "Migration Assessment Scan IRM Enabled Lists"
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
- Strat_SP_gtc
- SPMigration
- M365-collaboration
ms.custom:
ms.assetid: fce14caf-dc41-485d-91c6-4d533c8d1097
description: "Learn how to mitigate issues with IRM enabled lists during migration."
---

# Migration Assessment Scan: IRM Enabled Lists

Learn how to mitigate issues with IRM enabled lists during migration.
  
## Overview

Information Rights Management [IRM] is a feature that enables you to encrypt content when a user accesses it to ensure it cannot be forwarded or manipulated. The files are stored in an unencrypted format in SharePoint. When a user accesses a file in an IRM protected list, the file is protected prior to transit. The file can only be opened in an IRM supported client application such as Microsoft Office.
  
There are two main components to the IRM migration process:
  
- Configure the target environment to support Microsoft Azure Active Directory Rights Management.
    
- Disable IRM on the source and target SharePoint libraries. This is required as the migration tooling will access the files in the same manner as a user. If IRM is enabled on the source, the migration tooling will receive an encrypted file and upload that encrypted file to the target environment. This results in a file that can no longer be opened successfully.
    
## Data Migration

IRM settings associated with lists and libraries are not migrated. The following process is required to enable the migration tooling to properly handle IRM protected libraries. This process ensures that the content is transferred and accessible post migration.
  
1. Disable IRM on the source and target list.
    
2. Migration tooling will copy the files from the source and place them in the target.
    
3. Enable IRM on the source and target list.
    
> [!IMPORTANT]
> Any site that is configured as "No Access" (locked), in SharePoint will be skipped. To see a list of locked site collections see the Locked Sites scan output. 
  
## Preparing for Migration

1. IRM will need to be configured for SharePoint.
    
2. IRM will need to be disabled on the source list prior to the migration event for that site collection.
    
## Post Migration

1. Enable IRM on the migrated content list.
    
2. Perform the following steps to ensure documents in IRM protected libraries are protected.
    
  - Download a document from an IRM protected list.
    
  - Open the document on the client machine.
    
  - If the document is protected, there will be a status displayed beneath the ribbon.
    
## Scan Result Reports

The following table describes the columns in the **IRMEnabledLibrary-detail.csv** report. This scan report contains lists and libraries that have IRM enabled. If IRM is disabled on the farm, the scan will not execute and the output file will indicate this. 
  
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
|ListTitle  <br/> |Title of the list or library with IRM enabled.  <br/> |
|URL  <br/> |URL to the default list view.  <br/> |
|ItemCount  <br/> |Number of items in the list.  <br/> |
|ScanID  <br/> |Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool.  <br/> |
   

