---
title: "Differences between the classic and modern search experiences in SharePoint Online"
author: tklarsen
ms.author: tlarsen
manager: arnek
audience: Admin
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
search.appverid:
- SPO160
- MET150
 
description: "Learn about the differences between the classic and modersn search experiences"
---

# Differences between the classic and modern search experiences in SharePoint Online

SharePoint Online has both a classic and a modern search experience. The most visible difference is that *modern* search is personal and the results you see are different from what other people see, even when you search for the same words. You'll see results before you start typing, and the results update as you type. [Learn more about the modern search experience](https://support.office.com/en-us/article/What-s-new-in-search-in-Office-365-b81ab573-ec9c-4aa9-a369-b3c630f878a7)​.

​
Another important difference is that search administrators can customize the *classic* search experience, but **not** the modern. See [Overview of search](overview-of-search.md) to learn about the main areas where you can customize and impact the search experience and make sure that search is performing the way you want.​
​
Both search experiences use the same search index to find search results, and some search settings can impact both experiences:​


- When you create a [promoted result](../SharePointServer/search/manage-query-rules.md) at the tenant level, users can see it in both search experiences. In the modern search experience, users only see promoted results on the All tab on the search results page and only when they search across all of SharePoint.
- The modern search experience only shows results from the default result source. If you change the default [result source](manage-result-sources.md), both search experiences are impacted.
- If you temporarily [remove a search result](manage-result-sources.md), the result is removed in both search experiences.
- The [search schema](manage-search-schema.md) determines how content is collected in and retrieved from the search index. Because both search experiences use the same search index to find search results, any changes you make to the search schema, might affect both experiences. The following search schema settings don’t affect the modern search experience:
    - Sortable
    - Refinable 
    - Company name extraction



