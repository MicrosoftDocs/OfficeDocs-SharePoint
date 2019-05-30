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
 
description: "Learn how the classic and modern search experiences in SharePoint Online differ"
---

# Differences between the classic and modern search experiences in SharePoint Online

SharePoint Online has both a classic and a modern search experience. The modern search experience is Microsoft Search in SharePoint Online. Both search experiences use the same search index to find results.


As a search administrator, you can’t enable or disable either classic or modern search. Users get the classic search experience on publishing sites, classic team sites, and in the Search Center. Users get the modern search experience on the SharePoint start page, hub sites, communication sites, and modern team sites.


The most visible difference is that modern search is personal and the results you see are different from what other people see, even when you search for the same words. You'll see results before you start typing, and the results update as you type. [Learn more about the Microsoft Search experience](https://support.office.com/en-us/article/find-what-you-need-with-microsoft-search-d5ed5d11-9e5d-4f1d-b8b4-3d371fe0cb87)​.

​
Another difference is that search administrators can customize the *classic* search experience. See [Overview of search](overview-of-search.md) to learn about the main areas where you can customize classic search experience and make sure that search is performing the way you want.​

​
Unlike the classic search results page, the Microsoft Search results page isn’t built with web parts. You can’t customize the Microsoft Search results page or create additional search results pages.


Certain aspects of the classic search settings impact the modern search experience:

- The [search schema](manage-search-schema.md) determines how content is collected in and retrieved from the search index. Because both search experiences use the same search index to find search results, any changes you make to the search schema, apply to both experiences. The Microsoft Search experience doesn't support changing the sort order of results or building refiners based on metadata. Therefore, the following search schema settings don’t affect the Microsoft Search experience:
    - Sortable
    - Refinable 
    - Company name extraction
- The Microsoft Search experience only shows results from the default result source. If you change the default [result source](manage-result-sources.md), both search experiences are impacted.
- If you temporarily [remove a search result](remove-search-results.md), the result is removed in both search experiences.
- The classic search experience lets admins define promoted results, while the Microsoft Search experience uses bookmarks for the same. When you create a [promoted result](../SharePointServer/search/manage-query-rules.md) at the organization level, users can see it in both search experiences, but only on the All tab on the Microsoft Search results page and only when they search across all of SharePoint. For example, when users search from the Microsoft Search box on a hub site, they don't see any promoted results even if they are on the All tab. If you have a promoted result and a bookmark for the same content (same URL), the bookmark will override the promoted result in Microsoft Search.