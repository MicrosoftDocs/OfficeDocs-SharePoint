---
title: "Overview of the search schema in SharePoint Server"
ms.author: tlarsen
author: tlarsen
manager: pamgreen
ms.date: 3/9/2018
ms.audience: ITPro
ms.topic: article
ms.prod: office-online-server
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 86e4a832-ef3a-46cf-9b60-f9796292bf3e
description: "Summary: Learn how the search schema is used to build up the search index. The search schema contains the mapping from crawled properties to managed properties and the settings on the managed properties."
---

# Overview of the search schema in SharePoint Server

 **Summary:** Learn how the search schema is used to build up the search index. The search schema contains the mapping from crawled properties to managed properties and the settings on the managed properties. 
  
The search index is the center of search. What is in your search index determines what people will find when they look for information by entering search queries or by interacting with internet or intranet pages.
  
This article describes how content is collected in and retrieved from the search index by using the search schema. The search schema contains crawled properties, crawled property categories, the crawled to managed property mapping and the managed property settings. Managed property settings define what you can search for and how, for example if you can refine or query on a property. 
  
In this article:
  
- [Crawling and crawled properties](search-schema-overview.md#crawl_cps)
    
- [Managed properties and property mapping](search-schema-overview.md#mps_map)
    
- [The search schema](search-schema-overview.md#search_schema)
    
- [The search index](search-schema-overview.md#search_index)
    
- [Managed property settings overview](search-schema-overview.md#MP_Overview)
    
## Crawling and crawled properties
<a name="crawl_cps"> </a>

To build up the search index, you must first crawl content. You can crawl various content sources, for example SharePoint Servercontent, file shares or user profiles. The contents and metadata of the items that you crawl are represented as crawled properties.
  
Each item that has been crawled and passed on to the content processing component has crawled properties associated with it. Examples of properties are **Author**, **Title**, and **Creation Date**. Any new crawled properties will be discovered automatically. 
  
Crawled properties are grouped into categories that are based on the IFilter or protocol handler of the item. Example categories are **Office** (crawled properties from Word documents, Excel worksheets, and so on), **Business Data** (crawled properties from for example databases), and **Web** (crawled properties from web sites). 
  
For more information about crawling, see [Plan crawling and federation in SharePoint Server](plan-crawling-and-federation.md).
  
## Managed properties and property mapping
<a name="mps_map"> </a>

To include the contents and metadata of crawled properties in the search index, you must map crawled properties to managed properties. Only managed properties are written to the search index. 
  
Managed properties can have many settings. The settings on the managed property determine how the contents can be shown in search results and how people can search for it.
  
You can map multiple crawled properties to a single managed property. For example, you can map both the "Writer" and "Author" crawled properties to the "Author" managed property. Or, you can map a single crawled property to multiple managed properties. 
  
Also, the order in which crawled properties are mapped to a managed property can determine the content of a managed property. For example, a managed property can have multiple crawled properties mapped to it and can be set to includes all values from all crawled properties mapped to it. But, if you give the crawled property containing the SharePoint title priority over another title in the mapping, it will show the SharePoint title in the search results. 
  
A set of default mappings between crawled and managed properties has been defined, see [Overview of crawled and managed properties in SharePoint Server](../technical-reference/crawled-and-managed-properties-overview.md).
  
Some crawled property types automatically generate a new managed property and a mapping between the crawled and managed property. For example, all site columns from SharePoint libraries have this automatic generation and mapping. When you create a site column in a list, and you crawl that list, a crawled property, a managed property, and a mapping between the crawled and managed property is automatically created for the site column.
  
You can change the default mapping or any other mapping from crawled to managed properties, create new mappings, or create new managed properties. When you create a new managed property, or when you change certain settings on existing managed properties, a full crawl must complete before the managed property and its value is included in the search index. If the new or changed property is in a SharePoint library or list, you can reindex that individual library or list without starting a full crawl of the entire SharePoint content source. This has the same effect as a full crawl. 
  
See the table [Managed property settings overview](search-schema-overview.md#MP_Overview) later in this article for more information. 
  
## The search schema
<a name="search_schema"> </a>

The search schema is stored in the Search Administration database. The search schema contains: 
  
- The mapping between crawled properties and managed properties. This can be a mapping from one crawled property to one managed property, from one to many, many to one or even a many to many mapping. 
    
- How the managed properties should be written to the search index. For example, to which full-text index the values of the managed properties should be written and to which weight group (context).
    
- The settings for the different managed properties. For example, if you can search on, query on, or refine search results by particular managed properties.
    
- Crawled property categories that group properties according to their IFilter or protocol handler. If you edit a crawled property category, your changes apply to all of the crawled properties within the category. This can influence performance and how items are saved in the search index.
    
Search schema updates are propagated through the search system every minute.
  
### Multiple search schemas

You can create multiple search schemas. The main search schema is defined in the Search service application and can be edited in the Central Administration. Site collection administrators and tenant administrators can change the search schema for a particular site collection or tenant. For example, a site collection administrator can customize what is included in the search index by changing the search schema for that site collection and, by doing this, customize the search experience for that site collection. Site owners can view the search schema, but not change it. 
  
> [!NOTE]
> You can't view or change the site collection search schema in Central Administration. To view or make changes in the search schema for a site collection, you have to use Site Collection Administration. 
  
## The search index
<a name="search_index"> </a>

The search index consists of a set of files in folders on a server. The content processing component processes crawled items, uses the search schema to map crawled properties to managed properties, and translates the managed properties into a format that is written to the search index. In addition to various full-text indexes, there are separate indexes of the managed properties that are marked as retrievable and those that are marked as queryable. There is also a separate index for attribute vectors, and there are numeric indexes.
  
### Index update groups

Whenever an item changes, it must be re-indexed after it has been crawled again. To reduce the re-indexing load, SharePoint Server introduces several separate index update groups.
  
- **Default** Contains he majority of managed properties. This index update group contains all managed properties that do not belong to the Security, Link, Usage or People index update groups. 
    
- **Security** Contains the document Access Control List (ACL) managed property 
    
- **Link** Contains the managed properties related to link structure 
    
- **Usage** Contains the managed properties related to usage data 
    
- **People** Contains the managed properties related to people search 
    
Each update group is stored in a different folder in the search index.
  
### Full-text index

A full-text index contains all the text from the searchable managed properties that are stored in that full-text index. Each full-text index is divided into weight groups, also referred to as contexts. The different contexts relate to the relative importance of a managed property, which is one of the ranking features that are used to calculate the total relevance rank of a search result. The number, or ID, of a context is not important; the ranking model determines its relative importance by assigning a contribution weight to a particular context. A higher contribution weight results in a higher ranking score. For more information, see the section [Influence the ranking of search results by using the search schema](overview-of-search-result-ranking.md#Ranking_Schema) in the article [Overview of search result ranking in SharePoint Server](overview-of-search-result-ranking.md).
  
There are two pre-defined full-text indexes other than the default full-text index: the SharePoint Terms full-text index ( **SpTermsIdx** ) and the People index ( **PeopleIdx** ). 
  
Most managed properties are already mapped to a suitable context and full-text index by default. We do not recommend changing the context of any of the existing searchable managed properties. 
  
## Managed property settings overview
<a name="MP_Overview"> </a>

Settings on the managed properties determine how content is saved in the search index and if and how people can search for and retrieve it. 
  
The search schema can be edited in Central Administration, Site Collection Administration and Tenant Administration. Site administrators can view the search schema, but they can't edit the search schema. The following table describes the different settings and whether they are available for editing on different administrator levels.
  
|**Managed property setting**|**What it does**|**Example**|**Available in**|**Full crawl or reindex SharePoint list/library required after changing setting**|
|:-----|:-----|:-----|:-----|:-----|
|Searchable  <br/> |Enables querying against the content of the managed property. The content of this managed property is included in the full-text index.  <br/> |If the property is "author", a simple query for "Smith" returns items that contain the word "Smith" and items whose author property contains "Smith".  <br/> |Central Administration / Site Collection Administration / Tenant Administration  <br/> |Yes  <br/> |
|Advanced Searchable Settings  <br/> |Enables viewing and changing the full-text index that the managed property is written to. It also allows you to change the context of the managed property for the relevance rank calculation. We do not recommend changing the context of any of the existing managed properties. For more information, see the section [Influence the ranking of search results by using the search schema](overview-of-search-result-ranking.md#Ranking_Schema) in the article [Overview of search result ranking in SharePoint Server](overview-of-search-result-ranking.md).  <br/> ||Central Administration / Site Collection Administration / Tenant Administration  <br/> |Yes  <br/> |
|Queryable  <br/> |Enables querying against the specific managed property. The managed property name must be included in the query, either specified in the query itself or included in the query programmatically.  <br/> |If the managed property is "author", the query must contain "author:Smith".  <br/> |Central Administration / Site Collection Administration / Tenant Administration  <br/> |From disabled to enabled.  <br/> |
|Retrievable  <br/> |Enables the content of this managed property to be returned in search results. Enable this setting for managed properties that are relevant to present in search results.  <br/> ||Central Administration /Site Collection Administration /Tenant Administration  <br/> |From disabled to enabled.  <br/> |
|Allow multiple values  <br/> |Allows multiple values of the same type in this managed property.  <br/> |If this is the "author" managed property, and a document has multiple authors, each author name will be stored as a separate value in the managed property.  <br/> |Central Administration  <br/> |Yes  <br/> |
|Refinable  <br/> |Yes - active: Enables using the property as a refiner for search results in the front end. You must manually configure the refiner in the web part.  <br/> Yes - latent: Enables switching refinable to active later, without having to do a full re-crawl when you switch.  <br/> Both options require a full crawl to take effect.  <br/> **IMPORTANT:** If you select Yes - active or Yes - latent, you must also make the managed property Queryable.  <br/> |If the "author" managed property is set to Refinable, you can set up Author as a refiner in your search front-end later.  <br/> |Central Administration  <br/> |From disabled to enabled (if not already set to Sortable)  <br/> |
|Sortable  <br/> |Yes - active: Enables sorting the result set based on the property before the result set is returned.  <br/> Yes - latent: Enables switching sorting to active later without having to do a full re-crawl when you switch.  <br/> Both options require a full crawl to take effect.  <br/> |Use for large result sets that cannot be sorted and retrieved at the same time.  <br/> |Central Administration  <br/> |From disabled to enabled (if not already set to Refinable)  <br/> |
|Alias  <br/> |Defines an alias for a managed property if you want to use the alias instead of the managed property name in queries and in search results. Use the original managed property and not the alias to map to a crawled property.  <br/> |Use an alias if you don't want to or don't have permission to create a new managed property.  <br/> |Central Administration / Site Collection Administration / Tenant Administration  <br/> |No  <br/> |
|Token normalization  <br/> |Enables returning results independent of letter casing and diacritics used in the query.  <br/> |The query "curacao" will also match "Curaçao", "curacao" and "Curacao".  <br/> |Central Administration / Site Collection Administration / Tenant Administration  <br/> |Yes  <br/> |
|Complete matching  <br/> |Queries will only be matched against the exact content of the property.  <br/> |If you have a managed property "ID" that contains the string "1-23-456#7", complete matching only returns results on the query ID:"1-23-456#7", and not on ID:"1-23" or ID:"1 23 456 7".  <br/> |Central Administration / Site Collection Administration / Tenant Administration  <br/> |Yes  <br/> |
|Mappings to crawled properties  <br/> |The list shows all the crawled properties that are mapped to this managed property. A managed property can get its content from one or more crawled properties.  <br/> You can either include content from all crawled properties or include content from the first crawled property that is not empty, based on a specified order.  <br/> ||Central Administration / Site Collection Administration / Tenant Administration  <br/> |Yes  <br/> |
|Company name extraction  <br/> |Enables the system to extract company name entities from the managed property when crawling new or updated items. The extracted entities can later be used to set up refiners.  <br/> There is one pre-populated dictionary for company name extraction. The system saves the original managed property content unchanged in the index, and, in addition, copies the extracted entities to the managed property "companies". The "companies" managed property is configured to be searchable, queryable, retrievable, sortable and refinable.  <br/> You can edit the company name dictionary in the Term Store.  <br/> For more information, see [Manage company name extraction in SharePoint Server](manage-company-name-extraction.md).  <br/> ||Central Administration / Site Collection Administration / Tenant Administration  <br/> |Yes  <br/> |
|Custom entity extraction  <br/> |Enables one or more custom entity extractors to be associated with this managed property. This enables the system to extract entities from the managed property when crawling new or updated items. The extracted entities can later be used to set up refiners.  <br/> For more information, see [Create and deploy custom entity extractors in SharePoint Server](create-and-deploy-custom-entity-extractors.md).  <br/> ||Central Administration / Site Collection Administration  <br/> |Yes  <br/> |
   
## See also
<a name="MP_Overview"> </a>

#### Concepts

[Manage the search schema in SharePoint Server](manage-the-search-schema.md)
  
[Overview of crawled and managed properties in SharePoint Server](../technical-reference/crawled-and-managed-properties-overview.md)
  
[Plan crawling and federation in SharePoint Server](plan-crawling-and-federation.md)

