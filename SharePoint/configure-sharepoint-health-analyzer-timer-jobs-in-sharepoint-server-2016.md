---
title: Configure SharePoint Health Analyzer timer jobs in SharePoint Server 2016
ms.prod: SHAREPOINT
ms.assetid: 0fb9616f-3877-4ba8-a7a7-9f00b6d896cb
---


# Configure SharePoint Health Analyzer timer jobs in SharePoint Server 2016
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-31* **Summary:** Learn to configure health data collection timer jobs by using the SharePoint Central Administration website or Windows PowerShell.SharePoint Health Analyzer uses timer jobs to collect health data and then writes the data to the logging folder and to the Logging database. This data is used in reports to display health of the farm servers. You can reschedule these timer jobs, run them immediately, or enable or disable them. On that page, you can also configure usage data collection, event selection, and usage data collection settings. For more information, see  [Configure usage and health data collection in SharePoint Server](html/configure-usage-and-health-data-collection-in-sharepoint-server.md).In this article:
-  [Use Central Administration to configure health data timer jobs](#section1)
    
  
-  [Use Windows PowerShell to configure health data timer jobs](#section2)
    
  

## Use Central Administration to configure health data collection timer jobs
<a name="section1"> </a>

You can use Central Administration to configure health data collection timer jobs. **To configure health data collection timer jobs by using Central Administration**
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
    > [!NOTE:]
      
2. In Central Administration, on the home page, click **Monitoring**.
    
  
3. On the **Monitoring** page, in the **Reporting** section, click **Configure usage and health data collection**.
    
  
4. On the **Configure usage and health data collection** page, in the **Health Data Collection** section, click **Enable health data collection**.
    
  
5. In the **Health Data Collection** section, click **Health Logging Schedule**. The **Job Definitions** page opens. It lists all the timer jobs that collect health data.
    
  
6. On the **Job Definitions** page, click the timer job that you want to configure.
    
  
7. On the **Edit Timer Job** page, in the **Recurring Schedule** section, change the timer job schedule, and then click **OK**.
    
  

## Use Windows PowerShell to configure health data collection timer jobs
<a name="section2"> </a>

You can configure the health data collection timer job schedule by using PowerShell. **To configure health data timer jobs by using Windows PowerShell**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  
  - Add memberships that are required beyond the minimums above.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions.
    
    > [!NOTE:]
      
2. On the **Start** menu, click **All Programs**.
    
  
3. Click **SharePoint 2016**.
    
  
4. Click **SharePoint 2016 Management Shell**.
    
  
5. At the PowerShell command prompt, type the following command:
    
  ```
  
Set-SPTimerJob -Identity <SPTimerJobPipeBind>  -Schedule <ScheduleString>
  ```


    The value of the **Identity** parameter specifies the timer job. If you do not use the **Identity** parameter, all timer jobs are configured. To see a list of all the timer jobs, type the following command:
    


  ```
  Get-SPTimerJob | Format-Table -property id,title
  ```


     *<SPTimerJobPipeBind>*  can be a valid GUID, in the form 12345678-90ab-cdef-1234-567890bcdefgh; a valid name of a timer job (for example, TimerJob1); or an instance of a valid **SPTimerJob** object.
    
    Use the value of the **Schedule** parameter to specify the schedule, where *<ScheduleString>*  is one of the following:
    
  - **Every 5 minutes between 0 and 59**
    
  
  - **Hourly between 0 and 59**
    
  
  - **Daily at 15:00:00**
    
  
  - **Weekly between Fri 22:00:00 and Sun 06:00:00**
    
  
  - **Monthly at 15 15:00:00**
    
  
  - **Yearly at Jan 1 15:00:00**
    
  

    
    
    To see examples of timer job schedules, type the following command:
    


  ```
  Get-SPTimerJob | Format-Table -property id,title,schedule
  ```

For more information, see **Get-SPTimerJob** and **Set-SPTimerJob**.
> [!NOTE:]

  
    
    


# See also

#### 

 [Overview of monitoring in SharePoint Server](html/overview-of-monitoring-in-sharepoint-server.md)
  
    
    

  
    
    

