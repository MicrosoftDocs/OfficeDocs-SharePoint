---
title: "Differences between the search experiences in SharePoint Server"
ms.reviewer: 
author: MikePlumleyMSFT
ms.author: mikeplum
manager: pamgreen
audience: Admin
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
description: "Learn about the differences between the search experiences in SharePoint Server"
---

# Differences between the search experiences in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]

In addition to the classic search experience, SharePoint Server 2019 comes with a modern search experience. Both search experiences use the same search index to find results. 

As a user, the most visual difference is that in modern search, you see results even before you start typing in the search box, and the results update as you type. [Learn about the modern search experience](https://support.office.com/en-us/article/what-s-new-in-search-in-sharepoint-server-2019-public-preview-3f56ab51-f10f-4a34-a8c6-bfe02f44896d)​.

As a search administrator, you can’t turn off neither classic nor modern search. Users get the classic search experience on publishing sites, classic team sites, and in the Search Center. Users get the modern search experience on the SharePoint home page, communication sites, and modern team sites. There are some differences between the search experiences from a search administrator's perspective.

Search administrators can customize the *classic* search experience, but only impact some aspects of the modern search experience. There aren't separate search settings for the modern search experience. Instead certain of the classic search settings **also** apply to the modern search experience: 

- The [search schema](manage-the-search-schema.md) determines how content is collected in and retrieved from the search index. Because both search experiences use the same search index to find search results, any changes you make to the search schema, apply to both experiences. The following search schema settings don’t affect the modern search experience:
    - Sortable
    - Refinable 
    - Company name extraction
    - Custom entity extraction
- The modern search experience only shows results from the default result source. If you change the default [result source](configure-result-sources-for-search.md), both search experiences are impacted.
- If you temporarily [remove a search result](/sharepoint/search/delete-items-from-the-search-index-or-from-search-results#remove-an-item-from-the-search-results), the result is removed in both search experiences.
- When you create a [promoted result](manage-query-rules.md) at the tenant level, users can see it in both search experiences. In the modern search experience, users only see promoted results when they’ve filtered to All result types (default filter) on the search results page and only when they search across all sites.

Unlike the classic search results page, the modern search results page isn’t built with web parts. You can’t customize the modern search results page or create additional search results pages.






