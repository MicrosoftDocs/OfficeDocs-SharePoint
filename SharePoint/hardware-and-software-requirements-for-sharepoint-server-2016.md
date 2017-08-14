---
title: Hardware and software requirements for SharePoint Server 2016
ms.prod: SHAREPOINT
ms.assetid: 4d88c402-24f2-449b-86a6-6e7afcfec0cd
---


# Hardware and software requirements for SharePoint Server 2016
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-06-06* **Summary:** Find out the minimum hardware and software requirements you need to install and run SharePoint Server 2016.
> [!IMPORTANT:]

  
    
    

In this article:
-  [Hardware requirements—location of physical servers](#hwLocServers)
    
  
-  [Hardware requirements—web servers, application servers, and single server installations](#hwforwebserver)
    
  
-  [Software requirements](#section4)
    
  
-  [Optional software](#OptionalSoftware)
    
  
-  [Links to applicable software](#section5)
    
  
-  [Prerequisite installer operations and command line-options](#section7)
    
  

## Hardware requirements: Location of physical servers
<a name="hwLocServers"> </a>

Some enterprises have datacenters that are in close proximity to one another and connected by high-bandwidth fiber optic links. In this environment, you can configure the two datacenters as a single farm. This distributed farm topology is called a  *stretched*  d farm. Stretched farms for SharePoint Server 2016 are supported.For a stretched farm architecture to work as a supported high-availability solution, the following prerequisites must be met:
- There is a highly consistent intra-farm latency of <1 ms one way, 99.9% of the time over a period of ten minutes. (Intra-farm latency is commonly defined as the latency between the front-end web servers and the database servers.)
    
  
- The bandwidth speed must be at least 1 gigabit per second.
    
  
To provide fault tolerance in a stretched farm, use the standard best practice guidance to configure redundant service applications and databases.Note:﻿The intra-farm latency of <1 ms one way, 99,9% of the time over a period of ten minutes is also required for SharePoint environments with servers that are located in the same datacenter. The bandwidth speed should also be in this case at least 1 gigabit per second.
## Hardware requirements: Web servers, application servers, and MinRole installations
<a name="hwforwebserver"> </a>

The values in the following table are minimum values for installations on a web and application servers that are running SharePoint Server 2016 in a multiple server farm installation.For all installation scenarios, you must have sufficient hard disk space for the base installation and sufficient space for diagnostics such as logging, debugging, creating memory dumps, and so on. For production use, you must also have additional free disk space for day-to-day operations. In addition, maintain two times as much free space as you have RAM for production environments.For information about hardware and software requirements for Microsoft SQL Server 2014, see  [Hardware and Software Requirements for Installing SQL Server 2014](https://technet.microsoft.com/en-us/library/ms143506%28v=sql.120%29.aspx).
### 

Installation scenario Deployment type and scale RAM Processor Hard disk space Single server role that uses SQL Server  <br/> Development or evaluation installation of SharePoint Server 2016 with the minimum recommended services for development environments. Use the Single-Server farm role that will let you choose which service applications to provision. For additional information on Single-Server farm role, see  [Overview of MinRole Server Roles in SharePoint Server 2016](html/overview-of-minrole-server-roles-in-sharepoint-server-2016.md) <br/> 16 GB  <br/> 64-bit, 4 cores  <br/> 80 GB for system drive  <br/> 100 GB for second drive  <br/> Single server role that uses SQL Server  <br/> Pilot or user acceptance test installation of SharePoint Server 2016 running all available services for development environments.  <br/> 24 GB  <br/> 64-bit, 4 cores  <br/> 80 GB for system drive  <br/> 100 GB for second drive and additional drives  <br/> Web server or application server in a three-tier farm  <br/> Development or evaluation installation of SharePoint Server 2016 with a minimum number of services.  <br/> 12 GB  <br/> 64-bit, 4 cores  <br/> 80 GB for system drive  <br/> 80 GB for second drive  <br/> Web server or application server in a three-tier farm  <br/> Pilot, user acceptance test, or production deployment of SharePoint Server 2016 running all available services.  <br/> 16 GB  <br/> 64-bit, 4 cores  <br/> 80 GB for system drive  <br/> 80 GB for second drive and additional drives  <br/> 
## Deployment requirements: Farm Topology
<a name="hwforwebserver"> </a>

For information about how to plan for a server deployment, see  [Planning for a MinRole server deployment in SharePoint Server 2016](html/planning-for-a-minrole-server-deployment-in-sharepoint-server-2016.md).
## Software requirements for SharePoint Server 2016
<a name="section4"> </a>

The requirements in the following section apply to the following installations:
- Server farm with a single server in the farm
    
  
- Server farm with multiple servers in the farm
    
  

> [!NOTE:]

  
    
    


> [!NOTE:]

  
    
    


> [!IMPORTANT:]

  
    
    

The Microsoft SharePoint Products Preparation Tool can assist you in the installation of the software prerequisites for SharePoint Server 2016. Ensure that you have an Internet connection because some prerequisites are installed from the Internet.
## Minimum software requirements for SharePoint Server 2016

This section provides minimum software requirements for each server in the farm.
#### Minimum requirements for a database server in a farm

One of the following:
- The 64-bit edition of Microsoft SQL Server 2014 Service Pack 1 (SP1)
    
  
- Microsoft SQL Server 2016 RTM
    
  

> [!NOTE:]

  
    
    


> [!NOTE:]

  
    
    

One of the following server operating systems:
- Windows Server 2012 R2 Standard or Datacenter
    
  
- Windows Server 2016 Standard or Datacenter
    
  

#### Minimum requirements for SharePoint servers in a farm

One of the following server operating systems:
- Windows Server 2012 R2 Standard or Datacenter
    
  
- Windows Server 2016 Standard or Datacenter
    
  

> [!NOTE:]

  
    
    

The Microsoft SharePoint Products Preparation Tool installs the following prerequisites on SharePoint servers in a farm:
- Web Server (IIS) role
    
  
- Application Server role
    
  
- Microsoft .NET Framework version 4.6
    
  
- Microsoft SQL Server 2012 Service Pack 1 Native Client
    
  
- Microsoft WCF Data Services 5.6
    
  
- Microsoft Identity Extensions 
    
  
- Microsoft Information Protection and Control Client (MSIPC)
    
  
- Microsoft Sync Framework Runtime v1.0 SP1 (x64)
    
  
- Windows Server AppFabric 1.1
    
  
- Cumulative Update Package 7 for Microsoft AppFabric 1.1 for Windows Server (KB 3092423)
    
  
- Microsoft ODBC Driver 11 for SQL Server
    
  
- Visual C++ Redistributable Package for Visual Studio 2012
    
  
- Visual C++ Redistributable Package for Visual Studio 2015
    
  

#### Minimum requirements for client computers


- A supported browser. For more information, see  [Plan browser support in SharePoint Server 2016](html/plan-browser-support-in-sharepoint-server-2016.md).
    
  

## Optional software supported in SharePoint Server 2016
<a name="OptionalSoftware"> </a>

The optional software in this section is supported but is not required to install or use SharePoint Server 2016. This software might be required by capabilities such as business intelligence.
### 

Environment Optional software Single server farm, front-end web servers, and application servers in a farm  <br/>  .NET Framework Data Provider for SQL Server (part of Microsoft .NET Framework) <br/>  .NET Framework Data Provider for OLE DB (part of Microsoft .NET Framework) <br/>  Workflow Manager <br/>  You can install Workflow Manager on a dedicated computer. <br/>  Microsoft SQL Server 2008 R2 Reporting Services Add-in for Microsoft SharePoint Technologies <br/>  This add-in is used by Access Services for SharePoint Server 2016. <br/>  Microsoft SQL Server 2012 Data-Tier Application (DAC) Framework 64-bit edition <br/>  Microsoft SQL Server 2012 Transact-SQL ScriptDom 64-bit edition <br/>  Microsoft System CLR Types for Microsoft SQL Server 2012 64-bit edition <br/>  Microsoft SQL Server 2012 with SP1 LocalDB 64-bit edition <br/>  Microsoft Data Services for the .NET Framework 4 and Silverlight 4 (formerly ADO.NET Data Services) <br/>  Exchange Web Services Managed API, version 1.2 <br/>  Microsoft SQL Server 2008 R2 Remote Blob Store which is part of the Microsoft SQL Server 2008 R2 Feature Pack <br/>  SQL Server 2008 R2 Analysis Services ADOMD.NET <br/> 
## Links to applicable software
<a name="section5"> </a>

To install Windows Server 2012 R2, SQL Server 2014 Service Pack 1 (SP1) , or SharePoint Server 2016, you can go to the websites that are listed in this section. You can install most software prerequisites through the SharePoint Server 2016 Start page. The software prerequisites are also available from websites that are listed in this section. You can enable the Web Server (IIS) role and the Application Server role in Server Manager.In scenarios where installing prerequisites directly from the Internet is not possible, you can download the prerequisites and then install them from a network share. For more information, see  [Install prerequisites for SharePoint Server from a network share](html/install-prerequisites-for-sharepoint-server-from-a-network-share.md).
-  [SharePoint Server 2016](https://go.microsoft.com/fwlink/?linkid=851069)
    
  
-  [Language Packs for SharePoint Server 2016](https://go.microsoft.com/fwlink/?linkid=851068)
    
  
-  [Windows Server 2012 R2](https://go.microsoft.com/fwlink/p/?LinkId=618401)
    
  
-  [Windows Server 2016](https://go.microsoft.com/fwlink/?linkid=830779)
    
  
-  [Office 365 Enterprise](https://go.microsoft.com/fwlink/p/?LinkId=258856)
    
  
-  [Microsoft SQL Server 2014 Service Pack 1 (SP1)](https://go.microsoft.com/fwlink/p/?LinkId=618406)
    
  
-  [Microsoft .NET Framework version 4.6](https://go.microsoft.com/fwlink/?LinkId=722763)
    
  
-  [Microsoft WCF Data Services 5.6](https://go.microsoft.com/fwlink/p/?LinkId=320724 )
    
  
-  [Microsoft Information Protection and Control Client (MSIPC)](https://go.microsoft.com/fwlink/p/?LinkId=544913)
    
  
-  [Microsoft SQL Server 2012 Service Pack 1 (SP1) Native Client (installs with Microsoft SQL Server 2012 Feature Pack)](https://go.microsoft.com/fwlink/p/?LinkId=618409)
    
  
-  [Microsoft ODBC Driver 11 for SQL Server](https://go.microsoft.com/fwlink/p/?LinkId=618410)
    
  
-  [Microsoft Sync Framework Runtime v1.0 SP1 (x64)](https://go.microsoft.com/fwlink/p/?LinkId=618411)
    
  
-  [Windows Server AppFabric 1.1](https://go.microsoft.com/fwlink/p/?LinkId=618412)
    
  
-  [Cumulative Update Package 7 for AppFabric 1.1 for Windows Server](https://support.microsoft.com/en-us/kb/3092423)
    
  
-  [Visual C++ Redistributable Package for Visual Studio 2012](https://go.microsoft.com/fwlink/p/?LinkId=327788)
    
  
-  [Visual C++ Redistributable Package for Visual Studio 2015](https://go.microsoft.com/fwlink/p/?LinkId=620071)
    
  
-  [Microsoft Silverlight 3](https://go.microsoft.com/fwlink/p/?LinkId=166506)
    
  
-  [Exchange Web Services Managed API, version 1.2](https://go.microsoft.com/fwlink/p/?linkid=238668)
    
  
-  [Microsoft Identity Extensions](https://go.microsoft.com/fwlink/?LinkId=252368)
    
  

## Prerequisite installer operations and command-line options
<a name="section7"> </a>

The SharePoint Server 2016 prerequisite installer (prerequisiteinstaller.exe) installs the following software, if it has not already been installed on the target server, in the following order:
1. Application Server Role, Web Server (IIS) Role
    
  
2. Microsoft SQL Server 2012 SP1 Native Client
    
  
3. Microsoft ODBC Driver 11 for SQL Server
    
  
4. Microsoft Sync Framework Runtime v1.0 SP1 (x64)
    
  
5. Windows Server AppFabric 1.1
    
  
6. Microsoft Identity Extensions 
    
  
7. Microsoft Information Protection and Control Client 2.1
    
  
8. Microsoft WCF Data Services 5.6
    
  
9. Microsoft .NET Framework 4.6
    
  
10. Cumulative Update Package 7 for Microsoft AppFabric 1.1 for Windows Server (KB 3092423)
    
  
11. Visual C++ Redistributable Package for Visual Studio 2012
    
  
12. Visual C++ Redistributable Package for Visual Studio 2015
    
  
You can run prerequisiteinstaller.exe at a command prompt with the following options. When you run prerequisiteinstaller.exe at a command prompt, you might be asked to restart the server one or more times during the installation process. After restarting, you should continue the prerequisite installation by running prerequisiteinstaller.exe with the /continue option.
- /? This displays command-line options.
    
  
- /continue This is used to tell the installer that it is continuing from being restarted.
    
  
- /unattended This indicates no user interaction.
    
  
The installer installs from the file that you specify in the command-line options described in the following list. In this list, < *file*  > signifies the file from which you want to install. If you do not specify the < *file*  > option, the installer downloads the file from the Internet and installs it. If the option does not apply to the current operating system, it is ignored.
- **/SQLNCli:< *file*  >** Install Microsoft SQL Server 2012 SP1 Native Client from < *file*  >.
    
  
- **/IDFX11:< *file*  >** Install Microsoft Identity Extensions from < *file*  >.
    
  
- **/Sync:< *file*  >** Install Microsoft Sync Framework Runtime SP1 v1.0 (x64) from < *file*  >.
    
  
- **/AppFabric:< *file*  >** Install Windows Server AppFabric from < *file*  > (AppFabric must be installed with the options /i CacheClient,CachingService,CacheAdmin /gac).
    
  
- **/KB3092423:< *file*  >** Install Cumulative Update Package 7 for Microsoft AppFabric 1.1 for Windows Server (KB3092423) from < *file*  >.
    
  
- **/MSIPCClient:< *file*  >** Install Microsoft Information Protection and Control Client from < *file*  >.
    
  
- **/WCFDataServices56:< *file*  >** Install Microsoft WCF Data Services 5.6 from < *file*  >.
    
  
- **/ODBC:< *file*  >** Install Microsoft ODBC Driver 11 for SQL Server from < *file*  >.
    
  
- **/DotNetFx:< *file*  >** Install Microsoft .NET Framework 4.6 from < *file*  >.
    
  
- **/MSVCRT11:< *file*  >** Install Visual C++ Redistributable Package for Visual Studio 2012 from < *file*  >.
    
  
- **/MSVCRT14:< *file*  >** Install Visual C++ Redistributable Package for Visual Studio 2015 from < *file*  >.
    
  

## Installation options

Certain prerequisites are installed by the prerequisite installer with specific options. Those prerequisites with specific installation options are listed below with the options that are used by the prerequisite installer.
- Windows AppFabric
    
    /i CacheClient,CachingService,CacheAdmin /gac
    
  
- Microsoft WCF Data Services
    
    /quiet
    
  
The prerequisite installer creates log files at %TEMP%\\prerequisiteinstaller.<date>.<time>.log. You can check these log files for specific details about all changes the installer makes to the target computer.
