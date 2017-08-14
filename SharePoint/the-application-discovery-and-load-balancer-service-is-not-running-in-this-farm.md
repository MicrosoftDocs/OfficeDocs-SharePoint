---
title: The Application Discovery and Load Balancer Service is not running in this farm (SharePoint Server 2016)
ms.prod: SHAREPOINT
ms.assetid: 70d6f3af-2ad4-497d-a449-d75bacfd8aea
---


# The Application Discovery and Load Balancer Service is not running in this farm (SharePoint Server 2016)
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-05-30* **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "The Application Discovery and Load Balancer Service is not running in this farm" for SharePoint Server 2016. **Rule Name:**   The Application Discovery and Load Balancer Service is not running in this farm. **Summary:**   The Application Discovery and Load Balancer service provides information about the topology of the farm to users who are using services offered by the farm. Users can use this information to perform load balancing. The Application Discovery and Load Balancer Service should be running on at least one server in the farm. **Cause:** The Application Discovery and Load Balancer service is stopped. **Resolution: Start the Application Discovery and Load Balancer service on at least one server in the farm.**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the Microsoft PowerShell cmdlets.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint cmdlets.
    
    > [!NOTE:]
      
2. Start the SharePoint 2016 Management Shell.
    
    For Windows Server 2012 R2, on the **Start** screen, click **SharePoint 2016 Management Shell**.
    
    For more information about how to interact with Windows Server 2012 R2, see  [Common Management Tasks and Navigation in Windows](http://go.microsoft.com/fwlink/?LinkID=715712&amp;clcid=0x409).
    
  
3. At the PowerShell command prompt, type the following command: 
  
    
    

  
    
    
Get-SPServiceInstance -ALL
    
    For more information, see **Get-SPServiceInstance**.
    
  
4. Find the GUID of the Application Discovery and Load Balancer service.
    
  
5. Type the following command: 
  
    
    

  
    
    
Start-SPServiceInstance [-Identity]
    
    Where  *[-Identity]*  is the GUID for the Application Discovery and Load Balancer service. For more information, see **Start-SPServiceInstance**.
    
  

