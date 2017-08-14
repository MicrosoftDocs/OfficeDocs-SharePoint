---
title: Configure usage and health data collection in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: 33ed78c8-25fc-48ea-b0c1-50b540213cff
---


# Configure usage and health data collection in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-18* **Summary:** Learn how to configure usage and health data collection in SharePoint Server 2016 and SharePoint Server 2013.SharePoint Server writes usage and health data to the logging folder and to the logging database. You can use the SharePoint Central Administration website to configure health data collection settings.In this article:
-  [Before you begin](#begin)
    
  
-  [Configure usage and health data collection by using Central Administration](#section1)
    
  
-  [Configure usage data collection by using Windows PowerShell](#section2)
    
  
-  [Configure usage data collection for events by using Windows PowerShell](#section3)
    
  
-  [Log usage data in a different logging database by using Windows PowerShell](#section4)
    
  

## Before you begin
<a name="begin"> </a>


> [!NOTE:]
>  [Plan browser support in SharePoint Server 2016](html/plan-browser-support-in-sharepoint-server-2016.md)>  [Accessibility features in SharePoint](https://office.microsoft.com/en-us/sharepoint-foundation-help/accessibility-features-HA010369400.aspx)>  [Keyboard shortcuts](https://office.microsoft.com/en-us/sharepoint-server-help/keyboard-shortcuts-HA010369395.aspx)>  [Touch](https://msdn.microsoft.com/en-us/library/windows/desktop/cc872774.aspx)
  
    
    


## Configure usage and health data collection by using Central Administration
<a name="section1"> </a>

The usage and health data settings are farm-wide and cannot be set for individual servers in the farm. **To configure usage and health data collection by using Central Administration:**
1. Verify that user account performing this procedure is a member of the Farm Administrators group. 
    
    The 
    
  
2. In Central Administration, on the home page, click **Monitoring**.
    
  
3. On the Monitoring page, in the **Reporting** section, click **Configure usage and health data collection**.
    
  
4. On the Configure usage and health data collection page, in the **Usage Data Collection** section, select the **Enable usage data collection** check box.
    
  
5. In the **Event Selection** section, select the check boxes of the events that you want to log.
    
    Logging uses system resources and can affect performance and disk usage. Only log those events for which you want regular reports.
    
    For impromptu reports or investigations, enable logging for events, and then disable logging for the events after the report or investigation is complete. For more information, see  [Configure usage data collection for events by using Windows PowerShell](#section3).
    
  
6. In the **Usage Data Collection Settings** section, type the path of the folder to which you want usage and health information to be written in the **Log file location** box. The path that you specify must exist on each server in the farm.
    
    These settings are applied to all events. 
    
  
7. In the **Health Data Collection** section, select the **Enable health data collection** check box. To change the collection schedules, click **Health Logging Schedule**. You can see a list of timer jobs that collect health data. Click any of the timer jobs to change its schedule, or disable that timer job. If you disable a timer job, it stops collecting corresponding health data. For more information, see [Timer job reference for SharePoint Server 2016](html/timer-job-reference-for-sharepoint-server-2016.md).
    
  
8. To change log collection schedules, click **Log Collection Schedule**, and then click any of the timer jobs to change its schedule, or disable that timer job. If you disable a timer job, it stops collecting corresponding log data.
    
  
9. In the **Logging Database Server** section, to change the authentication method, select either the **Windows authentication** or **SQL authentication** option.
    
    To change the **Database Server** and **Database Name** values, you must use PowerShell. For more information, see [Log usage data in a different Logging Database by using Windows PowerShell](#section4).
    
  

## Configure usage data collection by using Windows PowerShell
<a name="section2"> </a>

 **To configure usage data collection by using Windows PowerShell:**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint 2013 Products cmdlets.
    
    > [!NOTE:]
      
2. On the **Start** menu, click **All Programs**.
    
  
3. Click **SharePoint 2016**.
    
  
4. Click **SharePoint 2016 Management Shell**.
    
  
5. At the PowerShell command prompt, type the following command:
    
  ```
  
Set-SPUsageService [-LoggingEnabled {1 | 0}] [-UsageLogLocation <Path> ] [-Verbose]
  ```


    Where  *<Path>*  is a path that exists on each computer in the farm.
    
    To view the progress of the command, use the **Verbose** parameter.
    
    Enable usage data logging by typing. 
    


  ```
  Set-SPUsageService -LoggingEnabled 1
  ```

For more information, see Set-SPUsageService.
## Configure usage data collection for events by using Windows PowerShell
<a name="section3"> </a>

The event types that are listed on the Configure usage and health data collection page in Central Administration are the same as Usage Definitions in PowerShell. You can use only PowerShell to configure usage definitions individually. Moreover, you can configure only the **DaysRetained** parameter. **To configure usage data logging for events by using Windows PowerShell:**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint 2013 Products cmdlets.
    
    > [!NOTE:]
      
2. On the **Start** menu, click **All Programs**.
    
  
3. Click **SharePoint 2016**.
    
  
4. Click **SharePoint 2016 Management Shell**.
    
  
5. At the PowerShell command prompt, type the following command:
    
  ```
  
Set-SPUsageDefinition -Identity <SPUsageDefinitionPipeBind>  [-Enable] [-DaysRetained <0-31>] [-Verbose]
  ```


    Where  *<SPUsageDefinitionPipeBind>*  specifies the usage definition object that you want to update. The type must be a valid GUID, in the form 12345678-90ab-cdef-1234-567890bcdefgh; a valid name of a usage definition (for example, SiteSubscriptionConfig1); or an instance of a valid **SPUsageDefinition** object. You can use the PowerShell **Get-SPUsageDefinition** cmdlet to obtain this GUID. For more information, see **Get-SPUsageDefinition**.
    
    Use the **Enable** parameter to enable usage logging for this usage definition. Use the **DaysRetained** parameter to specify how long the usage data is retained in the log before it is deleted. The range is 0 to 31 days. To view the progress of the command, use the **Verbose** parameter.
    
  
For more information, see Set-SPUsageDefinition.
## Log usage data in a different logging database by using Windows PowerShell
<a name="section4"> </a>

You can use PowerShell to change this setting. **To log usage data in a different logging database by using Windows PowerShell:**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint 2013 Products cmdlets.
    
    > [!NOTE:]
      
2. On the **Start** menu, click **All Programs**.
    
  
3. Click **SharePoint 2016**.
    
  
4. Click **SharePoint 2016 Management Shell**.
    
  
5. At the PowerShell command prompt type the following command:
    
  ```
  
Set-SPUsageApplication -DatabaseServer <DatabaseServerName>  -DatabaseName <DatabaseName>  [-DatabaseUserName <UserName> ] [-DatabasePassword <Password> ] [-Verbose]
  ```


    Where:
    
  -  *<DatabaseServerName>*  is the name of host server for the logging database. You must specify a value for the **DatabaseServer** parameter, even if the new database is located on the same database server as the old one.
    
  
  -  *<DatabaseName>*  is the name of the logging database.
    
  
  -  *<UserName>*  is the user name to use for connecting to the logging database. Use this parameter only if SQL Server Authentication is used to access the logging database.
    
  
  -  *<Password>*  is the password for the user specified in **DatabaseUserName**. You must specify both *<UserName>*  and *<Password>*  if the database owner is a different user account than the one with which you logged on.
    
  

    To view the progress of the command, use the **Verbose** parameter.
    
  
For more information, see Set-SPUsageApplication.
# See also

#### 

 [Overview of monitoring in SharePoint Server](html/overview-of-monitoring-in-sharepoint-server.md)
  
    
    

  
    
    

