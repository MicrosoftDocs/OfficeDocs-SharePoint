---
title: "Plan authoring sites for cross-site publishing in SharePoint Server"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.date: 3/12/2018
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 47603b59-cf37-4778-803d-97c4ebd9b452
description: "Learn how to plan authoring site collections for a SharePoint Server cross-site publishing solution."
---

# Plan authoring sites for cross-site publishing in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
When you use cross-site publishing in SharePoint Server, you use one or more authoring site collections for authoring and storing content, and one or more publishing site collections to control the design of the site and show content. This article describes how to plan authoring sites for your cross-site publishing solution.
  
This article builds on the information in [Overview of cross-site publishing in SharePoint Server](overview-of-cross-site-publishing.md). After you finish reading this article, make sure that you read the next article, [Plan publishing sites for cross-site publishing in SharePoint Server](plan-sharepoint-publishing-sites-for-cross-site-publishing.md).
  
## Plan site collections and site structure for SharePoint authoring sites
<a name="BKMK_SiteStructure"> </a>

Authoring site collections must have the SharePoint Server Cross-Site Collection Publishing feature activated. We recommend that you use the Product Catalog Site Collection template to create authoring site collections because the Cross-Site Collection Publishing feature is activated by default when you use that template. If you use a site collection template that does not have the Cross-Site Collection Publishing feature activated, you must activate it. Additionally, if you use a site collection template, such as the Team Site template, that does not create a publishing site, and you want to use publishing features such as Approval workflows and scheduling, you must also activate those publishing features. For information about activating the Cross-Site Publishing feature, see "Activate the Cross-Site Collection Publishing feature" in [Configure cross-site publishing in SharePoint Server](configure-cross-site-publishing.md). For more information about how to use the publishing features on a site that is not a publishing site, see [Publishing features overview (SharePoint Server 2010)](https://go.microsoft.com/fwlink/p/?LinkID=402901). For information about how to activate the publishing features, see [Enable publishing features](https://go.microsoft.com/fwlink/p/?LinkId=261798). For more information about how to design the logical architecture for a cross-site publishing solution, see [Plan the logical architecture for cross-site publishing in SharePoint Server](plan-the-logical-architecture-for-cross-site-publishing.md).
  
Because cross-site publishing separates the authoring and publishing environments, the structure of an authoring site can differ from the structure of the publishing site. As you plan how to structure authoring sites, consider the questions in the following list.
  
- **Should you use a Pages library or a list for content?**
    
    In SharePoint Server 2010, publishing sites used Pages libraries to store HTML content that was shown to users. By using cross-site publishing in SharePoint Server, you can also use lists and other libraries to store the content that is reused on the publishing sites. When you plan for where you can store this content, consider what the content is and how you plan to use it. In general, if you plan to author HTML content, we recommend that you use a Pages library instead of a list. A Pages library has the following benefits over a list:
    
  - You can create a more WYSIWYG environment for authoring pages to give authors an idea of how their content will appear on the publishing site.
    
  - You can use variations and translation with a Pages library to create multilingual content.
    
  - You can use the Approval workflow to route Pages library content for review and approval. The search system will not index pages that are not approved for publishing because they are not marked as major versions until they are published.
    
  - You can use scheduling to specify when content will be available. The search system will not index pages that have not been scheduled for publishing. This is because pages are not marked as major versions until they are published.
    
- **How many Pages libraries do you have to have?**
    
    The primary drawback to using a Pages library is that you can have only one Pages library per site. Depending on how much Pages content you plan to create, a single, large catalog can be difficult to consume on publishing sites because the queries that show content are more complex and time-consuming to configure. Accordingly, when you plan Pages content, consider how much content you will create and whether the content should be stored together. If you want to store Pages content in separate catalogs, you must create separate sites within the authoring site collection hierarchy, and then share the Pages library in each site as a catalog. You can then connect to these catalogs from one or more publishing sites.
    
    For example, in an intranet scenario in which you have a knowledge base site, you might want to keep troubleshooting articles separate from user manuals because they are authored by different groups of people. In the authoring site collection, you create one site to store troubleshooting articles in its Pages library, and another site to store user manuals in its Pages library. After you share both Pages libraries as catalogs, you can connect to them both from the same publishing site, and show the two types of content by using different Web Parts.
    
- **How many authoring site collections do you have to have?**
    
    In addition to deciding how many sites you must have in a single authoring site collection, you should also consider whether you have to have additional authoring site collections. You might use more than one authoring site collection if the content authors are in separate groups that have different security requirements, or are in separate geographical locations. For example, in an extranet scenario, you might use one authoring site collection for internal content authors who belong to a specific group in Active Directory Domain Services (AD DS), and a separate authoring site collection for external content authors who connect to the site by using forms-based authentication. Catalogs can be shared across web applications and farms so that you do not have to restrict authoring sites to a single web application or farm. Decide how many authoring site collections you must have, and then plan which catalogs to include in each site.
    
- **Do you plan to use variations to create multilingual content?**
    
    Do you have to provide content in more than one language? Even if you currently plan to only create and publish content in a single language, consider whether that business requirement might change in the future. If you might eventually want to use variations on the site, you should plan for using variations now. By setting up the site structure now to accommodate variations, you can save yourself and your organization time and resources in the future. If you have to change the site structure when you switch to using variations later, it is often more difficult and can affect the URLs that you planned for your sites. If you plan to use variations and cross-site publishing, each variation label has to be created as a separate site within the authoring site collection. You share the Pages library from each variation site as a catalog, and then you connect each publishing site collection to the catalog that matches its locale. For more information about variations, see [Variations overview in SharePoint Server](variations-overview.md). For more information about how to plan variation sites, see [Plan variations for multilingual cross-site publishing site in SharePoint Server](plan-variations-for-multilingual-cross-site-publishing-site.md).
    
- **What kind of navigation do you have to have on the authoring site?**
    
    Although you can use managed navigation on the authoring site so that the authoring site resembles the publishing site, this can confuse content authors. We recommend that you use structured navigation on the authoring site to make it easier for authors to create content. Consider the kind of content that will be created and stored on the authoring site. Will most content be HTML content that is stored in the Pages library? Or will you manually create or import list data? If you keep a simple structure for the authoring site and any lists and libraries, it makes it easier for content authors to create content.
    
## Plan security for SharePoint authoring sites
<a name="BKMK_Security"> </a>

You plan security for authoring sites in the same way that you do for most other sites in SharePoint Server. Consider the following questions:
  
- Who should have permissions to create the different kinds of content that is contained within the authoring site?
    
- Who should have permissions to create Pages content?
    
- Can the same group of people also create list content, or is a separate group responsible for that content?
    
- If you plan to use the Approval workflow, who should be included in the Approvers group? 
    
For information about security, see [Permissions planning for sites and content in SharePoint Server](../sites/permissions-planning-for-sites-and-content.md).
  
When you enable anonymous access for a catalog, security on the authoring site can be treated independently from how it is represented in search. When anonymous access is enabled, indexed content is searchable and viewable to anonymous users on the publishing site. However, if you change permissions to individual items in the catalog, those permissions are respected by the search system, and any items that are restricted to certain groups will not be available to anonymous users. This allows for greater flexibility when you plan to share content with anonymous users.
  
You must also plan to grant the crawler access to content on authoring site collections. The crawler uses a default content access account. If the default content access account does not have at least Read permission level to content, the content is not indexed and is not available to queries on publishing site collections. You can use the default content access account, or you can use crawl rules to specify a different content access account to use when crawling particular content. For more information, see "Plan crawler authentication" in [Plan crawling and federation in SharePoint Server](../search/plan-crawling-and-federation.md).
  
## Plan design and branding for SharePoint authoring sites
<a name="BKMK_Design"> </a>

As was mentioned earlier in this article, the structure of the authoring sites can differ from the structure of publishing sites. Likewise, the appearance of those sites can also be very different. If you want content authors to have a WYSIWYG user experience on the authoring site, you can use similar master pages, page layouts, and cascading style sheets to design the authoring site. However, the actual publishing sites might have different designs because of branding or other requirements. Therefore, the authoring site will not provide a complete WYSIWYG experience.
  
Even if you do not plan to apply the same branding to the authoring site that you use on the publishing site, if you plan to use Pages library content, you still have to plan for the basic page layouts that authors will use. As you plan the design of the authoring site, consider the following questions: 
  
- **What site columns must you have?** Site columns can be added as page fields to page layouts to hold additional content, such as managed metadata. 
    
- **What content types must you have?** You can create custom content types that use the Article Page content type as the parent content type. You can add site columns to the custom content type, which will be included as page fields in any page layouts that you create by using the custom content type. 
    
- **Can you use the default master page?** You might use the default master page, or create a new master page to use on the authoring site. 
    
- **What page layouts must you have?** You can create custom page layouts that contain specific page fields. For example, in an intranet scenario in which you have a knowledge base, you might create separate page layouts for troubleshooting guides and user manuals. 
    
For information about authoring web pages, see [SharePoint page model overview](https://go.microsoft.com/fwlink/p/?LinkId=261548), [Plan content types and workflows in SharePoint 2013](/previous-versions/office/sharepoint-server-2010/cc262735(v=office.14)), [Plan Web pages (SharePoint Server 2010)](https://go.microsoft.com/fwlink/p/?LinkId=402907) and [Plan Web page authoring (SharePoint Server 2010)](https://go.microsoft.com/fwlink/p/?LinkId=402906).
  
## Plan term sets for tagging content on SharePoint authoring sites
<a name="BKMK_PlanTaggingTermSetsForAuthoringSites"> </a>

You use term sets to tag catalog content such as pages or list items on the authoring site. By doing this, terms help categorize the content into a hierarchy. These same terms are later used on the publishing site to issue queries, show information about category and catalog item pages, create friendly URLs, and for managed navigation. When you plan the term sets and terms to use for tagging content, consider how you want the hierarchy structured. You can combine terms from more than one tagging term set into a single customized term set for navigation on the publishing site. You do not have to create a single, highly complex structure for the tagging term set on the authoring site. Also consider how you want the URLs to look on the publishing site, and plan to create terms that will help users find what they want. For example, if you have a level 1 term called Computers, and underneath that, a level 2 term called Laptops, and the catalog item name is CM61438, the friendly URL for the page that shows that model will be http://contoso.com/computers/laptops/CM61428. For more information, see [Plan terms and term sets in SharePoint Server 2013](/previous-versions/office/sharepoint-server-2010/ee519604(v=office.14)), and [Plan navigation term sets in SharePoint Server](plan-navigation-term-sets.md).
  
For information about creating term sets for tagging content, see "Create and manage term sets for tagging content on authoring sites" in [Configure cross-site publishing in SharePoint Server](configure-cross-site-publishing.md).
  
## Plan catalog content for SharePoint authoring sites
<a name="BKMK_catalogcontent"> </a>

Catalogs contain the content that is reused across site collections. You can use HTML content in a Pages library, data in a list, or assets such as pictures and video in an asset library. For example, in an Internet business scenario, you might use a list to show a catalog of products, or in an intranet scenario, you might use a Pages library to show a catalog of knowledge base articles. In either example, you might also have assets that you want to associate with content, such as pictures of products or videos that explain troubleshooting steps. This section describes how to plan for different kinds of catalog content in an authoring site.
  
For information about how to enable a library or list as a catalog, see "Share a library or list as a catalog" in [Configure cross-site publishing in SharePoint Server](configure-cross-site-publishing.md).
  
### Plan Pages libraries

After you decide whether to store content in one or more Pages libraries, and how to divide content between them, consider the following questions:
  
- **What term set will you associate with Pages library content?**
    
    If you use a Pages library, you must plan to add at least one managed metadata site column to a Page Layout Content Type, and link the site column to a tagging term set. When a content author creates a new page that uses that content type, they will be able to select a term with which to tag the page. For example, in the intranet knowledge base scenario, you might have a tagging term set that is named Article Types that contains separate terms for Troubleshooting Guides and for User Manuals. You can create a site column called Article Type that is linked to the Article Types term set, and add it to the Article Page content type. When a content author creates a new page, they must choose a term from the list of available Article Types terms. When the Pages library is shared as a catalog, you have to select that managed metadata column as the one to use as a navigation term set on the publishing sites. For more information, see [Plan term sets for tagging content on SharePoint authoring sites](plan-sharepoint-authoring-sites-for-cross-site-publishing.md#BKMK_PlanTaggingTermSetsForAuthoringSites) earlier in this article. 
    
- **What other fields must you add to the Page Layout Content Type?**
    
    In addition to planning the tagging field for navigation, you should consider any other fields that you want to add to a Page Layout Content Type. These can be other managed metadata fields that are linked to other term sets, or other kinds of fields, such as hyperlinks, numbers, and dates and times. By default, publishing page content types contain a Page Content field. This lets content authors insert HTML and images onto a page by using a rich text editor. You can create different page layouts that contain different fields, based on the content that is created. For example, in the intranet knowledge base scenario, you can use a page layout for Troubleshooting Articles that contains fields such as Applies To or Article Number, whereas you can use a page layout for User Manuals that contains fields such as Product Name or Model Number. As you plan Pages library content, decide what other site columns and content types are needed, what page layouts are needed, and which fields should go in which page layout. For more information, see [SharePoint page model overview](https://go.microsoft.com/fwlink/p/?LinkID=261548).
    
For more information, see [Plan Web pages (SharePoint Server 2010)](https://go.microsoft.com/fwlink/p/?LinkId=402907), and [Plan for large Pages libraries (SharePoint Server 2010)](https://go.microsoft.com/fwlink/p/?LinkId=402908).
  
### Plan list content
<a name="BKMK_PlanListContent"> </a>

When you plan to use lists to maintain catalog content, consider the following questions:
  
- **How many lists do you want to use?**
    
    Depending on the structure of the data, consider using several lists for creating and maintaining catalog content. You should consider using several lists when the attributes that are used to represent catalog items vary greatly between the different categories of data. For example, attributes representing washing machines are very different from the attributes representing MP3 players. In this case, consider creating one list for washing machines, and another list for MP3 players.
    
- **Which site columns do you have to have to represent the catalog items?**
    
    When you create and maintain catalog content in SharePoint lists, an item in the list represents a single catalog item — for example, a single product or a specific event. The different items have attributes to represent properties of the items, such as brand, color, and size for products, or date, time, and place for events. To add these attributes in the list, you have to create site columns that represent the different attributes, such as Brand, Color, Weight, Date, Time, and Place.
    
    When you plan the site columns that you want to represent the catalog content, consider both what you want to show, and how the different catalog items appear on the publishing site. You don't have to show all site columns from the list on a publishing site. However, you can use the information from all site columns to sort how catalog items must appear. For example, you can use the data in a site column named Amount in stock to sort catalog items so that the items with the greatest amount in stock appear in a prominent place.
    
    > [!IMPORTANT]
    > We recommend that you create site columns and not list columns. Managed properties are automatically created for site columns, taxonomy columns, and indexed list columns. Also be aware that all automatically created managed properties are of the text data type. For more information, see [Automatically created managed properties in SharePoint Server](../technical-reference/automatically-created-managed-properties-in-sharepoint.md). 
  
- **What content types do you want for lists?**
    
    If you have several lists, we recommend that you create a content type for each list, and then associate the appropriate site columns to this content type.
    
- **What term set do you want to use for each list that you will share as a catalog?**
    
    As described in [Plan term sets for tagging content on SharePoint authoring sites](plan-sharepoint-authoring-sites-for-cross-site-publishing.md#BKMK_PlanTaggingTermSetsForAuthoringSites) earlier in this article, you use term sets to categorize the catalog content into a hierarchy. To use tagging term sets for list content, you must have a site column that is a Managed Metadata data type, and is connected to the tagging term set. 
    
- **Is the data that you will input into a list consistent?**
    
    You should also plan a strategy to make sure that catalog list data is consistent. Catalog list data is often maintained by different people over a long time, and this can increase the inconsistency of the data. For example, let's say that you have a site column named Color, and you want to import the color information for individual items from an external system. The values in the external system vary in how the color is written (BLUE, Blue, blue). Before you import this data into a SharePoint list, make sure that the data is consistent. For this example, you make sure that all color names are represented as Blue.
    
    In addition to guaranteeing data consistency, you should also make sure that the managed metadata field that is used to tag catalog content is a required field. Missing data from this field may cause content to appear incorrectly on the publishing site.
    
For information about how to create list content for cross-site publishing, see "Create catalog content by using SharePoint lists" in [Configure cross-site publishing in SharePoint Server](configure-cross-site-publishing.md).
  
#### Plan to use the Product Catalog site collection

The Product Catalog Site Collection template is intended to be used to create sites in which to author, store and maintain any type of data that is used in a catalog scenario. The site collection template includes a Product Catalog list template that is optimized for maintaining catalog content in a list. By default, when you create a Product Catalog site collection, a Products list based on the Product Catalog list template is automatically created. The Products list is preconfigured with the Product with Image content type. The Product with Image content type has site columns associated with it, as described in the following table. 
  
**Site columns in the Product with Image content type**

|**Site column name**|**Site column type**|
|:-----|:-----|
|Title  <br/> |Single line of text  <br/> |
|Item Number  <br/> |Single line of text  <br/> |
|Group Number  <br/> |Single line of text  <br/> |
|Language Tag  <br/> |Choice  <br/> |
|Rollup Image  <br/> |Publishing Image  <br/> |
|Item Category  <br/> |Managed Metadata  <br/> |
   
In addition, a term set named Product Hierarchy is created. This term set is associated with the Item Category site column.
  
For performance considerations, see [Designing large lists and maximizing list performance (SharePoint Server 2010)](/previous-versions/office/sharepoint-server-2010/cc262813(v=office.14)).
  
### Plan asset library content
<a name="BKMK_PlanListContent"> </a>

When you plan to use assets in content, remember what is and is not indexed. The search system indexes some fields, such as text and HTML fields, but does not index assets such as pictures, audio and video files, and files such as Word documents or PDFs. These files are considered binary large objects (BLOBs), and are stored in the BLOB cache, not in the search index. This means that they will not be shown on the publishing site in the same manner as other content. As you plan the asset library content for authoring sites, consider the questions in the following list.
  
- **Where should the asset library be located?**
    
    To use assets in content, authoring site collections and publishing site collections must have access to the asset library. The location of the asset library depends on the kind of site that you want to create, and the solution architecture. If the users of the publishing site can have Read permission level on the authoring site collection, the asset library can be stored on the authoring site collection. However, if users on the publishing site cannot have Read permission level on the authoring site collection, the asset library must be created on a separate site collection with different permission levels. For example, in an Internet scenario in which users on the publishing site have only anonymous access, the asset library should be stored on a separate site collection, in a separate web application that is configured to allow anonymous access. However, in an intranet scenario in which users on the publishing site can have read access, the asset library can be stored in the authoring site collection. When the asset library is stored in a site collection separate from both the authoring and publishing sites, make sure that you add it to the list of Suggested Browser Content Locations for the authoring site so content authors can find and insert items from the asset library into their content. If you plan to use image renditions with the asset library, renditions must be enabled and configured on the site collection that hosts the images.
    
- **Does the asset library have to be shared as a catalog?**
    
    If the assets to be stored in the asset library are tagged with terms from a tagging term set, and you want to be able to query assets based on those terms, you can share the asset library as a catalog. For example, if you have one or more publishing sites that you want to show pictures or videos based on certain categories, the libraries that contain those assets must be shared as catalogs. If you want to allow anonymous users on the publishing site, make sure the asset library is accessible to anonymous users.
    
- **Where will assets be cached?**
    
    When you plan to use assets in content, also plan for where the asset files will be cached. In general, always enable the BLOB cache for publishing sites. The BLOB cache improves web site performance by retrieving BLOB files from the database and storing them in a directory on the front-end web server where they are served to users. This reduces the network traffic to and load on the database server. For more information, see [Plan for caching and performance in SharePoint Server](caching-and-performance-planning.md).
    
- **How big are the asset files?**
    
    If you plan to use very large files such as videos in content, you should plan to increase the maximum upload file size on the server where the asset library is located. This will allow you to upload files that are larger than the default setting permitted by SharePoint Server. For more information about the BLOB cache, bit-rate throttling, and maximum upload file size, see [Plan for caching and performance in SharePoint Server](caching-and-performance-planning.md).
    
For more information about how to plan for asset libraries, see [Plan digital asset libraries in SharePoint Server 2013](../sites/plan-digital-asset-libraries.md).
  
## See also
<a name="BKMK_catalogcontent"> </a>

#### Concepts

[Overview of publishing to Internet, intranet, and extranet sites in SharePoint Server](overview-of-publishing-to-internet-intranet-and-extranet-sites.md)
  
[Plan for Internet, intranet, and extranet publishing sites in SharePoint Server](plan-for-internet-intranet-and-extranet-publishing-sites.md)
  
[Plan for cross-site publishing in SharePoint Server](plan-for-cross-site-publishing.md)
  
[Overview of cross-site publishing in SharePoint Server](overview-of-cross-site-publishing.md)
  
[Plan the logical architecture for cross-site publishing in SharePoint Server](plan-the-logical-architecture-for-cross-site-publishing.md)
  
[Plan publishing sites for cross-site publishing in SharePoint Server](plan-sharepoint-publishing-sites-for-cross-site-publishing.md)
  
[Plan search for cross-site publishing sites in SharePoint Server 2016](plan-search-for-sharepoint-cross-site-publishing-sites.md)
  
[Configure cross-site publishing in SharePoint Server](configure-cross-site-publishing.md)
  
[Estimate capacity and performance for Web Content Management (SharePoint Server 2013)](web-content-management-capacity-and-performance.md)

