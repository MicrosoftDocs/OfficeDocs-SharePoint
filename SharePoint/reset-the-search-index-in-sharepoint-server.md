---
title: Reset the search index in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: 7a1835c3-6375-4647-b190-84676fc9f9b0
---


# Reset the search index in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-25* **Summary:** Learn how to reset the SharePoint Server search index.When you reset the search index in SharePoint Server, all content is immediately removed from the search index and users will not be able to retrieve search results. After you reset the search index, you must perform a full crawl of one or more content sources to create a new search index. Users will be able to retrieve search results again when the full crawl is finished and the new search index is created.
> [!NOTE:]

  
    
    


> [!NOTE:]

  
    
    

In this article:
-  [Before you begin](#begin)
    
  
-  [Reset the search index](#proc1)
    
  

## Before you begin
<a name="begin"> </a>


> [!NOTE:]
>  [Plan browser support](https://go.microsoft.com/fwlink/p/?LinkId=246502)> **Accessibility for SharePoint 2013**>  [Accessibility features in SharePoint 2013 Products](https://go.microsoft.com/fwlink/p/?LinkId=246501)>  [Keyboard shortcuts](https://go.microsoft.com/fwlink/p/?LinkID=246504)>  [Touch](https://go.microsoft.com/fwlink/p/?LinkId=246506)
  
    
    

Before you begin this operation, review the following information about prerequisites:
- Create a Search service application.
    
  
- Add one or more content sources.
    
  
- Perform at least one full crawl.
    
  
- Make sure that you are not running a backup of the Search service application when you reset the search index. 
    
  

## Reset the search index
<a name="proc1"> </a>

Use the following procedure to reset the search index. **To reset the search index**
1. Verify that the user account that is performing this procedure is an administrator for the Search service application for which you want to reset the search index.
    
  
2. On the SharePoint Central Administration home page, in the **Application Management** section, click **Manage service applications**.
    
  
3. On the Manage Search Applications page, click the Search service application for which you want to reset the search index. 
    
  
4. On the Search Administration page, under System Status, verify that the **Administrative status** of the Search service application is **Running** and not **Paused**.
    
  
5. On the Search Administration page, in the **Crawling** section, click **Index Reset**.
    
  
6. On the Index Reset page, verify that the **Deactivate search alerts during reset** check box is checked, and then click **Reset Now**.
    
  
7. In the confirmation dialog box that appears, click **OK** to confirm that you want to reset the index.
    
    The Search Administration page opens and the System Status is displayed.
    
  
After the search index reset is complete, you must perform a full crawl of all the content sources that you want to include in the search index. For more information, see Add, edit, or delete a content source in SharePoint 2013 Preview. Users will not be able to retrieve search results until you create a new search index. After the full crawl has completed and a new search index has been created, you must also re-enable search alerts. See Enable search alerts in SharePoint Server 2013.
