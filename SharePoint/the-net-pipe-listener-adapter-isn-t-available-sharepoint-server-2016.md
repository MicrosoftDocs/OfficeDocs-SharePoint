---
title: The Net.Pipe Listener Adapter isn't available (SharePoint Server 2016)
ms.prod: SHAREPOINT
ms.assetid: f8249a19-005f-4ae0-b7c0-04a683691fbf
---


# The Net.Pipe Listener Adapter isn't available (SharePoint Server 2016)
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-05-30* **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "The Net.Pipe Listener Adapter isn't available" for SharePoint Server 2016. **Rule Name:**   The Net.Pipe Listener Adapter isn't available. **Summary:**    The Net.Pipe Listener Adapter is a Windows service that receives activation requests over the net.pipe protocol and passes them to the Windows Process Activation Service. **Cause:**   If the Net.Pipe Listener Adapter service is not installed or started then the SharePoint Health Analyzer rule triggers an alert. **Resolution: Start the Net.Pipe Listener Adapter service on the server**
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
  
2. In Server Manager, click **Tools**, and then click **Services**.
    
  
3. In Services, double-click **Net.Pipe Listener Adapter** and make sure it is running.
    
    > [!NOTE:]
      

