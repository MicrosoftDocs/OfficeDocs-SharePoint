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
description: "Find out the minimum hardware requirements that you need for installing and running SharePoint Server Subscription Edition."
---

# Hardware and Topology Requirements for SharePoint Server Subscription Edition

[!INCLUDE [appliesto-xxx-xxx-xxx-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)]

  
> [!IMPORTANT]
> If you contact Microsoft Customer Support Services about a production system that does not meet the minimum hardware specifications described in this document, support will be limited until the system is upgraded to the minimum requirements. 

## Hardware requirements: Location of physical servers

Some enterprises have datacenters that are in close proximity to one another and connected by high-bandwidth fiber optic links. In this environment, you can configure the two datacenters as a single farm. This distributed farm topology is called a stretched farm. Stretched farms for SharePoint Server Subscription Edition are supported.

For a stretched farm architecture to work as a supported high-availability solution, the following prerequisites must be met:

- There is a highly consistent intra-farm latency of <1 ms one way, 99.9% of the time over a period of ten minutes. (Intra-farm latency is commonly defined as the latency between the front-end web servers and the database servers.
- The bandwidth speed must be at least 1 gigabit per second.

To provide fault tolerance in a stretched farm, use the standard best practice guidance to configure redundant service applications and databases.

> [!NOTE]
> The intra-farm latency of <1 ms one way, 99.9% of the time over a period of ten minutes is also required for SharePoint environments with servers that are located in the same datacenter. The bandwidth speed should also be in this case at least 1 gigabit per second.
  
    
## Hardware requirements: SharePoint Servers and MinRole installations

The values in the following table are minimum values for installations on servers that are running SharePoint Server in a multiple server farm installation.

For all installation scenarios, you must have sufficient hard disk space for the base installation and sufficient space for diagnostics such as logging, debugging, creating memory dumps, and so on. For production use, you must also have additional free disk space for day-to-day operations. In addition, maintain two times as much free space as you have RAM for production environments.

|**Installation scenario**|**Deployment type and scale**|**Processor**|**RAM**|**Hard disk**|
|:-----|:-----|:-----|:-----|:-----|
|Single server role that uses SQL Server  <br/> |Development or evaluation installation with the minimum recommended services for development environments.  <br/> |64-bit, 4 cores <br/> |16 GB  <br/> |80 GB for system drive  <br/> 100 GB for second drive  <br/> |
|Single server role that uses SQL Server  <br/> |Pilot or user acceptance test installation running all available services.  <br/> |64-bit, 4 cores <br/> |24 GB   <br/> |80 GB for system drive  <br/> 100 GB for second drive and additional drives  <br/> |
|SharePoint server in amulti-tier farm  <br/> |Development or evaluation installation with a minimum number of services.  <br/> |64-bit, 4 cores <br/> |12 GB  <br/> |80 GB for system drive  <br/> 80 GB for second drive  <br/> |
|SharePoint server in a multi-tier farm  <br/> |Pilot or user acceptance test installation running all available services.  <br/> |64-bit, 4 cores  <br/> |16 GB    <br/> |80 GB for system drive  <br/> 80 GB for second drive and additional drives  <br/> 

> [!NOTE]
> Hard disk space and number of drives depends on the amount of content and the way you choose to distribute data for a SharePoint environment.

## Deployment requirements: farm topology
<a name="hwforwebserver"> </a>

SharePoint Server supports the same farm topologies as SharePoint Server 2019. For more information, see [Planning for a MinRole server deployment in SharePoint Server 2019](planning-for-a-minrole-server-deployment-in-sharepoint-server.md).


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





  
