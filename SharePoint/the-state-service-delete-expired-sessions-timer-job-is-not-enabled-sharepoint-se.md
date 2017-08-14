---
title: The State Service Delete Expired Sessions timer job is not enabled (SharePoint Server 2016)
ms.prod: SHAREPOINT
ms.assetid: 17d06bdf-69e1-4a85-86f9-da78a3c79952
---


# The State Service Delete Expired Sessions timer job is not enabled (SharePoint Server 2016)
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-05-30* **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "The State Service Delete Expired Sessions timer job is not enabled", for SharePoint Server 2016. **Rule Name:**    The State Service Delete Expired Sessions timer job is not enabled. **Summary:**    The State Service uses a timer job to delete data for expired sessions from the State Service databases. If this timer job is not enabled, the server that hosts the State Service database will run out of disk space and the SharePoint farm will cease to function **Cause:**    The State Service Delete Expired Sessions timer job is not enabled. **Resolution:   Enable the timer job by using the SharePoint Central Administration website**
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
    > [!NOTE:]
      
2. Start Central Administration.
    
    For more information about how to interact with Windows Server 2012 R2, see  [Common Management Tasks and Navigation in Windows](http://go.microsoft.com/fwlink/?LinkID=715712&amp;clcid=0x409).
    
  
3. In Central Administration, click **Monitoring**.
    
  
4. On the Monitoring page, in the **Timer Jobs** section, click **Review job definitions**.
    
  
5. On the Job Definitions page, click the State Service Delete Expired Sessions timer job.
    
  
6. On the Edit Timer Job page, specify the schedule that you want, and then click **Enable**.
    
  
 **Resolution:   Enable the timer job by using Microsoft PowerShell**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server 2016 cmdlets.
    
    > [!NOTE:]
      
2. Start the SharePoint 2016 Management Shell.
    
    For Windows Server 2012 R2, on the **Start** screen, click **SharePoint 2016 Management Shell**.
    
  
3. At the PowerShell command prompt, type the following command:
    
  ```
  
Enable-SPTimerJob StateServiceExpiredSessionJobDefinition
  ```

For more information, see Enable-SPTimerJob. PShell_stsadm_deprecated
