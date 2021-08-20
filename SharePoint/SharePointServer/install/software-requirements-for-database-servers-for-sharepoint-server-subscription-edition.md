---
title: "Software requirements for Database Servers for SharePoint Server Subscription Edition"
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
ms.assetid: 
description: "Introduces articles that describe software and other requirements for SharePoint Server Subscription Edition."
---

# Software requirements for Database Servers for SharePoint Server Subscription Edition

[!INCLUDE [appliesto-xxx-xxx-xxx-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)] 
  
## Operating systems

SharePoint Server supports the following operating systems:
- [Windows Server 2019](https://www.microsoft.com/en-in/evalcenter/evaluate-windows-server-2019) Standard or Datacenter
- [Windows Server 2022](https://www.microsoft.com/en-in/evalcenter/evaluate-windows-server-2022-preview) Standard or Datacenter

Earlier versions of windows server are not supported. SharePoint server supports both the Standard and Datacenter editions of windows server, as well as both the Windows Server with Desktop Experience and windows server core installation options.

	
## Database versions

SharePoint server supports the following database versions:

- A Standard or Enterprise Edition of SQL Server for Windows that supports database compatibility level 150. This includes SQL Server 2019 and any future version of SQL Server for Windows that supports database compatibility level 150. For more information about database compatibility levels, see [Compatibility Certification](https://docs.microsoft.com/sql/database-engine/install-windows/compatibility-certification?view=sql-server-ver15) and [ALTER DATABASE (Transact-SQL) Compatibility Level](https://docs.microsoft.com/sql/t-sql/statements/alter-database-transact-sql-compatibility-level?view=sql-server-ver15).

- Microsoft Azure SQL Managed Instance (MI). This is only supported if your SharePoint Server farm is hosted in Microsoft Azure. For more information, see [Deploy Azure SQL Managed Instance with SharePoint Servers 2016 and 2019](../administration/deploy-azure-sql-managed-instance-with-sharepoint-servers-2016-2019).

> [!NOTE]
> SQL Server products and all future public updates are supported through the SQL Server product lifecycle.

> [!NOTE]
> SQL Server Express is not supported. Azure SQL Database (the non-Managed Instance DBaaS service) is also not supported for any SharePoint databases.

