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
ms.service: sharepoint-server-itpro
ms.localizationpriority: medium
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 
description: "Introduces articles that describe software and other requirements for SharePoint Server Subscription Edition."
---

# Software requirements for Database Servers for SharePoint Server Subscription Edition

[!INCLUDE [appliesto-xxx-xxx-xxx-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)] 

## Operating systems

SharePoint Server Subscription Edition supports database servers deployed on the following operating systems:
- [Windows Server 2019](https://www.microsoft.com/evalcenter/evaluate-windows-server-2019) Standard or Datacenter
- [Windows Server 2022](https://www.microsoft.com/evalcenter/evaluate-windows-server-2022) Standard or Datacenter

SharePoint Server Subscription Edition supports database servers deployed with the following Windows Server installation options:
- Server with Desktop Experience
- Server Core

## Database versions

SharePoint Server Subscription Edition supports the following database versions:

- A Standard or Enterprise Edition of SQL Server for Windows that supports database compatibility level 150. This includes SQL Server 2019 Cumulative Update 5 (CU5) or later, SQL Server 2022, and any future version of SQL Server for Windows that supports database compatibility level 150. For more information about database compatibility levels, see [Compatibility Certification](/sql/database-engine/install-windows/compatibility-certification) and [ALTER DATABASE (Transact-SQL) Compatibility Level](/sql/t-sql/statements/alter-database-transact-sql-compatibility-level).

- Microsoft Azure SQL Managed Instance (MI). This is only supported if your SharePoint Server farm is hosted in Microsoft Azure. For more information, see [Deploy Azure SQL Managed Instance with SharePoint Servers](/sharepoint/administration/deploy-azure-sql-managed-instance-with-sharepoint-servers).

> [!NOTE]
> SQL Server products and all future SQL Server Cumulative Updates are supported through the SQL Server product lifecycle.

> [!NOTE]
> SQL Server Express is not supported. Azure SQL Database (the non-Managed Instance DBaaS service) is also not supported for any SharePoint databases.
