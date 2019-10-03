---
title: "Configure properties of the Search Box Web Part in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 3/9/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 766e0169-1a5d-4730-9c9f-7e2b27ba7d5d
description: "Learn how to configure properties of the Search Box Web Part."
---

# Configure properties of the Search Box Web Part in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
By default, the Search Box Web Part is used on the home page for the Search Center (default.aspx), and all search results pages (results.aspx, peopleresults.aspx, conversationresults.aspx, videoresults.aspx). By changing properties in the Search Box Web Part you can you can do the following:
  
- Change the Web Part or page where the search results should be displayed — for example, a custom Search Results Web Part or a custom search results page.
    
- Turn off query suggestions and people suggestions. For more information about query suggestions, see [Manage query suggestions in SharePoint Server](manage-query-suggestions.md)
    
- Display links to a search preference page and an advanced search page.
    
- Change the display template that is applied to the Web Part.
    
## Before you begin
<a name="begin"> </a>

> [!NOTE]
> Because SharePoint Server runs as websites in Internet Information Services (IIS), administrators and users depend on the accessibility features that browsers provide. SharePoint Server supports the accessibility features of supported browsers. For more information, see the following resources: 
>- [Plan browser support](https://go.microsoft.com/fwlink/p/?LinkId=246502)
>- [Accessibility for SharePoint 2013](/SharePoint/accessibility-guidelines)
>- [Accessibility features in SharePoint 2013 Products](https://go.microsoft.com/fwlink/p/?LinkId=246501)
>- [Keyboard shortcuts](https://go.microsoft.com/fwlink/p/?LinkID=246504)
>- [Touch](https://go.microsoft.com/fwlink/p/?LinkId=246506)
    
## Configure properties of the Search Box Web Part
<a name="begin"> </a>

 **To configure the properties of a Search Box Web Part**
  
1. Verify that the user account that performs this procedure is a member of the Designers SharePoint group on the Enterprise Search Center site.
    
2. On the Search Center site home page, click the **Settings** menu, and then click **Edit Page**.
    
3. In the Web Part, click the **Search Box Web Part Menu** arrow, and then click **Edit Web Part**.
    
4. In the Web Part tool pane, in the **Properties for Search Box** section, expand the **Which search results page should queries be sent to** section, and then do the following: 
    
  - To display the settings that are defined on the Search Settings page, select the **Use this site's Search Settings** check box. 
    
  - To override the settings that are defined on the Search Settings page, clear the **Use this site's Search Settings** check box, and then do the following: 
    
    - To display search results in a Web Part on the page, in the section **Send queries to other Web Parts on this page**, select a Web Part.
    
      > [!NOTE]
      > If there are no other Web Parts on a page, search results will be sent to the search results page as specified on the Search Settings page. 
  
  - To send queries to a custom search results page, select **Send queries to a custom results page URL**, and then type the URL of the custom search results page.
    
    > [!NOTE]
    > You can't send queries to a custom search results page that uses a friendly URL. 
  
5. In the Web Part tool pane, in the **Properties for Search Box** section, expand the **Query Suggestions** section, and then do the following: 
    
  - To disable query suggestions, clear the **Show suggestions** check box. 
    
  - To specify additional properties for query suggestions, change the values in the following fields:
    
    - **Number of query suggestions:** How many query suggestions to display. 
    
    - **Minimum number of characters:** How many characters the user must type before query suggestions are displayed. 
    
    - **Suggestions delay (in milliseconds):** How many milliseconds elapse before query suggestions are displayed. 
    
    - **Number of personal favorites:** How many query suggestions are displayed to the user under the text **Are you looking for these again?** in the search results. These suggestions are based on search results that the user has clicked previously. To disable personal favorite results, clear the **Show personal favorite results** check box. 
    
  - To turn on people name suggestions, select **Show people name suggestions**.
    
6. In the Web Part tool pane, in the **Properties for Search Box** section, expand the **Settings** section, and then do the following: 
    
  - To show a link to a search preference page, select **Show preferences link**.
    
  - To show a link to an advanced search page, select **Show advanced link**, and then in the **Advanced search page URL** box, type the URL of the advanced search page that you want to link to. 
    
  - To apply another display template, in the **Search box control Display Template** list, select the display template that you want to apply to the Web Part. 
    
  - Select the **Make the search box have focus when the page is loaded** check box to make it possible for users to immediately type a query in the search box when the page is loaded without first having to click the search box. By default, this is selected. 
    
## See also
<a name="begin"> </a>

[How to change the text that is displayed in the Search Box Web Part in SharePoint Server 2013](https://blogs.technet.com/b/tothesharepoint/archive/2013/09/19/how-to-change-the-text-that-is-displayed-in-the-search-box-web-part-in-sharepoint-server-2013.aspx)

