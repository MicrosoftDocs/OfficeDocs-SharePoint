---
title: "Manage the Search Center in SharePoint Online"
ms.author: tlarsen
author: tklarsen
manager: arnek
ms.date: 4/5/2018
ms.audience: Admin
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
search.appverid:
- SPO160
- MET150
ms.assetid: 174d36e0-2f85-461a-ad9a-8b3f434a4213
description: "Learn how to customize the Search Center pages to improve the end user's search experience. Learn about search verticals (Everything, People, Videos, and Conversations) and the predefined Web Parts (Search Box Web Part, Search Results Web Part, Search Navigation Web Part, and Refinement Web Part.)"
---

# Manage the Search Center in SharePoint Online

A Search Center is a classic experience, where users enter search queries and view the search results. In SharePoint Online, a Search Center site is automatically available at *\<host_name\>/search/*. You'll have a default search home page and a default search results page. In addition, there are several pages known as search verticals. Search verticals are customized for searching specific content, such as People, Conversations, and Videos. Search verticals display search results that are filtered and formatted for a specific content type or class.
  
## Search Center pages
<a name="__top"> </a>

These pages are located in the **Pages** library, and they contain predefined Web Parts that you can customize to improve the end user's search experience. 
  
|**Page**|**Description**|
|:-----|:-----|
|default.aspx  <br/> |The home page for the Search Center, and the page where users enter their queries.  <br/> |
|results.aspx  <br/> |The default search results page for the Search Center. It's also the search results page for the **Everything** search vertical. When users type a query in the Search Box on a SharePoint site, this page displays their search results.  <br/> |
|peopleresults.aspx  <br/> |The search results page for the **People** search vertical.  <br/> |
|conversationresults.aspx  <br/> |The search results page for the **Conversations** search vertical.  <br/> |
|videoresults.aspx  <br/> |The search results page for the **Videos** search vertical.  <br/> |
|advanced.aspx  <br/> |The search page where users can apply some restrictions to their search phrases — for example, they can limit the search to an exact phrase.  <br/> |
   
As a SharePoint Online administrator, you can also create your own pages and add them to the Search Center as search verticals. 
  
## About the Web Parts used on Search Center pages
<a name="__top"> </a>

The Search Center pages contain the following predefined Web Parts: Search Box Web Part, Search Results Web Part, Search Navigation Web Part, and Refinement Web Part.
  
By default, the Web Parts on the search result pages are set up the same way. The only difference is that the query in the **Search Results** Web Part is directed to different result sources for each search vertical page. For example, for the **People** search vertical page, the query in the **Search Results** Web Part is limited to the **Local People Results** result source. For the **Videos** search vertical page, the query in the **Search Results** Web Part is limited to the **Local Video Results** **.**
  
For information about how to customize the Search Center Web Parts, see the following articles:
  
- [Change settings for the Search Box Web Part](search-box-web-part.md)
    
- [Change settings for the Search Results Web Part](https://support.office.com/article/40ff85b3-bc5e-4230-b1dd-f088188e487e)
    
- [Change settings for the Search Navigation Web Part](search-navigation-web-part.md)
    
- [Change settings for the Refinement Web Part](refinement-web-part.md)
    

