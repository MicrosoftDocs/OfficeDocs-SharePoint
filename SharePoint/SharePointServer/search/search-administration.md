---
title: "Administer search in SharePoint Server"
ms.author: tlarsen
author: tklarsen
manager: pamgreen
ms.date: 3/9/2018
ms.audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 820ace03-1fb7-41fd-a077-28b82ebddde3
description: "Summary: Learn how to manage the search schema and the search topology in SharePoint Server."
---

# Administer search in SharePoint Server

 **Summary:** Learn how to manage the search schema and the search topology in SharePoint Server. 
  
The following articles provide information about how you operate and manage search in SharePoint Server.

#####SharePoint Server 2019 Public Preview
SharePoint Server 2019 Public Preview offers a **modern** search experience in addition to the **classic** search experience. Users get the modern search experience on their SharePoint home page, on modern sites, and in modern document libraries.

Both experiences use the same search index to find results. Search settings that impact what's indexed affect both experiences, except these settings:
- Refinable. Modern search has built-in refiners.
- Sortable. Not supported in modern search.
- Company name extraction. Not supported in modern search. 
- Custom entity extraction. Not supported in modern search.

Only the classic search experience is customizable, but some of the customization settings also affect modern search:
- Modern search uses the default result source.
- When you remove search results temporarily by specifying URLs, the results are removed from both the classic and modern search results.
- When you create single promoted results at the Search service application level, users also see the promoted results on the modern search results page when:
    - They've searched across all of SharePoint
    - They've filtered the search results page to **All result types** (default filter)
 

  
## Articles about administering search

The following articles about administering search in SharePoint Server are available to view online. Writers update articles on a continuing basis as new information becomes available and as users provide feedback.
  
|                                                                   **Content**                                                                    |                                                                **Description**                                                                 |
| :----------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------- |
| [Manage the Search Center in SharePoint Server](manage-the-search-center-in-sharepoint-server.md)                                                | Learn about pages that are created in a Search Center site in SharePoint Server, and see articles about how to configure Web Parts.            |
| [Manage the search index in SharePoint Server 2016](manage-the-index.md)                                                                         | Learn how to manage collection of content in the search index and retrieval from the search index.                                             |
| [Manage crawling in SharePoint Server](manage-crawling.md)                                                                                       | Learn how to crawl content that you want users to be able to search for in SharePoint Server.                                                  |
| [Manage search relevance in SharePoint Server](manage-relevance.md)                                                                              | Learn how you can configure settings to provide the most relevant search results.                                                              |
| [Manage the search topology in SharePoint Server](manage-the-search-topology.md)                                                                 | Learn how to manage search components to scale out the search topology in SharePoint Server.                                                   |
| [View search diagnostics in SharePoint Server](view-search-diagnostics.md)                                                                       | Learn about search and usage reports, query health reports, crawl health reports and the crawl log to analyze the health of the search system. |
| [Enable search alerts in SharePoint Server](enable-search-alerts.md)                                                                             | Learn how to enable or disable search alerts.                                                                                                  |
| [Enable query logging in SharePoint Server](enable-query-logging.md)                                                                             | Learn how to enable or disable query logging.                                                                                                  |
| [Export and import customized search configuration settings in SharePoint Server](export-and-import-customized-search-configuration-settings.md) | Learn how to import and export customized search configuration settings.                                                                       |
   

