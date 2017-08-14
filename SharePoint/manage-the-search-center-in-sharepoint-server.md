---
title: Manage the Search Center in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: f628e7df-ce37-4c33-aed3-7c6745d48a39
---


# Manage the Search Center in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-24* **Summary:** Learn about pages that are created in a Search Center site in SharePoint Server 2016 and SharePoint Server 2013, and see articles about how to configure Web Parts.When you create an Enterprise Search Center site collection as described in  [Create a Search Center site in SharePoint Server](html/create-a-search-center-site-in-sharepoint-server.md), SharePoint Server creates a default search home page and a default search results page. In addition, several pages known as  *search verticals*  are also created. Search verticals are customized for searching specific content, such as People, Conversations, and Videos, and they display search results that are filtered and formatted for a specific content type or class.The following pages are created in an Enterprise Search Center site collection: 
- **default.aspx:** the home page for the Search Center, and the page where end-users enter their queries.
    
  
- **results.aspx:** the default search results page for the Search Center. It is also the search results page for the **Everything** search vertical.
    
  
- **peopleresults.aspx:** the search results page for the **People** search vertical.
    
  
- **conversationresults.aspx:** the search results page for the **Conversations** search vertical.
    
  
- **videoresults.aspx:** the search results page for the **Videos** search vertical.
    
  
- **advanced.aspx:** the search page where end-users can apply some restrictions to their search phrases — for example, limiting the search to an exact phrase.
    
  
These pages are located in the **Pages** library, and they contain Web Parts that you can customize to improve the end-user search experience. This article describes the Web Parts on these pages, and how you can configure the different Web Parts settings to improve how search results are displayed.By default, the Web Parts on the search vertical pages (results.aspx, peopleresults.aspx, conversationresults.aspx, videoresults.aspx, advanced.aspx) are the same. However the query in the **Search Results Web Part** is configured differently for each search vertical page. For each search vertical page, the query in the **Search Results Web Part** is directed to a particular result source. This can be a result source that defines the search vertical or any result source that you want to direct queries to when you create a custom search vertical. For example, for the **peopleresults.aspx** search vertical page, the query in the **Search Results Web Part** is limited to the **Local People Results (System)** result source. For the **videoresults.aspx** search vertical page, the query in the **Search Results Web Part** is limited to the **Local Video Results (System).**The following articles describe how to configure properties for each Web Part that is used in the Enterprise Search Center site: 
-  [Configure properties of the Search Box Web Part in SharePoint Server](html/configure-properties-of-the-search-box-web-part-in-sharepoint-server.md)
    
  
-  [Configure properties of the Search Results Web Part in SharePoint Server](html/configure-properties-of-the-search-results-web-part-in-sharepoint-server.md)
    
  
-  [Configure properties of the Refinement Web Part in SharePoint Server](html/configure-properties-of-the-refinement-web-part-in-sharepoint-server.md)
    
  
-  [Configure properties of the Search Navigation Web Part in SharePoint Server](html/configure-properties-of-the-search-navigation-web-part-in-sharepoint-server.md)
    
  

