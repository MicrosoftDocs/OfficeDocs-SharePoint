---
title: More cache hosts are running in this deployment than are registered with SharePoint (SharePoint Server 2016)
ms.prod: SHAREPOINT
ms.assetid: 5e7be5ff-5216-406b-9bfe-f9ff1f9651aa
---


# More cache hosts are running in this deployment than are registered with SharePoint (SharePoint Server 2016)
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-05-30* **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "More Cache hosts are running in this deployment than are registered with SharePoint", in SharePoint Server 2016. **Rule Name:** More Cache hosts are running in this deployment than are registered with SharePoint. **Summary:**   Some cache hosts are running but not registered with SharePoint Server 2016. **Cause:** SharePoint Server 2016 fails to identify some cache hosts. **Resolution: Log on to the cache host that is not registered with SharePoint Server 2016, and then manually stop the AppFabric Caching Service.**
1. Identify the cache hosts that are not registered with SharePoint Server 2016. To do this, in the SharePoint Central Administration website, in the **Monitoring** section, click **Review problems and solutions**, and then find the name of the server in the **Failing Servers** list. If there are multiple failing servers in a server farm, you must repeat the following steps on each failing server.
    
  
2. Verify that the user account that is performing this procedure is a member of the Administrators group on the local computer.
    
  
3. On **Server Manager**, click **Tools**, and then select **Services**.
    
  
4. In the **Services** list, double-click **AppFabric Caching Service**.
    
  
5. In the **AppFabric Caching Service Properties (Local Computer)** dialog box, click **Stop**.
    
  

