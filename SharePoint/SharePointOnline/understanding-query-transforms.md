---
title: "Understanding query transforms"
ms.author: tlarsen
author: tklarsen
manager: arnek
ms.date: 12/30/2016
ms.audience: End User
ms.topic: reference
f1_keywords:
- QueryTemplatesConceptualOverview
- WSSEndUser_QueryTemplatesConceptualOverview
ms.prod: office-online-server
localization_priority: Normal
search.appverid:
- WSU150
- SPS150
- SPS150
- SPO160
- SPS150
- OSU150
- SPB160
- GSS150
- GSA150
- OSI150
- BSA160
- OSU160
- GSP150
ms.assetid: b31631a5-0c1f-436e-8061-fd807bb96ae1
description: "Learn about changing search queries in SharePoint 2013 by using query transforms to provide search results that are in line with what users expect."
---

# Understanding query transforms

To provide search results that are appropriate for a user query, sometimes you have to change the query. For example, suppose you create a search vertical for Pictures. When someone types a query in the Pictures vertical, you have to change the query so that it returns only search results that are Pictures.
  
To change a query, you use the Query Builder to configure a query transform. You can configure a query transform to replace properties of a query, such as the [result source](understanding-result-sources.md) that the query will use to get search results, or the sort order that it will use when it displays search results. The transform also replaces the text of the query by using a query template that you can configure. The query template is the text that will replace the query text, and the template can contain query variables. 
  
A query variable is a placeholder for a value. When a transform replaces the text of a query with its query template, it also replaces the query variables in the template with specific values. 
  
A transform replaces contextual query variables with values pertaining to the query context. The following table shows some examples of contextual query variables.
  
|**A transform replaces this contextual query variable**|**With this**|
|:-----|:-----|
|{User.Name}  <br/> |Name of user who typed the query  <br/> |
|{Site.URL}  <br/> |Site where user typed the value  <br/> |
|{Today}  <br/> |Today's date  <br/> |
   
A transform replaces bound query variables with certain text that is in the user's query. The following table shows some examples of bound query variables. 
  
|**A transform replaces this bound query variable**|**With this**|
|:-----|:-----|
|{searchBoxQuery}  <br/> |The query that the user typed  <br/> |
|{searchTerms}  <br/> |The query that the user typed, as changed by the most recent transform  <br/> |
   
You can use a bound query variable when you add a restriction to a query, such as when you restrict a query to a particular content type. For example, for a Pictures search vertical, you could configure a query transform that adds "contenttype:picture" to the query text by using the query template "{searchTerms} contenttype:picture". If a user types the query "moon" in that vertical, the transform replaces "{searchTerms}" with "moon". Thus, the query transform changes the query to "moon contenttype:picture".
  
You can configure query transforms in three places:
  
- In a Web Part, such as a Search Results Web Part. Configure a transform in a Web Part when you do not need to make the same changes to queries elsewhere.
    
- In a [query rule](understanding-query-rules.md), which specifies that certain actions will be performed only if certain conditions are satisfied. Two of these actions use a transform to change the query:
    
  - Add a result block on the search results page. This action creates a copy of the query, and its transform changes only the copy.
    
  - Change the ranked results. This action changes the query that the user typed.
    
- In the result source that the query uses to get search results. 
    
A user query is transformed by the Web Part, then by any query rules that apply, and finally by the result source. Therefore, when you configure a transform in a result source, you know that the transform changes will not be discarded or overridden, because the result source transforms the query last. For example, to make sure that a Pictures search vertical returns only pictures, you would configure the appropriate transform in a result source, and then configure the Web Part in the search vertical to use that result source.
  
For more information, see [Overview of query processing](https://go.microsoft.com/fwlink/?linkid=261560) on TechNet. 
  
[To provide search results that are appropriate for a user query, sometimes you have to change the query. For example, suppose you create a search vertical for Pictures. When someone types a query in the Pictures vertical, you have to change the query so that it returns only search results that are Pictures.To change a query, you use the Query Builder to configure a query transform. You can configure a query transform to replace properties of a query, such as the result source that the query will use to get search results, or the sort order that it will use when it displays search results. The transform also replaces the text of the query by using a query template that you can configure. The query template is the text that will replace the query text, and the template can contain query variables. A query variable is a placeholder for a value. When a transform replaces the text of a query with its query template, it also replaces the query variables in the template with specific values. A transform replaces contextual query variables with values pertaining to the query context. The following table shows some examples of contextual query variables.A transform replaces this contextual query variableWith this{User.Name}Name of user who typed the query{Site.URL}Site where user typed the value{Today}Today's dateA transform replaces bound query variables with certain text that is in the user's query. The following table shows some examples of bound query variables. A transform replaces this bound query variableWith this{searchBoxQuery}The query that the user typed{searchTerms}The query that the user typed, as changed by the most recent transform You can use a bound query variable when you add a restriction to a query, such as when you restrict a query to a particular content type. For example, for a Pictures search vertical, you could configure a query transform that adds "contenttype:picture" to the query text by using the query template "{searchTerms} contenttype:picture". If a user types the query "moon" in that vertical, the transform replaces "{searchTerms}" with "moon". Thus, the query transform changes the query to "moon contenttype:picture".You can configure query transforms in three places:In a Web Part, such as a Search Results Web Part. Configure a transform in a Web Part when you do not need to make the same changes to queries elsewhere.In a query rule, which specifies that certain actions will be performed only if certain conditions are satisfied. Two of these actions use a transform to change the query:Add a result block on the search results page. This action creates a copy of the query, and its transform changes only the copy.Change the ranked results. This action changes the query that the user typed.In the result source that the query uses to get search results. A user query is transformed by the Web Part, then by any query rules that apply, and finally by the result source. Therefore, when you configure a transform in a result source, you know that the transform changes will not be discarded or overridden, because the result source transforms the query last. For example, to make sure that a Pictures search vertical returns only pictures, you would configure the appropriate transform in a result source, and then configure the Web Part in the search vertical to use that result source.For more information, see Overview of query processinghttps://go.microsoft.com/fwlink/?linkid=261560 on TechNet.Top of Page](understanding-query-transforms.md#__top)
  

