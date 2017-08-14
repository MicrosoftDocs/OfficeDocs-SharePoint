---
title: Delete items from the search index or from search results in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: 48d39f84-9698-4249-b7e0-b885c462622e
---


# Delete items from the search index or from search results in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-24* **Summary:** Learn how to remove an item from the search index or SharePoint Server search results by removing the URL.If you want to remove the metadata of an item from the search index or from the search results, you remove the URL of that item. To remove a URL from the search index, use the **Remove the Item from the Index** option that is available through the crawl log. To remove a URL from search results, use the **Search Result Removal** feature that allows for bulk URL removal. This can provide a more efficient method if many search results should be removed.
> [!NOTE:]

  
    
    

In this article:
-  [Before you begin](#begin)
    
  
-  [Remove an item from the search index](#proc1)
    
  
-  [Remove an item from the search results](#proc2)
    
  

## Before you begin
<a name="begin"> </a>


> [!NOTE:]
>  [Plan browser support](https://go.microsoft.com/fwlink/p/?LinkId=246502)> **Accessibility for SharePoint 2013**>  [Accessibility features in SharePoint 2013 Products](https://go.microsoft.com/fwlink/p/?LinkId=246501)>  [Keyboard shortcuts](https://go.microsoft.com/fwlink/p/?LinkID=246504)>  [Touch](https://go.microsoft.com/fwlink/p/?LinkId=246506)
  
    
    

Before you begin this operation, review the following information about prerequisites:
- Create a Search service application
    
  
- Add one or more content sources
    
  
- Perform at least one full crawl
    
  

## Remove an item from the search index
<a name="proc1"> </a>

 **To remove an item from the search index**
1. Verify that the user account that is performing this procedure is an administrator for the Search service application.
    
  
2. On the SharePoint Server Central Administration home page, in the **Application Management** section, click **Manage service applications**.
    
  
3. On the Manage Search Applications page, click the Search service application. 
    
  
4. On the Search Administration page, in the **Diagnostics** section, click **Crawl Log**.
    
  
5. On the Crawl Log page, click **URL View**.
    
  
6. Do one of the following: 
    
1. If you know the URL of the item that you want to remove, type the URL in the box.
    
  
2. If you do not know the URL of the item that you want to remove, search for it by using the filters **Content Source**, **Status** or **Message**.
    
  
7. Click **Search**.
    
  
8. Find and point to the URL of the item that you want to remove, click the arrow and then click **Remove the item from the Index**.
    
  
9. In the confirmation dialog that appears, click **OK** to confirm that you want to remove the item from the index.
    
  
10. **Verification:** the text **Removed from the search index by Admin** appears under the URL in the crawl log.
    
  

## Remove an item from the search results
<a name="proc2"> </a>

 **To remove an item from the search results**
1. Verify that the user account that is performing this procedure is an administrator for the Search service application.
    
  
2. On the SharePoint Server Central Administration home page, in the **Application Management** section, click **Manage service applications**.
    
  
3. On the Manage Search Applications page, click the Search service application. 
    
  
4. On the Search Administration page, in the **Queries and Results** section, click **Search Result Removal**.
    
  
5. On the Exclude URLs From Search Results page, in the **URLs to remove** box, type the URLs of the items that you want to remove from the search results.
    
  
6. Click **Remove Now**.
    
  

