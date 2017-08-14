---
title: Distributed cache service is not enabled in this deployment (SharePoint Server 2016)
ms.prod: SHAREPOINT
ms.assetid: 6e743c5b-b70c-4e86-ae31-e5ffcc0c099a
---


# Distributed cache service is not enabled in this deployment (SharePoint Server 2016)
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-05-30* **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "Distributed cache service is not enabled in this deployment", for SharePoint Server 2016 **Rule Name:** Distributed cache service is not enabled in this deployment. **Summary:**  The Distributed Cache service is started on all servers that run SharePoint products at installation time. However, an administrator that performs maintenance and operational tasks might need to start and stop the Distributed Cache service. This event occurs when the Distributed Cache service is stopped. **Cause:** The Distributed Cache service is disabled on this server. **Resolution: Enable the Distributed Cache service by using Microsoft PowerShell.**
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
    
  
3. On the server on which you want to enable the Distributed Cache service, run the following command:
    
    Add-SPDistributedCacheServiceInstance
    
  
4. Verify that the Distributed Cache service is started. To do this, in the SharePoint Central Administration website, click **Application Management**. In the **Service Applications** section, click **Manage services on server**. On the **Services on Server** page, make sure that the Distributed Cache service is listed, and the status is **Started**.
    
  

# See also

#### 

 **Add-SPDistributedCacheServiceInstance**
  
    
    

  
    
    

