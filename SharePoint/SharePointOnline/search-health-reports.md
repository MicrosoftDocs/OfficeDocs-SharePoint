---
title: "Search health reports"
ms.author: tlarsen
author: tklarsen
manager: arnek
ms.date: 12/30/2016
ms.audience: End User
ms.topic: article
f1_keywords:
- CrawlDiagnosticsHealth
- WSSCentralAdmin_CrawlDiagnosticsHealth
ms.prod: office-online-server
localization_priority: Normal
search.appverid:
- WSU150
- SPS150
- SPS150
- SPS150
- OSU150
- OSI150
ms.assetid: 0b67cef2-d9cd-43f9-80a7-6aaa04c97537
description: "Analyze the health of the SharePoint 2013 search system by using crawl health reports and query health reports."
---

# Search health reports

The search system in SharePoint Server 2013 provides two main kinds of health reports, query health reports and crawl health reports.
  
## In this article
<a name="__top"> </a>

> [Query health reports](search-health-reports.md#__toc329946337)
    
> [Crawl health reports](search-health-reports.md#__toc329946338)
    
## Query health reports
<a name="__toc329946337"> </a>

The following reports about query performance are available:
  
|**Query Health Report**|**Description**|
|:-----|:-----|
|Trend (Query Latency Trend)  <br/> | For a specified time interval, shows the query latency (in milliseconds) by percentile. For example, five percent of all queries had lower latency than the latency indicated by the fifth percentile line in the graph.  <br/>  The graph includes an overlay of query rate during the specified time interval, where query rate is the number of queries per minute for which the query object model (OM) returned results.  <br/>  The graph also includes an overlay of the crawl rate and the partial update rate for analytics.  <br/>  You can filter this report by:  <br/>  Start date/time  <br/>  End date/time  <br/>  Client type  <br/>  Result page (search results page), which only shows if verbose logging is enabled.  <br/>  By default, the graph displays data for all result pages in the Search service application.  <br/> |
|Overall (Overall Query Latency)  <br/> | For a specified time interval, shows the query rate (number of queries per minute) with an overlay of query latency in milliseconds.  <br/>  Shows the query latency in each of the following areas:  <br/>  Object model. This is the time it takes to communicate between the web server and the back-end.  <br/>  Backend. This is the time it takes to transform the query, perform index look up, process results (such as removing duplicates), and return results to the object model.  <br/>  You can filter this report by:  <br/>  Start date/time  <br/>  End date/time  <br/>  Client Type  <br/>  Result page (search results page), which only shows if verbose logging is enabled.  <br/>  By default, the graph shows data for all result pages in the Search service application.  <br/> |
|Main Flow (Default SharePoint Flow Query Latency)  <br/> | For a specified time interval, shows the query latency (in milliseconds) in the main flow for query and result processing. This indicates how fast the system processes a query and returns results to the web server. The graph shows the query latency for:  <br/>  Query rule condition matching  <br/>  Query transformation  <br/>  Query routing  <br/>  Result mixing  <br/>  Layout selection  <br/>  Query logging  <br/>  Other  <br/>  The graph includes an overlay of query rate during the specified time interval.  <br/>  You can filter this report by:  <br/>  Start date/time  <br/>  End date/time  <br/>  Client Type  <br/> |
|Federation (Federation Query Latency)  <br/> | For a specified time interval, shows the query latency in milliseconds for all result source types.  <br/>  By default, the graph shows data for all result pages in the Search service application.  <br/>  You can filter this report by:  <br/>  Start date/time  <br/>  End date/time  <br/>  Client type  <br/>  Result page (search results page), which only shows if verbose logging is enabled.  <br/>  Source type (result source type):  <br/>  Best Bet Provider  <br/>  Exchange Search Provider  <br/>  Local People Provider  <br/>  Local SharePoint Provider  <br/>  OpenSearch Provider  <br/>  Personal Favorites Provider  <br/>  Remote People Provider  <br/> |
|SharePoint Search Provider (Local SharePoint Search Flow Query Latency)  <br/> | For a specified time interval, shows the query latency (in milliseconds) for all queries that are processed by the local SharePoint search provider. The graph shows the query latency for:  <br/>  Keyword parsing  <br/>  Linguistics  <br/>  Recommendations Security Trimming  <br/>  Security token construction  <br/>  Index lookup  <br/>  Result type processing  <br/>  Custom security trimming  <br/>  Summary generation  <br/>  Other  <br/>  The graph includes an overlay of query rate during the specified time interval.  <br/>  You can filter this report by:  <br/>  Start date/time  <br/>  End date/time  <br/>  Client type  <br/> |
|People Search Provider (People Search Flow Query Latency)  <br/> | For a specified time interval, shows the query latency (in milliseconds) for all queries that are processed by the local people search provider. The graph shows the query latency in each of the following areas:  <br/>  Keyword parsing  <br/>  Linguistics  <br/>  People pre-processing  <br/>  Security token construction  <br/>  Index lookup  <br/>  Result type processing  <br/>  Custom security trimming  <br/>  Summary generation  <br/>  Other  <br/>  The graph includes an overlay of query rate during the specified time interval.  <br/>  You can filter this report by:  <br/>  Start date/time  <br/>  End date/time  <br/>  Client type  <br/> |
|Index Engine (Index Engine Query Latency  <br/> | For a specified time interval, shows the query latency in milliseconds for each index server that you filter on. By default, the graph shows data for all result pages in the Search service application. You can filter this report by:  <br/>  Start date/time  <br/>  End date/time  <br/>  Index server (a computer that hosts at least one index partition)  <br/>  Result page (search results page), which only shows if verbose logging is enabled.  <br/>  The graph includes an overlay of the index lookup time for the specified time interval in the past. Index lookup time is the average amount of time during a given minute that it took the index engine to return results. The index lookup time applies only to queries for which the index engine returned results.  <br/> |
   
[The search system in SharePoint Server 2013 provides two main kinds of health reports, query health reports and crawl health reports.](search-health-reports.md#__top)
  
## Crawl health reports
<a name="__toc329946338"> </a>

The following reports about crawl health are available:
  
|**Crawl Report**|**Description**|
|:-----|:-----|
|Crawl Rate  <br/> | For a specified time interval, shows a graph and a summary of the following:  <br/>  Number of content items crawled per minute. This includes:  <br/>  Total content items  <br/>  Modified items. These are content items that were changed and re-crawled.  <br/>  Not modified items. These are content items that were not changed and were not crawled.  <br/>  Security items. These are content items for which the security attributes were changed.  <br/>  Deleted items. These are content items that were deleted from the content source and which must also be deleted from the index.  <br/>  Average number of other crawl actions that were performed per minute. This includes:  <br/>  Retries (crawl retries)  <br/>  Errors (crawl errors)  <br/>  You can filter this report by:  <br/>  Start date/time  <br/>  End date/time  <br/>  Content sources (for example, Local SharePoint sites)  <br/>  Machine  <br/> |
|Crawl Latency  <br/> | For a specified time, shows a graph of the number of items that form the crawl load, for each of the following:  <br/>  In Crawler Queue  <br/>  Waiting to submit to content processing  <br/>  Submitted to content processing  <br/>  Waiting to Commit (SQL)  <br/>  You can filter this report by machine only.  <br/>  For a specified time interval, also shows a graph and a summary of the crawl latency; the amount of time in milliseconds that each content item is in each of the following subsystems in the feeding pipeline:  <br/>  Crawler  <br/>  Protocol handler (PH)  <br/>  Repository  <br/>  SQL Time  <br/>  You can filter this report by:  <br/>  Start date/time  <br/>  End date/time  <br/>  Content source (for example, Local SharePoint sites)  <br/>  Machine  <br/> |
|Crawl Queue  <br/> | For a specified time interval, shows the number of items in the following two crawl queues:  <br/>  Links to process. This is the number of uncrawled URLs that are queued to be crawled.  <br/>  Transactions queued. This is the number of crawled URLs that arequeued to be processed in the crawl pipeline.  <br/>  You can filter this report by start date/time and end date/time.  <br/> |
|Crawl Freshness  <br/> | For a specified time interval, shows the freshness of the content that was being indexed by the search system. The last modified time stamp of each document is compared with the time specified in the graph. You can view the freshness of the content as follows:  <br/>  Less than 1 month ago  <br/>  Less than 1 week ago  <br/>  Less than 1 day ago  <br/>  Less than 4 hours ago  <br/> |
|Content Processing Activity  <br/> | For a specified time interval, shows the amount of time that was spent in content processing for:  <br/>  Content sources  <br/>  Machines  <br/>  Content processing components  <br/>  Content processing activity  <br/>  The graph shows the amount of time that was spent in various content processing activities, such as:  <br/>  Linguistics processing  <br/>  Document parsing  <br/>  Document summary generation  <br/>  Indexing  <br/>  You can filter this report by:  <br/>  Start date/time  <br/>  End date/time  <br/>  Content source  <br/>  Machine  <br/>  Content processing component name  <br/>  Processing activity  <br/> |
|CPU And Memory Load  <br/> | For a specified time interval, shows the percentage of CPU used, the memory use in megabytes and the system overview for these processes:  <br/>  MSSDmn  <br/>  MSSearch  <br/>  NodeRunner  <br/>  Timer  <br/>  You can filter this report by:  <br/>  Machine  <br/>  Start date/time  <br/>  End date/time  <br/> |
|Continuous Crawl  <br/> | For a specified time interval, shows the time (in milliseconds) that the processes took with an overlay of discovery time (in minutes) for:  <br/>  Time In Links Table  <br/>  Time In Queue Table  <br/>  Crawler Time  <br/>  PH (Protocol Handler) Time  <br/>  Repository Time  <br/>  Content Pipeline Time  <br/>  SQL Time  <br/>  You can filter this report by:  <br/>  Content sources  <br/>  Start date/time  <br/>  End date/time  <br/> |
   
For more information, see [View search diagnostics](https://go.microsoft.com/fwlink/?linkid=261564) on TechNet. 
  
[The search system in SharePoint Server 2013 provides two main kinds of health reports, query health reports and crawl health reports.](search-health-reports.md#__top)
  

