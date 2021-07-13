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

## Operating systems

SharePoint Server requires Windows Server 2019 or Windows Server 2022. Earlier versions of Windows Server are not supported. SharePoint Server supports both the Standard and Datacenter editions of Windows Server, as well as both the Windows Server with Desktop Experience and Windows Server Core installation options.

You can download evaluation copies of Windows Server 2019 and Windows Server 2022 Preview from the Microsoft Evaluation Center.
- [Windows Server 2019](https://www.microsoft.com/en-in/evalcenter/evaluate-windows-server-2019)
- [Windows Server 2022](https://www.microsoft.com/en-in/evalcenter/evaluate-windows-server-2022-preview)
- 

> [!NOTE]
> We don't support installing the Office 2019 and SharePoint Server Subscription Edition on the same computer.

> [!NOTE]
> The minimum supported version is Office 2013 client.

## Prerequisite installer operations and command-line options

The SharePoint Server Subscription Edition prerequisite installer `prerequisiteinstaller.exe`installs the following software, if it has not already been installed on the target server, in the following order:

1. Web Server (IIS) Role
2. Microsoft WCF Data Services 5.6
3. Microsoft .NET Framework 4.8
4. Visual C++ Redistributable Package for Visual Studio 2015-2019

You can run `prerequisiteinstaller.exe` at a command prompt with the following options. When you run `prerequisiteinstaller.exe` at a command prompt, you might be asked to restart the server one or more times during the installation process. After restarting, you should continue the prerequisite installation by running `prerequisiteinstaller.exe` with the /continue option.

/? This displays command-line options.

/continue This is used to tell the installer that it is continuing from being restarted.

/unattended This indicates no user interaction.

The installer installs from the file that you specify in the command-line options described in the following list. In this list, <file> signifies the file from which you want to install. If you do not specify the `<file> option, the installer downloads the file from the Internet and installs it. If the option does not apply to the current operating system, it is ignored.

**/WCFDataServices56**:*<file>* Install Microsoft WCF Data Services 5.6 from *<file>*.

**/DotNet48**:*<file>* Install Microsoft .NET Framework 4.8 from *<file>*.

**/MSVCRT142**:*<file>* Install Visual C++ Redistributable Package for Visual Studio 2015-2019 from *<file>.*

## Installation options

Certain prerequisites are installed by the prerequisite installer with specific options. Those prerequisites with specific installation options are listed below with the options that are used by the prerequisite installer.
- Microsoft WCF Data Services
  
  /quiet

The prerequisite installer creates log files at **%TEMP%\prerequisiteinstaller.<date>.<time>**.log. You can check these log files for specific details about all changes the installer makes to the target computer.


## Manually configure Windows Server Roles and Features
To manually configure the required Windows Server Roles and Features, you can use one of two methods: 1. Server Manager 2. Microsoft PowerShell

To configure by using Server Manager, see Install or Uninstall Roles, Role Services, or Features

To configure by using PowerShell:

From a PowerShell command prompt window, type:
```Install-WindowsFeature NET-WCF-Pipe-Activation45,NET-WCF-HTTP-Activation45,NET-WCF-TCP-Activation45,Web-Server,Web-WebServer,Web-Common-Http,Web-Static-Content,Web-Default-Doc,Web-Dir-Browsing,Web-Http-Errors,Web-App-Dev,Web-Asp-Net45,Web-Net-Ext45,Web-ISAPI-Ext,Web-ISAPI-Filter,Web-Health,Web-Http-Logging,Web-Log-Libraries,Web-Request-Monitor,Web-Http-Tracing,Web-Security,Web-Basic-Auth,Web-Windows-Auth,Web-Filtering,Web-Performance,Web-Stat-Compression,Web-Dyn-Compression,WAS,WAS-Process-Model,WAS-Config-APIs -IncludeManagementTools```

> [!NOTE]
> Some Windows features being installed are “Features On Demand (FOD)”, which are downloaded from Windows Update. If the computer doesn’t have access to Windows Update, you can specify local installation files by adding the Source parameter and pointing to the \sources\sxs folder on the Windows Server installation media.

For example: -Source D:\sources\sxs

