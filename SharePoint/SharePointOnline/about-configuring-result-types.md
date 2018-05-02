---
title: "About configuring result types"
ms.author: tlarsen
author: tklarsen
manager: arnek
ms.date: 5/25/2017
ms.audience: End User
ms.topic: article
f1_keywords:
- ConfigureResultTypes
- WSSEndUser_ConfigureResultTypes
ms.prod: office-online-server
localization_priority: Normal
search.appverid:
- WSU150
- SPS150
- SPO160
- SPS150
- OSU150
- SPB160
- GSS150
- GSA150
- BSA160
- OSU160
- GSP150
ms.assetid: 89c412f0-e248-41ef-ad43-5471ef4ed997
description: "Use result types with display templates to control the ways in which search results appear and behave in SharePoint 2013."
---

# About configuring result types

You use display templates to control the ways in which search results appear and behave in search-related Web Parts. There are many pre-configured display templates, and you can create other display templates. You use a result type to specify a display template that the search system should use for a particular type of search result. This might be a type of search result that you want users to be able to distinguish easily from other types of search results, and for which you want to provide a particular appearance and behavior on the search results page. There are also many pre-configured result types, and you can create other result types. You can configure result types at the site collection level and at the site level.
  
Each result type specifies one or more conditions to compare search results against, such as the type or the result source of the search result, and an action to take if a search result meets those conditions. The action specifies the display template to use for the search result. For example, a pre-configured result type named **Person** specifies that if a search result is from the result source **Local People Results**, then use the **People Item** display template for that search result. The People Item display template shows information in the hover panel such as documents authored by the person and enables the user to go directly to those documents. 
  
To create a result type, do one of the following on the Manage Result Types page:
  
- Click **New Result Type**.
    
- In the list of existing result types, click the name of a result type, such as **Person**, and then click **Copy** so that you can modify the copy to create a new result type. 
    
For more information, see:
  
- SharePoint Server 2016: [Customize search result types in SharePoint 2016](https://technet.microsoft.com/en-us/library/dn135239%28v=office.16%29.aspx) (TechNet) 
    
- SharePoint Server 2013: [Customize search result types in SharePoint 2013](https://technet.microsoft.com/en-us/library/dn135239.aspx) (TechNet) 
    
- SharePoint Online: [Manage result types](manage-result-types.md) (Office.com) 
    
[You use display templates to control the ways in which search results appear and behave in search-related Web Parts. There are many pre-configured display templates, and you can create other display templates. You use a result type to specify a display template that the search system should use for a particular type of search result. This might be a type of search result that you want users to be able to distinguish easily from other types of search results, and for which you want to provide a particular appearance and behavior on the search results page. There are also many pre-configured result types, and you can create other result types. You can configure result types at the site collection level and at the site level.Each result type specifies one or more conditions to compare search results against, such as the type or the result source of the search result, and an action to take if a search result meets those conditions. The action specifies the display template to use for the search result. For example, a pre-configured result type named Person specifies that if a search result is from the result source Local People Results, then use the People Item display template for that search result. The People Item display template shows information in the hover panel such as documents authored by the person and enables the user to go directly to those documents.To create a result type, do one of the following on the Manage Result Types page:Click New Result Type.In the list of existing result types, click the name of a result type, such as Person, and then click Copy so that you can modify the copy to create a new result type.For more information, see:SharePoint Server 2016: Customize search result types in SharePoint 2016https://technet.microsoft.com/en-us/library/dn135239(v=office.16).aspx (TechNet)SharePoint Server 2013: Customize search result types in SharePoint 2013https://technet.microsoft.com/en-us/library/dn135239.aspx (TechNet)SharePoint Online: Manage result types (Office.com)Top of Page](about-configuring-result-types.md#__top)
  

