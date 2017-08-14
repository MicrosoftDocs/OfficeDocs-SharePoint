---
title: Cache settings operations in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: 0ae2f59b-309e-4853-8ce7-99bc40de4c03
---


# Cache settings operations in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-19* **Summary: ** Learn about the available caches and the settings that can be configured for the BLOB cache and cache profiles and object cache settings in SharePoint Server 2016 and SharePoint Server 2013.SharePoint Server provides four types of caches that help improve the speed at which web pages load in the browser: the BLOB cache, the page output cache, the object cache, and the anonymous search results cache. The BLOB cache is enabled and configured in the Web.config file in the web application to which you want to apply the cache. The page output cache and object cache areis usually configured in the user interface at the site collection level. Certain settings for these caches can also be configured at the web application level. The changes that you make to the Web.config file will be applied to all site collections and sites within the web application, and will supersede any configuration made at the site collection level or below.
> [!NOTE:]

  
    
    


## BLOB cache
<a name="section3"> </a>

SharePoint Server provides a disk-based cache that stores files that are used by web pages to help them load quickly in the browser, and reduces the load on the database server when it uses those files. These files are known as binary large objects (BLOBs), and the cache is known as the BLOB cache. The BLOB cache is stored directly on the hard disk drive of a front-end web server computer. The first time that a web page is called, these files are copied from the database to the cache on the server hard disk drive, and all subsequent requests for those files are then served from the hard disk drive cache of the server. By default, the BLOB cache is off and must be enabled to use the functionality it provides. When you enable the BLOB cache on your front-end web server, you reduce the load on the SharePoint Server database server created by read requests from web browsers.You enable the BLOB cache in the Web.config file of the web application to which you want to apply it. The changes that you make to the Web.config file will be applied to all site collections within the web application. For information about the BLOB cache, see  [Plan for caching and performance in SharePoint Server](html/plan-for-caching-and-performance-in-sharepoint-server.md).
## Page output cache profiles
<a name="section1"> </a>

The page output cache stores the rendered output of a page. It also stores different versions of the cached page, based on the permissions of the users who are requesting the page. Page output cache settings can be configured at the site collection level, at the site level, and for page layouts. By default, the page output cache is turned off.The page output cache uses cache profiles that specify how long items should be held in the cache. You can specify different cache profiles to be used for anonymous and authenticated users, which optimizes the use of the cache based on the authentication methods that are allowed on the site.You can configure cache profile settings for a web application by editing the Web.config file on the application server. The cache profile settings that you configure at the web application level will be used for all cache profiles in the site collections for that web application. 
> [!NOTE:]

  
    
    


> [!NOTE:]

  
    
    


## Object cache
<a name="section2"> </a>

The object cache reduces the amount of traffic between the web server and the SQL database by storing objects —such as lists and libraries, site settings, and page layouts —in memory on the front-end web server computer. As a result, the pages that require these items can be rendered quickly, increasing the speed with which pages are delivered to the client browser. Object cache settings can be configured at the web application level, and at the site collection level. By default, the object cache is on at the site collection level.You can optimize the object cache for a web application by specifying the size of the object cache. Specifying a larger number can enhance performance for some large sites at the cost of memory on each front-end web server. You can configure other settings for the object cache at site collection level.
> [!NOTE:]

  
    
    


## Anonymous search results cache
<a name="section2"> </a>

The anonymous search results cache is primarily used by publishing sites that allow access to anonymous users. It saves search results from anonymous users and reuses them for later queries that are the same as the original query. This improves performance on site pages that use the Content Search Web Part.
> [!NOTE:]

  
    
    


## TechNet articles about cache settings

The following articles about cache settings are available to view online. Writers update articles on a continuing basis as new information becomes available and as users provide feedback.
-  [Configure cache settings for a web application in SharePoint Server](html/configure-cache-settings-for-a-web-application-in-sharepoint-server.md) - Describes how to configure the disk-based BLOB cache, the page output cache profiles, and the object cache for a web application.
    
  
-  [Configure object cache user accounts in SharePoint Server](html/configure-object-cache-user-accounts-in-sharepoint-server.md) - Describes how to configure the object cache user accounts.
    
  
-  [Flush the BLOB cache in SharePoint Server](html/flush-the-blob-cache-in-sharepoint-server.md) - Describes how to clear the contents of the BLOB cache for a web application.
    
  

# See also

#### 

 [Plan for caching and performance in SharePoint Server](html/plan-for-caching-and-performance-in-sharepoint-server.md)
  
    
    
 [Monitor cache performance in SharePoint Server 2016](html/monitor-cache-performance-in-sharepoint-server-2016.md)
  
    
    

  
    
    

