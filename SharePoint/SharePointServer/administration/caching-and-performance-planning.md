---
title: "Plan for caching and performance in SharePoint Server"
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.date: 7/25/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: fd6a6c07-1979-4254-873c-f146fb630de5
description: "Learn about the BLOB cache, Bit Rate Throttling, and other SharePoint Server features that can improve browser performance."
---

# Plan for caching and performance in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
SharePoint Server provides a disk-based binary large object (BLOB) cache that reduces database load and increases browser performance for users. This article describes the BLOB cache, tells you how and when to use it, and lists key considerations for planning to use it. This article also contains information about when to use Bit Rate Throttling, an Internet Information Services (IIS) 7.0 extension that improves video performance for users when serving videos as part of managing digital assets in SharePoint Server. Finally, this article also discusses the other types of caches that are available in SharePoint Server, describes the limitations of upload file size restrictions, and lists considerations for adjusting the size limit for file transfers on the server.
  
For information about how to enable the BLOB cache, see [Configure cache settings for a web application in SharePoint Server](cache-settings-configuration-for-a-web-application.md). For information about managing digital assets, see [Plan digital asset libraries in SharePoint Server 2013](../sites/plan-digital-asset-libraries.md).
  
## Disk-based BLOB caching
<a name="Section1"> </a>

This section describes the disk-based BLOB cache, and provides important information about how to plan to use the cache with a SharePoint Server deployment. It tells how to decide when to use the BLOB cache, where to store it, how to enable it, and how to configure the size of the cache to get the best performance for users.
  
### BLOB cache overview
<a name="Section1a"> </a>

The disk-based BLOB cache controls the caching for binary large objects (BLOBs), such as frequently used image, audio, and video files, and other files that are used to display web pages, such as .css and .js files. The BLOB cache is enabled on a front-end web server and improves performance by retrieving BLOB files from the database and storing them in a directory on the front-end web end server where they are served to users. This reduces the network traffic to and load on the database server.
  
The BLOB cache also provides features that support serving media files to users. One such feature is support for byte-range requests, which lets users select a later point in the video and immediately begin playback. Another feature is progressive caching, which starts serving the beginning of a large video file while the rest of the file is being cached. Video files are divided and retrieved in smaller sections to reduce the load between the front-end and back-end servers. An administrator can configure the size of the sections.
  
The BLOB cache is also a prerequisite for using the image renditions feature. Image renditions let you display different sized versions of an image on different pages in a publishing site, based on the same source image. When you create an image rendition, you specify the width and height for all images that use that image rendition. For more information, see [How to: Manage image renditions in SharePoint ](https://msdn.microsoft.com/en-us/library/jj720398.aspx) in the MSDN Library. 
  
### Decide whether to use the BLOB cache
<a name="Section1b"> </a>

When enabled, the BLOB cache caches various image, audio, and video files, together with .css and .js files. An administrator can change the settings to add or remove file name extensions of file types to be cached. This functionality lets you either cache as many file types as possible, or to restrict the cache to certain kinds of files. For example, if you have an Internet-facing portal with read-only files such as .doc or .pdf files, you can specify that those files be cached so that they are displayed more quickly to users. If you have a collaboration site that contains files that are frequently updated, and also media assets, you can specify that the cache is to store only audio or video types by including only file name extensions for those files in the cache settings.
  
Before you enable the BLOB cache, carefully consider the scenario in which you plan to use it. If your site will be used for heavy collaboration, enabling the BLOB cache might temporarily affect the performance of your site while the files to be cached are first written to the disk. After the files have been stored in the cache, site performance will improve, so take this into consideration when you decide whether to enable the cache. Base your decision to enable BLOB caching on the following criteria:
  
- For a publishing site for which most of the visitors are anonymous or where most of the files are static content, enable the BLOB cache for as many file types as possible.
    
- For a publishing site that plans to use the image renditions feature, you must enable the BLOB cache.
    
- For other sites that contain lots of media assets that are read-only, or where only a small percentage of the media assets are updated, enable the BLOB cache for media files only.
    
There is one BLOB cache per web application. If you plan to use the BLOB cache together with an asset library that you expect will be large, or together with a site that will receive lots of traffic, consider putting the site collection that contains the asset library into its own web application so that it receives its own BLOB cache. This will ensure that other assets are not using up space in the BLOB cache that you want allocated to items in the asset library. It will also ensure that sites which receive lots of traffic do not prevent other sites which receive less traffic from benefitting from the BLOB cache.
  
### Store the BLOB cache
<a name="Section1c"> </a>

When you enable the BLOB cache, you must specify a location on the front-end web server where the files will be stored. By default, the cache will be created on the drive on which SharePoint Server is installed. Make sure that you put the BLOB cache on a drive that has sufficient disk space available in which to store the cache. Also, select a drive that will be used by as few processes as possible so that the BLOB cache process does not encounter conflicts when it tries to access the drive. If too many processes compete for disk access on the drive where the BLOB cache is located, BLOB cache performance and other processes will be adversely affected.
  
If you plan to use the BLOB cache in a scenario with heavy cache use, such as serving videos in a high traffic environment, and if you will use ULS logging, consider placing the BLOB cache on a separate physical drive from the ULS log — not on a separate partition. Storing the BLOB cache and the ULS log on the same drive can result in poor server performance. If you place the BLOB cache and the ULS log on the same physical drive, make sure that you closely monitor the disk queue length for any performance effect.
  
Each front-end web server has its own local copy of the BLOB cache that is built as requests for files are received. If you use load balancing with multiple front-end web servers, each server contains its own cache. When a file is requested by the first server, it is cached to that server only. If the next request for the same file comes from a second server, a second request is sent to the database server to retrieve the file to the cache on the second server.
  
### Enable the BLOB cache
<a name="Section1d"> </a>

The BLOB cache is configured in the web.config file for each web application and, by default, is not enabled. You must specifically enable the BLOB cache to get the performance advantage it provides. For information about how to enable the BLOB cache, see [Configure cache settings for a web application in SharePoint Server](cache-settings-configuration-for-a-web-application.md).
  
### Specify the size of the BLOB cache
<a name="Section1e"> </a>

When you decide how large to make the BLOB cache, you must consider the number and size of the files to determine the total size of the data to be stored in the cache. By default, the BLOB cache is set to 10 gigabytes (GB). Allow at least 20 percent more space on the drive than the size of the cache. For example, if you have 100 GB of content, set the size of the cache to 120 GB on a drive that has at least 150 GB of space. If the BLOB cache is too small, serving files to users slows, reducing the performance of your site.
  
If you plan to use the image renditions feature on your site, you should account for each rendition being a separate BLOB in the cache. For example, if you plan to have five renditions per image, then you must allocate significantly more than the general estimate of 20 percent more space on the drive.
  
## Output cache, object cache, and anonymous search results cache
<a name="section4"> </a>

In addition to the BLOB cache, SharePoint Server provides the following types of caches that help improve the speed at which web pages load in the browser:
  
> [!NOTE]
> You must be using the Publishing feature on your site to use the output cache or the object cache. 
  
- **Output cache**: Stores the rendered output of a page. It also stores different versions of the cached page, based on the permissions of the users who are requesting the page.
    
    Cache profiles describe specific cache settings for each type of page output cache. Cache profile settings can be configured in the user interface at the site collection level by a site collection administrator, and also at the web application level by an administrator on the front-end web server. The page output cache must be enabled at the site collection level before page output cache profiles can be configured at either the site collection level or web application level. For more information, see [Configure cache profile settings](cache-settings-configuration-for-a-web-application.md#output).
    
- **Object cache**: Reduces the traffic between the web server and the SQL database by storing objects such as lists and libraries, site settings, and page layouts in memory on the front-end web server. As a result, the pages that require these items can be rendered quickly, increasing the speed with which pages are delivered to the client browser.
    
    The object cache settings can be configured at the site collection level in the user interface by a site collection administrator, and is on by default. The maximum cache size can be configured at the web application level on the front-end web server to place a restriction on the maximum amount of memory that the cache will use for all site collections. For more information, see [Configure object cache settings](cache-settings-configuration-for-a-web-application.md#object).
    
- **Anonymous search results cache**: Used primarily by publishing sites that allow access to anonymous users. The anonymous search results cache saves search results from anonymous users and reuses them for later queries that are the same as the original query. This improves performance on site pages that use the Content Search Web Part.
    
## Bit Rate Throttling
<a name="Section2"> </a>

This section contains information about Bit Rate Throttling, describes when you should use it with the SharePoint Server solution, and explains how to enable it.
  
### Bit Rate Throttling overview
<a name="Section2a"> </a>

Bit Rate Throttling is an IIS 7.0 extension that meters the download speeds of media file types and data between a server and a client computer. The encoded bit rates of media file types such as Windows Media Video (WMV), MPEG-4 (MP4), and Adobe Flash Video, are automatically detected, and the rate at which those files are delivered to the client over HTTP are controlled according to the Bit Rate Throttling configuration. For more information, see [Bit Rate Throttling](https://go.microsoft.com/fwlink/p/?LinkId=155151).
  
### Decide to use Bit Rate Throttling
<a name="Section2b"> </a>

If you will make long-playing video assets available to users in SharePoint Server, enable Bit Rate Throttling in IIS. Without Bit Rate Throttling, IIS will serve video files by using as much bandwidth as it can, which will result in increased network performance. When you enable Bit Rate Throttling in IIS, it will serve video files that use only as much bandwidth as is needed to support progressive downloading and viewing of videos. When the BLOB cache is also enabled, Bit Rate Throttling uses extension rules for files cached to disk. Files that are served from the BLOB cache by using Bit Rate Throttling are sent to the client based on a percentage of the compressed size using the encoded bit rate. For example, if the videos in your organization are smaller than 10 MB, you may decide not to use Bit Rate Throttling because it will affect how fast users can download videos to their local computers. However, if you are serving video files, enable Bit Rate Throttling to control the speed at which files are downloaded to client computers.
  
> [!NOTE]
> Bit rate throttling will not work correctly if you do not first enable the BLOB cache and configure it to cache the files types that you want to throttle. 
  
### Enable Bit Rate Throttling
<a name="Section2c"> </a>

To enable Bit Rate Throttling in IIS 7.0, you must install IIS Media Services 2.0. For information about how to install IIS Media Services 2.0, see [Bit Rate Throttling Readme](https://go.microsoft.com/fwlink/p/?LinkID=154962). For information about how to configure Bit Rate Throttling, see [Bit Rate Throttling Configuration Walkthrough](https://go.microsoft.com/fwlink/p/?LinkId=155153).
  
## Maximum upload file size
<a name="Section3"> </a>

This section describes the upload file size limitation, tells how to decide what the maximum upload file size limit should be, and how to configure it.
  
### Maximum upload file size overview
<a name="Section3a"> </a>

The maximum upload file size is a setting that is used by the SharePoint Server web application that specifies the maximum size of a file that a user can upload to the server. When a new web application is created, SharePoint Server sets the default maximum upload size to 250 MB. If a user tries to upload a file larger than the specified maximum upload size, the upload will fail.
  
### Decide maximum upload file size
<a name="Section3b"> </a>

Every user that uploads a file to a library uses a connection to the server and increases the amount of data in the database. This impacts the load, response time and data capacity for a server. Depending on your scenario, this can negatively impact your server performance if the server is not configured to handle larger volumes of files. To determine what the upload file size limit should be for your server, consider the number of users for your site, and the size of the files they will upload. For example, if your users will primarily be uploading video files that are 500 MB, the upload file size limit should be large enough to easily accommodate the largest files users will upload. When planning to adjust the upload file size limit, keep in mind that this will also directly impact capacity planning for your server environment. For more information about planning for storage of large media files, see [Plan digital asset libraries in SharePoint Server 2013](../sites/plan-digital-asset-libraries.md). 
  
### Configure the maximum upload file size
<a name="Section3c"> </a>

To configure the upload file size in SharePoint Server, a farm administrator must change the **Maximum Upload Size** value on the Web Application General Settings page in Central Administration. 
  
> [!NOTE]
> If you increase the default maximum upload size for a web application, and you also plan to use content deployment to move content from site collections within that web application to another farm or site collection, you must also increase the default maximum upload size on the destination server, or the content deployment job will fail. 
  
## See also
<a name="Section3"> </a>

#### Concepts

[Monitor cache performance in SharePoint Server 2016](monitor-cache-performance.md)

