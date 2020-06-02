---
title: "Plan Excel Services Data Model settings in SharePoint Server 2013"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 6/23/2017
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: 40f1d080-3523-444f-a389-0f37a40ae44a
description: "Specify an instance of Analysis Services to be used with interactive data models in Excel Services."
---

# Plan Excel Services Data Model settings in SharePoint Server 2013

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
In Excel Services, you can specify one or more instances of SQL Server 2012 SP1 Analysis Services (SSAS) for use in processing Data Models created in Excel 2016. In this configuration, SQL Server 2012 Analysis Services provides a backend service for Excel Services to load, query, and refresh Excel 2016 Data Models so that users can interact with these types of workbooks in the browser. SQL Server 2012 Analysis Services must be installed in SQL Server PowerPivot for SharePoint mode.
  
In Excel Services, Data Models are created automatically when you choose multiple tables in the same import operation in Excel. If you build workbooks that store imported data in multiple tables, you will need an instance of SQL Server 2012 SP1 Analysis Services (SSAS) specified in Excel Services if you want to interact with that data in SharePoint Server 2013.
  
Analysis Services must be on the same network and domain as your SharePoint Server 2013 farm. You install and manage it by using SQL Server installation media and tools. After you install Analysis Services, the only additional configuration is to configure Excel Services Application Settings to point to the Analysis Services server instance.
  
You can specify multiple instances of Analysis Services in Excel Services settings. When you do this, data models are streamed to these instances in a round-robin fashion for load balancing. If you notice that resource usage on your instance of Analysis Services is excessive or working with data models in the browser has slowed, consider adding an additional instance of Analysis Services for greater capacity.
  
The Analysis Services instance is specified as part of Excel Services Application Settings. For information on configuring SQL Server 2012 SP1 Analysis Services (SSAS) for Excel Services, see [Manage Excel Services data model settings (SharePoint Server 2013)](manage-excel-services-data-model-settings.md).
  

