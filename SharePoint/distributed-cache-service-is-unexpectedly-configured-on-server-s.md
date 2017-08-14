---
title: Distributed cache service is unexpectedly configured on server(s)
ms.prod: SHAREPOINT
ms.assetid: d7d023a6-0d61-47ae-b442-3fd8108bcbb7
---


# Distributed cache service is unexpectedly configured on server(s)
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-05-30* **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "Distributed cache service is unexpectedly configured on server(s)" in SharePoint Server 2016. **Rule Name:** Distributed cache service is unexpectedly configured on server(s).
## 

 **Summary:**    The distributed cache service instance should not be configured for the failing servers. Remove the distributed cache service instances from the failing servers.Typically when you see this rule, it states that the distributed cache service is configured on a server that isn't meant to run this service in MinRole. For more information, see  [Description of MinRole and associated services in SharePoint Server 2016](html/description-of-minrole-and-associated-services-in-sharepoint-server-2016.md). **Cause:**   This rule occurs when you have configured the distributed cache service on a server that is not supposed to run this service in a SharePoint Server 2016 farm. **Resolution: Remove the distributed cache service instances from the failing servers**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server 2016 cmdlets.
    
    > [!NOTE:]
      
2. Start the SharePoint 2016 Management Shell on each failing server.
    
  
3. Type the following command at the PowerShell command prompt on each failing server:
    
  ```
  
Remove-SPDistributedCacheServiceInstance
  ```

For more information, see  [Remove-SPDistributedCacheServiceInstance](https://technet.microsoft.com/en-us/library/jj730452%28v=office.16%29.aspx).
