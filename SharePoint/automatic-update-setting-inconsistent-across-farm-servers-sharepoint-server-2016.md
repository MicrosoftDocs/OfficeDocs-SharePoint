---
title: Automatic Update setting inconsistent across farm servers (SharePoint Server 2016)
ms.prod: SHAREPOINT
ms.assetid: 2ddb9cfe-38fc-477c-88d1-beb190e36ab0
---


# Automatic Update setting inconsistent across farm servers (SharePoint Server 2016)
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-05-30* **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "Automatic update setting inconsistent across farm servers", for SharePoint Server 2016. **Rule Name:**   Automatic update setting inconsistent across farm servers. **Summary:**    Servers in the SharePoint farm do not have the same Automatic Update settings configured. **Cause:**   One or more servers in the farm have update settings that are different from the other servers in the farm. **Resolution: Ensure all servers in the farm have the same update settings**
1. Verify that you are a member of the Administrators group on the local computer.
    
  
2. In Control Panel, click **System and Security**, and then under **Windows Update**, click **Turn automatic updating on or off**.
    
  
3. On the Choose your Windows Update settings page, make sure that the update settings are the same as other servers in your farm. Change the update settings if needed.
    
    > [!NOTE:]
      

