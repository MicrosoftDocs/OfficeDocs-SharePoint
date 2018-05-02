---
title: "Understanding result sources"
ms.author: tlarsen
author: tklarsen
manager: arnek
ms.date: 12/30/2016
ms.audience: End User
ms.topic: reference
f1_keywords:
- AboutResultSources
- WSSEndUser_AboutResultSources
ms.prod: office-online-server
localization_priority: Normal
search.appverid:
- WSU150
- SPS150
- SPS150
- SPO160
- SPS150
- OSU150
- SPB160
- GSS150
- GSA150
- OSI150
- BSA160
- GSP150
ms.assetid: 3fb2c8c4-ecbd-4210-abf7-1f0df59a370b
description: "Use result sources in SharePoint 2013 to limit searches to a certain set of content."
---

# Understanding result sources

In SharePoint Server 2010, federated locations and scopes provided ways to limit searches to a certain set of content or subset of search results. In SharePoint Server 2013, result sources provide this functionality.
  
You create and use a result source to specify a location to get search results from, and to specify a protocol for getting those results. In SharePoint Server 2010, you specified a location and a protocol by creating a federated location, and you could specify the protocol as local SharePoint index, FAST Search Server 2010 for SharePoint index, or OpenSearch. In contrast, for protocol (which is called the  *Source Type*  ) in SharePoint Server 2013, you can specify local SharePoint index, remote SharePoint index, OpenSearch, or Microsoft Exchange Server index. If you specify remote SharePoint index as the Source Type, you do not have to supply any custom code to handle authentication as you did in SharePoint Server 2010. 
  
In a result source, you can also restrict queries to a subset of content by using a [query transform](understanding-query-transforms.md). For example, the pre-defined "Local Video Results" result source uses a query transform to return only video results from the local SharePoint index. In SharePoint Server 2010, you configured this kind of query restriction by using search scopes.
  
On a search results page, you can expose results for queries on a particular result source in several ways, such as in a result block or in a dedicated Web Part.
  
In SharePoint Server 2010, only a Search service application administrator was able to manage and configure federated locations. In contrast, in SharePoint Server 2013, site collection administrators, site owners, and site designers can also create and configure result sources to meet their specific requirements, rather than having to rely on Search service application administrators.
  
For more information, see:
  
- SharePoint Online: [Manage result sources](manage-result-sources.md) (Office.com) 
    
- SharePoint Server 2013: [Configure result sources for search in SharePoint Server 2013](https://technet.microsoft.com/library/jj683115%28v=office.15%29) (TechNet) 
    
[In SharePoint Server 2010, federated locations and scopes provided ways to limit searches to a certain set of content or subset of search results. In SharePoint Server 2013, result sources provide this functionality.You create and use a result source to specify a location to get search results from, and to specify a protocol for getting those results. In SharePoint Server 2010, you specified a location and a protocol by creating a federated location, and you could specify the protocol as local SharePoint index, FAST Search Server 2010 for SharePoint index, or OpenSearch. In contrast, for protocol (which is called the Source Type) in SharePoint Server 2013, you can specify local SharePoint index, remote SharePoint index, OpenSearch, or Microsoft Exchange Server index. If you specify remote SharePoint index as the Source Type, you do not have to supply any custom code to handle authentication as you did in SharePoint Server 2010.In a result source, you can also restrict queries to a subset of content by using a query transform. For example, the pre-defined "Local Video Results" result source uses a query transform to return only video results from the local SharePoint index. In SharePoint Server 2010, you configured this kind of query restriction by using search scopes.On a search results page, you can expose results for queries on a particular result source in several ways, such as in a result block or in a dedicated Web Part.In SharePoint Server 2010, only a Search service application administrator was able to manage and configure federated locations. In contrast, in SharePoint Server 2013, site collection administrators, site owners, and site designers can also create and configure result sources to meet their specific requirements, rather than having to rely on Search service application administrators.For more information, see:SharePoint Online: Manage result sources (Office.com)SharePoint Server 2013: Configure result sources for search in SharePoint Server 2013https://technet.microsoft.com/library/jj683115(v=office.15) (TechNet) Top of Page](understanding-result-sources.md#__top)
  

