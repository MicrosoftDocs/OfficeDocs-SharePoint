---
title: "Business Data Connectivity connectors are currently enabled in a partitioned environment (SharePoint Server)"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 2/22/2018
audience: ITPro
ms.topic: troubleshooting
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: e4b1234e-2b69-4c44-9621-398d20122cab
description: "Learn how to resolve the SharePoint Health Analyzer rule: Business Data Connectivity connectors are currently enabled in a partitioned environment, for SharePoint Server."
---

# Business Data Connectivity connectors are currently enabled in a partitioned environment (SharePoint Server)

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
 **Rule Name:** Business Data Connectivity connectors are currently enabled in a partitioned environment 
  
 **Summary:** Business Data Connectivity (BDC) Models containing External Content Types with database, WCF, Web service or custom connectors can be used by tenants to elevate their user permissions. In a partitioned environment, we recommend you disable the Business Data Connectivity connectors. 
  
 **Cause:** Business Data Connectivity connectors are currently enabled in a partitioned environment. 
  
 **Resolution: Disable unwanted connectors by using Microsoft PowerShell.**
  
- To disable the unwanted connectors, follow the instructions in [Business Data Connectivity connectors in a partitioned environment in SharePoint Server](https://support.microsoft.com/kb/983546).
    

