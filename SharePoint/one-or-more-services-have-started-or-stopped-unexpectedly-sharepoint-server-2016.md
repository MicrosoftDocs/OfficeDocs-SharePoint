---
title: One or more services have started or stopped unexpectedly (SharePoint Server 2016)
ms.prod: SHAREPOINT
ms.assetid: f91de311-e531-4a15-bcc4-b4af01774e0b
---


# One or more services have started or stopped unexpectedly (SharePoint Server 2016)
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-05-30* **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "One or more services have started or stopped unexpectedly" for SharePoint Server 2016. **Rule Name:**   One or more services have started or stopped unexpectedly. **Summary:**    A critical service required for the SharePoint farm to function is not running. **Cause:**   One or more critical services are not running on the specified server. **Resolution: Start the service that is not running**
1. Verify that the user account that is performing this procedure is a member of the Administrators group on the local computer.
    
  
2. In Server Manager, click **Tools**, and then click **Services**.
    
  
3. Right-click the service that you want to start, and then click **Start**.
    
  

