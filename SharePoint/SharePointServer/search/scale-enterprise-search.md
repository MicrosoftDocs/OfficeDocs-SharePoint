---
title: "Scale enterprise search in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 11/23/2016
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 3e2db0df-d07c-4adc-98a1-81e3fd42a272
description: "Learn which approach to use to scale your enterprise search architecture for performance and availability."
---

# Scale enterprise search in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
Sometimes it's necessary to scale your search topology, for example:
  
- Because your search environment has grown in amount of content or number of users, or both.
    
- Because you've identified a bottleneck while monitoring your search solution and this bottleneck might affect the search performance.
    
- Because your search environment has specific performance requirements that weren't addressed when you implemented one of the recommended search architectures described in Plan enterprise search architecture.
    
## How to scale your search topology

1. Redesign your search topology:
    
  - If you're scaling because your search environment has grown, follow the guidance in [Redesign enterprise search topology for more content and users in SharePoint 2016](redesign-topology-for-more-content-and-users.md).
    
  - If you're scaling because you have specific performance requirements or to remove a bottleneck, follow the guidance in [Redesign enterprise search topology for specific performance requirements in SharePoint 2016](redesign-for-specific-performance-requirements.md).
    
2. Implement the redesigned topology either on new servers, servers in your existing farm, or a combination. Follow the guidance in [Manage the search topology in SharePoint Server](manage-the-search-topology.md).
    

