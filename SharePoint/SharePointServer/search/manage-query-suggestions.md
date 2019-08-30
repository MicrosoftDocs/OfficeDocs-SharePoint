---
title: "Manage query suggestions in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 3/7/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 502fcb0a-c20a-433d-aac1-02ba20d81a7e
description: "Query suggestions are phrases that you want the search system to suggest to users as they start typing a query. This article explains how to switch query suggestions on or off. It also explains how you can add phrases to the automatic query suggestions, and how you can add phrases that should not be used as query suggestions."
---

# Manage query suggestions in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
Query suggestions help users find information quickly by showing queries that might be similar to the one they're typing. For example, as users start to type "sales", they may be able to pick common sales-related queries from a list below the Search Box. 
  
The search system automatically creates suggestions for a query when users have clicked one or more of the results for that query at least six times. The query suggestions are generated daily for each result source and for each site collection, so the automatic query suggestions can be different for different result sources and site collections.
  
When you follow the steps in this article to manually add phrases that should or shouldn't be used as query suggestions, the query suggestions apply to **all** result sources and **all** site collections. 
  
    
## Add phrases that should always or never be used as query suggestions
<a name="proc3"> </a>

To add phrases that you want the search system to always or never suggest to users as they start typing a query, you have to create one or several text files that contain these phrases, and then import the files into the search system. 
  
You should create separate text files for the phrases that you want to always be suggested, and for the phrases that you want to never be suggested. If you want to add query suggestions for multiple languages, you should also create separate files per language. The language determines how the query suggestions are processed internally in the search system, but all query suggestions are always displayed or suppressed for **all** languages as users enter their queries. Add each phrase as a separate line in the text file that you create, and save the file in UTF-8 encoding. 
  
> [!CAUTION]
> When you import a text file with phrases for query suggestions, you overwrite any existing manual query suggestions in the search system. The automatic query suggestions are not overwritten. If you want to edit existing manual query suggestions or add new ones, you should first export the existing query suggestions to a text file, and then update and re-import that file. 
  
 **To add phrases that should always be used as query suggestions**
  
1. Verify that the user account that is performing this procedure is an administrator for the Search service application.
    
2. Open the **Query Suggestion Settings** page. 
    
  - On the home page of the SharePoint Central Administration website, in the **Application Management** section, click **Manage service applications**.
    
  - On the **Manage Service Applications** page, click the Search service application. 
    
  - On the Search Administration Page, in the **Queries and Results** section, click **Query Suggestions**. The Query Suggestion Settings page opens.
    
3. In the **Language for suggestion phrases** section, select the processing language for the query suggestions that you always want to suggest. 
    
4. In the **Always suggest phrases** section, click **Import from text file**. Browse to the file that you want to import and click **OK**.
    
5. Click **Save Settings**. 
    
> [!NOTE]
> If you want to edit existing manual query suggestions or add new ones, click **Export to file**, update the text file and then re-import it. To remove all manual query suggestions, upload an empty text file. 
  
 **To add phrases that should never be used as query suggestions**
  
1. Verify that the user account that is performing this procedure is an administrator for the Search service application.
    
2. Open the **Query Suggestion Settings** page. 
    
  - On the home page of the SharePoint Central Administration website, in the **Application Management** section, click **Manage service applications**.
    
  - On the **Manage Service Applications** page, click the Search service application. 
    
  - On the Search Administration Page, in the **Queries and Results** section, click **Query Suggestions**. The Query Suggestion Settings page opens.
    
3. In the **Language for suggestion phrases** section, select the processing language for the query suggestions that you never want to suggest. 
    
4. In the **Never suggest phrases** section, click **Import from text file**. Browse to the file that you want to import and click **OK**.
    
5. Click **Save Settings**. 
    
> [!NOTE]
> If you want to edit existing manual query suggestions or add new ones, click **Export to text file**, update the text file and then re-import it. To remove all manual query suggestions, upload an empty text file. 
  
## Switch query suggestions on or off
<a name="proc2"> </a>

Query suggestions are turned on by default. The following steps explain how to turn query suggestions on or off. 
  
 **To enable or disable query suggestions**
  
1. Verify that the user account that is performing this procedure is an administrator for the Search service application.
    
2. Open the **Query Suggestion Settings** page. 
    
  - On the home page of the SharePoint Central Administration website, in the **Application Management** section, click **Manage service applications**.
    
  - On the **Manage Service Applications** page, click the Search service application. 
    
  - On the Search Administration Page, in the **Queries and Results** section, click **Query Suggestions**. The Query Suggestion Settings page opens.
    
3. In the **Search Suggestions** section, do one of the following: 
    
  - To enable query suggestions, check the **Show search suggestions** check box. 
    
  - To disable query suggestions, clear the **Show search suggestions** check box. 
    
4. Click **Save Settings**.
    

