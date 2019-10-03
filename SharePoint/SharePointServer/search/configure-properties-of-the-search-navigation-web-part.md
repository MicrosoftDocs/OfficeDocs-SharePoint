---
title: "Configure properties of the Search Navigation Web Part in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 3/8/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 79428586-0a1c-4fd8-ae49-e1e76eb022e1
description: "Learn how to configure properties of the Search Navigation Web Part, and how to add a link to a new search vertical page."
---

# Configure properties of the Search Navigation Web Part in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
The Search Navigation Web Part is configured to display links to the search verticals **Everything**, **People**, **Conversations** and **Videos**. It uses search results from the Search Results Web Part so that when users click a search vertical link, the search results are filtered and displayed following the configuration of the search vertical. You can also create your own search vertical and add it to be displayed in the Search Navigation Web Part. 
  
By changing properties on the Search Navigation Web Part you can do the following:
  
- Specify a different Web Part from which search results are received.
    
- Change the number of search vertical links to display.
    
The search vertical properties, such as display name and links, are configured on the Search Settings page for the corresponding site.
  
    
## Before you begin
<a name="begin"> </a>

> [!NOTE]
> Because SharePoint Server runs as websites in Internet Information Services (IIS), administrators and users depend on the accessibility features that browsers provide. SharePoint Server supports the accessibility features of supported browsers. 
  
For more information, see the following resources:
  
- [Plan browser support](https://go.microsoft.com/fwlink/p/?LinkId=246502)
    
- [Accessibility for SharePoint 2013](/SharePoint/accessibility-guidelines)
    
- [Accessibility features in SharePoint 2013 Products](https://go.microsoft.com/fwlink/p/?LinkId=246501)
    
- [Keyboard shortcuts](https://go.microsoft.com/fwlink/p/?LinkID=246504)
    
- [Touch](https://go.microsoft.com/fwlink/p/?LinkId=246506)
    
## Configure the properties of the Search Navigation Web Part
<a name="BKMK_ConfigureSearchNavigation"> </a>

 **To configure the properties of a Search Navigation Web Part**
  
1. Verify that the user account that performs this procedure is a member of the Designers SharePoint group on the Enterprise Search Center site.
    
2. On the search results page, click the **Settings** menu, and then click **Edit Page**.
    
3. In the Search Navigation Web Part, click the **Search Navigation Web Part** menu arrow, and then click **Edit Web Part**.
    
4. In the Web Part tool pane, in the **Control** section, do the following: 
    
  - To receive search results from another Web Part on the page, in the **Use Current Query from** list, select a Web Part. 
    
  - To change the number of search vertical links to display before overflowing, in the **Maximum Links Before Overflow** box, type a number. 
    
## Change the properties of a search vertical in the Search Navigation Web Part
<a name="BKMK_ChangeProperties"> </a>

 **To change the properties of a search vertical in the Search Navigation Web Part**
  
1. Verify that the user account that performs this procedure is a member of the Owners group on the Enterprise Search Center site.
    
2. On the **Settings** menu for the site, click **Site Settings**.
    
3. On the **Site Settings** page, in the **Search** section, click **Search Settings**.
    
4. On the **Search Settings** page, in the **Configure Search Navigation** section, click to select the search vertical for which you want to change the properties, and then click **Edit**.
    
5. In the **Navigation Link** dialog box, do the following: 
    
  - To change the display name of a search vertical, in the **Title** field, type a display name. 
    
  - To change the URL of the search vertical, in the **URL** field, type a URL. 
    
    > [!NOTE]
    > You can't use a page that uses a friendly URL for your search vertical. 
  
6. On the **Search Settings** page, click **OK** to save the changes. 
    
## Add a search vertical to the Search Navigation Web Part
<a name="BKMK_AddSearchVertial"> </a>

Before you start this procedure, verify that you have created a new page for the search vertical. We recommend that you copy one of the existing search vertical pages — for example, **results.aspx**, and then modify the copy to create a new page.
  
 **To add a search vertical to the Search Navigation Web Part**
  
1. Verify that the user account that performs this procedure is a member of the Owners group on the Enterprise Search Center site.
    
2. On the **Settings** menu for the site, click **Site Settings**.
    
3. On the **Site Settings** page, in the **Search** section, click **Search Settings**.
    
4. On the **Search Settings** page, in the **Configure Search Navigation** section, click **Add Link**.
    
5. In the **Navigation Link** dialog box, do the following: 
    
  - In the **Title** field, type a display name. 
    
  - In the **URL** field, type the URL to the new search vertical. 
    
  - Click **OK** to save the new search vertical. 
    

