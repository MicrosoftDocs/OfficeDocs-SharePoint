---
title: "Understanding result sources for search in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/26/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: f3855245-795f-4a77-bc70-5456511eaadd
description: "Use a result source in SharePoint Server to specify a provider to get search results from for the classic search experience, and optionally to narrow a search to a subset of those results."
---

# Understanding result sources for search in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
This article provides a brief overview of result sources in SharePoint Server. 

> [!NOTE]
> The modern search experience in SharePoint Server 2019 gets its results from the default result source. If you change the default result source it impacts both the classic and modern search experiences.
    
## What is a result source?
<a name="BKMK_What"> </a>

When a user issues a query, the search system associates the query with a result source to provide search results. The result source is a definition that specifies each of the following: 
  
- A search provider or source URL to get search results from — for example, the search index of the local SharePoint Search service
    
- A protocol to use to get search results — for example, the OpenSearch protocol
    
- A query transform, which can narrow results from the given search provider or URL to a specified subset — for example, a subset that has a particular content type
    
A result source can also specify other settings, such as an authentication method to use when requesting results from a provider.
  
An example of a pre-configured result source is "Local Video Results". This result source specifies the local SharePoint search index as the provider and "Local SharePoint" as the protocol, and it has a query transform that specifies that it will return only files that have file extensions that correspond to videos, such as MP4. The "Local Video Results" result source is used by the Videos search experience, or search vertical, on the default enterprise Search Center results page.
  
The following screen shot shows the four search experiences that are available on a default enterprise Search Center results page. The user can choose one of these search experiences before submitting a query from the search box.
  
![enterprise Search Center default search experiences](../media/Videos_search_experience.gif)
  
The following table shows the result sources that are used by the four search experiences that are available on a default enterprise Search Center results page. Each search experience uses a different result source.
  
**Search experiences and corresponding result sources**

| **This search experience** | **Uses this preconfigured result source** |
| :------------------------- | :---------------------------------------- |
| Everything                 | Local SharePoint Results                  |
| People                     | Local People Results                      |
| Conversations              | Conversations                             |
| Videos                     | Local Video Results                       |
   
## Available result sources
<a name="BKMK_Result_sources_available"> </a>

SharePoint Server provides 16 pre-configured result sources, which are available in all sites and site collections in web applications that consume a Search service application. The pre-configured result sources are shown in the following table. You can view details about result sources from the Manage Result Sources page.
  
**Pre-configured result sources**

|     **This result source**     |                           **Specifies these items in the local SharePoint index**                            |
| :----------------------------- | :----------------------------------------------------------------------------------------------------------- |
| Conversations                  | Discussions in microblogs, newsfeed posts, and community sites                                               |
| Documents                      | Microsoft Office documents and PDF documents                                                                 |
| Items matching a content type  | Items that match a content type that the incoming query specifies                                            |
| Items matching a tag           | Documents or list items that match a managed metadata term that the incoming query specifies                 |
| Items related to current user  | Documents or list items that are related to the user in a way that the query template specifies              |
| Local People Results           | People items from the profile database of the User Profile service application                               |
| Local Reports and Data Results | Excel, Office Data Connection (ODC), or Report Definition Language (RDL) items, or items in a report library |
| Local SharePoint Results       | All items from the local SharePoint search index except People items                                         |
| Local Video Results            | Videos                                                                                                       |
| Pages                          |                                                                                                              |
| Pictures                       | Photos and images                                                                                            |
| Popular                        | Documents and list items sorted by view count                                                                |
| Recently changed items         | Documents and list items sorted by Modified date                                                             |
| Recommendations                | Documents and list items that you recommend for the incoming query                                           |
| Wiki                           | SharePoint wiki pages                                                                                        |
   
From the Manage Result Sources page, you can create other result sources in either of the following two ways:
  
- You can click **New Result Source**. For more information, see [Configure result sources for search in SharePoint Server](configure-result-sources-for-search.md).
    
- You can point to the arrow next to an existing result source, click **Copy**, and then modify the copy as necessary and save it with a new name.
    
## Result source protocols and URLs
<a name="BKMK_What_protocols_and_locations"> </a>

A result source specifies one of four protocols to use to get search results, as shown in the following table.
  
**Result source protocols**

| **A result source that specifies this protocol** |                                        **Gets search results from this search provider**                                         |
| :----------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------- |
| Local SharePoint                                 | The search index of the local Search service                                                                                     |
| Remote SharePoint                                | The search index of a Search service hosted in another farm                                                                      |
| OpenSearch 1.0/1.1                               | An external search provider (such as a remote search engine or feed) that uses the OpenSearch protocol to provide search results |
| Exchange                                         | Exchange Web Services                                                                                                            |
   
A result source that uses a protocol other than "Local SharePoint" must also specify a URL from which to get search results, as shown in the following table.
  
**Result source URLs**

| **A result source that uses this protocol** |                           **Must specify this URL**                            |
| :------------------------------------------ | :----------------------------------------------------------------------------- |
| Remote SharePoint                           | The address of the root site collection of the remote SharePoint Server farm   |
| OpenSearch 1.0/1.1                          | The URL of the RSS feed of a search provider that uses the OpenSearch protocol |
| Exchange                                    | An Exchange Web Services URL                                                   |
   
## Who can create result sources?
<a name="BKMK_Who"> </a>

Result sources can be created at the Search service application level, site collection level, or site level. This enables Search service application administrators, site collection administrators, and site owners to create and use result sources to meet their specific requirements for providing search results to users. When you create a result source at the Search service application level, for example, the result source is available to any query rule that is created at the same level, and also to any query rule that is created for a site collection or site that is in a web application that consumes that Search service application. For information about levels and permissions for result sources, see [Create a result source](configure-result-sources-for-search.md#BKMK_CreateResutlSource) in [Configure result sources for search in SharePoint Server](configure-result-sources-for-search.md). 
  
## Specifying a result source to use for a query
<a name="BKMK_When"> </a>

A query is initially associated with a result source according to the search experience in which the user performs the query. For example, if a user clicks **People** below a search box (see the screen shot earlier in this article) to specify the People search experience, the query uses the "Local People Results" result source. 
  
A Search Box Web Part is always associated with a particular Search Results Web Part. When a user types a query in a search box, the Search Box Web Part sends the query to the associated Search Results Web Part. That Search Results Web Part specifies the result source for the query; by default, this result source is "Local SharePoint Results". You can set a different result source as the default. You can also edit any Search Results Web Part to specify a different result source for it to use. For example, you might add a new search experience called "Reports", and create a search results page for displaying search results for that search experience. You could then edit the default Search Results Web Part that is on the new Reports results page to specify an appropriate result source for that search experience. An example of such a result source would be a SharePoint site that contains content types that correspond to reports. For more information, see the following resources:
  
- [Set a result source as default](../administration/configure-result-sources-for-web-content-management.md#BKMK_Default) in [Configure result sources for search in SharePoint Server](configure-result-sources-for-search.md)
    
- [Configure properties of the Search Results Web Part in SharePoint Server](configure-properties-of-the-search-results-web-part.md)
    
You can configure the search system so that a query becomes associated with an additional or a different result source under certain conditions. One way to do this is to create a query rule that displays search results from another result source if a query is more frequently performed in that result source than in the one that the user performed it on. For example, let's say that a user queries on "keynote speech" in the Conversations search experience but the query is more popular in the Videos search experience. In that case, you could configure an action that also displays results from the Videos result source in a separate result block. For more information, see the following resources:
  
- [Transforming queries with query rules](plan-to-transform-queries-and-order-results.md#Trans_Query_Rules) in [Plan to transform queries and order results in SharePoint Server](plan-to-transform-queries-and-order-results.md)
    
- [Manage query rules in SharePoint Server](manage-query-rules.md)
    
When you create a query rule, on the Manage Query Rules page you specify a result source to which the rule will apply. Then on the Add/Edit Query Rule page, in the **Context** section, you can add or remove result sources to which the rule will apply. When a query is submitted to any result source other than those that you set as applicable, the rule cannot fire. For example, if you create a query rule that you want to fire only for people searches, you would specify "Local People Results" as the result source to which the rule applies. 
  
## Narrowing search results by using a query transform
<a name="BKMK_How-does_query_transform_affect_query"> </a>

You can configure the search system so that it interprets the intent of user queries and then modifies queries accordingly to provide more targeted search results. One way to do this is to use the **Query Transform** section that is part of the definition of each result source. For example, to provide a Videos search experience, in the result source you could configure a query transform to specify a SharePoint site from which to get search results for video queries. 
  
You can also modify queries in the Web Part that issues a query, and in query rules. A user query is transformed first by any modifications that were configured in the Web Part, then by any query rules that fire, and finally by the query transform in the result source for the query. The query rules and result sources can take the modified query as input and modify the query again. However, the modifications made to a query by a result source cannot be modified further, because the query transform in a result source modifies the query last. For more information, see [Plan to transform queries and order results in SharePoint Server](plan-to-transform-queries-and-order-results.md).
  
Each pre-configured result source uses a query transform and thus provides an example of how you can use a query transform to narrow search results. On the Manage Result Sources page, you can click each result source to see how it uses a query transform. For example, you can click the pre-configured "Local People Results" result source to see that it uses the following query transform to provide people-related results from the profile database:
  
{?{searchTerms} ContentClass=urn:content-class:SPSPeople}
  
For more information, see [Building search queries in SharePoint 2013 (https://msdn.microsoft.com/library/jj163973.aspx)](https://msdn.microsoft.com/library/jj163973.aspx).
  
## See also
<a name="BKMK_How-does_query_transform_affect_query"> </a>

[Query variables in SharePoint Server](../technical-reference/query-variables.md)
  
[Default connectors in SharePoint Server](../technical-reference/default-connectors.md)
  
[Transforming queries in result sources](plan-to-transform-queries-and-order-results.md#Trans_Result_Sources)
  
[About result sources and federation](plan-crawling-and-federation.md#Section12)

