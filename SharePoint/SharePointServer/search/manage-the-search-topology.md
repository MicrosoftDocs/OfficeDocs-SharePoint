---
title: "Manage the search topology in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 3/7/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: a2420e0a-bc3d-4a07-b7b9-f44c7a74ade1
description: "Learn how to manage search components to scale out the search topology in SharePoint Server."
---

# Manage the search topology in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
The following articles provide information about how you manage search components in SharePoint Server.
  
Before you change the search topology, you must define, install and configure the required application servers and database servers that you want to use for search.
  
For information about planning an initial enterprise search architecture, see [Plan enterprise search architecture in SharePoint Server 2016](plan-enterprise-search-architecture.md). To learn which approach to use to scale enterprise search architecture, see [Scale enterprise search in SharePoint Server](scale-enterprise-search.md). For information about planning an initial search architecture for cloud hybrid search, see [Plan your search architecture in SharePoint Server for cloud hybrid search](../hybrid/plan-cloud-hybrid-search-for-sharepoint.md#BKMK_Plan_search_architecture).
  
For example farm architectures and search topologies for internet sites, see the technical diagrams [Internet sites search architectures for SharePoint Server 2013](https://www.microsoft.com/en-us/download/details.aspx?id=54296) and [Search architectures for SharePoint Server 2013](https://docs.com/officeitpro/3386/search-architectures-for-sharepoint-server-2016). You can also find these diagrams in [Technical diagrams for SharePoint Server](../technical-reference/technical-diagrams.md) . [Scale search for Internet sites in SharePoint Server](scale-search-for-internet-sites.md) gives guidance on scaling out search topology for Internet sites. 
  
## Articles about managing the search topology

The following articles about managing the search topology in SharePoint Server are available to view online. Writers update articles on a continuing basis as new information becomes available and as users provide feedback.
  
|                                                   **Content**                                                    |                                                                                                                **Description**                                                                                                                |
| :--------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Change the default search topology in SharePoint Server](change-the-default-search-topology.md)                 | Learn how to change from the default search topology with an empty search index to a new search topology using Windows PowerShell.                                                                                                            |
| [Manage search components in SharePoint Server](manage-search-components.md)                                     | Learn how to use Microsoft PowerShell to manage search components in an existing search topology that has content in the search index. Use these procedures to scale out or scale down the search topology of the Search service application. |
| [Manage the index component in SharePoint Server](manage-the-index-component.md)                                 | Learn how and when to use Microsoft PowerShell to scale out the search index by adding an index component to create an additional index replica or index partition.                                                                           |
| [Manage a paused Search service application in SharePoint Server](manage-a-paused-search-service-application.md) | Learn why the Search service application is paused and what you can do to resume it.                                                                                                                                                          |
   

