---
title: "Plan hybrid federated search for SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 6/20/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- Ent_O365_Hybrid
- IT_Sharepoint_Server
- IT_SharePoint_Hybrid_Top
ms.assetid: d845819f-0cbf-4595-bb14-19414acbd79b
description: "Plan to configure a SharePoint hybrid environment so that user searches from a Search Center display hybrid federated results."
---

# Plan hybrid federated search for SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-SPO-md](../includes/appliesto-2013-2016-2019-SPO-md.md)] 
  
A SharePoint hybrid environment enables you to provide hybrid solutions that integrate functionality and data access between services and features of SharePoint Online in Office 365 and SharePoint Server. With SharePoint hybrid federated search, user searches from a Search Center display hybrid results—that is, results from both the SharePoint Server 2013 and SharePoint Online search indexes.
  
    
## Options for displaying hybrid federated search solutions
<a name="BKMK_AvailableSolutions"> </a>

You can set up SharePoint hybrid federated search so that it works in either or both of the following two ways:
  
- User searches from the SharePoint Server Search Center display hybrid results. This is called outbound hybrid search. For information about how to set up outbound hybrid search, see [Display hybrid federated search results in SharePoint Server](display-hybrid-federated-search-results-in-sharepoint-server.md)
    
- User searches from the SharePoint Online Search Center display hybrid results. This is called inbound hybrid search. For information about how to set up inbound hybrid search, see [Display hybrid federated search results in SharePoint Online](display-hybrid-federated-search-results-in-sharepoint-online.md)
    
You can set up either search option first, and then optionally also set up the other one at any time.
  
**Watch a video about some of the main concepts behind hybrid SharePoint Search. (Length: 9 minutes 20 seconds)**

> [!VIDEO https://www.microsoft.com/videoplayer/embed/fbfdea50-faac-4232-806a-390d4f4e8900?autoplay=false]
  
## Choosing an option for displaying hybrid federated search
<a name="BKMK_ChoosingSolution"> </a>

How do you decide whether to set up hybrid federated search in the SharePoint Server farm (outbound hybrid search), or in SharePoint Online (inbound hybrid search), or both? That can depend in part on which deployment users are working in, what content they will need, and where that content is stored.
  
Outbound hybrid search is generally simplest hybrid federated search solution to configure, primarily because it doesn't require configuration of a reverse proxy device. It is also generally the safest hybrid federated search solution because, unlike inbound hybrid search, it doesn't involve receiving unsolicited calls from the Internet.
  
For the convenience of users, it can be beneficial to set up hybrid federated search in the deployment where most users are working. That way, users don't have to go to the remote deployment to search for content.
  
For performance reasons, it can be beneficial to set up hybrid federated search in the deployment where most of the content is stored. If most of the search results are from the local deployment, the overall query latency is likely to be less (all other things being equal) than if many results are from the remote deployment. Also, in general, when a user clicks a search result for local content, the response time to open that content will be faster than it would be to open content that is stored remotely. This is especially true for large files.
  
It can be reasonable to set up hybrid federated search in both deployments under any of the following circumstances:
  
- Many users are working in one deployment and many other users are working in the other deployment.
    
- Much of the content is in one deployment and much is in the other deployment.
    
- Most users are working in one deployment and most of the content is in the other deployment.
    
> [!IMPORTANT]
> If there is content in SharePoint Server that you don't want users of SharePoint Online to be able to view due to regulatory or legal or geopolitical constraints, then you should not set up any hybrid federated search in SharePoint Online that could return results that include that SharePoint Server content. For more information, see [Delete items from the search index or from search results in SharePoint Server](../search/delete-items-from-the-search-index-or-from-search-results.md). 
  
## Prerequisites for hybrid federated search
<a name="BKMK_Prereqs"> </a>

This section covers the phases of the hybrid deployment process that you have to complete before you perform each of the possible SharePoint hybrid federated search configurations.
  
In this section:
  
- [Prerequisites for outbound hybrid search ](#BKMK_PrereqsOutbound)
    
- [Prerequisites for inbound hybrid search](#BKMK_PrereqsInbound)
    
### Prerequisites for outbound hybrid search
<a name="BKMK_PrereqsOutbound"> </a>

Before you can configure SharePoint Server to display hybrid federated search results, you have to complete all the steps in the [Configure hybrid federated search from SharePoint Server to SharePoint Online - roadmap](configure-hybrid-federated-search-sharepoint-serverroadmap.md). You must also do the following:
  
- Perform at least one crawl in the SharePoint Server deployment, so that there is content in the SharePoint Server search index. (The SharePoint Online content must also be crawled, but you don't have to attend to that because SharePoint Online crawls its content automatically.) For more information, see [Manage crawling in SharePoint Server](../search/manage-crawling.md).
    
- Create an enterprise Search Center in the SharePoint Server deployment by using the Enterprise Search Center template to create a new site collection. For more information, see [Create a Search Center site in SharePoint Server](../search/create-a-search-center-site.md).
    
### Prerequisites for inbound hybrid search
<a name="BKMK_PrereqsInbound"> </a>

Before you can configure SharePoint Online to display hybrid federated search results, you have to complete all the steps in the [Configure hybrid federated search from SharePoint Online to SharePoint Server - roadmap](configure-hybrid-federated-search-sharepoint-onlineroadmap.md).
  
In addition, you have to perform at least one crawl in the SharePoint Server deployment, so that there is content in the SharePoint Server search index. (The SharePoint Online content must also be crawled, but you don't have to attend to that because SharePoint Online crawls its content automatically.) For more information, see [Manage crawling in SharePoint Server](../search/manage-crawling.md).
  
## Planning considerations for hybrid federated search
<a name="BKMK_PlanningConsiderations"> </a>

In this section:
  
- [Benchmark local search performance before you deploy hybrid federated search](plan-hybrid-federated-search.md#BKMK_Benchmark)
    
- [Plan where to create the result source and query rule](#BKMK_PlanWhereCreate)
    
- [Plan where to display the result block from the remote deployment](#BKMK_PlanWhereDisplay)
    
- [Consider providing hybrid federated search results only for certain searches](plan-hybrid-federated-search.md#BKMK_OnlyCertainSearches)
    
- [Train users how to get around in the SharePoint hybrid environment](#BKMK_TrainUsers)
    
### Benchmark local search performance before you deploy hybrid federated search
<a name="BKMK_Benchmark"> </a>

Before you deploy hybrid federated search, we strongly recommend that you test local search in whichever deployments you plan to deploy hybrid federated search, such as in SharePoint Online or in SharePoint Server. At that time, troubleshoot any issues that arise that are related to local search, until you have local search working smoothly. That way, if search-related issues arise after you deploy hybrid federated search, you might have a better idea whether those issues might be attributable to hybrid federated search. 
  
For example, in hybrid federated search, search results from the two deployments are displayed synchronously, which means that no results are displayed until results from both deployments are available. For this reason, if there is significant query latency, it is not likely to be immediately evident whether getting results from one deployment or the other is causing the lag. Therefore, before you deploy hybrid federated search, test local search performance to determine benchmarks for query latency. You can do this by running tests that simulate the user query load. Then try the same tests after you deploy hybrid federated search. If there is an increase in query latency after you deploy hybrid federated search, it might be due to a delay in getting search results from the remote deployment. The remote deployment might be slow to respond, or there might be network-related delays caused by factors such as low network bandwidth or geographical distance between the two deployments.
  
### Plan where to create the result source and query rule
<a name="BKMK_PlanWhereCreate"> </a>

When you configure either outbound or inbound hybrid search, there are two main steps. You perform these steps in the deployment in which you want users to be able to get hybrid federated search results. The first step is to create a result source, which specifies where to get remote search results from. For example, if you are configuring outbound search, you create a result source in the SharePoint Server farm that specifies SharePoint Online as the remote provider to get search results from. In the second step, you create a query rule. When the query rule fires, it causes search results from content in the remote deployment to be displayed in a separate group, called a result block, on a search results page in the local deployment.
  
You can create the result source and query rule at the Search service application level in SharePoint Server (or at the tenant level in SharePoint Online), or at the site collection level, or the site level. If you create the result source at the Search service application level, the result source will be available to any query rule that is created at the same level, and also to any query rule that is created for a site collection or site that is in a web application that consumes the Search service application. Also, if you create the result source and query rule at the Search service application level, then they might be easier to keep track of, and they can generally be recovered in the case of a disaster recovery scenario. However, the advantage of creating the result source and query rule at the site collection level or the site level is that the administrative work of maintaining the result source and query rule is performed at that level, so that the Search service application administrator doesn't have to attend to it.
  
### Plan where to display the result block from the remote deployment
<a name="BKMK_PlanWhereDisplay"> </a>

In the query rule that you create for hybrid federated search, you can configure the result block from the remote deployment to be shown at the top of the first page of search results (above all of the results from the local deployment), or to be ranked by relevance compared to the results from the local deployment. For testing and troubleshooting, it's best to show the result block at the top of the first page of search results so that you can readily see it. This makes it easy to verify that results from the remote deployment are being displayed in the result block, and to verify that clicking a result does not result in an error in displaying the target of the search result. When you're done testing and troubleshooting, you can edit the query rule so that the result block is ranked by relevance compared to results from the local deployment. This setting that ranks the result block by relevance compared to local search results is typically more useful for users.
  
### Consider providing hybrid federated search results only for certain searches
<a name="BKMK_OnlyCertainSearches"> </a>

The easiest way to configure hybrid federated search is to create a query rule in the local deployment that fires and gets results from the remote deployment for any query text. As an alternative that will avoid delays in getting search results from the remote deployment, you can construct one or more query rules that will fire and get search results from the remote deployment only for certain searches, such as searches for which you know that there is relevant content in the remote deployment. For example, if there is content in the remote deployment about using a particular in-house software tool, you can specify conditions in a query rule so that the rule will fire only if a search query contains the name of the tool. When you create a query rule, you can also narrow its scope by specifying that the rule is only to be performed from certain categories (based on terms for topic categories in the term store of a Managed Metadata service application), or by specifying that the rule is only to be performed by users in certain user segments (based on terms that describe users in the term store of a Managed Metadata service application).
  
### Train users how to get around in the SharePoint hybrid environment
<a name="BKMK_TrainUsers"> </a>

With hybrid federated search, the target of a search result might be a document or site in the remote deployment. After a user clicks such a search result, it might be difficult for the user to know how to get back to the deployment they were working in before or where to go to perform another search. Users can click the Back button in the browser to return to the place they were working in before. However, it can also be helpful to share URLs with users to let them know how to get to sites and Search Centers that they will need to use in the SharePoint hybrid environment. 
  
## See also
<a name="BKMK_PlanningConsiderations"> </a>

#### Concepts

[Configure hybrid federated search from SharePoint Server to SharePoint Online - roadmap](configure-hybrid-federated-search-sharepoint-serverroadmap.md)
  
[Configure hybrid federated search from SharePoint Online to SharePoint Server - roadmap](configure-hybrid-federated-search-sharepoint-onlineroadmap.md)

