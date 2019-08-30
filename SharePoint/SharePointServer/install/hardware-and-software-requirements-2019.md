---
title: "Hardware and software requirements for SharePoint Server 2019"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/24/2018
audience: ITPro
ms.topic: interactive-tutorial
ms.prod: sharepoint-server-itpro
localization_priority: Priority
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
- SP2019
ms.custom: 
ms.assetid: 4d88c402-24f2-449b-86a6-6e7afcfec0cd
description: "Find out the minimum hardware and software requirements you need to install and run SharePoint Server."
---

# Hardware and software requirements for SharePoint Server 2019

[!INCLUDE[appliesto-xxx-xxx-2019-xxx-md](../includes/appliesto-xxx-xxx-2019-xxx-md.md)] 
  
> [!IMPORTANT]
> If you contact Microsoft Customer Support Services about a production system that does not meet the minimum hardware specifications described in this document, support will be limited until the system is upgraded to the minimum requirements. 
  
    
## Hardware requirements: Location of physical servers
<a name="hwLocServers"> </a>

Some enterprises have datacenters that are in close proximity to one another and connected by high-bandwidth fiber optic links. In this environment, you can configure the two datacenters as a single farm. This distributed farm topology is called a stretched farm. Stretched farms for SharePoint Server 2019 are supported. 
  
For a stretched farm architecture to work as a supported high-availability solution, the following prerequisites must be met:
  
- There is a highly consistent intra-farm latency of \<1 ms one way, 99.9% of the time over a period of ten minutes. (Intra-farm latency is commonly defined as the latency between the front-end web servers and the database servers.)
    
- The bandwidth speed must be at least 1 gigabit per second.
    
To provide fault tolerance in a stretched farm, use the standard best practice guidance to configure redundant service applications and databases.
  
> [!NOTE]  
> The intra-farm latency of \<1 ms one way, 99,9% of the time over a period of ten minutes is also required for SharePoint environments with servers that are located in the same datacenter. The bandwidth speed should also be in this case at least 1 gigabit per second.
  
## Hardware requirements: SharePoint Servers and MinRole installations
<a name="hwforwebserver"> </a>

The values in the following table are minimum values for installations on servers that are running SharePoint Server 2019 in a multiple server farm installation.
  
For all installation scenarios, you must have sufficient hard disk space for the base installation and sufficient space for diagnostics such as logging, debugging, creating memory dumps, and so on. For production use, you must also have additional free disk space for day-to-day operations. In addition, maintain two times as much free space as you have RAM for production environments.
  
For information about hardware and software requirements for Microsoft SQL Server 2016 or higher, see [Hardware and Software Requirements for Installing SQL Server](/sql/sql-server/install/hardware-and-software-requirements-for-installing-sql-server?view=sql-server-2017).
  
|**Installation scenario**|**Deployment type and scale**|**RAM**|**Processor**|**Hard disk space**|
|:-----|:-----|:-----|:-----|:-----|
|Single server role that uses SQL Server  <br/> |Development or evaluation installation of SharePoint Server 2019 with the minimum recommended services for development environments. Use the Single-Server farm role that will let you choose which service applications to provision. For additional information on Single-Server farm role, see [Overview of MinRole Server Roles in SharePoint Server](overview-of-minrole-server-roles-in-sharepoint-server.md) <br/> |16 GB  <br/> |64-bit, 4 cores  <br/> |80 GB for system drive  <br/> 100 GB for second drive  <br/> |
|Single server role that uses SQL Server  <br/> |Pilot or user acceptance test installation of SharePoint Server 2019 running all available services for development environments.  <br/> |24 GB  <br/> |64-bit, 4 cores  <br/> |80 GB for system drive  <br/> 100 GB for second drive and additional drives  <br/> |
|Web server or application server in a three-tier farm  <br/> |Development or evaluation installation of SharePoint Server 2019 with a minimum number of services.  <br/> |12 GB  <br/> |64-bit, 4 cores  <br/> |80 GB for system drive  <br/> 80 GB for second drive  <br/> |
|Web server or application server in a three-tier farm  <br/> |Pilot, user acceptance test, or production deployment of SharePoint Server 2019 running all available services.  <br/> |16 GB  <br/> |64-bit, 4 cores  <br/> |80 GB for system drive  <br/> 80 GB for second drive and additional drives  <br/> |
   
## Deployment requirements: Farm Topology
<a name="hwforwebserver"> </a>

For information about how to plan for a server deployment, see [Planning for a MinRole server deployment in SharePoint Server 2019](planning-for-a-minrole-server-deployment-in-sharepoint-server.md).
  
## Software requirements for SharePoint Server 2019
<a name="section4"> </a>

The requirements in the following section apply to the following installations:
  
- Server farm with a single server in the farm
    
- Server farm with multiple servers in the farm
    
  
> [!NOTE]
> SharePoint Server 2019 supports drives that are formatted with the Resilient File System (ReFS). For additional information about ReFs, see [Resilient File System Overview](https://go.microsoft.com/fwlink/p/?LinkId=618431) and [Resilient File System](https://go.microsoft.com/fwlink/p/?LinkId=618432)

> [!IMPORTANT]
> SharePoint Server 2019 requires a minimum of an Active Directory 2003 native forest and domain functional level.
  
> [!IMPORTANT]
> SharePoint Server 2019 does not support single label domain names. For more information, see [Information about configuring Windows for domains with single-label DNS names](https://go.microsoft.com/fwlink/p/?LinkID=193849). 
  
The Microsoft SharePoint Products Preparation Tool can assist you in the installation of the software prerequisites for SharePoint Server 2019. Ensure that you have an Internet connection because some prerequisites are installed from the Internet.
  
### Minimum software requirements for SharePoint Server 2019

This section provides minimum software requirements for each server in the farm.
  
#### Minimum requirements for a database server in a farm

One of the following:
  
- Microsoft SQL Server 2016 RTM Standard or Enterprise Editions
    
- Microsoft SQL Server 2017 RTM Standard or Enterprise Editions for Windows

- Microsoft Azure SQL Managed Instance (MI) - For more information, see [Deploy Azure SQL Managed Instance with SharePoint Servers 2016 and 2019](../administration/deploy-azure-sql-managed-instance-with-sharepoint-servers-2016-2019.md).
    
> [!NOTE]
> SQL Server products and all future public updates are supported through the SQL Server product lifecycle. 
  

> [!NOTE]
> SQL Server Express is not supported. Azure SQL Database (the DBaaS service) is also not supported for any SharePoint databases 
  
One of the following server operating systems:
  
- Windows Server 2016 Standard or Datacenter
    
- Windows Server 2019 Standard or Datacenter 
    
#### Minimum requirements for SharePoint servers in a farm

One of the following server operating systems:
  
- Windows Server 2016 Standard or Datacenter (Desktop Experience)
    
- Windows Server 2019 Standard or Datacenter (Desktop Experience)

> [!NOTE]
> We don't support installing or upgrading SharePoint 2019 RTM on a server that previously hosted a prerelease version of SharePoint. A new server build is required to host SharePoint 2019 RTM.

> [!NOTE]
> We don't support installing the Office 2019 client and SharePoint Server 2019 on the same computer. 

> [!NOTE]
> The minimum supported version is Office 2010 client.
  
> [!IMPORTANT]
> The Microsoft SharePoint Products Preparation Tool might not be able to install **Microsoft .NET Framework version 3.5** automatically. In this case you need to manually install the **.NET Framework 3.5 Feature** Windows Feature as a prerequisite using the Windows Server install media.

The Microsoft SharePoint Products Preparation Tool installs the following prerequisites on SharePoint servers in a farm:
  
- Web Server (IIS) role

- Windows Process Activation Service feature
    
- Microsoft .NET Framework version 3.5
    
- Microsoft .NET Framework version 4.7.2
    
- Microsoft SQL Server 2012 Service Pack 4 Native Client
    
- Microsoft WCF Data Services 5.6
    
- Microsoft Identity Extensions
    
- Microsoft Information Protection and Control Client 2.1 (MSIPC)
    
- Microsoft Sync Framework Runtime v1.0 SP1 (x64)
    
- Windows Server AppFabric 1.1
    
- Cumulative Update Package 7 for Microsoft AppFabric 1.1 for Windows Server (KB 3092423)

- Visual C++ Redistributable Package for Visual Studio 2012
    
- Visual C++ Redistributable Package for Visual Studio 2017
    
    >[!NOTE]
    >The required software above will be supported when used by SharePoint via the SharePoint Product Lifecycle.
    
#### Minimum requirements for client computers

- A supported browser. For more information, see [Plan browser support in SharePoint Server 2019](browser-support-planning-0.md).

## Manually configure Windows Server Roles and Features
To manually configure the required Windows Server Roles and Features, you can use one of two methods: 1. Server Manager 2. Microsoft PowerShell

To configure by using Server Manager, see [Install or Uninstall Roles, Role Services, or Features](/windows-server/administration/server-manager/install-or-uninstall-roles-role-services-or-features)


To configure by using PowerShell:

From a PowerShell command prompt window, type:

```Install-WindowsFeature NET-HTTP-Activation,NET-Non-HTTP-Activ,NET-WCF-Pipe-Activation45,NET-WCF-HTTP-Activation45,Web-Server,Web-WebServer,Web-Common-Http,Web-Static-Content,Web-Default-Doc,Web-Dir-Browsing,Web-Http-Errors,Web-App-Dev,Web-Asp-Net,Web-Asp-Net45,Web-Net-Ext,Web-Net-Ext45,Web-ISAPI-Ext,Web-ISAPI-Filter,Web-Health,Web-Http-Logging,Web-Log-Libraries,Web-Request-Monitor,Web-Http-Tracing,Web-Security,Web-Basic-Auth,Web-Windows-Auth,Web-Filtering,Web-Performance,Web-Stat-Compression,Web-Dyn-Compression,Web-Mgmt-Tools,Web-Mgmt-Console,WAS,WAS-Process-Model,WAS-NET-Environment,WAS-Config-APIs,Windows-Identity-Foundation,Xps-Viewer -IncludeManagementTools -Verbose```

> [!NOTE]
> Some Windows features being installed are “Features On Demand (FOD)”, which are downloaded from Windows Update.  If the computer doesn’t have access to Windows Update, you can specify local installation files by adding the **Source** parameter and pointing to the \sources\sxs folder on the Windows Server installation media.
>
> For example: -Source D:\sources\sxs

    
## Optional software supported in SharePoint Server 2019
<a name="OptionalSoftware"> </a>

The optional software in this section is supported but is not required to install or use SharePoint Server 2019. This software might be required by capabilities such as business intelligence.
  
|**Environment**|**Optional software**|
|:-----|:-----|
|Single server farm, front-end web servers, and application servers in a farm  <br/> | .NET Framework Data Provider for SQL Server (part of Microsoft .NET Framework)  <br/>  .NET Framework Data Provider for OLE DB (part of Microsoft .NET Framework)  <br/>  SharePoint Workflow Manager  <br/>  You can install SharePoint Workflow Manager on a dedicated computer.  <br/>  Microsoft SQL Server 2008 R2 Reporting Services Add-in for Microsoft SharePoint Technologies  <br/>  This add-in is used by Access Services for SharePoint Server 2019.  <br/>  Microsoft SQL Server 2012 Data-Tier Application (DAC) Framework 64-bit edition  <br/>  Microsoft SQL Server 2012 Transact-SQL ScriptDom 64-bit edition  <br/>  Microsoft System CLR Types for Microsoft SQL Server 2012 64-bit edition  <br/>  Microsoft SQL Server 2012 with SP1 LocalDB 64-bit edition  <br/>  Microsoft Data Services for the .NET Framework 4 and Silverlight 4 (formerly ADO.NET Data Services)  <br/>  Exchange Web Services Managed API, version 1.2  <br/>  |
   
## Links to applicable software
<a name="section5"> </a>

To install Windows Server 2016 or higher, SQL Server 2016 or higher, or SharePoint Server 2019, you can go to the websites that are listed in this section. You can install most software prerequisites through the SharePoint Server 2019 Start page. The software prerequisites are also available from websites that are listed in this section. You can enable the Web Server (IIS) role in Server Manager.
  
In scenarios where installing prerequisites directly from the Internet is not possible, you can download the prerequisites and then install them from a network share. For more information, see [Install prerequisites for SharePoint Server from a network share](install-prerequisites-from-network-share.md).
  
- [SharePoint Server 2019](https://go.microsoft.com/fwlink/?LinkId=2006095)
    
- [Language Packs for SharePoint Server 2019](https://go.microsoft.com/fwlink/?LinkId=2006096)
    
- [Windows Server 2016](https://www.microsoft.com/evalcenter/evaluate-windows-server-2016)
    
- [Windows Server 2019](https://www.microsoft.com/evalcenter/evaluate-windows-server-2019)
    
- [Microsoft SQL Server 2016](https://www.microsoft.com/evalcenter/evaluate-sql-server-2016) 

- [Microsoft SQL Server 2017 RTM](https://www.microsoft.com/evalcenter/evaluate-sql-server-2017-rtm)
    
- [Microsoft .NET Framework version 4.7.2](https://www.microsoft.com/net/download/dotnet-framework-runtime)
    
- [Microsoft WCF Data Services 5.6](https://go.microsoft.com/fwlink/p/?LinkId=320724 )
    
- [Microsoft Information Protection and Control Client (MSIPC)](https://go.microsoft.com/fwlink/p/?LinkId=544913)
   
- [Microsoft SQL Server 2012 SP4 Feature Pack - Native Client \x64\sqlncli.msi](https://www.microsoft.com/download/details.aspx?id=56041)
    
- [Microsoft Sync Framework Runtime v1.0 SP1 (x64)](https://go.microsoft.com/fwlink/p/?LinkId=618411)
    
- [Windows Server AppFabric 1.1](https://go.microsoft.com/fwlink/p/?LinkId=618412)
    
- [Cumulative Update Package 7 for AppFabric 1.1 for Windows Server](https://support.microsoft.com/kb/3092423)

- [Visual C++ Redistributable Package for Visual Studio 2012](https://go.microsoft.com/fwlink/?LinkId=627156)
    
- [Visual C++ Redistributable Package for Visual Studio 2017](https://visualstudio.microsoft.com/downloads/)
    
- [Exchange Web Services Managed API, version 1.2](https://go.microsoft.com/fwlink/p/?linkid=238668)
    
- [Microsoft Identity Extensions](https://go.microsoft.com/fwlink/?LinkId=252368)
    
## Prerequisite installer operations and command-line options
<a name="section7"> </a>

The SharePoint Server 2019 prerequisite installer (prerequisiteinstaller.exe) installs the following software, if it has not already been installed on the target server, in the following order:
  
1. Web Server (IIS) Role
    
2. Microsoft SQL Server 2012 SP4 Native Client
    
3. Microsoft Sync Framework Runtime v1.0 SP1 (x64)
    
4. Windows Server AppFabric 1.1
    
5. Microsoft Identity Extensions
    
6. Microsoft Information Protection and Control Client 2.1
    
7. Microsoft WCF Data Services 5.6
    
8. Microsoft .NET Framework 4.7.2
    
9. Cumulative Update Package 7 for Microsoft AppFabric 1.1 for Windows Server (KB 3092423)

10. Visual C++ Redistributable Package for Visual Studio 2012
    
11. Visual C++ Redistributable Package for Visual Studio 2017
   
    
You can run prerequisiteinstaller.exe at a command prompt with the following options. When you run prerequisiteinstaller.exe at a command prompt, you might be asked to restart the server one or more times during the installation process. After restarting, you should continue the prerequisite installation by running prerequisiteinstaller.exe with the /continue option.
  
- /? This displays command-line options.
    
- /continue This is used to tell the installer that it is continuing from being restarted.
    
- /unattended This indicates no user interaction.
    
The installer installs from the file that you specify in the command-line options described in the following list. In this list, < _file_> signifies the file from which you want to install. If you do not specify the < _file_> option, the installer downloads the file from the Internet and installs it. If the option does not apply to the current operating system, it is ignored.
  
- **/SQLNCli:<_file_>** Install Microsoft SQL Server 2012 SP4 Native Client from <_file_>.
    
- **/Sync:<_file_>** Install Microsoft Sync Framework Runtime SP1 v1.0 (x64) from <_file_>.
    
- **/AppFabric:<_file_>** Install Windows Server AppFabric from <_file_> (AppFabric must be installed with the options /i CacheClient,CachingService,CacheAdmin /gac).

- **/IDFX11:<_file_>** Install Microsoft Identity Extensions from <_file_>.
   
- **/MSIPCClient:<_file_>** Install Microsoft Information Protection and Control Client from <_file_>.

- **/KB3092423:<_file_>** Install Cumulative Update Package 7 for Microsoft AppFabric 1.1 for Windows Server (KB3092423) from <_file_>.
    
- **/WCFDataServices56:<_file_>** Install Microsoft WCF Data Services 5.6 from <_file_>.
    
- **/DotNet472:<_file_>** Install Microsoft .NET Framework 4.7.2 from <_file_>.
    
- **/MSVCRT11:<_file_>** Install Visual C++ Redistributable Package for Visual Studio 2012 from <_file_>.

- **/MSVCRT141:<_file_>** Install Visual C++ Redistributable Package for Visual Studio 2017 from <_file_>.
    
   
### Installation options

Certain prerequisites are installed by the prerequisite installer with specific options. Those prerequisites with specific installation options are listed below with the options that are used by the prerequisite installer.
  
- Windows AppFabric
    
    /i CacheClient,CachingService,CacheAdmin /gac
    
- Microsoft WCF Data Services
    
    /quiet
    
The prerequisite installer creates log files at %TEMP%\prerequisiteinstaller.\<date\>.\<time\>.log. You can check these log files for specific details about all changes the installer makes to the target computer.
