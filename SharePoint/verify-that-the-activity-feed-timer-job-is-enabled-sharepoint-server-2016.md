---
title: Verify that the Activity Feed Timer Job is enabled (SharePoint Server 2016)
ms.prod: SHAREPOINT
ms.assetid: d04ccc23-89b1-4927-9607-2a1073d67580
---


# Verify that the Activity Feed Timer Job is enabled (SharePoint Server 2016)
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-05-30* **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "Verify that the Activity Feed Timer Job is enabled", for SharePoint Server 2016. **Rule Name:**   Verify that the Activity Feed Timer Job is enabled. **Summary:**    You must enable the Activity Feed timer job if you want users to receive information about their colleagues, such as updates to profile properties and creation of social tags and notes. **Cause:**   The Activity Feed timer job is not enabled. **Resolution: Enable the Activity Feed timer job**
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
  
2. On the SharePoint Central Administration website, on the Quick Launch, click **Monitoring**.
    
  
3. On the Monitoring page, in the **Timer Jobs** section, click **Review job definitions**.
    
  
4. On the Job Definitions page, in the list of timer jobs, click **User Profile Service Application – Activity Feed Job**.
    
  
5. On the Edit Timer Job page, in the **Recurring Schedule** section, specify when you want the timer job to run, and then click **Enable**.
    
  

# See also

#### 

 [Timer job reference for SharePoint Server 2016](html/timer-job-reference-for-sharepoint-server-2016.md)
  
    
    

  
    
    

