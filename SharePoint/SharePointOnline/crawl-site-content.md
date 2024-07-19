---
title: Manually request crawling and reindexing of a site, a library or a list
ms.reviewer: 
ms.author: ruihu
author: maggierui
manager: jtremper
recommendations: true
ms.date: 4/24/2024
audience: End User
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.collection: M365-collaboration
ms.localizationpriority: medium
search.appverid:
- SPO160
- MET150
ms.assetid: 9afa977d-39de-4321-b4ca-8c7c7e6d264e
description: Manually request crawling and full reindexing of a site by clicking the Reindex site button. All of the site content is marked as changed and will be picked up during the next crawl and reindexed.
---

# Manually request crawling and reindexing of a site, a library or a list

In SharePoint, content is automatically crawled based on a defined crawl schedule. The crawler picks up content that has changed since the last crawl and updates the index. You'll want to manually request crawling and full reindexing of a site, a document library, or a list after a schema change has occurred. 

> [!CAUTION]
>  Reindexing a site can cause a massive load on the search system. Don't reindex your site unless you've made changes that require all items to be reindexed. 

## Reindex after changing managed properties
<a name="__top"> </a>

When people search for content on your SharePoint sites, what's in your search index decides what they find. The search index contains information from all documents and pages on your site. 
  
The search index is built up by crawling the content on your SharePoint site. The crawler picks up content and metadata from the documents in the form of [crawled properties](/sharepoint/manage-search-schema#about-the-search-schema). To get the content and metadata from the documents into the search index, the crawled properties must be mapped to managed properties. Only managed properties are kept in the index. This means that users can only search on managed properties.
  
When you change a managed property, or when you change the mapping of crawled and managed properties, the site must be recrawled before your changes are reflected in the search index. Because your changes are made in the search schema, and not to the actual site, the crawler won't automatically reindex the site. To make sure that your changes are crawled and fully reindexed, you must request a reindexing of the site. The site content is recrawled so that you can start using the managed properties in queries, query rules and display templates.
  
You can also choose to only reindex a document library or a list. When you've changed a managed property that's used in a library or list, or changed the mapping of crawled and managed properties, you can specifically request a reindexing of that library or list only. All of the content in that library or list is marked as changed, and the content is picked up during the next scheduled crawl and reindexed.
  
Learn more about search and crawled and managed properties in [Manage the search schema in SharePoint](manage-search-schema.md).
  
See also: [Enable content on a site to be searchable](make-site-content-searchable.md)
  
## Reindex a site
<a name="__top"> </a>
  
1. On the site, select **Settings** ![Settings icon.](media/a47a06c3-83fb-46b2-9c52-d1bad63e3e60.png), and then select **Site settings**. If you don't see **Site settings**, select **Site information**, and then select **View all site settings**. 
    
2. Under **Search**, select **Search and offline availability**.
    
3. In the **Reindex site** section, select **Reindex site**. 
    
4. A warning appears, check the box before **Please check this box to acknowledge and agree to the statement above.** Select **Reindex site** again to confirm. The content is reindexed during the next scheduled crawl. 
    
## Reindex a document library or a list
<a name="__top"> </a>

1. On the site, go to the list or library that you want to reindex. 
    
1. In the upper right corner, select **Settings**, and then choose **Library Settings** or **List Settings**. 

1. On the Settings page, under **General Settings**, choose **Advanced settings**. If you don't see the **Settings** page, you may need to choose **More library settings** or **More List settings**.
    
2. Scroll down to **Reindex Document Library** or **Reindex List**, and select the button. A warning appears. Select the button again to confirm. The content is reindexed during the next scheduled crawl.
  
