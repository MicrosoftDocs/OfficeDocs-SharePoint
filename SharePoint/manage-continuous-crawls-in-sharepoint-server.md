---
title: Manage continuous crawls in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: f1bb8664-85dd-49bc-b162-daebf657377e
---


# Manage continuous crawls in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-24* **Summary:** Learn how to enable and disable continuous crawls in SharePoint Server 2016 and SharePoint Server 2013, and how to change the frequency interval of continuous crawls. **Enable continuous crawls** is a crawl schedule option that is an alternative to incremental crawls. This option is new in SharePoint Server and applies only to content sources of type **SharePoint Sites**.Continuous crawls crawl SharePoint Server sites frequently to help keep search results fresh. Like incremental crawls, a continuous crawl crawls content that was added, changed, or deleted since the last crawl. Unlike an incremental crawl, which starts at a particular time and repeats regularly at specified times after that, a continuous crawl automatically starts at predefined time intervals. The default interval for continuous crawls is every 15 minutes. Continuous crawls help ensure freshness of search results because the search index is kept up to date as the SharePoint Server content is crawled so frequently. Thus, continuous crawls are especially useful for crawling SharePoint Server content that is quickly changing.A single continuous crawl includes all content sources in a Search service application for which continuous crawls are enabled. Similarly, the continuous crawl interval applies to all content sources in the Search service application for which continuous crawls are enabled.You cannot run multiple full crawls or multiple incremental crawls for the same content source at the same time. However, multiple continuous crawls can run at the same time. Therefore, even if one continuous crawl is processing a large content update, another continuous crawl can start at the predefined time interval and crawl other updates. Continuous crawls of a particular content repository can also occur while a full or incremental crawl is in progress for the same repository.A continuous crawl does not process or retry items that return errors more than three times. A "clean-up" incremental crawl automatically runs every four hours for content sources that have continuous crawl enabled to re-crawl any items that repeatedly return errors. This incremental crawl will try to crawl the item again and then will postpone retries if the error persists.You can set incremental crawl times on the  *Search_Service_Application_Name*  : Add/Edit Content Source page, but you can change the frequency interval for continuous crawls only by using Microsoft PowerShell.In this article:
-  [To enable continuous crawls for an existing content source](#proc1)
    
  
-  [To enable continuous crawls for a new content source](#Enable_for_new)
    
  
-  [To disable continuous crawls for a content source](#proc2)
    
  
-  [To disable continuous crawls for all content sources](#Disable_for_all)
    
  
-  [To change the continuous crawl interval](#Change_interval)
    
  
 **To enable continuous crawls for an existing content source**
1. Verify that the user account that is performing this procedure is an administrator for the Search service application.
    
  
2. In Central Administration, in the **Application Management** section, click **Manage service applications**.
    
  
3. Click the Search service application.
    
  
4. On the  *Search_Service_Application_Name*  : Search Administration page, in the Quick Launch, under **Crawling**, click **Content Sources**.
    
  
5. On the  *Search_Service_Application_Name*  : Manage Content Sources page, click the SharePoint content source for which you want to enable continuous crawl.
    
  
6. In the **Crawl Schedules** section, select **Enable Continuous Crawls**.
    
  
7. Click **OK**.
    
  
8. **Verification:** On the *Search_Service_Application_Name*  : Manage Content Sources page, verify that the **Status** column has the status **Crawling Continuous**.
    
  
 **To enable continuous crawls for a new content source**
1. Verify that the user account that is performing this procedure is an administrator for the Search service application.
    
  
2. In Central Administration, in the **Application Management** section, click **Manage service applications**.
    
  
3. Click the Search service application.
    
  
4. On the  *Search_Service_Application_Name*  : Search Administration page, in the Quick Launch, under **Crawling**, click **Content Sources**.
    
  
5. On the  *Search_Service_Application_Name*  : Manage Content Sources page, click **New Content Source**.
    
  
6. Create a content source of the type **SharePoint Sites**.
    
1. In the **Name** section, type a name in the **Name** field.
    
  
2. In the **Content Source Type** section, select **SharePoint Sites**.
    
  
3. In the **Start Addresses** section, type the start address or addresses.
    
  
4. In the **Crawl Settings** section, select the crawling behavior for all start addresses.
    
  
5. In the **Crawl Schedules** section, select **Enable Continuous Crawls**.
    
  
7. Click **OK**.
    
  
8. **Verification:** On the *Search_Service_Application_Name*  : Manage Content Sources page, verify that the newly added content source appears and that the **Status** column has the status **Crawling Continuous**.
    
  
 **To disable continuous crawls for a content source**
1. Verify that the user account that is performing this procedure is an administrator for the Search service application.
    
  
2. In Central Administration, in the **Application Management** section, click **Manage service applications**.
    
  
3. Click the Search service application.
    
  
4. On the  *Search_Service_Application_Name*  : Search Administration page, in the Quick Launch, under **Crawling**, click **Content Sources**.
    
  
5. On the  *Search_Service_Application_Name*  : Manage Content Sources page, click the SharePoint content source for which you want to disable continuous crawls.
    
  
6. In the **Crawl Schedules** section, clear **Enable Incremental Crawls**. This disables continuous crawls.
    
  
7. To confirm that you want to disable continuous crawls, click **OK**.
    
  
8. Optional: click **Edit schedule** to change the schedule for incremental crawls, and then click **OK**.
    
  
9. On the  *Search_Service_Application_Name*  : Edit Content Source page, click **OK**.
    
  
10. **Verification:** On the *Search_Service_Application_Name*  : Manage Content Sources page, verify that the **Status** column has changed to **Idle**. This might take some time, because all URLs that remain in the crawl queue are still crawled after you disable continuous crawls.
    
  

## 
<a name="proc2"> </a>

 **To disable continuous crawls for all content sources**
1. Verify that the user account that performs this procedure is an administrator for the Search service application.
    
  
2. Start a SharePoint 2016 Management Shell on a server in the farm.
    
  - For Windows Server 2008 R2:
    
    On the **Start** menu, click **All Programs**, click **SharePoint 2016**, then right-click **SharePoint 2016 Management Shell** and then click **Run as administrator**.
    
  
  - For Windows Server 2012:
    
1. On the **Start** screen, right-click **SharePoint 2016 Management Shell** and then click **Run as administrator**.
    
    If **SharePoint 2016 Management Shell** does not appear on the **Start** screen:
    
  
2. Right-click **Computer**, click **All apps**, right-click **SharePoint 2016 Management Shell**, and then click **Run as administrator**.
    
  

    For more information about how to use Windows Server 2012, see  [Common Management Tasks and Navigation in Windows Server 2012](http://go.microsoft.com/fwlink/p/?LinkId=276950).
    
  
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

4. **Verification:** On the *Search_Service_Application_Name*  : Manage Content Sources page, verify that the **Status** column has changed to **Idle** for all content sources. This might take some time, because all URLs that remain in the crawl queue are still crawled after you disable continuous crawls.
    
  

## 
<a name="Proc3"> </a>

 **To change the continuous crawl interval**
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
  
2. Start a SharePoint 2016 Management Shell.
    
  - For Windows Server 2008 R2:
    
    On the **Start** menu, click **All Programs**, click **SharePoint 2016**, right-click **SharePoint 2016 Management Shell** and then click **Run as administrator**.
    
  
  - For Windows Server 2012:
    
1. On the **Start** screen, right-click **SharePoint 2016 Management Shell**, and then click **Run as administrator**.
    
    If **SharePoint 2016 Management Shell** does not appear on the **Start** screen:
    
  
2. Right-click **Computer**, click **All apps**, right-click **SharePoint 2016 Management Shell** and then click **Run as administrator**.
    
  

    For more information about how to interact with Windows Server 2012, see  [Common Management Tasks and Navigation in Windows Server 2012](http://go.microsoft.com/fwlink/p/?LinkId=276950).
    
  
3. At the Microsoft PowerShell command prompt, type the following commands:
    
  ```
  
$ssa = Get-SPEnterpriseSearchServiceApplication
$ssa.SetProperty("ContinuousCrawlInterval",n )
  ```


    Where:
    
  -  *n*  is the regular interval in minutes at which you want to continuous crawls to start. The default interval is every 15 minutes. The shortest interval that you can set is 1 minute.
    
    > [!NOTE:]
      

# See also

#### 

 [Plan crawling and federation in SharePoint Server](html/plan-crawling-and-federation-in-sharepoint-server.md)
  
    
    

#### 

 **Set-SPEnterpriseSearchCrawlContentSource**
  
    
    

  
    
    

