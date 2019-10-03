---
title: "Reset the search index in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 9/8/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 7a1835c3-6375-4647-b190-84676fc9f9b0
description: "Learn how to reset the SharePoint Server search index."
---

# Reset the search index in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
When you reset the search index in SharePoint Server, all content is immediately removed from the search index and users will not be able to retrieve search results. After you reset the search index, you must perform a full crawl of one or more content sources to create a new search index. Users will be able to retrieve search results again when the full crawl is finished and the new search index is created.
  
> [!NOTE]
> After a search index reset, a full crawl won't restore all analytics features that are powered by the Analytics Processing Component. Examples of analytics features are raising or demoting items in search results based on which search results users have clicked, or displaying the number of times a search result has been viewed. For more information, see [Overview of analytics processing in SharePoint Server](overview-of-analytics-processing.md). 
> 
> If you can, you should perform a backup and restore of your Search service application instead of a search index reset. These procedures will fully restore all features that are powered by the Analytics Processing Component. For more information, see [Back up Search service applications in SharePoint Server](../administration/back-up-a-search-service-application.md) and [Restore Search service applications in SharePoint Server](../administration/restore-a-search-service-application.md). 
  
> [!NOTE]
> If your SharePoint environment is hybrid and uses [cloud hybrid search](/SharePoint/hybrid/learn-about-cloud-hybrid-search-for-sharepoint), you index your on-premises content in your search index in Office 365. See [Learn about cloud hybrid search for SharePoint](/SharePoint/hybrid/learn-about-cloud-hybrid-search-for-sharepoint) for guidance on deleting metadata of on-premises items from the search index in Office 365. 
  
    
## Before you begin
<a name="begin"> </a>

Make sure that you are not running a backup of the Search service application.
  
## Reset the search index
<a name="proc1"> </a>

Use the following procedure to reset the search index.
  
 **To reset the search index**
  
1. Verify that the user account that is performing this procedure is an administrator for the Search service application for which you want to reset the search index.
    
2. On the SharePoint Central Administration home page, in the **Application Management** section, click **Manage service applications**.
    
3. On the Manage Search Applications page, click the Search service application for which you want to reset the search index. 
    
4. On the Search Administration page, under System Status, verify that the **Administrative status** of the Search service application is **Running** and not **Paused**. 
    
5. On the Search Administration page, in the **Crawling** section, click **Index Reset**.
    
6. On the Index Reset page, verify that the **Deactivate search alerts during reset** check box is checked, and then click **Reset Now**.
    
7. In the confirmation dialog box that appears, click **OK** to confirm that you want to reset the index. 
    
    The Search Administration page opens and the System Status is displayed.
    
After the search index reset is complete, you must perform a full crawl of all the content sources that you want to include in the search index. For more information, see Add, edit, or delete a content source in SharePoint 2013 Preview. Users will not be able to retrieve search results until you create a new search index. After the full crawl has completed and a new search index has been created, you must also re-enable search alerts. See [Enable search alerts](enable-search-alerts.md).
  

