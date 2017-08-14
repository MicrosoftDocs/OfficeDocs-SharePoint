---
title: The InfoPath Forms Services Maintenance timer job is not enabled (SharePoint Server 2016)
ms.prod: SHAREPOINT
ms.assetid: 0d326419-25c2-4591-acc6-9e487aa80c6e
---


# The InfoPath Forms Services Maintenance timer job is not enabled (SharePoint Server 2016)
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-05-30* **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "The InfoPath Forms Services Maintenance timer job is not enabled", in SharePoint Server 2016. **Rule Name:**    The InfoPath Forms Services Maintenance timer job is not enabled. **Summary:**    The InfoPath Forms Services Maintenance timer job is not enabled.The InfoPath Forms Services Maintenance timer job is used by InfoPath Forms Services to improve performance by caching form template data on each front-end web server. **Cause:**    The timer job may have been disabled on the Job Definitions page on the SharePoint Central Administration website or the Microsoft PowerShell  **Disable-SPTimerJob** cmdlet was used. **Resolution:   Enable the timer job by using the Central Administration web site**
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators SharePoint group.
    
  
2. Start Central Administration.
    
    For Windows Server 2012 R2, on the **Start** screen, click **SharePoint 2016 Central Administration**.
    
    For more information about how to interact with Windows Server 2012 R2, see  [Common Management Tasks and Navigation in Windows](http://go.microsoft.com/fwlink/?LinkID=715712&amp;clcid=0x409).
    
  
3. On Central Administration, click **Monitoring**.
    
  
4. Click **Review Job definitions**.
    
  
5. Click **InfoPath Forms Services Maintenance**.
    
  
6. Click **Enable**.
    
  
 **Resolution:   Enable the timer job by using PowerShell**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  
  - Add memberships that are required beyond the minimums above.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server 2016 cmdlets.
    
    > [!NOTE:]
      
2. Start the SharePoint 2016 Management Shell.
    
    For UNRESOLVED_TOKEN_VAL(1st_WindowsServ82), on the **Start** screen, click **SharePoint 2016 Management Shell**.
    
  
3. At the PowerShell command prompt, type the following command:
    
  ```
  
Enable-SPTimerJob "<FormsMaintenanceJobDefinition> "
  ```


    Where:
    
  -  *<FormsMaintenanceJobDefintion>*  is the actual name of the timer job to enable.
    
  
For more information, see Enable-SPTimerJob.
