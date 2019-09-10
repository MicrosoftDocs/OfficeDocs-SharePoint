---
title: "SharePoint Online search administration overview"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
audience: Admin
ms.topic: overview
ms.service: sharepoint-online
localization_priority: Normal
search.appverid:
- SPO160
- MET150
ms.assetid: 21ea5d29-6cb2-4e40-9cc8-77c05d94beb5
description: "Use the SharePoint Online search administration page to customize the classic search experience for users. Define searchable managed properties in the search schema, identify high-quality pages to improve relevance, manage query rules and result sources, and remove individual results. You can also evaluate any changes by viewing reports about usage and search."
---

# SharePoint Online search administration overview

SharePoint Online has both a classic and a modern search experience. As a global or SharePoint admin in Office 365, you can customize and impact the search experiences for users.  [Learn about the differences between the classic and modern search experiences](differences-classic-modern-search.md). You can define searchable managed properties in the search schema, identify high-quality pages to improve relevance, manage query rules and result sources, and remove individual results. You can also evaluate any changes by viewing reports about usage and search.
  
The changes you make from the search administration page are valid for the whole tenant, but you can also customize search on site collection level and on site level.
  
## How to get to the search administration page
<a name="__top"> </a>

1. Sign in to https://admin.microsoft.com as a global or SharePoint admin. (If you see a message that you don't have permission to access the page, you don't have Office 365 administrator permissions in your organization.)
    
    > [!NOTE]
    > If you have Office 365 Germany, sign in at https://portal.office.de. If you have Office 365 operated by 21Vianet (China), sign in at https://login.partner.microsoftonline.cn/. Then select the Admin tile to open the admin center.  

2. If the classic SharePoint admin center appears, select **Open it now** at the top of the page to open the new SharePoint admin center. 

3. In the left pane of the new SharePoint admin center, select **Classic features**. 

4. Under **Search**, select **Open**.

    
## What do you want to do?
<a name="__top"> </a>

|**Choose this option:**|**To do this:**|
|:-----|:-----|
|[Manage the search schema](manage-search-schema.md) <br/> |Learn how to create a customized search experience by changing the search schema. In the search schema, you can view, create, or change managed properties, and map crawled properties to managed properties.  <br/> |
|[Manage search dictionaries](manage-search-dictionaries.md) <br/> |Learn how to manage search dictionaries. You can use search dictionaries to include or exclude company names to be extracted from the content of your indexed documents, or you can include or exclude words for query spelling correction.  <br/> |
|[Manage authoritative pages](manage-authoritative-pages.md) <br/> |Influence the pages or documents that should appear at the top of your list of search results by identifying high-quality pages, also known as authoritative pages.  <br/> |
|[Manage query suggestion settings](manage-query-suggestions.md) <br/> |Learn how to add phrases that you want the system to suggest to users as they search for an item, and how to add phrases that you don't want the system to suggest to users. Also, learn how to turn this feature on or off.  <br/> |
|[Manage result sources](manage-result-sources.md) <br/> |Result sources limit searches to certain content or to a subset of search results. Learn how to create your own result sources, or change the predefined result sources.  <br/> |
|[Manage query rules](manage-query-rules.md) <br/> |Improve search results by creating and managing query rules. Query rules can help searches respond to the intent of users.  <br/> |
|[Manage query client types](query-throttling.md) <br/> |Learn how query client types decide in which order queries are performed.  <br/> |
|[Remove search results](remove-search-results.md) <br/> |Learn how you can temporarily remove items from the search results with immediate effect. These items can be documents, pages, or sites that you don't want users to see when they search.  <br/> |
|[View usage and search reports](view-search-usage-reports.md) <br/> |View usage reports and search reports and see how often your users search, what their top queries are, and which queries they're having trouble getting answers for.  <br/> |
|[Manage Search Center settings](specify-default-search-center.md) <br/> |Choose where searches should go by specifying the URL of your Search Center.  <br/> |
|[Import and export customized search configuration settings](export-and-import-search-settings.md) <br/> |Learn how to export and import customized search configuration settings between tenants, site collections, and sites.  <br/> |
|[Manage crawl log permissions](set-crawl-log-permissions.md) <br/> |Learn how to grant users or groups read access to crawl log information for the tenant. A typical use case is in eDiscovery, where users may need to check whether crawled content was in fact added to the search index.  <br/> |
   
> [!NOTE]
> Thesaurus isn't available in SharePoint Online. 
  
## See also
<a name="__top"> </a>

[Search limits for SharePoint Online](search-limits.md)

