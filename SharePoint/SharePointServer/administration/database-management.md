---
title: "Manage databases in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 8/4/2017
audience: ITPro
ms.topic: hub-page
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: f436a248-984f-40bd-bbe2-ac4dd1e1f961
description: "Learn how to manage the databases that are associated with SharePoint Server."
---

# Manage databases in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
The following articles and related resources provide information about database management with SharePoint Server.
  
  
|**Content**|**Description**|
|:-----|:-----|
|[Add content databases in SharePoint Server](add-a-content-database.md) <br/> |Adding a content database to an existing Web application is a common task. This article describes how to add a content database to an existing SharePoint Server implementation.  <br/> |
|[Attach or detach content databases in SharePoint Server](attach-or-detach-content-databases.md) <br/> |Certain operations, such as applying updates or creating copies of configuration settings, require that you detach and then attach databases. This article describes how to do these procedures.  <br/> |
|[Move site collections between databases in SharePoint Server](move-site-collections-between-databases.md) <br/> |Under some circumstances, you might want to move one or more site collections to a different content database. For example, a site collection can outgrow the content database on which it is located, and you would have to move the site collection to a larger content database. Conversely, if site collections do not grow to their expected capacity, it might be convenient to combine several site collections onto one content database. This article describes how to move site collections between databases.  <br/> |
|[Move content databases in SharePoint Server](move-content-databases.md) <br/> |This article describes how to move content databases between servers that are running SQL Server, between instances of SQL Server, or from one SharePoint Server Web application to another. You can also move a content database to load balance a database server or Web application.  <br/> |
|[Move all databases in SharePoint Server](move-all-databases.md) <br/> |This article describes how to move all of the databases supported by SharePoint Server from one database server to another database server. If your SharePoint databases are hosted on different servers, this procedure applies to the database server that hosts the configuration database.  <br/> |
|[Move or rename service application databases in SharePoint Server](move-or-rename-service-application-databases.md) <br/> |Learn how to move and rename service application databases by using SQL Server, and then how to point the service application to the moved or renamed database.  <br/> |
|[Run a farm that uses read-only databases in SharePoint Server](run-a-farm-that-uses-read-only-databases.md) <br/> |A read-only farm can be part of a disaster recovery environment. Alternatively, it can be part of a highly available maintenance, patching, or upgrade environment that provides user access while another version of the farm is being updated. This article describes how to run a SharePoint Server farm in which content databases are set to be read-only (a read-only farm).  <br/> |
|[Manage RBS in SharePoint Server](manage-rbs.md) <br/> |Learn about Remote BLOB Storage (RBS) and how to manage RBS in SharePoint Server.  <br/> |
|[Best practices for SQL Server in a SharePoint Server farm](best-practices-for-sql-server-in-a-sharepoint-server-farm.md) <br/> |Learn about best practices for SQL Server in a SharePoint Server farm.  <br/> |
   
## See also

#### Concepts

  
[Overview of backup and recovery in SharePoint Server](backup-and-recovery-overview.md)
  
[Plan for backup and recovery in SharePoint Server](backup-and-recovery-planning.md)
  
[Database types and descriptions in SharePoint Server](../technical-reference/database-types-and-descriptions.md)

