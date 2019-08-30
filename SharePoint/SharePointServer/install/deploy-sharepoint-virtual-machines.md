---
title: "Deploying SharePoint Server on virtual machines"
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
description: "Learn about deploying and managing virtual machines for SharePoint Server."
---

# Plan for virtualization of SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 

SharePoint Server may be deployed as a virtual server on Hyper-V or other platforms supported as part of the [Server Virtualization Validation Program](https://www.windowsservercatalog.com/svvp.aspx). Virtual machines provide increased flexibility for IT administrators.

## Limitations
<a name="Section1"> </a>

SharePoint Server imposes certain restrictions when operating as a virtual machine. These restrictions stem from the use of the local configuration cache and search index when used in a SharePoint Server farm deployment. As certain hypervisor operations cannot synchronize actions, the configuration cache and/or search index may become out of sync with either other SharePoint Servers in the farm or SharePoint databases residing on the SQL Server.

SharePoint Server does not support the following type of operations while SharePoint Server is online.

 * Virtual machine online backups - If full virtual machine backups are required, shut down the SharePoint and SQL Servers in the farm prior to taking virtual machine backups. If a restore is required, restore all servers in the farm.
 * Virtual machine snapshots - If a snapshot of SharePoint is required, shut down all SharePoint Servers and SQL Servers in the farm prior to taking a virtual machine snapshot. If a restore is required, restore all servers in the farm. Delete the snapshot as soon as possible as it may incur a performance penalty.
 * Virtual machine replication - Note an exception to this is [Azure Site Recovery](https://docs.microsoft.com/en-us/azure/site-recovery/site-recovery-sharepoint).
 * SAN (Storage Area Network) replication of SharePoint Server virtual disks

SharePoint Server also does not support dynamic/ballooning memory and we recommend against using differencing disks for long periods of time.
     
## Virtual Machine Templates
<a name="Section2"> </a>

SharePoint Server supports virtual machine templates. Templates can be created by installing SharePoint Server prerequisites, SharePoint Server, and any applicable public updates. As long as the Configuration Wizard has not been run, the virtual machine can be saved as a template following your virtualization software guidance.

Do not create a template from a virtual machine running SharePoint Server that is already joined to a farm.

## See also
<a name="Section3"> </a>

[Hardware and software requirements for SharePoint Server 2019](hardware-and-software-requirements-2019.md)

[Hardware and software requirements for SharePoint Server 2016](hardware-and-software-requirements.md)

[Hardware and software requirements for SharePoint 2013](hardware-and-software-requirements-0.md)
