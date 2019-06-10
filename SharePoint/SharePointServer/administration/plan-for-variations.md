---
title: "Plan for variations in SharePoint Server"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.date: 7/25/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 45264de9-6859-45c1-9d6d-70035c471a2a
description: "Learn how to plan for variations, identify the source and target variation sites, and decide how content will be synced on target variation sites in SharePoint Server and SharePoint Online."
---

# Plan for variations in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-SPO-md](../includes/appliesto-2013-2016-2019-SPO-md.md)] 
  
The variations feature in SharePoint Server and SharePoint Online makes content available to specific audiences on different sites by syncing content from a source variation site to each target variation site. Content on a target variation site can be translated into other languages before it is published. Variations can be used only on sites that are created by using one of the Publishing site templates, or on a site for which the SharePoint Server Publishing Infrastructure feature was activated.
  
This article contains information about important items that you should consider when you use variations in a publishing site collection, and it describes the tasks that are involved in planning a solution that uses variations in SharePoint Server. This article does not provide an overview of variations, describe how to use variations, or explain how to create variation labels and hierarchies. For more information about variations, see [Variations overview in SharePoint Server](variations-overview.md).
  
## About planning variations
<a name="bkm_about"> </a>

The planning process that is described in this article starts with describing important items that you should consider when you plan to use variations with a SharePoint Server solution. The remainder of the article describes the steps that are required to plan for using variations with SharePoint Server. These steps include the following:
  
- Determine the variations that are needed and select the variations root site.
    
- Specify the source variation site and plan the target variation sites.
    
- Decide how sites, lists, and pages will be created on the target source sites.
    
- Plan how variations timer jobs will be scheduled.
    
You can record this information in the [Variations planning worksheet](https://go.microsoft.com/fwlink/p/?LinkId=279753).
  
## Important items to consider when planning to use variations
<a name="bkm_considerations"> </a>

Before you plan to use variations with a SharePoint Server solution, you should be aware of the interaction between variations and other SharePoint Server features. This section contains information about important items to consider when you plan to use variations with a SharePoint Server solution.
  
### Content approval
<a name="Section2a"> </a>

Content approval is the method by which site members with approver permissions control the publication of content. In content approval, content is considered published when a new major version is approved, because major versions are viewable by users who have read permissions. Content approval in variation sites requires major and minor versioning in the Pages libraries on the source and target variation sites. For more information about content approval, see [Plan content approval and scheduling (SharePoint Server 2010)](https://go.microsoft.com/fwlink/p/?LinkID=95836).
  
Content approval has unique factors that you should consider when you are planning variations:
  
- On the source variation site, when a page is submitted for approval, an e-mail message is generated and sent to the contact of the page by using the values stored in the following columns, in the following order:
    
  - **Contact**
    
  - **Contact E-Mail Address**
    
  - **Modified By**
    
    > [!NOTE]
    > Starting with the **Contact** field, each field is checked for contact information to which the notification can be sent. If the first field is empty, the next field is tried until contact information is found. 
  
    After the page is approved for publication, it is enabled for syncing to the target variation sites. You can configure the variations settings so that content is either manually or automatically synced to the variation sites.
    
- On target variation sites, a page that is synced from the source variation site is always assigned a minor version number. If the page is new to the target site, it is assigned version 0.1. If the page already exists on the target variation site, the synced page is assigned the next available minor version number. For example, if a target variation site has version 2.1 of a page and a new variation of that page is synced to the target site, the page becomes version 2.2.
    
- If a page is published on the source variation site, when the page is synced to target variation sites, the **Approval** status is set to **Draft**. If **Content Approval** and **Document Version History** are enabled in the Pages library on target variation sites, the page must be approved on each target variation site before the page is available to readers. 
    
> [!NOTE]
> Changes made to content that originates on the source variation site can supersede changes made to the content on the target variation site. For example, if the source variation site is in one language and the target variation site is in another, the following situation might occur: An editor changes a localized page on the target variation site, assigning it a new minor version, 1.1. Then, a writer on the source variation site makes different changes to the same page, which is synced to the target variation site as version 1.2. This supersedes the version 1.1 changes to the page. In this example, an editor for the target variation site would have to restore the previous version of the page from the **Version History**, accept the new version, or use the **View Changes** button to view differences between the current version and previous versions of the page, and manually merge the new and previous versions into a new version. For more information about versioning, see [Plan document versioning, content approval, and check-out controls in SharePoint 2013](/previous-versions/office/sharepoint-server-2010/cc262378(v=office.14)). 
  
### Site navigation
<a name="Section2b"> </a>

If you use site variations, you must plan your site navigation experience carefully. In SharePoint Server, site navigation links to the current site's peer sites are automatically generated and displayed in the Global Navigation and Current Navigation menus of a web page. In variation sites, where the current site's peers are variations of the same site, you might not want to give site users the ability to browse to other sites in this manner. You can use the **Navigation Settings** page to change the settings of the Global Navigation and Current Navigation menus so that peer sites are not displayed. 
  
> [!NOTE]
> Changes to site navigation on the source variation site are not synced to the target variation sites. If you want the site navigation on target variation sites to match the site navigation on the source variation site, you must manually change the site navigation settings on the target variation sites. 
  
For more information about site navigation, see [Overview of site navigation in SharePoint Server](../sites/site-navigation-overview.md).
  
### Content deployment
<a name="Section2c"> </a>

Content deployment copies content from a source site collection to a destination site collection.
  
We recommend that you disable any content deployment jobs that include the source variation site while Variations Create Hierarchies Job Definition runs. If content deployment runs while the Variations Create Hierarchies Job Definition timer job is also running, a target variation site that is only partially created may be synced to the target variation site on the destination server.
  
For more information about content deployment planning, see [Plan content deployment ](https://go.microsoft.com/fwlink/p/?LinkID=95854).
  
### Cross-site publishing
<a name="Section2c"> </a>

Unlike the variations feature, which syncs content from a source variation site to a target variation site, the cross-site publishing feature uses the search index to only show content on other sites. You can share a list or library as a catalog, which is indexed by the search service, and then show the content in query results in Web Parts on other pages and in other site collections.
  
The variations feature is limited to syncing content within a single site collection. However, you can share lists and libraries as catalogs in variation sites. Then you can create any number of site collections to represent your variation labels, and display content in these site collections. This enables you to have different country code top-level domains for different variation labels. For example, you can have contoso.co.uk or contoso.mx.
  
> [!NOTE]
> Cross-site publishing is available only in SharePoint Server. 
  
For information about cross-site publishing, see [Plan for cross-site publishing in SharePoint Server](plan-for-cross-site-publishing.md).
  
For information about how to plan your site architecture when you want to use variations on a multilingual cross-site publishing site, see [Plan variations for multilingual cross-site publishing site in SharePoint Server](plan-variations-for-multilingual-cross-site-publishing-site.md).
  
### Web Parts
<a name="Section2d"> </a>

A Web Part is one of the building blocks of pages based on SharePoint Server. Most Web Parts are designed to display a specific type of data, such as text, HTML, or images. SharePoint Server includes a default set of Web Parts, and you can also develop or import custom Web Parts.
  
Web Parts are synced with pages of variation sites. If **Update Target Page Web Parts** is enabled, Web Parts are updated only on the target variation site if a page that contains that Web Part is synced to the target variation site. If the Web Part appears on multiple target pages on different target variation sites, all instances of the Web Part are updated when the page from the source variation site is synced to the target variation sites. For example, if a page contains a Media Web Part, and the Web Part is configured to point to video A that is stored on a site outside the variations hierarchy, when the page is published on the source variation site, the page is synced to all target variation sites. The pages on the target variation sites display video A in the Media Web Part. If the page on the source variation site is updated and the Media Web Part is changed to point to video B, the pages on the target variation sites continue to point to video A until the page on the source variation site is published and synced to the target variation sites. Also, if readers on the target variation sites do not have permission to view the video file that is stored outside the variations hierarchy, they cannot view the video. To prevent unintended Web Parts behavior such as this, you can configure the variations settings so that Web Part updates are not synced to target variation sites. 
  
### Multilingual sites
<a name="Section2d"> </a>

SharePoint Server has several features that enable you to support users in different regions or users who speak different languages. You can use these features to create websites in different languages and to enable users to view the user interface of a site in a language other than the one in which a site was created. If you plan to use variations with multilingual sites, there are additional steps that you must follow to enable multilingual support for the variation sites. For more information about how to plan multilingual sites, see [Plan for multilingual sites in SharePoint Server](../sites/plan-for-multilingual-sites.md).
  
## Determine the variations needed
<a name="bkm_list"> </a>

Variations are used to create multilingual sites, and sites based on regional differences. Determine which variations are needed for your solution, and make a list of the sites that will belong to the variations hierarchy.
  
If you will be using variations for creating multilingual sites in SharePoint Server, and if you want the site administration pages of the target variation sites to be displayed in another language, you must install the language pack for each language that corresponds to a variation site. For information about how to install language packs, see [Install or uninstall language packs for SharePoint Server 2016](../install/install-or-uninstall-language-packs-0.md). If you will be using variations for creating multilingual sites in SharePoint Online, all language packs are installed and available for use.
  
## Specify the source variation site
<a name="bkm_source"> </a>

The source variation site is the site where content to be shared by all sites is authored and published, and it is the site that is used to sync changes to the target variation sites. The first variation label that you create is automatically specified as the source variation site. There can be only one source variation site for a variations hierarchy. After a source variation site is specified, it cannot be changed.
  
Review the list of sites for your variations solution, and decide which site will be the source variation site. Record the source variation site for your solution in the top row of the **Variations data sheet** tab in the [Variations planning worksheet](https://go.microsoft.com/fwlink/p/?LinkId=279753). Enter the information for the following columns: 
  
- **Site template language** The name of the language pack to use as the default user interface language. For example, English. If you are not using the multilingual user interface on the target sites, leave this column empty. 
    
- **Locale** The locale that the label represents. For example, English (United States). 
    
- **Variations home** The location where the source and target variations will be created. The variation home site provides the URL for all variation sites and contains the landing page that redirects users to the correct variation site. The home site can be a site at any level in a site collection, including the top-level site. However, after you specify the home site, you cannot change it after you click **Create Hierarchies**, and you cannot use variations anywhere else in the site collection.
    
    To indicate a top-level website of the site collection, type a slash (/).
    
    > [!NOTE]
    > If the home site contains a site hierarchy, or list or Pages library content that you want to include in the source variation site, you must manually copy them to the source variation site after it is created. 
  
- **Label name** The name as it will appear in the URL. 
    
- **Label description** A description for the label. 
    
- **Display name** The name as it will appear in the site navigation. 
    
- **Publishing site template** The site template that is used to create the source variation site. Type Publishing Site with Workflow or Publishing Site.
    
- **Label contact** One or more contacts for the variation site. 
    
## Plan target variation sites
<a name="bkm_target"> </a>

Review the list of sites for your variations hierarchy, and record each target variation site in the [Variations planning worksheet](https://go.microsoft.com/fwlink/p/?LinkId=279753). For each site, enter the information for the following columns.
  
- **Site template language** The name of the language pack to use as the default user interface language. For example, German. If you are not using the multilingual user interface on the target sites, leave this column empty. 
    
- **Locale** The locale that the label represents. For example, German (Germany). 
    
- **Label name** The name as it will appear in the URL. 
    
- **Label description** A description for the label. 
    
- **Display name** The name as it will appear in the site navigation. 
    
- **Hierarchy creation** The portion of the source hierarchy that will be synced to the target variation site. Type one of the following: 
    
  - Publishing Sites, Lists with Variations, and All Pages
    
  - Publishing Sites Only
    
  - Root Site Only
    
- **Allow human translation** Whether to allow human translation on the target label. Type Y or N.
    
- **Translator language** The translator language to use on the target label if human translation is allowed. 
    
- **Allow machine translation** Whether to allow machine translation on the target label. Type Y or N.
    
    > [!NOTE]
    > If the Machine Translation Service is not enabled on the server, the machine translation option is not available. 
  
- **Machine translator language** The machine translation language to use on the target label if machine translation is allowed. 
    
- **Label contact** One or more contacts for the variation site. 
    
> [!NOTE]
> SharePoint Server supports up to 209 variation labels. SharePoint Online supports up to 50 variation labels. 
  
### Plan custom master pages, layout pages or style sheets

You can decide to use custom master pages, page layouts, or style sheets for variation sites. For example, you might need different master pages and page layouts for sites where the language is read right-to-left. Master pages, page layouts, and style sheets are managed only in the top-level site of a site collection. Therefore, you must make all changes to these resources in one of the locations in the top-level site as shown in the following table.
  
**Table: Resource locations for variations customization**

|**Resource**|**Location**|
|:-----|:-----|
|Master Page  <br/> |Master Page Gallery  <br/> |
|Layout Page  <br/> |Master Page Gallery  <br/> |
|XSL styles and cascading style sheets  <br/> |Style Library  <br/> |
   
Target pages can have different page layouts independent of the source variation site. If the page layout on the source site changes, the page layout of the target page is not changed.
  
### Plan custom content types

You must use the same content type (either the Page content type, or a content type based on the Page content type) for all pages that are stored in the Pages library of the source variation site. The easiest way to do this is to use a content type that is defined on the **Site Content Type** page in the top-level site of the site collection. 
  
If you must have custom columns for one or more pages on the variation sites, add them to the content type that you are using in your Pages libraries. For example, you can add a column that indicates whether the page was localized. For more information about how to plan content types and columns, see [Plan content types and workflows in SharePoint 2013](/previous-versions/office/sharepoint-server-2010/cc262735(v=office.14)).
  
## Decide how sites, lists, and pages will be created on target variation sites
<a name="bkm_targetcreation"> </a>

If the source variation site will have other sites below it in a site hierarchy, you must plan for how those sites will be created on the target variation sites. There are two ways in which sites can be created on target variation sites: automatically and manually. By default, any new sites that are added below the source variation site will be automatically created on all target variation sites. However, if you disable automatic site and page creation for variations, for each new site that you create below the source variation site, you must manually specify the target variation sites on which the site should be created. Although enabling new sites to be created automatically on the target variation sites has the advantage of reducing tasks for the site administrator, the advantage to manual site creation is that you can specify which sites should be created on which target variation sites. This can be useful if you want a site to be included only on some, but not all, target variation sites.
  
For list and page content, there are two decisions that you must make about how the content is propagated.
  
1. From the source perspective, what happens when new content is published? You can choose to do one of the following:
    
  - Automatically create a copy of the content in all target variation sites. This is the **Create Everywhere** option, and it is enabled by default. 
    
  - Manually create a copy of the content in selected target variation sites. Subsequent updates to that content will be available automatically for the specified target variation sites. This is the **Create Selectively** option. 
    
2. From the target perspective, what happens when new content is available? You can choose to do one of the following:
    
  - Automatically sync the change from the source variation site, and add it as a new draft version on the target variation site.
    
  - Notify the target label owner that a change is available. The label owner decides whether to manually sync the content.
    
By default, any new pages that are published in the Pages library of the source variation site will automatically be created on all target variation sites. However, if **Create Selectively** is enabled, for each new page that you create on the source variation site, you must manually specify the target variation site on which the page should be created. The **Create Selectively** option can be useful if you want certain pages to be included only on some, but not all, target variation sites. 
  
Lists can be created automatically on target variation sites only if they are created on the source variation site before the variation hierarchy is created. If a list is created after the variations hierarchy is set up, a list must be created manually on the target variation sites by using the **Settings** button on the **Variations** tab on the ribbon for the list on the source variation site. However, new list items can be created automatically on a target variation site. 
  
By default, the **Create Everywhere** option is enabled. You should carefully consider the potential increase in administrative tasks if you decide to enable the **Create Selectively** option. You can configure the settings for site, list, and page creation behavior on the **Variations Settings** page in Site Collection Administration. For information, see [Create a multi-language website](https://go.microsoft.com/fwlink/p/?LinkId=279696).
  
## Plan variations timer job scheduling
<a name="bkm_timerjobs"> </a>

The variations feature uses timer jobs to perform tasks such as creating and propagating sites and pages. A timer job runs inside OWSTIMER, a Windows service for SharePoint Server. Each timer job has its own default schedule for when the job runs. You can change the frequency with which each job runs on the **Job Definitions** page on the Central Administration website. 
  
> [!NOTE]
> Timer jobs are not configurable in SharePoint Online. 
  
The following table lists the variations timer jobs and the default schedule for each job.
  
**Table: Variations timer jobs and default schedules**

|**Job name**|**Default schedule**|
|:-----|:-----|
|Variations Create Hierarchies Job Definition  <br/> |Hourly  <br/> |
|Variations Propagate List Items Job Definition  <br/> |Every 15 minutes  <br/> |
|Variations Propagate Page Job Definition  <br/> |Every 15 minutes  <br/> |
|Variations Propagate Sites and Lists Job Definition  <br/> |Every 30 minutes  <br/> |
   
You can specify when each job will run by setting a recurring schedule in minutes, hourly, daily, weekly, or monthly intervals. If you select daily, weekly, or monthly, you can specify a window of time for when the job should run, and the server will randomly select a time within the specified range in which to start to run the job. This option is most appropriate for high-load jobs that run on multiple servers in a farm. Be aware that running this type of job on all servers in the farm at the same time might increase the server load and affect performance. To avoid this possibility, you can specify an exact starting time for a job.
  
You should carefully plan when the variations timer jobs should run on your servers, and set the recurring schedule accordingly. For example, to determine how often the **Variations Propagate List Items Job Definition** or the **Variations Propagate Page Job Definition** should run and sync list items or pages to target variation sites, consider how many list items or pages will be created on the source variation site, and how often those list items or pages will be updated. 
  
If you plan to change the default schedule of the variations timer jobs, record the new schedule for each timer job on the **Variations Timer Jobs** tab in the [Variations planning worksheet](https://go.microsoft.com/fwlink/p/?LinkId=279753).
  
## Variations planning worksheet
<a name="bkm_worksheet"> </a>

Download an Excel version of the [Variations planning worksheet](https://go.microsoft.com/fwlink/p/?LinkId=279753).
  
## See also
<a name="bkm_worksheet"> </a>

#### Concepts

[Variations overview in SharePoint Server](variations-overview.md)

