---
title: "Timer job reference for SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
audience: ITPro
ms.topic: reference
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
description: "Learn about the timer jobs in SharePoint Server."
---

# Timer job reference for SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]

This article describes the default timer jobs for SharePoint Server 2019, SharePoint Server 2016, and SharePoint 2013. A timer job runs in a specific Windows service for SharePoint Server 2019. Timer jobs perform infrastructure tasks for the Timer service, such as clearing the timer job history and recycling the Timer service. Timer jobs also perform tasks for web applications, such as sending email alerts. A timer job contains a definition of the service to run and specifies how frequently the service is started. The SharePoint Timer service (SPTimerv4) runs timer jobs. Many features in SharePoint Server rely on timer jobs to run services according to a schedule.

> [!NOTE]
> Classic timer jobs are not available in SharePoint Online. The timer jobs in this article are only available on SharePoint Server 2019, SharePoint Server 2016, and SharePoint 2013.

## Manage timer jobs
<a name="ManageJobs"> </a>

The SharePoint Central Administration website has a **Timer Job Status** page on which you can check the status of a timer job and a **Job Definitions** page on which you can edit the timer job definition. You can find links to these pages in Central Administration, on the **Monitoring** page, in the **Timer Jobs** section. You can click **Review job definitions** to see a list of all timer jobs, or click **Check job status** to see scheduled and running timer jobs.

On the **Timer Job Status** page, on the **View** menu, you can filter the timer jobs at the following levels: 
  
- **All** Displays all timer jobs for the farm. 
    
- **Service** Displays all the timer jobs for a particular service. If you select this option, use the **Service** menu to select the service by which you want to filter the listed jobs. 
    
- **Web Application** Displays all the timer jobs for a web application. If you select this option, use the **Web Application** menu to select the web application by which you want to filter the listed jobs. 
    
- **Server** Displays all the timer jobs for the specified server. If you select this option, use the **Server** menu to select the server by which you want to filter the listed jobs. 
    
- **Job Definition** Displays all the timer jobs for the specified job definition. On the **Timer Job Status** page, open the **Job Definition** menu, and then click **Change Job Definition** to get a list of job definitions. 
    
- **Failed Jobs** Displays all the timer jobs on the farm that failed to finish.
 
The SharePoint Timer service (SPTimerv4) is based on the Gregorian calendar for scheduling. For every job that you schedule, you specify when the timer job will run, specified in a 24-hour time format. You must specify the time in local time instead of as an offset from Coordinated Universal Time (UTC). The time is stored in that format. By default, daily, weekly, and monthly schedules also include a window of execution. The timer service selects a random time within the window of execution interval to start the job on each applicable server. This capability helps to reduce the overall load of resource-intensive timer jobs that run on multiple servers on the farm. You can specify timer job schedules on the **Edit Timer Job** page or by using Microsoft PowerShell. For more information, see [Get-SPTimerJob](/powershell/module/sharepoint-server/get-sptimerjob?view=sharepoint-ps) and [Set-SPTimerJob](/powershell/module/sharepoint-server/set-sptimerjob?view=sharepoint-ps).

## Default timer jobs
<a name="DefaultJobs"> </a>

The following articles list the default timer jobs for SharePoint Server 2019, SharePoint Server 2016, and SharePoint 2013.

- [Default timer jobs in SharePoint Server 2019](/Sharepoint/technical-reference/default-timer-jobs-in-sharepoint-server-2019)

- [Default timer jobs in SharePoint Server 2016](/SharePoint/technical-reference/default-timer-jobs-in-sharepoint-server-2016)

- [Default timer jobs in SharePoint 2013](/SharePoint/technical-reference/default-timer-jobs-in-sharepoint-2013)
