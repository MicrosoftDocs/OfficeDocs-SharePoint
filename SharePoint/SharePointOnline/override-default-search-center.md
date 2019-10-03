---
title: "Specify search settings for a site collection or a site"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 6/21/2018
audience: Admin
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
search.appverid:
- SPO160
- MET150
ms.assetid: 99da1d77-f42b-4f56-b48a-24e87f336e91
description: "Learn how to specify how search should behave for a site collection or a site. The shared Search Box at the top of most pages will use these settings."
---

# Specify search settings for a site collection or a site

As a global or SharePoint admin, you can specify how search should behave for a classic site collection or a site. The shared Search Box at the top of most classic pages uses these search settings. Any settings you specify on site collection level applies to all sites within that site collection, unless you specify other settings for the site.
 
You can specify where searches should go for your classic site collection or site by specifying the URL of your Search Center. For example, if you have created an Enterprise Search Center on your site where users can search everything in your company, you can enter the URL of that site here. If you do not enter a Search Center URL, searches will go to the default Search Center, available at \<host_name\>/search/.
  
When you create an Enterprise Search Center site collection SharePoint creates a default search home page and a default search results page. In addition, several pages known as search verticals are also created. Search verticals are customized for searching specific content, such as People, Conversations, and Videos, and they display search results that are filtered and formatted for a specific content type or class. 
  
For more on creating and customizing a search center for your site, see [Manage the Search Center in SharePoint Online](manage-search-center.md).
  
You can change which search results page queries are sent to. By default, queries are sent to the same search results page as the parent, but you can override this for a site collection or a site. 
  
You can also configure search navigation for a site. With search navigation, users can move quickly between different search vertical pages. Navigation links are shown in the Search Navigation Web Part on search result pages, and can also be shown as a drop-down menu in the search box.
  
> [!NOTE]
>  It may take up to 30 minutes before changes take effect. 
  
## Specify search settings for a site collection
<a name="__toc349306989"> </a>

1. On the site, select **Settings** ![Settings icon.](media/a47a06c3-83fb-46b2-9c52-d1bad63e3e60.png), and then select **Site settings**. If you don't see **Site settings**, select **Site information**, and then select **View all site settings**.

2. Under **Site Collection Administration**, click **Search Settings**.
    
3. To specify a Search Center, in the **Search Center URL** box, type the URL of the Search Center site. 
    
4. To change which search result page queries are sent to, in the section **Which search results page should queries be sent to?**, clear **Use the same results page settings as my parent**, and then select one of the following: 
    
  - **Send queries to a custom results page URL**. Enter the URL. Custom URLs can be relative or absolute, and can also include special tokens, such as {SearchCenterURL}. 
    
    Example: /SearchCenter/Pages/results.aspx or http://server/sites/SearchCenter/Pages/results.aspx.
    
  - **Turn on the drop-down menu inside the search box, and use the first Search Navigation node as the destination results page**. If you choose this option, users can choose search vertical in the search box when they enter a query. 
    
5. Click **OK**.
    
## Specify search settings for a site
<a name="__toc349306990"> </a>

By default, a site has the same search settings as the site collection that the site belongs to. You can, however, override these settings by defining specific search settings for the site.
  
1. On the site, select **Settings** ![Settings icon.](media/a47a06c3-83fb-46b2-9c52-d1bad63e3e60.png), and then select **Site settings**. If you don't see **Site settings**, select **Site information**, and then select **View all site settings**.

2. Under **Search**, click **Search Settings**.
    
3. To specify a Search Center, in the **Search Center URL** box, type the URL of the Search Center site. 
    
4. To change which search result page queries are sent to, in the section **Which search results page should queries be sent to?**, clear **Use the same results page settings as my parent**, and then select one of the following: 
    
  - **Send queries to a custom results page URL**. Enter the URL. Custom URLs can be relative or absolute, and can also include special tokens, such as {SearchCenterURL}. 
    
    Example: /SearchCenter/Pages/results.aspx or http://server/sites/SearchCenter/Pages/results.aspx.
    
  - **Turn on the drop-down menu inside the search box, and use the first Search Navigation node as the destination results page**. Make sure that the search vertical you want as a default is the first option in the **Configure Search Navigation** section. 
    
5. To configure search navigation, edit settings in the **Configure Search Navigation** section as required. You can, for example: 
    
  - Change the display name or the URL of a search vertical
    
  - Change the order of the search vertical links
    
  - Add a search vertical
    
    See [Change settings for the Search Navigation Web Part](search-navigation-web-part.md) for steps. 
    
6. Click **OK**.
    

