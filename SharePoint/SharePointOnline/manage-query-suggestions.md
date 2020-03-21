---
title: "Customize query suggestions in SharePoint search"
ms.reviewer: 
ms.author: arnek
author: arnek
manager: pamgreen
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
search.appverid:
- SPO160
- MET150
ms.assetid: 9ef0f859-3b92-41e9-b393-cb43d6094c7b
description: "Learn how to add phrases that you want the system to suggest to users as they search for an item, and how to add phrases that you don't want the system to suggest to users. Also, learn how to turn this feature on or off."
---

# Customize query suggestions in SharePoint search

Query spelling suggestions are words that appear below the search box as a user types a query. SharePoint automatically creates a query suggestion when you've clicked a search result for a query at least six times. For example, if you've entered the query word "coffee" and then clicked a search result six times, "coffee" automatically becomes a query suggestion. 
  
Automatic query suggestions are generated daily for each result source and each site collection, so the query suggestions can be different for different result sources and site collections.
  
SharePoint has both a classic and a modern search experience, [learn about the differences between the classic and modern search experiences in SharePoint](differences-classic-modern-search.md). The modern search experience uses the same default result source as the classic search experience. Automatic query suggestions for the default result source appear in both the classic and modern search experiences.

 You can manually create your own lists of query suggestions and import them to SharePoint. Manual query suggestions apply to **all** result sources, **all** site collections, and to **both** search experiences.
  
To create query suggestions for multiple languages, you'll need to create a separate file for each language. The language determines how the query suggestions are processed internally in the search system. All manual query suggestions are always displayed for **all** languages. Add each phrase as a separate line in the text file that you create and save the file in UTF-8 encoding. 
  
Query suggestions are turned on by default. To turn them off, go to **Search Suggestions** and uncheck **Show search suggestions**.
  
## To create query suggestions in SharePoint search
<a name="__toc343004643"> </a>

1. Go to the [More features page of the new SharePoint admin center](https://admin.microsoft.com/sharepoint?page=classicfeatures&modern=true) and sign in with an account that has [admin permissions](/sharepoint/sharepoint-admin-role)
 for your organization.

>[!NOTE]
>If you have Office 365 Germany, [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=848041), then browse to the SharePoint admin center and open the More features page. <br>If you have Office 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the More features page.
 
2. Under **Search**, select **Open**.

3. Select **Query Suggestion Settings** on the search administration page.

   
4. Open a text editor of your choice, and enter a list of terms that you want the system to always suggest to users. Only add one term per line to the text file, and don't mix languages in the text file.
    
5. Save the text file to a location that's accessible from SharePoint.
    
6. To import a list of query suggestions to SharePoint search, go to **Always suggest phrases** \> **Import from text file**. When you import query suggestions, any existing ones will be overwritten.
    
7. Browse to the file that you want to import.
    
8. Go to **Language for suggestion phrases**, and select the processing language of your query suggestions. It should match the language of the terms in the text file. 
    
9. Choose **Save Settings**.
    
### Related tasks

You can edit a list of query suggestions that you've manually created. To edit a list that you've already imported in to SharePoint, choose **Export to text file**, update the text file with your changes, and then re-import it. After you've uploaded your query suggestions file, it might take a few hours until your query suggestions are displayed. You can check that they're working properly by entering a phrase from your list of query suggestions in the search box. The query suggestion should appear below the search box.
  
To get rid of a list of query terms, you must overwrite it. Do this by importing an empty text file. 
  
You can also prevent terms from appearing in the search box. To do this, create a text file with the query terms that you never want users to see below the search box, and then import it to **Never suggest phrases**.
