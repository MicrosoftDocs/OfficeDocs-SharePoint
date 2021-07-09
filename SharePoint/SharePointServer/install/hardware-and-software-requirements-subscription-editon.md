---
title: "Hardware and Topology Requirements for SharePoint Server Subscription Edition"
ms.reviewer: 
ms.author: v-nsatapathy
author: nimishasatapathy
manager: serdars
ms.date: 6/22/2021
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: interactive-tutorial
ms.prod: sharepoint-server-itpro
localization_priority: Priority
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
- SP2019
ms.custom: 
ms.assetid: 4d88c402-24f2-449b-86a6-6e7afcfec0cd
description: "Find out the minimum hardware requirements that you need for installing and running SharePoint Server Subscription edition."
---

# Hardware and Topology Requirements for SharePoint Server Subscription Edition

[!INCLUDE [appliesto-xxx-xxx-xxx-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)]

  
> [!IMPORTANT]
> If you contact Microsoft Customer Support Services about a production system that does not meet the minimum hardware specifications described in this document, support will be limited until the system is upgraded to the minimum requirements. 
  
    
## Hardware requirements

Testing SharePoint Server in a pre-production environment with the following hardware configurations:

|**Installation scenario**|**Deployment type and scale**|**Processor**|**RAM**|**Hard disk**|
|:-----|:-----|:-----|:-----|:-----|
|Single server role that uses SQL Server  <br/> |Development or evaluation installation with the minimum recommended services for development environments.  <br/> |64-bit, 4 cores <br/> |16 GB  <br/> |80 GB for system drive  <br/> 100 GB for second drive  <br/> |
|Single server role that uses SQL Server  <br/> |Pilot or user acceptance test installation running all available services.  <br/> |64-bit, 4 cores <br/> |24 GB   <br/> |80 GB for system drive  <br/> 100 GB for second drive and additional drives  <br/> |
|SharePoint server in amulti-tier farm  <br/> |Development or evaluation installation with a minimum number of services.  <br/> |64-bit, 4 cores <br/> |12 GB  <br/> |80 GB for system drive  <br/> 80 GB for second drive  <br/> |
|SharePoint server in a multi-tier farm  <br/> |Pilot or user acceptance test installation running all available services.  <br/> |64-bit, 4 cores  <br/> |16 GB    <br/> |80 GB for system drive  <br/> 80 GB for second drive and additional drives  <br/> 

> [!NOTE]
> Hard disk space and number of drives depends on the amount of content and the way you choose to distribute data for a SharePoint environment.

## Prerequisites for SharePoint Server installation

Before you run SharePoint Server set up, additional softwares must be installed. You can install the prerequisite softwares using the following options:
- Automatically using the SharePoint prerequisite installer `prerequisiteinstaller.exe`
- Manually.

Following are the prerequisite softwares that must be installed prior to running SharePoint Server setup:
- Various Windows Server roles and features such as the Web Server (IIS) Role. 
You can enable these in Windows Server Manager or by running the following PowerShell command:

 ```
Install-WindowsFeature NET-WCF-Pipe-Activation45,NET-WCF-HTTP-Activation45,NET-WCF-TCP-Activation45,Web-Server,Web-WebServer,Web-Common-Http,Web-Static-Content,Web-Default-Doc,Web-Dir-Browsing,Web-Http-Errors,Web-App-Dev,Web-Asp-Net45,Web-Net-Ext45,Web-ISAPI-Ext,Web-ISAPI-Filter,Web-Health,Web-Http-Logging,Web-Log-Libraries,Web-Request-Monitor,Web-Http-Tracing,Web-Security,Web-Basic-Auth,Web-Windows-Auth,Web-Filtering,Web-Performance,Web-Stat-Compression,Web-Dyn-Compression,WAS,WAS-Process-Model,WAS-Config-APIs -IncludeManagementTools
   ```
- `Microsoft WCF Data Services 5.6.exe`
- `Microsoft .NET Framework 4.8.exe`
- `Visual C++ Re-distributable Package for Visual Studio 2015-2019.exe`

The prerequisite installer creates log files at **%TEMP%\prerequisiteinstaller.<date>.<time>.log**. You can check these log files for specific details about all changes the installer makes to the target computer.

## Prerequisite installer operations and command-line options

The SharePoint Server prerequisite installer (`prerequisiteinstaller.exe`) installs the following software, if it has not already been installed on the target server, in the following order:
1. **/WCFDataServices56:<*file*>** Install Microsoft WCF Data Services 5.6 from <*file*>.
2. **/DotNet48:<*file*>** Install Microsoft .NET Framework 4.8 from <*file*>.
3. **/MSVCRT142:<*file*>** Install Visual C++ Redistributable Package for Visual Studio 2015-2019 from <*file*>.

   
## Deployment requirements: farm topology
<a name="hwforwebserver"> </a>

SharePoint Server supports the same farm topologies as SharePoint Server 2019. For more information, see [Planning for a MinRole server deployment in SharePoint Server 2019](planning-for-a-minrole-server-deployment-in-sharepoint-server.md).

## Minimum requirements for client computers

A supported browser. For more information, see [System requirements for Microsoft 365 and office:Browsers](https://www.microsoft.com/microsoft-365/microsoft-365-and-office-resources?rtc=1#coreui-heading-uyetipy).
    
  
## Software requirements
<a name="section4"> </a>

The requirements in the following section apply to the following installations:
  
- Operating systems
    
- Database servers

### Operating systems

SharePoint Server requires Windows Server 2019 or Windows Server 2022. Earlier versions of Windows Server are not supported. SharePoint Server supports both the Standard and Datacenter editions of Windows Server, as well as both the Windows Server with Desktop Experience and Windows Server Core installation options.

You can download evaluation copies of Windows Server 2019 and Windows Server 2022 Preview from the Microsoft Evaluation Center.
- [Windows Server 2019](https://www.microsoft.com/en-in/evalcenter/evaluate-windows-server-2019)
- [Windows Server 2022](https://www.microsoft.com/en-in/evalcenter/evaluate-windows-server-2022-preview)

### Database servers

SharePoint Server requires SQL Server 2019 for its databases. Earlier versions of SQL Server are not supported.
You can download evaluation copies of SQL Server 2019 from the Microsoft Evaluation Center.

- [SQL Server 2019](https://www.microsoft.com/en-in/evalcenter/evaluate-sql-server-2019)
  
