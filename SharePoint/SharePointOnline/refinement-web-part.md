---
title: "Change settings for the Refinement Web Part"
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
ms.assetid: fc0a2cb2-4947-4df8-ace2-3486ad8318b3
description: "Learn how to customize refiners on search results pages by changing settings in the Refinement Web Part. The Refinement Web Part filters search results into categories called refiners."
---

# Change settings for the Refinement Web Part

The Refinement Web Part filters search results into categories called refiners. Users can click these refiners to narrow search results to find what they're looking for more easily. 
  
By default, the Refinement Web Part is used on all default search vertical pages in the Enterprise Search Center, which are the search results pages for **Everything**, **People**, **Conversations**, and **Videos**.
  
As a global or SharePoint admin in Office 365, you can change how the Refinement Web Part is set up. You can:
  
- Filter search results from a different Search Results Web Part.
    
- Specify which refiners to show.
    
    > [!NOTE]
    >  Any managed properties that you want to use as refiners must be set to refinable and queryable in the search schema. Also, the content source that contains the managed properties must have been crawled before the properties can be used as refiners. 
  
- Change the display template for a refiner.
    
- Change display names for refiners.
    
- Add counts to refiners.
    
## Change how the Refinement Web Part behaves and looks
<a name="__toc348362488"> </a>

1. On the page that contains the Refinement Web Part, on the **Settings** menu, click **Edit Page**.
    
2. In the Web Part, click the **Refinement Web Part Menu** arrow, and then click **Edit Web Part**. 
    
3. In the Web Part tool pane, in the **Refinement Target** section, select the Web Part that you want to filter search results from. By default, the Search Results Web Part is selected. 
    
4. In the Web Part tool pane, verify that the **Choose Refiners in this Web Part** is selected. 
    
5. Click **Choose Refiners**.
    
6. On the **Refinement configuration** page, from the **Available refiners** section, use the buttons to choose which refiners to show in the Web Part, and also in what order to show them. If you have specified an **Alias** for a refinable managed property, this alias is shown in the **Configuration for** section. 
    
7. In the **Configuration for** section, choose how you want each refiner to look. 
    
    > [!NOTE]
    >  If you've a single language site, you can change the refiner display name in the **Display name** section. For multilingual sites, change the refiner display language as described under [Change the display name for a refiner](refinement-web-part.md#__change_the_display). 
  
8. Click **OK**.
    
## Change the display name for a refiner in the classic search experience
<a name="__change_the_display"> </a>

By default, the name of the managed property will be used as a display name for the refiner. In many cases, the managed property name is hard to understand—for example, **RefinableString00** or **ColorOWSTEXT**. You can fix this by changing the name of the refiner in a JavaScript file.
  
1. On the page that contains the Refinement Web Part, select **Settings** ![Settings icon.](media/a47a06c3-83fb-46b2-9c52-d1bad63e3e60.png), and then select **Site settings**. If you don't see **Site settings**, select **Site information**, and then select **View all site settings**.
    
2. On the **Site Settings** page, in the **Web Designer Galleries** section, click **Master pages and page layouts**. 
    
3. On the **Master Page Gallery** page, click **Display Templates**.
    
4. On the **Display Templates** page, click **Language Files**.
    
5. On the **Language Files** page, click the folder for the relevant language. 
    
6. Open the **CustomStrings.js** file. 
    
7. Add one line for each managed property that you want to change the display name for. Use this syntax: 
    
     `"rf_RefinementTitle_ManagedPropertyName": "Sample Refinement Title for ManagedPropertyName"`
    
    For example, add this line to change the display name for the managed property **RefinableInt00** to **Price**: 
  
      `"rf_RefinementTitle_RefinableInt00": "Price"`

8. Save the file.
    
## Add refiner counts
<a name="__toc348362490"> </a>

By default, the Refinement Web Part doesn't show refiner counts — that is, the number of results for each refiner value. For example, if you've enabled the managed property Color as a refiner, the refiner values will be colors, such as Red, Green, and Blue. You can add refiner counts by changing a value in an HTML file so that the refiner values are shown as Red (10), Green (12), and Blue (8).
  
1. On the page that contains the Refinement Web Part, select **Settings** ![Settings icon.](media/a47a06c3-83fb-46b2-9c52-d1bad63e3e60.png), and then select **Site settings**. If you don't see **Site settings**, select **Site information**, and then select **View all site settings**.
    
2. On the **Site Settings** page, in the **Web Designer Galleries** section, click **Master pages and page layouts**. 
    
3. On the **Master Page Gallery** page, click **Display Templates**.
    
4. On the **Display Templates** page, click **Filters**.
    
5. Open the **Filter_Default.html** file. 
    
6. Change the value for **ShowCounts** to **true**.
    
7. Save the file.
    
## See also
<a name="__toc348362490"> </a>

[Manage the Search Center in SharePoint Online](manage-search-center.md)
  
[Change settings for the Search Box Web Part](search-box-web-part.md)
  
[Change settings for the Search Navigation Web Part](search-navigation-web-part.md)
  
[Change settings for the Search Results Web Part](https://support.office.com/article/40ff85b3-bc5e-4230-b1dd-f088188e487e)

