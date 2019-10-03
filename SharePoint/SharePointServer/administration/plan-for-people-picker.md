---
title: "Plan for People Picker in SharePoint"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 8/1/2017
audience: ITPro
ms.topic: interactive-tutorial
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: 2093c146-c880-48c6-9526-24cdf80969ba
description: "Learn how to plan for the People Picker web control in SharePoint Server."
---

# Plan for People Picker in SharePoint

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
You use the People Picker control to find and select people, groups, and claims when a site, list, or library owner assigns permissions in SharePoint Server. This article describes how to plan for People Picker. For information about how to configure People Picker, see [Configure People Picker in SharePoint Server](/previous-versions/office/sharepoint-server-2010/gg602075(v=office.14)).
  
Before reading this article, you should understand the concepts described in the following articles: 
  
- [Plan for user authentication methods in SharePoint Server](../security-for-sharepoint-server/plan-user-authentication.md)
    
- [People Picker and claims providers overview](people-picker-and-claims-providers-overview.md)
    
- [The Role of Claims](https://go.microsoft.com/fwlink/p/?LinkID=208326)
    
- [SharePoint Claims-Based Identity](https://go.microsoft.com/fwlink/p/?LinkID=196647)
    
    
## People Picker and claims providers
<a name="claimproviders"> </a>

A claims provider lists, resolves, searches, and determines the "friendly" display of users, groups, and claims in the People Picker when claims-based authentication is used. If your web application uses claims-based authentication, you must decide whether to use one of the default claims providers or create a custom claims provider that will meet the business needs of your organization.
  
For more information about how claims providers are related to the People Picker control, see [Plan for custom claims providers for People Picker in SharePoint](plan-for-custom-claims-providers-for-people-picker.md).
  
## Using People Picker with multiple forests or domains
<a name="forests"> </a>

By default, People Picker will return users, groups, and claims from the domain on which SharePoint Server is installed, only. If you want People Picker to return query results from more than one forest or domain, you must configure People Picker to use an encrypted account and password even if you have a one- or two-way trust between the forests or domains. For more information about trusts, see [Managing Trusts](https://go.microsoft.com/fwlink/p/?LinkId=207573).
  
To configure People Picker for a one-way trust, see [Configure People Picker in SharePoint Server](/previous-versions/office/sharepoint-server-2010/gg602075(v=office.14)).
  
## Planning considerations for People Picker
<a name="planning"> </a>

Planning for People Picker largely depends on what forests and domains that you want users to be able to query, and what users, groups, and claims you want to display in query results. As you plan for the forests and domains that you want users to query, consider the following questions:
  
- Do users have to query across a forest or a domain?
    
- What is the domain name system (DNS) name for each forest or domain that you want users to query?
    
- Will your forest or domain have a one-way or two-way trust with other forests or domains?
    
- If you are using a one-way trust, what credentials will be used to query the other farms or domains?
    
Planning for the users, groups, and claims you want to display in the query results in People Picker will help you determine how to configure People Picker to return and display results from claims providers. As you plan for the users, groups, and claims you want to display in query results, consider the following questions:
  
- Are there certain Lightweight Directory Access Protocol (LDAP) filters that you want to apply to query results?
    
- Do you want to restrict the query results to users, groups, or claims in a specific site collection?
    
- Do you want to restrict the query results to users, groups, or claims in a certain Active Directory organizational unit (OU)?
    
## See also
<a name="planning"> </a>

#### Concepts

[Plan for user authentication methods in SharePoint Server](../security-for-sharepoint-server/plan-user-authentication.md)
  
[People Picker and claims providers overview](people-picker-and-claims-providers-overview.md)
  
[Plan for custom claims providers for People Picker in SharePoint](plan-for-custom-claims-providers-for-people-picker.md)
#### Other Resources

[Configure People Picker in SharePoint Server](/previous-versions/office/sharepoint-server-2010/gg602075(v=office.14))

