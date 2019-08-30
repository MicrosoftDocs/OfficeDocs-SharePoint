---
title: "View search diagnostics in SharePoint Server"
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
ms.assetid: 5cf2a498-d879-4673-b4d4-2eaa36695ff9
description: "Learn about usage reports, query health reports, crawl health reports and the crawl log to analyze the health of the search system."
---

# View search diagnostics in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
You can access and analyze several query and crawl health reports, logs and usage reports from the Search service application in the SharePoint ServerCentral Administration to monitor the health of the search system.
  
    
## Before you begin
<a name="begin"> </a>

Before you begin this operation, review the following information:
  
- The health reports and logs only contain information after a full crawl has completed. 
    
- To view the health reports and the crawl log, you have to be an administrator of the Search service application. Alternatively, an administrator who is a member of the Farm Administrators group can grant user accounts Read permissions on the Search service application. A user account that has Read permissions can only view the Search service application status page, the health reports and the crawl log.
    
## Query health reports
<a name="proc1"> </a>

SharePoint Server provides the following reports about query performance:
  
- Trend (Query Latency Trend)
    
    For a specified time interval, shows the query latency (in milliseconds) by percentile. For example, five percent of all queries had lower latency than the latency indicated by the fifth percentile line in the graph.
    
    The graph includes an overlay of query rate during the specified time interval, where query rate is the number of queries per minute for which the query object model (OM) returned results.
    
    The graph also includes an overlay of the crawl rate and the partial update rate for analytics. 
    
    You can filter this report by:
    
  - Start date/time
    
  - End date/time
    
  - Client type
    
  - Result page (search results page), which only shows if verbose logging is enabled.
    
  By default, the graph displays data for all result pages in the Search service application.
    
- Overall (Overall Query Latency)
    
    For a specified time interval, shows the query rate (number of queries per minute) with an overlay of query latency in milliseconds. 
    
    Shows the query latency in each of the following areas:
    
  - Object model. This is the time it takes to communicate between the web server and the back-end. 
    
  - Backend. This is the time it takes to transform the query, perform index look up, process results (such as removing duplicates), and return results to the object model.
    
  You can filter this report by:
    
  - Start date/time
    
  - End date/time
    
  - Client Type
    
  - Result page (search results page), which only shows if verbose logging is enabled.
    
    By default, the graph shows data for all result pages in the Search service application.
    
- Main Flow (Default SharePoint Flow Query Latency)
    
    For a specified time interval, shows the query latency (in milliseconds) in the main flow for query and result processing. This indicates how fast the system processes a query and returns results to the web server. The graph shows the query latency for:
    
  - Query rule condition matching
    
  - Query transformation
    
  - Query routing
    
  - Result mixing
    
  - Layout selection
    
  - Query logging
    
  - Other
    
  The graph includes an overlay of query rate during the specified time interval.
    
  You can filter this report by:
    
  - Start date/time
    
  - End date/time
    
  - Client Type
    
- Federation (Federation Query Latency)
    
    For a specified time interval, shows the query latency in milliseconds for all result source types.
    
    By default, the graph shows data for all result pages in the Search service application. 
    
    You can filter this report by:
    
  - Start date/time
    
  - End date/time
    
  - Client type
    
  - Result page (search results page), which only shows if verbose logging is enabled.
    
  - Source type (result source type):
    
  - Best Bet Provider
    
  - Exchange Search Provider
    
  - Local People Provider
    
  - Local SharePoint Provider
    
  - OpenSearch Provider
    
  - Personal Favorites Provider
    
  - Remote People Provider
    
- SharePoint Search Provider (Local SharePoint Search Flow Query Latency)
    
    For a specified time interval, shows the query latency (in milliseconds) for all queries that are processed by the local SharePoint search provider. The graph shows the query latency for:
    
  - Keyword parsing
    
  - Linguistics
    
  - Recommendations Security Trimming
    
  - Security token construction
    
  - Index lookup
    
  - Result type processing
    
  - Custom security trimming
    
  - Summary generation
    
  - Other
    
  The graph includes an overlay of query rate during the specified time interval.
    
  You can filter this report by:
    
  - Start date/time
    
  - End date/time
    
  - Client type
    
- People Search Provider (People Search Flow Query Latency)
    
    For a specified time interval, shows the query latency (in milliseconds) for all queries that are processed by the local people search provider. The graph shows the query latency in each of the following areas:
    
  - Keyword parsing
    
  - Linguistics
    
  - People pre-processing
    
  - Security token construction
    
  - Index lookup
    
  - Result type processing
    
  - Custom security trimming
    
  - Summary generation
    
  - Other
    
  The graph includes an overlay of query rate during the specified time interval.
    
  You can filter this report by:
    
  - Start date/time
    
  - End date/time
    
  - Client type
    
- Index Engine (Index Engine Query Latency
    
    For a specified time interval, shows the query latency in milliseconds for each index server that you filter on. By default, the graph shows data for all result pages in the Search service application. You can filter this report by:
    
  - Start date/time
    
  - End date/time
    
  - Index server (a computer that hosts at least one index partition)
    
  - Result page (search results page), which only shows if verbose logging is enabled.
    
  The graph includes an overlay of the index lookup time for the specified time interval in the past. Index lookup time is the average amount of time during a given minute that it took the index engine to return results. The index lookup time applies only to queries for which the index engine returned results.
    
 **To view query health reports**
  
1. Verify that the user account that is performing this procedure is an administrator of or has Read permissions to the Search service application. 
    
2. In Central Administration, under **Application Management**, click **Manage service applications**.
    
3. On the Service Applications page, click the Search service application.
    
4. On the Search Administration page, in the Quick Launch, in the **Diagnostics** section, click **Query Health Reports**.
    
5. On the Search Service Application: Query Latency Trend page, click the query report that you want to view.
    
## Crawl health reports
<a name="proc2"> </a>

SharePoint Server provides the following reports about crawl health:
  
- Crawl Rate
    
    For a specified time interval, shows a graph and a summary of the following:
    
  - Number of content items crawled per minute. This includes:
    
  - Total content items
    
  - Modified items. These are content items that were changed and re-crawled.
    
  - Not modified items. These are content items that were not changed and were not crawled.
    
  - Security items. These are content items for which the security attributes were changed.
    
  - Deleted items. These are content items that were deleted from the content source and which must also be deleted from the index.
    
  - Average number of other crawl actions that were performed per minute. This includes:
    
  - Retries (crawl retries)
    
  - Errors (crawl errors)
    
  You can filter this report by: 
    
  - Start date/time
    
  - End date/time
    
  - Content sources (for example, Local SharePoint sites)
    
  - Machine
    
- Crawl Latency
    
    For a specified time, shows a graph of the number of items that form the crawl load, for each of the following:
    
  - In Crawler Queue
    
  - Waiting to submit to content processing
    
  - Submitted to content processing
    
  - Waiting to Commit (SQL)
    
  You can filter this report by machine only. 
    
  For a specified time interval, also shows a graph and a summary of the crawl latency; the amount of time in milliseconds that each content item is in each of the following subsystems in the feeding pipeline:
    
  - Crawler
    
  - Protocol handler (PH) 
    
  - Repository
    
  - SQL Time
    
  You can filter this report by:
    
  - Start date/time
    
  - End date/time
    
  - Content source (for example, Local SharePoint sites) 
    
  - Machine
    
- Crawl Queue
    
    For a specified time interval, shows the number of items in the following two crawl queues: 
    
  - Links to process. This is the number of uncrawled URLs that are queued to be crawled.
    
  - Transactions queued. This is the number of crawled URLs that arequeued to be processed in the crawl pipeline.
    
  You can filter this report by start date/time and end date/time.
    
- Crawl Freshness
    
    For a specified time interval, shows the freshness of the content that was being indexed by the search system. The last modified time stamp of each document is compared with the time specified in the graph. You can view the freshness of the content as follows:
    
  - Less than 1 month ago
    
  - Less than 1 week ago
    
  - Less than 1 day ago
    
  - Less than 4 hours ago
    
- Content Processing Activity
    
    For a specified time interval, shows the amount of time that was spent in content processing for:
    
  - Content sources
    
  - Machines
    
  - Content processing components
    
  - Content processing activity
    
  The graph shows the amount of time that was spent in various content processing activities, such as:
    
  - Linguistics processing
    
  - Document parsing
    
  - Document summary generation
    
  - Indexing
    
  You can filter this report by:
    
  - Start date/time 
    
  - End date/time
    
  - Content source
    
  - Machine
    
  - Content processing component name
    
  - Processing activity 
    
- CPU and Memory Load
    
    For a specified time interval, shows the percentage of CPU used, the memory use in megabytes and the system overview for these processes:
    
  - MSSDmn
    
  - MSSearch
    
  - NodeRunner
    
  - Timer
    
  You can filter this report by:
    
  - Machine
    
  - Start date/time 
    
  - End date/time
    
- Continuous Crawl
    
    For a specified time interval, shows the time (in milliseconds) that the processes took with an overlay of discovery time (in minutes) for:
    
  - Time In Links Table
    
  - Time In Queue Table
    
  - Crawler Time
    
  - PH (Protocol Handler) Time
    
  - Repository Time
    
  - Content Pipeline Time
    
  - SQL Time
    
  You can filter this report by:
    
  - Content sources
    
  - Start date/time 
    
  - End date/time
    
 **To view crawl health reports**
  
1. Verify that the user account that is performing this procedure is an administrator of or has Read permissions to the Search service application. 
    
2. In Central Administration, under **Application Management**, click **Manage service applications**.
    
3. On the Service Applications page, click the Search service application.
    
4. On the Search Administration page, in the Quick Launch, in the **Diagnostics** section, click **Crawl Health Reports**.
    
5. On the Search Service Application: Crawl Reports page, click the crawl health report that you want to view.
    
## Crawl log
<a name="proc3"> </a>

The crawl log tracks information about the status of crawled content. This log lets you determine whether crawled content was successfully added to the index, whether it was excluded because of a crawl rule, or whether indexing failed because of an error. The crawl log also contains information such as the time of the last successful crawl and whether any crawl rules were applied. You can use the crawl log to diagnose problems with the search experience. 
  
 **To view the crawl log**
  
1. Verify that the user account that is performing this procedure is an administrator of the Search service application, or has Read permissions to it.
    
2. In Central Administration, under **Application Management**, click **Manage service applications**.
    
3. On the Service Applications page, click the Search service application.
    
4. On the Search Administration page, in the Quick Launch, in the **Diagnostics** section, click **Crawl Log**.
    
5. On the Crawl Log - Content Source page, click the view that you want.
    
### Crawl log views

The following table shows the different views that you can select to see the status of crawled content.
  
**Overview of crawl log views**

|        **View**        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| :--------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Content Source   | Summarizes items crawled per content source. Shows successes, warnings, errors, top-level errors, and deleted items. The data in this view represents the current status of items that are already present in the index per content source.  <br/><br/> You can also see the average time that it took to complete a crawl of a content source for the last crawl, for the last 24 hours, for the last 7 days and for the last 30 days. You can view the developments of the crawl duration, and see whether a particular content source is getting smaller or larger in size.                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Host Name        | Summarizes items crawled per host. Shows successes, warnings, errors, deleted items, top-level errors, and the total number of crawled items. The data in this view represents the current status of items that are already present in the index per host.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Crawl History    | Summarizes crawl transactions that were completed during a crawl. There can be multiple crawl transactions per item in a single crawl, so the number of transactions can be larger than the total number of items. This view shows data for these crawls:  <br/><br/>**Full**. Crawls all items in a content source.  <br/><br/> **Incremental**. Crawls items that have changed since the last full or incremental crawl. This kind of crawl only runs if it is scheduled.  <br/><br/>**Delete**. If start addresses are removed from a content source, a delete crawl removes items associated with the deleted start address from the index before a full or incremental crawl runs. This kind of crawl cannot be scheduled.  <br/><br/> **Continuous**. Crawls items in a SharePoint content source on a very frequent interval. <br/><br/>  The Search Administration database provides the data for this view. You can filter the results by content source.  <br/><br/>  This view also shows the crawl rate and the repository latency.  |
| Error Breakdown  | Provides summaries of errors per content source or per host name. The MSSCrawlURLReport table in the crawl database provides the data for this view. You can filter by content source or by host.   <br/><br/>Note that the filter drop-down box only shows content sources that contain errors. If there is an error on an item that does not appear in the index, the error is not listed in this view.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Databases        | Lets you view the state of the crawl databases used by this Search service application.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| URL View         | Lets you search the crawl logs by content source, URL, or host name, and view details of all items in the index. The MSSCrawlURLReport table in the crawl database provides the data for this view. You can filter the results by setting the **Status**, **Message**, **Start Time**, and **End Time** fields. <br/><br/>Note that the URL View only shows the Display URL. If items have the same Display URL (for example for a folder or views) but different Access URLs, the same Display URL displays several times in the URL View. You can query the Crawl database directly to see which items have the same Display URL.  <br/>                                                                                                                                                                                                                                                                                                                                                                                     |
   
The following table shows which additional columns are available in the Content Source, Host Name and Crawl History views. These columns show information about crawled items.
  
**Overview of additional columns in the Content Source, Host Name and Crawl History views**

|     **Item**     |                                                                                                                                                                     **Description**                                                                                                                                                                      |
| :--------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Successes        | Items were successfully crawled and searchable.                                                                                                                                                                                                                                                                                                          |
| Warnings         | Items might not have been successfully crawled and might not be searchable.                                                                                                                                                                                                                                                                              |
| Errors           | Items were not successfully crawled and might not be searchable.                                                                                                                                                                                                                                                                                         |
| Top Level Errors | Errors in top-level documents, including start addresses, virtual servers, and content databases. Every top-level error is counted as an error, but not all errors are counted as top-level errors. Because the **Errors** column includes the count from the **Top Level Errors** column, top-level-errors are not counted again in the Host Name view. |
| Deletes          | Items that were removed from the index and are no longer searchable.                                                                                                                                                                                                                                                                                     |
| Not Modified     | Items were not changed between crawls. This column only shows in the Crawl History view.                                                                                                                                                                                                                                                                 |
| Security Update  | The security settings of items were crawled because they were changed. This column only shows in the Crawl History view.                                                                                                                                                                                                                                 |
| Security Errors  | The security update of items caused an error. This column only shows in the Crawl History view.                                                                                                                                                                                                                                                          |
   
## Usage reports
<a name="Proc4"> </a>

You can use the usage reports and the search reports provided on the View Usage Reports page to view usage data that was collected about this site collection. 
  
 **To view usage reports**
  
1. Verify that the user account that is performing this procedure is an administrator of or has Read permissions to the Search service application.
    
2. In Central Administration, under **Application Management**, click **Manage service applications**.
    
3. On the Service Applications page, click the Search service application.
    
4. On the Search Administration page, in the Quick Launch, in the **Diagnostics** section, click **Usage Reports**.
    
5. On the View Usage Reports page, click the usage or search reports view that you want view.
    
The following table shows the different usage reports and search reports that you can select.
  
**Overview of usage report or search report**

| **Usage report or search report** |                                                                                                                               **Description**                                                                                                                               |
| :-------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Number of Queries                 | This report shows the number of search queries performed. Use this report to identify search query volume trends and to determine times of high and low search activity.                                                                                                    |
| Top Queries by Day                | This report shows the most popular search queries. Use this report to understand what types of information visitors are seeking.                                                                                                                                            |
| Top Queries by Month              | This report shows the most popular search queries. Use this report to understand what types of information visitors are seeking.                                                                                                                                            |
| Abandoned Queries by Day          | This report shows popular search queries that received low click-through. Use this report to identify search queries that might create user dissatisfaction and to improve the discoverability of content. Then, consider using query rules to improve the query's results. |
| Abandoned Queries by Month        | This report shows popular search queries that received low click-through. Use this report to identify search queries that might create user dissatisfaction and to improve the discoverability of content. Then, consider using query rules to improve the query's results. |
| No Result Queries by Day          | This report shows popular search queries that returned no results. Use this report to identify search queries that might create user dissatisfaction and to improve the discoverability of content. Then, consider using query rules to improve the query's results.        |
| No Result Queries by Month        | This report shows popular search queries that returned no results. Use this report to identify search queries that might create user dissatisfaction and to improve the discoverability of content. Then, consider using query rules to improve the query's results.        |
| Query Rule Usage by Day           | This report shows how often query rules trigger, how many dictionary terms they use, and how often users click their promoted results. Use this report to see how useful your query rules and promoted results are to users.                                                |
| Query Rule Usage by Month         | This report shows how often query rules trigger, how many dictionary terms they use, and how often users click their promoted results. Use this report to see how useful your query rules and promoted results are to users.                                                |
   

