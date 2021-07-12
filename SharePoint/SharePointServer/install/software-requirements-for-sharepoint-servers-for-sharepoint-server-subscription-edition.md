---
title: "Software Requirements for SharePoint Servers for SharePoint Server Subscription Edition"
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
description: "This article introduces topic that describe software requirements for SharePoint Server."
---


# Software Requirements for SharePoint Servers for SharePoint Server Subscription Edition

[!INCLUDE [appliesto-xxx-xxx-xxx-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)] 

## Minimum requirements for SharePoint servers in a farm

One of the following server operating systems:
- Windows Server 2016 Standard or Datacenter (Desktop Experience)
- Windows Server 2019 Standard or Datacenter (Desktop Experience)

> [!NOTE]
> We don't support installing the Office 2019 client and SharePoint Server Subscription Edition on the same computer.

> [!NOTE]
> The minimum supported version is Office 2013 client.

The Microsoft SharePoint Products Preparation Tool installs the following prerequisites on SharePoint servers in a farm:
1. Web Server (IIS) Role
2. Microsoft WCF Data Services 5.6
3. Microsoft .NET Framework 4.8
4. Visual C++ Redistributable Package for Visual Studio 2015-2019
> [!NOTE]
> The required software above will be supported when used by SharePoint via the SharePoint Product Lifecycle.

## Manually configure Windows Server Roles and Features
To manually configure the required Windows Server Roles and Features, you can use one of two methods: 1. Server Manager 2. Microsoft PowerShell

To configure by using Server Manager, see Install or Uninstall Roles, Role Services, or Features

To configure by using PowerShell:

From a PowerShell command prompt window, type:
```Install-WindowsFeature NET-WCF-Pipe-Activation45,NET-WCF-HTTP-Activation45,NET-WCF-TCP-Activation45,Web-Server,Web-WebServer,Web-Common-Http,Web-Static-Content,Web-Default-Doc,Web-Dir-Browsing,Web-Http-Errors,Web-App-Dev,Web-Asp-Net45,Web-Net-Ext45,Web-ISAPI-Ext,Web-ISAPI-Filter,Web-Health,Web-Http-Logging,Web-Log-Libraries,Web-Request-Monitor,Web-Http-Tracing,Web-Security,Web-Basic-Auth,Web-Windows-Auth,Web-Filtering,Web-Performance,Web-Stat-Compression,Web-Dyn-Compression,WAS,WAS-Process-Model,WAS-Config-APIs -IncludeManagementTools```

> [!NOTE]
> Some Windows features being installed are “Features On Demand (FOD)”, which are downloaded from Windows Update. If the computer doesn’t have access to Windows Update, you can specify local installation files by adding the Source parameter and pointing to the \sources\sxs folder on the Windows Server installation media.

For example: -Source D:\sources\sxs

### Operating systems

SharePoint Server requires Windows Server 2019 or Windows Server 2022. Earlier versions of Windows Server are not supported. SharePoint Server supports both the Standard and Datacenter editions of Windows Server, as well as both the Windows Server with Desktop Experience and Windows Server Core installation options.

You can download evaluation copies of Windows Server 2019 and Windows Server 2022 Preview from the Microsoft Evaluation Center.
- [Windows Server 2019](https://www.microsoft.com/en-in/evalcenter/evaluate-windows-server-2019)
- [Windows Server 2022](https://www.microsoft.com/en-in/evalcenter/evaluate-windows-server-2022-preview)