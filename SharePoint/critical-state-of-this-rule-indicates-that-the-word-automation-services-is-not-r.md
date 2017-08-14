---
title: Critical state of this rule indicates that the Word Automation Services is not running when it should be running (SharePoint Server 2016)
ms.prod: SHAREPOINT
ms.assetid: e00cc8ed-8a01-4928-9175-49efe03288a1
---


# Critical state of this rule indicates that the Word Automation Services is not running when it should be running (SharePoint Server 2016)
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-05-30* **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "Critical state of this rule indicates that the Word Automation Services is not running when it should be running" in SharePoint Server 2016. **Rule Name:**   Critical state of this rule indicates that the Word Automation Services is not running when it should be running. **Summary:** Word Automation Services uses a timer job to pull conversion items from the Word Automation Services database and then assign those conversion items to individual application servers. If the timer job does not run, conversion items cannot start to convert. **Cause:** The Word Automation Services timer job is not enabled. **Resolution: Enable the Word Automation Services timer job.**
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
  
2. On the SharePoint Central Administration website, click **Monitoring**.
    
  
3. On the Monitoring page, in the **Timer Jobs** section, click **Review job definitions**.
    
  
4. On the Job Definitions page, in the list of timer jobs, click **Word Automation Services Timer Job**.
    
  
5. On the Edit Timer Job page, in the **Recurring Schedule** section, specify when you want the timer job to run, and then click **Enable**.
    
  

