---
title: "Overview of publishing to Internet, intranet, and extranet sites in SharePoint Server"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.date: 7/24/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: a3ad4dea-36b2-48df-b699-8fd9725df53c
description: "Learn about SharePoint Server publishing, the kinds of SharePoint Server publishing sites, and the publishing methods available for SharePoint Server sites."
---

# Overview of publishing to Internet, intranet, and extranet sites in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
You can use the publishing features in SharePoint Server to create branded Internet, intranet, and extranet sites. However, some publishing features are available only in SharePoint Server 2016.
  
This article describes what is meant by publishing in the context of web content management (WCM) in SharePoint Server, and explains how to use publishing sites to benefit your organization. It includes a list of the major publishing components, introduces the types of publishing sites that are available, and explains the publishing methods that you can use for SharePoint Server publishing sites. For information about how to plan publishing sites, see [Plan for Internet, intranet, and extranet publishing sites in SharePoint Server](plan-for-internet-intranet-and-extranet-publishing-sites.md).
  
## What is publishing in SharePoint Server?
<a name="publishing"> </a>

WCM in SharePoint Server consists of features and functionality that you use to configure, customize, optimize, and publish site collections, sites, and pages. When we talk about publishing sites in SharePoint Server, we are referring to sites that use one or more of these features to author and deploy branded artifacts, content, and configuration files to Internet, intranet, and extranet sites.
  
## Use and benefits of SharePoint Server publishing sites
<a name="benefits"> </a>

You can use SharePoint Server publishing sites to create different types of branded sites, depending on your business needs and goals. The following list gives examples of how you can use SharePoint Server publishing sites:
  
- **Internet presence site** Provide information to customers, partners, investors, and potential employees. For example, you might use an Internet presence site to provide news articles or reviews that are tagged with metadata to categorize articles so that users can search or browse for information. 
    
- **Internet business site** Promote products and services that your company offers to customers. For example, you might use an Internet business site to show a catalog of products such as TVs, stereos, MP3 players, and mobile devices. 
    
- **Intranet sites** Deploy a site that has a tightly managed navigation structure to provide authored content to intranet readers. For example, you might use a published intranet site to provide human resources information to employees. 
    
- **Extranet sites** Provide access to targeted content to remote employees, partners, and customers. For example, you might use an extranet site to provide access to a knowledge base that uses authored content tagged with metadata to categorize articles so that users can search or browse for specific information, such as troubleshooting articles, support issues, and service packs. 
    
SharePoint Server publishing sites let you establish a branded, online identity for your company or organization. The benefits of using SharePoint Server publishing sites include the following:
  
- Brand consistency by using custom design assets, such as master pages and page layouts, edited in HTML and automatically converted into SharePoint resources.
    
- Tight control over site navigation.
    
- Decentralized content creation, which enables globally contributed content.
    
- Centralized publishing workflow and approval processes.
    
- Dynamic, customized sites.
    
## About SharePoint Server publishing features
<a name="pubfeatures"> </a>

Publishing in SharePoint Server consists of two separate features: the SharePoint Server Publishing Infrastructure feature, and the SharePoint Server Publishing feature. These features provide the core publishing functionality for SharePoint Server. The following list describes the major functionality that is enabled by the publishing features:
  
- **Site templates** By default, some site collection and site templates have the publishing feature enabled. You can enable publishing features for other kinds of site collections and sites. 
    
- **Special groups and permission levels** Special groups such as Approvers, Designers, and Hierarchy Managers are included, and permission levels such as Approve, Design, and Manage Hierarchy are added to the site collection to support tasks that compose the creation and publication of content. 
    
- **Navigation** The global navigation menu replaces the top link bar, and the managed navigation feature is enabled. 
    
- **Master pages, page layouts, and display templates** Master pages, page layouts, and display templates let you customize the overall behavior and appearance of your site. For more information, see [SharePoint page model overview](https://go.microsoft.com/fwlink/p/?LinkId=261548).
    
- **Design Manager and design packages** The Design Manager is a new interface and central hub for managing all aspects of branding your SharePoint site. It enables a step-by-step approach for creating design assets in the web development tool of your choice that you can use to brand sites. 
    
    After you finish designing your site, you can choose Export Package in the Design Manager to export a single .wsp file called a design package. When you export a design package, SharePoint Server automatically packages all of the contents that you have added or changed in the Master Page Gallery, Style Library, Theme Gallery, the Device Channels list, and Page content types into a design package. You can import the design package into another site, even if that site already has content. .
    
- **Device channels** By using device channels, you can target different designs to different devices (such as Windows Phone) or groups of devices (such as all smartphones). 
    
- **Site columns and content types** Special site columns such as **Page Content**, **Scheduling Start Date**, and **Scheduling End Date** are added to the site collection, and content types such as Page Layout, Article Page, and Enterprise Wiki Page are added to support creating content. 
    
- **Special Web Parts** Special Web Parts such as Content and Structure Reports, Content Search, Content Query, and Taxonomy Refinement Panel are added to support the display of publishing-related data. 
    
- **Pages library** The Pages library is used to store all web pages that are created in the site. 
    
- **Page editing menus** The page editing ribbon lets users quickly and easily author and manage their content. 
    
- **Approval workflow and scheduling** An approval workflow lets authors route their content for review and approval before it is published. Scheduling functionality lets authors specify when a piece of content should go live on the site, and when it should expire. 
    
- **Variations for multilingual sites** The variations feature lets you create multilingual content and target it to specific audiences on different sites by copying content from a source variation site to each target variation site. You can then use machine translation to translate page content, or you can package content for human translation. 
    
- **Caching** The object cache reduces the amount of traffic between the web server and the SQL database by storing objects — such as lists and libraries, site settings, and page layouts — in memory on the front-end web server. The page output cache stores the rendered output of a page and uses cache profiles that specify how long items should be held in the cache. The binary large object (BLOB) cache is a disk-based cache for caching items such as frequently used images, audio and video files, and other files that are used to display web pages, such as .css and .js files. 
    
## About SharePoint Server publishing site collection templates
<a name="pubsites"> </a>

SharePoint Server has three site collection templates that you can use to create a publishing site based on your site needs and goals: Publishing Portal, Product Catalog, and Enterprise Wiki. The following table describes each template.
  
**Publishing site collection templates**

|**Template**|**Description**|
|:-----|:-----|
|**Publishing Portal** <br/> |Use for an Internet site or a large intranet portal site. You can use distinctive branding to customize this site. Typically, this site has many more readers than contributors. By default, this site collection template enables content approval workflows for a more formal and controlled publishing process. It also lets you grant permissions to anonymous users to view only content pages. Anonymous users cannot view SharePoint Server administrative pages, such as the **Site Settings** page.  <br/> |
|**Enterprise Wiki** <br/> |A site in which your organization can publish knowledge that it accumulates and wants to share across the enterprise. It provides an easy content editing experience in a single location for co-authoring content, for discussions, and for collaborating on projects.  <br/> |
|**Product Catalog** <br/> |Use for managing library or list data that is shared as a catalog for cross-site collection publishing. Catalog data is published to an Internet-facing site by using Web Parts that use Search technology. The catalog can be configured to support catalog item variants and multilingual catalog item properties. The site includes administration pages for managing faceted navigation for catalog items.  <br/> |
   
In addition to using one of these established site collection templates, you can also turn on publishing for any non-publishing site by activating the SharePoint Server Publishing Infrastructure feature at the site collection level, and the SharePoint Server Publishing feature at the site level.
  
## Understanding SharePoint Server publishing methods
<a name="pubmodels"> </a>

SharePoint Server has two ways that you can make published content available to users: author-in-place and cross-site publishing. The following list summarizes these publishing methods.
  
- **Author-in-place** You use a single site collection to author content and make it available to readers of your site. Content is branded by using master pages and page layouts on the same site, and approval and publishing workflows are used to submit pages for approval and then publish them for readers. This was the primary publishing method that was available in SharePoint Server 2010. 
    
- **Cross-site collection publishing** You use one or more site collections to author content, and one or more site collections to control the design of the site and the display of the content. The authoring site collection is used to hold the source content, and can contain catalogs of Pages libraries and lists that are indexed by the search system, and made available to the publishing site collection. The publishing site collection takes the data from the authoring site collection and shows it on web pages by using the Content Search Web Part and the Catalog-Item Reuse Web Part. These Web Parts use configured queries to get data from the search index and show it on the site. Content is branded on the publishing site by using master pages, page layouts, and display templates. These let a designer control how data appears in the Content Search Web Part and the Catalog-Item Reuse Web Part. For more information, see [Overview of cross-site publishing in SharePoint Server](overview-of-cross-site-publishing.md).
    
## See also
<a name="pubmodels"> </a>

#### Concepts

[Plan for Internet, intranet, and extranet publishing sites in SharePoint Server](plan-for-internet-intranet-and-extranet-publishing-sites.md)
  
[Overview of cross-site publishing in SharePoint Server](overview-of-cross-site-publishing.md)
  
[Plan for cross-site publishing in SharePoint Server](plan-for-cross-site-publishing.md)
  
[Estimate capacity and performance for Web Content Management (SharePoint Server 2013)](web-content-management-capacity-and-performance.md)

