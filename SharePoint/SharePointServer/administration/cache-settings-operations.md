---
title: "Cache settings operations in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/20/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 0ae2f59b-309e-4853-8ce7-99bc40de4c03
description: "Learn about the available caches and the settings that can be configured for the BLOB cache and cache profiles and object cache settings in SharePoint Server."
---

# Cache settings operations in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
SharePoint Server provides four types of caches that help improve the speed at which web pages load in the browser: the BLOB cache, the page output cache, the object cache, and the anonymous search results cache. The BLOB cache is enabled and configured in the Web.config file in the web application to which you want to apply the cache. The page output cache and object cache areis usually configured in the user interface at the site collection level. Certain settings for these caches can also be configured at the web application level. The changes that you make to the Web.config file will be applied to all site collections and sites within the web application, and will supersede any configuration made at the site collection level or below.
  
> [!NOTE]
> To use the page output cache or the object cache, you must be using the Publishing feature on your site. 
  
### BLOB cache
<a name="section3"> </a>

SharePoint Server provides a disk-based cache that stores files that are used by web pages to help them load quickly in the browser, and reduces the load on the database server when it uses those files. These files are known as binary large objects (BLOBs), and the cache is known as the BLOB cache. The BLOB cache is stored directly on the hard disk drive of a front-end web server computer. The first time that a web page is called, these files are copied from the database to the cache on the server hard disk drive, and all subsequent requests for those files are then served from the hard disk drive cache of the server. By default, the BLOB cache is off and must be enabled to use the functionality it provides. When you enable the BLOB cache on your front-end web server, you reduce the load on the SharePoint Server database server created by read requests from web browsers.
  
You enable the BLOB cache in the Web.config file of the web application to which you want to apply it. The changes that you make to the Web.config file will be applied to all site collections within the web application. For information about the BLOB cache, see [Plan for caching and performance in SharePoint Server](caching-and-performance-planning.md).
  
### Page output cache profiles
<a name="section1"> </a>

The page output cache stores the rendered output of a page. It also stores different versions of the cached page, based on the permissions of the users who are requesting the page. Page output cache settings can be configured at the site collection level, at the site level, and for page layouts. By default, the page output cache is turned off.
  
The page output cache uses cache profiles that specify how long items should be held in the cache. You can specify different cache profiles to be used for anonymous and authenticated users, which optimizes the use of the cache based on the authentication methods that are allowed on the site.
  
You can configure cache profile settings for a web application by editing the Web.config file on the application server. The cache profile settings that you configure at the web application level will be used for all cache profiles in the site collections for that web application. 
  
> [!NOTE]
> There is a known issue with the Content Search Web Part. The SendContentBeforeQuery setting in the Web Part does not work correctly on pages that use output caching. This issue is resolved in the SharePoint Server 2013 cumulative update for March 2013. For more information, see Microsoft Knowledge Base article 2767999: [Description of the SharePoint Server 2013 update: March 12, 2013](http://go.microsoft.com/fwlink/p/?LinkId=286308). 
  
> [!NOTE]
> To use the page output cache and the associated cache profile settings, you must be using the Publishing feature on your site. 
  
### Object cache
<a name="section2"> </a>

The object cache reduces the amount of traffic between the web server and the SQL database by storing objects —such as lists and libraries, site settings, and page layouts —in memory on the front-end web server computer. As a result, the pages that require these items can be rendered quickly, increasing the speed with which pages are delivered to the client browser. Object cache settings can be configured at the web application level, and at the site collection level. By default, the object cache is on at the site collection level.
  
You can optimize the object cache for a web application by specifying the size of the object cache. Specifying a larger number can enhance performance for some large sites at the cost of memory on each front-end web server. You can configure other settings for the object cache at site collection level.
  
> [!NOTE]
> To use the object cache, you must be using the Publishing feature on your site. 
  
### Anonymous search results cache
<a name="section2"> </a>

The anonymous search results cache is primarily used by publishing sites that allow access to anonymous users. It saves search results from anonymous users and reuses them for later queries that are the same as the original query. This improves performance on site pages that use the Content Search Web Part.
  
> [!NOTE]
> There is a known issue in which Content Search Web Part and the Catalog-Item Reuse Web Part do not use the anonymous search results cache on category pages. This issue is resolved in the SharePoint Server 2013 cumulative update for March 2013. For more information, see Microsoft Knowledge Base article 2767999: [Description of the SharePoint Server 2013 update: March 12, 2013](http://go.microsoft.com/fwlink/p/?LinkId=286308).

>  [!NOTE]
>  If you have category pages that you created before the cumulative update was installed, you must re-create the category pages. Save the layouts and any customizations on the original category pages that you want to keep. Disconnect and then reconnect to the catalog, and then copy the customizations to the new category pages.
  
## Articles about cache settings

The following articles about cache settings are available. 
  
- [Configure cache settings for a web application in SharePoint Server](cache-settings-configuration-for-a-web-application.md) - Describes how to configure the disk-based BLOB cache, the page output cache profiles, and the object cache for a web application. 
    
- [Configure object cache user accounts in SharePoint Server](configure-object-cache-user-accounts.md) - Describes how to configure the object cache user accounts. 
    
- [Flush the BLOB cache in SharePoint Server](flush-the-blob-cache.md) - Describes how to clear the contents of the BLOB cache for a web application. 
    
## See also

#### Concepts

[Plan for caching and performance in SharePoint Server](caching-and-performance-planning.md)
  
[Monitor cache performance in SharePoint Server 2016](monitor-cache-performance.md)

