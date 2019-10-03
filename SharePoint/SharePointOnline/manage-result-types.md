---
title: "Manage result types"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 6/29/2018
audience: End User
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
search.appverid:
- SPO160
- MET150
ms.assetid: ceccf561-e82c-495c-bf3e-b3f006ae9c8c
description: "Create and use result types to customize how results are displayed for particular types of documents."
---

# Manage result types

As a site collection administrator or site owner, you can create and use result types to customize how results are displayed for particular types of documents. 
  
SharePoint Online has both a classic and a modern search experience. For the classic search experience, you use a result type to specify a [display template](use-result-types-and-display-templates.md) that the search system should use for a particular type of document or search result. As documents aren't all the same, search results shouldn't be either. By using result types and display templates, it's much easier for users to find the results they are looking for. You can't customize how results are displayed for the modern search experience. [Learn about the differences between the classic and modern search experiences in SharePoint Online](differences-classic-modern-search.md).
  
A result type specifies one or more conditions to compare search results against, such as the type or the result source of the search result, and an action to take if a search result meets those conditions. The action specifies the display template to use for the search result. 
  
For example, a preconfigured result type named **Person** specifies that if a search result comes from the result source **Local People Results**, then use the **People Item** display template. The **People Item** display template shows information in the hover panel such as documents the person's authored and gives you quick access to those documents. 
  
Another example is to have a result type that fires if the **ContentType** property **contains** *Sales Report*  , and then have a specific display template for sales reports. Users will identify the search result as a sales report right away. 
  
See [Change how search results look by using result types and display templates](use-result-types-and-display-templates.md) for more information. 
  
There are many preconfigured result types to choose from, and you can also create new custom result types. You can configure result types at site collection level and at site level.
  
## Add a new result type
<a name="__top"> </a>

1. Go to the **Manage Result Types** page for a site collection or a site: 
    
  - For a site collection, in your site collection, select **Settings** ![Settings icon.](media/a47a06c3-83fb-46b2-9c52-d1bad63e3e60.png), and then select **Site settings**. If you don't see **Site settings**, select **Site information**, and then select **View all site settings**. Under **Site Collection Administration**, select **Search Result Types**.
    
  - For a site, select **Settings** ![Settings icon.](media/a47a06c3-83fb-46b2-9c52-d1bad63e3e60.png), and then select **Site settings**. If you don't see **Site settings**, select **Site information**, and then select **View all site settings**. Under **Search**, select **Result Types**.
    
2. On the **Manage Result Types** page, do one of the following: 
    
  - Click **New Result Type**, or 
    
  - In the list of existing result types, click the name of a result type, such as **Person**, and then click **Copy** so that you can modify the copy to create a new result type. 
    
3. In the **General Information** section, in the **Give it a name** box, type a name for the result type. 
    
4. In the **Conditions** section, in the first list, choose a result source that the results should match. 
    
5. In the **Conditions** section, in the second list, choose which types of content should match. To match all content, skip the rule. To add more content types, click **Add value**.
    
6. To add more advanced conditions related to managed properties, expand **Show more conditions**. 
    
1. In the first list, choose a property to match.
    
2. Choose how the property should relate to one or more values.
    
3. Enter one or more values for the property in the box. Separate by using semicolons. 
    
4. To add more properties to match, click **Add property**.
    
7. In the **Actions** section, select a display template. The URL of the display template is shown under **Display template URL**.
    
8. Check the **Optimize for frequent use** box if the result type will be among the most frequently used result types. 
    
9. Click **Save**. 
    

