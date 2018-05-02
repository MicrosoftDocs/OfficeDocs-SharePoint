---
title: "How to build a query"
ms.author: tlarsen
author: tklarsen
manager: arnek
ms.date: 12/30/2016
ms.audience: End User
ms.topic: article
f1_keywords:
- HowToBuildYourQuery
- WSSEndUser_HowToBuildYourQuery
ms.prod: office-online-server
localization_priority: Normal
search.appverid:
- SPS150
- SPO160
- OSU150
- OSI150
- OSU160
ms.assetid: 2c2e5864-8590-4715-9568-267ad59654fd
description: "The Content Search Web Part displays content based on search. Every time a user opens a page that has a Content Search Web Part on it, a query is sent to the search index, and search results are displayed automatically in the Web Part. You can use one of the default queries that are available in Quick Mode, or you can choose to build your own query by using Advanced Mode."
---

# How to build a query

The Content Search Web Part displays content based on search. Every time a user opens a page that has a Content Search Web Part on it, a query is sent to the search index, and search results are displayed automatically in the Web Part. You can use one of the default queries that are available in **Quick Mode**, or you can choose to build your own query by using **Advanced Mode**.
  
## What do you want to do?
<a name="__top"> </a>

> [Build a quick query](how-to-build-a-query.md#__toc329693515)
    
> [Basics](how-to-build-a-query.md#__toc329693516)
    
> [Add refiners to your query](how-to-build-a-query.md#__goback)
    
> [Add more settings](how-to-build-a-query.md#__toc329693518)
    
> [Test your query](how-to-build-a-query.md#__toc329693519)
    
> [Build an advanced query](how-to-build-a-query.md#__toc329693520)
    
> [Basics](how-to-build-a-query.md#__toc329693521)
    
> [Add refiners to your query](how-to-build-a-query.md#__toc329693522)
    
> [Add more settings](how-to-build-a-query.md#__toc329693523)
    
> [Define sorting](how-to-build-a-query.md#__toc329693524)
    
> [Test your query](how-to-build-a-query.md#__toc329693525)
    
## Build a quick query
<a name="__toc329693515"> </a>

In **Quick Mode**, the Basics tab contains the most basic options for building a query. You can refine your query further by using the **Refiners** tab and the **Settings** tab, and test out search results for different versions of the final query on the **Test** tab. 
  
### Basics
<a name="__toc329693516"> </a>

You can easily build a query by selecting options on the **Basics** tab. The **Search Result Preview** pane on the right hand side automatically displays the search results. 
  
1. In the **Select a query** list, choose a query by selecting a result source. Result sources specify what content to get search results from. 
    
2. In the **Restrict results by app** list, select an option for restricting where you want to get search results from. 
    
3. Under **Restrict by tag**, you can choose to limit results to content that is tagged with specific terms.
    
4. Under **Restrict by content type**, you can choose to limit results to content of a specific content type.
    
5. Under **Add additional filters** you can add additional Keyword Query Language (KQL) restrictions. 
    
6. Click **OK** to save your settings. 
    
### Add refiners to your query
<a name="__toc329693516"> </a>

On the **Refiners** tab, you can choose to limit the results returned by adding pre-selected refiners to your query. You can also choose to group search results based on a managed property. Click **Show more** to display the **Group results** option. 
  
### Add more settings
<a name="__toc329693518"> </a>

On the **Settings** tab, you can select more settings for your query. You can decide to use query rules, use URL rewriting, select loading behavior, and define priority for the query. 
  
### Test your query
<a name="__toc329693518"> </a>

The **Test** tab shows the final query text based on what you selected in the other tabs. You can test alternative queries by editing the query text directly. You can also test different query options by clicking **Show more**.
  
> [!NOTE]
>  Any changes that you make to the query in the **Test** tab are not saved. 
  
[The Content Search Web Part displays content based on search. Every time a user opens a page that has a Content Search Web Part on it, a query is sent to the search index, and search results are displayed automatically in the Web Part. You can use one of the default queries that are available in Quick Mode, or you can choose to build your own query by using Advanced Mode.](how-to-build-a-query.md#__top)
  
## Build an advanced query
<a name="__toc329693520"> </a>

You can build a more advanced query by using Keyword Query Language (KQL). In Advanced Mode, the Basics tab contains lists for adding keyword filters and property filters to your query. The Advanced Mode also has a separate **Sorting** tab. 
  
### Basics

In the Basics tab, click **Switch to Advanced Mode** to display lists for adding keyword filters and property filters to your query. For more information about Keyword Query Language, see [Keyword Query Language (KQL) syntax reference](https://go.microsoft.com/fwlink/?linkid=261563) on MSDN. 
  
When you have added the filters, click **Test query** to display the results in the **Search Result Preview** pane on the right hand side. 
  
### Add refiners to your query
<a name="__toc329693522"> </a>

On the **Refiners** tab, you can choose to add refiners to your query. You can also choose to group search results based on a managed property. Click **Show more** to display the **Group results** option. 
  
### Add more settings
<a name="__toc329693523"> </a>

On the **Settings** tab, you can select more settings for your query. You can decide to use query rules, use URL rewriting, select loading behavior, and define priority for the query. 
  
### Define sorting
<a name="__toc329693524"> </a>

On the **Sorting** tab, you can define several levels of sorting your search results, select which ranking model to use, and add rules for dynamic ordering. 
  
### Test your query
<a name="__toc329693525"> </a>

The **Test** tab shows the final query text based on what you selected in the other tabs. You can test alternative queries by editing the query text directly. You can also test different query options by clicking **Show more**. 
  
> [!NOTE]
>  Any changes that you make to the query in the **Test** tab are not saved. 
  
[The Content Search Web Part displays content based on search. Every time a user opens a page that has a Content Search Web Part on it, a query is sent to the search index, and search results are displayed automatically in the Web Part. You can use one of the default queries that are available in Quick Mode, or you can choose to build your own query by using Advanced Mode.](how-to-build-a-query.md#__top)
  

