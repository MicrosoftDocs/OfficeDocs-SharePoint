---
title: "Plan to transform queries and order results in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/25/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 60a1110d-27dc-45d0-86e2-cddc72d072b2
description: "Learn how you can transform queries to provide more targeted SharePoint Server search results and how you can influence the way search results are ordered and displayed."
---

# Plan to transform queries and order results in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
You can add query transforms to a Web Part, add query rules that transform queries when certain conditions are met, and you can transform all queries directed to a result source to create a specialized search experience. 
  
SharePoint Server contains a number of predesigned search experiences, or search verticals, such as "Videos", "People" and "Conversations". These all contain predefined query transforms to optimize the search experience. You can also design your own search experiences that include your own query transforms, for instance for "Music" or "Pictures".
  
    
## Understanding query transforms and query variables
<a name="Query_vars_temp"> </a>

You can configure a query transform to replace certain properties of a query, such as the result source that the query will use to get search results from, or the sort order that it will use when it displays search results. 
  
A query transform can contain query variables. Query variables are placeholders for values, and when a query is actually run, the query variables are replaced with specific values.
  
The following table shows some examples of query variables.
  
| **A query transform replaces this query variable:** |                             **With this:**                              |
| :-------------------------------------------------- | :---------------------------------------------------------------------- |
| {User.Name}                                         | The name of the user who typed the query.                               |
| {Site.URL}                                          | The site where the user typed the query.                                |
| {Today}                                             | Today's date.                                                           |
| {SearchBoxQuery}                                    | The query that the user typed.                                          |
| {searchTerms}                                       | The query that the user typed, as changed by the most recent transform. |
   
See [Query variables in SharePoint Server](../technical-reference/query-variables.md) for an overview of all the available query variables. 
  
When a query transform replaces the incoming query, it uses a  *query template*  . A query template is a query that includes query variables, for example "{searchTerms} contenttype:picture". 
  
If you, for example, want to create a **Pictures** search vertical that only returns pictures in the search results, you could configure a query transform that uses the query template "{searchTerms} contenttype:picture" to add "contenttype:picture" to all queries. If a user then types the query "moon" in the Pictures vertical, the transform replaces the query variable "{searchTerms}" with "moon" and changes the query to "moon contenttype:picture". 
  
You can configure query transforms in three places:
  
- In a Web Part
    
- In a query rule
    
- In the result source
    
A user query is transformed first by the Web Part, then by any query rules that apply, and finally by the result source. When you configure a transform in a result source, you know that the transform changes will not be discarded or overridden, because the result source transforms the query last.
  
## Using the Query Builder to write and test query transforms
<a name="Trans_Query_Builder"> </a>

The Query Builder helps you write and test query transforms. To build queries you use Keyword Query Language (KQL), and you can also add query variables. You can test the query from within the Query Builder by setting temporary test values for the query variables, run the query and preview the search results. 
  
For more information about building search queries and for KQL syntax examples, see [Building search queries in SharePoint 2013](https://msdn.microsoft.com/en-us/library/office/jj163973.aspx) (MSDN). For an overview of all the available query variables, see [Query variables in SharePoint Server](../technical-reference/query-variables.md).
  
## Transforming queries for a Web Part
<a name="Trans_Web_Part"> </a>

You can transform queries in search Web Parts, such as the Content Search Web Part and the Search Results Web Part. Query transforms on a Web Part can be overridden by a query rule or by a query transform on the result source.
  
Query transforms in a Web Part are most often used to specify the result source that the queries should be sent to. For example, if you want to create a search experience that is customized for searching for pictures only, you would first create a result source with a query transform that returns only pictures. Then, you would create a Web Part that has a query transform that changes any query run in that Web Part to use your new **Pictures** result source instead of the default one. 
  
Another common use of query transforms in Web Parts is to make changes that are specific to one Web Part. For example, after creating the **Pictures** result source, you could add a Web Part with a query transform that uses the **Pictures** result source and in addition restrict the search results to only show recently modified pictures. 
  
## Transforming queries with query rules
<a name="Trans_Query_Rules"> </a>

You use query rules to try to capture the real intent behind a user query, and to return results that better match that intent. For each query rule you can specify under which conditions the rule should be applied, and also which actions the rule should trigger when it is applied. Most often you create query rules that apply to one site, but you can also create query rules that apply to a site collection or to all site collections in a Search service application. 
  
The first step in creating a query rule is to specify the **context** of the rule. The minimum requirement is that you specify which result source the query must target for the query rule to be applied. To create a rule that only applies to people search, for example, you would specify that the context is the result source **Local People Results**. Optionally, you can include a user segment or topic category in the context of a query rule. 
  
The next step is to specify the **conditions** that will cause the rule to be applied. If you want the query rule to apply to all queries, you can remove all conditions. 
  
The following table shows the available query rule conditions. 
  
|     **Query rule condition**     |                                                                                                                    **Description**                                                                                                                    |                                                                                                **Example**                                                                                                 |
| :------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Query matches keyword exactly    | Apply the query rule when the query exactly matches a word or phrase that you specify.                                                                                                                                                                | You specify "picture; pic" as the keywords. The query rule will apply when users type the query "picture" or "pic" in a search box. The rule will not apply if a user types "pictures" or "sunny picture". |
| Query contains action term       | Apply the query rule when the query contains a term in the form of a single word or phrase that indicates that the user is trying to do something. The term must be at the beginning or end of the query and might be a verb, a command, or a filter. | If a query contains the phrase "download", the user is probably not looking for items that contain the word "download", but is probably trying to download something.                                      |
| Query matches dictionary exactly | Apply the query rule when the query exactly matches a dictionary entry. This entry can be a term in the term store, or an entry in the people names dictionary.                                                                                       |                                                                                                                                                                                                            |
| Query more common in source      | Apply the query rule if the user's query is more commonly performed against a different result source than the current one. This condition uses an analysis of queries that users entered in the various result sources.                              | You can create a query rule that checks if a query is more commonly performed in a **Video** vertical. It will make video results more prominent if it is.                                                 |
| Result type commonly clicked     | Apply the query rule if the query often ends in users clicking results of a particular result type. When you create a new result type, you can indicate that these clicks should be recorded to be used in query rules.                               | If this is a query where people often click the result type "pictures", it may be appropriate to provide picture-related results in a result block.                                                        |
| Advanced query text match        | Apply the query rule if the query matches a regular expression. It also allows you to use variations of the keyword, dictionary and action term conditions explained earlier, but with more advanced control.                                         | To match all phone numbers that are in the format nnn-nnn-nnnn, you specify the regular expression "\(?(\d{3})\)?-?(\d{3})-(\d{4})".                                                                       |
   
The final step is to specify which **actions** the query rule should trigger when it is applied. Optionally, you can specify the start and end date for a query rule to be active. 
  
The following table shows the available query rule actions. 
  
|            **Query rule action**            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                        **Example**                                                                                                                         |
| :------------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Add promoted results                        | Show promoted results (known as Best Bets in earlier versions of SharePoint Server) above ranked results. Promoted results are best used when an item is not indexed or if it has a poor document summary. In other cases, consider changing the ranking of the results.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | For the query "sick leave", you can for instance add a link to a Human Resources site above all ranked results.                                                                                                                                            |
| Add result blocks                           | Add a block of results that contains a small subset of results that are related to a query in a specific way. You can promote a result block, or you can rank it with other search results. <br/> <br/> The query transform specified for the result block transforms a copy of the original query. <br/> <br/> You can also specify which display template should be used to display the result block.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | For a query that contains "Contoso sales report", a query rule could use a taxonomy dictionary to recognize "Contoso" as a customer, and then display a result block with results about "Contoso" from your customer relationship management (CRM) system. |
| Change ranked results by changing the query | Add a query transform that changes the original query. For example, the transform can promote or demote certain results. <br/> <br/> Changing the ranking of search results, such as boosting appropriate results by their site or URL, is a common alternative to adding promoted results. Changing ranked results by changing the query has the advantage that the results are security trimmed and refinable. Also, the search results will disappear if the document is no longer available. You can change the sorting order of the search results dynamically, based on several variables such as file extension or specific keywords. You can either promote or demote results, and you can specify how much the results should be promoted or demoted. <br/> <br/> For more information, see the section [Influence the ranking of search results with query rules](overview-of-search-result-ranking.md#Ranking_QueryRules) in [Overview of search result ranking in SharePoint Server](overview-of-search-result-ranking.md). <br/> <br/> | For a query that contains "download toolbox", a query rule could recognize the word "download" as an action term and boost search results that point to a particular download site on your intranet.                                                       |
   
## Transforming queries in result sources
<a name="Trans_Result_Sources"> </a>

For each result source, you can specify that all search results from that result source should be transformed in a specific way. For example, the pre-configured "Local Video Results" result source uses a query transform to return only video results from the local SharePoint index. 
  
SharePoint Server provides a number of preconfigured result sources with predefined query transforms out-of-the-box. You can also create new result sources and apply different query transforms on them. You can create more than one result source per search provider, and you can set different query transforms on each result source.
  
A user query is transformed first by the Web Part, then by any query rules that apply, and finally by the result source. When you configure a transform in a result source, you know that the transform changes will not be discarded or overridden, because the result source transforms the query last. You can re-use a result source query transform in Web Parts or result blocks, and you can create query rules or result types that are only applied to results from certain result sources.
  
## Changing the way results are shown by using result types
<a name="ResultTypesQuery"> </a>

With result types, you can conditionally change how search results are displayed. To customize the appearance of a group of related results, you can create a display template in HTML and associate the display template with a result type. You can create rules to specify when to show the display template, and you can prioritize these rules.
  
## How the search system processes a query
<a name="HowQueryProc"> </a>

When someone enters a query or clicks on an element that triggers a query, the search system sends the query to the query processing component. This component processes the query and then sends it to the appropriate search providers to retrieve results. A search provider can be a local search index or a remote source. After the results are collected from the search providers, the query processing component performs additional processing and then returns the results so that they can be displayed.
  
The search system processes a query by doing the following:
  
1. Applying any Web Part transforms.
    
2. Applying any query rules. A query rule action can either transform the original query or it can trigger a parallel query that is transformed for a result block.
    
3. Applying any query transforms on result sources.
    
4. Parsing the query and creating a query syntax tree for internal use.
    
5. Processing the query linguistically by performing word breaking, stemming, spelling correction, and synonym expansion.
    
6. Appending user-access information to the query. This specifies the user who is performing the query and the permissions that the user has.
    
7. Sending the query to the search index or another search provider.
    
8. Collecting and merging search results from all search providers and sending them back to the query processing component.
    
9. Evaluating the search results against result types. If a result matches a particular result type, the result is displayed by using the display template that you have specified for the result type. 
    
10. Applying additional security trimming, if appropriate.
    
## See also
<a name="HowQueryProc"> </a>

[Manage query rules in SharePoint Server](manage-query-rules.md)
  
[Configure result sources for search in SharePoint Server](configure-result-sources-for-search.md)
  
[Manage the Search Center in SharePoint Server](manage-the-search-center-in-sharepoint-server.md)

