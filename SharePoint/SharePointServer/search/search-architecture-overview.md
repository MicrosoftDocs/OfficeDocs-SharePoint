---
title: "Overview of search architecture in SharePoint Server"
ms.author: tlarsen
author: tlarsen
manager: pamgreen
ms.date: 3/2/2018
ms.audience: ITPro
ms.topic: article
ms.prod: office-online-server
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: c12cdce4-1a73-4602-96ff-ac50da27f614
description: "Summary: Learn about SharePoint Server search architecture, SharePoint Server search components, SharePoint Server search databases, and the SharePoint Server search topology."
---

# Overview of search architecture in SharePoint Server

 **Summary:** Learn about SharePoint Server search architecture, SharePoint Server search components, SharePoint Server search databases, and the SharePoint Server search topology. 
  
The search architecture contains search components and databases. How you structure the search architecture depends on where you intend to use search: for the enterprise or for Internet sites. When building the search architecture, you should take into account considerations such as high availability and fault tolerance, the volume of your content and the estimated amount of page views and queries per second.
  
For information about search topologies for different use cases: see the technical diagrams [Enterprise search architectures for SharePoint Server 2016](https://www.microsoft.com/en-us/download/54292) and [Internet sites search architectures for SharePoint Server 2016](https://www.microsoft.com/en-us/download/details.aspx?id=54296).
  
In this article:
  
- [Overview of search components and search databases](search-architecture-overview.md#OverviewSearchComponents)
    
- [About the crawl component](search-architecture-overview.md#CrawlComponent)
    
- [About the content processing component](search-architecture-overview.md#ContentProcComponent)
    
- [About the analytics processing component](search-architecture-overview.md#AnalyticsProcComp)
    
- [About the index component](search-architecture-overview.md#IndexComp)
    
- [About the query processing component](search-architecture-overview.md#QueryProcComp)
    
- [About the search administration component](search-architecture-overview.md#SearchAdminComp)
    
- [About the crawl database](search-architecture-overview.md#CrawlDB)
    
- [About the link database](search-architecture-overview.md#LinkDB)
    
- [About the analytics reporting database](search-architecture-overview.md#AnalyticsDB)
    
- [About the search administration database](search-architecture-overview.md#AdminDB)
    
## Overview of search components and search databases
<a name="OverviewSearchComponents"> </a>

The following tables show an overview of all the available search components and search databases. For more information about how search components and databases interact, see the [Search architectures for SharePoint Server 2016](https://www.microsoft.com/en-us/download/details.aspx?id=54295) technical diagram. 
  
**Search components**

|**Search component name**|**Description**|
|:-----|:-----|
|Crawl component  <br/> |Crawls content sources to collect crawled properties and metadata from crawled items and sends this information to the content processing component.  <br/> |
|Content processing component  <br/> |Transforms the crawled items and sends them to the index component. This component also maps crawled properties to managed properties.  <br/> |
|Analytics processing component  <br/> |Carries out search analytics and usage analytics.  <br/> |
|Index component  <br/> |Receives the processed items from the content processing component and writes them to the search index. This component also handles incoming queries, retrieves information from the search index and sends back the result set to the query processing component.  <br/> |
|Query processing component  <br/> |Analyzes incoming queries. This helps optimize precision, recall and relevance. The queries are sent to the index component, which returns a set of search results for the query.  <br/> |
|Search administration component  <br/> |Runs the system processes for search, and adds and initializes new instances of search components.  <br/> |
   
**Search databases**

|**Search database name**|**Description**|
|:-----|:-----|
|Crawl database  <br/> |Stores tracking information and historical information about crawled items such as documents and URLs. It also stores information such as the last crawl time, the last crawl ID and the type of update (add, update, delete) during the last crawl.  <br/> |
|Link database  <br/> |Stores unprocessed information that is extracted by the content processing component and information about search clicks. The analytics processing component analyzes this information.  <br/> |
|Analytics reporting database  <br/> |Stores the results of usage analysis.  <br/> |
|Search administration database  <br/> |Stores search configuration data.  <br/> |
   
## About the crawl component
<a name="CrawlComponent"> </a>

The crawl component crawls the content sources. You can crawl lots of content sources, for example file shares, SharePoint Server content, line of business applications and many more. To retrieve information, the crawl component connects to the content sources by invoking the appropriate indexing connector or protocol handler. After retrieving the content, the crawl component passes crawled items to the content processing component.
  
For more information about crawling content sources, see [Plan crawling and federation in SharePoint Server](plan-crawling-and-federation.md).
  
## About the content processing component
<a name="ContentProcComponent"> </a>

The content processing component processes crawled items and sends these items to the index component. The content processing component performs operations such as document parsing and property mapping. It also performs linguistics processing such as language detection and entity extraction. The component transforms crawled items into artifacts that are included in the search index. The content processing component also writes information about links and URLs to the link database.
  
For more information about content processing, see [Plan crawling and federation in SharePoint Server](plan-crawling-and-federation.md).
  
## About the analytics processing component
<a name="AnalyticsProcComp"> </a>

The analytics processing component performs two types of analyses: search analytics and usage analytics. This component uses information from these analyses to improve search relevance, create search reports, and generate recommendations and deep links.
  
- Search analytics is about extracting information, such as links, the number of times an item is clicked, anchor text, data related to people, and metadata, from the link database. This information is important to relevance.
    
- Usage analytics is about analyzing usage log information received from the front-end via the event store. Usage analytics generates usage and statistics reports.
    
The results from the analyses are added to the items in the search index. In addition, results from usage analytics are stored in the analytics reporting database.
  
For more information, see [Overview of analytics processing in SharePoint Server](overview-of-analytics-processing.md).
  
## About the index component
<a name="IndexComp"> </a>

You can divide the search index into discrete portions, called index partitions. The search index is the aggregation of all index partitions. Each index partition holds one or more index replicas that contain the same information. To achieve fault tolerance and redundancy, create additional index replicas for each index partition and distribute the index replicas over multiple servers.
  
The index component is the logical representation of an index replica. In the search topology, you have to provision one index component for each index replica.
  
The index component:
  
- Receives processed items from the content processing component and writes those items to an index file. Index files are stored on a disk in the server that hosts the index component.
    
- Receives queries from the query processing component and returns result sets.
    
For more information about the search schema and the search index, see [Overview of the search schema in SharePoint Server](search-schema-overview.md).
  
## About the query processing component
<a name="QueryProcComp"> </a>

The query component analyzes and processes queries and results. It performs linguistics processing such as word breaking and stemming. When the query processing component receives a query from the search front-end, it analyzes and processes the query to optimize precision, recall and relevance. The processed query is submitted to the index component. The index component returns a result set based on the processed query to the query processing component, which in turn processes that result set, before returning it to the search front-end.
  
For more information, see [Plan to transform queries and order results in SharePoint Server](plan-to-transform-queries-and-order-results.md).
  
## About the search administration component
<a name="SearchAdminComp"> </a>

The search administration component runs the system processes for search. This component performs provisioning, which is to add and initialize instances of the other search components.
  
## About the crawl database
<a name="CrawlDB"> </a>

The crawl database stores tracking information and historical information about crawled items. For example, it stores information about the last crawl time, the last crawl ID and the type of update during the last crawl.
  
## About the link database
<a name="LinkDB"> </a>

The link database stores information extracted by the content processing component. In addition, it stores information about search clicks; the number of times people click on a search result from the search result page. This information is stored unprocessed, to be analyzed by the analytics processing component.
  
## About the analytics reporting database
<a name="AnalyticsDB"> </a>

The analytics reporting database stores the results of usage analytics. In addition, it stores statistics information from the analyses. SharePoint Server uses this information to create Excel reports that show different statistics.
  
## About the search administration database
<a name="AdminDB"> </a>

The search administration database stores search configuration data, such as the topology, crawl rules, query rules, and the mappings between crawled and managed properties. It also stores the access control list (ACL) for the crawl component. There can be only one search administration database per search service application.
  
## See also
<a name="AdminDB"> </a>

#### Concepts

[Manage the search topology in SharePoint Server](manage-the-search-topology.md)

