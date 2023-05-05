---
ms.date: 08/17/2018
title: "Difference between classic & modern search experiences - SharePoint"
ms.reviewer: 
ms.author: serdars
author: SerdarSoysal
manager: serdars
recommendations: true
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.collection: M365-collaboration
ms.localizationpriority: medium
search.appverid:
- SPO160
- MET150
ms.custom:
- seo-marvel-apr2020
- admindeeplinkSPO
description: "This article provides an overview of the difference between the classic and modern search experiences in Microsoft SharePoint."
---

# Differences between the classic and modern search experiences in SharePoint

SharePoint in Microsoft 365 has both a classic and a modern search experience. Microsoft Search in SharePoint is the modern search experience. Both search experiences use the same search index to find results.

As a search admin, you can’t enable or disable either search experience, both are enabled by default. Users get the classic search experience on publishing sites, classic team sites, and in the Search Center. Users get the Microsoft Search experience on the SharePoint start page, hub sites, communication sites, and modern team sites. [Learn about classic and modern sites](https://support.office.com/article/5725c103-505d-4a6e-9350-300d3ec7d73f)

The most visible difference is that the Microsoft Search box is placed at the top of the SharePoint, in the header bar. Another difference is that Microsoft Search is personal. The results you see are different from what other people see, even when you search for the same words. You'll see results before you start typing in the search box, based on your previous activity and trending content in Microsoft 365, and the results update as you type. [Learn more about the Microsoft Search experience for users](https://support.office.com/article/d5ed5d11-9e5d-4f1d-b8b4-3d371fe0cb87).

Search admin can customize the *classic* search experience, but not the Microsoft Search experience. As a search admin you can *tailor* Microsoft Search to your organization so it's easy for your users to find often needed content in your organization.

For example, if your organization has Microsoft Search fully deployed, custom result sources at site collection or tenant level won't affect the search result. The search admin can use Microsoft search verticals instead. To learn more, see [Manage search verticals](/microsoftsearch/manage-verticals).

You use the <a href="https://go.microsoft.com/fwlink/?linkid=2185219" target="_blank">SharePoint admin center</a> to manage classic search and the Microsoft 365 admin center to manage Microsoft Search. Certain aspects of the classic search settings also impact the modern search experience:

- The [search schema](manage-search-schema.md) determines how content is collected in and retrieved from the search index. Because both search experiences use the same search index to find search results, any changes you make to the search schema, apply to both experiences. The Microsoft Search experience doesn't support changing the sort order of results or building refiners based on metadata. Therefore, the following search schema settings don’t affect the Microsoft Search experience:
  - Sortable
  - Refinable
  - Company name extraction (deprecated since November 15, 2019)

- In environments where vertical configuration is available the modern search experience only shows results from the standard result source (Local SharePoint Results). To learn more, see [Manage search verticals](/microsoftsearch/manage-verticals).
- In environments where vertical configuration is not available the modern search experience only shows results from the default result source. If you change the default [result source](manage-result-sources.md), both modern and classic search experiences are impacted.
- Depending on the search scenario, some Microsoft Search features might not work if the [classic global Search Center URL](./specify-default-search-center.md) is not set to point to the URL of the default classic Search Center. Depending on your tenant, this URL is "yourcompanyname.sharepoint.com/search" or "yourcompanyname.sharepoint.com/search/pages". Furthermore, ensure that the Search Center site collection exists and that all users have read access to it.
- If you temporarily [remove a search result](remove-search-results.md), the result is removed in both search experiences.
- The classic search experience lets admins define **promoted results** to help users find important content, while the Microsoft Search experience uses **bookmarks** to achieve the same. When you [create a promoted result](../SharePointServer/search/manage-query-rules.md) at the organization level, users might also see it on the **All** tab on the Microsoft Search results page if they searched across the whole organization. For example, when users search from the search box on a hub site, they're only searching in the sites associated with the hub and therefore they don't see any promoted results even if they are on the **All** tab. But when users search from the SharePoint start page, they might see promoted results on the **All** tab. If you have defined both a promoted result and a bookmark for the same content (same URL), only the bookmark will appear on the **All** tab.

