---
title: "Configure cache settings for a web application in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 9/19/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 478be4b7-1480-4f97-87c5-b18cd2436bce
description: "Learn how to configure the BLOB cache, page output cache profiles, and the object cache for a web application."
---

# Configure cache settings for a web application in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
This article describes how to configure the disk-based BLOB cache, the page output cache profiles, and the object cache for a web application in SharePoint Server.
  
You enable and configure the BLOB cache, and make configuration changes to the page output cache profiles and the object cache in the Web.config file in the web application to which you want to apply those changes. The changes you make to the Web.config file will be applied to all site collections within the web application. 
  
SharePoint Server includes cache performance monitors that let you verify that the farm cache settings are correct and that the caching is running at maximum performance. For more information, see [Monitor cache performance in SharePoint Server 2016](monitor-cache-performance.md).
  
> [!NOTE]
> Configuring the page output cache profiles and the object cache at the web application level will supersede any configuration that was made by site administrators at the site collection level or below. 
  
> [!TIP]
> There may be times when the BLOB cache becomes out of sync with the content. For example, after you restore a content database, the BLOB cache will be out of sync with the content. To correct that situation, you must flush the BLOB cache. For more information, see [Flush the BLOB cache in SharePoint Server](flush-the-blob-cache.md). 
  
For more information, see [Cache settings operations in SharePoint Server](cache-settings-operations.md).
  
    
## Configure BLOB cache settings
<a name="BLOB"> </a>

By default, the disk-based BLOB cache is off and must be enabled on the front-end web server if you want to use it. Use the following procedure to configure disk-based cache settings for a web application.
  
> [!IMPORTANT]
> Before you make changes to the web.config file, make a copy of it by using a different name (for example, web.config1), so that if a mistake is made in the file, you can restore the original file. 
  
 **To configure BLOB cache settings**
  
1. Verify that you have the following administrative credentials: You must be a member of the Administrators group on the local computer to configure the BLOB cache settings.
    
2. Open **Server Manager**, click **Tools**, and then click **Internet Information Services (IIS) Manager**.
    
3. In Internet Information Services (IIS) Manager, in the **Connections** pane, expand the server name that contains the web application, and then expand **Sites** to view the web application or applications that have been created. 
    
4. Right-click the name of the web application for which you want to configure the disk-based cache, and then click **Explore**. Windows Explorer opens, with the directories for the selected web application listed.
    
5. In the **Open With** dialog box, click **Notepad**, and then click **OK**.
    
6. In the web.config Notepad file, find the following line:  `<BlobCache location="C:\BlobCache\14" path="\.(gif|jpg|jpeg|jpe|jfif|bmp|dib|tif|tiff|themedbmp|themedcss|themedgif|themedjpg|themedpng|ico|png|wdp|hdp|css|js|asf|avi|flv|m4v|mov|mp3|mp4|mpeg|mpg|rm|rmvb|wma|wmv|ogg|ogv|oga|webm|xap)$" maxSize="10" enabled="false" />`
    
   The default max size for an image when using Image Renditions is 40 mega pixels. Should you want to modify this value you will need to add the imageRenditionMaxSourcePixels parameter. For example:
   `<BlobCache location="C:\BlobCache\14" path="\.(gif|jpg|jpeg|jpe|jfif|bmp|dib|tif|tiff|themedbmp|themedcss|themedgif|themedjpg|themedpng|ico|png|wdp|hdp|css|js|asf|avi|flv|m4v|mov|mp3|mp4|mpeg|mpg|rm|rmvb|wma|wmv|ogg|ogv|oga|webm|xap)$" maxSize="10" imageRenditionMaxSourcePixels="100000000" enabled="true" />`
   This will set the max image size for Image Renditions to work at around 100 mega pixels.
  
7. In this line, change the  `location` attribute to specify a directory that has enough space to accommodate the cache size. 
    
    > [!NOTE]
    > We strongly recommend that you specify a directory that is not on the same drive as where either the server operating system swap files or server log files are stored. 
  
8. To add or remove file types from the list of file types to be cached, for the  `path` attribute, modify the regular expression to include or remove the appropriate file extension. If you add file extensions, make sure to separate each file type with a pipe (|), as shown in this line of code. 
    
9. To change the size of the cache, type a new number for  `maxSize`. The size is expressed in gigabytes (GB), and 10 GB is the default.
    
    > [!IMPORTANT]
    > It is recommended that you not set the cache size smaller than 10 GB. When you set the cache size, make sure to specify a number large enough to provide a buffer at least 20 percent bigger than the estimated size of the content that will be stored in the cache. 
  
10. To enable the BLOB cache, change the  `enabled` attribute, from  `"false"` to  `"true"`.
    
11. Save the Notepad file, and then close it.
    
> [!CAUTION]
> When you save a change to the web.config file, the web application in Internet Information Services (IIS) 7.0 automatically recycles. This recycling can cause a brief interruption in service to sites contained in that web application, and users can lose session state. For information about recycling web applications in IIS 7.0, see [IIS Process Recycling](https://go.microsoft.com/fwlink/p/?LinkId=154094). 
  
## Configure cache profile settings
<a name="output"> </a>

Cache profile settings can be configured in the user interface at the site collection level by a site collection administrator, as well as at the web application level by an administrator on the front-end web server. The page output cache must be enabled at the site collection level before page output cache profiles can be configured at either the site collection level or web application level. If page output cache profiles are enabled at the web application level, the settings specified in Web.config will be used for all page output cache profiles, overriding any values that have been entered through the user interface at the site collection level.
  
> [!NOTE]
> To use the page output cache and the associated cache profile settings, you must be using the Publishing feature on your site. 
  
> [!NOTE]
> There is a known issue with the Content Search Web Part. The SendContentBeforeQuery setting in the Web Part does not work correctly on pages that use output caching. This issue is resolved in the SharePoint Server 2013 cumulative update for March 2013. For more information, see Microsoft Knowledge Base article 2767999: [Description of the SharePoint Server 2013 update: March 12, 2013](https://go.microsoft.com/fwlink/p/?LinkId=286308). 
  
Use the following procedure to configure the cache profile settings for a web application.
  
> [!IMPORTANT]
> Before you make changes to the web.config file, make a copy of it by using a different name (for example, web.config1), so that if a mistake is made in the file, you can restore the original file. 
  
 **To configure page output cache profile settings**
  
1. Verify that you have the following administrative credentials: You must be a member of the Administrators group on the local computer to configure the cache profile settings.
    
2. Open **Server Manager**, click **Tools**, and then click **Internet Information Services (IIS) Manager**.
    
3. In Internet Information Services (IIS) Manager, in the **Connections** pane, expand the server name that contains the web application, and then expand **Sites** to view the web application or applications that have been created. 
    
4. Right-click the name of the web application for which you want to configure the disk-based cache, and then click **Explore**. Windows Explorer opens, with the directories for the selected web application listed.
    
5. Right-click **web.config**, click **Open** and choose **Notepad** if you're asked to find a program to use to open this file. 
    
6. In the web.config Notepad file, find the following line:  `<OutputCacheProfiles useCacheProfileOverrides="false" varyByHeader="" varyByParam="*" varyByCustom="" varyByRights="true" cacheForEditRights="false" />`
    
7. To enable the cache profile at the web application level, change the  `useCacheProfileOverrides` attribute, from  `"false"` to  `"true"`.
    
    > [!NOTE]
    > If you set this to true the settings specified in Web.config will be used for all page output cache profiles. This overrides any values that have been entered through the user interface at the site collection level. 
  
8. To override the  `varyByHeader` attribute, type a custom parameter as specified in the .NET Framework Class Library entry [HttpCachePolicy.VaryByHeaders Property](https://msdn.microsoft.com/en-us/library/system.web.httpcachepolicy.varybyheaders%28v=vs.110%29.aspx).
    
9. To override the  `varyByParam` attribute, type a custom parameter as specified in the .NET Framework Class Library entry [HttpCachePolicy.VaryByParams Property](http://go.microsoft.com/fwlink/p/?LinkId=164242&amp;clcid=0x409).
    
10. To override the  `varyByCustom` attribute, type a custom parameter as specified in the .NET Framework Class Library entry [HttpCachePolicy.SetVaryByCustom Method](http://go.microsoft.com/fwlink/p/?LinkId=164240&amp;clcid=0x409).
    
11. To override the  `varyByRights` attribute, change the value from  `"true"` to  `"false"`. This will remove the requirement that users must have identical effective permissions on all securable objects to see the same cached page as any other user.
    
12. To override the  `cacheForEditRights` attribute, change the  `cacheForEditRights` attribute, from  `"false"` to  `"true"`. This will bypass the normal behavior in which people with edit permissions have their pages cached.
    
13. Save the Notepad file, and then close it.
    
> [!CAUTION]
> When you save a change to the web.config file, the web application in Internet Information Services (IIS) 7.0 automatically recycles. This recycling can cause a brief interruption in service to sites contained in that web application, and users can lose session state. For information about recycling web applications in IIS 7.0, see [Start or Stop the Web Server (IIS 8)](http://go.microsoft.com/fwlink/?LinkID=718159&amp;clcid=0x409). 
  
## Configure object cache settings
<a name="object"> </a>

The object cache settings can be configured at the site collection level in the user interface by a site collection administrator, and is on by default. The maximum cache size can be configured at the web application level on the front-end web server to place a restriction on the maximum amount of memory that the cache will use for all site collections. For example, individual site collections might have the object cache set at 100 MB, while the web application might be set at 1 GB. In this case, no more than 1 GB of memory will be used by all the caches on the server.
  
> [!NOTE]
> To use the object cache, you must be using the Publishing feature on your site. 
  
Use the following procedure to configure the object cache settings for a web application on a front-end web server.
  
> [!IMPORTANT]
> Before you make changes to the web.config file, make a copy of it by using a different name (for example, web.config1), so that if a mistake is made in the file, you can restore the original file. 
  
 **To configure object cache settings**
  
1. Verify that you have the following administrative credentials: You must be a member of the Administrators group on the local computer to configure the object cache settings.
    
2. Open **Server Manager**, click **Tools**, and then click **Internet Information Services (IIS) Manager**.
    
3. In Internet Information Services (IIS) Manager, in the **Connections** pane, expand the server name that contains the web application, and then expand **Sites** to view the web application or applications that have been created. 
    
4. Right-click the name of the web application for which you want to configure the disk-based cache, and then click **Explore**. Windows Explorer opens, with the directories for the selected web application listed.
    
5. Right-click **web.config**, click **Open** and select **Notepad** if you're asked to find a program to use to open this file. 
    
6. In the Web.config Notepad file, find the following line:  `<ObjectCache maxSize="100" />`
    
7. To change the size of the cache, type a new number for  `maxSize`. The size is expressed in megabytes (MB), and 100 MB is the default.
    
8. Save the Notepad file, and then close it.
    
> [!CAUTION]
> When you save a change to the web.config file, the web application in Internet Information Services (IIS) 7.0 automatically recycles. This recycling can cause a brief interruption in service to sites contained in that web application, and users can lose session state. For information about recycling web applications in IIS 7.0, see [Start or Stop the Web Server (IIS 8)](http://go.microsoft.com/fwlink/?LinkID=718159&amp;clcid=0x409). 
  
## See also
<a name="object"> </a>

#### Concepts

[Cache settings operations in SharePoint Server](cache-settings-operations.md)
  
[Plan for caching and performance in SharePoint Server](caching-and-performance-planning.md)

