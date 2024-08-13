---
ms.date: 07/11/2018
title: "SharePoint classic search administration overview"
ms.reviewer: 
ms.author: ruihu
author: maggierui
manager: jtremper
recommendations: true
audience: Admin
f1.keywords:
- NOCSH
ms.topic: overview
ms.service: sharepoint-online
ms.collection: M365-collaboration
ms.localizationpriority: medium
ms.custom: admindeeplinkSPO
search.appverid:
- SPO160
- MET150
ms.assetid: 21ea5d29-6cb2-4e40-9cc8-77c05d94beb5
description: "Use the search page in the classic SharePoint admin center to customize the classic search experience for users."
---

# SharePoint classic search administration overview

As a [SharePoint Administrator](/sharepoint/sharepoint-admin-role) and [above](/microsoft-365/admin/add-users/about-admin-roles) in Microsoft 365, you can customize and impact the search experiences for your users. You can define searchable managed properties in the search schema, identify high-quality pages to improve relevance, manage query rules and result sources, and remove individual results. You can also evaluate any changes by viewing reports about usage and search.
  
The changes you make from the search administration page are valid for the whole tenant, but you can also customize search on site collection level and on site level.

You can customize and tailor the classic search experience more than Microsoft Search in SharePoint. Some classic search settings can impact both experiences, [learn how to avoid impacting Microsoft Search](differences-classic-modern-search.md).
  
## How to get to the classic search administration page
<a name="__top"> </a>

1. Go to <a href="https://go.microsoft.com/fwlink/?linkid=2185077" target="_blank">**More features** in the SharePoint admin center</a>, and sign in with an account that has [admin permissions](./sharepoint-admin-role.md) for your organization.

   > [!NOTE]
   > If you have Office 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the More features page.

2. Under **Search**, select **Open**.
    
## What do you want to do?
<a name="__top"> </a>

| Choose this option: | To do this: |
|:-----|:-----|
|[Manage the search schema](manage-search-schema.md) |Learn how to create a customized search experience by changing the search schema. In the search schema, you can view, create, or change managed properties, and map crawled properties to managed properties. |
|[Manage search dictionaries](manage-search-dictionaries.md) |Learn how to manage search dictionaries for classic search. You can use search dictionaries to include or exclude company names to be extracted from the content of your indexed documents, or you can include or exclude words for query spelling correction. |
|[Manage authoritative pages](manage-authoritative-pages.md) |Influence the pages or documents that should appear at the top of the search results by identifying high-quality pages, also known as authoritative pages, for the classic search experience. |
|[Manage query suggestion settings](manage-query-suggestions.md) |Learn how to add phrases that you want the system to suggest to users as they search for an item using classic search, and how to add phrases that you don't want the system to suggest to users. Also, learn how to turn this feature on or off. |
|[Manage result sources](manage-result-sources.md) |Result sources limit searches to certain content or to a subset of search results. Learn how to create your own result sources, or change the predefined result sources. |
|[Manage query rules](manage-query-rules.md) |Improve search results in the classic search experience by creating and managing query rules. Query rules can help searches respond to the intent of users. |
|[Manage query client types](query-throttling.md) |Learn how query client types decide in which order queries are performed in the classic search experience. |
|[Remove search results](remove-search-results.md) |Learn how you can temporarily remove items from the search results with immediate effect. These items can be documents, pages, or sites that you don't want users to see when they search. |
|[View usage and search reports](view-search-usage-reports-modern-sites.md) |View usage reports and search reports and see how often your users search, what their top queries are, and which queries they're having trouble getting answers for. |
|[Manage Search Center settings](specify-default-search-center.md) |Choose where searches in the classic search experience should go by specifying the URL of your Search Center. |
|[Import and export customized search configuration settings](export-and-import-search-settings.md) |Learn how to export and import customized search configuration settings between tenants, site collections, and sites. |
|[Manage crawl log permissions](set-crawl-log-permissions.md) |Learn how to grant users or groups read access to crawl log information for the tenant. A typical use case is in eDiscovery, where users may need to check whether crawled content was in fact added to the search index. |
   
> [!NOTE]
> Thesaurus isn't available in SharePoint in Microsoft 365. 
  
## See also
<a name="__top"> </a>

[Search limits for SharePoint](search-limits.md)

