---
title: "Overview of managing digital assets in SharePoint Server 2013"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/13/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: dfe5a861-519a-4fc0-89b8-185df5e73284
description: "Learn about the asset library and how you can use it to store and share image, audio, or video files."
---

# Overview of managing digital assets in SharePoint Server 2013

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)]
  
This article describes digital assets (also known as rich media) and defines key terms that are used in relation to managing digital assets in SharePoint Server 2013. It also explains aspects of managing digital assets by using the assets library in SharePoint Server 2013, describes the primary users of an asset library, and outlines common scenarios for using the asset library in SharePoint Server 2013.
  
For more information about how to plan a solution for managing digital assets, see [Plan digital asset libraries in SharePoint Server 2013](plan-digital-asset-libraries.md).
  
Increasing numbers of office workers create or reuse images and other rich media assets as part of their daily tasks. Often, however, no centralized repository exists at the departmental or enterprise level that is optimized for storing these assets. A centralized repository lets users easily discover and reuse rich media assets that others have already created. The asset library in SharePoint Server 2013 can save an organization time and other resources by providing a specialized repository for storing and managing digital assets. Users no longer have to look for assets in multiple locations over the network, or re-create assets from scratch. By using a centralized repository for managing digital assets, the organization also exerts tighter control over brand-sensitive content and can make sure that only approved assets for products are made available to the appropriate users.
  
    
## About managing digital assets
<a name="Section1"> </a>

A digital asset is an image, audio, or video file, or other reusable rich content fragment that an organization uses in applications across the enterprise. The asset library in SharePoint Server 2013 enables users to easily create, discover, and reuse existing digital assets within the organization. 
  
In SharePoint Server 2013 you use an asset library to store and share digital assets with users. The asset library is a SharePoint Server 2013 library template that is customized to use content types designed specifically for storing and cataloging rich media assets. 
  
An effective solution for managing digital assets specifies the following:
  
- The metadata to provide for each kind of asset.
    
- The amount of storage space that is required for the assets, and the performance issues to consider for serving the assets to users.
    
- Where to store assets at each stage of the life cycle of an asset.
    
- How to control access to an asset at each stage of its life cycle.
    
- How to move assets within the organization as team members contribute to creation, review, approval, publication, and disposition of assets.
    
- Which policies to apply to assets so that asset-related actions are audited, assets are retained or disposed of correctly, and assets that are important to the organization are protected.
    
- How assets are treated as corporate records, which must be retained according to requirements and corporate guidelines.
    
For information about how to plan a digital asset solution by using SharePoint Server 2013, see [Plan digital asset libraries in SharePoint Server 2013](plan-digital-asset-libraries.md).
  
## Users of an asset library
<a name="Section2"> </a>

Users of an asset library in SharePoint Server 2013 generally fall into one of the following three categories:
  
- **Asset creators.** This includes people who create individual assets, such as graphic artists, video producers, or marketing copywriters, and who submit assets to the asset library. For example, a graphic artist might create a product logo in multiple resolutions and sizes, and in both color and black and white, and then upload all versions of the logo to the asset library for use by other members of a product marketing team. 
    
- **Asset managers.** This includes people who manage the assets in the library. They are in charge of the end-to-end workflow from the time that an asset is first submitted, through publication, to the time when an asset expires. They are also in charge of managing and organizing assets in the library. For example, an asset manager might take multiple versions of a product logo and categorize them appropriately in the library, add important metadata such as keywords, and set a date after which the asset cannot be used. 
    
- **Asset consumers.** This includes people who have to find and use assets from the library to create other work products. For example, web designers can use a product logo from the asset library when they create marketing pages for product websites. 
    
Depending on the scenario, there can be crossover between these users. For example, users who have permission to upload assets to the library may also have permission to categorize and manage the assets they submit to the archive. Asset creators can also be asset consumers if they look for and use assets that are added to other work products, which in turn are uploaded as separate assets. For example, a video producer might use a product logo while making a marketing video for a product, and then upload the video to the library as a separate asset.
  
## Managing digital assets in SharePoint Server 2013
<a name="Section3"> </a>

SharePoint Server 2013 provides a library template named Asset Library that is customized to use new image, audio, and video content types designed specifically for storing and cataloging rich media assets. These new content types use new column types such as Preview, Picture Size, Date Picture Taken, and Length (seconds) that contribute to the metadata for a particular asset. The asset library also has a preview mode that displays a thumbnail and some of this metadata when you rest the pointer over an asset. Enterprise keywords can be assigned to assets to make them more easily discovered by searching. Keywords can be assigned by an asset creator when a new asset is uploaded, or keywords can be added later by an asset manager. Users can rate assets, a capability that provides additional metadata for assets. The metadata can then be used when assets are displayed in a Web Part. For example, if you have a library of training videos that users have viewed and rated, you can use a Web Part to display the top-rated videos on a web page.
  
Asset creators and asset managers work directly in the asset library to upload, categorize, and manage assets. Asset consumers can browse the library to find assets for inserting into projects in other applications. Asset consumers can browse an asset library from Office applications and insert an asset into the open application, such as Word or PowerPoint.
  
You can display digital assets to users in SharePoint Server 2013 in the following ways:
  
- Allow users to browse the asset library.
    
- Insert a Web Part into a web page on a team site.
    
- Use the video field control on a publishing page on a publishing site.
    
- Use the Content Query Web Part.
    
The specific methods that you use to display assets to users of the asset library will vary depending on who the users are, how they have to use assets from the library, and which methods for displaying assets are most appropriate for a scenario.
  
In addition to the features that are part of the asset library, you can take advantage of SharePoint Server 2013 features such as workflows, routing, rules, and policies. These features help manage the assets as they come into the asset library, track the progress of assets, automate publication of assets on approval, and set the expiration for assets.
  
## Scenarios for using the asset library
<a name="Section4"> </a>

Users with Edit permissions can add an asset library to any SharePoint Server 2013 site collection or site. The following table describes possible scenarios in which you might use a digital asset library.
  
|**Scenario**|**Description**|
|:-----|:-----|
|Corporate brand library  <br/> |The asset library stores branded corporate assets such as logos, artwork, and other digital assets, and workflows and policies help manage the content. Creative teams can submit digital assets to the asset library where they are reviewed and published. Content stewards manage and edit the digital assets to make sure that they are correctly tagged and organized. Information workers and extranet partners who want corporate logos or brand assets use the library to find the content they require.  <br/> |
|Divisional portal  <br/> |The asset library is a repository for images and rich media files for a single portal site. In this scenario, any contributor or designer can upload logos and images to the library for other people to view and use. The content is typically managed by contributors, and there is minimal workflow or policy associated with adding and managing content. For example, the divisional portal library might have multiple contributors but only a few approvers. Authors and web designers of the site use content in the library by viewing, downloading, and inserting it into their work products, such as documents or presentations.  <br/> |
|Team site  <br/> |Similar to a divisional portal but smaller. The asset library is a repository for images and rich media for a single team site. In this scenario, any team member can upload assets to the library for other team members to view and use. The content is managed as necessary by contributors, and there is minimal workflow or policy. Team members use content in the library by viewing, downloading, and inserting it into their work products, such as documents or presentations.  <br/> |
|Corporate archive  <br/> |The asset library stores pictures, video, documents, and other assets that have historical value to the organization. Users can submit current and past items, which are collected, scanned, organized, and tagged by curators who manage the library so that other users can browse, search, and view archived content.  <br/> |
|Divisional media sharing site  <br/> |The asset library stores audio and video files. In this scenario, anyone can contribute to the library, and there is minimal or no management of items in the library. Ratings are enabled for the library, and are combined with social tagging of assets to drive the structure and presentation of assets within the library.  <br/> |
   

