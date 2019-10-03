---
title: "Change settings for the Search Box Web Part"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 6/19/2018
audience: Admin
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
search.appverid:
- SPO160
- MET150
ms.assetid: 1915c232-3a41-440a-b5be-b1cdf364b607
description: "Learn how to customize the Search Box Web Part."
---

# Change settings for the Search Box Web Part

The Search Box Web Part shows a text box where users can enter words or phrases to search for information. By default, the Search Box Web Part is used on the home page for the Search Center (default.aspx), and all default search results pages (**Everything**, **People**, **Conversations**, and **Videos**).
  
As a global or SharePoint admin in Office 365, you can change settings in the Search Box Web Part. You can:
  
- Change where the search results should be displayed — for example, show results in a custom Search Results Web Part or a custom search results page.
    
- Turn off query suggestions and people suggestions. 
    
- Show links to a search preference page and an advanced search page.
    
- Change the display template that is used for the Web Part. 
 
    
## Change where search results are displayed
<a name="__toc349558305"> </a>

1. On the Search Center site home page, click the **Settings** menu, and then click **Edit Page**.
    
2. In the Web Part, click the **Search Box Web Part Menu** arrow, and then click **Edit Web Part**.
    
3. In the **Search Box** tool pane, under **Properties for Search Box**, expand **Which search results page should queries be sent to**.
    
  - To use the settings that are defined on the **Search Settings** page, select the **Use this site's Search Settings** check box. 
    
  - To override the settings that are defined on the **Search Settings** page, clear the **Use this site's Search Settings** check box. 
    
  - To show search results in a Web Part on the page, in the section **Send queries to other Web Parts on this page**, select a Web Part.
    
    > [!NOTE]
    >  If there are no other Web Parts on a page, search results will be sent to the search results page that is specified on the **Search Settings** page. 
  
  - To send queries to a different search results page, select **Send queries to a custom results page URL**, and then type the URL of the custom search results page.
    
    > [!NOTE]
    > You can't send queries to a custom search results page that uses a friendly URL. 
  
4. Click **OK**.
    
## Change settings for query suggestions, people suggestions, and personal favorites results
<a name="__toc349558306"> </a>

Personal favorites results are suggestions based on search results that the user has clicked before. Query suggestions are turned on by default.
  
As a global or SharePoint admin in Office 365, you can turn off or on query suggestions, people suggestions, and personal favorites results, or edit the different settings for query suggestions. 
  
1. On the Search Center site home page, click the **Settings** menu, and then click **Edit Page**.
    
2. In the Web Part, click the **Search Box Web Part Menu** arrow, and then click **Edit Web Part**.
    
3. In the **Search Box** tool pane, under **Properties for Search Box**, expand the **Query Suggestions** section. 
    
  - To turn off query suggestions, clear the **Show suggestions** check box. 
    
  - To change how many query suggestions to show, type the maximum number in the **Number of query suggestions** box. 
    
  - To change how many characters the user must type before query suggestions are shown, edit the number in the **Minimum number of characters** box. 
    
  - To change how many milliseconds elapse before query suggestions are shown, edit the number in the **Suggestions delay (in milliseconds)** box. 
    
  - To change how many query suggestions are shown under the text **Are you looking for these again?** in the search results, change the value for **Number of personal favorites**: Personal favorite results are based on search results that the user has clicked before. To disable personal favorite results, clear **Show personal favorite results**. 
    
  - To turn on people name suggestions, select **Show people name suggestions**.
    
4. Click **OK**.
    
## Show links or change the display template
<a name="__toc349558307"> </a>

1. On the Search Center site home page, click the **Settings** menu, and then click **Edit Page**.
    
2. In the Web Part, click the **Search Box Web Part Menu** arrow, and then click **Edit Web Part**.
    
3. In the **Search Box** tool pane, under **Properties for Search Box**, expand the **Settings** section: 
    
  - To show a link to a search preference page, select **Show preferences link**.
    
  - To show a link to an advanced search page, select **Show advanced link**, and then in the **Advanced search page URL** box, type the URL of the advanced search page that you want to link to. 
    
  - To apply another display template, in the **Search box control Display Template** list, select the display template that you want to apply to the Web Part. 
    
  - Select the **Make the search box have focus when the page is loaded** check box so that users can immediately type a query in the search box when the page is loaded without first having to click the search box. This option is selected by default. 
    
4. Click **OK**.
    
## See also
<a name="__toc349558307"> </a>

[Manage the Search Center in SharePoint Online](manage-search-center.md)
  
[Change settings for the Search Navigation Web Part](search-navigation-web-part.md)
  
[Change settings for the Refinement Web Part](refinement-web-part.md)
  
[Change settings for the Search Results Web Part](https://support.office.com/article/40ff85b3-bc5e-4230-b1dd-f088188e487e)

