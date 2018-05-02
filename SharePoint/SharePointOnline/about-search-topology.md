---
title: "About search topology"
ms.author: tlarsen
author: tklarsen
manager: arnek
ms.date: 12/30/2016
ms.audience: ITPro
ms.topic: reference
f1_keywords:
- AboutSSATopologyAndSystemStatus
- WSSCentralAdmin_AboutSSATopologyAndSystemStatus
ms.prod: office-online-server
localization_priority: Normal
search.appverid:
- SPS150
- OSU150
- OSI150
ms.assetid: 65de12f3-4e77-4911-98c5-622cf7e13bf3
description: "View the current distribution and status of the search topology, that is to say all search components of a Search service application, across servers in your farm."
---

# About search topology

The **Search Application Topology** section on the Search Administration page shows the current distribution and status of search components across servers in your farm. 
  
To improve search performance and availability, you can scale out the search topology and install search components on multiple servers. For more information about scaling the search topology and search performance and capacity planning, see the [Search planning](https://go.microsoft.com/fwlink/?linkid=261562) section on TechNet. 
  
The following status indicators provide a visual indication of the status of the search components in your farm:
  
- A green check mark - indicates that the search component is running correctly.
    
- A yellow triangle - indicates that the search component cannot perform all operations correctly.
    
- A red cross - indicates that the search component is not running, or that there are errors that prevent the component from running correctly.
    
Use the Windows PowerShell cmdlet Get-SPEnterpriseSearchStatus to retrieve more detailed diagnostic information about the status of the search components in the active topology of a Search service application. 
  
If you have created the Search service application with the Farm Configuration Wizard, all search components are installed on the server that hosts the Central Administration. This is referred to as the default search topology. If you have created the Search service application in a different way, you have to create the search topology from scratch.
  
You can change the search topology by using Windows PowerShell. For more information, see [Manage the search topology](https://go.microsoft.com/fwlink/?linkid=261610) on TechNet. 
  
[The Search Application Topology section on the Search Administration page shows the current distribution and status of search components across servers in your farm.To improve search performance and availability, you can scale out the search topology and install search components on multiple servers. For more information about scaling the search topology and search performance and capacity planning, see the Search planninghttps://go.microsoft.com/fwlink/?linkid=261562 section on TechNet.The following status indicators provide a visual indication of the status of the search components in your farm:A green check mark - indicates that the search component is running correctly.A yellow triangle - indicates that the search component cannot perform all operations correctly.A red cross - indicates that the search component is not running, or that there are errors that prevent the component from running correctly.Use the Windows PowerShell cmdlet Get-SPEnterpriseSearchStatus to retrieve more detailed diagnostic information about the status of the search components in the active topology of a Search service application. If you have created the Search service application with the Farm Configuration Wizard, all search components are installed on the server that hosts the Central Administration. This is referred to as the default search topology. If you have created the Search service application in a different way, you have to create the search topology from scratch.You can change the search topology by using Windows PowerShell. For more information, see Manage the search topologyhttps://go.microsoft.com/fwlink/?linkid=261610 on TechNet.Top of Page](about-search-topology.md#__top)
  

