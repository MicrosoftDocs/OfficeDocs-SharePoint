---
title: "Migration Assessment Scan Web Application Policies"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.date: 7/5/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Priority
ms.collection:
- IT_SharePoint_Hybrid_Top
- IT_Sharepoint_Server_Top
- Strat_SP_gtc
ms.custom:
ms.assetid: d538651b-75e4-4221-9ea1-c2d0be1e0589
description: "Learn how to fix issues with Web Application policies during migration."
---

# Migration Assessment Scan: Web Application Policies

Learn how to fix issues with Web Application policies during migration.
  
## Overview

In the source environment, there are typically discrete web applications for Team, Portal, Partner, and MySite (OneDrive). SharePoint On Premise allows the use of web application policies to grant or deny blanket-level permissions to entire web applications. These permissions override any permissions set at the site collection, site, list/library, or item level.
  
The target environment uses a single web application to host all site collections.
  
We do not currently offer a permission feature that applies uniquely to specific root site names and all child items together.
  
## Data Migration

None of the web application policies are migrated to the target environment.
  
> [!IMPORTANT]
> Any site that is configured as "No Access" (locked), in SharePoint will be skipped. To see a list of locked site collections see the Locked Sites scan output. 
  
## Preparing for Migration

Web application policies are not migrated. Some alternatives at this time include:
  
- Change administrative procedures to manage all permissions at the site collection level (this can be performed via Tenant Admin) instead of using web application policies.
    
- Use licensing to grant or limit specific capabilities to specific users and groups.
    
## Post Migration

Ensure the alternative options function correctly during the User Acceptance Testing phase.
  
## Scan Result Reports

 **WebApplicationPolicy-detail.csv** This scan report lists all policies for all of your web applications. 
  
|**Column**|**Description**|
|:-----|:-----|
|WebApplication  <br/> |The source web application.  <br/> |
|PolicyDisplayName  <br/> |Display Name of the user or group.  <br/> |
|PolicyUserName  <br/> |The login ID of the user or group.  <br/> |
|PolicyRoleBinding  <br/> |Permission granted to the user or group in the source.  <br/> |
|ScanID  <br/> |Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool.  <br/> |
   

