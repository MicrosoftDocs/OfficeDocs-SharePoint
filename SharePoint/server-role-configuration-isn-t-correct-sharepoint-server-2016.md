---
title: Server role configuration isn't correct (SharePoint Server 2016)
ms.prod: SHAREPOINT
ms.assetid: 23829b00-db4c-4400-b236-e86ea60fa193
---


# Server role configuration isn't correct (SharePoint Server 2016)
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-05-30* **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "Server role configuration isn't correct" for SharePoint Server 2016. **Rule Name:**   Server role configuration isn't correct. **Summary:**    This new rule helps ensure that your servers are operating in their optimal MinRole configuration. This rule runs every night at midnight on each server in your SharePoint Server 2016 farm. The rule scans all service instances on the server to detect if any are not in compliance.UNRESOLVED_TOKEN_VAL() **Cause:**   A service application on the server isn't correctly configured. **Resolution: Automatically reconfigures the service to match the expected configuration**
1. If any service instance is not in compliance, the health rule automatically reconfigures the service to match the expected configuration.
    
  
2. No manual intervention by the SharePoint farm administrator is required.
    
  
3. The automatic repair functionality of this health rule can be disabled by the SharePoint farm administrator while still allowing the health rule to run.
    
  
4. If the health rule detects that a server is out of compliance and the automatic repair functionality is disabled, it generates a health report in Central Administration. The health report identifies which servers are out of compliance and offers the ability to automatically repair the server and also provide instructions about how to manually fix the servers.
    
    For more information, see the Health monitoring section in  [Overview of MinRole Server Roles in SharePoint Server 2016](html/overview-of-minrole-server-roles-in-sharepoint-server-2016.md).
    
  

