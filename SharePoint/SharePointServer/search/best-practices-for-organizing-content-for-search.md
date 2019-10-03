---
title: "Best practices for organizing content for search in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 9/4/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: e913bd67-b50b-47d7-9784-2d312b97de0b
description: "Learn how to organize SharePoint Server content and metadata to make the content easier to find."
---

# Best practices for organizing content for search in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
These best practices for organizing SharePoint Server content and applying useful metadata will help make sure that the right content is included in the search index and that the right content is returned in search results. 
  
    
## Keep your most important content in SharePoint
<a name="Keep_content_in_SP"> </a>

If possible, keep your most important content in SharePoint, and crawl and index as much premium content as possible. If you cannot crawl and index the content, consider federating results from other sources into your local search results. 
  
Try to organize content with similar value and importance into nearby site structures. The search system will automatically infer the relative importance, but you can also influence the importance of sites directly by defining authoritative pages. For more information, see the section [Specify authoritative pages](best-practices-for-organizing-content-for-search.md#Rel_Auth).
  
It is important to know what content to crawl and include in the search index, but it is also important to know what content **not** to crawl. For example, you do not want to crawl and index backup file shares. You should also establish routines for archiving obsolete content, deleting low-quality content and encourage users to add expiration dates to announcements. 
  
## Organize content in hierarchies and use natural language
<a name="Organize_hierarchies"> </a>

By organizing SharePoint content in **natural hierarchies**, you not only make it is easier for users to understand where they can find and file their content, but you also make it easier for the search system to rank the content and return search results that better match the user's intent. 
  
|           **Flat structure**            |                   **Structure with hierarchy**                   |
| :-------------------------------------- | :--------------------------------------------------------------- |
| http://Europe  <br/> http://Asia  <br/> | http://sales  <br/> http://sales/Europe  <br/> http://sales/Asia |
   
URLs and other metadata of files, such as file names, are analyzed linguistically by the search system. If you use natural language for URLs and for metadata, the search system can more easily understand what information is in the site or file and give it an appropriate ranking in the results. It is much easier for the search system (and users) to understand a URL and file name like http://sales/Europe/presentations/phones.ppt than it is to make sense of http://slseur/p_phones.ppt. 
  
## Encourage users to enter rich and consistent metadata for their sites and content
<a name="Encourage_metadata"> </a>

Metadata is data that provides additional information about one or more aspects of sites and content, such as who created the content or site, when was it created, and what the purpose of the content or the site is. Consistent and rich metadata increases the quality of the content itself, and it also enables the search system to more easily discover relationships between content, and to provide more targeted and relevant search results.
  
These are some examples of important metadata that you should encourage users to provide:
  
- Title of a document
    
- Description of a site
    
- The author(s) of a document
    
- The date the content was created
    
For some document types, such as PowerPoint and Word, the search system extracts additional metadata such as headings and subheadings from inside the content, and uses this information to return the right search results and to provide rich document summaries and previews. 
  
To provide the right search results for people, it is also important that My Sites and user profile data is entered so that this information can be used as metadata by the search system. 
  
## Managing multilingual content
<a name="Multillingual_content"> </a>

The search system detects the language of most content automatically. These recommendations help prevent that the search system detects the wrong language:
  
- If possible, keep content in different languages on different sites. If the search system cannot detect the language of a particular content item, it assumes that it is in the language of the site where it is stored. 
    
- Avoid mixing languages in content and that content's metadata. Use the same language in the metadata as the language that is used in the content itself.
    
- Avoid mixing languages in a single piece of metadata. This is mostly applicable to URLs.
    
## Specify authoritative pages
<a name="Rel_Auth"> </a>

You can use the **Authoritative Pages** feature in the Search service application to specify SharePoint sites that contain the most relevant information. Search results from authoritative pages are ranked higher in the search results. 
  
You can specify three degrees of authority, and you can also specify non-authoritative sites. When you identify a site as an authority, sites that are connected to the authoritative page via hyperlinks are also boosted in the results, based on their proximity to the authoritative page. A most-authoritative page contains or links to the most relevant information. URLs designated as non-authoritative are ranked lower than other sites.
  
We recommend that you only specify a small number (four-five) of authoritative pages. If you specify lots of authoritative pages, it is difficult to predict the effects on the ranking of search results.
  
For more information, see [Configure authoritative pages in SharePoint Server](configure-authoritative-pages.md).
  

