---
title: "Administer search in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 3/9/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 820ace03-1fb7-41fd-a077-28b82ebddde3
description: "Learn how to manage the search topology and how to customize the search experience to make it easier for users to find the information they’re looking for."
---

# Administer search in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
Below are the main areas where you can customize and impact the search experience for your users and make sure that search is performing the way you want. SharePoint Server 2019 has both a classic and a modern search experience. Both search experiences use the same search index to find search results, and some settings can impact both experiences. [Learn about the differences between the search experiences in SharePoint Server](differences-search-2016-2019.md).

## Make sure the content can be found

The content must be crawled and added to the search index for your users to find what they're looking for when they search in SharePoint Server.

[Learn how to manage the index](manage-the-index.md)

[Learn how to manage crawling](manage-crawling.md)

## Make the results in the Search Center look great
The Search Center is a classic search experience, which you can customize. Presenting the search results the right way makes content easier to find. The Search Center comes with several pages, and you can use the different search Web Parts to help each user find what they're looking for. [Learn how to manage the Search Center](manage-the-search-center-in-sharepoint-server.md)

## Show relevant search results
All search results are not relevant to everyone all the time. There are a number of settings that you can use to show users the most relevant results. [Learn how to manage relevance](manage-relevance.md).

## Check logs and reports
See how you can check if the crawler has added content to the search index, and if your users are finding what they're looking for.

[Learn how to view search diagnostics](view-search-diagnostics.md)

[Learn how to enable query logging](enable-query-logging.md)

[Learn how to enable search alerts](enable-search-alerts.md)


## Manage the search topology
To keep search performant, you might need to scale out the search topology by managing the search components. [Learn how to manage the search topology](manage-the-search-topology.md).
   

