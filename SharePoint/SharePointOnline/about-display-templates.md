---
title: "About display templates in the Content Search Web Part and other search-driven Web Parts"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 6/26/2014
audience: End User
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
search.appverid:
- SPO160
- SPS150
- MET150
ms.assetid: c7cb0a7e-fb1e-45b1-b259-c0dae30f7528
description: "The Content Search Web Part and the other search-driven Web Parts use display templates to control how the search results appear in the Web Part. By using display templates, you can control the ways in which search results appear and behave in search-driven Web Parts."
---

# About display templates in the Content Search Web Part and other search-driven Web Parts

The Content Search Web Part and the other search-driven Web Parts use display templates to control how the search results appear in the Web Part. By using display templates, you can control the ways in which search results appear and behave in search-driven Web Parts.
  
 Display templates are HTML files that specify which managed properties from the search result to display, and also how these properties should be displayed. For example, a display template could specify that the managed property PublishingImage displays a 100x100 pixel picture, and the managed property Title appears in bold to the left of the image. You can use any of the pre-configured display templates, or create your own. 
  
The different search-driven Web Parts have different default display template settings that are optimized for the intended use of that Web Part. For example, by default, the Content Search Web Part displays a list of items where each item has a picture on the left side and three lines of text on the right. 
  
## To change display template settings

1. In the **Control** list, select a display template to control the organization and layout of your search results and the overall look of the Web Part. 
    
2. In the **Item** list, select a display template for the individual items that are displayed in the search results within the Web Part. 
    
3. Select the **Don't show anything when there are no results** check box if you don't want to display the Web Part at all if there are no search results returned by the query in that Web Part. 
    
    If you clear the check box, the Web Part is displayed even if there are no search results, and the Web Part will show the "No results" message in the selected Control display template.
    
## To change which managed properties are displayed in the fields in the Item Display Template

By default, display templates have a set of property mappings in them that were defined when the display template was created. However, you can override these settings in a particular Content Search Web Part.
  
1. Under **Property Mappings**, select the check box **Change the mapping of managed properties for the fields in the Item Display Template**.
    
2. In the different lists below the check box, enter the managed property to use for that field in the Item Display Template. 
    
    If you enter multiple managed property names in a list, separate the managed properties by using semicolon. When displaying content, SharePoint will use the first property that is not empty.
    
For more information, see:
  
- [About search criteria for the Content Search Web Part and other search-driven Web Parts](https://support.office.com/article/9937e459-2b94-4a04-8c06-90696a7d94a8)
    

