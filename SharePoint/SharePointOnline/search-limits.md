---
ms.date: 07/11/2018
title: "Search limits for SharePoint"
ms.reviewer: 
ms.author: jtremper
author: maggierui
manager: jtremper
recommendations: true
audience: End User
f1.keywords: NOCSH
ms.topic: reference
ms.service: sharepoint-online
ms.collection: M365-collaboration
ms.localizationpriority: medium
search.appverid:
- SPO160
- MET150
ms.assetid: 7c06e9ed-98b6-4304-a900-14773a8fa32f
description: "Learn about Search limits for SharePoint."
---

# Search limits for SharePoint

As an admin who manages SharePoint (for more info, see [SharePoint search administration overview](manage-search-the-admin-center.md)), you should also be aware of limits to search. For example, there are limits to the number of entries you can have in a custom search dictionary or the number of rows that are returned as part of a search.
  
There are two types of limits:
  
- **Boundary** A number that can't be exceeded.
- **Supported** A recommended number, based on testing that Microsoft has done, that shouldn't be exceeded.
    If you exceed a supported limit, you might encounter unexpected results or see a significant decrease in performance.
  
These limits apply to all SharePoint plans.
  
The following table lists the limits for SharePoint search.
  
|Limit|Maximum value|Limit type|Notes|
|:-----|:-----|:-----|:-----|
|Size of document that can be downloaded by the crawl components  |150 MB|Boundary  |Search downloads metadata of the document only for files >150 MB. The content of the document isn't downloaded.  |
|Parsed content size  |2 million characters  |Boundary  |Search stops parsing an item after it has parsed up to 2 million characters of content from it, including the item's attachments. The actual number of parsed characters can be lower than this limit because search uses a maximum of 30 seconds on parsing a single item and its attachments. When search stops parsing an item, the item is marked as partially processed. Any unparsed content isn't processed and therefore isn't indexed.  |
|Characters processed by the word breaker  |1,000,000  |Boundary  |Search breaks content into individual words (tokens). The word breaker produces tokens from the first 1,000,000 characters of a single item, including the item's attachments.  <br/> The actual amount of tokens can be lower than this limit because search uses a maximum of 30 seconds on word breaking. Any remaining content isn't processed.  |
|Indexed managed property size  |512 KB per managed property that is set to either "searchable" or "queryable"  |Boundary  ||
|Retrievable managed property size  |64 KB per managed property  |Boundary  ||
|Sortable and refinable managed property size  |16 KB per managed property  |Boundary  ||
|Token size  |Variable - the size depends on the word breaker, and the word-breaker is language-dependent.  |Boundary  |Search can index tokens of any length but the word breaker that is used to produce tokens can limit the token length. Word breakers are language-aware components that break content into single words (tokens).  |
|Unique indexed tokens per managed property |10,000 |Boundary |This is the maximum number of unique tokens that can be added to the search index per managed property. If the limit is exceeded, the index contains the first 10,000 tokens from the managed property and the file will be marked as partially processed by setting the IsPartiallyProcessed property to true. |
|Distinct users or Active Directory / Microsoft Entra security groups having access to an item |10,000 |Boundary |When more than 10,000 distinct users or Active Directory / Microsoft Entra security groups have access to an item, the item isn't searchable by any user. Such items will only be returned as part of an eDiscovery query through the Security & Compliance center. |
|Number of entries in a custom search dictionary  |5,000 terms per tenant  |Boundary  |This limits the number of terms allowed for inclusions and exclusions dictionaries for query spelling correction and company extraction. You can store more terms than this limit in the term store, but search only uses 5,000 terms per tenant.  |
|Managed property mappings  |100 per managed property  |Supported  |Crawled properties can be mapped to managed properties. Exceeding this limit may decrease crawl speed and query performance.  |
|Values per managed property  |1,000  |Boundary  |A managed property can have multiple values of the same type. This is the maximum number of values per managed multi-valued managed property per document. If this number is exceeded, the remaining values are discarded.  |
|Number of bytes in a multi-valued string property  |32 KB  |Boundary  |If you reach this limit, the multi-valued property is truncated.  |
|Unique contexts used for ranking  |15 unique contexts per rank model  |Boundary  ||
|Authoritative pages  |1 top level and minimal second- and third-level pages per tenant  |Supported  |Use as few second- and third-level pages as possible while still achieving the desired relevance.  <br/> If you add additional pages, you may not achieve the desired relevance. Add the key site to the first relevance level. Add more key sites at either second or third relevance levels, one at a time. Evaluate relevance after each addition to ensure that you have achieved the desired relevance effect.  |
|Text length for queries using Keyword Query Language  |4 KB (4,096 characters)  |Boundary  ||
|Number of rows in a result set  |500  |Boundary  |To display the entire result set, issue more paging queries.  <br/> For Discovery queries the maximum number of rows in a result set is 10,000.  |
|User-defined full-text indexes  |3  |Boundary  ||
|Maximum number of on-premises items indexed in Microsoft 365  |20 million items  |Threshold  |For each 1 TB of storage space your tenant has in Microsoft 365, you can index 1 million items of on-premises content in your tenant's search index in Office 365 with the cloud hybrid search solution. This quota is by default limited upwards to 20 million items. To increase the number of items that can be indexed beyond 20 million items, contact Microsoft Support.  |

## See also
  
- [SharePoint Limit](/office365/servicedescriptions/sharepoint-online-service-description/sharepoint-online-limits)
- [SharePoint Service Description](/office365/servicedescriptions/sharepoint-online-service-description/sharepoint-online-service-description)
- [Overview of the search schema in SharePoint Server 2013](../SharePointServer/search/search-schema-overview.md)
- [SharePoint feature availability across Office 365 plans](/office365/servicedescriptions/sharepoint-online-service-description/search#bkmk_searchfeaturessp)
