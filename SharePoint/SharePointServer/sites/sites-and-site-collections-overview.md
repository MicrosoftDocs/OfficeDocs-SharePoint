---
title: "Overview of sites and site collections in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
- SharePoint_Online
ms.assetid: 462e12d6-1a5d-4b7c-a0d5-14c551262be1
description: "Learn about site collections, sites, and site templates in SharePoint Server."
---

# Overview of sites and site collections in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
A site collection is made up of one top-level site and all sites below it. As shown in the following figure, it is the top level of organization in a SharePoint Server web application. The number of site collections you can have in a single web application depends on the capacity of your server infrastructure. For more information about SharePoint Server boundaries, see [Software boundaries and limits for SharePoint Servers 2016 and 2019](../install/software-boundaries-and-limits-0.md).
  
**Figure: Structure of a site collection in SharePoint Server 2016**

![Diagram of a site collection](../media/DiagramOfSiteCollection.gif)
  
The SharePoint Server 2019 modern experience is similar to the experience in SharePoint Online. The main difference is Hub sites aren't available in SharePoint Server. We do recommend that you use the same process as in SharePoint Online, create site collections for each unit of work instead of creating subsites. This will make it easier when migrating your SharePoint farm to SharePoint Online.

The following guidelines show the relationship between SharePoint Server sites and site collections, and content databases:
  
- All content in a site collection must be stored in a single content database. You can't store a site collection's content across multiple content databases.
    
- You can scale up content databases that support a site collection. You can also scale-out a content database at the web application level to support additional site collections.
    
- A site collection can exist in only one content database, but one content database can host the content for multiple site collections.
    
- A site can't exist outside of a site collection and can only exist in one site collection but a site collection can host many sites.
    
    
## Overview of SharePoint site collections
<a name="section1"> </a>

You create a site collection to host sites that have something in common. For example, the sites might be in a common administrative boundary or share common branding. The site collection might be created to house all the sites and content for a business unit. Or, a single site collection might have become too large to manage, and it must be split into smaller ones. Lastly, some site collections are created exclusively to host specific SharePoint Server functionality, such as Enterprise Search Center or to host My Sites. Site collections are a way of organizing sites for a common purpose. We recommend ahat you create site collections for each unit of work instead of creating subsites.
  
SharePoint Server supports two types of site collections: host-named site collections and path-based site collections. In a path-based site collection, all the subsites in the site collection will share a root or parent URL (DNS name). For example, Team A could have a site collection at http<!-- nolink -->://contoso.com/sites/teamA, and Team B would have a site collection at http<!-- nolink -->://contoso/sites/teamB. All sites in either site collection would have the http<!-- nolink -->://contoso.com/sites/teamA or /teamB root. The only way to have a different URL root is to create a different web application.
  
To better align with SharePoint Online best practices, you should use host-named site collections. Host-named site collections allow you to assign custom names to each site collection that you create in a web application. For example, you can have two site collections in the same web application addressed like this: http<!-- nolink -->://TeamA.contoso.com and http<!-- nolink -->://TeamB.contoso.com. This is much more scalable and has been heavily tested in SharePoint Online.
  
Because site collections and sites exist in a parent-child relationship, there are aspects of control and functionality that can be configured at the site collection level and used at the site level. This provides many benefits as follows:
  
- For site designers, a site collection's galleries and libraries (such as the Master Page Gallery or the Site Collection Images library) provide a means for creating a unified, branded user experience across all sites in the site collection.
    
- For site collection administrators, a site collection provides a unified mechanism and scope for administration. For example, security, policies, and features can be managed for a whole site collection; Site Collection Web Analytics Reports, audit log reports, and other data can help administrators track site collection security and performance.

  SharePoint Server 2019 offers the choice to create modern Team and Communication sites like in SharePoint Online, or keep the classic experience. Using the modern experience site collections is inline with our recommendation to create site collections for each unit of work to make it easier when you decide to migrate to SharePoint Online.     
    
- For farm administrators, site collections can be moved between content databases. By doing this, farm administrators can manage the size of their content databases.
    
- For site authors, shared site columns, content types, web parts, authoring resources, workflows, and other site collection features provide a consistent authoring environment.
    
- For site users, a site collection's unified navigation, branding, and search tools provide a unified website experience.
    
Every site collection starts as a single, top-level site. Because it is a site, its structure and functionality is based on a site template. SharePoint Server provides many site templates, plus you can also create and use your own as needed. The following tables describe the site collection templates that are available in SharePoint Servers 2016 and 2019.
  
**Table: Site templates in SharePoint Servers 2016 and 2019**

|**Type**|**Name**|**Description**|**Availability**|
|:-----|:-----|:-----|:-----|
|**Collaboration** <br/> |Team Site  <br/> |A place to work together with a group of people.  <br/> **SharePoint Server 2019** offers a modern and classic team site.  <br/> |Site collection and site  <br/> |
|**Collaboration** <br/> |Blog  <br/> |A site for a person or team to post ideas, observations, and expertise that site visitors can comment on.  <br/> |Site collection and site  <br/> |
|**Collaboration** <br/> |Developer Site  <br/> |A site for developers to build, test, and publish apps for Office.  <br/> |Site collection only  <br/> |
|**Collaboration** <br/> |Project Site  <br/> |A site for managing and collaborating on a project. This site template brings all status, communication, and artifacts relevant to the project into one place.  <br/> |Site collection and site  <br/> |
|**Collaboration** <br/> |Community Site  <br/> |A place where community members discuss topics of common interest. Members can browse and discover relevant content by exploring categories, sorting discussions, by popularity or by viewing only posts that have a best reply. Members gain reputation points by participating in the community, such as starting discussions and replying to them, liking posts, and specifying best replies.  <br/> |Site collection and site  <br/> |
|**Enterprise** <br/> |Document Center  <br/> |A site to centrally manage documents in your enterprise.  <br/> |Site collection and site  <br/> |
|**Enterprise** <br/> |In-Place Hold Policy Center  <br/> |A site to manage policies to preserve content for specific amounts of time.  <br/> |Site collection only  <br/> |
|**Enterprise** <br/> |eDiscovery Center  <br/> |A site to manage the preservation, search, and export of content for legal matters and investigations.  <br/> |Site collection only  <br/> |
|**Enterprise** <br/> |Records Center  <br/> |This template creates a site designed for records management. Records managers can configure the routing table to direct incoming files to specific locations. The site also lets you manage whether records can be deleted or modified after they are added to the repository.  <br/> |Site collection and site  <br/> |
|**Enterprise** <br/> |Business Intelligence Center  <br/> |A site for presenting Business Intelligence content.  <br/> |Site collection and site  <br/> |
|**Enterprise** <br/> |Compliance Policy Center  <br/> |A site to manage policies and delete documents after specified times.  <br/> |Site collection and site  <br/> |
|**Enterprise** <br/> |Enterprise Search Center  <br/> |A site focused on delivering an enterprise-wide search experience.  <br/> **Note:** <br/> Search Centers should be separate site collections because they search for information across a company portal or division. If you create a Search Center as a subsite, you might have to create some workarounds for a full customization. For more information, see [Customizing the Search Center](https://go.microsoft.com/fwlink/p/?LinkID=194624&amp;clcid=0x409).  <br/> |Site collection and site  <br/> |
|**Enterprise** <br/> |My Site Host  <br/> |A site used for hosting personal sites (My Sites) and the public People Profile page.  <br/> |Site collection only  <br/> |
|**Enterprise** <br/> |Community Portal  <br/> |A site for discovering communities.  <br/> |Site collection only  <br/> |
|**Enterprise** <br/> |Basic Search Center  <br/> |A site focused on delivering a basic search experience. It includes a welcome page with a search box that connects users to a search results page and an advanced search page. This Search Center will not appear in navigation.  <br/> **Note:** <br/> Search Centers should be separate site collections because they search for information across a company portal or division. If you create a Search Center as a subsite, you might have to create some workarounds for a full customization. For more information, see [Customizing the Search Center](https://go.microsoft.com/fwlink/p/?LinkID=194624).  <br/> |Site collection and site  <br/> |
|**Enterprise** <br/> |Visio Process Repository  <br/> |A site for viewing, sharing, and storing Visio process diagrams. It includes a versioned document library and templates for Basic Flowcharts, Cross-functional Flowcharts, and BPMN diagrams.  <br/> **Note:** <br/> The Visio Process Repository site template will be removed in the next version of SharePoint Server.  <br/> |Site collection and site  <br/> |
|**Publishing** <br/> |Publishing Portal  <br/> |A starter hierarchy for an Internet-facing site or a large intranet portal. This site can be customized easily with distinctive branding. Typically, this site has many more readers than contributors and it is used to publish web pages with approval workflows.  <br/> |Site collection only  <br/> |
|**Publishing** <br/> |Enterprise Wiki  <br/> |A site for publishing knowledge that you capture and want to share across the enterprise.  <br/> |Site collection and site  <br/> |
|**Publishing** <br/> |Product Catalog  <br/> |A site for managing product catalog data that can be published to an Internet-facing site through search.  <br/> |Site collection only  <br/> |
|**Publishing** <br/> |Communication Site  <br/> |Available in SharePoint Server 2019 only as a modern experience. A site for publishing dynamic, modern content to people in your organization to keep them informed and engaged on topics, events, or projects.  <br/> |Site collection only  <br/> |
|**Custom** <br/> |\<Select template later…\>  <br/> |Create an empty site and pick a template for the site at a later time.  <br/> |Site collection only  <br/> |
   
The following table describes the 2013 experience version site templates that are available in SharePoint 2013.
  
**Table: 2013 experience version site templates in SharePoint 2013**

|**Type**|**Name**|**Description**|**Availability**|
|:-----|:-----|:-----|:-----|
|**Collaboration** <br/> |Team Site  <br/> |A place to work together with a group of people.  <br/> |Site collection and site, Server and Foundation  <br/> |
|**Blog** <br/> ||A site for a person or team to post ideas, observations, and expertise that site visitors can comment on.  <br/> |Site collection and site, Server and Foundation  <br/> |
|**Develop Site** <br/> ||A site for developers to build, test, and publish apps for Office.  <br/> |Site collection and site, Server and Foundation  <br/> |
|**Project Site** <br/> ||A site for managing and collaborating on a project. This site template brings all status, communication, and artifacts relevant to the project into one place.  <br/> |Site collection and site, Server only  <br/> |
|**Community Site** <br/> ||A place where community members discuss topics of common interest. Members can browse and discover relevant content by exploring categories, sorting discussions, by popularity or by viewing only posts that have a best reply. Members gain reputation points by participating in the community, such as starting discussions and replying to them, liking posts, and specifying best replies.  <br/> |Site collection and site, Server only  <br/> |
|**Enterprise** <br/> |Document Center  <br/> |A site to centrally manage documents in your enterprise.  <br/> |Site collection and site, Server only  <br/> |
|**eDiscovery Center** <br/> ||A site to manage the preservation, search, and export of content for legal matters and investigations.  <br/> |Site collection only, Server only  <br/> |
|**Records Center** <br/> ||This template creates a site designed for records management. Records managers can configure the routing table to direct incoming files to specific locations. The site also lets you manage whether records can be deleted or modified after they are added to the repository.  <br/> |Site collection and site, Server only  <br/> |
|**Business Intelligence Center** <br/> ||A site for presenting Business Intelligence content.  <br/> |Site collection and site, Server only  <br/> |
|**Enterprise Search Center** <br/> ||A site focused on delivering an enterprise-wide search experience.  <br/> **Note:** <br/> Search Centers should be separate site collections because they search for information across a company portal or division. If you create a Search Center as a subsite, you might have to create some workarounds for a full customization. For more information, see [Customizing the Search Center](https://go.microsoft.com/fwlink/p/?LinkID=194624&amp;clcid=0x409) in the MSDN Library.  <br/> |Site collection and site, Server only  <br/> |
|**My Site Host** <br/> ||A site used for hosting personal sites (My Sites) and the public People Profile page.  <br/> |Site collection only, Server only  <br/> |
|**Community Portal** <br/> ||A site for discovering communities.  <br/> |Site collection only, Server only  <br/> |
|**Basic Search Center** <br/> ||A site focused on delivering a basic search experience. It includes a welcome page with a search box that connects users to a search results page and an advanced search page. This Search Center will not appear in navigation.  <br/> **Note:** <br/> Search Centers should be separate site collections because they search for information across a company portal or division. If you create a Search Center as a subsite, you might have to create some workarounds for a full customization. For more information, see [Customizing the Search Center](https://go.microsoft.com/fwlink/p/?LinkID=194624) in the MSDN Library.  <br/> |Site collection and site, Server and Foundation  <br/> |
|**Visio Process Repository** <br/> ||A site for viewing, sharing, and storing Visio process diagrams. It includes a versioned document library and templates for Basic Flowcharts, Cross-functional Flowcharts, and BPMN diagrams.  <br/> **Note:** <br/> The Visio Process Repository site template will be removed in the next version of SharePoint Server.  <br/> |Site collection and site, Server only  <br/> |
|**Publishing** <br/> |Publishing Portal  <br/> |A starter hierarchy for an Internet-facing site or a large intranet portal. This site can be customized easily with distinctive branding. Typically, this site has many more readers than contributors and it is used to publish web pages with approval workflows.  <br/> |Site collection only, Server only  <br/> |
|**Enterprise Wiki** <br/> ||A site for publishing knowledge that you capture and want to share across the enterprise.  <br/> |Site collection and site, Server only  <br/> |
|**Product Catalog** <br/> ||A site for managing product catalog data that can be published to an Internet-facing site through search.  <br/> |Site collection only, Server only  <br/> |
|**Blank** <br/> |Publishing site  <br/> |A blank site for expanding your website and quickly publishing web pages. Contributors can work on draft versions of pages and publish them to make them visible to readers. The site includes document and image libraries for storing web publishing assets.  <br/> |Site only, Server only  <br/> |
||Publishing Site with workflow  <br/> |A site for publishing web pages on a schedule by using approval workflows. It includes document and image libraries for storing web publishing assets. By default, only sites with this template can be created under this site.  <br/> |Site only, Server only  <br/> |
|**Custom** <br/> |\<Select template later…\>  <br/> |Create an empty site and pick a template for the site at a later time.  <br/> |Site collection only, Server and Foundation  <br/> |
   
The following table describes the 2010 experience version site templates that are available in SharePoint 2013.
  
**Table: 2010 experience version site templates in SharePoint 2013**

|**Type**|**Name**|**Description**|**Availability**|
|:-----|:-----|:-----|:-----|
|Collaboration  <br/> |Team Site  <br/> |Same functionality as the 2013 Team site.  <br/> |Site collection and site, Server and Foundation  <br/> |
|Blank Site  <br/> |A blank site for you to customize based on your requirements.  <br/> |Site collection and site, Server and Foundation  <br/> |Site collection and site, Server and Foundation  <br/> |
|Document Workspace  <br/> |A site for colleagues to work together on a document. It provides a document library for storing the primary document and supporting files.  <br/> |Site collection and site, Server and Foundation  <br/> |Site collection and site, Server and Foundation  <br/> |
|Blog  <br/> |Same functionality as the 2013 Blog site.  <br/> |Site collection and site, Server and Foundation  <br/> |Site collection and site, Server and Foundation  <br/> |
|Group Work Site  <br/> |This template provides a groupware solution that enables teams to create, organize, and share information. It includes a Group Calendar, Circulation, Phone-Call Memo, a document library, and other basic lists.  <br/> |Site collection and site, Server and Foundation  <br/> |Site collection and site, Server and Foundation  <br/> |
|Visio Process Repository  <br/> |Same functionality as the 2013 Visio Process Repository.  <br/> |Site collection and site, Server only  <br/> |Site collection and site, Server and Foundation  <br/> Site collection and site, Server and Foundation  <br/> |
|Meetings  <br/> |Basic Meeting Workspace  <br/> |A site to plan, organize, and capture the results of a meeting. It provides lists for managing the agenda, meeting attendees, and documents.  <br/> |Site collection and site, Server and Foundation  <br/> |
|Blank Meeting Workspace  <br/> |A blank meeting site for you to customize based on your requirements.  <br/> |Site collection and site, Server and Foundation  <br/> |Site collection and site, Server and Foundation  <br/> |
|Decision Meeting Workspace  <br/> |A site for meetings that track status or make decisions. It provides lists for creating tasks, storing documents, and recording decisions.  <br/> |Site collection and site, Server and Foundation  <br/> |Site collection and site, Server and Foundation  <br/> |
|Social Meeting Workspace  <br/> |A site to plan social occasions. It provides lists for tracking attendees, providing directions, and storing pictures of the event.  <br/> |Site collection and site, Server and Foundation  <br/> |Site collection and site, Server and Foundation  <br/> |
|Multipage Meeting Workspace  <br/> |A site to plan, organize, and capture the results of a meeting. It provides lists for managing the agenda and meeting attendees in addition to two blank pages for you to customize based on your requirements.  <br/> |Site collection and site, Server and Foundation  <br/> |Site collection and site, Server and Foundation  <br/> |
|Enterprise  <br/> |Document Center  <br/> |A site to centrally manage documents in your enterprise.  <br/> |Site collection and site, Server only  <br/> |
|Records Center  <br/> |This template creates a site designed for records management. Records managers can configure the routing table to direct incoming files to specific locations.  <br/> |Site collection and site, Server only  <br/> |Site collection and site, Server only  <br/> |
|Business Intelligence Center  <br/> |Same functionality as the 2013 Business Intelligence site.  <br/> |Site collection only, Server only  <br/> |Site collection and site, Server only  <br/> |
|Enterprise Search Center  <br/> |A site for delivering the search experience. It includes a search box with scopes for general searches and for people searches. You can add and customize tabs to focus on other search scopes or result types.  <br/> |Site collection and site, Server only  <br/> |Site collection and site, Server only  <br/> |
|My Site Host  <br/> |Same functionality as the 2013 My Site Host site.  <br/> |Site collection only, Server only  <br/> |Site collection and site, Server only  <br/> |
|Basic Search Center  <br/> |A site for delivering the search experience. The site includes pages for search results and advanced searches.  <br/> |Site collection and site, Server and Foundation  <br/> |Site collection and site, Server only  <br/> |
|FAST Search Center  <br/> |A site for delivering the FAST search experience.  <br/> |Site collection and site, Server only  <br/> |Site collection and site, Server only  <br/> |
|Publishing  <br/> |Publishing Portal  <br/> |Same functionality as the 2013 Publishing Portal site.  <br/> |Site collection only, Server only  <br/> |
|Enterprise Wiki  <br/> |Same functionality as the 2013 Enterprise Wiki site.  <br/> |Site collection only, Server only  <br/> |Site collection only, Server only  <br/> |
|Publishing Site with Workflow  <br/> |Same functionality as the 2013 Publishing Site with Workflow site.  <br/> |2010 site only, Server only  <br/> |Site collection only, Server only  <br/> |
|Custom  <br/> |\<Select template later…\>  <br/> |Same functionality as the 2013 \<Select template later…\> option.  <br/> |Site collection only, Server and Foundation  <br/> |
|Web Databases  <br/> |Assets Web Database  <br/> |Create an assets database to keep track of assets, including asset details and owners.  <br/> |2010 site only  <br/> |
|Charitable Contributions Web Database  <br/> |Create a database to track information about fundraising campaigns including donations made by contributors, campaign-related events, and pending tasks.  <br/> |2010 site only  <br/> |2010 site only  <br/> |
|Contacts Web Database  <br/> |Create a contacts database to manage information about people that your team works with, such as customer and partner.  <br/> |2010 site only  <br/> |2010 site only  <br/> |
|Issues Web Database  <br/> |Create an issues database to manage a set of issues or problems. You can assign, prioritize, and follow the progress of issues from start to finish.  <br/> |2010 site only  <br/> |2010 site only  <br/> |
|Projects Web Database  <br/> |Create a project tracking database to track multiple projects and assign tasks to different people.  <br/> |2010 site only  <br/> |2010 site only  <br/> |
   
> [!NOTE]
> The Web Databases site templates that are available through the 2010 experience sites in SharePoint 2013 are no longer available in the 2013 experience sites in SharePoint 2013. In SharePoint Server 2016, you create an Access database by creating a new app, instead of creating a site. 
  
> [!IMPORTANT]
> Some SharePoint 2010 Products site templates, such as the Document Workspace Site templates, were deprecated and are not available as an option in SharePoint 2013. Existing sites that were created by using these deprecated site templates and then upgraded will continue to operate in SharePoint 2013. The deprecated site templates will be removed completely from the next version of SharePoint. 
  
Examples of solutions that benefit from being implemented as site collections are as follows:
  
- **Team collaboration site** A site collection to support authoring and collaboration tasks. Often, this kind of site includes collaborative content that is not published but only used internally. For example, a team collaboration site collection might contain a site for each team in your organization to use to plan projects, coordinate tasks, record meeting notes, and store team documents. 
    
- **Published Internet site** A site collection for publishing content to anonymous Internet readers. A small number of authors create and publish content for many readers. For example, you might use a published Internet site to provide information about company products or services to customers. You can implement publishing sites in a single site collection, where authoring and publishing tasks are performed on the same site. You can also implement publishing sites as two or more site collections that separate the stages of authoring and publishing. Content is created on one or more authoring site collections, and is displayed on one or more publishing site collections by using the Cross-Site Collection Publishing feature in SharePoint Server. For information about how to decide which publishing method to use, see [Plan for Internet, intranet, and extranet publishing sites in SharePoint Server](../administration/plan-for-internet-intranet-and-extranet-publishing-sites.md). For information about cross-site publishing, see [Plan for cross-site publishing in SharePoint Server](../administration/plan-for-cross-site-publishing.md).
    
## Overview of SharePoint sites
<a name="section2"> </a>

You create sites in your site collection to partition your content so that you can have finer control of the appearance and the permission to the content. You can also have different features available on the various sites in your site collection. You can use a site template with its default configuration, or you can change the site's default settings through site administration, and then save the site as a new template. For more information, see [Create and use site templates](https://go.microsoft.com/fwlink/?LinkId=394630).
  
> [!NOTE]
> You cannot save a SharePoint publishing site collection or site as a template. If you activate the SharePoint Server Publishing Infrastructure feature on a non-publishing site collection, the **Save site as template** link is removed from the **Site Actions** section on the **Site Settings** page. 
  
You can configure the following items for a site:
  
- **Templates** Sites in a site collection can each use different templates. 
    
- **Language** If language packs were installed on the web server, you can select a specific language to use together with the site template when you create a new site. The user interface that appears on the site is displayed in the language that was selected when the site was created. Content and other items created by users are displayed in the language in which they are created. For more information, see [Plan for multilingual sites in SharePoint Server](plan-for-multilingual-sites.md) and [Install or uninstall language packs for SharePoint Servers 2016 and 2019](../install/install-or-uninstall-language-packs-0.md). 
    
- **Security** You can define unique user groups and permissions for each site. 
    
- **Navigation** You can fine-tune your site's navigation experience by configuring unique navigation links in each part of your site's hierarchy. Site navigation often reflects the relationships among the sites in a site collection. Therefore, planning navigation and planning sites structures are closely related activities. For more information, see [Overview of site navigation in SharePoint Server](site-navigation-overview.md).
    
    In SharePoint Server publishing sites, you can use managed navigation to create a site navigation that is derived from a tightly managed taxonomy. For more information, see [Overview of managed navigation in SharePoint Server](../administration/overview-of-managed-navigation.md).
    
- **Web pages** Each site can have a unique welcome page and other pages. 
    
- **Site layouts** Each site can have a unique layout or master pages. 
    
- **Themes** You can change colors and fonts on a site. For more information, see [Overview of themes in SharePoint Server](themes-overview.md).
    
- **Regional settings** Each site can have custom regional settings, such as locale, time zone, sort order, time format, and calendar type. 
    
- **Search** Each site can have custom search settings. For example, you can specify that a particular site never appears in search results. 
    
- **Content types** Each site can have unique content types and site columns. 
    
- **Workflows** You can make each site have unique workflows. 
    
- **Apps** You can install apps for SharePoint to deliver specific information or functionality to a SharePoint site. An app for SharePoint is a small, easy-to-use, stand-alone application that solves a specific end-user or business need. 
    
## See also
<a name="section2"> </a>

#### Concepts

[Plan sites and site collections in SharePoint Server](plan-sites-and-site-collections.md)
  
[Overview of site navigation in SharePoint Server](site-navigation-overview.md)
  
[Overview of site policies in SharePoint Server](site-policy-overview.md)

