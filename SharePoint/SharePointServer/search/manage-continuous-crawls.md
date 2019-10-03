---
title: "Manage continuous crawls in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 3/8/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: f1bb8664-85dd-49bc-b162-daebf657377e
description: "Learn how to enable and disable continuous crawls in SharePoint Server, and how to change the frequency interval of continuous crawls."
---

# Manage continuous crawls in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
 **Enable continuous crawls** is a crawl schedule option that is an alternative to incremental crawls. This option is new in SharePoint Server and applies only to content sources of type **SharePoint Sites**.
  
Continuous crawls crawl SharePoint Server sites frequently to help keep search results fresh. Like incremental crawls, a continuous crawl crawls content that was added, changed, or deleted since the last crawl. Unlike an incremental crawl, which starts at a particular time and repeats regularly at specified times after that, a continuous crawl automatically starts at predefined time intervals. The default interval for continuous crawls is every 15 minutes. Continuous crawls help ensure freshness of search results because the search index is kept up to date as the SharePoint Server content is crawled so frequently. Thus, continuous crawls are especially useful for crawling SharePoint Server content that is quickly changing.
  
A single continuous crawl includes all content sources in a Search service application for which continuous crawls are enabled. Similarly, the continuous crawl interval applies to all content sources in the Search service application for which continuous crawls are enabled.
  
You cannot run multiple full crawls or multiple incremental crawls for the same content source at the same time. However, multiple continuous crawls can run at the same time. Therefore, even if one continuous crawl is processing a large content update, another continuous crawl can start at the predefined time interval and crawl other updates. Continuous crawls of a particular content repository can also occur while a full or incremental crawl is in progress for the same repository.
  
A continuous crawl doesn't process or retry items that repeatedly return errors. Such errors are retried during a "clean-up" incremental crawl, which automatically runs every four hours for content sources that have continuous crawl enabled. Items that continue to return errors during the incremental crawl will be retried during future incremental crawls, but will not be picked up by the continuous crawls until the errors are resolved.
  
You can set incremental crawl times on the  _Search_Service_Application_Name_: Add/Edit Content Source page, but you can change the frequency interval for continuous crawls only by using Microsoft PowerShell.
  
    
## To enable continuous crawls for an existing content source
<a name="proc1"> </a>

1. Verify that the user account that is performing this procedure is an administrator for the Search service application.
    
2. In Central Administration, in the **Application Management** section, click **Manage service applications**.
    
3. Click the Search service application.
    
4. On the  _Search_Service_Application_Name_: Search Administration page, in the Quick Launch, under **Crawling**, click **Content Sources**. 
    
5. On the  _Search_Service_Application_Name_: Manage Content Sources page, click the SharePoint content source for which you want to enable continuous crawl. 
    
6. In the **Crawl Schedules** section, select **Enable Continuous Crawls**. 
    
7. Click **OK**.
    
8. **Verification:** On the  _Search_Service_Application_Name_: Manage Content Sources page, verify that the **Status** column has the status **Crawling Continuous**.
    
## To enable continuous crawls for a new content source
<a name="proc1"> </a>

1. Verify that the user account that is performing this procedure is an administrator for the Search service application.
    
2. In Central Administration, in the **Application Management** section, click **Manage service applications**.
    
3. Click the Search service application.
    
4. On the  _Search_Service_Application_Name_: Search Administration page, in the Quick Launch, under **Crawling**, click **Content Sources**.
    
5. On the  _Search_Service_Application_Name_: Manage Content Sources page, click **New Content Source**. 
    
6. Create a content source of the type **SharePoint Sites**.
    
  - In the **Name** section, type a name in the **Name** field. 
    
  - In the **Content Source Type** section, select **SharePoint Sites**. 
    
  - In the **Start Addresses** section, type the start address or addresses. 
    
  - In the **Crawl Settings** section, select the crawling behavior for all start addresses. 
    
  - In the **Crawl Schedules** section, select **Enable Continuous Crawls**.
    
7. Click **OK**. 
    
8. **Verification:** On the  _Search_Service_Application_Name_: Manage Content Sources page, verify that the newly added content source appears and that the **Status** column has the status **Crawling Continuous**.
    
## To disable continuous crawls for a content source
<a name="proc2"> </a>

1. Verify that the user account that is performing this procedure is an administrator for the Search service application.
    
2. In Central Administration, in the **Application Management** section, click **Manage service applications**.
    
3. Click the Search service application.
    
4. On the  _Search_Service_Application_Name_: Search Administration page, in the Quick Launch, under **Crawling**, click **Content Sources**. 
    
5. On the  _Search_Service_Application_Name_: Manage Content Sources page, click the SharePoint content source for which you want to disable continuous crawls. 
    
6. In the **Crawl Schedules** section, clear **Enable Incremental Crawls**. This disables continuous crawls.
    
7. To confirm that you want to disable continuous crawls, click **OK**.
    
8. Optional: click **Edit schedule** to change the schedule for incremental crawls, and then click **OK**.
    
9. On the  _Search_Service_Application_Name_: Edit Content Source page, click **OK**. 
    
10. **Verification:** On the  _Search_Service_Application_Name_: Manage Content Sources page, verify that the **Status** column has changed to **Idle**. This might take some time, because all URLs that remain in the crawl queue are still crawled after you disable continuous crawls.
    
## To disable continuous crawls for all content sources
<a name="proc2"> </a>

1. Verify that the user account that performs this procedure is an administrator for the Search service application.
    
2. Start a SharePoint Management Shell on a server in the farm.
    
3. At the Microsoft PowerShell command prompt, type the following commands:
    
  ```
  $SSA =  Get-SPEnterpriseSearchServiceApplication
  $SPContentSources = $SSA | Get-SPEnterpriseSearchCrawlContentSource | WHERE {$_.Type -eq "SharePoint"} 
  foreach ($cs in $SPContentSources) 
  { 
    $cs.EnableContinuousCrawls = $false 
    $cs.Update() 
  }
  ```

4. **Verification:** On the  _Search_Service_Application_Name_: Manage Content Sources page, verify that the **Status** column has changed to **Idle** for all content sources. This might take some time, because all URLs that remain in the crawl queue are still crawled after you disable continuous crawls. 
    
## To change the continuous crawl interval
<a name="Proc3"> </a>

1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
2. Start a SharePoint Management Shell.
    
3. At the Microsoft PowerShell command prompt, type the following commands:
    
  ```
  $ssa = Get-SPEnterpriseSearchServiceApplication
  $ssa.SetProperty("ContinuousCrawlInterval",n)
  ```

    Where:
    
  -  _n_ is the regular interval in minutes at which you want to continuous crawls to start. The default interval is every 15 minutes. The shortest interval that you can set is 1 minute. 
    
    > [!NOTE]
    > If you reduce the interval, you increase the load on SharePoint Server and the crawler. Make sure that you plan and scale out for this increased consumption of resources accordingly. 
  
## See also
<a name="Proc3"> </a>

[Plan crawling and federation in SharePoint Server](plan-crawling-and-federation.md)

[Set-SPEnterpriseSearchCrawlContentSource](/powershell/module/sharepoint-server/Set-SPEnterpriseSearchCrawlContentSource?view=sharepoint-ps)

