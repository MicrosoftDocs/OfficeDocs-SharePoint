---
title: "Switch to an Enterprise Search Center in SharePoint Online"
ms.author: tlarsen
author: tklarsen
manager: arnek
ms.date: 6/29/2018
ms.audience: Admin
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
search.appverid:
- SPO160
- MET150
ms.assetid: 7c1a7462-d3d8-4a14-92f4-981b0ade9963
description: "Learn how to switch from the Basic Search Center to an Enterprise Search Center."
---

# Switch to an Enterprise Search Center in SharePoint Online

The Search Center is a classic search experience. It's a site or site collection with a starting page where users enter queries and a search result page where users can drill into and refine search results, or run a new query. It also offers an advanced search page.

By default SharePoint comes with a Basic Search Center. An Enterprise Search Center delivers an enterprise-wide search experience, including four search results pages known as search verticals. [Learn about search verticals](manage-search-center.md).

As an administrator you can switch to an Enterprise Search Center if your organization needs an enterprise-wide search experience. You can either add an Enterprise Search Center or you can convert the Basic Search Center to an Enterprise Search Center. Adding an Enterprise Search Center is easier because you can use a template.
 
  
## Add an Enterprise Search Center
Follow the steps in [Create a site collection](create-site-collection.md) to create a new site collection that uses the Enterprise Search Center template.

    
## Convert the Basic Search Center to an Enterprise Search Center

1. [Activate the site collection features](#activate-site-collection-features-for-the-search-center) that the Enterprise Search Center needs.
2. [Verify that the search results page is set to display links](#verify-which-search-verticals-links-will-display) to the Everything, People, Conversations, and Videos search pages (verticals).
3. [Display links to verticals on the search results page](#display-links-to-verticals-on-the-search-results-page) on the search results page.

    
### Activate site collection features for the Search Center
An Enterprise Search Center needs the following site collection features:
- SharePoint Server Publishing Infrastructure
- Document ID Service
- Document Sets
- Library and Folder Based Retention
- Limited-access user permission lockdown mode
- Publishing Approval Workflow
- Reporting
- Reports and Data Search Support
- Search server Web Parts and Templates
- SharePoint Server Enterprise Site Collection features
- SharePoint Server Standard Site Collection features
- Site Policy
- Video and Rich Media

1. Sign in to Office 365 as a global admin or SharePoint admin.
2. In a web browser, go to the Basic Search Center site (<host name>/search).
3. Open the **Site menu** by clicking the gear icon in the upper-right portion of the page, and then click **Site settings**.
4. In the **Site Collection Administration section**, select **Site collection features**.
5. Activate each of the features from the list above, starting with **SharePoint Server Publishing Infrastructure**.

    
### Verify which search verticals links will display
The Enterprise Search Center shall show the **Everything**, **People**, **Conversations**, and **Videos** search verticals. 
1. In a web browser, go to the results page of the Basic Search Center site (<host name>/results.aspx).
2. Open the **Site** menu by clicking the gear icon in the upper-right portion of the page, and then click **Site settings**.
3. On the **Site Settings** page, in the **Search** section, click **Search Settings**.
4. On the **Search Settings** page, in the **Configure Search Navigation** section, click to select the search vertical that you want to change or delete, and then click **Edit**.
5. Click **OK**.

### Display links to verticals on the search results page
You need to add the Search Navigation Web Part to the Search Center for the search results page to show verticals. 

In a web browser, go to the results page of the Basic Search Center site (<host name>/results.aspx).
1. Open the **Site menu** by clicking the gear icon in the upper-right portion of the page, and then click **Edit page**.
2. In the Web Part Zone where you want to show links to verticals, click **Add a Web Part**.
3. In the **Categories** list, click **Search**.
4. In the **Parts** list, click **Search Navigation**, and then click **Add**.
5. Click **Stop editing**.


    
## See also

[Manage the Search Center in SharePoint Online](manage-search-center.md)
  
[Change settings for the Search Navigation Web Part](search-navigation-web-part.md)

