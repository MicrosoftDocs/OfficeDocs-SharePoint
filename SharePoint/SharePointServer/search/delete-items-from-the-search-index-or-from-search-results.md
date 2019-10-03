---
title: "Delete items from the search index or from search results in SharePoint Server"
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
ms.assetid: 48d39f84-9698-4249-b7e0-b885c462622e
description: "Learn how to remove an item from the search index or SharePoint Server search results by removing the URL."
---

# Delete items from the search index or from search results in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
If you want to remove the metadata of an item from the search index or from the search results, you remove the URL of that item. To remove a URL from the search index, use the **Remove the Item from the Index** option that is available through the crawl log. To remove a URL from search results, use the **Search Result Removal** feature that allows for bulk URL removal. This can provide a more efficient method if many search results should be removed. 
  
> [!NOTE]
> 
> - If your SharePoint environment is hybrid and uses [cloud hybrid search](/SharePoint/hybrid/learn-about-cloud-hybrid-search-for-sharepoint), you index your on-premises content in your search index in Office 365. See [Learn about cloud hybrid search for SharePoint](/SharePoint/hybrid/learn-about-cloud-hybrid-search-for-sharepoint) for guidance on deleting the metadata of an on-premises item and deleting on-premises search results from the search index in Office 365. 
>
> - For SharePoint Server 2019, removing the URL of an item affects both the **classic** and **modern** search experiences.
  
    
## Remove an item from the search index
<a name="proc1"> </a>

 **To remove an item from the search index**
  
1. Verify that the user account that is performing this procedure is an administrator for the Search service application.
    
2. On the SharePoint Server Central Administration home page, in the **Application Management** section, click **Manage service applications**.
    
3. On the Manage Search Applications page, click the Search service application. 
    
4. On the Search Administration page, in the **Diagnostics** section, click **Crawl Log**.
    
5. On the Crawl Log page, click **URL View**.
    
6. Do one of the following: 
    
  - If you know the URL of the item that you want to remove, type the URL in the box.
    
  - If you do not know the URL of the item that you want to remove, search for it by using the filters **Content Source**, **Status** or **Message**.
    
7. Click **Search**.
    
8. Find and point to the URL of the item that you want to remove, click the arrow and then click **Remove the item from the Index**.
    
9. In the confirmation dialog that appears, click **OK** to confirm that you want to remove the item from the index. 
    
10. **Verification:** the text **Removed from the search index by Admin** appears under the URL in the crawl log. 
    
## Remove an item from the search results
<a name="proc2"> </a>

 **To remove an item from the search results**
  
1. Verify that the user account that is performing this procedure is an administrator for the Search service application.
    
2. On the SharePoint Server Central Administration home page, in the **Application Management** section, click **Manage service applications**.
    
3. On the Manage Search Applications page, click the Search service application. 
    
4. On the Search Administration page, in the **Queries and Results** section, click **Search Result Removal**.
    
5. On the Exclude URLs From Search Results page, in the **URLs to remove** box, type the URLs of the items that you want to remove from the search results. 
    
6. Click **Remove Now**.
    

