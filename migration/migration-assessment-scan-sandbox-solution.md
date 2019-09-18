---
title: "Migration Assessment Scan Sandbox Solution"
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
ms.assetid: 411c5512-e99c-4010-8a25-113515851cd7
description: "Learn how to mitigate issues with Sandbox solutions during migration."
---

# Migration Assessment Scan: Sandbox Solution

Learn how to mitigate issues with Sandbox solutions during migration.
  
## Overview

> [!IMPORTANT]
> SharePoint Online does not support Sandbox solutions. 
  
SharePoint Online does not support sandbox solutions. As a result, any functionality that is using the sandbox in your current environment will need to be replaced with a supported technology. See the Office Dev Center Patterns and Practices site for information on building customizations.
  
https://dev.office.com/patterns-and-practices
  
## Data Migration

> [!IMPORTANT]
> Any site that is configured as "No Access" (locked), in SharePoint will be skipped. To see a list of locked site collections see the Locked Sites scan output. 
  
## Scan Result Reports

The following table describes the columns in the **SandboxSolution-detail.csv** report. 
  
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
|SandboxSolutionName  <br/> |Sandbox solution name  <br/> |
|WebApplicationURL  <br/> |Web application URL hosting the sandbox solution  <br/> |
|SandboxSolutionID  <br/> |Sandbox solution ID  <br/> |
|Signature  <br/> |Sandbox solution hash value  <br/> |
|HasAssembly  <br/> |True if the solution contains assemblies; otherwise, false  <br/> |
|SolutionStatus  <br/> |Sandbox solution status, which may be activated, deactivated, or disabled  <br/> |
|SolutionType  <br/> |Sandbox solution type, which maybe "Custom Code", "Site Template", or "Design Package"  <br/> |
|CreatedBy  <br/> |User identity who created the solution  <br/> |
|CreatedDate  <br/> |Date when the solution was created  <br/> |
|ModifiedBy  <br/> |User identity who last modified the solution  <br/> |
|ModifiedDate  <br/> |Date when the solution was last modified  <br/> |
|ScanID  <br/> |Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool.  <br/> |
   

