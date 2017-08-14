---
title: This Distributed Cache host may cause cache reliability problems (SharePoint Server 2016)
ms.prod: SHAREPOINT
ms.assetid: 45b39899-1686-43e5-9073-e51d2979ba9b
---


# This Distributed Cache host may cause cache reliability problems (SharePoint Server 2016)
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-05-30* **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "This Distributed Cache host may cause cache reliability problems", in SharePoint Server 2016. **Rule Name:** This Distributed Cache host may cause cache reliability problems. **Summary:**  The Distributed Cache service on this cache host has been stopped but has not been unregistered from the farm. To avoid reliability issues, we recommend that you either start the Distributed Cache service on the server, or remove the cache host from the cache cluster. **Cause:** The Distributed Cache service on this Distributed Cache host has been stopped but not unregistered from the farm. **Resolution: Start the Distributed Cache service on the server by using Microsoft PowerShell.**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  
  - Farm Administrators group.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server 2016 cmdlets.
    
    > [!NOTE:]
      
2. Start the SharePoint 2016 Management Shell.
    
    For Windows Server 2012 R2, on the **Start** screen, click **SharePoint 2016 Management Shell**.
    
    For more information about how to interact with Windows Server 2012 R2, see  [Common Management Tasks and Navigation in Windows](http://go.microsoft.com/fwlink/?LinkID=715712&amp;clcid=0x409).
    
  
3. On the server on which you want to start the Distributed Cache service, type the following command at the PowerShell command prompt:
    
  ```
  
Add-SPDistributedCacheServiceInstance
  ```

4. In the SharePoint Central Administration website, click **Application Management**. In the **Service Applications** section, click **Manage services on server**.
    
  
5. On the **Services on Server** page, verify that the Distributed Cache service is listed and the status is **Started**.
    
  
 **Resolution: Remove the cache host from the cache cluster by using Windows PowerShell.**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  
  - Farm Administrators group.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server 2016 cmdlets.
    
    > [!NOTE:]
      
2. Start the SharePoint 2016 Management Shell.
    
  
3. Type the following command at the PowerShell command prompt:
    
  ```
  
Remove-SPDistributedCacheServiceInstance
  ```


    > [!NOTE:]
      

    For more information, see **Remove-SPDistributedCacheServiceInstance**.
    
  
4. Verify that the server is removed from the cache cluster. To do this, in Central Administration, click **Manage services on server**, and then, on the **Services on Server** page, make sure that the Distributed Cache service is not listed.
    
  

