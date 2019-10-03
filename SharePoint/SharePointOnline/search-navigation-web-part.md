---
title: "Change settings for the Search Navigation Web Part"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 6/29/2018
audience: Admin
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
search.appverid:
- SPO160
- MET150
ms.assetid: 7c1a7462-d3d8-4a14-92f4-981b0ade9963
description: "Learn how to customize the Search Navigation Web Part. The Search Navigation Web Part on search results pages contains links that let users move quickly between search verticals."
---

# Change settings for the Search Navigation Web Part

The Search Navigation Web Parts shows links that let users move quickly between the different search pages, known as search verticals. Search verticals are predesigned to give users different search experiences depending on what they are looking for. For example, if users click the **People** link, they are taken to the people search vertical, which is a search page specifically set up to display people information.
  
By default, the Search Navigation Web Part is set up to show links to the search verticals **Everything**, **People**, **Conversations** and **Videos**. The Search Navigation Web Part uses search results from the Search Results Web Part so that when users click a search vertical link, the search results are filtered and displayed according to how the search vertical is set up. 
  
As a global or SharePoint admin in Office 365, you can change how the Search Navigation Web Part is set up by specifying a different Web Part to get the results from, change how many links to show, and change the appearance and layout of the Web Part. You make these changes by editing the properties in the Web Part tool pane.
  
To make other changes, such as changing display names for the links, or change their order, go to the **Search Settings** for the corresponding site. Here, you can also add a link to a new search vertical to be shown in the Web Part. 
  
## Change the settings for the Search Navigation Web Part
<a name="__toc347912378"> </a>

Here's how you can change the set-up of the Search Navigation Web Part. You can specify a different Web Part to get the results from, change how many links to show, and change the appearance and layout of the Web Part. 
  
1. On the search results page, click the **Settings** menu, and then click **Edit Page**.
    
2. In the Search Navigation Web Part, click the **Search Navigation Web Part** menu arrow, and then click **Edit Web Part**.
    
3. In the Web Part tool pane, in the **Control** section: 
    
  - To receive search results from another Web Part on the page, in the **Use Current Query from** list, select a Web Part. 
    
  - To change the number of search vertical links to display before overflowing, in the **Maximum Links Before Overflow** box, type a number. 
    
4. To change how the Web Part looks, edit the settings in the **Appearance** and **Layout** sections. 
    
5. Click **OK**.
    
## Change the display name or the URL of a search vertical
<a name="__toc347912379"> </a>

1. On the site, select **Settings** ![Settings icon.](media/a47a06c3-83fb-46b2-9c52-d1bad63e3e60.png), and then select **Site settings**. If you don't see **Site settings**, select **Site information**, and then select **View all site settings**.
    
2. On the **Site Settings** page, in the **Search** section, click **Search Settings**.
    
3. On the **Search Settings** page, in the **Configure Search Navigation** section, click to select the search vertical that you want to change, and then click **Edit**.
    
4. In the **Navigation Link** dialog box: 
    
  - To change the display name of a search vertical, in the **Title** field, type a display name. 
    
  - To change the URL of the search vertical, in the **URL** field, type a URL. 
    
    > [!NOTE]
    > You can't use a page that uses a friendly URL for your search vertical. 
  
5. Click **OK**.
    
## Change the order of the search vertical links
<a name="__toc347912380"> </a>

1. On the site, select **Settings** ![Settings icon.](media/a47a06c3-83fb-46b2-9c52-d1bad63e3e60.png), and then select **Site settings**. If you don't see **Site settings**, select **Site information**, and then select **View all site settings**.
    
2. On the **Site Settings** page, in the **Search** section, click **Search Settings**.
    
3. On the **Search Settings** page, in the **Configure Search Navigation** section, click to select a search vertical. 
    
4. Click **Move Up** or **Move Down** to change the display order. 
    
5. Click **OK**.
    
## Add a search vertical to the Search Navigation Web Part
<a name="__toc347912381"> </a>

As a global or SharePoint admin in Office 365, you can create a new search vertical page and add it to the Search Navigation Web Part. When you create a new page, we recommend that you copy one of the existing search vertical pages — for example, **results.aspx**, and then modify the copy to create a new page.
  
Here's how you can add a link to the new search vertical page in the Web Part:
  
1. On the site, select **Settings** ![Settings icon.](media/a47a06c3-83fb-46b2-9c52-d1bad63e3e60.png), and then select **Site settings**. If you don't see **Site settings**, select **Site information**, and then select **View all site settings**.
    
2. On the **Site Settings** page, in the **Search** section, click **Search Settings**.
    
3. On the **Search Settings** page, in the **Configure Search Navigation** section, click **Add Link**.
    
4. In the **Navigation Link** dialog box: 
    
  - In the **Title** field, type a display name. 
    
  - In the **URL** field, type the URL of the new search vertical. 
    
  - Click **OK** to save the new search vertical. 
    
5. To change the display order, use the **Move Up** or **Move Down** buttons. 
    
6. Click **OK**.
    
## See also
<a name="__toc347912381"> </a>

[Manage the Search Center in SharePoint Online](manage-search-center.md)
  
[Change settings for the Search Box Web Part](search-box-web-part.md)
  
[Change settings for the Refinement Web Part](refinement-web-part.md)
  
[Change settings for the Search Results Web Part](https://support.office.com/article/40ff85b3-bc5e-4230-b1dd-f088188e487e)

