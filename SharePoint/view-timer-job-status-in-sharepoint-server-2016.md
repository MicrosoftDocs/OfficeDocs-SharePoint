---
title: View timer job status in SharePoint Server 2016
ms.prod: SHAREPOINT
ms.assetid: 1cd060e0-1eb6-424c-8ade-f8d39cd20d1d
---


# View timer job status in SharePoint Server 2016
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-05-30* **Summary:** Learn to view SharePoint timer job status by using the SharePoint Central Administration website or Windows PowerShell.A timer job runs a specific Windows service for SharePoint Server 2016. The timer job contains a definition of the service to run and specifies how frequently the service is started. The SharePoint Timer Service runs timer jobs. Many features in SharePoint Server 2016 rely on timer jobs to run services according to a schedule. You can view the status of timer jobs that have been run by using the Central Administration website or PowerShell.
> [!NOTE:]
>  [Plan browser support](https://go.microsoft.com/fwlink/p/?LinkId=246502)>  [Accessibility features in SharePoint Products](https://go.microsoft.com/fwlink/p/?LinkId=246501)>  [Keyboard shortcuts](https://go.microsoft.com/fwlink/p/?LinkID=246504)>  [Touch](https://go.microsoft.com/fwlink/p/?LinkId=246506)
  
    
    


## In this article:
<a name="begin"> </a>


-  [View timer job status by using Central Administration](#section1)
    
  
-  [View timer job status by using Windows PowerShell](#section2)
    
  

## View timer job status by using Central Administration
<a name="section1"> </a>

You can view timer job status by using Central Administration. **To view timer job status by using Central Administration**
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
  
2. In Central Administration, on the home page, click **Monitoring**.
    
  
3. On the **Monitoring** page, in the **Timer Jobs** section, click **Check job status**.
    
  
4. Timer job status is divided into three groups: **Scheduled**, **Running**, and **History**. To page through the timer job status data rows, click the paging arrows at the bottom of these groups.
    
  
5. To view the timer job status for a specific group, click the title of the group. Or, in the Quick Launch, click **Scheduled Jobs**, **Running Jobs**, or **Job History**.
    
  

## View timer job status by using Windows PowerShell
<a name="section2"> </a>

You can view timer job status by using PowerShell. **To view timer job status by using Windows PowerShell**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions.
    
    > [!NOTE:]
      
2. Start the SharePoint 2016 Management Shell.
    
  - On the Start screen, click SharePoint 2016 Management Shell.
    
  
3. At the PowerShell command prompt, type the following command:
    
  ```
  
Get-SPTimerJob -Identity <SPTimerJobPipeBind>  | Format-Table DisplayName,Id,LastRunTime,Status
  ```


    Where  *<SPTimerJobPipeBind>*  can be a valid GUID, in the form 12345678-90ab-cdef-1234-567890bcdefgh; a valid name of a timer job (for example, TimerJob1); or an instance of a valid SPTimerJob object.
    
    You can use the value of the **Identity** parameter to specify a timer job. If you do not use the **Identity** parameter, all timer jobs are returned.
    
    To view the history of a specific timer job, type the following command:
    


  ```
  (Get-SPTimerJob -Identity <SPTimerJobPipeBind> ).HistoryEntries | Format-Table -Property Status,StartTime,EndTime,ErrorMessage
  ```


    Where  *<SPTimerJobPipeBind>*  can be a valid GUID, in the form 12345678-90ab-cdef-1234-567890bcdefgh; a valid name of a timer job (for example, TimerJob1); or an instance of a valid SPTimerJob object.
    
  
For more information, see **Get-SPTimerJob**.
> [!NOTE:]

  
    
    


