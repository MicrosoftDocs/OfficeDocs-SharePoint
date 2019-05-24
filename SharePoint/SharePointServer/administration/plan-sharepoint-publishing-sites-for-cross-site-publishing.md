---
title: "Plan publishing sites for cross-site publishing in SharePoint Server"
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.date: 3/12/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 6f1b9f42-2408-43e3-ab87-33b122a8b545

description: "Learn how to plan publishing site collections for a SharePoint Server cross-site publishing solution."
---

# Plan publishing sites for cross-site publishing in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
When you use cross-site publishing in SharePoint Server, you use one or more authoring site collections for authoring and storing content, and one or more publishing site collections to control the design of the site and show content. This article describes how to plan publishing sites for your cross-site publishing solution.
  
This article builds on the information in [Overview of cross-site publishing in SharePoint Server](overview-of-cross-site-publishing.md). After you finish reading this article, make sure that you read the next article, [Plan search for cross-site publishing sites in SharePoint Server 2016](plan-search-for-sharepoint-cross-site-publishing-sites.md).
  
## Plan site collections and site structure for SharePoint publishing sites
<a name="BKMK_SiteStructure"> </a>

Publishing site collections must have the SharePoint Server publishing features activated. We recommend that you use the Publishing Portal Site Collection template to create publishing site collections because the publishing features are activated by default when you use that site collection template. If you use a site collection template that is not for a publishing site collection, you must enable the SharePoint Server publishing features. For more information, see [Publishing features overview (SharePoint Server 2010)](https://go.microsoft.com/fwlink/p/?LinkId=402901). For information about how to activate the publishing features, see [Enable publishing features](https://go.microsoft.com/fwlink/p/?LinkID=261798).
  
Because the publishing site collection reuses content and term sets from the authoring site to show content, publishing sites are much more lightweight than authoring sites. Therefore, the site structure for a publishing site is usually very different from the authoring site. The publishing site contains a master page, a limited number of page layouts, managed navigation, and a single Pages library that contains the catalog and catalog item pages used to show catalog content. The URLs for the site are created based on the terms in the tagging term set used on the authoring site. Therefore, you do not have to manually create a complex site structure for a publishing site. 
  
## Plan security for SharePoint publishing sites
<a name="BKMK_Security"> </a>

Although you plan security for publishing sites in the same way that you do for any other SharePoint Server site, also consider the following:
  
- Who are the designers, and what permission levels should they be granted? Because the publishing site is where master pages, page layouts, and CSS files are stored, designers must have read and write permissions to the site.
    
- Is this an Internet site that allows for anonymous access? What web application should the publishing site collection be in to allow anonymous access for visitors? You must decide who should have Read permission levels for content shown on the publishing site.
    
- If this is an Internet site, do you have to set up claims-based authentication for designers?
    
- If this is an intranet or extranet site, what authentication method do you have to use? For more information about user authentication, see [Plan for user authentication methods in SharePoint Server](../security-for-sharepoint-server/plan-user-authentication.md).
    
When you enable anonymous access for a catalog, security on the authoring site can be treated independently from how it is represented in search. When anonymous access is enabled, indexed content is searchable and viewable to anonymous users on the publishing site. However, if you change permissions to individual items in the catalog, those permissions are respected by the search system, and any items that are restricted to certain groups will not be available to anonymous users. This allows for greater flexibility when you plan to share content with anonymous users.
  
## Plan design and branding for SharePoint publishing sites
<a name="BKMK_Design"> </a>

In a cross-site publishing solution, the publishing sites contain the files and other resources that a designer creates and that are used to brand the site. The following list describes the major branding components that a designer must create.
  
- **Master pages** Define the chrome and shared elements of a site. 
    
- **Page layouts** Templates for specific types of pages in a site. 
    
- **Display templates** Templates used within Content Search Web Parts that control which managed properties are shown in the search results, and how they appear. 
    
In general, you plan the design of the publishing sites exactly as you do for any branded site. You should work with a designer to collect design requirements, decide the browsers and devices that you want to support, and then create a wireframe for the sites. To plan for specific SharePoint Server aspects of the publishing sites, consider the following:
  
- How many publishing sites will you have?
    
- How many visual designs will you have for the publishing sites?
    
- How many master pages are needed?
    
- What catalog content will be shown on each publishing site, and how should it look?
    
- What devices will you support, and will you have to have separate device channels and master pages?
    
For more information, see [SharePoint page model overview](https://go.microsoft.com/fwlink/p/?LinkId=261548).
  
## Plan catalog connections for SharePoint publishing sites
<a name="BKMK_CatalogConnections"> </a>

When you connect a publishing site to a catalog, SharePoint Server automatically creates a result source for the catalog. You can also do the following:
  
- Integrate the tagging term set from the catalog into the navigation term set on the publishing site.
    
- Create a category page layout and catalog item page layout for the catalog content.
    
- Set up a catalog item friendly URL to the catalog item page.
    
If you choose to not integrate the catalog into your publishing site when you connect to a catalog, you must do each of those tasks manually.
  
For information about how to connect a publishing site to a catalog, see [Connect a publishing site to a catalog in SharePoint Server](connect-a-publishing-site-to-a-catalog.md).
  
## Plan navigation term sets for SharePoint publishing sites
<a name="BKMK_navtermsets"> </a>

When you connect a publishing site to a catalog, you have the option to pin the tagging terms from the authoring site to navigation of the publishing site. When you view the Site Navigation term set in the Term Store Management Tool, you'll be able to configure the navigation settings for each term. When you plan the navigation term sets for a publishing site, consider the following:
  
- Will the navigation term titles be the same as the original tagging term titles? If the titles will be different, what should the new titles be?
    
- Should the navigation term appear in the Global and Current Navigation Menus?
    
- Should the navigation term use a friendly URL that points to a term-driven page, point to a different URL, or just be a text-only heading?
    
When you configure the navigation term set, you'll be able to change other settings such as target page settings, search engine optimization, and catalog item page settings. If you use a site collection template, such as the Team Site template, that does not create a publishing site collection, and then activate the publishing feature, you must also be sure to turn on managed navigation for the site collection.
  
## Plan to show catalog content in SharePoint publishing sites
<a name="BKMK_DisplayCatalogContent"> </a>

This section describes how to plan to show catalog content in publishing sites. The structure of the catalog data will be important when you plan the category pages and catalog item pages. How you want to show the content in the different levels within the catalog will determine which Web Parts you use on the category pages and catalog item pages.
  
### Plan category pages and catalog item pages
<a name="BKMK_PlanCategoryPagesAndItemDetailPages"> </a>

When you set up a site that uses catalog content, SharePoint Server can automatically create a category page and a catalog item page for you when you connect to a catalog. This section describes what you should plan for if you choose to customize the default pages, or create these pages yourself. For more information about category pages and catalog item pages, see "Category pages and catalog item pages" in the "Publishing site collections for SharePoint cross-site publishing" section in [Overview of cross-site publishing in SharePoint Server](overview-of-cross-site-publishing.md).
  
#### Plan category pages

As you plan to customize default category pages, or create your own, consider the structure of the content, and determine what content you want to show at different points within this structure. Consider the following:
  
- **How many levels (categories) do you have in the term set that is used for catalog navigation?**
    
    If you want to make a clear differentiation between the levels (categories) within the catalog, you could create one category page per level within the term set.
    
- **Will you customize the default category pages, or create your own?**
    
    If you choose to create your own category pages, after you connect to a catalog and specify the custom category page to show content, you must open the page in edit mode and configure the queries for any Content Search Web Parts that you added to the page.
    
- **What content is important to show for users to easily browse within the catalog?**
    
    When you think about what content to show, you should also think about which Web Parts you want to include on category pages. For example, if you use a Refinement Panel Web Part and faceted navigation, users can easily browse to content by filtering on properties from the catalog. You can also add a Popular Items Web Part to show items that are perceived to be relevant for the user. You should also consider if you want to use only Search Web Parts, or if you want to include other content Web Parts. For more information, see [Plan to add Search Web Parts to pages](#BKMK_PlanToAddSearchDrivenWebPartsToPages) later in this article. 
    
- **Can you use the same design across all category pages?**
    
    If you can't use the same design across all category pages, you'll have to create separate pages that have separate design. After you connect to a catalog and specify the category page to use to show content, you must open the page in edit mode and configure the queries for any Content Search Web Parts on the page.
    
- **How much work do you think is acceptable when maintaining these pages?**
    
    The more category pages that you have, the more maintenance work that you'll have to do. Limit the number of category pages so that you reduce the number of places where you have to do change management.
    
For information about how to create and customize a category page layout, see [How to: Customize page layouts for a catalog-based site in SharePoint 2013](https://msdn.microsoft.com/library/dn144674.aspx)
  
#### Plan catalog item pages

As you plan to customize default catalog item pages, or create your own, consider the following:
  
- **Do you want to display items in a group?**
    
    The automatically created catalog item page uses Catalog Item Reuse Web Parts when displaying content. By default, the Catalog Item Reuse Web Part is configured to use server-side rendering, and therefore, search engines such as Google and Bing can discover and log individual items in the catalog. Also, users who haven't enabled JavaScript, for example for accessibility reasons, will be able to view the content. The Catalog Item Reuse Web Part is configured to automatically record the default usage events used by Usage analytics.
    
    When you plan to display items on a catalog item page, consider if you want to display an item in a group or not. For example, in an Internet Business scenario where you have a website selling clothes, you may want to group all available sizes of a particular item on the catalog item page. Users who browse to the catalog item page, can then quickly view all available sizes for that item. For this group scenario, you can't use the automatically created catalog item page because it uses Catalog Item Reuse Web Parts. Catalog Item Reuse Web Parts can only retrieve one item at a time, and not a group of items. Therefore, if you want to display items in a group on your catalog item page, you have to create your own catalog item page, and use a Content Search Web Part to display the items.
    
    > [!NOTE]
    > Even though the Content Search Web Part by default uses client-side rendering and JavaScript to display search results, it will automatically implement XSLT-based server-side rendering to render content to search engines such as Google and Bing. However, users who haven't enabled JavaScript, for example for accessibility reasons, won't be able to view the content. To make sure that your content can be viewed independently of whether JavaScript is enabled, consider changing the Content Search Web Part to always use XSLT-based server-side rendering. > Also be aware that usage events for Usage analytics are not automatically recorded in the Content Search Web Part, but you can configure the display template to record usage events. For more information, see [Configure recommendations and usage event types in SharePoint Server](configure-recommendations-and-usage-event-types.md). 
  
    For more information about the differences between the Catalog Item Reuse Web Part and the Content Search Web Part, see [Search Web Parts and when to use the different Web Parts](plan-sharepoint-publishing-sites-for-cross-site-publishing.md#BKMK_WhenToUseDifferentWP).
    
- **Can you use the same design across all catalog item pages?**
    
    If you can't use the same design across all catalog item pages, you'll have to create separate pages that have separate designs. After you connect to a catalog and specify the catalog item page to use to show content, you must open the page in edit mode and configure the queries for any Content Search Web Parts on the page.
    
- **How much work do you think is acceptable when maintaining these pages?**
    
    The more catalog item pages that you have, the more maintenance work you'll have to do. Limit the number of catalog item pages to reduce the number of places where you have to do change management.
    
For information about how to create and customize a catalog item page layout, see [How to: Customize page layouts for a catalog-based site in SharePoint 2013](https://msdn.microsoft.com/library/dn144674.aspx)
  
### Plan to add Search Web Parts to pages
<a name="BKMK_PlanToAddSearchDrivenWebPartsToPages"> </a>

The Search Web Parts show content from the search index. The Search Web Parts have different predefined queries, such as what type of content to search for, and where to search for the content. When users browse to a page that contains a Search Web Part, the Web Part automatically issues the query defined in the Web Part, and the search results appear in the Web Part. As search system discovers new content, an updated list of items appears in the Web Part every time that the page is viewed.
  
You can add one or more Search Web Parts to the pages. When you add a Search Web Part, you can use the predefined query, or you can change the default query settings. You can also change how the results appear in the Web Part, for example, by specifying to sort items by price or by popularity. You can change the predefined query by editing the Web Part and changing its search criteria.
  
The Search Web Parts use display templates to control how the results appear in the Web Part. Display templates are HTML files that specify which managed properties from the search result to show, and also how these properties should be shown. For example, a display template could specify that the managed property PublishingImage shows a 100x100 pixel picture, and the managed property Title appears in bold to the left of the image. 
  
For information about how to create and customize display templates, see [SharePoint 2013 Design Manager display templates](https://msdn.microsoft.com/library/jj945138.aspx)
  
### Search Web Parts and when to use the different Web Parts
<a name="BKMK_WhenToUseDifferentWP"> </a>

The following table describes Search Web Parts that are commonly used in web content management scenarios. For information about Search Web Parts commonly used in a productivity search scenario, see [Manage the Search Center in SharePoint Server](../search/manage-the-search-center-in-sharepoint-server.md).
  
**Search Web Parts**

|**Category**|**Web Part**|**Description**|
|:-----|:-----|:-----|
|Content Rollup  <br/> |Content Query  <br/> |Do not use for cross-site publishing. Use the Content Search Web Part or one of the Web Parts in the Search-Driven Content Web Part category.  <br/> |
||Content Search  <br/> |Use this Web Part to display catalog content on a category page. You can also use it to display items in a group on your catalog item page. In the Content Search Web Part (CSWP), you can select a result source to specify which content should be searched. You can also use Keyword Query Language to add more filters and search terms to the query.  <br/> By default, this Web Part uses client-side rendering, which means that you can use JavaScript in the display template to customize how search results should be displayed. To enable search engines such as Google and Bing to discover and log individual items in the catalog, the CSWP will automatically implement XSLT-based server-side rendering when rendering content to search engines.  <br/> Another benefit of using client-side rendering is that the server requires fewer resources because the rendering happens in the browser. For information about performance considerations when you add a CSWP to a page, see [Estimate capacity and performance for Web Content Management (SharePoint Server 2013)](web-content-management-capacity-and-performance.md) <br/> > [!NOTE]> Because the Content Search Web Part uses JavaScript to display content, users who haven't enabled JavaScript, for example for accessibility reasons, won't be able to view the content. To make sure that that your content can be viewed independently of whether JavaScript is enabled, consider changing the Content Search Web Part to always use XSLT-based server-side rendering. Note that using XSLT-based server-side rendering often require more server resources and may reduce performance.           |
|Search  <br/> |Refinement Panel  <br/> |This Web Part adds refiners to the page. You can use this Web Part to add stand-alone refiners and refiners for faceted navigation.  <br/> You must enable managed properties as refiners before any refiners will display in this Web Part. For more information, see [Configure refiners and faceted navigation in SharePoint Server](configure-refiners-and-faceted-navigation.md).  <br/> |
||Taxonomy Refinement Panel  <br/> |This Web Part combines refinement with managed navigation, and can be used to add a powerful search-driven navigation experience to the catalog content. It can only be used in combination with managed navigation, and must be associated with another Search Web Part on the page, such as a Content Search Web Part. It enables you to filter search results in the associated Web Part by displaying refiners based on the current navigation term. The refiners shown in the Taxonomy Refinement Panel Web Part are child refiners of the current navigation term. When a user clicks a refiner, the search results in the associated Web Part are filtered accordingly. What makes this Web Part especially powerful is that it accounts for previous queries or refinements made by the user when displaying the refiners.  <br/> > [!IMPORTANT]> We don't recommend that you use the Taxonomy Refinement Panel Web Part on a page that has more than 200 navigation nodes under it. A large number of navigation nodes may cause slow server response times and decrease throughput. For more information, see [Estimate capacity and performance for Web Content Management (SharePoint Server 2013)](web-content-management-capacity-and-performance.md)          |
|Search-Driven Content  <br/> |Articles  <br/> |Shows items that are associated with the Article Page content type.  <br/> |
||Catalog Item Reuse  <br/> |Only use this Web Part on a catalog item page when you don't want to display your catalog items in a group. This Web Part uses server-side rendering so that search engines such as Bing or Google can discover and log individual items in the catalog. It's also configured to automatically record the default usage events used by Usage Analytics.  <br/> The configuration of this Web Part is somewhat different from the other Search Web Parts. Most configuration of this Web Part is performed in the HTML page layout file of the catalog item page. The Web Part can only display one managed property. Therefore, for each managed property that you want to display on your catalog item page, you must add one Catalog Item Reuse Web Part to the HTML page layout file. In addition, you must add one Catalog Item Reuse Web Part as a Web Part directly on the catalog item page. In that Web Part, you configure the query for the catalog item that should be retrieved. The Catalog Item Reuse Web Parts that were added in the HTML page layout file are configured to reuse the data that are retrieved by this query.  <br/> The Catalog Item Reuse Web Part doesn't use display templates to show content. Instead, formatting is based on the managed property type, for example **Date** or **HTML**.  <br/> For information about how to customize a catalog item page layout that uses Catalog Item Reuse Web Parts, see [How to: Customize page layouts for a catalog-based site in SharePoint 2013](https://msdn.microsoft.com/library/dn144674.aspx) <br/> For information about performance considerations when you add a Catalog-Item Reuse Web Part to your page, see [Estimate capacity and performance for Web Content Management (SharePoint Server 2013)](web-content-management-capacity-and-performance.md) <br/> |
||Items Matching a Tag  <br/> |Shows items that are tagged with a term.  <br/> |
||Pictures  <br/> |Shows any items that are associated with the Picture or Image content type.  <br/> |
||Popular Items  <br/> |Use this Web Part to show the most popular items that satisfy a set of criteria. For example, you can add this Web Part to a Category page to show "Most popular items in category."  <br/> |
||Recently Changed Items  <br/> |Shows items that were recently changed. This can help users track the latest activity on a site or in a library.  <br/> |
||Recommended Items  <br/> |Use this Web Part to show content recommendations based on how users have previously interacted with the site. For example, you can add this Web Part to a catalog item page. If a user views a specific item, this Web Part will show other items that users have previously viewed, such as "Users who viewed this item also viewed these items."  <br/> By default, the query is restricted to recommended items for the current site. You can change this setting to recommended items based on a token from the URL, and also restrict the query to a specific URL or content type.  <br/> |
||Videos  <br/> |Displays any items that are associated with the Video content type. It will sort items by number of views.  <br/> |
||Web Pages  <br/> |Displays any items that are derived from the Page content type.  <br/> |
||Wiki Pages  <br/> |Displays any items that are associated with the Wiki Page content type.  <br/> |
   
For information about how to add and configure Search Web Parts, see [Configure Search Web Parts in SharePoint Server](configure-search-web-parts.md).
  
## See also
<a name="BKMK_DisplayCatalogContent"> </a>

#### Concepts

[Overview of publishing to Internet, intranet, and extranet sites in SharePoint Server](overview-of-publishing-to-internet-intranet-and-extranet-sites.md)
  
[Plan for Internet, intranet, and extranet publishing sites in SharePoint Server](plan-for-internet-intranet-and-extranet-publishing-sites.md)
  
[Plan for cross-site publishing in SharePoint Server](plan-for-cross-site-publishing.md)
  
[Overview of cross-site publishing in SharePoint Server](overview-of-cross-site-publishing.md)
  
[Plan the logical architecture for cross-site publishing in SharePoint Server](plan-the-logical-architecture-for-cross-site-publishing.md)
  
[Plan authoring sites for cross-site publishing in SharePoint Server](plan-sharepoint-authoring-sites-for-cross-site-publishing.md)
  
[Plan search for cross-site publishing sites in SharePoint Server 2016](plan-search-for-sharepoint-cross-site-publishing-sites.md)
  
[Configure cross-site publishing in SharePoint Server](configure-cross-site-publishing.md)
  
[Estimate capacity and performance for Web Content Management (SharePoint Server 2013)](web-content-management-capacity-and-performance.md)

