---
title: "Manually request crawling and re-indexing of a site, a library or a list"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 6/20/2018
audience: End User
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
search.appverid:
- SPO160
- MET150
ms.assetid: 9afa977d-39de-4321-b4ca-8c7c7e6d264e
description: "Manually request crawling and full re-indexing of a site by clicking the Reindex site button. All of the site content is marked as changed and will be picked up during the next crawl and re-indexed."
---

# Manually request crawling and re-indexing of a site, a library or a list

In SharePoint Online, content is automatically crawled based on a defined crawl schedule. The crawler picks up content that has changed since the last crawl and updates the index. You will want to manually request crawling and full re-indexing of a site, a document library, or a list after a schema change has occurred. 

> [!CAUTION]
>  Re-indexing a site can cause a massive load on the search system. Don't re-index your site unless you've made changes that require all items to be re-indexed. 

## Re-index after changing managed properties
<a name="__top"> </a>

When people search for content on your SharePoint sites, what's in your search index decides what they'll find. The search index contains information from all documents and pages on your site. 
  
The search index is built up by crawling the content on your SharePoint site. The crawler picks up content and metadata from the documents in the form of crawled properties. To get the content and metadata from the documents into the search index, the crawled properties must be mapped to managed properties. Only managed properties are kept in the index. This means that users can only search on managed properties.
  
When you have changed a managed property, or when you have changed the mapping of crawled and managed properties, the site must be re-crawled before your changes will be reflected in the search index. Because your changes are made in the search schema, and not to the actual site, the crawler will not automatically re-index the site. To make sure that your changes are crawled and fully re-indexed, you must request a re-indexing of the site. The site content will be re-crawled and re-indexed so that you can start using the managed properties in queries, query rules and display templates.
  
You can also choose to only re-index a document library or a list. When you have changed a managed property that's used in a library or list, or changed the mapping of crawled and managed properties, you can specifically request a re-indexing of that library or list only. All of the content in that library or list is marked as changed, and the content is picked up during the next scheduled crawl and re-indexed.
  
Learn more about search and crawled and managed properties in [Manage the search schema in SharePoint Online](manage-search-schema.md).
  
See also: [Enable content on a site to be searchable](make-site-content-searchable.md)
  
## Re-index a site
<a name="__top"> </a>
  
1. On the site, select **Settings** ![Settings icon.](media/a47a06c3-83fb-46b2-9c52-d1bad63e3e60.png), and then select **Site settings**. If you don't see **Site settings**, select **Site information**, and then select **View all site settings**. 
    
2. Under **Search**, click **Search and offline availability**.
    
3. In the **Reindex site** section, click **Reindex site**. 
    
4. A warning appears, click **Reindex site** again to confirm. The content will be re-indexed during the next scheduled crawl. 
    
## Re-index a document library or a list
<a name="__top"> </a>

1. On the site, go to the list or library that you want to re-index. 
    
2. In the ribbon, click the **Library** tab or the **List** tab. 
    
3. In the **Library** ribbon, choose **Library Settings**. Or, in the **List** ribbon, choose **List Settings**.
  
1. On the Settings page, under **General Settings**, choose **Advanced settings**.
    
2. Scroll down to **Reindex Document Library** or **Reindex List**, and click the button. The content will be re-indexed during the next scheduled crawl.
    

  

