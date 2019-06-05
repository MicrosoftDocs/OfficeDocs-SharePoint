---
title: "Overview of managed navigation in SharePoint Server"
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.date: 3/12/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 9d1f5998-e6b6-474c-a2aa-47782b63e53e
description: "Learn about managed navigation and navigation term sets for SharePoint Server publishing sites."
---

# Overview of managed navigation in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]. 
  
The managed navigation feature in SharePoint Server enables you to build navigation for a publishing site that is derived from a SharePoint Server managed metadata taxonomy. In SharePoint Server 2010, by default, you could base navigation only on the structure of a site. To create site navigation based on any data structure, you had to create a custom navigation provider. By using managed navigation, you can design site navigation around important business concepts. Managed navigation also lets you create friendly URLs without changing the structure of your site. In SharePoint Server 2010, all publishing site URLs contained a reference to the Pages library and any folders within that library — for example, http://contoso.com/Pages/AboutUs.aspx. In SharePoint Server 2016 and SharePoint Server 2013, you can create URLs that are better for Search Engine Optimization (SEO), and easier for site visitors to read — for example, http://contoso.com/AboutUs. Managed navigation is not available in SharePoint Foundation 2013. 
  
This article describes the key elements of the managed navigation feature, its uses and benefits, how it works, how terms can be used in other locations, limitations of the feature, and includes examples of how managed navigation can be used in a publishing site.
  
For information about how to create the navigation term set that is used for site navigation, see [Plan navigation term sets in SharePoint Server](plan-navigation-term-sets.md).
  
For capacity and performance considerations when using managed navigation, see [Estimate capacity and performance for Web Content Management (SharePoint Server 2013)](web-content-management-capacity-and-performance.md)
  
## Elements of managed navigation in SharePoint Server
<a name="section1"> </a>

This section describes key concepts that are related to managed navigation.
  
### Navigation term set

A term is a word or phrase that can be associated with an item in SharePoint Server. A term set is a collection of related terms. The term set that managed navigation uses to build site navigation is called a navigation term set. For more information, see [Plan for managed metadata in SharePoint Server](../governance/managed-metadata-planning.md) and [Plan managed metadata (OLD)](/previous-versions/office/sharepoint-server-2010/ee530389(v=office.14)).
  
The navigation term set is the backbone of the managed navigation feature. By default, as you create new pages in your publishing site, new terms are automatically added to the navigation term set. For example, when you create a new page named Company History, a term named Company History is added to the navigation term set. You can choose to turn off automatic term creation on the Navigation Settings page. You can also manually add terms to the navigation term set by using the Term Store Management Tool. For more information, see [Create and manage terms in a term set](https://docs.microsoft.com/sharepoint/create-and-manage-terms). 
  
> [!NOTE]
> If automatic term creation is enabled, a new term will only be created if you choose **Add a page** on the **Settings** menu. Adding a page by using the **New Document** button on the **Files** tab in the ribbon does not create a new term in the navigation term set. 
  
Each term in a navigation term set has a friendly URL that loads a physical page in the context of that term. Terms in the navigation term set can be configured to do one of the following:
  
- Point to the same page as other terms
    
- Point to a unique page for each term
    
- Point to a URL or appear only as text
    
If you use cross-site publishing, you must use a tagging term set on the authoring site to tag catalog items for reuse. You can combine terms from one or more tagging term sets in the authoring site to create a single customized navigation term set in the publishing site. For more information about cross-site publishing, see [Plan for cross-site publishing in SharePoint Server](plan-for-cross-site-publishing.md).
  
### Target pages, category pages, and catalog-item pages

Target pages display page content, and are associated with terms and friendly URLs. You can change the default target pages that are used by the term and any child terms. 
  
When you use cross-site publishing, target pages are also known as category pages. A category page is a special page that can be automatically created when you connect a publishing site to a catalog. You can also create category pages by hand. The category page contains a Content Search Web Part that uses a term from the navigation term set to query for and dynamically display catalog content associated with the current navigation term. This enables you to use the same page repeatedly to display different content, based on the associated navigation term selected by the page visitor. For example, let's say you use cross-site publishing to display electronic products from a catalog. The category page that is used to show a list of products that use the navigation term Cameras is the same page that is also used to display a list of products that use the navigation term Printers. For more information about Content Search Web Parts, see [Plan publishing sites for cross-site publishing in SharePoint Server](plan-sharepoint-publishing-sites-for-cross-site-publishing.md).
  
A catalog-item page is also a special page that can be automatically created when you connect a publishing site to a catalog. Whereas a category page displays a set of items that match the current navigation term (for example, Laptops), the catalog-item page returns the details for a single item (for example, when a user chooses a specific model on the Laptops category page). The catalog-item page contains a Catalog-Item Reuse Web Part that uses the ID for a specific item that was returned in the results of a Content Search Web Part on a category page to show the details for the item. The ID is the set of primary key properties specified when the publishing site connects to the catalog. Catalog-item pages can be configured only when a site uses cross-site publishing and is connected to a catalog. For example, the URL http://contoso.com/cameras might contain a list of available camera models. If you click the link for the individual product Contoso Digital Camera M200, the catalog-item page displays specific information about that particular camera. Similar to the category page, the catalog-item page enables you to show different items without having to create a different page for each item in the catalog. You use the same page but it shows different content based on the selected item from a result set. 
  
For more information about category pages and catalog-item pages, see "Publishing site collections for SharePoint cross-site publishing" in [Overview of cross-site publishing in SharePoint Server](overview-of-cross-site-publishing.md).
  
### Friendly URLs

Friendly URLs are URLs that correspond to a term in the navigation term set, and that provide a shorter, more meaningful URL to a page. This makes the URL more useful to visitors to your site, and also improves search engine optimization (SEO) for your site. For example, the URL http://www.contoso.com/products/household/vacuum-cleaner is more meaningful to both users and search engines than the URL http://www.contoso.com/Products/Inventory/Pages/productViewer.aspx?productID=115&amp;name=vacuum%20cleaner&amp;CID=34q327234ef. By default, when you create a new page, a new navigation term is created, and a corresponding friendly URL is created for the page. You can use a single friendly URL to point to a single page. You can also have multiple friendly URLs that point to the same page, such as a category page. For example, if you use cross-site publishing to display content from a knowledge base, you can have separate friendly URLs for /kb/manuals, /kb/troubleshooting-guides, and /kb/product-specs that all point to the same category page, Category-KB-Articles.aspx. You do not have to use cross-site publishing to use multiple friendly URLs that point to the same page.
  
### Global navigation and current navigation controls

The global navigation control (called Top Navigation in the Snippet Gallery) is the primary navigation control that is used to display the navigation for a site. The global navigation control appears at the top of the page in the default master page, and can show one or more levels of navigation, based on terms in the navigation term set. The current navigation control (called Vertical Navigation in the Snippet Gallery) is a secondary navigation control that appears on the left side of the page in the default master page. Current navigation can show one or more levels of navigation that represent the next level of the navigation term set hierarchy based on the term that is selected in the global navigation control. For information about the Snippet Gallery, see [Add snippets to a master page or a page layout in SharePoint Server 2016](https://go.microsoft.com/fwlink/p/?LinkId=286810) in the MSDN Library. 
  
## How managed navigation works in SharePoint Server
<a name="section2"> </a>

Managed navigation works by associating a term from a navigation term set with a friendly URL and a page in the Pages library. By default, when a new page is created, a new term is created in the navigation term set, and a friendly URL is configured that points to the page. If you are using a standard publishing site that uses the author-in-place publishing model, this means that you'll probably have a 1:1 relationship between pages that are created in the site and terms in the navigation term set. Managing many terms and their corresponding pages can become difficult if your site has many pages. By using cross-site publishing to show content from one or more catalogs, you can use a few category and catalog-item pages to easily display lots of data with minimal configuration and page management. By using managed navigation, you can change the navigation term set and have those changes appear on your site without having to add new pages or change the physical structure of the site and its content.
  
Before you can use managed navigation, it must be configured in Navigation Settings on the site collection. By default, managed navigation is enabled for site collections that are created by using the Publishing Portal or the Enterprise Wiki site collection templates. On the other hand, the Product Catalog site collection template uses structural navigation because it is intended to be used as a source for catalogs that will be shared with a publishing site for cross-site publishing. When managed navigation is configured, two additional settings are also configured: new pages are automatically added to navigation, and friendly URLs are automatically created for new pages. If you turn off both settings, new pages will not be added to the navigation, and no new terms will be added to the Site Navigation term set.
  
> [!NOTE]
> To enable managed navigation for a non-publishing site, you must activate the SharePoint Server Publishing Infrastructure feature for the site collection, and activate the SharePoint Server Publishing feature for the site. 
  
## Use and benefits of managed navigation in SharePoint Server
<a name="section3"> </a>

You should use managed navigation with any publishing site in which you want the structure of the site navigation to be separate from the structure of the site and its content. If you plan to use cross-site publishing, you can use a tightly managed taxonomy to create a complex navigation structure that would otherwise be difficult and time-consuming to manage if each navigation node represented a separate page. When you use cross-site publishing, managed navigation is enabled by default in the publishing site. You can also use managed navigation in a standard author-in-place publishing scenario. The following table describes possible scenarios in which you might want to use managed navigation.
  
**Table: SharePoint managed navigation scenarios**

|**Scenario**|**Description**|
|:-----|:-----|
|Internet business site  <br/> |You can use cross-site publishing to create an Internet business site that contains a catalog that shows products to customers based on metadata. Users view pages that are created dynamically based on navigation, and users can filter results by using additional refiners. For more information, see "Plan refiners and faceted navigation" in [Plan search for cross-site publishing sites in SharePoint Server 2016](plan-search-for-sharepoint-cross-site-publishing-sites.md).  <br/> |
|Intranet site  <br/> |You can use cross-site publishing to create an internal Human Resources (HR) website that uses a tightly managed navigation structure to show authored content.  <br/> |
|Internet presence site  <br/> |You can use author-in-place publishing to create an Internet Presence site where pages are automatically added to the managed navigation. Content authors can configure navigation properties directly from the pages they create.  <br/> |
   
## Examples of managed navigation in SharePoint Server
<a name="section4"> </a>

This section provides examples of how you can use term sets, tagging term sets, and target pages to define your site's navigation hierarchy.
  
### Simple managed navigation

In the simplest form of managed navigation, every term in the navigation term set corresponds to a page in the site. Site navigation controls reflect the order and the hierarchy of terms in the navigation term set. To change the "structure" of your site — the way the structure appears as displayed in the navigation controls — you simply rearrange terms in the navigation term set.
  
For example, consider a structure that's common to many public websites. A global navigation menu is displayed horizontally across the top of the page. The global navigation menu has entries for the highest level of information that's contained on the site. In this example, the global navigation menu contains the following entries:
  
- Products
    
- Customer support
    
- About us
    
The current navigation menu is displayed vertically on the left side of the page. It shows the next level in the navigation hierarchy, relative to whichever page the site visitor is currently viewing. If the visitor is viewing the **About us** page, then the current navigation menu displays the following entries: 
  
- Company history
    
- Press releases
    
- Contact us
    
You can easily implement this navigation hierarchy by using managed navigation. The navigation term set contains the following terms, arranged hierarchically:
  
- Products
    
- Customer support
    
- About us
    
  - Company history
    
  - Press releases
    
  - Contact us
    
**Figure: Navigation term set driving navigation controls**

![Navigation term set driving navigation controls](../media/managed-nav-simple.gif)
  
You configure each term in the navigation term set to correspond to a page to display. If you create the pages before you create the navigation term set, you can even have the terms created automatically and the correspondence between terms and pages set up automatically. You can also customize the appearance of the controls themselves — for example, how many levels of the navigation hierarchy to display. To change the structure of your website, you can reorder terms in the navigation term set, and the navigation controls will automatically display the new structure.
  
Attributes of the terms influence the appearance and behavior of items in the navigation controls. For example, you can change the title of the "Customer support" term to "Customer assistance," and the navigation controls will use the new wording, but still display the same page when the user selects **Customer assistance**. You can modify attributes of navigation terms to control how the term is displayed, whether the term should be included in the global navigation control and the current navigation control, what text is displayed when a site visitor hovers over the term in a navigation menu, and so on.
  
### Catalogs and term-driven pages

Cross-site publishing is available only in SharePoint Server Enterprise. If your site uses cross-site publishing, then you can associate one or more tagging term sets with the publishing site. You specify which part of the tagging term set (on the authoring site) to add to the navigation term set (on the publishing site). For more information about cross-site publishing and tagging term sets, see [Overview of cross-site publishing in SharePoint Server](overview-of-cross-site-publishing.md).
  
You can add tagging terms either by pinning them or by reusing them. A pinned term is essentially a link. If you change the term in the tagging term set, the changes also apply to the pinned term in the navigation term set. You can pin only a term, or you can pin a term and all of its sub-terms. A reused term is essentially a copy. No association is maintained between the tagging term and the reused navigation term. 
  
Returning to the example, assume that the publishing site uses cross-site publishing. There is an authoring site that has a tagging term set with the following hierarchy of terms:
  
- Cameras
    
  - Digital
    
  - Film
    
- Computers
    
  - Laptop
    
  - Gaming
    
  - High-performance
    
  - Ultra-light
    
  - Slate
    
  - Desktop
    
- Printers
    
  - Inkjet
    
  - Laser
    
A list on the authoring site is used as a catalog of all available products. Items in the list are tagged with terms from the tagging term set.
  
If you pin the root of the tagging term set to the navigation term set, and modify the global navigation control to display two levels of navigation, then the global navigation menu will still display the following entries:
  
- Products
    
- Customer support
    
- About us
    
Furthermore, the **Products** menu item in the global navigation menu will expand to show the following menu items: 
  
- Cameras
    
- Computers
    
- Printers
    
If a visitor to the site selects the **Cameras** entry on the global navigation menu, then the current navigation control displays the following entries: 
  
- Digital
    
- Film
    
The navigation term set that represents this structure is the following:
  
- Products
    
  - Cameras
    
  - Digital
    
  - Film
    
  - Computers
    
  - Laptop
    
  - Gaming
    
  - High-performance
    
  - Ultra-light
    
  - Slate
    
  - Desktop
    
  - Printers
    
  - Inkjet
    
  - Laser
    
- Customer support
    
- About us
    
  - Company history
    
  - Press releases
    
  - Contact us
    
**Figure: Tagging term set driving navigation term set**

![Tagging term set driving navigation term set](../media/managed-nav-tagging.gif)
  
When a visitor to the site navigates to a node under **Products**, a page is automatically generated that shows the following information:
  
- If the term has sub-terms, the page displays sub-categories. For example, the page that corresponds to the term Cameras displays the categories for Digital and Film.
    
- If the term has no sub-terms, the page displays items that are tagged with the term. For example, the page that corresponds to the term Digital displays items that are tagged with "Digital."
    
You define the page that is generated by setting attributes on the term in the navigation term set. You can specify values for the following attributes for each term:
  
- **A friendly URL** The friendly URL is displayed in the browser's address bar when the user views the page. It is most likely a suffix that is appended to the parent term's friendly URL. For example, if the friendly URL for the Cameras term is "www.contoso.com/cameras," the friendly URL for the Film term could be "www.contoso.com/cameras/film." 
    
- **A target page** This is the page that loads when the friendly URL is accessed. A term can use the same target page as its parent term, or you can override the parent's target page and specify a different one. If you specify a new target page, you can also indicate that it should be used by all child terms of the current term (unless a child term overrides its parent's target page). 
    
- **A catalog item page** This is the page that is rendered when a site visitor views an item that is tagged with the term. For example, the target page for the Film term might display images and brief descriptions of all film cameras, whereas the catalog item page for the Film term would display an image of the specific camera that was selected, along with detailed product specifications. A term can use the same catalog item page as its parent term, or you can override the parent's catalog item page and specify a different one. If you specify a different catalog item page, you can also indicate that it should be used by all child terms of the current term (unless the child term overrides its parent's catalog item page). 
    
## Using terms in other term sets
<a name="section5"> </a>

When you use cross-site publishing, there are two ways to use terms from an authoring site collection as navigation terms in a publishing site collection: you can pin terms or reuse terms.
  
When you pin a term from a tagging term set in an authoring site collection into the site navigation of a publishing site collection, that term is shared with the navigation term set in the publishing site collection. Any changes that you make to the original term in the authoring site collection will be reflected anywhere that term is pinned. You can't change the general settings for a term in the publishing site collection where the term is pinned. You also can't add shared properties to the term from the publishing site collection. However, you can add local properties to the term. You can pin a single term, or you can pin a term with all its child terms.
  
When you reuse a term from a tagging term set in an authoring site collection into the site navigation of a publishing site, that term is copied to the navigation term set in the publishing site collection and no association with the original term is maintained. Any changes that you make to the original term in the authoring site collection are not made on any reused copies of the term. You can change the general settings for the reused term in the publishing site collection. You can also add both shared and local properties to the term from the publishing site collection. You can reuse a single term, or a term with all its child terms.
  
## Limitations of managed navigation in SharePoint Server
<a name="section6"> </a>

Because managed navigation uses term sets to build the site navigation, it has the same limitations as any other term set:
  
- There is no version control on terms. If you make a change to a term, you can't later revert the change back to an earlier version of the term.
    
- There is no publishing workflow on terms. As soon as you make a change to a term, it will appear in the navigation with the change. If you are using cross-site publishing, this also means that when a new term is added to the navigation term set, the term itself may be visible in the navigation on the publishing site before the associated content is indexed by search. You can choose to hide terms from the navigation until the content is published and indexed by search.
    
## See also
<a name="section6"> </a>

#### Concepts

[Plan navigation term sets in SharePoint Server](plan-navigation-term-sets.md)
  
[Plan for managed metadata in SharePoint Server](../governance/managed-metadata-planning.md)
  
[Overview of cross-site publishing in SharePoint Server](overview-of-cross-site-publishing.md)
  
[Plan authoring sites for cross-site publishing in SharePoint Server](plan-sharepoint-authoring-sites-for-cross-site-publishing.md)
  
[Plan publishing sites for cross-site publishing in SharePoint Server](plan-sharepoint-publishing-sites-for-cross-site-publishing.md)
  
[Estimate capacity and performance for Web Content Management (SharePoint Server 2013)](web-content-management-capacity-and-performance.md)
#### Other Resources

[Plan managed metadata (OLD)](/previous-versions/office/sharepoint-server-2010/ee530389(v=office.14))

