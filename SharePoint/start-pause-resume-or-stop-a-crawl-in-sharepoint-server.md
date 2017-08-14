---
title: Start, pause, resume, or stop a crawl in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: fbfd98f1-403f-4648-9850-f7bd37f2255e
---


# Start, pause, resume, or stop a crawl in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-25* **Summary:** Learn how to start, pause, resume or stop a full or incremental crawl for a content source.When you perform a full crawl for a content source, all content specified by the content source is crawled even if the content already exists in the search index. You can start a full crawl for each content source separately. Alternatively, clicking the **Start all crawls** link on the Manage Content Sources page causes the content specified in all content sources to be crawled using an incremental crawl, unless either of the following conditions is true:
- The system detects that a full crawl is required.
    
  
- The content source is of type **SharePoint Sites** and **Enable Continuous Crawls** is selected in the **Crawl Schedules** section on the Add/Edit Content Source page for the content source. Continuous crawl is a new crawl schedule option in SharePoint Server that applies only to content sources of type **SharePoint Sites**.
    
  
In this article:
-  [Before you begin](#begin)
    
  
-  [Start, pause, resume, or stop a crawl](#proc1)
    
  
-  [Disable continuous crawls](#proc2)
    
  

## Before you begin
<a name="begin"> </a>

Before you can perform the procedures in this article, there must be a Search service application in the farm so that you can perform crawls. For more information, see  [Create and configure a Search service application in SharePoint Server 2016](html/create-and-configure-a-search-service-application-in-sharepoint-server-2016.md). A Search service application can contain one or more content sources. Each crawl that you perform is associated with a particular content source, which specifies the content to crawl.
## Start, pause, resume, or stop a crawl for a content source
<a name="proc1"> </a>

From the Manage Content Sources page, you can start, pause, resume, or stop a crawl for any content source that does not have continuous crawls enabled. **To start, pause, resume, or stop a crawl for a content source**
1. Verify that the user account that is performing this procedure is an administrator for the Search service application.
    
  
2. In Central Administration, in the **Application Management** section, click **Manage Service Applications**.
    
  
3. On the Manage Service Applications page, in the list of service applications, click the Search service application.
    
  
4. On the Search Administration page, in the **Crawling** section, click **Content Sources**.
    
  
5. On the Manage Content Sources page, in the list of content sources, point to the name of the content source that you want, click the arrow and then click one of the following menu items. (The value in the **Status** column might not automatically refresh when the value changes. To update values in the **Status** column, refresh the Manage Content Sources page by clicking **Refresh**.)
    
  - **Start Full Crawl**. The value in the **Status** column changes to **Crawling Full** for the selected content source.
    
  
  - **Start Incremental Crawl**. The value in the **Status** column changes to **Crawling Incremental** for the selected content source.
    
  
  - **Resume Crawl**. The value in the **Status** column changes back to **Crawling Full** or **Crawling Incremental** for the selected content source.
    
  
  - **Pause Crawl**. The value in the **Status** column changes to **Paused** for the selected content source.
    
    > [!NOTE:]
      
  - **Stop Crawl**. You must click **OK** to confirm that you want to stop the crawl. The value in the **Status** column changes to **Idle** for the selected content source.
    
    > [!NOTE:]
      

## Disable continuous crawls
<a name="proc2"> </a>

From the Manage Content Sources page, continuous crawls can be enabled or disabled, but they cannot be paused or resumed. If you want to pause a content source that is currently in continuous crawl mode, disable continuous crawl first. For more information, see  [Manage continuous crawls in SharePoint Server](html/manage-continuous-crawls-in-sharepoint-server.md). 
