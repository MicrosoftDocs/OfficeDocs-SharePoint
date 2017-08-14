---
title: Manage query suggestions in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: 502fcb0a-c20a-433d-aac1-02ba20d81a7e
---


# Manage query suggestions in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-24* **Summary:** Query suggestions are phrases that you want the search system to suggest to users as they start typing a query. This article explains how to switch query suggestions on or off. It also explains how you can add phrases to the automatic query suggestions, and how you can add phrases that should not be used as query suggestions.Query suggestions help users find information quickly by showing queries that might be similar to the one they're typing. For example, as users start to type "sales", they may be able to pick common sales-related queries from a list below the Search Box. The search system automatically creates suggestions for a query when users have clicked one or more of the results for that query at least six times. The query suggestions are generated daily for each result source and for each site collection, so the automatic query suggestions can be different for different result sources and site collections.When you follow the steps in this article to manually add phrases that should or shouldn't be used as query suggestions, the query suggestions apply to **all** result sources and **all** site collections.In this article:
-  [Before you begin](#BKMK_Before_you_begin)
    
  
-  [Add phrases that should always or never be used as query suggestions ](#proc3)
    
  
-  [Switch query suggestions on or off](#proc2)
    
  

## Before you begin
<a name="BKMK_Before_you_begin"> </a>


> [!NOTE:]
>  [Plan browser support](https://go.microsoft.com/fwlink/p/?LinkId=246502)> **Accessibility for SharePoint 2013**>  [Accessibility features in SharePoint 2013 Products](https://go.microsoft.com/fwlink/p/?LinkId=246501)>  [Keyboard shortcuts](https://go.microsoft.com/fwlink/p/?LinkID=246504)>  [Touch](https://go.microsoft.com/fwlink/p/?LinkId=246506)
  
    
    

Before you begin this operation, review the following information about prerequisites:
- Create a Search service application
    
  

## Add phrases that should always or never be used as query suggestions
<a name="proc3"> </a>

To add phrases that you want the search system to always or never suggest to users as they start typing a query, you have to create one or several text files that contain these phrases, and then import the files into the search system. You should create separate text files for the phrases that you want to always be suggested, and for the phrases that you want to never be suggested. If you want to add query suggestions for multiple languages, you should also create separate files per language. The language determines how the query suggestions are processed internally in the search system, but all query suggestions are always displayed or suppressed for **all** languages as users enter their queries. Add each phrase as a separate line in the text file that you create, and save the file in UTF-8 encoding.
> [!WARNING:]

  
    
    

 **To add phrases that should always be used as query suggestions**
1. Verify that the user account that is performing this procedure is an administrator for the Search service application.
    
  
2. Open the **Query Suggestion Settings** page.
    
1. On the home page of the SharePoint Central Administration website, in the **Application Management** section, click **Manage service applications**.
    
  
2. On the **Manage Service Applications** page, click the Search service application.
    
  
3. On the Search Administration Page, in the **Queries and Results** section, click **Query Suggestions**. The Query Suggestion Settings page opens.
    
  
3. In the **Language for suggestion phrases** section, select the processing language for the query suggestions that you always want to suggest.
    
  
4. In the **Always suggest phrases** section, click **Import from text file**. Browse to the file that you want to import and click **OK**.
    
  
5. Click **Save Settings**.
    
  

> [!NOTE:]

  
    
    

 **To add phrases that should never be used as query suggestions**
1. Verify that the user account that is performing this procedure is an administrator for the Search service application.
    
  
2. Open the **Query Suggestion Settings** page.
    
1. On the home page of the SharePoint Central Administration website, in the **Application Management** section, click **Manage service applications**.
    
  
2. On the **Manage Service Applications** page, click the Search service application.
    
  
3. On the Search Administration Page, in the **Queries and Results** section, click **Query Suggestions**. The Query Suggestion Settings page opens.
    
  
3. In the **Language for suggestion phrases** section, select the processing language for the query suggestions that you never want to suggest.
    
  
4. In the **Never suggest phrases** section, click **Import from text file**. Browse to the file that you want to import and click **OK**.
    
  
5. Click **Save Settings**.
    
  

> [!NOTE:]

  
    
    


## Switch query suggestions on or off
<a name="proc2"> </a>

Query suggestions are turned on by default. The following steps explain how to turn query suggestions on or off. **To enable or disable query suggestions**
1. Verify that the user account that is performing this procedure is an administrator for the Search service application.
    
  
2. Open the **Query Suggestion Settings** page.
    
1. On the home page of the SharePoint Central Administration website, in the **Application Management** section, click **Manage service applications**.
    
  
2. On the **Manage Service Applications** page, click the Search service application.
    
  
3. On the Search Administration Page, in the **Queries and Results** section, click **Query Suggestions**. The Query Suggestion Settings page opens.
    
  
3. In the **Search Suggestions** section, do one of the following:
    
1. To enable query suggestions, check the **Show search suggestions** check box.
    
  
2. To disable query suggestions, clear the **Show search suggestions** check box.
    
  
4. Click **Save Settings**.
    
  

