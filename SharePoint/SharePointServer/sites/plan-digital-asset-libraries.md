---
title: "Plan digital asset libraries in SharePoint Server 2013"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/13/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: d8635abe-1b1b-42db-95ff-ab9341d957e2
description: "Learn how to plan storage and performance, permissions and security, metadata and search, Web Parts, views and filters, and client support."
---

# Plan digital asset libraries in SharePoint Server 2013

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)] 
  
The SharePoint Server 2013 asset library is a special kind of document library. It is a collection of media files — such as image, audio, and video files — that is shared with other site users. 
  
For information about how to manage digital assets, see [Overview of managing digital assets in SharePoint Server 2013](managing-digital-assets-overview.md).
  
    
## Asset library overview
<a name="Section1"> </a>

Asset libraries are collections of media files on SharePoint Server 2013 that you share with other site users. As part of planning for managing digital assets, you must decide which kind of asset library best fits the needs of the organization. Because the asset library is a SharePoint Server 2013 library with specialized content types for digital assets, you use many of the same methods that you use to plan a document management solution.
  
You can use an asset library in the following two ways:
  
- **As a general document library for digital assets at the team level.** The asset library stores images, audio, and video files for use by a team. A site owner might give everyone on the team permissions to upload, organize and manage assets, or you might restrict the task of organizing and managing assets to a small subset of people on the team. 
    
    > [!NOTE]
    > SharePoint Server 2013 does not support live streaming of audio or video content. 
  
- **As a centralized repository for digital assets for the organization.** In this situation, you use content approval and workflow for all assets that are added to the library. People who have different roles might be responsible for separate stages of the approval process. For example, graphic designers and audio or video producers could upload assets to the library. But a content manager might be responsible for triaging incoming assets, assigning additional metadata to the assets, and approving them for publication. 
    
For more information about scenarios in which you might use a digital asset library, see the [Scenarios for using the asset library](managing-digital-assets-overview.md#Section4) section in [Overview of managing digital assets in SharePoint Server 2013](managing-digital-assets-overview.md).
  
## Plan for asset libraries
<a name="Section2"> </a>

Planning the asset libraries for a digital asset solution consists of the following major steps:
  
1. [Identify roles for managing digital assets](plan-digital-asset-libraries.md#Section2a)
    
2. [Analyze asset usage](plan-digital-asset-libraries.md#Section2b)
    
3. [Plan organization of asset libraries](plan-digital-asset-libraries.md#Section2c)
    
4. [Plan content types](plan-digital-asset-libraries.md#Section2d)
    
5. [Plan content governance for digital assets](plan-digital-asset-libraries.md#Section2e)
    
6. [Plan workflows](plan-digital-asset-libraries.md#Section2f)
    
7. [Plan policies](plan-digital-asset-libraries.md#Section2g)
    
8. [Other uses for an asset library](plan-digital-asset-libraries.md#Section2h)
    
### Identify roles for managing digital assets
<a name="Section2a"> </a>

The first step in planning a digital asset library is to determine the participants and stakeholders for the solution. Find out who creates digital assets in the organization, what kinds of assets they create, who manages the assets, and who maintains the servers on which the assets are stored. For more information and for a worksheet to record the data that you collect, see [Identify users and analyze document usage in SharePoint Server](../governance/identify-users-and-analyze-document-usage.md).
  
### Analyze asset usage
<a name="Section2b"> </a>

After you identify who works on assets, determine the kinds of assets they work on, and how they use the assets. This helps you determine how to structure the asset libraries, how many libraries are required, which content types to use for the assets, and which information management policies to apply to the asset libraries. Because the size of most digital assets is much larger than standard documents, you must also plan for storage capacity. For more information and for a worksheet to record the data that you collect, see [Identify users and analyze document usage in SharePoint Server](../governance/identify-users-and-analyze-document-usage.md). 
  
### Plan organization of asset libraries
<a name="Section2c"> </a>

As you plan the asset libraries, you decide where you should create them, how they must be used, how many are needed, and how to organize them. You use the same methods to plan asset libraries as you do to plan document libraries. This section describes the following steps for planning asset libraries:
  
- Determine how many asset libraries are needed
    
- Decide where you want to create each asset library
    
- Choose a fixed or collaborative library
    
- Decide how to organize the asset library
    
 **Determine how many asset libraries are needed.** This determination, as in the earlier analysis and planning steps, also depends on how the asset library will be used. For example, if you have individual teams that must use asset libraries for collaboration, and who must use content governance such as versioning while they work on assets, you can create an asset library for each team site. You can then let the teams manage their own assets. If you want the asset library to serve as a large-scale centralized repository that is used by many teams, you might create a single asset library. Then, you can adjust the permissions to manage how people use, manage, and search the library. For more information, see [Plan document libraries in SharePoint 2013](/previous-versions/office/sharepoint-server-2010/cc262215(v=office.14)).
  
> [!NOTE]
> If you enable the disk-based cache for a web application, every site collection within that web application will use the cache. If you do not have to have the disk-based cache for most the sites, consider putting in a separate web application only those site collections that contain an asset library that requires the disk-based cache. 
  
 **Decide where you want to create each asset library.** Where you create the asset library depends on how you plan to use it. For an asset library that will be used at the team level, you might create the asset library at the site level. For a centralized repository, you might create the asset library at the site collection level. If the asset library will be used with a web publishing site, put the library in the same site collection as the publishing site so that asset files that are used by publishing pages are available to the publishing site. Use your asset analysis to determine who creates and uses assets, and how those assets are used. This will help you decide where asset libraries are needed in the enterprise. 
  
 **Choose a fixed or collaborative library.** Depending on the scenario, the asset library will be either a fixed library or a collaborative environment. In a fixed library, completed assets are checked in and the library is read-only. In a collaborative environment, versioning is enabled for the library, and users who have appropriate permissions can both read and write to existing assets. 
  
 **Decide how to organize the asset library.** You can plan to store all assets in the root of the asset library, and use custom views to display assets to library users based on certain criteria. You can also use folders to hold assets based on criteria that you specify. For example, you might put video files in one folder and audio files in another. Or, you might create folders based on products and put all assets related to a particular product into the product folder. Refer to your asset analysis to determine the most common scenarios for how assets are used in your organization. 
  
### Plan content types
<a name="Section2d"> </a>

The content types included in an asset library are image, audio, and video. You can either use these content types or create custom content types that are derived from them, depending on the classification needs of your organization. For example, you might create two separate content types for posters and product logos, and derive the base characteristics for those new content types from the image content type. This arrangement lets you associate separate properties for the two new content types, specify different workflows, or set different information management policies based on the content types. For more information, see [Plan content types and workflows in SharePoint 2013](/previous-versions/office/sharepoint-server-2010/cc262735(v=office.14)).
  
### Plan content governance for digital assets
<a name="Section2e"> </a>

You plan the appropriate degree of control for each content type and storage location for digital assets. For example, if the asset library is a collaborative solution, you can use versioning to store successive iterations of assets in the library, and can require users to check assets in and out before working on assets. You can also specify an approval process by which assets must be approved before they can be made available to an audience. For more information, see [Plan document versioning, content approval, and check-out controls in SharePoint 2013](/previous-versions/office/sharepoint-server-2010/cc262378(v=office.14)).
  
### Plan workflows
<a name="Section2f"> </a>

You use workflows to perform management tasks on assets in the asset library in the same manner as you use workflows in a document library. Important considerations include the following:
  
- Do assets have to be reviewed and approved before they can be used by asset consumers?
    
- Who is responsible for managing the expiration of assets?
    
- Are assets retained or deleted after expiration?
    
For more information, see [Plan content types and workflows in SharePoint 2013](/previous-versions/office/sharepoint-server-2010/cc262735(v=office.14)).
  
### Plan policies
<a name="Section2g"> </a>

For each content type that you want to use in the asset library, you must plan the information management policies that specify how assets are audited, retained, and labeled. For more information, see [Plan for information management policy in SharePoint Server](../governance/information-management-policy-planning.md).
  
> [!IMPORTANT]
> SharePoint Server 2013 does not automatically apply Information Rights Management (IRM) protection to audio or video content that is stored in a SharePoint Server 2013 asset library. Additionally, when audio or video assets stored in SharePoint Server 2013 are viewed by a user, copies of those assets might be stored in the user's local browser cache. The SharePoint Server 2013 media player supports playing IRM-protected audio and video formats where the Digital Rights Management protection was applied by an external IRM provider that is supported by Silverlight 3 or later versions. For more information, see [Digital Rights Management (DRM)](https://go.microsoft.com/fwlink/p/?LinkId=154933) (https://go.microsoft.com/fwlink/p/?LinkId=154933). 
  
### Other uses for an asset library
<a name="Section2h"> </a>

The following table lists additional uses for an asset library in SharePoint Server 2013.
  
|**Feature**|**Description**|
|:-----|:-----|
|Podcasts  <br/> |Users can enter the URL for the library RSS feed into their podcast application to receive updates when new audio and video files are added to the asset library. For more information about how to upload audio and video files, see [Set up an Asset Library to store image, audio, or video files](https://office.microsoft.com/en-us/office365-sharepoint-online-enterprise-help/set-up-an-asset-library-to-store-image-audio-or-video-files-HA102785730.aspx).  <br/> |
|Suggested Content Browser Locations  <br/> |When you are using a publishing site, the URL for an asset library in a separate site can be added to the Suggested Content Browser Locations list for the publishing site. This lets content creators access the asset library when they insert assets into web pages within SharePoint Server 2013, or within Office applications, such as Word.  <br/> |
|Content Organizer  <br/> |When you are using an asset library as a centralized repository, consider using the Content Organizer site feature to automate the routing of assets that are uploaded to the library by users. When the Content Organizer site feature is activated, a new library named Drop Off Library is automatically created. This lets you create rules that specify how assets added to this library are routed to other libraries, such as the asset library. For example, you can specify that all audio assets are stored in one folder of the asset library, whereas all video assets are stored in another folder.  <br/> An advantage to using the Content Organizer is that certain metadata fields can be required to receive user input when new assets are added. This helps control how different types of assets are routed. In addition, this can automate some of the content management work and reduce the workload of administering the asset library and managing the assets it contains. For more information, see [Configure the Content Organizer to route documents](https://office.microsoft.com/en-us/sharepoint-server-help/configure-the-content-organizer-to-route-documents-HA102772938.aspx) <br/> |
|Published links  <br/> |Members of the Administrators group on the local computer can add links to SharePoint sites and lists from client applications in Office such as Word, Excel, and PowerPoint. These links appear on the **My SharePoint Sites** tab of the **Open**, **Save**, and **Save As** dialog boxes when you open and save documents from these applications. Users can manually add links to their published link lists by browsing to a library and clicking **Connect to Office**. For more information, see [Add or delete links to Office client applications (SharePoint Server 2010)](https://go.microsoft.com/fwlink/p/?LinkId=154958).  <br/> |
   
## Plan for permissions and security
<a name="Section3"> </a>

Planning for permissions and security in an asset library is the same as planning for permissions and security in a document library. For information about the available default groups, permission levels, and when to use custom groups or levels, see [Determine permission levels and groups in SharePoint 2013](/SharePoint/sites/determine-permission-levels-and-groups-in-sharepoint-server).
  
## Plan for storage and performance
<a name="Section4"> </a>

Because an asset library is a specialized kind of document library, determining storage requirements for digital assets resembles determining storage requirements for documents. The primary difference is that asset libraries typically contain fewer assets than document libraries contain. But the assets in an asset library are larger than those in a document library. When you plan for storage, analyze the content to determine how many assets will be stored in the asset library, and the average size of those assets. For example, if you have 50,000 assets and the average file size is 10 megabytes (MB), you must have at least 500 gigabytes (GB) of storage on the database server. If you will be using the asset library to store video files, you must determine the average size of those files. By default, the maximum video file upload size is 250 MB. If you know that you have to support larger video files, you can increase the file upload size up to 2 GB for every web application by using Central Administration. If you will be using the disk-based binary large object (BLOB) cache, you must also make sure that the front-end web server has sufficient disk space in which to store the cached files. 
  
Depending on the type of digital asset files that will be stored in the asset library, you should enable the disk-based BLOB cache and Bit Rate Throttling to provide better performance for users. It is usually a good idea to enable the disk-based BLOB cache. When the BLOB cache is enabled, it stores specified file types on the front-end web server to reduce the load put on the database server when those files are requested and served to users.
  
The video renditions feature lets users upload multiple renditions of a video. The video renditions can have different codecs and formats, or different bit rates. A user can choose the rendition to play. By default, the video with the lowest bit rate is chosen. 
  
If you will be using the asset library to serve audio and video files to users, we recommend that you always enable the BLOB cache, and that you enable Bit Rate Throttling on the server. Bit Rate Throttling controls the rate at which audio and video files are downloaded to the client so that overall performance on the site is not affected. For more information about the disk-based cache, see [Plan for caching and performance (SharePoint Server 2010)](/SharePoint/administration/caching-and-performance-planning). For information about how to enable and configure Bit Rate Throttling, see [Bit Rate Throttling Readme](https://go.microsoft.com/fwlink/p/?LinkId=154962) (https://go.microsoft.com/fwlink/p/?LinkId=154962). 
  
## Plan for metadata and Search
<a name="Section5"> </a>

The addition of metadata that helps describe the type and content of a digital asset greatly improves the discoverability of content in an asset library. When you plan an asset library, remember that rich media files are not automatically searchable because they do not contain text that a search engine can index. The metadata that is used to describe digital assets can include information such as the title, description, author, copyright, and enterprise keywords that provide additional details about the asset. Some metadata, such as the size and dimensions of an image, is entered automatically when the asset is uploaded to the asset library. Other metadata is added manually. For example, an asset creator might add a text description of an image when the asset is uploaded. Or, a library manager might add keywords and update approval status during triage of incoming assets or performance of administrative task. 
  
SharePoint Server 2013 includes many improvements for video search. Users can use the Search Navigation Web Part to filter the search results to display only video results. The video search results page shows a thumbnail for each video. Users can click the thumbnail to go to the video player page or pause on the thumbnail to view additional information such as who uploaded the video, when it was uploaded, number of views, and so on. The video search results page also provides video-specific search refiners. Users can refine the search results by length of video, people in the video, and upload date.
  
## Plan for video thumbnails
<a name="thumbnail"> </a>

Thumbnail preview images are created automatically when a video is uploaded to an asset library. Content authors can also choose a frame from the video or upload a picture and use that as the thumbnail preview image. For automatic thumbnail creation to work, you must install the Desktop Experience feature on the front-end web server that hosts SharePoint Server 2013. For more information, see [Desktop Experience Overview](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc772567(v=ws.11)).
  
## Plan for Web Parts and web pages
<a name="Section6"> </a>

SharePoint Server 2013 has many Web Parts and field controls that take advantage of the content types in an asset library. Web Parts are added to web zones in Web Part pages by content owners. Field controls are added to publishing pages by site developers and designers. Examples of Web Parts and field controls that are used to display digital assets include the following:
  
- **Media Web Part and field control.** Used to display embedded video in a web page. 
    
- **Image Web Part and field control.** Used to display images on a web page. 
    
- **Content Query Web Part.** Used to display items from all sites in a site collection, a selected site or subsite, or a specific list or library. The query can be configured to return a list of items based on list and content types, and can be filtered and targeted to a specific audience. 
    
- **Content Search Web Part.** Used to display content that was crawled and added to the search index. You can configure the Web Part and choose the video content type from the query builder. 
    
When you design web pages for sites, consider which fields to expose to users in web pages and Web Parts to help users find the assets they need. You can customize the information that is displayed when a user rests the pointer on an asset in the asset library by editing the Thumbnail view in the Library Settings page. For more information about Web Parts and field controls, see [Understanding Field Controls and Web Parts in SharePoint Server 2007 Publishing Sites](https://go.microsoft.com/fwlink/p/?LinkID=210863).
  
## Plan for client support
<a name="Section7"> </a>

SharePoint Server 2013 supports HTML5 and Silverlight media players. The HTML5 media player is the default media player that is used to play all video files that are compatible with the HTML5 **\<video\>** element implementation for the current browser. SharePoint Server 2013 selects the player automatically, depending on the video format. If the video format cannot be played on the HTML 5 media player, the system uses the Silverlight media player. 
  
To use the Silverlight media player, Silverlight 3, or later versions, must be installed on the client computers. For more information about Silverlight 3, see [Silverlight Overview](https://go.microsoft.com/fwlink/p/?LinkId=154002) (https://go.microsoft.com/fwlink/p/?LinkId=154002). 
  
For more information about the media formats that are supported by Silverlight media players, see [Supported Media Formats, Protocols, and Log Fields](https://msdn.microsoft.com/en-us/library/cc189080%28VS.95%29.aspx).
  
## See also
<a name="Section7"> </a>

#### Concepts

[Overview of managing digital assets in SharePoint Server 2013](managing-digital-assets-overview.md)

