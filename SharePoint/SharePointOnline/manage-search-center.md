---
title: "Manage the Search Center in SharePoint Online"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 4/5/2018
audience: Admin
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

The Search Center is a classic search experience. The Search Center is a site or site collection that has a starting page where users enter search queries and a search results page where users can drill into and refine search results, or run a new query.  

SharePoint Online offers two types of Search Centers: the **Basic** Search Center and the **Enterprise** Search Center. By default SharePoint Online is set up with the Basic Search Center. 

Both Search Centers search the same content and show the same search results. The main difference is that the Enterprise Search Center comes with the search verticals People, Conversations, and Videos. Search verticals are pages that are tailored for displaying search results that are filtered and formatted for a specific content type or class. Search verticals help users move quickly between such different types and classes of content. Also, as a search administrator you have more options for tailoring the look and feel of the Enterprise Search Center.

If your organization needs an enterprise-wide search experience, [evaluate first whether the modern search experience covers your needs](get-started-with-modern-search-experience.md). Modern search also comes with verticals, it doesn't require any set up, and the results are personal. [Learn about the modern search experience for users](https://support.office.com/article/what-s-new-in-search-in-office-365-b81ab573-ec9c-4aa9-a369-b3c630f878a7?). 

If modern search doesn't cover you needs, you can [switch from the Basic Search Center to an Enterprise Search Center](switch-from-enterprise-search-center-to-basic.md).



## Search Center pages
<a name="__top"> </a>

These pages are located in the **Pages** library, and they contain predefined Web Parts that you can customize to improve the end user's search experience. 
  
|**Page**|**Description**|
|:-----|:-----|
|default.aspx  <br/> |The home page for Search Centers, and the page where users enter their queries.  <br/> |
|results.aspx  <br/> |The default search results page for the Search Centers. <br/> If you have an Enterprise Search Center, this is also the search results page for the **Everything** search vertical.  <br/> |
|peopleresults.aspx  <br/> |If you have an Enterprise Search Center, this is the search results page for the **People** search vertical.   <br/> |
|conversationresults.aspx  <br/> |If you have an Enterprise Search Center, this is the search results page for the **Conversations** search vertical. <br/> |
|videoresults.aspx  <br/> |If you have an Enterprise Search Center, this is the search results page for the **Videos** search vertical.  <br/> |
|advanced.aspx  <br/> |This is the search page where users can apply some restrictions to their search phrases — for example, they can limit the search to an exact phrase.  <br/> |
   
As a global or SharePoint admin, you can also create your own search pages and add them to the Enterprise Search Center as search verticals, see [Add a search vertical to the Search Navigation Web Part](search-navigation-web-part.md#add-a-search-vertical-to-the-search-navigation-web-part).

  
## About the Web Parts used on Search Center pages
<a name="__top"> </a>

The Search Center pages contain the following predefined Web Parts: Search Box Web Part, Search Results Web Part, Search Navigation Web Part, and Refinement Web Part.

If you have an Enterprise Search Center, the Web Parts on the search result pages are by default set up the same way. The only difference is that the query in the **Search Results** Web Part is directed to different result sources for each search vertical page. For example, for the **People** search vertical page, the query in the **Search Results** Web Part is limited to the **Local People Results** result source. For the **Videos** search vertical page, the query in the **Search Results** Web Part is limited to the **Local Video Results**.
   
For information about how to customize the Search Center Web Parts, see the following articles:
  
- [Change settings for the Search Box Web Part](search-box-web-part.md)
    
- [Change settings for the Search Results Web Part](https://support.office.com/article/40ff85b3-bc5e-4230-b1dd-f088188e487e)
    
- [Change settings for the Search Navigation Web Part](search-navigation-web-part.md)
    
- [Change settings for the Refinement Web Part](refinement-web-part.md)
    

