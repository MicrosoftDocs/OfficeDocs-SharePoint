---
title: "Understanding query rules"
ms.author: tlarsen
author: tklarsen
manager: arnek
ms.date: 5/25/2017
ms.audience: End User
ms.topic: reference
f1_keywords:
- QueryRulesConceptualOverview
- WSSEndUser_QueryRulesConceptualOverview
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
ms.assetid: 8ca2588d-9dc7-45aa-90a4-428d4d695d07
description: "Help searches in SharePoint 2013 respond to the intent of your users by creating query rules."
---

# Understanding query rules

Without any custom code, you can help searches respond to the intent of your users by creating query rules. In a query rule, you specify conditions and correlated actions. When a query meets the conditions, the search system performs the actions to improve the relevance of the search results.
  
For example, you might specify a condition that checks whether the query matches a term in a SharePoint term set, or another condition that checks whether the query is frequently performed on a particular search vertical in your search system, such as Videos. 
  
A query rule can specify the following three types of actions:
  
- Add Promoted Results (formerly called Best Bets) that appear above ranked results. For example, for the query "sick leave", a query rule could specify a particular Promoted Result, such as a link to a site that has a statement of company policy regarding time off work.
    
- Add one or more groups of results, called result blocks. A result block contains a small subset of results that are related to a query in a particular way. Like individual results, you can promote a result block or rank it with other search results. For example, for a query that contains "Fabrikam sales report", a query rule might use a taxonomy dictionary to recognize "Fabrikam" as a customer, and then display a result block with pertinent results about Fabrikam from your customer relationship management (CRM) system.
    
- Change the ranking of results. For example, for a query that contains "download toolbox", a query rule could recognize the word "download" as an action term and boost search results that point to a particular download site on your intranet.
    
For more information, see:
  
- SharePoint Online: [Manage query rules](manage-query-rules.md) (Office.com) 
    
- SharePoint Server 2016: [Manage query rules in SharePoint Server 2016](https://technet.microsoft.com/en-us/library/jj871676%28v=office.16%29.aspx) (TechNet) 
    
- SharePoint Server 2013: [Manage query rules in SharePoint Server 2013](https://technet.microsoft.com/en-us/library/jj871676.aspx) (TechNet) 
    
[Without any custom code, you can help searches respond to the intent of your users by creating query rules. In a query rule, you specify conditions and correlated actions. When a query meets the conditions, the search system performs the actions to improve the relevance of the search results.For example, you might specify a condition that checks whether the query matches a term in a SharePoint term set, or another condition that checks whether the query is frequently performed on a particular search vertical in your search system, such as Videos. A query rule can specify the following three types of actions:Add Promoted Results (formerly called Best Bets) that appear above ranked results. For example, for the query "sick leave", a query rule could specify a particular Promoted Result, such as a link to a site that has a statement of company policy regarding time off work.Add one or more groups of results, called result blocks. A result block contains a small subset of results that are related to a query in a particular way. Like individual results, you can promote a result block or rank it with other search results. For example, for a query that contains "Fabrikam sales report", a query rule might use a taxonomy dictionary to recognize "Fabrikam" as a customer, and then display a result block with pertinent results about Fabrikam from your customer relationship management (CRM) system.Change the ranking of results. For example, for a query that contains "download toolbox", a query rule could recognize the word "download" as an action term and boost search results that point to a particular download site on your intranet.For more information, see:SharePoint Online: Manage query rules (Office.com)SharePoint Server 2016: Manage query rules in SharePoint Server 2016https://technet.microsoft.com/en-us/library/jj871676(v=office.16).aspx (TechNet)SharePoint Server 2013: Manage query rules in SharePoint Server 2013https://technet.microsoft.com/en-us/library/jj871676.aspx (TechNet)Top of Page](understanding-query-rules.md#__top)
  

