---
title: Hardware and software requirements for SharePoint 2013
ms.prod: SHAREPOINT
ms.assetid: a88d3f72-7ac3-4f08-b302-c4ca0a796268
---


# Hardware and software requirements for SharePoint 2013
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint 2013, SharePoint Foundation 2013, SharePoint Server 2013*  * **Topic Last Modified:** 2017-07-18* **Summary:** Lists the minimum hardware and software requirements to install and run SharePoint 2013.
> [!IMPORTANT:]

  
    
    

In this article:
-  [Overview](hardware-and-software-requirements-for-sharepoint-server-2016.md#section1)
    
  
-  [Hardware and software requirements for other SharePoint 2013 capabilities](hardware-and-software-requirements-for-sharepoint-server-2016.md#reqOtherCap)
    
  
-  [Hardware requirements—location of physical servers](hardware-and-software-requirements-for-sharepoint-server-2016.md#hwLocServers)
    
  
-  [Hardware requirements—web servers, application servers, and single server installations](hardware-and-software-requirements-for-sharepoint-server-2016.md#hwforwebserver)
    
  
-  [Hardware requirements—database servers](hardware-and-software-requirements-for-sharepoint-server-2016.md#section3)
    
  
-  [Software requirements](hardware-and-software-requirements-for-sharepoint-server-2016.md#section4)
    
  
-  [Optional software](hardware-and-software-requirements-for-sharepoint-server-2016.md#OptionalSoftware)
    
  
-  [Links to applicable software](hardware-and-software-requirements-for-sharepoint-server-2016.md#section5)
    
  
-  [Prerequisite installer operations and command line-options](hardware-and-software-requirements-for-sharepoint-server-2016.md#section7)
    
  

> [!IMPORTANT:]

  
    
    


## Overview
<a name="section1"> </a>

SharePoint 2013 provides for several installation scenarios. Currently, these installations include single server with built-in database installations, single-server farm installations, and multiple-server farm installations. This article describes the hardware and software requirements for SharePoint 2013 in each of these scenarios.
## Hardware and software requirements for other SharePoint 2013 capabilities
<a name="reqOtherCap"> </a>

If you plan to use capabilities that are offered through SharePoint 2013 or through other integration channels, such as SQL Server or Exchange Server, you also need to meet the hardware and software requirements that are specific to that capability. The following list provides links to hardware and software requirements for some SharePoint 2013 capabilities:
- **Software requirements for Project Server 2016**
    
  
- For eDiscovery, each front-end web server must have the Exchange Web Services Managed API, version 1.2 installed. For more information, see the following articles:
    
  -  [Configure eDiscovery in SharePoint Server](html/configure-ediscovery-in-sharepoint-server.md)
    
  
  -  [Configure Exchange for SharePoint eDiscovery Center](https://technet.microsoft.com/en-us/library/jj218665%28v=exchg.150%29)
    
  
-  [Software requirements for business intelligence in SharePoint Server](html/software-requirements-for-business-intelligence-in-sharepoint-server.md)
    
  
- Hardware requirements for search in UNRESOLVED_TOKEN_VAL(SharePoint Server 2013):
    
  -  [Step 3: Which hardware requirements should I be aware of?](plan-enterprise-search-architecture-in-sharepoint-server-2016.md#BKMK_AssignHW)
    
  
  -  [Hardware requirements for search topologies for Internet sites](scale-search-for-internet-sites-in-sharepoint-server.md#HW_FIS)
    
  
-  [Mobile device browsers supported in SharePoint 2013](html/mobile-device-browsers-supported-in-sharepoint-2013.md)
    
  

## Hardware requirements—location of physical servers
<a name="hwLocServers"> </a>

Some enterprises have data centers that are located in close proximity to one another and are connected by high-bandwidth fiber optic links. In this environment it is possible to configure the two data centers as a single farm. This distributed farm topology is called a  *stretched*  farm. Stretched farms for SharePoint 2013 are supported as of April 2013.For a stretched farm architecture to work as a supported high-availability solution, the following prerequisites must be met:
- There is a highly consistent intra-farm latency of <1ms one way, 99.9% of the time over a period of ten minutes. (Intra-farm latency is commonly defined as the latency between the front-end web servers and the database servers.)
    
  
- The bandwidth speed must be at least 1 gigabit per second. 
    
  
To provide fault tolerance in a stretched farm, use the standard best practice guidance to configure redundant service applications and databases. For more information, see  [Create a high availability architecture and strategy for SharePoint Server](html/create-a-high-availability-architecture-and-strategy-for-sharepoint-server.md).
## Hardware requirements—web servers, application servers, and single server installations
<a name="hwforwebserver"> </a>

The values in the following table are minimum values for installations on a single server with a built-in database and for web and application servers that are running SharePoint 2013 in a multiple server farm installation. For all installation scenarios, you must have sufficient hard disk space for the base installation and sufficient space for diagnostics such as logging, debugging, creating memory dumps, and so on. For production use, you must also have additional free disk space for day-to-day operations. In addition, maintain two times as much free space as you have RAM for production environments. For more information, see  [Capacity management and sizing for SharePoint Server 2013](https://go.microsoft.com/fwlink/p/?LinkID=95812).
### 

Installation ScenarioDeployment type and scaleRAMProcessorHard disk spaceSingle server with a built-in database or single server that uses SQL Server  <br/> Development or evaluation installation of SharePoint Server 2013 or SharePoint Foundation 2013 with the minimum recommended services for development environments. For information, see  [Minimum recommended services for development environments](hardware-and-software-requirements-for-sharepoint-server-2016.md#MinimumRecDev).  <br/> 8 GB  <br/> 64-bit, 4 cores  <br/> 80 GB for system drive  <br/> Single server with a built-in database or single server that uses SQL Server  <br/> Development or evaluation installation of SharePoint Server 2013 or SharePoint Foundation 2013 running Visual Studio 2012 and the minimum recommended services for development environments. For information, see  [Minimum recommended services for development environments](hardware-and-software-requirements-for-sharepoint-server-2016.md#MinimumRecDev).  <br/> 10 GB  <br/> 64-bit, 4 cores  <br/> 80 GB for system drive  <br/> Single server with a built-in database or single server that uses SQL Server  <br/> Development or evaluation installation of SharePoint Server 2013 running all available services.  <br/> 24 GB  <br/> 64-bit, 4 cores  <br/> 80 GB for system drive  <br/> Web server or application server in a three-tier farm  <br/> Pilot, user acceptance test, or production deployment of SharePoint Server 2013 or SharePoint Foundation 2013.  <br/> 12 GB  <br/> 64-bit, 4 cores  <br/> 80 GB for system drive  <br/> 
## Hardware requirements—database servers
<a name="section3"> </a>

The requirements in the following table apply to database servers in environments that have multiple servers in the farm. 
> [!NOTE:]

  
    
    


### 

ComponentMinimum requirementProcessor  <br/>  64-bit, 4 cores for small deployments (fewer than 1,000 users) <br/>  64-bit, 8 cores for medium deployments (between 1,000 to 10,000 users) <br/> RAM  <br/>  8 GB for small deployments (fewer than 1,000 users) <br/>  16 GB for medium deployments (between 1,000 to 10,000 users) <br/>  For large deployments over 10,000 users, see the "Estimate memory requirements" section in [Storage and SQL Server capacity planning and configuration (SharePoint Server 2010)](https://go.microsoft.com/fwlink/p/?LinkID=119416). This document does not apply to search in SharePoint 2013.  <br/>  These values are larger than those recommended as the minimum values for SQL Server because of the distribution of data that is required for a SharePoint 2013 environment. For more information about SQL Server system requirements, see [Hardware and Software Requirements for Installing SQL Server 2008 R2](https://go.microsoft.com/fwlink/p/?LinkId=238814).  <br/> Hard disk  <br/> 80 GB for system drive  <br/> Hard disk space depends on how much content that you have in your deployment. For information about how to estimate the amount of content and other databases for your deployment, see  [Storage and SQL Server capacity planning and configuration (SharePoint Server 2010)](https://go.microsoft.com/fwlink/p/?LinkID=119416).  <br/> 
## Software requirements
<a name="section4"> </a>

The requirements in the following section apply to the following installations: 
- Single server with built-in database
    
  
- Server farm with a single server in the farm
    
  
- Server farm with multiple servers in the farm
    
  

> [!IMPORTANT:]

  
    
    

The Microsoft SharePoint Products Preparation Tool can assist you in the installation of the software prerequisites for SharePoint 2013. Ensure that you have an Internet connection, because some prerequisites are installed from the Internet. For more information about how to use the Microsoft SharePoint Products Preparation Tool, see **Install SharePoint 2013 across multiple servers for a three-tier farm** and **Install SharePoint 2013 across multiple servers for a three-tier farm**.
> [!NOTE:]

  
    
    


> [!NOTE:]

  
    
    


## Minimum software requirements

This section provides minimum software requirements for each server in the farm.Minimum requirements for a database server in a farm:
- One of the following:
    
  - The 64-bit edition of Microsoft SQL Server 2012.
    
  
  - The 64-bit edition of SQL Server 2008 R2 Service Pack 1
    
  
- The 64-bit edition of Windows Server 2008 R2 Service Pack 1 (SP1) Standard, Enterprise, or Datacenter or the 64-bit edition of Windows Server 2012 Standard or Datacenter
    
  
- The SharePoint parsing process crashes in Windows Server 2008 R2 (KB 2554876)
    
  
- FIX: IIS 7.5 configurations are not updated when you use the ServerManager class to commit configuration changes (KB 2708075)
    
  
- Hotfix: ASP.NET (SharePoint) race condition in .NET 4.5 RTM:
    
  - Windows Server 2008 R2 SP1 (KB 2759112)
    
  
  - Windows Server 2012 (KB 2765317)
    
  
- Microsoft .NET Framework version 4.5
    
  
Minimum requirements for a single server with built-in database:
> [!NOTE:]

  
    
    


- The 64-bit edition of Windows Server 2008 R2 Service Pack 1 (SP1) Standard, Enterprise, or Datacenter or the 64-bit edition of Windows Server 2012 R2 Standard or Datacenter
    
    > [!NOTE:]
      
- The SharePoint parsing process crashes in Windows Server 2008 R2 (KB 2554876)
    
  
- FIX: IIS 7.5 configurations are not updated when you use the ServerManager class to commit configuration changes (KB 2708075)
    
  
- Hotfix: ASP.NET (SharePoint) race condition in .NET 4.5 RTM: 
    
  - Windows Server 2008 R2 SP1 (KB 2759112)
    
  
  - Windows Server 2012 (KB 2765317)
    
  
- The Setup program installs the following prerequisite for a single server with built-in database:
    
  - Microsoft SQL Server 2008 R2 SP1 - Express Edition
    
  
- The Microsoft SharePoint Products Preparation Tool installs the following prerequisites for a single server with built-in database:
    
  - Web Server (IIS) role
    
  
  - Application Server role
    
  
  - Microsoft .NET Framework version 4.5
    
  
  - SQL Server 2008 R2 SP1 Native Client
    
  
  - Microsoft WCF Data Services 5.0
    
  
  - Microsoft Information Protection and Control Client (MSIPC)
    
  
  - Microsoft Sync Framework Runtime v1.0 SP1 (x64)
    
  
  - Windows Management Framework 3.0 which includes Microsoft PowerShell 3.0
    
  
  - Windows Identity Foundation (WIF) 1.0 and Microsoft Identity Extensions (previously named WIF 1.1)
    
  
  - Windows Server AppFabric
    
  
  - Cumulative Update Package 1 for Microsoft AppFabric 1.1 for Windows Server (KB 2671763)
    
  
Minimum requirements for front-end web servers and application servers in a farm:
> [!NOTE:]

  
    
    


- The 64-bit edition of Windows Server 2008 R2 Service Pack 1 (SP1) Standard, Enterprise, or Datacenter or the 64-bit edition of Windows Server 2012 R2 Standard or Datacenter.
    
    > [!NOTE:]
      
- The SharePoint parsing process crashes in Windows Server 2008 R2 (KB 2554876) 
    
  
- FIX: IIS 7.5 configurations are not updated when you use the ServerManager class to commit configuration changes (KB 2708075)
    
  
- Hotfix: ASP.NET (SharePoint) race condition in .NET 4.5 RTM: 
    
  - Windows Server 2008 R2 SP1 (KB 2759112)
    
  
  - Windows Server 2012 (KB 2765317)
    
  
- The Microsoft SharePoint Products Preparation Tool installs the following prerequisites for front-end web servers and application servers in a farm:
    
  - Web Server (IIS) role
    
  
  - Application Server role
    
  
  - Microsoft .NET Framework version 4.5
    
  
  - SQL Server 2008 R2 SP1 Native Client
    
  
  - Microsoft WCF Data Services 5.0
    
  
  - Microsoft Information Protection and Control Client (MSIPC)
    
  
  - Microsoft Sync Framework Runtime v1.0 SP1 (x64)
    
  
  - Windows Management Framework 3.0 which includes Microsoft PowerShell 3.0
    
  
  - Windows Identity Foundation (WIF) 1.0 and Microsoft Identity Extensions (previously named WIF 1.1)
    
  
  - Windows Server AppFabric
    
  
  - Cumulative Update Package 1 for Microsoft AppFabric 1.1 for Windows Server (KB 2671763)
    
  

#### Minimum requirements for client computers


- A supported browser. For more information, see  [Plan browser support in SharePoint 2013](html/plan-browser-support-in-sharepoint-2013.md). For information on browsers supported on mobile devices, see  [Mobile device browsers supported in SharePoint 2013](html/mobile-device-browsers-supported-in-sharepoint-2013.md).
    
  

#### Minimum recommended services for development environments
<a name="MinimumRecDev"> </a>

The following are the minimum SharePoint 2013 services and service applications that are recommended for development environments:
- App Management service application
    
  
- Central Administration web site
    
  
- Claims to Windows Token service (C2WTS)
    
  
- Distributed cache service
    
  
- Microsoft SharePoint Foundation 2013 Site and Subscription Settings service
    
  
- Secure Store Service
    
  
- User Profile service application (UNRESOLVED_TOKEN_VAL(SharePoint Server 2013) only)
    
  

## Optional software
<a name="OptionalSoftware"> </a>

The optional software in this section is supported but is not required to install or use SharePoint 2013. This software might be required by capabilities such as business intelligence. For more information about system requirements for other capabilities, see  [Hardware and software requirements for other SharePoint 2013 capabilities](hardware-and-software-requirements-for-sharepoint-server-2016.md#reqOtherCap).
### 

EnvironmentOptional softwareSingle server with built-in database, front-end web servers, and application servers in a farm  <br/>  .NET Framework Data Provider for SQL Server (part of Microsoft .NET Framework) <br/>  .NET Framework Data Provider for OLE DB (part of Microsoft .NET Framework) <br/>  Workflow Manager <br/>  You can install Workflow Manager on a dedicated computer. <br/>  Microsoft SQL Server 2008 R2 Reporting Services Add-in for Microsoft SharePoint Technologies <br/>  This add-in is used by Access Services for SharePoint Server 2016. <br/>  Microsoft SQL Server 2012 Data-Tier Application (DAC) Framework 64-bit edition <br/>  Microsoft SQL Server 2012 Transact-SQL ScriptDom 64-bit edition <br/>  Microsoft System CLR Types for Microsoft SQL Server 2012 64-bit edition <br/>  Microsoft SQL Server 2012 with Service Pack 1 (SP1) LocalDB 64-bit edition <br/>  Microsoft Data Services for the .NET Framework 4 and Silverlight 4 (formerly ADO.NET Data Services) <br/>  Exchange Web Services Managed API, version 1.2 <br/>  Microsoft SQL Server 2008 R2 Remote Blob Store which is part of the Microsoft SQL Server 2008 R2 Feature Pack <br/>  SQL Server 2008 R2 Analysis Services ADOMD.NET <br/>  KB 2472264 <br/>  If you are running a geo-distributed deployment and your servers are running Windows Server 2008 R2, then installing KB 2472264 can optimize network latency in a dedicated datacenter network. For more information, and to download the software, see [You cannot customize some TCP configurations by using the netsh command in Windows Server 2008 R2](https://go.microsoft.com/fwlink/p/?LinkId=254821).  <br/> Client computer  <br/>  Windows 7 <br/>  For information about how to use Windows 7 with SharePoint 2013 in a development environment, see [Start: Set up the development environment for SharePoint 2013](https://msdn.microsoft.com/en-us/library/ee554869%28v=office.15%29.aspx).  <br/>  Silverlight 3 <br/>  Office 2016 <br/>  Microsoft Office 2010 with Service Pack 2 <br/>  With [KB 2553248](https://go.microsoft.com/fwlink/p/?LinkID=254211) <br/>  Microsoft Office 2007 with Service Pack 2 <br/>  With [KB 2583910](https://go.microsoft.com/fwlink/p/?LinkID=254212) <br/>  Microsoft Office for Mac 2011 with Service Pack 1 <br/>  Microsoft Office 2008 for Mac version 12.2.9 <br/>  Support ends April 9, 2013. <br/> 
## Links to applicable software
<a name="section5"> </a>

To install Windows Server 2008 R2 SP1, Windows Server 2012, SQL Server, or SharePoint 2013, you can go to the web sites that are listed in this section. You can install most software prerequisites through the SharePoint 2013 Start page. The software prerequisites are also available from web sites that are listed in this section. You can enable the Web Server (IIS) role and the Application Server role in Server Manager.In scenarios where installing prerequisites directly from the Internet is not possible you can download the prerequisites and then install them from a network share. For more information, see  [Install prerequisites for SharePoint Server from a network share](html/install-prerequisites-for-sharepoint-server-from-a-network-share.md).
-  [Windows 7 and Windows Server 2008 R2 Service Pack 1 (SP1) (KB 976932)](https://go.microsoft.com/fwlink/p/?LinkId=214566)
    
  
-  [Microsoft SharePoint Server 2013](https://go.microsoft.com/fwlink/p/?LinkId=258858)
    
  
-  [Microsoft SharePoint Foundation 2013](https://go.microsoft.com/fwlink/p/?LinkId=258859)
    
  
-  [Office 365 Enterprise](https://go.microsoft.com/fwlink/p/?LinkId=258856)
    
  
-  [The SharePoint parsing process crashes in Windows Server 2008 R2 (KB 2554876)](https://go.microsoft.com/fwlink/p/?LinkId=258850)
    
  
-  [FIX: IIS 7.5 configurations are not updated when you use the ServerManager class to commit configuration changes (KB 2708075)](https://go.microsoft.com/fwlink/p/?LinkId=258851)
    
  
- Hotfix: ASP.NET (SharePoint) race condition in .NET 4.5 RTM: 
    
  -  [Windows Server 2008 R2 SP1 (KB 2759112)](https://go.microsoft.com/fwlink/p/?LinkId=267536)
    
  
  -  [Windows Server 2012 and Windows 8 (KB 2765317)](https://go.microsoft.com/fwlink/p/?LinkId=268725)
    
  
-  [Windows Server 2012, Datacenter Edition or Standard Edition](https://go.microsoft.com/fwlink/p/?LinkId=262392)
    
  
-  [Microsoft SQL Server 2008 R2 Service Pack 1](https://go.microsoft.com/fwlink/p/?LinkId=238815)
    
  
-  [Microsoft .NET Framework version 4.5](https://go.microsoft.com/fwlink/p/?LinkId=250950)
    
  
-  [Microsoft SQL Server 2008 R2 SP1 - Express Edition](https://go.microsoft.com/fwlink/p/?LinkId=238818)
    
  
-  [Workflow Manager](https://go.microsoft.com/fwlink/p/?LinkID=252092)
    
  
-  [WCF Data Services 5.0 for OData](https://go.microsoft.com/fwlink/p/?LinkId=238821)
    
  
-  [Microsoft Information Protection and Control Client (MSIPC)](https://go.microsoft.com/fwlink/p/?LinkID=219568)
    
  
-  [Windows Management Framework 3.0](https://go.microsoft.com/fwlink/p/?LinkId=273961) which includes Microsoft PowerShell 3.0
    
  
-  [Microsoft Sync Framework Runtime v1.0 SP1 (x64)](https://go.microsoft.com/fwlink/p/?LinkID=224449)
    
  
-  [Windows Identity Foundation 1.0 for Windows Server 2008 R2](https://go.microsoft.com/fwlink/p/?LinkID=226830)
    
  
-  [Windows Identity Extensions for Windows Server 2008 R2](https://go.microsoft.com/fwlink/p/?linkid=252368)
    
  
-  [Microsoft SQL Server 2008 R2 Feature Pack](https://go.microsoft.com/fwlink/p/?LinkId=254815) which includes the Microsoft SQL Server 2008 R2 SP1 Native Client and the SQL Server Remote BLOB Store
    
  
-  [Microsoft SQL Server 2008 R2 SP1 Feature pack](https://go.microsoft.com/fwlink/p/?linkid=238653) which includes Microsoft SQL Server 2008 R2 ADOMD.NET
    
  
-  [Microsoft Silverlight 3](https://go.microsoft.com/fwlink/p/?LinkId=166506)
    
  
-  [Exchange Web Services Managed API, version 1.2](http://go.microsoft.com/fwlink/p/?linkid=238668)
    
  
- Microsoft SQL Server 2012 Native Client 64-bit edition –  [ENU\\x64\\sqlncli.MSI](https://go.microsoft.com/fwlink/p/?LinkId=239568)
    
  
- Microsoft SQL Server 2012 Data-Tier Application (DAC) Framework 64-bit edition –  [ENU\\x64\\dacframework.msi](https://go.microsoft.com/fwlink/p/?LinkId=238829)
    
  
- Microsoft SQL Server 2012 Transact-SQL ScriptDom 64-bit edition –  [SQLDOM.msi](https://go.microsoft.com/fwlink/p/?LinkId=239635)
    
  
- Microsoft System CLR Types for Microsoft SQL Server 2012 64-bit edition –  [SQLSysClrTypes.msi](https://go.microsoft.com/fwlink/p/?LinkId=239644)
    
  
- Microsoft SQL Server 2012 with Service Pack 1 (SP1) LocalDB 64-bit edition, which is also a component of SQL Server 2012 with Service Pack 1 (SP1) Express –  [ENU\\x64\\SqlLocalDB.msi](http://go.microsoft.com/fwlink/p/?LinkId=262352)
    
  
-  [Microsoft SQL Server 2014](https://technet.microsoft.com/en-us/sqlserver/dn135309.aspx)
    
  

## Prerequisite installer operations and command-line options
<a name="section7"> </a>

The SharePoint 2013 prerequisite installer (prerequisiteinstaller.exe) installs the following software, if it has not already been installed on the target server, in this order:
1. Microsoft .NET Framework version 4.5
    
  
2. Windows Management Framework 3.0
    
  
3. Application Server Role, Web Server (IIS) Role
    
  
4. Microsoft SQL Server 2008 R2 SP1 Native Client
    
  
5. Windows Identity Foundation (KB974405)
    
  
6. Microsoft Sync Framework Runtime v1.0 SP1 (x64)
    
  
7. Windows Identity Extensions
    
  
8. Microsoft Information Protection and Control Client
    
  
9. Microsoft WCF Data Services 5.0
    
  
10. Windows Server AppFabric
    
  
11. Cumulative Update Package 1 for Microsoft AppFabric 1.1 for Windows Server (KB 2671763)
    
  
You can run prerequisiteinstaller.exe at a command prompt with the following options. When you run prerequisiteinstaller.exe at a command prompt, you may be asked to restart the server one or more times during the installation process. After rebooting, you should continue the prerequisite installation by running prerequisiteinstaller.exe with the /continue option.
- /? Display command-line options
    
  
- /continue This is used to tell the installer that it is continuing from a restart
    
  
- /unattended No user interaction
    
  
The installer installs from the file that you specify in the command-line options described in the following list. In this list, < *file*  > signifies the file from which you want to install. If you do not specify the < *file*  > option, the installer downloads the file from the Internet and installs it. If the option does not apply to the current operating system, it is ignored.
- **/SQLNCli:< *file*  >** Install Microsoft SQL Server 2008 SP1 Native Client from < *file*  >
    
  
- **/PowerShell:< *file*  >** Install Windows Management Framework 3.0 from < *file*  >
    
  
- **/NETFX:< *file*  >** Install Microsoft .NET Framework version 4.5 from < *file*  >
    
  
- **/IDFX:< *file*  >** Install Windows Identity Foundation (KB974405) from < *file*  >
    
  
- **/IDFX11:< *file*  >** Install Windows Identity Foundation v1.1 from < *file*  >
    
  
- **/Sync:< *file*  >** Install Microsoft Sync Framework Runtime SP1 v1.0 (x64) from < *file*  >
    
  
- **/AppFabric:< *file*  >** Install Windows Server AppFabric from < *file*  > (AppFabric must be installed with the options /i CacheClient,CachingService,CacheAdmin /gac)
    
  
- **/KB2671763:< *file*  >** Install Microsoft AppFabric 1.1 for Windows Server (AppFabric 1.1) from < *file*  >
    
  
- **/MSIPCClient:< *file*  >** Install Microsoft Information Protection and Control Client from < *file*  >
    
  
- **/WCFDataServices:< *file*  >** Install Microsoft WCF Data Services from < *file*  >
    
  

## Installation options

Certain prerequisites are installed by the prerequisite installer with specific options. Those prerequisites with specific installation options are listed below with the options that are used by the prerequisite installer.
- Windows AppFabric
    
    /i CacheClient,CachingService,CacheAdmin /gac
    
  
- Microsoft WCF Data Services
    
    /quiet
    
  
The prerequisite installer creates log files at %TEMP%\\prerequisiteinstaller.<date>.<time>.log. You can check these log files for specific details about all changes the installer makes to the target computer.
