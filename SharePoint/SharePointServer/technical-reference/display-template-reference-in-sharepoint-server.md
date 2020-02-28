---
title: "Display template reference in SharePoint Server"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 48e3f884-88ab-4538-89fe-b476f1e53b11

description: "Learn about the different display templates that are available in SharePoint Server."
---

# Display template reference in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-SPO-md](../includes/appliesto-2013-2016-2019-SPO-md.md)]
  
## Display templates for the Content Search Web Part

You can use the following display templates to change the appearance of content that is shown in a Content Search Web Part. These display template files are located in the Content Web Parts subfolder in the Display Templates folder in the Master Page Gallery. 
  
|**Display template type**|**Name in Web Part Tool Pane**|**Name in Master Page Gallery**|**Description**|
|:-----|:-----|:-----|:-----|
|Control display template  <br/> |List  <br/> |Control_List  <br/> |Displays the items in the Web Part as a list. It is the default control display template when you add a new Content Search Web Part to a page.  <br/> |
|Control display template  <br/> |List with Paging  <br/> |Control_ListWithPaging  <br/> |Displays the items in the Web Part as a list, and lets users page through the items by using arrows. It is the default control display template for Content Search Web Parts on Category pages.  <br/> |
|Control display template  <br/> |Slideshow  <br/> |Control_Slideshow  <br/> |Displays the items in the Web Part as a picture slide show that rotates through a set of images every 5 seconds. It shows one item at a time, with the title of the item overlaying the picture.  <br/> |
|Item display template  <br/> |Diagnostic  <br/> |Item_Diagnostic  <br/> |Displays the underlying values for items returned by the query specified in the Web Part. This item display template can be very helpful when troubleshooting why items do not appear correctly in the Web Part.  <br/> |
|Item display template  <br/> |Large picture  <br/> |Item_LargePicture  <br/> |Displays an image of the item returned by the query specified in the Web Part, with the title of the item overlaying the image. This item display template should be used with the **Slideshow** control display template, and with images that are more than 400 pixels wide.  <br/> |
|Item display template  <br/> |Picture on left, 3 lines on right  <br/> |Item_Picture3Lines  <br/> |Displays a 100 pixel x 100 pixel image of the item returned by the query specified in the Web Part. The title and the default item description are displayed to the right of the image. An additional line is available as a placeholder that can be used to display a managed property.  <br/> |
|Item display template  <br/> |Picture on top, 3 lines on bottom  <br/> |Item_PictureOnTop  <br/> |Displays a 304 pixel x 100 pixel image of the item returned by the query specified in the Web Part. The title and the default item description are displayed below the image. An additional line is available as a placeholder that can be used to display a managed property.  <br/> |
|Item display template  <br/> |Recommended Items: Picture on left, 3 lines on right  <br/> |Item_RecommendationsClickLogging  <br/> |Displays a 100 pixel x 100 pixel image of the item returned by the query specified in the Web Part. The title and the default item description are displayed to the right of the image. An additional line is available as a placeholder that can be used to display a managed property.  <br/> |
|Item display template  <br/> |Two lines  <br/> |Item_TwoLines  <br/> |Displays a small thumbnail icon next to a hyperlink of the title of the item returned by the query specified in the Web Part. An additional line is available as a placeholder that can be used to display a managed property.  <br/> |
|||Group_Content  <br/> |This file is used to render the different display templates. You should not change this file.  <br/> |
   
## Display templates for the Refinement Web Part and the Taxonomy Refinement Web Part

You can use the display templates listed in the following table to change the appearance of content that is shown in a Refinement Web Part and a Taxonomy Refinement Web Part. These display template files are located in the Filters subfolder in the Display Templates folder in the Master Page Gallery. Note that there are different display templates for different refiner types.
  
|**Display template type**|**Name in Web Part Tool Pane**|**Name in Master Page Gallery**|**Description**|
|:-----|:-----|:-----|:-----|
|Control display template  <br/> |Vertical  <br/> |Control_Refinement  <br/> |The control display template for the Refinement Web Part.  <br/> |
|Control display template  <br/> |Default Taxonomy Refinement  <br/> |Control_TaxonomyRefinement  <br/> |The control display template for the Taxonomy Refinement Web Part.  <br/> |
|Item display template  <br/> |Refinement Item  <br/> |Filter_Default  <br/> |Item display template for refiners of type Text, Decimal, and Date. Displays the refiners in a list. Users can click a specific refiner to narrow the search results.  <br/> |
|Item display template  <br/> |Multi-value Refinement Item  <br/> |Filter_MultiValue  <br/> |Item display template for refiners of type Text, Decimal, and Date. Displays the refiners in a list that has a check box next to each refiner. Users can select multiple refiners to narrow the search results. If you want to change how multi-value refiners are shown on a page, you should not change this display template, but instead use the Multi-value Refinement Item Body template.  <br/> |
|Item display template  <br/> |Multi-value Refinement Item Body  <br/> |Filter_MultiValue_Body  <br/> |Item display template that works together with Multi-value Refinement Item file. If you want to change how multi-value refiners are shown on a page, you should change this display template.  <br/> |
|Item display template  <br/> |Slider  <br/> |Filter_Slider  <br/> |Item display template for refiners of type Decimal. Displays the refiners according to ranges in a slider bar. Users can slide the bar to narrow search results.  <br/> |
|Item display template  <br/> |Slider with bar graph  <br/> |Filter_SliderBarGraph  <br/> |Item display template for refiners of type Decimal. Displays the refiners according to ranges in a slider bar and bar graph. Users can slide the bar or click a bar graph to narrow search results.  <br/> |
|Item display template  <br/> |Link with count  <br/> |Filter_TaxonomyRefinement  <br/> |The default item display template for the Taxonomy Refinement Web Part. Displays the refiners in a list. For each refiner, the number of items that contains the refiner value is displayed. Users can click a specific taxonomy refiner to narrow the search results.  <br/> |
||User Specified Refinement Exchange  <br/> |Filter_eDiscoveryExchangeRefinement  <br/> |This is a system file, and you'll be unable to apply this to a Web Part. You should not change this file.  <br/> |
||Message Type Refinement  <br/> |Filter_eDiscoveryExchangeTypeRefinement  <br/> |This is a system file, and you'll be unable to apply this to a Web Part. You should not change this file.  <br/> |
||User Specified Refinement SharePoint  <br/> |Filter_eDiscoverySharepointRefinement  <br/> |This is a system file, and you'll be unable to apply this to a Web Part. You should not change this file.  <br/> |
   
## Display templates for the Search Results Web Part

You can use the display templates in the following table to change the appearance of content shown in a Search Results Web Part. Note that the hover panels for the different result types have separate display templates. These display template files are located in the Search subfolder in the Display Templates folder in the Master Page Gallery. 
  
|**Display template type**|**Name in Web Part Tool Pane**|**Name in Master Page Gallery**|**Description**|
|:-----|:-----|:-----|:-----|
|Control display template  <br/> |Default Search Box  <br/> |Control_SearchBox  <br/> |Displays the search box in a Search Box Web Part. It is the default control display template for the Search Box Web Part.  <br/> |
|Control display template  <br/> |Site Search Box  <br/> |Control_SearchBoxCompact  <br/> |Displays the search box in a Search Box Web Part in a compact form.  <br/> |
|Control display template  <br/> |Default Result  <br/> |Control_SearchResults  <br/> |The default control display template for the Search Results Web Part.  <br/> |
|Control display template  <br/> |Default Group  <br/> |Group_Default  <br/> |Displays the default group template. Items can be arranged horizontally or vertically depending on how the item template styled. Note that this control display is hidden, so that you will not be able to select this in the Web Part tool pane.  <br/> |
|Item display template  <br/> |Best Bet Item  <br/> |Item_BestBet  <br/> |Displays a single promoted result that is specified by using query rules.  <br/> |
|Hover panel  <br/> |Common Hover Panel Actions  <br/> |Item_CommonHoverPanel_Actions  <br/> |Displays the hover panel actions that are common to all search results.  <br/> |
|Hover panel  <br/> |Common Hover Panel Body  <br/> |Item_CommonHoverPanel_Body  <br/> |Displays the hover panel footer elements that are common to all search results.  <br/> |
|Hover panel  <br/> |Common Hover Panel Header  <br/> |Item_CommonHoverPanel  <br/> |Displays the hover panel header elements that are common to all search results.  <br/> |
|Item display template  <br/> |Common Item Body  <br/> |Item_CommonItem_Body  <br/> |Displays the inline search result body elements that are common to all search results.  <br/> |
|Item display template  <br/> |Community Item  <br/> |Item_Community  <br/> |Displays a search result that is customized for community posts and replies.  <br/> |
|Hover panel  <br/> |Community Hover Panel  <br/> |Item_Community_HoverPanel  <br/> |Displays a search result hover panel that is customized for community posts and replies.  <br/> |
|Item display template  <br/> |Default Item  <br/> |Item_Default  <br/> |Displays the default search result item template.  <br/> |
|Hover panel  <br/> |Default Hover Panel  <br/> |Item_Default_HoverPanel  <br/> |Displays the default search hover panel template.  <br/> |
|Item display template  <br/> |Discussion Item  <br/> |Item_Discussion  <br/> |Displays a search result that is customized for community discussions.  <br/> |
|Hover panel  <br/> |Discussion Hover Panel  <br/> |Item_Discussion_HoverPanel  <br/> |Displays a search result hover panel that is customized for community discussions.  <br/> |
|Item display template  <br/> |Excel Item  <br/> |Item_Excel  <br/> |Displays a search result that is customized for Microsoft Excel documents.  <br/> |
|Hover panel  <br/> |Excel Hover Panel  <br/> |Item_Excel_HoverPanel  <br/> |Displays a search result hover panel that is customized for Microsoft Excel documents.  <br/> |
|Item display template  <br/> |Microblog Item  <br/> |Item_MicroBlog  <br/> |Displays a search result that is customized for microblog feed posts and replies.  <br/> |
|Hover panel  <br/> |Microblog Hover Panel  <br/> |Item_MicroBlog_HoverPanel  <br/> |Displays a search result hover panel that is customized for microblog feed posts and replies.  <br/> |
|Item display template  <br/> |Office Document Item  <br/> |Item_OfficeDocument  <br/> |Displays a search result that is customized for Microsoft Office documents.  <br/> |
|Hover panel  <br/> |Office Document Hover Panel  <br/> |Item_OfficeDocument_HoverPanel  <br/> |Displays a search result hover panel that is customized for a Microsoft Office document.  <br/> |
|Item display template  <br/> |OneNote Item  <br/> |Item_OneNote  <br/> |Displays a search result that is customized for Microsoft OneNote documents.  <br/> |
|Hover panel  <br/> |OneNote Hover Panel  <br/> |Item_OneNote_HoverPanel  <br/> |Displays a search result hover panel that is customized for Microsoft OneNote document.  <br/> |
|Item display template  <br/> |PDF Item  <br/> |Item_PDF  <br/> |Displays search results that are customized for Portable Document Format (PDF) documents.  <br/> |
|Hover panel  <br/> |PDF Hover Panel  <br/> |Item_PDF_HoverPanel  <br/> |Displays a search result hover panel that is customized for a PDF document.  <br/> |
|Item display template  <br/> |People Item  <br/> |Item_Person  <br/> |Displays a search result that is customized for a person.  <br/> |
|Item display template  <br/> |People Intent Item  <br/> |Item_Person_CompactHorizontal  <br/> |Displays a search result that is customized for showing a person in a compact and horizontal layout.  <br/> |
|Hover panel  <br/> |People Hover Panel  <br/> |Item_Person_HoverPanel  <br/> |Displays a search result hover panel that is customized for a person.  <br/> |
|Item display template  <br/> |Personal Result Item  <br/> |Item_PersonalFavorite  <br/> |Displays a personal favorite search result.  <br/> |
|Item display template  <br/> |Picture Item  <br/> |Item_Picture  <br/> |Displays a search result that is customized for a picture.  <br/> |
|Hover panel  <br/> |Picture Hover Panel  <br/> |Item_Picture_HoverPanel  <br/> |Displays a search result hover panel that is customized for a picture.  <br/> |
|Item display template  <br/> |PowerPoint Item  <br/> |Item_PowerPoint  <br/> |Displays a search result that is customized for a Microsoft PowerPoint document.  <br/> |
|Hover panel  <br/> |PowerPoint Hover Panel  <br/> |Item_PowerPoint_HoverPanel  <br/> |Displays a search result hover panel that is customized for a Microsoft PowerPoint document.  <br/> |
|Item display template  <br/> |Reply Item  <br/> |Item_Reply  <br/> |Displays a search result that is customized for a reply in community discussions.  <br/> |
|Hover panel  <br/> |Reply Hover Panel  <br/> |Item_Reply_HoverPanel  <br/> |Displays a search result hover panel that is customized for a reply in community discussions.  <br/> |
|Item display template  <br/> |Site Item  <br/> |Item_Site  <br/> |Displays a search result that is customized for a SharePoint site.  <br/> |
|Hover panel  <br/> |Site Hover Panel  <br/> |Item_Site_HoverPanel  <br/> |Displays a search result hover panel that is customized for a SharePoint site.  <br/> |
|Item display template  <br/> |Video Item  <br/> |Item_Video  <br/> |Displays a search result that is customized for a video file.  <br/> |
|Item display template  <br/> |Video  <br/> |Item_VideoCompactHorizontal  <br/> |Displays a search result that is customized for a video file horizontal layout.  <br/> > [!NOTE]> The Video Hover Panel will not work with this display template           |
|Hover panel  <br/> |Video Hover Panel  <br/> |Item_Video_HoverPanel  <br/> |Displays a search result hover panel that is customized for video file.  <br/> |
|Item display template  <br/> |Web Page Item  <br/> |Item_WebPage  <br/> |Displays a search result that is customized for a web page.  <br/> |
|Hover panel  <br/> |Web page Hover Panel  <br/> |Item_WebPage_HoverPanel  <br/> |Displays a search result hover panel that is customized for a web page.  <br/> |
|Item display template  <br/> |Word Item  <br/> |Item_Word  <br/> |Displays a search result that is customized for a Microsoft Word document.  <br/> |
|Hover panel  <br/> |Word Hover Panel  <br/> |Item_Word_HoverPanel  <br/> |Displays a search result hover panel that is customized for a Microsoft Word document.  <br/> |
   

