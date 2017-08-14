---
title: Product / patch installation or server upgrade required (SharePoint Server 2016)
ms.prod: SHAREPOINT
ms.assetid: 89377b22-b1de-4f11-9a16-e54783c046fc
---


# Product / patch installation or server upgrade required (SharePoint Server 2016)
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-05-30* **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "Product / patch installation or server upgrade required" for SharePoint Server 2016. **Rule Name:**   Product / patch installation or server upgrade required **Summary:**   You must install all required products on all servers in the farm, and all products should have the same software update and upgrade level across the farm. **Cause:** You have not installed required products or updates, or the server needs to be upgraded. **Resolution: Install software updates and security updates or upgrade the server.**
- Check if there are any pending updates and restart all the servers. 
    
    **Install updates on the server.**
    
1. Log on to one server.
    
  
2. Verify that the user account that is performing this procedure is a member of the Administrators group on the local computer.
    
  
3. Open **Windows Update**. and check to see if there are any pending updates or a restart is required, schedule the updates or restart the computer.
    
  
4. Repeat the previous steps on all servers.
    
  

    For more information, see  [Deploy software updates for SharePoint Server 2016](html/deploy-software-updates-for-sharepoint-server-2016.md).
    
  
- If a previous upgrade attempt has failed, you must resolve upgrade issues before attempting upgrade again. You can use the SharePoint Central Administration website to find information about current and previous upgrade attempts and determine issues that may be preventing upgrade from succeeding. To do this in Central Administration, in the **Upgrade and Migration** section, click **Check upgrade status**.
    
  

