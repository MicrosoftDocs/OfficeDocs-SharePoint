---
title: The Machine Translation Service is not running when it should be running (SharePoint Server 2016)
ms.prod: SHAREPOINT
ms.assetid: f140e0ad-07e4-42f8-a198-54d800355698
---


# The Machine Translation Service is not running when it should be running (SharePoint Server 2016)
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-05-30* **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "The Machine Translation Service is not running when it should be running", in SharePoint Server 2016. **Rule Name:**  The Machine Translation Service is not running when it should be running. **Summary:** The Machine Translation Service batch mode uses a timer job to pull translation items from the Machine Translation Service database and then assign those translation items to individual application servers. If the timer job doesn't run, items can't be translated. **Cause:**  The Machine Translation Service timer job isn't enabled. **Resolution: Enable the Machine Translation Service timer job.**
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
  
2. On Central Administration , click **Monitoring**.
    
  
3. On the Job Definitions page, in the list of timer jobs, click **Machine Translation Service Timer Job**.
    
  
4. On the Edit Timer Job page, in the **Recurring Schedule** section, specify when you want the timer job to run, and then click **Enable**.
    
    The default is every 15 minutes.
    
  

## 


# See also

#### 

 [Timer job reference for SharePoint Server 2016](html/timer-job-reference-for-sharepoint-server-2016.md)
  
    
    

  
    
    

