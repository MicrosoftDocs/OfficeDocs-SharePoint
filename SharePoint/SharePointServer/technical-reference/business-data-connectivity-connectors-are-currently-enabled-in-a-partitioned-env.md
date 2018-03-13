---
title: "Business Data Connectivity connectors are currently enabled in a partitioned environment (SharePoint Server)"
ms.author: stevhord
author: bentoncity
manager: pamgreen
ms.date: 2/22/2018
ms.audience: ITPro
ms.topic: troubleshooting
ms.prod: office-online-server
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: e4b1234e-2b69-4c44-9621-398d20122cab
description: "Summary: Learn how to resolve the SharePoint Health Analyzer ruleBusiness Data Connectivity connectors are currently enabled in a partitioned environmentfor SharePoint Server 2016 and SharePoint 2013."
---

# Business Data Connectivity connectors are currently enabled in a partitioned environment (SharePoint Server)

 **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "Business Data Connectivity connectors are currently enabled in a partitioned environment" for SharePoint Server 2016 and SharePoint 2013. 
  
 **Rule Name:** Business Data Connectivity connectors are currently enabled in a partitioned environment 
  
 **Summary:** Business Data Connectivity (BDC) Models containing External Content Types with database, WCF, Web service or custom connectors can be used by tenants to elevate their user permissions. In a partitioned environment, we recommend you disable the Business Data Connectivity connectors. 
  
 **Cause:** Business Data Connectivity connectors are currently enabled in a partitioned environment. 
  
 **Resolution: Disable unwanted connectors by using Microsoft PowerShell.**
  
- To disable the unwanted connectors, follow the instructions in [Business Data Connectivity connectors in a partitioned environment in SharePoint Server](https://support.microsoft.com/kb/983546).
    

