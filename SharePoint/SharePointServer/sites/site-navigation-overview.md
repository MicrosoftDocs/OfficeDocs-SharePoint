---
title: "Overview of site navigation in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 8/1/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: a6a42ac0-abad-44ce-98f3-508c531a29b2
description: "Learn about the types of navigation controls that are available in SharePoint Server."
---

# Overview of site navigation in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
Site navigation are the sets of controls and links in your site collections, sites and pages that help orient users to where they are and help them easily get to other relevant locations. For example, you can configure site navigation to help users get to other sites in the site collection or you can configure it so that the top navigation and the vertical navigation controls are dynamically generated based on context of what the user is looking at. A well planned site navigation strategy make SharePoint Server sites easier to use.
  
SharePoint Server has many features that use search technology to provide site owners with ways to display content dynamically on web pages. For more information about search-driven sites, see [Plan for cross-site publishing in SharePoint Server](../administration/plan-for-cross-site-publishing.md).
  
    
## Navigation controls overview
<a name="section1"> </a>

Navigation controls can be displayed on master pages, page layouts, and — by using Web Part zones — directly in a page's content.
  
By default, SharePoint Server bases its navigation model on the hierarchical structure of the site collection. By using the navigation features, you can link any site to any other in the hierarchy and to pages in those sites. Additionally, you can create links to arbitrary locations, such as to an external website.
  
 **Managed Navigation** - When you use managed navigation, you create a term set that represents the navigation hierarchy, and navigation controls display data from the term set. You can change the navigation hierarchy by changing the term set. For more information, see [Overview of managed navigation in SharePoint Server](../administration/overview-of-managed-navigation.md). Managed navigation is disabled by default in all site templates except the Publishing Portal site collection template.
  
Navigation links are subject to security trimming. This means that if a site user does not have permissions to the destination SharePoint Server site or page of the link, then that link is not displayed. Pages, sites, and links that are manually added to navigation can be configured to be available only to members of a particular audience. Users who are not members of that audience cannot see links to sites and pages that are targeted to that audience.
  
## Common Navigation Controls
<a name="section2"> </a>

A master page defines the outer frame of the web pages in a site. Master pages contain the elements that you want all pages in your site to share, such as branding information; common commands, such as Search; and navigation elements that you want to be available throughout the site. A master page often includes the top navigation control (where links are presented on drop-down menus) and the vertical navigation control.
  
You can apply your own custom styles to these navigation controls by using Design Manager and an HTML editor of your choice.
  
### Top Link Bar
<a name="Section2a"> </a>

The **Top link bar** control displays links to the sites that are one level below the current site in a site hierarchy. It is common for the top link bar to appear at the top of each page in a site. By default, all sites that are one level below the current site are added to the top navigation, and each site has its own unique top navigation. Site owners can customize the top navigation for a specific site. 
  
Site owners can choose to inherit the top navigation from the parent site. This approach allows users to switch from one site to another from anywhere within the site collection, by allowing the top navigation to stay the same in all the sites in the site collection. For example, an Internet site that is used to market an organization's products could have a site for each line of its products. By displaying each product's site in the top navigation of each site, site designers can make it possible for users to easily switch from one site to another without having to return to the site home page.
  
Other top navigation configuration features include the following:
  
- Linking to the web pages of all the top-level sites in SharePoint Server only
    
- Linking to specified external sites
    
- Linking to specified sites or pages that are anywhere in the site.
    
- Organizing links under headings in SharePoint Server only.
    
- Manually sorting the items on the top link bar
    
- Restricting the maximum number of items to show at the global navigation level in SharePoint Server only
    
All top link bar features, such as linking to external sites, can be defined uniquely for each site. If you are on a top level site, you can add, move or rearrange the links by clicking **EDIT LINKS**
  
By using Design Manager you can additionally customize the appearance and functionality of the top link bar in SharePoint Server only. 
  
### Quick Launch
<a name="Section2b"> </a>

Quick launch typically highlights the important content in the current site, such as lists and libraries. It is common for it to appear on the left of each page in a site.
  
Quick launch configuration features include the following:
  
- Linking to sites that are on the same level of the site hierarchy as the current site in SharePoint Server only
    
- Linking to specific external sites or to pages in the current site
    
- Organizing links under headings.
    
- Manually sorting the items in Quick Launch
    
- Restricting the maximum number of items to show at the navigation level in SharePoint Server only
    
If you want to add, remove, or rearrange the links, click **EDIT LINKS** in the vertical navigation. You can also add, remove, rearrange links or create new headings in Site Settings for the site. To enable or disable Quick Launch, click the gear icon in the upper-right corner and then click **Site Settings**. In the **Look and Feel** area, click **Tree view**, and then select the **Enable Quick Launch** check box. 
  
Just as you customize top navigation, you can also customize the appearance and functionality of vertical navigation by using Design Manager in SharePoint Server.
  
### Tree view
<a name="Section2d"> </a>

Tree view appears on the left side of the page. If you have enabled Quick launch and Tree view, Tree view will appear below Quick launch. Tree view displays site content, such as lists, libraries, and sites that are in the current site, in a hierarchical structure.
  
By default, tree view navigation is turned off. To enable tree view, click the gear icon in the upper-right corner and then click **Site Settings**. In the **Look and Feel** area, click **Tree view**, and then select the **Enable Tree View** check box. 
  
### Metadata navigation
<a name="Section2e"> </a>

Metadata navigation displays metadata about library and list content in the tree view navigation, and lets users filter library or list content based on specified fields. Site administrators can configure metadata navigation by using the Metadata Navigation Settings page for a list or library to configure the navigation hierarchies and key filters that are available to users. Metadata navigation is displayed only when a user views the list or library for which metadata navigation was configured. 
  
### Managed navigation
<a name="Section2e"> </a>

Managed navigation enables you to define and maintain the navigation on your site by using term sets. This method supplements the existing SharePoint navigation based on site structure. You create the managed navigation structure by adding terms to the navigation term set in the Term Store Management tool. You can copy the navigation term set and translate it into the same languages that are used for variations labels. For more information, see [Overview of managed navigation in SharePoint Server](../administration/overview-of-managed-navigation.md).
  
## Navigation Web Parts
<a name="section4"> </a>

A Web Part is a control that authors can insert into a Web Part zone on a page and configure. The Summary Links, Table of Contents, Content Query, and Content Search controls each have Web Part counterparts that page authors can insert into Web Part zones on pages. The Web Parts have the same configuration features and the same functionality as their related controls. However, they can be configured when they are inserted on the page instead of when the site designer inserts them on the layout of the page. To make navigation Web Parts available for page authors to insert on a page, you can include one or more Web Part zones on a page layout, or you can include a Rich Text Editor control on a page, which will allow users to add Web Parts directly to the Rich Text Editor Web Part.
  
The following navigation Web Parts are available only for non-Publishing sites:
  
- **Content Rollup - Categories** Displays categories from the Site Directory 
    
- **Content Rollup - Site Aggregator** Displays sites of your choice. 
    
- **Content Rollup - Sites in Category** Displays sites from the Site Directory in a specific category. 
    
- **Social Collaboration - Tag Cloud** Displays the most popular subjects being tagged inside your organization. 
    
If you make it possible for authors to insert navigation Web Parts on pages, you reduce the control that you have over your site's navigation because authors can then control part of the navigation experience of site users. This might be appropriate in a loosely controlled environment, such as a collaboration site in an organization, where individual authors must be able to point users to content that is related to the author's work. It is less appropriate in a more tightly controlled environment, such as an Internet presence site, in which the navigation experience is planned and implemented in a consistent, controlled way by the site designers and planners.
  
> [!NOTE]
> If you want to include Web Part zones on page layouts but prevent authors from inserting navigation Web Parts into these zones, you can change the permissions that are required to use navigation Web Parts in the Web Parts gallery of your site to make those Web Parts unavailable to authors based on their permission level. 
  
## See also
<a name="section4"> </a>

#### Concepts

[Overview of managed navigation in SharePoint Server](../administration/overview-of-managed-navigation.md)
  
[Manage web parts in SharePoint Server](manage-web-parts.md)

