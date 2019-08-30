---
title: "Overview of search result ranking in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/24/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 7c8ddec1-c8ff-4a90-afae-387b27a653f1
description: "Learn how SharePoint Server uses ranking models to calculate the relevance rank of search results for the classic search experience and how you can influence the order of search results by using query rules, the search schema and ranking models."
---

# Overview of search result ranking in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
The search engine calculates the relevance rank, that is to say, the order in which the search results for a query appear. The ranking model is at the core of this calculation. In most cases, you can influence relevance by using the available SharePoint Server ranking models in combination with query rules without having to consider customizing any ranking models. 
  
    
## What is a ranking model?
<a name="Ranking_Models"> </a>

There are several ranking models in SharePoint Server that are optimized for specific cases. These ranking models provide an effective ranking of results without any further customization. A ranking model contains a collection of ranking features to calculate the rank score of a particular item, for example a document, in the search results. The type of content that is ranked determines the set of ranking features that the ranking model uses and the relative importance of these different ranking features. 
  
In the classic search experience, for the default search verticals **Everything**, **Videos**, **Conversations** and **People**, the search system uses the most appropriate ranking model automatically. If you create your own search vertical, you can configure which ranking model to use for that vertical. 
  
SharePoint Server provides the following types of ranking models:
  
- **General purpose ranking models.**
    
    General purpose ranking models compute the relevance rank for most types of search results.
    
- **People search ranking models.**
    
    People search ranking models compute the relevance rank for search results that are related to people. They calculate, among other things, how relevant search results are based on social distance and expertise.
    
- **Special purpose ranking models.**
    
    Special purpose ranking models compute the relevance rank for search results related to various specific ranking scenarios. For example, there is a ranking model to calculate the ranking score for recommendations and there are ranking models to calculate relevance ranks for cross-site publishing sites that have an associated product catalog.
    
The following table lists the available ranking models in SharePoint Server.
  
| **Ranking model type** |                **Ranking model name**                 |                                                                                                                                                         **Description**                                                                                                                                                          |
| :--------------------- | :---------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| General purpose        | Default Search Model                                  | Default ranking model for the Search service application. This ranking model ranks most search results, such as the search results for queries on the result source "Local SharePoint Results". This model is used for the search verticals **Everything**, **Videos** and **Conversations**.                                    |
| General purpose        | Search Ranking Model with Two Linear Stages           | This ranking model is a copy of the Default Search Model with the exception that stage two is a linear stage instead of a neural net stage. We recommend that you use a copy of this model as the base model if you want to create a custom ranking model.                                                                       |
| General purpose        | O15 MainResultsDefaultRankingModel                    | Ranking model that was used as the default ranking model for the Search service application before the SharePoint Server 2013 cumulative update of August 2013. The cumulative update introduces some improvements to the Default Search Model. This ranking model was added for backward compatibility.                         |
| General purpose        | O14 Default Search Model                              | Ranking model that was used as the default ranking model for the Search service application in SharePoint Server 2010 and Search Server 2010. This ranking model was added for backward compatibility.                                                                                                                           |
| General purpose        | Search Model With Boosted Minspan                     | Ranking model that puts a higher weight on proximity features than the Default Search Model. Proximity features in the ranking model look at each of the query terms and determine how close to one another these query terms occur in the items. Proximity is only considered in the managed properties **Body** and **Title**. |
| General purpose        | Search Model Without Minspan                          | Default Search Model without proximity features.                                                                                                                                                                                                                                                                                 |
| People search          | People Search application ranking model               | Default ranking model for people search. This ranking model ranks search results for people. People search is based on user profile information from My Sites that are kept in the User Profile service application.                                                                                                             |
| People search          | People Search expertise ranking model                 | Ranking model for people search that puts a higher weight on expertise. Expertise is calculated based on how few levels the person is from the top position within an organization.                                                                                                                                              |
| People search          | People Search expertise social distance ranking model | Ranking model for people search based on expertise with a higher weight on social distance. Social distance is the relationship, as defined by their position in the organization, between the user who typed the query and the people who are listed in the search results.                                                     |
| People search          | People Search name ranking model                      | Ranking model for people name search.                                                                                                                                                                                                                                                                                            |
| People search          | People Search name social distance ranking model      | Ranking model for people name search that puts a higher weight on social distance.                                                                                                                                                                                                                                               |
| People search          | People Search social distance model                   | Ranking model for people search that puts a higher weight on social distance.                                                                                                                                                                                                                                                    |
| Special purpose        | Catalog ranking model                                 | Ranking model for internet facing websites. This ranking model ranks search results for websites that use cross-site publishing and that have a product catalog associated with the SharePoint Server site collection.                                                                                                           |
| Special purpose        | Popularity ranking model                              | Ranking model for popularity based search. This ranking model ranks SharePoint Server content based on the number of times an item that is stored in SharePoint Server has been accessed.                                                                                                                                        |
| Special purpose        | Recommender ranking model                             | Ranking model to rank recommendations. Recommendations are based on item-to-item relationships collected from an analysis of how users have interacted with items on a site or with search results.                                                                                                                              |
| Special purpose        | Site suggestion ranking model                         | Ranking model for social suggestions. Items that other users have clicked will get a higher ranking.                                                                                                                                                                                                                             |
   
## How does a search result get a rank?
<a name="Ranking_SearchResults"> </a>

A ranking model computes the relevance rank of a search result. A search result gets a rank through a process called **rank evaluation**. The rank evaluation results in a ranking score. Items with the highest score get the highest position in search results. Search results are sorted in descending order based on their ranking score. 
  
For example, the default search model uses two stages for rank evaluation. During stage one, the ranking model applies fairly inexpensive ranking features to get a gross ranking of the results. During stage two, the ranking model applies additional and more expensive rank features to the items with the highest rank. By default, the search results page shows the ten documents that have the highest ranking score after these two stages of rank evaluation.
  
Each ranking model has several ranking features. The relative weight of these ranking features in the overall ranking calculation varies per ranking model. Ranking features can be query dependent or query independent. To calculate the final ranking score of a search result, all the calculations of all the ranking features in the ranking model are combined.
  
Ranking models use information from the search index, as explained in the following table.
  
| **Information about a search index item** |                                                                                              **Description**                                                                                               |
| :---------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Content                                   | These are the words contained in the items. For items that are text based, such as documents, this is typically most of the text. For other types of items, such as videos, there is little or no content. |
| Metadata                                  | The metadata associated with items such as title, author, URL and creation date. Metadata is automatically extracted from most types of items.                                                             |
| Web graph data                            | This is information such as authority (from authoritative pages settings) and anchor text (from the hyperlinks associated with the item, and items linking to the item).                                   |
| File type                                 | Some file types can be considered more important for ranking than others. For example, Word and PowerPoint results are typically more important than Excel results.                                        |
| Interaction                               | Information about the number of times a search result is clicked, and which queries led to a result being clicked.                                                                                         |
   
## How can I influence the rank of a search result?
<a name="Ranking_InfluenceIntro"> </a>

You can influence the ranking of search results in the following ways:
  
**Query rules: define which actions to take when a query matches a condition.**

Query rules apply to classic search results, with one exception. [Learn what's different for modern search.](differences-search-2016-2019.md)
    
  - Promote particular results to the top of the search results.
    
  - Add a result block to promote particular results.
    
  - Change the rank by changing the query.
    
    - Change the sorting of the ranked results based on managed properties.
    
    - Dynamically promote or demote particular results.
    
    - Change the ranking model when someone runs a certain query.
    
  See the section [Influence the ranking of search results with query rules](overview-of-search-result-ranking.md#Ranking_QueryRules) for more information. 
    
**Search schema: configure the context of a managed property.**
    
  - Change the context of a managed property in Advanced Searchable Settings.
    
    See the section [Influence the ranking of search results by using the search schema](overview-of-search-result-ranking.md#Ranking_Schema) for more information. 
    
**Create and use a custom ranking model.**

Custom ranking models only apply to the classic search experience.
    
  - Customize a copy of an existing ranking model, deploy it and use this custom model to rank search results.
    
    See the section [Influence the ranking of search results by using a custom ranking model](overview-of-search-result-ranking.md#Ranking_CustomModel) for more information. 
    
In most cases, using the available ranking models in SharePoint Server in combination with query rules should provide sufficient ways to influence ranking.
  
## Influence the ranking of search results with query rules
<a name="Ranking_QueryRules"> </a>

If you are not satisfied with the search result ranking for specific queries, we recommend that you try to influence the ranking for those queries with query rules. In most cases, configuring query rules will help you reach your goals, and you won't have to consider changing the context of a managed property or creating a custom ranking model. 
  
For each query rule, you can influence the way you sort, rank and display search results. Each query rule consists of a query rule condition and a query rule action. Whenever a query matches a query rule condition, the query rule action that you specify in the query rule triggers.
  
You can specify the following query rule actions for a query rule:
  
- **Add promoted results on top of the ranked search results.**
    
    When you add a promoted result, you show this result above the ranked results. For example, for the query "sick leave", you can add a link to a Human Resources site above all ranked results.
    
- **Add a result block.**
    
    A result block displays search results as a group. You can configure the query rule to define for which queries you want to show the results in a result block. In the same manner as you can promote a specific result, you can promote a result block when a specified query condition applies.
    
- **Change the rank by changing the query.**
    
  - **Sort by managed property.**
    
    You can change the sorting order of the search results by specifying by which managed property the search results should be sorted, and if this should be done in ascending or descending order. You can add more than one sort level. If you sort by one or more managed properties, you do not use a ranking model to rank the search results.
    
  - **Dynamic ordering: promote or demote search results.**
    
    You can dynamically change the ranking of search results. You can specify when you want to change the ranking of the search results for a query, and by how much, when a certain condition applies. The table below shows the conditions that you can set.
    

 
  - **Change the ranking model.**
    
    You can change which ranking model is used when a query rule fires.
    
| **Change ranking when:** |                                      **Description**                                       |
| :----------------------- | :----------------------------------------------------------------------------------------- |
| Result contains keyword  | Matches if the result contains the keywords anywhere in its contents, including meta-data. |
| Title contains keyword   | Matches if the result title contains the specified keywords or phrases.                    |
| Title matches keyword    | Matches if the result title exactly matches the specified keywords or phrases.             |
| URL starts with          | Matches if the result URL starts with the specified URL.                                   |
| URL exactly matches      | Matches if the result URL exactly matches the specified URL.                               |
| Content type is          | Matches if the result is of the content type that you specify.                             |
| File extension matches   | Matches if the result has the specified file extension.                                    |
| Result has the tag       | Matches if the result has the specified taxonomy tag as part of its meta-data.             |
| Manual condition         | Add any restriction using standard query syntax.                                           |

For more information, see [Plan to transform queries and order results in SharePoint Server](plan-to-transform-queries-and-order-results.md) and [Manage query rules in SharePoint Server](manage-query-rules.md).
  
## Influence the ranking of search results by using the search schema
<a name="Ranking_Schema"> </a>

You can influence the ranking of search results by changing the context of a searchable managed property in a full-text index. However, most managed properties are already mapped to a suitable context and full-text index by default. We do not recommend changing the context of any of the existing searchable managed properties. However, if you create a new managed property and you want this property to be considered by the ranking models, you have to map it to a full-text index context.
  
SharePoint Server has several full-text indexes. Each full-text index has several managed properties that are stored in that full-text index. In this section, we only discuss the default full-text index and only a few of the default full-text index contexts in combination with the default search ranking model.
  
A full-text index contains all the text from the searchable managed properties that are stored in that full-text index. Each full-text index is divided into weight groups, also referred to as contexts. The different contexts relate to the relative importance of a managed property, which is one of the ranking features that are used to calculate the total relevance rank. The number, or ID, of a context is not important; the ranking model determines its relative importance by assigning a contribution weight to a particular context. A higher contribution weight results in a higher ranking score.
  
By default, new managed properties are mapped to context 0, which means that they are returned in the search results but are not considered by any of the ranking models. If you want a new managed property to be considered by the default search ranking model, you should map it to the default full-text index and to one of the contexts shown in the table below. There are more contexts in the default full-text index, but you should only use the contexts mentioned in the following table. Each ranking model considers the contexts differently; the table only shows how the Default Search Model considers contexts in the default full-text index.
  
| **Context** | **Example of a managed property in this context** | **Relative contribution weight to ranking (Default Search Model and default full-text index)** |
| :---------- | :------------------------------------------------ | :--------------------------------------------------------------------------------------------- |
| 0           | -                                                 | Used only for recall, not for ranking.                                                         |
| 1           | **Title**                                         | 0.3610                                                                                         |
| 2           | **Filename**                                      | 0.1512                                                                                         |
| 5           | **Author**                                        | 0.1581                                                                                         |
| 7           | **Body**                                          | 0.0194                                                                                         |
   
For example, you create a new managed property of the type **string** that contains about ten words or less. You consider this new managed property to be about as important as the existing managed property **Title**. In that case, you should map the new managed property to context 1. 
  
Another example. You create a managed property of the type **string** that contains lots of words, for example a description of something. You should map this new managed property to context 7 because it is similar to the managed property **Body**, both in length as well as in importance. 
  
> [!IMPORTANT]
> Map managed properties with similar importance and size (in words) to the same context. 
  
After changing the context of a managed property, it is important to monitor the search results, as the change may not have the expected or desired consequences. It will take some time before the changes appear in the search results, because the content has to be re-indexed before changes to the search schema are picked up. If you have already crawled one or more content sources that include content that contains the managed property that you changed the context of, you have to do a full re-crawl of those content sources before you can see any changes in the ranking.
  
You can change the context of a searchable managed property in the **Advanced Searchable Settings**, using the search schema feature in the Search service application. See [Overview of the search schema in SharePoint Server](search-schema-overview.md) and [Manage the search schema in SharePoint Server](manage-the-search-schema.md) for more information. 
  
## Influence the ranking of search results by using a custom ranking model
<a name="Ranking_CustomModel"> </a>

The most advanced way to change the ranking of search results is to create a custom ranking model. In most cases, the ranking models that SharePoint Server supplies provide good ranking, and you can influence this ranking with query rules as discussed in [Influence the ranking of search results with query rules](overview-of-search-result-ranking.md#Ranking_QueryRules)
  
Examples of when you may want to create and use a custom ranking model:
  
- You have created a search experience in which query performance is extremely important and you want to make the ranking model calculations faster.
    
- You have built a custom app and want to create a ranking model that is specific to that app.
    
- You have added a special managed property for a special search experience and want to include this managed property in the ranking calculations. 
    
> [!CAUTION]
> If you create a custom ranking model, this influences all the queries using that ranking model. You should test the effect of the custom ranking model on many queries. 
  
You can read more about how to create, deploy and use a custom ranking model in the article [Customizing ranking models to improve relevance in SharePoint 2013](https://msdn.microsoft.com/library/c166ecdd-7f93-4bbb-b543-2687992dd2bc.aspx) on MSDN. 
  
> [!NOTE]
> If you want to create a custom ranking model for the default search results, use a copy of the **Search Ranking Model with Two Linear Stages** as the base model for your custom ranking model, it will be easier to re-tune and customize your ranking model. 
  
## See also
<a name="Ranking_CustomModel"> </a>


[Plan to transform queries and order results in SharePoint Server](plan-to-transform-queries-and-order-results.md)
  
[Overview of the search schema in SharePoint Server](search-schema-overview.md)
  
[Create a custom ranking model by using the Ranking Model Tuning App](https://docs.microsoft.com/en-us/sharepoint/search/create-custom-ranking-model)

