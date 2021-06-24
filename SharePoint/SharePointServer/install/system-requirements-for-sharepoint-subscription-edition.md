---
title: "System requirements for SharePoint Subscription edition"
ms.reviewer: 
ms.author: v-nsatapathy
author: nimishasatapathy
manager: serdars
ms.date: 06/21/2021
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: concetpual
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 64233599-f18c-4081-a3ce-450e878a1b9f

description: "This article introduces topics that describe hardware, software, and other requirements for SharePoint Server."
---

# System requirements for SharePoint Subscription edition

[!INCLUDE[appliesto-xxx-2016-2019-xxx-md](../includes/appliesto-xxx-2016-2019-xxx-md.md)] 
  
Before you install SharePoint Server, you must make sure that you have installed all required hardware and software. To effectively plan your deployment, you must understand the level of support that is provided for the web browsers that you will be using in your environment and how support for IP versions 4 and 6 is implemented in SharePoint Servers 2016 and 2019. You must also understand the URL and path length restrictions in SharePoint Servers 2016 and 2019.
  
## SharePoint Server v.Next Prerequisites

SharePoint Server v.Next requires additional software prerequisites, which must be installed before you run SharePoint Server v.Next setup. All the required prerequisites can be automatically installed by the SharePoint prerequisite installer "prerequisiteinstaller.exe", or you can choose to manually install them yourself.
- Various Windows Server roles and features such as the Web Server (IIS) Role. You can enable these in Windows Server Manager or by running the following PowerShell command:
Install-WindowsFeature NET-WCF-Pipe-Activation45,NET-WCF-HTTP-Activation45,NET-WCF-TCP-Activation45,Web-Server,Web-WebServer,Web-Common-Http,Web-Static-Content,Web-Default-Doc,Web-Dir-Browsing,Web-Http-Errors,Web-App-Dev,Web-Asp-Net45,Web-Net-Ext45,Web-ISAPI-Ext,Web-ISAPI-Filter,Web-Health,Web-Http-Logging,Web-Log-Libraries,Web-Request-Monitor,Web-Http-Tracing,Web-Security,Web-Basic-Auth,Web-Windows-Auth,Web-Filtering,Web-Performance,Web-Stat-Compression,Web-Dyn-Compression,WAS,WAS-Process-Model,WAS-Config-APIs -IncludeManagementTools
- "Microsoft WCF Data Services 5.6"
- "Microsoft .NET Framework 4.8"
- "Visual C++ Re-distributable Package for Visual Studio 2015-2019"

The prerequisite installer creates log files at %TEMP%\prerequisiteinstaller.<date>.<time>.log. You can check these log files for specific details about all changes the installer makes to the target computer.

## Test Environments without an Internet Connection

The SharePoint prerequisite installer requires an active Internet connection to download and install the prerequisites. In scenarios where there is no access to the Internet, you can download the prerequisites and then install them from a network share. For more information, see [Hardware and software requirements for SharePoint Server 2019](hardware-and-software-requirements-2019.md).

## Minimum Requirements for Client Computers

A supported browser.For more information, see "System requirements for Microsoft 356 and office: Browsers".


