---
title: "Customize query suggestions in SharePoint search"
ms.reviewer: 
ms.author: serdars
author: SerdarSoysal
manager: serdars
recommendations: true
audience: Admin
f1.keywords: NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.localizationpriority: medium
ms.custom: admindeeplinkSPO
search.appverid:
- SPO160
- MET150
ms.assetid: 9ef0f859-3b92-41e9-b393-cb43d6094c7b
description: "Learn how to add phrases that you want the system to suggest to users as they search for an item, and how to add phrases that you don't want the system to suggest to users. Also, learn how to turn this feature on or off."
---

# Customize query suggestions in SharePoint search

Query spelling suggestions are words that appear below the search box as a user types a query. SharePoint automatically creates query suggestions from frequently entered queries that resulted in a click on a search result. For example, if you've repeatedly entered the query word "coffee" and then clicked a search result each time, "coffee" automatically becomes a query suggestion. 
  
Automatic query suggestions are generated periodically for each result source and each site collection, so the query suggestions can be different for different result sources and site collections.

For example, in the following screenshot, "contoso" is automatically suggested.
![Screenshot of Query Suggestion.](media/query-suggestion.png)
  
SharePoint has both a classic and a modern search experience, [learn about the differences between the classic and modern search experiences in SharePoint](differences-classic-modern-search.md). The modern search experience uses the same default result source as the classic search experience. Automatic query suggestions for the default result source appear in both the classic and modern search experiences.

As an admin you can manually create your own lists of queries that always shall be suggested or phrases that never shall be suggested, and import them to SharePoint. 
- Your list of queries that shall always be suggested only applies to modern search and only in tenant-wide scope.
- Your list of phrases that never shall appear apply to both classic and modern search, to all result sources and all site collections.
  
To create query suggestions for multiple languages, you'll need to create a separate file for each language. The language determines how the query suggestions are processed internally in the search system. All manual query suggestions are always displayed for **all** languages. Add each phrase as a separate line in the text file that you create and save the file in UTF-8 encoding. 
  
Query suggestions are turned on by default. To turn them off, go to **Search Suggestions**, and clear **Show search suggestions**.
  
## To create query suggestions in SharePoint search
<a name="__toc343004643"> </a>

1. Go to <a href="https://go.microsoft.com/fwlink/?linkid=2185077" target="_blank">**More features** in the SharePoint admin center</a>, and sign in with an account that has [admin permissions](./sharepoint-admin-role.md) for your organization.

   > [!NOTE]
   > If you have Office 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the More features page.
 
2. Under **Search**, select **Open**.

3. On the search administration page, select **Query Suggestion Settings**.
 
4. Open a text editor of your choice, and enter a list of terms that you want the system to always suggest to users. Only add one term per line to the text file, and don't mix languages in the text file.
    
5. Save the text file to a location that's accessible from SharePoint.
    
6. To import a list of query suggestions to SharePoint search, go to **Always suggest phrases** > **Import from text file**. When you import query suggestions, any existing ones will be overwritten.
    
7. Browse to the file that you want to import.
    
8. Go to **Language for suggestion phrases**, and select the processing language of your query suggestions. It should match the language of the terms in the text file. 
    
9. Select **Save Settings**.
    
### Related tasks

You can edit a list of query suggestions that you've manually created. To edit a list that you've already imported into SharePoint, choose **Export to text file**, update the text file with your changes, and then re-import it. After you've uploaded your query suggestions file, it might take up to a week until your query suggestions are displayed. You can check that they're working properly by entering a phrase from your list of query suggestions in the search box. The query suggestion should appear below the search box.
  
To get rid of a list of query terms, you must overwrite it. Do this by importing an empty text file. 
  
To prevent terms from appearing in the search box, create a text file with the query terms that you never want users to see below the search box, and then import it to **Never suggest phrases**.
