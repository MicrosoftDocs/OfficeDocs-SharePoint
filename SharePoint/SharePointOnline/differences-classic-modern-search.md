---
title: "Differences between the classic and modern search experiences in SharePoint"
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
 
description: "Learn how the classic and modern search experiences in SharePoint differ"
---

# Differences between the classic and modern search experiences in SharePoint

SharePoint has both a classic and a modern search experience. Microsoft search in SharePoint is the modern search experience. Both search experiences use the same search index to find results.

As a search admin, you can’t enable or disable either search experience, both are enabled by default. Users get the classic search experience on publishing sites, classic team sites, and in the Search Center. Users get the Microsoft search experience on the SharePoint start page, hub sites, communication sites, and modern team sites. [Learn about classic and modern sites](https://support.office.com/article/5725c103-505d-4a6e-9350-300d3ec7d73f)

The most visible difference is that the Microsoft search box is placed at the top of the SharePoint, in the header bar. Another difference is that Microsoft search is personal. The results you see are different from what other people see, even when you search for the same words. You'll see results before you start typing in the search box, based on your previous activity and trending content in Office 365, and the results update as you type. [Learn more about the Microsoft search experience for users](https://support.office.com/article/d5ed5d11-9e5d-4f1d-b8b4-3d371fe0cb87)​.

​Search admin can customize the *classic* search experience, but not the Microsoft search experience. As a search admin you can *tailor* Microsoft search to your organization so it's easy for your users to find often needed content in your organization.

You use the SharePoint admin center to manage classic search and the Microsoft 365 admin center to manage Microsoft search. Certain aspects of the classic search settings also impact the modern search experience:

- The [search schema](manage-search-schema.md) determines how content is collected in and retrieved from the search index. Because both search experiences use the same search index to find search results, any changes you make to the search schema, apply to both experiences. The Microsoft search experience doesn't support changing the sort order of results or building refiners based on metadata. Therefore, the following search schema settings don’t affect the Microsoft search experience:
    - Sortable
    - Refinable 
    - Company name extraction (to be deprecated as of November 15th, 2019)
- The modern search experience only shows results from the default result source. If you change the default [result source](manage-result-sources.md), both search experiences are impacted.
- If you temporarily [remove a search result](remove-search-results.md), the result is removed in both search experiences.
- The classic search experience lets admins define **promoted results** to help users find important content, while the Microsoft search experience uses **bookmarks** to achieve the same. When you [create a promoted result](../SharePointServer/search/manage-query-rules.md) at the organization level, users might also see it on the **All** tab on the Microsoft search results page if they searched across the whole organization. For example, when users search from the search box on a hub site, they're only searching in the sites associated with the hub and therefore they don't see any promoted results even if they are on the **All** tab. But when users search from the SharePoint start page, they might see promoted results on the **All** tab. If you have defined both a promoted result and a bookmark for the same content (same URL), only the bookmark will appear on the **All** tab.
