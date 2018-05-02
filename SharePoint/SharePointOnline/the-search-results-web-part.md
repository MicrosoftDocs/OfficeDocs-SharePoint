---
title: "Change settings for the Search Results Web Part"
ms.author: tlarsen
author: tklarsen
manager: arnek
ms.date: 2/13/2018
ms.audience: End User
ms.topic: article
f1_keywords:
- configureresultswpineditmode
ms.prod: office-online-server
localization_priority: Normal
search.appverid: SPO160
ms.assetid: 40ff85b3-bc5e-4230-b1dd-f088188e487e
description: "Learn how to change the query and other settings to display search results in the SharePoint Search Results Web Part."
---

# Change settings for the Search Results Web Part

The Search Results Web Part shows the search results of a query that was entered in a Search Box Web Part.
  
By default, the Search Results Web Part is used on all default search vertical pages. Search verticals are customized for searching specific content, such as ( **Everything**, **People**, **Conversations**, and **Videos**), and they display search results that are filtered and formatted for a specific content type or class. The Search Results Web Part shows search results, and it also sends the search results to the Refinement Web Part and to the Search Navigation Web Part.
  
> [!NOTE]
> See [Configure a Content Search Web Part in SharePoint](the-content-search-web-part.md) to add a Content Search Web Part (CSWP) to your page and configure it for simple and advanced results. 
  
The Search Results Web Part uses a query that's specified in the Web Part to show search results. As a SharePoint Online administrator, you can change the query or other settings for displaying search results.
  
To add and configure a Search Results Web Part on a page, see [About configuring the Search Results Web Part](about-configuring-the-search-results-web-part.md). You can also find additional information see [Configure properties of the Search Results Web Part in SharePoint Server](https://technet.microsoft.com/en-us/library/gg549987.aspx).
  
## What do you want to do?

> [Change the query in the Search Results Web Part](the-search-results-web-part.md#__toc349550189)
    
> [Define the query by using Keyword Query Language (KQL) in Advanced Mode](the-search-results-web-part.md#__define_the_query)
    
> [Add refiners](the-search-results-web-part.md#__add_refiners)
    
> [Define sorting](the-search-results-web-part.md#bkmk_define_sorting)
    
> [Add more settings](the-search-results-web-part.md#bkmk_add_more_settings)
    
> [Test your query](the-search-results-web-part.md#bkmk_test_your_query)
    
> [Define the query by using predefined values in Quick Mode](the-search-results-web-part.md#__define_the_query_1)
    
> [Change display template settings](the-search-results-web-part.md#__toc349550196)
    
> [Change Results settings and Results control settings](the-search-results-web-part.md#__toc349550197)
    
## Change the query in the Search Results Web Part
<a name="__toc349550189"> </a>

The Search Results Web Part uses a query that is specified in the Web Part to show search results. By default, this query uses the query variable  `{searchboxquery}`. The query variable is a placeholder for a value, which means that when you run the query, a value replaces the placeholder. For example, when a user types the search term yellow in the Search Box, the  `{searchboxquery}` variable in the Search Results Web Part searches for all items that contain the phrase yellow. 
  
By changing the query in the Search Results Web Part, you can:
  
- Change the result source to specify which content should be searched. By default, these result sources are set for the different search vertical pages:
    
- Everything (results.aspx): **Local SharePoint Results (System)**
    
- People (peopleresults.aspx): **Local People Results (System)**
    
- Conversations (conversationresults.aspx): **Conversations (System)**
    
- Videos (videoresults.aspx): **Local Video Results (System)**
    
- Add query variables or property filters to customize search results for different users or user groups.
    
- Promote or demote items or pages within the search results.
    
- Change the sorting of search results.
    
There are two main ways of changing the query:
  
- [Define the query by using Keyword Query Language (KQL) in Advanced Mode](the-search-results-web-part.md#__define_the_query)
    
- [Define the query by using predefined values in Quick Mode](the-search-results-web-part.md#__define_the_query_1)
    
### Define the query by using Keyword Query Language (KQL) in Advanced Mode
<a name="__define_the_query"> </a>

1. On the search results page, click **Settings**, and then click **Edit Page**. The search results page opens in Edit mode.
    
2. In the Search Results Web Part, move the pointer to the right of the Web Part title, click the arrow, and then click **Edit Web Part** on the menu. The Search Results Web Part tool pane opens under the ribbon in the top right of the page. 
    
3. In the Web Part tool pane, in the **Search Criteria** section, click **Change query**. The Build Your Query dialog box opens in **Advanced Mode**.
    
4. On the **BASICS** tab, in the **Select a query** section, select a result source to specify which content should be searched. 
    
5. You can now change the **Query text**. By default, the query variable {searchboxquery} is defined. Change the query text by using Keyword Query Language (KQL), or use the **Keyword filter** and **Property filter** lists to build the query: 
    
  - The keyword query can consist of free-text keywords, property filters, or operators. Use braces to enclose query variables. The query variables will be replaced with a value when the query is run. Keyword queries have a maximum length of 2,048 characters. For more information about KQL, see [Keyword Query Language (KQL) syntax reference](https://msdn.microsoft.com/en-us/library/ee558911%28v=office.15%29.aspx).
    
  - Use keyword filters to add query variables to your query. Select predefined query variables from the list, and then add them to the query by clicking **Add keyword filter**. For a list of available query variables, see [Query variables in SharePoint Server 2013](https://technet.microsoft.com/en-us/library/jj683123).
    
  - Use property filters to query the content of managed properties that are set to  *queryable*  in the search schema. Select managed properties from the **Property filter** lists. Click **Add property filter** to add the filter to the query. 
    
    > [!NOTE]
    > Custom managed properties are not shown in the **Property filter** list. To add a custom managed property to your query, in the ** Query text ** box, enter the name of your custom managed property followed by the query condition, for example  *MyCustomColorProperty:Green* 
  
6. Click **Test query** to see a preview of the search results. 
    
7. You can also add more details to your query:
    
  - [Add refiners](the-search-results-web-part.md#__add_refiners)
    
  - [Define sorting](the-search-results-web-part.md#bkmk_define_sorting)
    
  - [Add more settings](the-search-results-web-part.md#bkmk_add_more_settings)
    
  - [Test your query](the-search-results-web-part.md#bkmk_test_your_query)
    
8. Click **OK** to save the query and return to the Web Part tool pane. 
    
#### Add refiners
<a name="__add_refiners"> </a>

On the **REFINERS** tab, you can choose to limit returned results by adding preselected refiners to your query. 
  
You can specify that the search results that are returned in the Search Results Web Part should be limited to one or more values from the refiners. The list shows all managed properties that are enabled as refiners in the search schema.
  
- To add a refiner to the query, choose a refiner from the list, and then click **Add**.
    
You can specify that the search results should be grouped based on one or more managed properties. This is useful when there are several variants for a given item, and you want to group them under a single result.
  
- To define grouping of results, click **Show more** to show the **Group results** section. 
    
#### Define sorting
<a name="bkmk_define_sorting"> </a>

Use the **SORTING** tab to specify how to sort search results. You can define several levels of sorting, select which ranking model to use, and add rules for dynamic ordering. 
  
The **Sort by** list shows all managed properties that are set as sortable in the search schema. 
  
- To sort results based on managed properties:
    
1. In the **Sort by** list, select a managed property, and then select **Descending** or **Ascending**.
    
2. To add more sorting levels, click **Add sort level**.
    
- To sort results by relevance rank:
    
1. In the **Sort by** list, select **Rank**.
    
2. (Optional) In the **Ranking Model** list, choose the ranking model to use. 
    
3. (Optional) Under **Dynamic ordering**, you can specify additional ranking by adding rules that will change the order of results when certain conditions apply. Click **Add dynamic ordering rule**, and then specify conditional rules.
    
#### Add more settings
<a name="bkmk_add_more_settings"> </a>

Use the **Settings** tab to select more settings for your query. You can choose to use query rules, use URL rewriting, and specify whether to remove duplicate results or not. 
  
#### Test your query
<a name="bkmk_test_your_query"> </a>

The **Test** tab shows the final query text based on what you selected in the other tabs. You can test alternative queries by editing the query text directly. You can also test different query options by clicking **Show more**.
  
> [!NOTE]
> Any changes that you make to the query in the **Test** tab are not saved. 
  
|**Section**|**Description**|
|:-----|:-----|
|**Query text** <br/> |Shows the final query that will be run by the Search Results Web Part. The final query text is based on the original query template where dynamic variables are replaced with current values. Other changes to the query may be made as part of a query rule.  <br/> |
||Click **Show more** to display more information.  <br/> |
|**Query Template** <br/> |The content of the query template that is applied to the query.  <br/> |
|**Refined by** <br/> |The refiners that are applied to the query, as defined on the **REFINERS** tab.  <br/> |
|**Grouped by** <br/> |The managed property on which search results should be grouped, as defined in the **REFINERS** tab.  <br/> |
|**Applied query rules** <br/> |Shows which query rules are applied to the query.  <br/> |
|**Query template variables** <br/> |The query variables that will be applied to the query and the values of the variables that apply to the current page. Type other values to test the effect they will have on the query.  <br/> |
|User segment terms  <br/> |Test how the query works for different user segment terms. Click **Add user segment term** to add terms to the query.  <br/> |
|Test query  <br/> |Click the **Test Query** button to preview the search results.  <br/> |
   
[Top of Page](the-search-results-web-part.md#__top)
  
### Define the query by using predefined values in Quick Mode
<a name="__define_the_query_1"> </a>

1. On the **BASICS** tab, make sure that you are in Advanced Mode. Click **Switch to Quick Mode** in the top right corner if you are in Advanced Mode. 
    
2. In the Select a query section, select a result source to specify which content should be searched.
    
3. In the Restrict by app section, select an option from the list to restrict results to a specific site, library, list, or URL.
    
4. Choose options in the **Restrict by tag** section to limit results to content that's tagged with a term from a term set: 
    
5. Don't restrict by any tag: Search results will not be limited based on tags (default).
    
6. Restrict by navigation term of current page: Search results will be limited to content that's tagged with the term of the current page. The current tag is shown as the last part of the friendly URL. This choice only makes sense if your site uses managed navigation.
    
7. Restrict by current and child navigation: Search results will be limited to content that's tagged with the term of the current page (shown as the last part of the friendly URL), and content that's tagged with subterms of the current page. Only relevant if your site uses managed navigation.
    
8. Restrict on this tag: Search results will be limited to content that's tagged with the tag that you type in the box.
    
9. You can also add more details to your query:
    
  - [Add refiners](the-search-results-web-part.md#__add_refiners)
    
  - [Add more settings](the-search-results-web-part.md#bkmk_add_more_settings)
    
  - [Test your query](the-search-results-web-part.md#bkmk_test_your_query)
    
10. Click **OK** to save the query and return to the Web Part tool pane. 
    
[Top of Page](the-search-results-web-part.md#__top)
  
## Change display template settings
<a name="__toc349550196"> </a>

1. On the search results page, click **Settings**, and then click **Edit Page**. The search results page opens in Edit mode.
    
2. In the Search Results Web Part, move your pointer to the right of the Web Part title, click the arrow, and then click **Edit Web Part** on the menu. The Search Results Web Part tool pane opens under the ribbon in the top right of the page. 
    
3. In the Web Part tool pane, in the **Display Templates** section, in the **Results Control Display Template** list, you can choose a display template to control the overall look of the Web Part. 
    
4. In the other lists in this section, you choose a display template for  *individual results*  : 
    
  - The default selection is **Use result types to display items**. This selection will apply different display templates according to the result type of the search result. For example, if the result type of a search result is a PDF file, the display template **PDF Item** is applied. If the result type of a search result is an image, the **Picture Item** display template is applied. 
    
  - To apply one display template to all result types of the search results, select **Use a single template to display items**, and then select the display template that you want to apply.
    
See [Change how search results look by using result types and display templates](result-types-disp-templates.md) for more information. 
  
[Top of Page](the-search-results-web-part.md#__top)
  
## Change Results settings and Results control settings
<a name="__toc349550197"> </a>

1. On the search results page, click **Settings**, and then click **Edit Page**. The search results page opens in Edit mode.
    
2. In the Search Results Web Part, move your pointer to the right of the Web Part title, click the arrow, and then click **Edit Web Part** on the menu. The Search Results Web Part tool pane opens under the ribbon in the top right of the page. 
    
3. In the Web Part tool pane, in the **Settings** section, change **Results Settings** to specify how results are shown: 
    
|**If you select**|**Then the Web Part displays**|**Selected by default**|
|:-----|:-----|:-----|
|Number of results per page  <br/> |The maximum number of search results displayed per page.  <br/> ||
|Show ranked results  <br/> |Ranked results.  <br/> Clear to show only promoted blocks (such as promoted results or personal favorites) or result controls (such as result counts).  <br/> |Yes  <br/> |
|Show promoted results  <br/> |Search results that are promoted by using query rules.  <br/> |Yes  <br/> |
|Show "Did you mean?"  <br/> |Query spelling corrections as Did you mean suggestions.  <br/> |Yes  <br/> |
|Show personal favorites  <br/> |Users' personal favorites, which are results a user's previously clicked.  <br/> |Yes  <br/> |
|Show View Duplicates link  <br/> |A View Duplicates link that users can click to view results that were classified as duplicates.  <br/> |No  <br/> |
|Show link to search center  <br/> |Link to the Search Center.  <br/> |No  <br/> |
   
4. In the Web Part tool pane, in the **Settings** section, change **Results control settings** to specify more options for what to show in the Search Results Web Part: 
  
|**If you select**|**Then the Web Part displays**|**Selected by default:**|
|:-----|:-----|:-----|
|Show advanced link  <br/> |A link to the Advanced Search page.  <br/> |Yes  <br/> |
|Show result count  <br/> |The number of results found.  <br/> |Yes  <br/> |
|Show language dropdown  <br/> |A language drop-down list. Gives users a way to switch the language of their query. The drop-down list will only appear if the user's selected two or more languages from the search user preferences page  <br/> |Yes  <br/> |
|Show sort dropdown  <br/> |A sort drop-down list. Gives users a way to change the sort order of results.  <br/> |No  <br/> |
|Show paging  <br/> |A paging control below the search results.  <br/> |Yes  <br/> |
|Show preferences link  <br/> |A link to the search user preferences page.  <br/> |Yes  <br/> |
|Show AlertMe link  <br/> |A link to the Alert Me page.  <br/> |Yes  <br/> |
   
[Top of Page](the-search-results-web-part.md#__top)
  
See also:
  
- [Manage the Search Center in SharePoint Online](manage-the-search-center.md)
    
- [Change settings for the Search Box Web Part](the-search-box-web-part.md)
    
- [Change settings for the Search Navigation Web Part](the-search-navigation-web-part.md)
    
- [Change settings for the Refinement Web Part](the-refinement-web-part.md)
    

