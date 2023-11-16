---
title: "Overview of crawled and managed properties in SharePoint Online"
ms.reviewer: misvenso
ms.author: jhendr
author: JoanneHendrickson
manager: jtremper
ms.date: 03/10/2023
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.localizationpriority: medium
description: "Learn about the default managed properties for SharePoint Online, their settings, and the default mapping between crawled and managed properties."
---

# Overview of crawled and managed properties in SharePoint Online
 
A  *crawled property*  is content and metadata that is extracted from an item, such as a document or a URL, during a crawl. A crawled property can be an author, title, or subject. To include the content and metadata of crawled properties in the search index, you map crawled properties to managed properties. Managed properties can have a large number of settings, or attributes. These attributes determine how the contents are shown in search results. The search schema contains the attributes on managed properties and the mapping between crawled properties and managed properties. For more information, see [Overview of the search schema in SharePoint Server](../../SharePoint/SharePointServer/search/search-schema-overview.md) and [Manage the search schema in SharePoint Online](manage-search-schema.md).
  
## Managed properties overview

For a list of default managed properties and their attributes inherited from SharePoint Server see [Overview of crawled and managed properties in SharePoint Server](../SharePointServer/technical-reference/crawled-and-managed-properties-overview.md).

The following table lists the default managed properties and their attributes specific to SharePoint Online. For each managed property that by default is mapped to one or several crawled properties, these crawled properties are listed in the **Mapped Crawled Properties** column.

### Managed properties for SharePoint in Microsoft 365.
|Property name|Type|Multi-valued|Queryable|Searchable|Retrievable|Refinable|Sortable|Mapped crawled properties|Comment
|---|---|---|---|---|---|---|---|---|---|
|DepartmentId|Text|No|Yes|No|Yes|Yes|No|ows_DepartmentId|Site ID of the hub of the immediate hub. Applies to all items in the hub/associated sites.
|RelatedHubSites|Text|Yes|Yes|No|Yes|No|No|ows_RelatedHubSites|Site IDs of associated hubs including hub hierarchies. Can be used instead of DepartmentId for most scenarios. Applies to all items in the hub/associated sites.
|IsHubSite|Yes/No|No|Yes|No|Yes|No|No|ows_IsHubSite|Applies to the site result of a hub (contentclass=STS_Site)
|ModifierAADIDs|Text|Yes|Yes|No|Yes|Yes|Yes||Semi-colon separated list of AADIDs for modifiers of a file or page ordered in date descending order. (\*)
|ModifierDates|Date and Time|Yes|No|No|Yes|No|No||Semi-colon separated list of modification dates for modifiers of a file or page ordered in date descending order. (\*)
|ModifierNames|Text|Yes|Yes|No|Yes|No|No||Semi-colon separated list of the names for modifiers of a file or page ordered in date descending order. (\*)
|ModifierUPNs|Text|Yes|No|No|Yes|No|No||Semi-colon separated list of UPNs for modifiers of a file or page ordered in date descending order. (\*)
|ChapterTitle|Text|Yes|Yes|Yes|Yes|No|No|ChapterTitle|Semi-colon separated list of [auto-generated chapters on Teams meeting videos](https://support.microsoft.com/en-us/office/auto-generated-chapters-on-teams-meeting-videos-7af781d3-ed33-4aae-bb66-0abd4c6c4c98). (\*)
|ChapterOffset|Text|Yes|No|No|Yes|No|No|ChapterOffset|Semi-colon separated list of time codes matching the chapter titles for [auto-generated chapters on Teams meeting videos](https://support.microsoft.com/office/auto-generated-chapters-on-teams-meeting-videos-7af781d3-ed33-4aae-bb66-0abd4c6c4c98). (\*)

\* Property is not guaranteed to contain data.

See [Manage search schema - Default unused managed properties](manage-search-schema.md#default-unused-managed-properties) for a list of the reusable managed properties available in SharePoint Online.
