---
title: "Hybrid search in SharePoint"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 10/4/2017
audience: ITPro
ms.topic: concetpual
ms.prod: sharepoint-server-itpro
localization_priority: Priority
ms.collection:
- Ent_O365_Hybrid
- IT_Sharepoint_Server
- IT_SharePoint_Hybrid_Top
- Strat_SP_gtc
- M365-collaboration
ms.custom: 
ms.assetid: c7f7540b-d631-4fdb-8dc6-fa90553a998e
description: "Hybrid search lets your users search for files and documents across SharePoint Server and Office 365 at the same time. Depending on how you set up hybrid search, you can have only on-premises users search for content stored in Office 365, only online users search for content stored in SharePoint Server, or both user groups search for content stored in the other environment."
---

# Hybrid search in SharePoint

[!INCLUDE[appliesto-2013-2016-2019-SPO-md](../includes/appliesto-2013-2016-2019-SPO-md.md)]

 Hybrid search lets your users search for files and documents across SharePoint Server and Office 365 at the same time. Depending on how you set up hybrid search, you can have only on-premises users search for content stored in Office 365, only online users search for content stored in SharePoint Server, or both user groups search for content stored in the other environment. 
  
There are two variants of hybrid search:
  
- Cloud hybrid search
    
- Hybrid federated search
    
## What is cloud hybrid search?

With the [cloud hybrid search solution](learn-about-cloud-hybrid-search-for-sharepoint.md) for SharePoint, you index all your crawled content, including on-premises content, in your search index in Office 365. When users enter a query in a search center, they get search results from the Office 365 search index, and thus get results both from on-premises and Office 365 content. 
  
![Figure showing on-premises and Office 365 content feeding the Office 365 search index, and search results coming from the Office 365 search index.](../media/190a4c47-d434-4d9b-bb14-81138f245ffd.png)
  
## What is hybrid federated search?

With the [hybrid federated search solution](learn-about-hybrid-federated-search-for-sharepoint.md) for SharePoint, you federate results from your search index in SharePoint Server 2013 and your search index in Office 365. When users enter a query in a search center, they get search results from the Office 365 search index and from the SharePoint Server 2013 search index, and thus get results both from on-premises and Office 365 content. 
  
![Figure showing searches from Office 365 getting results from the on-premises search index and the Office 365 index, and searches from the on-premises index getting results from the on-premises search index and the Office 365 index](../media/651bc6ac-5dbb-4266-83d6-be1bba093506.png)
  
## Cloud hybrid search or hybrid federated search - what's the difference for your users?

With cloud hybrid search, search results come from one search index. A search center in for example SharePoint Online in Office 365 displays and ranks results in one single result block. SharePoint Online calculates search relevance ranking and refiners for all your results, regardless of whether the results come from on-premises or Office 365 content.
  
![Illustration of how search results display with cloud hybrid search and with hybrid federated search.](../media/d88c8cf0-2820-4d5f-b54a-06f285226f66.png)
  
With hybrid federated search, search results come from two indexes. A search center in for example SharePoint Online in Office 365 displays and ranks results in two result blocks. SharePoint Online displays and ranks search results from Office 365 content, but uses the ranking from SharePoint Server 2013 for search results from on-premises content and displays these search results in the order that they arrive.
  
![Illustrations shows results in two result blocks, ranked separately.](../media/86bc8cc0-c1d8-4f40-bac9-96e8a6383063.png)
  
## Should you choose cloud hybrid search or hybrid federated search?

We recommend that you choose **cloud hybrid search** for these benefits: 
  
- Your users get unified search results, search relevance ranking, and refiners even if your organization has a hybrid deployment with content both on-premises and in Office 365. 
    
- Your users automatically get the newest SharePoint Online search experience without your organization having to update your existing SharePoint servers.
    
- Your users can use cloud capabilities such as Office Delve also for your on-premises content.
    
- You no longer have to worry about the size of your search index, because your search index is in Office 365. This means that the footprint of your SharePoint Server 2013 search farm is smaller, and your total cost of ownership for search is lower.
    
- You don't need to upgrade any of your existing installations of SharePoint to have enterprise search in the cloud because SharePoint Server 2013 supports crawling of existing SharePoint Server 2007, SharePoint Server 2010 and SharePoint Server 2013 content farms.
    
- You no longer have to migrate your search index to a newer version of SharePoint because this happens automatically for you in Office 365.
    
If you have some on-premises content that's highly sensitive and shouldn't be indexed outside your on-premises network, then we recommend using a combination of cloud hybrid search and hybrid federated search.
  
## See also

#### Concepts

[Plan hybrid federated search for SharePoint Server](plan-hybrid-federated-search.md)
#### Other Resources

[Learn about cloud hybrid search for SharePoint](learn-about-cloud-hybrid-search-for-sharepoint.md)
  
[Plan cloud hybrid search for SharePoint](plan-cloud-hybrid-search-for-sharepoint.md)
  
[Learn about hybrid federated search for SharePoint](learn-about-hybrid-federated-search-for-sharepoint.md)

