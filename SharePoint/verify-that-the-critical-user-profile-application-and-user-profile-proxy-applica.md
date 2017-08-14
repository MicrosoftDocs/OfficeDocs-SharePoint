---
title: Verify that the critical User Profile Application and User Profile Proxy Application timer jobs are available and have not been mistakenly deleted (SharePoint Server 2016)
ms.prod: SHAREPOINT
ms.assetid: bfe89420-2a60-4ce7-8b11-2b45fd38f822
---


# Verify that the critical User Profile Application and User Profile Proxy Application timer jobs are available and have not been mistakenly deleted (SharePoint Server 2016)
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-05-30* **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "Verify that the critical User Profile Application and User Profile Proxy Application timer jobs are available and have not been mistakenly deleted", in SharePoint Server 2016. **Rule Name:**   Verify that the critical User Profile Application and User Profile Proxy Application timer jobs are available and have not been mistakenly deleted. **Summary:**   User Profile Service Application or User Profile service proxy timer jobs are not available and might have been deleted. **Cause: A required timer job for the User Profile service or the User Profile service proxy is missing.** **Resolution: Edit the rule definition so that the configuration is automatically repaired.**
1. On the SharePoint Central Administration website, click **Monitoring**.
    
  
2. On the Monitoring page, in the **Health Analyzer** section, click **Review rule definitions**.
    
  
3. On the Health Analyzer Rule Definitions – All Rules page, in the **Category: Configuration** section, click the name of the rule.
    
  
4. In the **Health Analyzer Rule Definitions** dialog box, click **Edit Item**.
    
  
5. Select the **Repair Automatically** check box, and then click **Save**.
    
  
The system automatically creates the missing timer jobs.For more information, see  [Timer job reference for SharePoint Server 2016](html/timer-job-reference-for-sharepoint-server-2016.md).
