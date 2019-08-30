---
title: "Differences between the classic and modern search experiences in SharePoint Online"
ms.reviewer: 
author: MikePlumleyMSFT
ms.author: mikeplum
manager: pamgreen
audience: Admin
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
search.appverid:
- SPO160
- MET150
 
description: "Learn how the classic and modern search experiences differ"
---

# Differences between the classic and modern search experiences in SharePoint Online

SharePoint Online has both a classic and a modern search experience. Both search experiences use the same search index to find results. 

As a search administrator, you can’t enable or disable either classic or modern search. Users get the classic search experience on publishing sites, classic team sites, and in the Search Center. Users get the modern search experience on the SharePoint start page, hub sites, communication sites, and modern team sites.

The most visible difference is that modern search is personal and the results you see are different from what other people see, even when you search for the same words. You'll see results before you start typing, and the results update as you type. [Learn more about the modern search experience](https://support.office.com/article/b81ab573-ec9c-4aa9-a369-b3c630f878a7)​.

​
Another difference is that search administrators can customize the *classic* search experience, but only impact some aspects of the modern search experience. See [Overview of search](overview-of-search.md) to learn about the main areas where you can customize and impact the search experience and make sure that search is performing the way you want.​
​

Unlike the classic search results page, the modern search results page isn’t built with web parts. You can’t customize the modern search results page or create additional search results pages.

There aren't separate search settings for the modern search experience. Instead, certain aspects of the classic search settings **also** apply to the modern search experience: 

- The [search schema](manage-search-schema.md) determines how content is collected in and retrieved from the search index. Because both search experiences use the same search index to find search results, any changes you make to the search schema, apply to both experiences. The modern search experience doesn't support changing the sort order of results or building refiners based on metadata. Therefore, the following search schema settings don’t affect the modern search experience:
    - Sortable
    - Refinable 
    - Company name extraction
- The modern search experience only shows results from the default result source. If you change the default [result source](manage-result-sources.md), both search experiences are impacted.
- If you temporarily [remove a search result](remove-search-results.md), the result is removed in both search experiences.
- When you create a [promoted result](../SharePointServer/search/manage-query-rules.md) at the organization level, users can see it in both search experiences. In the modern search experience, users only see promoted results on the All tab on the search results page and only when they search across all of SharePoint. For example, when users search from the search box on a hub site, they don't see any promoted results even if they are on the All tab.




