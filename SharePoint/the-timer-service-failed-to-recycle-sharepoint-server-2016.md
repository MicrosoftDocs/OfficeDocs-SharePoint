---
title: The timer service failed to recycle (SharePoint Server 2016)
ms.prod: SHAREPOINT
ms.assetid: 88878bbd-e26e-4fed-8f2a-40a81fb4d528
---


# The timer service failed to recycle (SharePoint Server 2016)
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-05-30* **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "The timer service failed to recycle" for SharePoint Server 2016. **Summary:**  The last attempt to recycle the timer service failed. More than half of the attempts during the past week have also failed. **Cause:** The Timer Service Recycle job conflicts with other long-running timer jobs. **Resolution: Change the schedule for the Timer Service Recycle job so that it does not conflict with other long-running timer jobs.**
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
  
2. On the SharePoint Central Administration website, click **Monitoring**.
    
  
3. On the Monitoring page, in the **Timer Jobs** section, click **Review job definitions**.
    
  
4. On the Job Definitions page, click **Timer Service Recycle**.
    
  
5. On the Edit Timer Job page, change the schedule so that it does not conflict with other long-running timer jobs, and then click **OK**. The default setting is to run daily at 6 AM.
    
  
For more information, see  [Timer job reference for SharePoint Server 2016](html/timer-job-reference-for-sharepoint-server-2016.md).
