---
title: One of the cache hosts in the cluster is down (SharePoint Server 2016)
ms.prod: SHAREPOINT
ms.assetid: c8a62094-b951-47d5-b048-ce6bc5b518be
---


# One of the cache hosts in the cluster is down (SharePoint Server 2016)
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-05-30* **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "One of the cache hosts in the cluster is down", in SharePoint Server 2016. **Rule Name:**   One of the cache hosts in the cluster is down. **Summary:** One of the cache hosts in the cluster is down. This indicates that the SharePoint cache client is trying to connect to the wrong cache host. **Cause:**   The AppFabric Caching service is stopped. **Resolution: Start the AppFabric Caching service.**
- Verify that the user account that is performing this procedure is a member of the Administrators group on the local computer.
    
  
- In **Server Manager**, click **Tools**, and then click **Services**.
    
  
- In the **Services** list, make sure that the status of **AppFabric Caching Service** is **Started**. If not, right-click **AppFabric Caching Service**, and click **Start**.
    
  
By default, the **Repair Automatically** option is enabled for this rule. You can restore the default setting for this rule by doing the following: **Set the Health Analyzer rule to repair automatically**
1. On the SharePoint Central Administration website , click **Monitoring**.
    
  
2. On the Monitoring page, in the **Health Analyzer** section, click **Review rule definitions**.
    
  
3. On the Health Analyzer Rule Definitions – All Rules page, in the **Category: Configuration** section, click the name of the rule.
    
  
4. On the **Health Analyzer Rule Definitions** page, click **Edit Item**.
    
  
5. Select the **Repair Automatically** check box, and then click **Save**.
    
  

