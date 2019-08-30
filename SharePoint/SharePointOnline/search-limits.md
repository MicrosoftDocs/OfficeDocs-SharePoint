---
title: "Search limits for SharePoint Online"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 9/1/2017
audience: End User
ms.topic: reference
ms.service: sharepoint-online
localization_priority: Normal
search.appverid:
- SPO160
- MET150
ms.assetid: 7c06e9ed-98b6-4304-a900-14773a8fa32f
description: "As an admin who manages SharePoint Online (for more information, see SharePoint Online search administration overview), you should also be aware of limits to search. For example, there are limits to the number of entries you can have in a custom search dictionary or the number of rows that are returned as part of a search."
---

# Search limits for SharePoint Online

As an admin who manages SharePoint Online (for more information, see [SharePoint Online search administration overview](manage-search-the-admin-center.md)), you should also be aware of limits to search. For example, there are limits to the number of entries you can have in a custom search dictionary or the number of rows that are returned as part of a search.
  
There are two types of limits:
  
- **Boundary** A number that can't be exceeded. 
    
- **Supported** A recommended number, based on testing that Microsoft has done, that shouldn't be exceeded. 
    
    If you exceed a supported limit, you might encounter unexpected results or see a significant decrease in performance.
    
  
These limits apply to all SharePoint Online plans.
  
The following table lists the limits for SharePoint Online search.
  
|**Limit**|**Maximum value**|**Limit type**|**Notes**|
|:-----|:-----|:-----|:-----|
|Size of document that can be downloaded by the crawl components  <br/> |64 MB, 3MB for Excel documents  <br/> |Boundary  <br/> |Search downloads metadata and content from a document until it reaches the maximum document size. The rest of the content is not downloaded.  <br/> |
|Parsed content size  <br/> |2 million characters  <br/> |Boundary  <br/> |Search stops parsing an item after it has parsed up to 2 million characters of content from it, including the item's attachments. The actual amount of parsed characters can be lower than this limit because search uses a maximum of 30 seconds on parsing a single item and its attachments. When search stops parsing an item, the item is marked as partially processed. Any unparsed content isn't processed and therefore isn't indexed.  <br/> |
|Characters processed by the word breaker  <br/> |1,000,000  <br/> |Boundary  <br/> |Search breaks content into individual words (tokens). The word breaker produces tokens from the first 1,000,000 characters of a single item, including the item's attachments.  <br/> The actual amount of tokens can be lower than this limit because search uses a maximum of 30 seconds on word breaking. Any remaining content isn't processed.  <br/> |
|Indexed managed property size  <br/> |512 KB per managed property that is set to either "searchable" or "queryable"  <br/> |Boundary  <br/> ||
|Retrievable managed property size  <br/> |16 KB per managed property  <br/> |Boundary  <br/> ||
|Sortable and refinable managed property size  <br/> |16 KB per managed property  <br/> |Boundary  <br/> ||
|Token size  <br/> |Variable - the size depends on the word breaker, and the word-breaker is language-dependent.  <br/> |Boundary  <br/> |Search can index tokens of any length but the word breaker that is used to produce tokens can limit the token length. Word breakers are language-aware components that break content into single words (tokens).  <br/> |
|Number of entries in a custom search dictionary  <br/> |5,000 terms per tenant  <br/> |Boundary  <br/> |This limits the number of terms allowed for inclusions and exclusions dictionaries for query spelling correction and company extraction. You can store more terms than this limit in the term store, but search only uses 5,000 terms per tenant.  <br/> |
|Managed property mappings  <br/> |100 per managed property  <br/> |Supported  <br/> |Crawled properties can be mapped to managed properties. Exceeding this limit may decrease crawl speed and query performance.  <br/> |
|Values per managed property  <br/> |1,000  <br/> |Boundary  <br/> |A managed property can have multiple values of the same type. This is the maximum number of values per managed multi-valued managed property per document. If this number is exceeded, the remaining values are discarded.  <br/> |
|Unique contexts used for ranking  <br/> |15 unique contexts per rank model  <br/> |Boundary  <br/> ||
|Authoritative pages  <br/> |1 top level and minimal second- and third-level pages per tenant  <br/> |Supported  <br/> |Use as few second- and third-level pages as possible while still achieving the desired relevance.  <br/> If you add additional pages you may not achieve the desired relevance. Add the key site to the first relevance level. Add more key sites at either second or third relevance levels, one at a time. Evaluate relevance after each addition to ensure that you have achieved the desired relevance effect.  <br/> |
|Text length for queries using Keyword Query Language  <br/> |4 KB (4,096 characters)  <br/> |Boundary  <br/> |For Discovery queries the maximum text length is 16 KB (16,384 characters).  <br/> |
|Number of rows in a result set  <br/> |500  <br/> |Boundary  <br/> |To display the entire result set, issue more paging queries.  <br/> For Discovery queries the maximum number of rows in a result set is 10,000.  <br/> |
|User-defined full-text indexes  <br/> |3  <br/> |Boundary  <br/> ||
|Maximum number of on-premises items indexed in Office 365  <br/> |20 million items  <br/> |Threshold  <br/> |For each 1 TB of storage space your tenant has in Office 365, you can index 1 million items of on-premises content in your tenant's search index in Office 365 with the cloud hybrid search solution. This quota is by default limited upwards to 20 million items. To increase the number of items that can be indexed beyond 20 million items, contact Microsoft Support.  <br/> |
   
## See also:
  
- [SharePoint Online Limit](https://go.microsoft.com/fwlink/p/?LinkID=856113)
    
- [SharePoint Online Service Description](/office365/servicedescriptions/sharepoint-online-service-description/sharepoint-online-service-description)
    
- [Overview of the search schema in SharePoint Server 2013](/SharePoint/search/search-schema-overview)
    
- [SharePoint feature availability across Office 365 plans](/office365/servicedescriptions/sharepoint-online-service-description/search#bkmk_searchfeaturessp)
    

