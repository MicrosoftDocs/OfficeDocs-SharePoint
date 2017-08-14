---
title: One or more categories are configured with Verbose trace logging (SharePoint Server 2016)
ms.prod: SHAREPOINT
ms.assetid: c78266d8-33de-4edc-94ea-b8110ac8db81
---


# One or more categories are configured with Verbose trace logging (SharePoint Server 2016)
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-05-30* **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "One or more categories are configured with verbose trace logging" in SharePoint Server 2016. **Rule Name:**   One or more categories are configured with Verbose trace logging. **Summary:**    SharePoint Server writes diagnostic logging information to record activity on the server. The logs contain information that can help you diagnose server problems. This rule occurs when diagnostic logging is set to verbose. The verbose setting is appropriate when you have to diagnose a server problem, but you should turn off verbose logging during normal operations. **Cause:**   One or more categories of diagnostic logging are set to verbose. **Resolution: Reset diagnostic logging to the default level**
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
  
2. On the SharePoint Central Administration website, click **Monitoring**.
    
  
3. On the Monitoring page, in the **Reporting** section, click **Configure diagnostic logging**.
    
  
4. On the Diagnostic Logging page, in the **Event Throttling** section, in the **Least critical event to report to the event log** list and **Least critical event to report to the trace log** list, select **Reset to default**.
    
  
5. Click **OK**.
    
  

