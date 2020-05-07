---
title: "Monitor cache performance in SharePoint Server 2016"
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
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: a2609bd3-928a-479a-9c8d-c0a751d76fcf
description: "Learn how to monitor the SharePoint BLOB cache, the ASP.NET output cache, and the SharePoint object cache."
---

# Monitor cache performance in SharePoint Server 2016

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
By monitoring cache performance, you can make sure that that the farm cache settings are correct and that the caching is running at maximum performance. 
  
## About cache monitoring
<a name="about"> </a>

SharePoint Server 2016 provides three types of caches that help improve the speed at which web pages load in the browser: the BLOB cache, the ASP.NET output cache, and the object cache. 
  
- The **BLOB cache** is a disk-based cache that stores binary large object files that are used by web pages to help the pages load quickly in the browser. 
    
- The **ASP.NET output cache** stores the rendered output of a page. It also stores different versions of the cached page, based on the permissions of the users who are requesting the page. 
    
- The **object cache** reduces the traffic between the web server and the SQL database by storing objects such as lists and libraries, site settings, and page layouts in memory on the front-end web server. As a result, the pages that require these items can be rendered quickly, increasing the speed with which pages are delivered to the client browser. 
    
Monitoring consists of regularly viewing specific performance monitors and making adjustments in the settings to correct any performance issues. The monitors measure cache hits, cache misses, cache compactions, and cache flushes. The following list describes each of these performance monitors.
  
- A **cache hit** occurs when the cache receives a request for an object whose data is already stored in the cache. A high number of cache hits indicates good performance and a good end-user experience. 
    
- A **cache miss** occurs when the cache receives a request for an object whose data is not already stored in the cache. A high number of cache misses might indicate poor performance and a slower end-user experience. 
    
- **Cache compaction** (also known as trimming), happens when a cache becomes full and additional requests for non-cached content are received. During compaction, the system identifies a subset of the contents in the cache to remove, and removes them. Typically these contents are not requested as frequently. 
    
    Compaction can consume a significant portion of the server's resources. This can affect both server performance and the end-user experience. Therefore, compaction should be avoided. You can decrease the occurrence of compaction by increasing the size of the cache. Compaction usually happens if the cache size is decreased. Compaction of the object cache does not consume as many resources as the compaction of the BLOB cache.
    
- A **cache flush** is when the cache is completely emptied. After the cache is flushed, the cache hit to cache miss ratio will be almost zero. Then, as users request content and the cache is filled up, that ratio increases and eventually reaches an optimal level. A consistently high number for this counter might indicate a problem with the farm, such as constantly changing library metadata schemas. 
    
You can monitor the effectiveness of the cache settings to make sure that the end-users are getting the best experience possible. Optimum performance occurs when the ratio of cache hits to cache misses is high and when compactions and flushes only rarely occur. If the monitors do not indicate these conditions, you can improve performance by changing the cache settings. 
  
The following sections provide specific information for monitoring each kind of cache.
  
## Monitoring BLOB cache performance
<a name="blob"> </a>

You can monitor the effectiveness of the cache settings by using the performance monitors that are listed in the following table. 
  
**SharePoint Publishing Cache counter group**

|**Counter name**|**Ideal value or pattern**|**Notes**|
|:-----|:-----|:-----|
|Total Number of cache Compactions  <br/> |0  <br/> |If this number is continually or frequently high, the cache size is too small for the data being requested. To improve performance, increase the size of the cache.  <br/> |
|BLOB Cache % full  <br/> |\>= 90% shows red  <br/> \>= 80% shows yellow  <br/> \<80% shows green  <br/> |This can show that the cache size is too small. To improve performance, increase the size of the cache.  <br/> |
|Publishing cache flushes / second  <br/> |0  <br/> |Site owners might be performing actions on the sites that are causing the cache to be flushed. To improve performance during peak-use hours, make sure that site owners only perform these actions during off-peak hours.  <br/> |
|Publishing cache hit ratio  <br/> |Depends on usage pattern. For read-only sites, the ratio should be 1. For read-write sites, the ratio may be lower.  <br/> |A low ratio can indicate that unpublished items are being requested, and these cannot be cached. If this is a portal site, the site might be set to require check-out, or many users have items checked out.  <br/> |
   
> [!NOTE]
> For the BLOB cache, a request is only counted as a cache miss if the user requests a file whose extension is configured to be cached. For example, if the cache is enabled to cache .jpg files only, and the cache gets a request for a .gif file, that request is not counted as a cache miss. 
  
## Monitoring ASP.NET output cache performance
<a name="output"> </a>

You can monitor the effectiveness of the cache settings by using the performance monitors that are listed in the following table. 
  
**ASP.NET Applications counter group**

|**Counter name**|**Ideal value or pattern**|**Notes**|
|:-----|:-----|:-----|
|Cache API trims  <br/> |0  <br/> |Increase the amount of memory that is allocated to the ASP.NET output cache.  <br/> |
|Cache API hit ratio  <br/> |Depends on usage pattern. For read-only sites, the ratio should be 1. For read-write sites, the ratio may be lower.  <br/> | Potential causes of a low hit ratio include the following:  <br/>  If you are using anonymous user caching (for example, for an Internet-facing site), users are regularly requesting content that has not yet been cached.  <br/>  If you are using ASP.NET output caching for authenticated users, many users may have edit permissions on the pages that they are viewing.  <br/>  If you have customized any of the **VaryBy\*** parameters on any page (or master page or page layout) or customized a cache profile, you may have configured a parameter that prevents the pages in the site from being cached effectively (For example, you might be varying by user for a site that has many users).  <br/> |
   
> [!NOTE]
> For the ASP.NET output cache, all pages are cached for a fixed duration that is independent of user actions. Therefore, there are flush-related monitoring events. 
  
For more information about the ASP.NET output cache, see [Output Caching and Cache Profiles](https://go.microsoft.com/fwlink/p/?LinkID=121543) (https://go.microsoft.com/fwlink/p/?LinkID=121543) or [cache Element for caching (ASP.NET Settings Schema)](https://go.microsoft.com/fwlink/p/?LinkId=195986) (https://go.microsoft.com/fwlink/p/?LinkId=195986). 
  
## Monitoring object cache performance
<a name="object"> </a>

The object cache is used to store metadata about sites, libraries, lists, list items, and documents that are used by features such as site navigation and the Content Query Web Part. This cache helps users when they browse to pages that use these features because the data that they require is stored or retrieved directly from the object cache instead of from the content database.
  
The object cache is stored in the RAM of each web server in the farm. Each web server maintains its own object cache.
  
You can monitor the effectiveness of the cache settings by using the performance monitors that are listed in the following table. 
  
**SharePoint Publishing Cache counter group**

|**Counter name**|**Ideal value or pattern**|**Notes**|
|:-----|:-----|:-----|
|Total number of cache compactions  <br/> |0  <br/> |If this number is high, the cache size is too small for the data being requested. To improve performance, increase the size of the cache.  <br/> |
|Publishing cache flushes / second  <br/> |0  <br/> |Site owners might be performing actions on the sites that are causing the cache to be flushed. To improve performance during peak-use hours, make sure that site owners perform these actions only during off-peak hours.  <br/> |
|Publishing cache hit ratio  <br/> |Depends on usage pattern. For read-only sites, the ratio should be 1. For read-write sites, the ratio may be lower.  <br/> | If the ratio starts to decrease, this might be caused by one or more of the following:  <br/>  The cache was recently flushed or compacted.  <br/>  Users are accessing content that was recently added to the site. This might occur after lots of new content is added to the site.  <br/> |
   

