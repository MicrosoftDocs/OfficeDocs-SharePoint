---
title: "Result types and display templates that are used to display classic search results in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/26/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 7a690328-78c5-4dc2-b03f-30165ad186c1
description: "Learn about the default result types and display templates that are used to display search results."
---

# Result types and display templates that are used to display classic search results in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
SharePoint Server includes many default search features that do a great job in helping users find what they're looking for. But you might want your search results to look a certain way, for example, display information that's specific to your company or business. To customize how search results look and what information they contain, you can create new result types and display templates or change existing ones. This article does not describe how you can do this, but gives an overview of the default result types and display templates that are used to display search results.
  
    
## About result types
<a name="BKMK_AboutSearchResults"> </a>

When you search for something on a SharePoint site, very often many search results are returned. By default, the search results are displayed differently so that you can easily differentiate between the different types of search results. For example, just by glancing at the image below you can see that the first two search results are PowerPoint presentations, the third result is a Word document, and so on.
  
![Search results displayed according to result type](../media/ContosoSearchResults.png)
  
To display search results differently like this, search results are sorted into **result types**. A result type is a classification of a search result. For example, if a search result is found in a Microsoft PowerPoint presentation, the search result belongs to the **Microsoft PowerPoint** result type. If a search result is found in a PDF file, the search result belongs to the **PDF** result type. 
  
The following table shows the default result types.
  
|**Result type**|**Search result found in**|
|:-----|:-----|
|Person  <br/> |The **Local People Results** result source  <br/> |
|Microsoft Access  <br/> |A Microsoft Access file  <br/> |
|Microsoft Excel  <br/> |A Microsoft Excel file  <br/> |
|Microsoft OneNote  <br/> |A Microsoft OneNote file  <br/> |
|Microsoft PowerPoint  <br/> |A Microsoft PowerPoint file  <br/> |
|Microsoft Publisher  <br/> |A Microsoft Publisher file  <br/> |
|Microsoft Visio  <br/> |A Microsoft Visio file  <br/> |
|Microsoft Word  <br/> |A Microsoft Word file  <br/> |
|Discussion  <br/> |An entry within a community site  <br/> |
|Reply  <br/> |A reply to an e-mail  <br/> |
|Email  <br/> |An e-mail  <br/> |
|Image  <br/> |An image file  <br/> |
|PDF  <br/> |A PDF file  <br/> |
|Text  <br/> |A TXT file  <br/> |
|Video  <br/> |A video file  <br/> |
|XML  <br/> |An XML file  <br/> |
|Zip  <br/> |A ZIP file  <br/> |
|SharePoint Blog  <br/> |A SharePoint Blog site  <br/> |
|SharePoint Community  <br/> |A SharePoint Community Site  <br/> |
|SharePoint Discussion Board  <br/> |A SharePoint Discussion Board library  <br/> |
|SharePoint Document Library  <br/> |A SharePoint Document library  <br/> |
|SharePoint List  <br/> |A SharePoint list  <br/> |
|SharePoint MicroBlog Post  <br/> |A blog post within a SharePoint Blog Site  <br/> |
|SharePoint Picture Library  <br/> |A SharePoint Picture library  <br/> |
|SharePoint site  <br/> |A SharePoint site  <br/> |
|SharePoint Survey  <br/> |A SharePoint survey  <br/> |
|SharePoint Wiki  <br/> |A SharePoint Enterprise Wiki Site  <br/> |
|SharePoint Picture Library List Item  <br/> |An item in a SharePoint picture library  <br/> |
|SharePoint List Item  <br/> |An item in a SharePoint list  <br/> |
|Webpage  <br/> |External web pages, for example HTML or ASPX pages  <br/> |
|Default Result Type  <br/> |Anything not covered by the other result types, for example Java files, C++ or C#  <br/> |
   
## How result types and display templates are connected
<a name="BKMK_Association"> </a>

In a SharePoint Search Center, search results are displayed in a **Search Results Web Part**. To control how the search results are displayed, two types of display templates are used:
  
1. **Item display template**
    
2. **Hover panel display template**
    
![Display templates used to control how the search results are displayed](../media/Contoso_Search_Display_Templates.gif)
  
The item display template defines how each result is displayed. The hover panel display template shows additional information when a user hovers with the mouse pointer over a search result. 
  
The following diagram shows how result types and display templates are connected.
  
![How result types and display templates are connected](../media/Result_type_display_template1B.gif)
  
1. Each result type refers to an item display template.
    
2. Each item display template contains a variable that refers to a hover panel display template. This variable is  `var hoverUrl`. 
    
The following table shows how the default result types are connected to item display templates and hover panel display templates.
  
|**Result type**|**Item display template title as shown in the user interface**|**Item display template file name as shown in the Master Page Gallery**|**Hover panel display template file name as shown in the Master Page Gallery**|
|:-----|:-----|:-----|:-----|
|Person  <br/> |People Item  <br/> |Item_Person  <br/> |Item_Person_HoverPanel  <br/> |
|Microsoft Access  <br/> |Office Document Item  <br/> |Item_OfficeDocument  <br/> |Item_OfficeDocument_HoverPanel  <br/> |
|Microsoft Excel  <br/> |Excel Item  <br/> |Item_Excel  <br/> |Item_Excel_HoverPanel  <br/> |
|Microsoft OneNote  <br/> |OneNote Item  <br/> |Item_OneNote  <br/> |Item_OneNote_HoverPanel  <br/> |
|Microsoft Powerpoint  <br/> |PowerPoint Item  <br/> |Item_PowerPoint  <br/> |Item_PowerPoint_HoverPanel  <br/> |
|Microsoft Publisher  <br/> |Office Document Item  <br/> |Item_OfficeDocument  <br/> |Item_OfficeDocument_HoverPanel  <br/> |
|Microsoft Visio  <br/> |Office Document Item  <br/> |Item_OfficeDocument  <br/> |Item_OfficeDocument_HoverPanel  <br/> |
|Microsoft Word  <br/> |Word Item  <br/> |Item_Word  <br/> |Item_Word_HoverPanel  <br/> |
|Discussion  <br/> |Discussion  <br/> |Item_Discussion  <br/> |Item_Discussion_HoverPanel  <br/> |
|Reply  <br/> |Reply Item  <br/> |Item_Reply  <br/> |Item_Reply_HoverPanel  <br/> |
|Email  <br/> |Default Item  <br/> |Item_Default  <br/> |Item_Default_HoverPanel  <br/> |
|Image  <br/> |Default Item  <br/> |Item_Default  <br/> |Item_Default_HoverPanel  <br/> |
|PDF  <br/> |PDF Item  <br/> |Item_PDF  <br/> |Item_PDF_HoverPanel  <br/> |
|Text  <br/> |Default Item  <br/> |Item_Default  <br/> |Item_Default_HoverPanel  <br/> |
|Video  <br/> |Video Item  <br/> |Item_Video  <br/> |Item_Video_HoverPanel  <br/> |
|XML  <br/> |Default Item  <br/> |Item_Default  <br/> |Item_Default_HoverPanel  <br/> |
|Zip  <br/> |Default Item  <br/> |Item_Default  <br/> |Item_Default_HoverPanel  <br/> |
|SharePoint Blog  <br/> |Default Item  <br/> |Item_Default  <br/> |Item_Default_HoverPanel  <br/> |
|SharePoint Community  <br/> |Community Item  <br/> |Item_Community  <br/> |Item_Community_HoverPanel  <br/> |
|SharePoint Discussion Board  <br/> |Default Item  <br/> |Item_Default  <br/> |Item_Default_HoverPanel  <br/> |
|SharePoint Document Library  <br/> |Default Item  <br/> |Item_Default  <br/> |Item_Default_HoverPanel  <br/> |
|SharePoint List  <br/> |Default Item  <br/> |Item_Default  <br/> |Item_Default_HoverPanel  <br/> |
|SharePoint MicroBlog Post  <br/> |Default Item  <br/> |Item_Default  <br/> |Item_Default_HoverPanel  <br/> |
|SharePoint Picture Library  <br/> |Default Item  <br/> |Item_Default  <br/> |Item_Default_HoverPanel  <br/> |
|SharePoint Site  <br/> |Site Item  <br/> |Item_Site  <br/> |Item_Site_HoverPanel  <br/> |
|SharePoint Survey  <br/> |Default Item  <br/> |Item_Default  <br/> |Item_Default_HoverPanel  <br/> |
|SharePoint Wiki  <br/> |Default Item  <br/> |Item_Default  <br/> |Item_Default_HoverPanel  <br/> |
|SharePoint Picture Library List Item  <br/> |Picture Item  <br/> |Item_Picture  <br/> |Item_Picture_HoverPanel  <br/> |
|SharePoint List Item  <br/> |Default Item  <br/> |Item_Default  <br/> |Item_Default_HoverPanel  <br/> |
|Webpage  <br/> |Web Page Item  <br/> |Item_WebPage  <br/> |Item_WebPage_HoverPanel  <br/> |
|Default Result Type  <br/> |Default Item  <br/> |Item_Default  <br/> |Item_Default_HoverPanel  <br/> |
   
## Common display templates that are used by all result types
<a name="BKMK_Common"> </a>

In addition to the display templates that are listed in the previous section, there are some display templates that are used by all result types. These are called common display templates. The common display templates are referred to from both the item display templates and the hover panel display template. The following diagram shows how they are referenced.
  
![How result types and all display templates are connected](../media/Result_type_display_template2B.gif)
  
1. Each item display template refers to the Common Item Body item display template. The reference is  `_#=ctx.RenderBody(ctx)=#_`.
    
2. Each hover panel display template contains three references to the three common hover panel display templates. The references are  `_#=ctx.RenderHeader(ctx)=#_,` `_#=ctx.RenderBody(ctx)=#_` and  `_#=ctx.RenderFooter(ctx)=#_`.
    
The following table shows the common display templates.
  
|**Display template title as shown in the user interface**|**Display template name as shown in the Master Page Gallery**|**Description**|
|:-----|:-----|:-----|
|Common Item Body  <br/> |Item_CommonItem_Body  <br/> |Displays information in the body of the Search Results Web Part.  <br/> |
|Common Hover Panel Header  <br/> |Item_CommonHoverPanel  <br/> |Displays information in the header of the hover panel.  <br/> |
|Common Hover Panel  <br/> |Item_CommonPanel_Body  <br/> |Displays information in the body of the hover panel.  <br/> |
|Common Hover Panel Actions  <br/> |Item_CommonHoverPanel_Actions  <br/> |Displays actions in the footer of the hover panel, such as Edit or Send.  <br/> |
   
## Display template that is used for promoted results
<a name="BKMK_BestBets"> </a>

You can use query rules to promote individual results so that they appear towards the top of the search results list. The promoted results are displayed by using a specific item display template that is not connected to a result type. Therefore, it is used to display all search results that are promoted. This display template does not refer to a hover panel display template.
  
The following table shows the display template that is used for promoted results.
  
|**Item display template title**|**Item display template file name as shown in the Master Page Gallery**|**Description**|
|:-----|:-----|:-----|
|Best Bet Item  <br/> |Item_BestBet  <br/> |Displays search results that are promoted by using query rules.  <br/> |
   
## See also
<a name="BKMK_BestBets"> </a>

#### Concepts

[Customize search result types in SharePoint Server](../search/customize-search-result-types.md)
  
[Manage the Search Center in SharePoint Server](../search/manage-the-search-center-in-sharepoint-server.md)
  
[Manage query rules in SharePoint Server](../search/manage-query-rules.md)
  
[Display template reference in SharePoint Server](display-template-reference-in-sharepoint-server.md)

