---
title: Configure cache settings for a web application in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: 478be4b7-1480-4f97-87c5-b18cd2436bce
---


# Configure cache settings for a web application in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-19* **Summary: ** Learn how to configure the BLOB cache, page output cache profiles, and the object cache for a web application.This article describes how to configure the disk-based BLOB cache, the page output cache profiles, and the object cache for a web application in SharePoint Server 2016 and SharePoint Server 2013.You enable and configure the BLOB cache, and make configuration changes to the page output cache profiles and the object cache in the Web.config file in the web application to which you want to apply those changes. The changes you make to the Web.config file will be applied to all site collections within the web application. SharePoint Server 2016 includes cache performance monitors that let you verify that the farm cache settings are correct and that the caching is running at maximum performance. For more information, see  [Monitor cache performance in SharePoint Server 2016](html/monitor-cache-performance-in-sharepoint-server-2016.md).
> [!NOTE:]

  
    
    


> [!TIP:]

  
    
    

For more information, see  [Cache settings operations in SharePoint Server](html/cache-settings-operations-in-sharepoint-server.md).In this article:
-  [Configuring BLOB cache settings](#BLOB)
    
  
-  [Configuring page output cache profile settings](#output)
    
  
-  [Configuring object cache settings](#object)
    
  

## Configure BLOB cache settings
<a name="BLOB"> </a>

By default, the disk-based BLOB cache is off and must be enabled on the front-end web server if you want to use it. Use the following procedure to configure disk-based cache settings for a web application.
> [!IMPORTANT:]

  
    
    

 **To configure BLOB cache settings**
1. Verify that you have the following administrative credentials: You must be a member of the Administrators group on the local computer to configure the BLOB cache settings.
    
  
2. Open **Server Manager**, click **Tools**, and then click **Internet Information Services (IIS) Manager**.
    
  
3. In Internet Information Services (IIS) Manager, in the **Connections** pane, expand the server name that contains the web application, and then expand **Sites** to view the web application or applications that have been created.
    
  
4. Right-click the name of the web application for which you want to configure the disk-based cache, and then click **Explore**. Windows Explorer opens, with the directories for the selected web application listed.
    
  
5. In the **Open With** dialog box, click **Notepad**, and then click **OK**.
    
  
6. In the web.config Notepad file, find the following line: <BlobCache location="C:\\BlobCache\\14" path="\\.(gif|jpg|jpeg|jpe|jfif|bmp|dib|tif|tiff|themedbmp|themedcss|themedgif|themedjpg|themedpng|ico|png|wdp|hdp|css|js|asf|avi|flv|m4v|mov|mp3|mp4|mpeg|mpg|rm|rmvb|wma|wmv|ogg|ogv|oga|webm|xap)$" maxSize="10" enabled="false" />
    
    > [!NOTE:]
      
7. In this line, change the location attribute to specify a directory that has enough space to accommodate the cache size.
    
    > [!NOTE:]
      
8. To add or remove file types from the list of file types to be cached, for the path attribute, modify the regular expression to include or remove the appropriate file extension. If you add file extensions, make sure to separate each file type with a pipe (|), as shown in this line of code.
    
  
9. To change the size of the cache, type a new number for maxSize. The size is expressed in gigabytes (GB), and 10 GB is the default.
    
    > [!IMPORTANT:]
      
10. To enable the BLOB cache, change the enabled attribute, from"false" to"true".
    
  
11. Save the Notepad file, and then close it.
    
  

> [!CAUTION:]

  
    
    


## Configure cache profile settings
<a name="output"> </a>

Cache profile settings can be configured in the user interface at the site collection level by a site collection administrator, as well as at the web application level by an administrator on the front-end web server. The page output cache must be enabled at the site collection level before page output cache profiles can be configured at either the site collection level or web application level. If page output cache profiles are enabled at the web application level, the settings specified in Web.config will be used for all page output cache profiles, overriding any values that have been entered through the user interface at the site collection level.
> [!NOTE:]

  
    
    


> [!NOTE:]

  
    
    

Use the following procedure to configure the cache profile settings for a web application.
> [!IMPORTANT:]

  
    
    

 **To configure page output cache profile settings**
1. Verify that you have the following administrative credentials: You must be a member of the Administrators group on the local computer to configure the cache profile settings.
    
  
2. Open **Server Manager**, click **Tools**, and then click **Internet Information Services (IIS) Manager**.
    
  
3. In Internet Information Services (IIS) Manager, in the **Connections** pane, expand the server name that contains the web application, and then expand **Sites** to view the web application or applications that have been created.
    
  
4. Right-click the name of the web application for which you want to configure the disk-based cache, and then click **Explore**. Windows Explorer opens, with the directories for the selected web application listed.
    
  
5. Right-click **web.config**, click **Open** and choose **Notepad** if you're asked to find a program to use to open this file.
    
  
6. In the web.config Notepad file, find the following line: <OutputCacheProfiles useCacheProfileOverrides="false" varyByHeader="" varyByParam="*"  varyByCustom="" varyByRights="true" cacheForEditRights="false" />
    
  
7. To enable the cache profile at the web application level, change the useCacheProfileOverrides attribute, from"false" to"true".
    
    > [!NOTE:]
      
8. To override the varyByHeader attribute, type a custom parameter as specified in the .NET Framework Class Library entry [HttpCachePolicy.VaryByHeaders Property](https://msdn.microsoft.com/en-us/library/system.web.httpcachepolicy.varybyheaders%28v=vs.110%29.aspx).
    
  
9. To override the varyByParam attribute, type a custom parameter as specified in the .NET Framework Class Library entry [HttpCachePolicy.VaryByParams Property](http://go.microsoft.com/fwlink/p/?LinkId=164242&amp;clcid=0x409).
    
  
10. To override the varyByCustom attribute, type a custom parameter as specified in the .NET Framework Class Library entry [HttpCachePolicy.SetVaryByCustom Method](http://go.microsoft.com/fwlink/p/?LinkId=164240&amp;clcid=0x409).
    
  
11. To override the varyByRights attribute, change the value from"true" to"false". This will remove the requirement that users must have identical effective permissions on all securable objects to see the same cached page as any other user.
    
  
12. To override the cacheForEditRights attribute, change thecacheForEditRights attribute, from"false" to"true". This will bypass the normal behavior in which people with edit permissions have their pages cached.
    
  
13. Save the Notepad file, and then close it.
    
  

> [!CAUTION:]

  
    
    


## Configure object cache settings
<a name="object"> </a>

The object cache settings can be configured at the site collection level in the user interface by a site collection administrator, and is on by default. The maximum cache size can be configured at the web application level on the front-end web server to place a restriction on the maximum amount of memory that the cache will use for all site collections. For example, individual site collections might have the object cache set at 100 MB, while the web application might be set at 1 GB. In this case, no more than 1 GB of memory will be used by all the caches on the server.
> [!NOTE:]

  
    
    

Use the following procedure to configure the object cache settings for a web application on a front-end web server.
> [!IMPORTANT:]

  
    
    

 **To configure object cache settings**
1. Verify that you have the following administrative credentials: You must be a member of the Administrators group on the local computer to configure the object cache settings.
    
  
2. Open **Server Manager**, click **Tools**, and then click **Internet Information Services (IIS) Manager**.
    
  
3. In Internet Information Services (IIS) Manager, in the **Connections** pane, expand the server name that contains the web application, and then expand **Sites** to view the web application or applications that have been created.
    
  
4. Right-click the name of the web application for which you want to configure the disk-based cache, and then click **Explore**. Windows Explorer opens, with the directories for the selected web application listed.
    
  
5. Right-click **web.config**, click **Open** and select **Notepad** if you're asked to find a program to use to open this file.
    
  
6. In the Web.config Notepad file, find the following line: <ObjectCache maxSize="100" />
    
  
7. To change the size of the cache, type a new number for maxSize. The size is expressed in megabytes (MB), and 100 MB is the default.
    
  
8. Save the Notepad file, and then close it.
    
  

> [!CAUTION:]

  
    
    


# See also

#### 

 [Cache settings operations in SharePoint Server](html/cache-settings-operations-in-sharepoint-server.md)
  
    
    
 [Plan for caching and performance in SharePoint Server](html/plan-for-caching-and-performance-in-sharepoint-server.md)
  
    
    

  
    
    

