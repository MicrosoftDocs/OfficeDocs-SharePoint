---
title: Manage a paused Search service application in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: 18b1dbaf-d8e1-416b-b2fb-fe6cd0a369f1
---


# Manage a paused Search service application in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-24* **Summary:** Learn why the Search service application is paused and what you can do to resume it in SharePoint Server 2016 and SharePoint Server 2013.Most operations that require the Search service application to be paused have to complete before the Search service application automatically resumes.We’ll show you how you can find out if and why the Search service application is paused. There are many reasons why the Search service application can be paused -- we’ll list only the most common situations.
## 

 **To manage a paused search service application**
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
  
2. Start a SharePoint 2016 Management Shell on one of the servers in the farm.
    
  - For Windows Server 2008 R2:
    
  - On the **Start** menu, click **All Programs**, click **SharePoint 2016**, right-click **SharePoint 2016 Management Shell** and then click **Run as administrator**.
    
  
  - For Windows Server 2012:
    
  - On the **Start** screen, right-click **SharePoint 2016 Management Shell** and then click **Run as administrator**.
    
    If **SharePoint 2016 Management Shell** is not on the **Start** screen:
    
  
  - Right-click **Computer**, click **All apps**, right-click **SharePoint 2016 Management Shell** and then click **Run as administrator**.
    
  

    For more information about how to interact with Windows Server 2012, see  [Common Management Tasks and Navigation in Windows Server 2012](https://technet.microsoft.com/en-us/library/hh831491.aspx).
    
  
3. At the Microsoft PowerShell command prompt, type the following command(s) to find out if the Search service application is paused.
    
  ```
  
$ssa.IsPaused() -ne 0
  ```


    If this command returns **False**, the Search service application is running.
    
    If this command returns **True**, the Search service application is paused. Go to step 4 to find out why, and what action you should take.
    
  
4. At the Microsoft PowerShell command prompt, type the following command(s) until you find the reason why the Search service application is paused.
    
### 

Command If the command returns True, the Search service application is paused for this reason: Action ($ssa.IsPaused() -band 0x01) -ne 0 <br/> A change in the number of crawl components or crawl databases is in progress.  <br/> Wait until the topology change completes.  <br/> ($ssa.IsPaused() -band 0x02) -ne 0 <br/> A backup or restore procedure is in progress.  <br/> Wait until the backup or restore completes.  After the procedure completes, run the command $ssa.ForceResume(0x02) to verify. For more information, see [Restore Search service applications in SharePoint Server](html/restore-search-service-applications-in-sharepoint-server.md).    <br/> ($ssa.IsPaused() -band 0x04) -ne 0 <br/> A backup of the Volume Shadow Copy Service (VSS) is in progress.  <br/> Wait until the backup completes.  After the VSS backup completes, run the command $ssa.ForceResume(0x02) to verify.   <br/> ($ssa.IsPaused() -band 0x08) -ne 0 <br/> One or more servers in the search topology that host query components are offline.  <br/> Wait until the servers are available again.  <br/> ($ssa.IsPaused() -band 0x20) -ne 0 <br/> One or more crawl databases in the search topology are being rebalanced.  <br/> Wait until the operation completes.  <br/> ($ssa.IsPaused() -band 0x40) -ne 0 <br/> One or more link databases in the search topology are being rebalanced.  <br/> Wait until the operation completes.  <br/> ($ssa.IsPaused() -band 0x80) -ne 0 <br/> An administrator has manually paused the Search service application.  <br/> If you know the reason, you can resume the Search service application. Run the command $ssa.resume() to resume the Search service application. <br/> If you don’t know the reason, find out why someone has manually paused the Search service application.  <br/> ($ssa.IsPaused() -band 0x100) -ne 0 <br/> The search index is being deleted.  <br/> Wait until the search index is deleted.  <br/> ($ssa.IsPaused() -band 0x200) -ne 0 <br/> The search index is being repartitioned.  <br/> Wait until the operation completes. For more information, see  [Manage the index component in SharePoint Server](html/manage-the-index-component-in-sharepoint-server.md).  <br/> 5. After you’ve waited until the operation completes, at the Microsoft PowerShell command prompt, type the following command to make sure that the Search service application is running:
    
  ```
  
$ssa.IsPaused() -ne 0
  ```


    If this command returns **False**, the Search service application is running.
    
    If this command returns **True**, the Search service application is paused. Re-run the commands from step 4 to find out why.
    
  

