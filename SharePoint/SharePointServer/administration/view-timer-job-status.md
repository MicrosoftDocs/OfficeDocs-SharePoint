---
title: "View timer job status in SharePoint Server 2016"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.date: 3/12/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 1cd060e0-1eb6-424c-8ade-f8d39cd20d1d
description: "Learn to view SharePoint timer job status by using the SharePoint Central Administration website or Windows PowerShell."
---

# View timer job status in SharePoint Server 2016

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
A timer job runs a specific Windows service for SharePoint Server 2016. The timer job contains a definition of the service to run and specifies how frequently the service is started. The SharePoint Timer Service runs timer jobs. Many features in SharePoint Server 2016 rely on timer jobs to run services according to a schedule. You can view the status of timer jobs that have been run by using the Central Administration website or PowerShell.
  
> [!NOTE]
> Because SharePoint Server 2016 runs as websites in Internet Information Services (IIS), administrators and users depend on the accessibility features that browsers provide. SharePoint Server 2016 supports the accessibility features of supported browsers. For more information, see the following resources: > [Plan browser support](https://docs.microsoft.com/sharepoint/install/browser-support-planning-0)> [Accessibility guidelines in SharePoint](https://docs.microsoft.com/sharepoint/accessibility-guidelines)> [Accessibility in SharePoint](https://docs.microsoft.com/sharepoint/dev/general-development/accessibility-in-sharepoint)> [Keyboard shortcuts](https://support.office.com/article/466e33ee-613b-4f47-96bb-1c20f20b1015)> [Touch](https://go.microsoft.com/fwlink/p/?LinkId=246506).
  
## View timer job status by using Central Administration
<a name="section1"> </a>

You can view timer job status by using Central Administration.
  
 **To view timer job status by using Central Administration**
  
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
2. In Central Administration, on the home page, click **Monitoring**.
    
3. On the **Monitoring** page, in the **Timer Jobs** section, click **Check job status**.
    
4. Timer job status is divided into three groups: **Scheduled**, **Running**, and **History**. To page through the timer job status data rows, click the paging arrows at the bottom of these groups.
    
5. To view the timer job status for a specific group, click the title of the group. Or, in the Quick Launch, click **Scheduled Jobs**, **Running Jobs**, or **Job History**.
    
## View timer job status by using Windows PowerShell
<a name="section2"> </a>

You can view timer job status by using PowerShell.
  
 **To view timer job status by using Windows PowerShell**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint 2016 Management Shell.
    
  - On the Start screen, click SharePoint 2016 Management Shell.
    
3. At the PowerShell command prompt, type the following command:
    
  ```
  Get-SPTimerJob -Identity <SPTimerJobPipeBind> | Format-Table DisplayName,Id,LastRunTime,Status
  ```

    Where  _\<SPTimerJobPipeBind\>_ can be a valid GUID, in the form 12345678-90ab-cdef-1234-567890bcdefgh; a valid name of a timer job (for example, TimerJob1); or an instance of a valid SPTimerJob object. 
    
    You can use the value of the **Identity** parameter to specify a timer job. If you do not use the **Identity** parameter, all timer jobs are returned. 
    
    To view the history of a specific timer job, type the following command:
    
  ```
  (Get-SPTimerJob -Identity <SPTimerJobPipeBind>).HistoryEntries | Format-Table -Property Status,StartTime,EndTime,ErrorMessage
  ```

    Where  _\<SPTimerJobPipeBind\>_ can be a valid GUID, in the form 12345678-90ab-cdef-1234-567890bcdefgh; a valid name of a timer job (for example, TimerJob1); or an instance of a valid SPTimerJob object. 
    
For more information, see [Get-SPTimerJob](/powershell/module/sharepoint-server/Get-SPTimerJob?view=sharepoint-ps). 
  
> [!NOTE]
> We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions. 
  
> [!NOTE]
> Please be aware that Get-SPTimerJob commandlet will show you logs in GMT time zone whereas SharePoint Central Administration will show all events in local time.

