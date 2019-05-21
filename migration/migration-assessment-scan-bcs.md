---
title: "Migration Assessment Scan BCS"
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
ms.custom:
ms.assetid: 382f6607-5434-4e03-8b9a-0ce04ead9ace
description: "Learn how to fix issues with BCS before migrating your data."
---

# Migration Assessment Scan: BCS

Learn how to fix issues with BCS before migrating your data.
  
## Overview

Business Connectivity Services (BCS) was introduced in SharePoint 2010 as an improvement to the Business Data Catalog created for Office SharePoint Server 2007. BCS enables SharePoint to access data from external data systems such as SAP, ERP, and CRM, in addition to other data-driven applications that are exposed through Windows Communication Foundation (WCF) services or Open Data (OData) endpoints.
  
## Data Migration

BCS applications are not migrated to the target environment. Depending on the type of data you are accessing and the location, you may need to implement a BCS hybrid solution.
  
> [!IMPORTANT]
> Any site that is configured as "No Access" (locked), in SharePoint will be skipped. To see a list of locked site collections see the Locked Sites scan output. 
  
## Preparing for Migration

Identify the BCS applications deployed to the source environment and determine if those applications are required post migration. If they are, work through the following options:
  
- Configure a hybrid BCS configuration.
    
- Expose the data source you need to access to the Internet, so that you can connect to it from the target environment.
    
Once you land on a solution, push the updated BCS applications to the target environment at any time during the migration validation phase.
  
## Post Migration

Ensure that your solutions, which rely on the BCS applications, function with the newly deployed BCS applications.
  
## Scan Result Reports

The following table describes the columns in the **BCSApplications-detail.csv** report. 
  
This file contains the BCS LobSystem definitions that are deployed to the target environment and some information to help you identify the definition and what it is used for.
  
|**Column**|**Description**|
|:-----|:-----|
|Name  <br/> |Name of the BCS definition.  <br/> |
|Description  <br/> |Description of the BCS definition.  <br/> |
|Namespace  <br/> |The namespace associated with the BCS definition.  <br/> |
|Version  <br/> |Version of the BCS definition.  <br/> |
|LOBSystemType  <br/> |Type of system used in the BCS definition.  <br/> |
|LOBEntities  <br/> |The entities found in the BCS definition.  <br/> |
|LOBName  <br/> |Line of business name found in the BCS definition.  <br/> |
|ScanID  <br/> |Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool.  <br/> |
   

