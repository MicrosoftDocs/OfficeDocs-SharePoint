---
title: The number of Distributed Cache hosts in the farm exceeds the recommended value (SharePoint Server 2016)
ms.prod: SHAREPOINT
ms.assetid: e56b99dc-3731-4cdd-8576-3777c3827e49
---


# The number of Distributed Cache hosts in the farm exceeds the recommended value (SharePoint Server 2016)
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-05-30* **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "The number of Distributed Cache hosts in the farm exceeds the recommended value" for SharePoint Server 2016. **Rule Name:** The number of Distributed Cache hosts in the farm exceeds the recommended value. **Summary:**  On a farm with four or more servers, you must not start the Distributed Cache service on all servers on the farm. You can only run Distributed cache on servers that are configured as Distributed cache role in SharePoint Server 2016 MInRole. If you configure all servers as cache hosts, you may experience reliability and performance problems in the farm. For more information, see [Overview of MinRole Server Roles in SharePoint Server 2016](html/overview-of-minrole-server-roles-in-sharepoint-server-2016.md). **Cause:** The Distributed Cache service is started on every server on this farm. **Resolution: Reduce the number of cache hosts by using Windows PowerShell.**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the Microsoft PowerShell cmdlets.
    
  
  - Farm Administrators group.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server 2016 cmdlets.
    
    > [!NOTE:]
      
2. Start the SharePoint 2016 Management Shell.
    
    For Windows Server 2012 R2, on the **Start** screen, click **SharePoint 2016 Management Shell**.
    
    For more information about how to interact with Windows Server 2012 R2, see  [Common Management Tasks and Navigation in Windows](http://go.microsoft.com/fwlink/?LinkID=715712&amp;clcid=0x409).
    
  
3. Remove one or more servers from the cache cluster. On each server that you want to remove from the cache cluster, run the following cmdlet:
    
    Remove-SPDistributedCacheServiceInstance
    
  
4. Verify that the server is removed from the cache cluster. To do this, in the SharePoint Central Administration website, click **Manage services on server**, and then, on the **Services on Server** page, make sure that the Distributed Cache service is not listed for the server from which you removed the service.
    
  

# See also

#### 

 **Add-SPDistributedCacheServiceInstance**
  
    
    

  
    
    

