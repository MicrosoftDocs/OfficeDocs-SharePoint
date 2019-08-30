---
title: "Changing the ranking of classic search results in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 9/4/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: 35f58247-a349-461b-b4d4-8963c3b98df6
description: "Learn how to change the ranking of classic search results in SharePoint Server."
---

# Changing the ranking of classic search results in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
 **Audience:** SharePoint Server and SharePoint Online search administrators. 
  
 **Before you start:**
  
To change the ranking of classic search results, you need:
  
- A basic understanding of search in SharePoint
    
- Knowledge and understanding of the content that is returned in search results, to judge how relevant a search result for a given query is
    
- A running Search service application and Enterprise Search Center
    
- Content in the search index
    
## Why is search result ranking important?

Whether you're working with an Enterprise Search Center on premises, with SharePoint Online, or with a cross-site publishing solution, your search results will be ranked. In most cases, this default search result ranking should be just fine.
  
But, sometimes, you may want to influence the ranking of search results to make results even more relevant to your end-users. We recently published a set of  articles that explain how you can change the ranking of search results and that will help you understand how search result ranking works in SharePoint Server. (See references later in this article.)
  
## How are search results ranked?

Search results are ranked using a ranking model. A ranking model calculates the position of a search result in the result set. There are several ranking models in SharePoint that automatically do this for you. So, usually, you don't have to care about which ranking model is used for a query, or what it does exactly.
  
## Using query rules to change search result ranking

If you are not satisfied with the search result ranking that SharePoint provides, we recommend that you add query rules to optimize search result ranking for your search scenarios.
  
The good thing about query rules is that they are available to a large range of search administrators. You can add query rules to the Search service application as a search administrator on premises, or as a tenant administrator in SharePoint Online. You can also add and reuse query rules as a site collection administrator or site owner, both on premises and online.
  
For each query rule, you can influence the way that you sort, rank and display search results. Each query rule consists of a query rule condition and a query rule action. Whenever a query matches a query rule condition, the query rule action that you specify in the query rule is triggered. After you have entered a condition, you can specify to:
  
- Add promoted results that always appear above the ranked search results.
    
- Add a result block that shows particular search results as a group, and promote that block.
    
- Change the order of the search results:
    
  - Sort by one or several managed properties.
    
    When you sort results in this manner, you override the ranking model.
    
  - Apply dynamic ranking.
    
    You can promote or demote results, based on a query condition that you specify.
    
[Influence the ranking of search results with query rules](overview-of-search-result-ranking.md#Ranking_QueryRules) provides more details. In most cases, you can use query rules to adjust ranking. However, to avoid increased query latency be careful not to add too complex or too many query rules. 
  
## Using custom ranking models: if query rules don't work

If it turns out that you can't use query rules to achieve your goals, you can consider creating and deploying a custom ranking model. For example, you can create a custom ranking model to include custom managed properties in the search result ranking calculations.
  
Since creating and tuning a custom ranking model is complex and can have a very large effect on your search results, we recommend that you do not take this lightly. You can only create and deploy a custom ranking model on premises.
  
When you create a custom ranking model, you copy an existing SharePoint Server ranking model and edit that copy. Then, you should validate how good the custom ranking model is by running many queries and comparing the results that you get with the new ranking model to the results that you got with the previous ranking model. Once you're done creating and validating, you deploy your custom ranking model and tell the search system that it should use the new ranking model to rank all or some of your search results.
  
As with any ranking model that is included with SharePoint Server, a custom ranking model calculates the position of a search result in the result set. A search result is considered relevant if it receives a high rank score. A high rank score is a specific numeric score that's calculated by the search engine that uses a ranking model. A ranking model is a list of one or more rank stages that contain a set of rank features. The ranking model defines how the search engine calculates the relevance rank using various factors, which are represented in the ranking model as rank features.
  
There are several ranking models available in SharePoint Server. For more details, see [Overview of search result ranking in SharePoint Server](overview-of-search-result-ranking.md). Most search results are ranked using the Default Search Model. Read [Customizing ranking models to improve relevance in SharePoint 2013](https://go.microsoft.com/fwlink/p/?LinkId=401186) on MSDN to learn more about the most important ranking features in the Default Search Model. This article also explains how to deploy a custom ranking model. 
  
We hope that the articles give you an overview of how search result ranking works and how you can change it.
  

