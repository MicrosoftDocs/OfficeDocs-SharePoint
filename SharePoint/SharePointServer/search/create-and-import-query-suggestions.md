---
title: "Create and import query suggestions for the classic search experience in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 9/5/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: 59be233e-be37-4639-b7b4-9059f5bb59ba
description: "Learn how to import query suggestions in SharePoint Server."
---

# Create and import query suggestions for the classic search experience in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
An easy way to help users search for information in SharePoint Server is to create  *query suggestions*  . Query suggestions are words that appear under the search box as users type a query. 
  
![Query Suggestion](../media/OTCSP_coffee_suggestion.png)
  
SharePoint Server automatically creates a query suggestion when users have clicked a search result for a query at least six times. For example, if users have entered the query word "coffee" and then clicked on a search result six times, then "coffee" automatically becomes a query suggestion. We can also create query spelling suggestions manually. In this article, we'll use a simple example to show how to do this.
  
In this article, you'll learn:
  
- [How to create a query suggestions file](create-and-import-query-suggestions.md#BKMK_HowToCreateAQuerySuggestionsFile)
    
- [How to import a query suggestions file to SharePoint Server](create-and-import-query-suggestions.md#BKMK_HowToImportQuerySuggestionsFileToSharepointOnline)
    
- [How to import a query suggestions file to SharePoint Server](create-and-import-query-suggestions.md#BKMK_HowToImportQuerySuggestionsFileToSharepointServer2013)
    
- [How to verify that your query suggestions are working](create-and-import-query-suggestions.md#BKMK_HowToVerifyThatYourQuerySuggestionsAreWorking)
    
## How to create a query suggestions file
<a name="BKMK_HowToCreateAQuerySuggestionsFile"> </a>

1. Open a text editor, for example Notepad.
    
2. Enter the query spelling suggestions that you want to add. Add one word or phrase per line.
    
     ![Query Suggestion List](../media/OTCSP_QuerySuggestionList.png)
  
3. Save the file as a **.txt** file and encoding **UTF-8**. 
    
     ![Save as TXT File](../media/OTCSP_SaveTXT.png)
  
Now that you have a query suggestions file, the next task is to import it to SharePoint Server.
  
## How to import a query suggestions file to SharePoint Online
<a name="BKMK_HowToImportQuerySuggestionsFileToSharepointOnline"> </a>

1. From the Office 365 Admin menu, select **SharePoint**. 
    
     ![Share Point Menu](../media/OTCSP_SharePointMenu.png)
  
2. On the **SharePoint admin center**, select **search**. 
    
     ![Click Search](../media/OTCSP_search.png)
  
3. On the **search administration** page, select **Query Suggestion Settings**. 
    
     ![Select Query Suggestion Settings](../media/OTCSP_QuerySuggestionSettings.png)
  
4. In the **Language for suggestions phrases** section, select the language of your query suggestions. In the **Always suggest phrases** section, select **Import from text file**. 
    
     ![Import from Text File](../media/OTCSP_AlwaysSuggest.png)
  
5. In the **Text file that has phrases** section, select **Choose File**, and import your query suggestions file. 
    
     ![Import Query Suggestions File](../media/OTCSP_ChooseFile.png)
  
6. Select **OK**, and then **Save Settings**. 
    
     ![Click Save Settings](../media/OTCSP_SaveSettings.png)
  
> [!IMPORTANT]
> When you import query suggestions, existing query suggestions are overwritten. If you haven't previously imported any query suggestions, you have nothing to worry about. Automatically created query suggestions will not be overwritten when you import new ones. But, if you want to import additional query suggestions, you should export the existing query suggestions file, update it, and then reimport it. 
  
## How to import a query suggestions file to SharePoint Server
<a name="BKMK_HowToImportQuerySuggestionsFileToSharepointServer2013"> </a>

1. Go to **Central Administration** --> **Manage service applications** --> **Search Service Application** --> **Query Suggestions**. 
    
2. On the **Query Suggestion Settings** page, in the **Always suggest phases** section, select **Import from text file**. 
    
     ![Import from Text File](../media/OTCSP_CA_ImportFromTextFile.png)
  
3. On the **Import phrases for query suggestions** page, select **Browse**, and import your query suggestions file. 
    
     ![Select Browse](../media/OTCSP_Browse.png)
  
4. Select **OK**, and then **Save Settings**. 
    
     ![Save Settings](../media/OTCSP_CA_SaveSettings.png)
  
> [!IMPORTANT]
> When you import query suggestions, existing query suggestions are overwritten. If you haven't previously imported any query suggestions, you have nothing to worry about. Automatically created query suggestions won't be overwritten when you import new ones. But, if you want to import additional query suggestions, you should export the existing query suggestions file, update it, and then reimport it. 
  
## How to verify that your query suggestions are working
<a name="BKMK_HowToVerifyThatYourQuerySuggestionsAreWorking"> </a>

> [!IMPORTANT]
> After you have uploaded your query suggestions file, it might take some hours before your query suggestions are displayed. 
  
To verify that your query suggestions are working correctly, in a search box, type two letters of a phrase from your query suggestions file. The query suggestions appear under the search box.
  
![Query Suggestion](../media/OTCSP_CupOfJoe.png)
  
![Query Suggestion](../media/OTCSP_CaffeLatte.png)
  
## See also
<a name="BKMK_HowToVerifyThatYourQuerySuggestionsAreWorking"> </a>

#### Concepts

[Manage query suggestions in SharePoint Server](manage-query-suggestions.md)
#### Other Resources

[Customize query suggestions in SharePoint search](https://docs.microsoft.com/en-us/sharepoint/manage-query-suggestions)

