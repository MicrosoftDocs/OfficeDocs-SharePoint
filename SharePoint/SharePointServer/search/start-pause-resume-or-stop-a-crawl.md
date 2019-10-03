---
title: "Start, pause, resume, or stop a crawl in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/26/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: fbfd98f1-403f-4648-9850-f7bd37f2255e
description: "Learn how to start, pause, resume or stop a full or incremental crawl for a content source."
---

# Start, pause, resume, or stop a crawl in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
When you perform a full crawl for a content source, all content specified by the content source is crawled even if the content already exists in the search index. You can start a full crawl for each content source separately. Alternatively, clicking the **Start all crawls** link on the Manage Content Sources page causes the content specified in all content sources to be crawled using an incremental crawl, unless either of the following conditions is true: 
  
- The system detects that a full crawl is required.
    
- The content source is of type **SharePoint Sites** and **Enable Continuous Crawls** is selected in the **Crawl Schedules** section on the Add/Edit Content Source page for the content source. Continuous crawl is a new crawl schedule option in SharePoint Server that applies only to content sources of type **SharePoint Sites**.
    
    
## Before you begin
<a name="begin"> </a>

Before you can perform the procedures in this article, there must be a Search service application in the farm so that you can perform crawls. For more information, see [Create and configure a Search service application in SharePoint Server 2016](create-and-configure-a-search-service-application.md). A Search service application can contain one or more content sources. Each crawl that you perform is associated with a particular content source, which specifies the content to crawl.
  
## Start, pause, resume, or stop a crawl for a content source
<a name="proc1"> </a>

From the Manage Content Sources page, you can start, pause, resume, or stop a crawl for any content source that does not have continuous crawls enabled.
  
 **To start, pause, resume, or stop a crawl for a content source**
  
1. Verify that the user account that is performing this procedure is an administrator for the Search service application.
    
2. In Central Administration, in the **Application Management** section, click **Manage Service Applications**.
    
3. On the Manage Service Applications page, in the list of service applications, click the Search service application.
    
4. On the Search Administration page, in the **Crawling** section, click **Content Sources**.
    
5. On the Manage Content Sources page, in the list of content sources, point to the name of the content source that you want, click the arrow and then click one of the following menu items. (The value in the **Status** column might not automatically refresh when the value changes. To update values in the **Status** column, refresh the Manage Content Sources page by clicking **Refresh**.)
    
  - **Start Full Crawl**. The value in the **Status** column changes to **Crawling Full** for the selected content source. 
    
  - **Start Incremental Crawl**. The value in the **Status** column changes to **Crawling Incremental** for the selected content source. 
    
  - **Resume Crawl**. The value in the **Status** column changes back to **Crawling Full** or **Crawling Incremental** for the selected content source. 
    
  - **Pause Crawl**. The value in the **Status** column changes to **Paused** for the selected content source. 
    
    > [!NOTE]
    > Pausing a crawl has the disadvantage that references to crawl components can remain in the MSSCrawlComponentsState table in the search administration database. This can cause a problem if you want to remove any crawl components (say, because you want to remove a server that hosts those components from the farm). However, when you stop a crawl, references to crawl components in the MSSCrawlComponentsState table are deleted. Therefore, if you want to remove crawl components, it is better to stop crawls than to pause crawls. For more information about removing crawl components, see [Best practices for crawling in SharePoint Server](best-practices-for-crawling.md). 
  
  - **Stop Crawl**. You must click **OK** to confirm that you want to stop the crawl. The value in the **Status** column changes to **Idle** for the selected content source. 
    
    > [!NOTE]
    > If you stop a full or incremental crawl that is in progress (for example, so that you can change the search topology), the next time a crawl occurs for that content source, the Search system automatically performs a full crawl. 
  
## Disable continuous crawls
<a name="proc2"> </a>

From the Manage Content Sources page, continuous crawls can be enabled or disabled, but they cannot be paused or resumed. If you want to pause a content source that is currently in continuous crawl mode, disable continuous crawl first. For more information, see [Manage continuous crawls in SharePoint Server](manage-continuous-crawls.md). 
  

