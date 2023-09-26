---
title: "Hardware and topology requirements for SharePoint Server Subscription Edition"
ms.reviewer: 
ms.author: serdars
author: nimishasatapathy
manager: serdars
ms.date: 6/22/2021
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: interactive-tutorial
ms.service: sharepoint-server-itpro
ms.localizationpriority: high
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
- SP2019
ms.custom: 
ms.assetid: 4d88c402-24f2-449b-86a6-6e7afcfec0cd
description: "Find out the minimum hardware requirements that you need for installing and running SharePoint Server Subscription Edition."
---

# Hardware and topology requirements for SharePoint Server Subscription Edition

[!INCLUDE [appliesto-xxx-xxx-xxx-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)]

> [!IMPORTANT]
> If you contact Microsoft Customer Support Services about a production system that does not meet the minimum hardware specifications described in this document, support will be limited until the system is upgraded to the minimum requirements. 

## Hardware requirements for SharePoint servers

The values in the following table are minimum values for installations on servers that are running SharePoint Server in a multiple server farm installation.

Ensure the following before you proceed with deployment of SharePoint environment:

- For all installation scenarios:
  - You have sufficient hard disk space for the base installation.
  - You have sufficient hard disk space for diagnostics such as logging, debugging, creating memory dumps, and so on.
- For production environment
  - You have additional free disk space for day-to-day operations.
  - Maintain two times as much as free space as you have RAM

|Installation scenario|Deployment type and scale|Processor|RAM|Hard disk|
|---|---|---|---|---|
|Single server role that uses SQL Server|Development or evaluation installation with the minimum recommended services for development environments.|64-bit, 4 cores|16 GB|80 GB for system drive  <br/> 100 GB for second drive|
|Single server role that uses SQL Server|Pilot or user acceptance test installation running all available services.|64-bit, 4 cores|24 GB|80 GB for system drive  <br/> 100 GB for second drive and additional drives|
|SharePoint server in a multi-tier farm|Development or evaluation installation with a minimum number of services.|64-bit, 4 cores|12 GB|80 GB for system drive  <br/> 80 GB for second drive|
|SharePoint server in a multi-tier farm|Pilot or user acceptance test installation running all available services.|64-bit, 4 cores|16 GB|80 GB for system drive  <br/> 80 GB for second drive and additional drives|

> [!NOTE]
> Hard disk space and number of drives depends on the amount of content and the way you choose to distribute data for a SharePoint environment.

## Hardware requirements: Location of physical servers

Some enterprises have datacenters that are in close proximity to one another and are connected by high-bandwidth fiber optic links. In this environment, you can configure the two datacenters as a single farm. This distributed farm topology is called a stretched farm. Stretched farms for SharePoint Server Subscription Edition are supported.

For a stretched farm architecture to work as a supported high-availability solution, the following prerequisites must be met:

- There is a highly consistent intra-farm latency of <1 ms one way, 99.9% of the time over a period of 10 minutes. Intra-farm latency is commonly defined as the latency between the front-end web servers and the database servers.
- The bandwidth speed must be at least 1 gigabit per second.

To provide fault tolerance in a stretched farm, use the standard best practice guidance to configure redundant service applications and databases.

> [!NOTE]
> The intra-farm latency of <1 ms one way, 99.9% of the time over a period of ten minutes is also required for SharePoint environments with servers that are located in the same datacenter. The bandwidth speed should also be in this case at least 1 gigabit per second.

## Deployment requirements for farm topology
<a name="hwforwebserver"> </a>

SharePoint Server supports the same farm topologies as SharePoint Server 2019. For more information, see [Planning for a MinRole server deployment in SharePoint Server 2019](planning-for-a-minrole-server-deployment-in-sharepoint-server.md).
