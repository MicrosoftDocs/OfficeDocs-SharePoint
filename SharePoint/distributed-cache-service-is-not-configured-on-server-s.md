---
title: Distributed cache service is not configured on server(s)
ms.prod: SHAREPOINT
ms.assetid: 0e24bb6a-8977-467f-bf69-0cfef1c8e288
---


# Distributed cache service is not configured on server(s)
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-05-30* **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "Distributed cache service is not configured on server(s)" in SharePoint Server 2016. **Rule Name:** Distributed cache service is not configured on server(s).
## 

 **Summary:**    The distributed cache service should be configured for the failing servers. Register the distributed cache host on the failing servers, and then start the service instances. **Cause:**   This rule occurs when you have used the MinRole feature in SharePoint Server 2016 to assign a distributed cache role to a server or servers but haven't registered the distributed cache host or started the service. **Resolution: Use the Add-SPDistributedCacheServiceInstance cmdlet to register a cache host**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server 2016 cmdlets.
    
    > [!NOTE:]
      
2. Start the SharePoint 2016 Management Shell on each failing server.
    
  
3. Type the following command at the PowerShell command prompt on each failing server:
    
  ```
  
Add-SPDistributedCacheServiceInstance
  ```

For more information, see  [Add-SPDistributedCacheServiceInstance](https://technet.microsoft.com/en-us/library/jj730445%28v=office.16%29.aspx).
## Related Topics

 [Description of MinRole and associated services in SharePoint Server 2016](html/description-of-minrole-and-associated-services-in-sharepoint-server-2016.md)
