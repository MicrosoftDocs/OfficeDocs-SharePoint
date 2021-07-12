---
title: "Software Requirements for Database Servers for SharePoint Server Subscription Edition"
ms.reviewer: 
ms.author: v-nsatapathy
author: nimishasatapathy
manager: serdars
ms.date: 7/10/2021
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: conceptual
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: ' kkkkk .m
description: "This article introduces topics that describe software and database servers requirements for SharePoint Server."
---

# Software Requirements for Database Servers for SharePoint Server Subscription Edition

[!INCLUDE [appliesto-xxx-xxx-xxx-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)] 
  
The OS versions list Windows Server 2019 and Windows Server 2022, Standard or Datacenter, Desktop Experience or Server Core installation modes.
	
The database versions supports:

- A Standard or Enterprise Edition of SQL Server for Windows that supports database compatibility level 150. This includes SQL Server 2019 and any future version of SQL Server for Windows that supports database compatibility level 150. For more information about database compatibility levels, see [Compatibility Certification](https://docs.microsoft.com/sql/database-engine/install-windows/compatibility-certification?view=sql-server-ver15) and [ALTER DATABASE (Transact-SQL) Compatibility Level](https://docs.microsoft.com/sql/t-sql/statements/alter-database-transact-sql-compatibility-level?view=sql-server-ver15).

- Microsoft Azure SQL Managed Instance (MI). This is only supported if your SharePoint Server farm is hosted in Microsoft Azure. For more information, see [Deploy Azure SQL Managed Instance with SharePoint Servers 2016 and 2019](https://docs.microsoft.com/sharepoint/administration/deploy-azure-sql-managed-instance-with-sharepoint-servers-2016-2019).

> [!NOTE]
> SQL Server products and all future public updates are supported through the SQL Server product lifecycle.

> [!NOTE]
> SQL Server Express is not supported. Azure SQL Database (the non-Managed Instance DBaaS service) is also not supported for any SharePoint databases.

