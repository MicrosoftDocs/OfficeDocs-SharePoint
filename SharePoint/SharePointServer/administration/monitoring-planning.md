---
title: "Plan for monitoring in SharePoint Server"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.date: 8/25/2017
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: a0c9aaa9-5b6d-449c-a69b-f058ac4cf9f1

description: "Learn about SharePoint Server monitoring tools and scenarios. Plan schedules and create a response plan to keep the SharePoint farm running."
---

# Plan for monitoring in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
To make sure that SharePoint Server is running smoothly, IT professionals must monitor farms, servers, applications, services, and performance closely. You should do preventive maintenance regularly to prevent problems from happening, and create a plan that will minimize damage when a problem occurs.
  
Microsoft provides many tools that help you monitor the overall health status of the SharePoint Server environment. If anything goes wrong, you can find plenty of resources and use the monitoring tools to analyze logs, identify the cause, and then take correct actions to solve the problems.
  
You also need to plan how many people you want to monitor the SharePoint Server environment. Then create a response plan to cover actions that you should take when a problem occurs.
  
    
## Overview of monitoring tools
<a name="section1"> </a>

There are many tools that you can use to monitor SharePoint Server and troubleshoot problems. Each tool covers different parts of the SharePoint environment, and some tools may overlap areas. Consider which tools can maximize your monitoring actions. The following monitoring tools are available:
  
- SharePoint Health Analyzer
    
    On the Central Administration home page, click **Monitoring**, **Health Analyzer**. You can use this built-in feature to analyze and resolve problems in the following areas: security, performance, configuration, and availability. Health Analyzer rules are predefined and run at scheduled intervals, such as hourly, daily, weekly, and monthly. If an error is detected, the corresponding rule is triggered. Each rule has a brief explanation about why the error occurs and provides you with a link to a detailed article that contains step-by-step help to resolve the problem. When you follow the help process, you can re-run the rule to verify resolution. If the error does not appear in the list, the problem is resolved.
    
- Timer Jobs
    
    On the Central Administration home page, click **Monitoring**, **Timer Jobs**. SharePoint Server uses configurable timer jobs to collect health data and then writes the data to the logging folder and to the Logging database. The data is then used in reports to display the health status of the farm servers. 
    
    You can reschedule a timer job, enable or disable it, and run it on demand. Daily, weekly, and monthly schedules also include a window of execution. The timer service will select a random time within this interval to start running the timer job on each applicable server. This feature is appropriate for high-load jobs that run on multiple servers on the farm.
    
    > [!NOTE]
    > Running timer jobs at the same time on all servers on the farm can affect system performance. You should plan timer jobs carefully to avoid overlap with other timer jobs. 
  
- Reporting
    
    On the Central Administration home page, click **Monitoring**, **Reporting**. This feature lets you configure diagnostic logging and data collection, and view administrative and health reports. Because some configurations will use up drive space and adversely affect system performance you must carefully plan what configurations to set.
    
- Microsoft PowerShell
    
    PowerShell is a powerful tool for monitoring SharePoint Server. You can run commands to obtain the exact logs that you want to view. For more information, see [View diagnostic logs in SharePoint Server](view-diagnostic-logs.md).
    
- System Center - Operations Manager with System Center Management Pack for SharePoint Server
    
    System Center - Operations Manager is a powerful monitoring platform that lets you monitor services, devices, and operations for many computers in a single console. By using Operations Manager, you can view status, health, performance information, and alerts generated for availability, performance, configuration and security situations. For more information, see [Operations Manager](https://go.microsoft.com/fwlink/p/?LinkID=226376).
    
    To use Operations Manager to monitor SharePoint Server, you must install System Center Management Pack for SharePoint Server. You can use this tool to monitor events, collect SharePoint component-specific performance counters in one central location, and raise alerts for operator intervention as necessary. Download and install [System Center Management Pack for SharePoint Server 2016](https://www.microsoft.com/download/details.aspx?id=52043).
    
- Event Viewer
    
    Event Viewer is a Microsoft Management Console (MMC) snap-in. It lets you browse and manage event logs. It is a very handy tool for troubleshooting problems. You can filter for specific events across multiple logs, and reuse useful event filters as custom views. For more information, see [Event Viewer](https://go.microsoft.com/fwlink/?LinkId=253618).
    
- SharePoint Developer Dashboard
    
    This tool provides diagnostic information that can help a developer or system administrator analyze performance of SharePoint Web pages. This utility can help if a page is loading slowly, a Web Part is not performing, or if a database query on the page is not performing. The SharePoint Developer Dashboard is disabled by default. You can enable it by using PowerShell. For more information, see [SharePoint Developer Dashboard](https://go.microsoft.com/fwlink/p/?LinkID=199580).
    
- Windows Management Instrumentation (WMI)
    
    WMI provides many classes for you to monitor the SharePoint Server environment. For each manageable resource, there is a corresponding WMI class. For more information, see [Windows Management Instrumentation (WMI) Overview](/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn265977(v=ws.11)).
    
- SQL Server Reporting Services (SSRS)
    
    SQL Server Reporting Services provides a full range of ready-to-use tools and services to help you create, deploy, and manage reports for your organization. It also has programming features that let you extend and customize reporting functionality. By using SQL Server Reporting Services, you can create interactive, tabular, graphical, or free-form reports from relational, multidimensional, or XML-based data sources. You can publish reports, schedule report processing, or access reports on-demand. You can use SQL Server Reporting Services to create reports based on predefined models, and to interactively explore data within the model. You can select from a variety of viewing formats, export reports to other applications, and subscribe to published reports. The reports that you create can be viewed over a Web-based connection or as part of a Windows application or SharePoint site. For more information, see [Reporting Services (SSRS)](/sql/reporting-services/create-deploy-and-manage-mobile-and-paginated-reports?view=sql-server-2014).
    
SharePoint Health Analyzer, Timer Jobs, Reporting, and PowerShell are built-in features, whereas System Center, System Center Management Pack for SharePoint Server 2016, and SQL Server Reporting Services are independent tools. SharePoint Developer Dashboard and WMI are built-in tools and intended for developers or system administrators. These tools are complementary and apply to different scenarios. 
  
The following table shows a summary of these tools. You must balance the pros and cons of the monitoring tools when you determine which tools to use under certain scenarios.
  
**Summary of monitoring tools**

|**Tool**|**Optional or built-in**|**Skill level required**|**Pros**|**Cons**|**Resources**|
|:-----|:-----|:-----|:-----|:-----|:-----|
|SharePoint Health Analyzer  <br/> |Built-in  <br/> |Basic  <br/> | Gives step-by-step instructions for resolving a problem.  <br/>  Customizable. You can disable some rules if you don't need them.  <br/> | Does not cover all possible problems.  <br/>  A rule is triggered only after a problem has already happened.  <br/> |[Configure SharePoint Health Analyzer rules in SharePoint Server](configure-sharepoint-health-analyzer-rules.md) <br/> [View and resolve SharePoint Health Analyzer alerts in SharePoint Server](/previous-versions/office/sharepoint-server-2010/ee663488(v=office.14)) <br/> [SharePoint Health Analyzer rules reference for SharePoint Server 2016](../technical-reference/sharepoint-health-analyzer-rules-reference.md) <br/> |
|Timer jobs  <br/> |Built-in  <br/> |Advanced: You have to consider the implications of enabling or disabling a timer job and changing schedules.  <br/> | Wide range of monitoring items.  <br/>  Easy to reschedule.  <br/>  Customizable. You can create new timer jobs to meet your specific requirements.  <br/> |Can affect system performance and conflict with one another.  <br/> |[Configure SharePoint Health Analyzer timer jobs in SharePoint Server 2016](configure-sharepoint-health-analyzer-timer-jobs.md) <br/> [Timer job reference for SharePoint Server](../technical-reference/timer-job-reference-for-sharepoint-server.md) <br/> |
|Reporting  <br/> |Built-in  <br/> |Viewing skill level: Basic  <br/> |Flexible. Lets you configure the severity of events to log, enable event log flood protection, and configure trace logs.  <br/> | Only shows administrative and health statistics, without any suggested solutions.  <br/>  You have to interpret the logging data.  <br/>  Can affect performance and disk usage.  <br/> |[View reports and logs in SharePoint Server 2016](view-reports-and-logs.md) <br/> |
|PowerShell  <br/> |Built-in  <br/> |Advanced: you have to know what to look for, and you have to run PowerShell commands.  <br/> |Filters data, displays it in various ways, and outputs data to a grid with which you can filter, sort, group, and export the data to Excel 2016.  <br/> |You have to know which PowerShell commands to run.  <br/> |[View diagnostic logs in SharePoint Server](view-diagnostic-logs.md) <br/> [Scripting with Windows PowerShell](/powershell/scripting/components/console/powershell.exe-command-line-help?view=powershell-6) <br/> |
|System Center           with System Center Management Pack for SharePoint Server  <br/> |Optional but recommended  <br/> |Advanced: you need to know what to look for and how to interpret data.  <br/> |The tool can detect, diagnose, and alert you about software and hardware incidents, and refer you to knowledge articles. It helps you to do more monitoring with fewer people by monitoring many key scenarios.  <br/> |Requires additional servers to deploy.  <br/> |[System Center Management Pack for SharePoint Server 2016](https://www.microsoft.com/download/details.aspx?id=52043) <br/> |
|Event Viewer  <br/> |Built-in  <br/> |Basic  <br/> |You can view events from multiple event logs, save useful event filters as custom views that can be reused, schedule a task to run in response to an event, and create and manage event subscriptions.  <br/> |Does not suggest resolutions.  <br/> |[Event Viewer](https://go.microsoft.com/fwlink/?LinkId=253618) <br/> |
|SharePoint Developer Dashboard  <br/> |Built-in  <br/> |Advanced: you have to know what to look for and how to interpret data.  <br/> |Easy to analyze performance of SharePoint pages.  <br/> |Limited to monitoring performance of SharePoint pages.  <br/> |[SharePoint Developer Dashboard](https://go.microsoft.com/fwlink/p/?LinkID=199580) <br/> |
|Windows Management Instrumentation (WMI)  <br/> |Built-in  <br/> |Advanced: you have to know what to look for and how to write WMI scripts for the managed objects.  <br/> |Can monitor, track, and control system events that are related to software applications, hardware components, and networks.  <br/> | You have to identify which managed objects to monitor.  <br/>  You have to write WMI scripts.  <br/> |[Windows Management Instrumentation (WMI) Overview](/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn265977(v=ws.11)) <br/> |
|SQL Server Reporting Services  <br/> |Optional but recommended.  <br/> |Advanced: you have to design and manage reports.  <br/> |Comprehensive platform to create and manage reports.  <br/> |Advanced skills required to create and develop solutions.           You have to know PerformancePoint Dashboard Designer and Visual Studio.  <br/> |[Reporting Services (SSRS)](/sql/reporting-services/create-deploy-and-manage-mobile-and-paginated-reports?view=sql-server-2014) <br/> |
   
For a SharePoint farm with no more than 10 servers, we recommend that you at least install the following independent tools:
  
- System Center 2012 - Operations Manager with System Center Management Pack for SharePoint Server 2013
    
    Monitors the health status of SharePoint products.
    
- SQL Server Reporting Services
    
    Deploy it if you use the Reporting Services to view Report Definition Language (RDL) files, and design reports by Visual Studio and PerformancePoint Dashboard Designer.
    
## Identify monitoring scenarios
<a name="section2"> </a>

Identify the scenarios that you want to monitor —for example, health, workflows, search, SQL Server, virtual environments, and performance. The following table shows some key scenarios and the monitoring tools that you can use to monitor those scenarios. 
  
**Scenarios and monitoring tools**

|**Tool\Scenario**|**Health**|**Search**|**Databases**|**Performance**|**Workflows**|**Virtual environments**|**Business Data Connectivity**|**Business Intelligence**|**Access Services**|**Farms**|**Servers**|**Service applications**|**Web applications**|
|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|
|SharePoint Health Analyzer  <br/> |√  <br/> |√  <br/> |√  <br/> |√  <br/> |X  <br/> |X  <br/> |√  <br/> |√  <br/> |√  <br/> |√  <br/> |√  <br/> |√  <br/> |X  <br/> |
|Timer jobs  <br/> |√  <br/> |√  <br/> |√  <br/> |√  <br/> |√  <br/> |X  <br/> |X  <br/> |√  <br/> |X  <br/> |X  <br/> |X  <br/> |√  <br/> |√  <br/> |
|Reporting  <br/> |√  <br/> |√  <br/> |√  <br/> |√  <br/> |√  <br/> |X  <br/> |√  <br/> |√  <br/> |√  <br/> |√  <br/> |√  <br/> |√  <br/> |X  <br/> |
|PowerShell  <br/> |√  <br/> |√  <br/> |√  <br/> |√  <br/> |√  <br/> |X  <br/> |√  <br/> |√  <br/> |√  <br/> |√  <br/> |√  <br/> |√  <br/> |√  <br/> |
|System Center           with System Center Management Pack for SharePoint Server  <br/> |√  <br/> |√  <br/> |√  <br/> |√  <br/> |X  <br/> |√  <br/> |√  <br/> |√  <br/> |√  <br/> |√  <br/> |√  <br/> |√  <br/> |X  <br/> |
|Event Viewer  <br/> |√  <br/> |√  <br/> |√  <br/> |√  <br/> |√  <br/> |X  <br/> |√  <br/> |√  <br/> |√  <br/> |√  <br/> |√  <br/> |√  <br/> |√  <br/> |
|SharePoint Developer Dashboard  <br/> |X  <br/> |X  <br/> |X  <br/> |√\*  <br/> |X  <br/> |X  <br/> |X  <br/> |X  <br/> |X  <br/> |X  <br/> |X  <br/> |X  <br/> |X  <br/> |
|Windows Management Instrumentation (WMI)  <br/> |√  <br/> |√  <br/> |√  <br/> |√  <br/> |X  <br/> |√\*\*  <br/> |X  <br/> |√  <br/> |X  <br/> |X  <br/> |√  <br/> |X  <br/> |X  <br/> |
|SQL Server Reporting Services  <br/> |√  <br/> |√  <br/> |√  <br/> |√  <br/> |√  <br/> |X  <br/> |√  <br/> |√  <br/> |√  <br/> |√  <br/> |√  <br/> |√  <br/> |√  <br/> |
   
 **Note:**
  
\*: SharePoint Developer Dashboard only monitors performance of web pages.
  
\*\*: The WMI interfaces can manage the Hyper-V services.
  
## Determine daily, weekly, and monthly monitoring items
<a name="section3"> </a>

You can decide which items to monitor daily, weekly and monthly based on the "Daily Tasks" section (on page 45), the "Weekly Tasks" section (on page 53), the "Monthly Tasks" section (on page 54), and the "Impromptu Tasks" section (on page 54) in the [SharePoint Server 2013: Operations Framework and Checklists](https://www.microsoft.com/download/details.aspx?id=42531)white paper.
  
> [!NOTE]
> While this white paper addresses SharePoint 2013, you can still use this information to help plan monitoring schedules for SharePoint Server.
  
## Plan monitoring personnel
<a name="section4"> </a>

You have to estimate how many people you will require to monitor the SharePoint Server environment. Depending on the size of the SharePoint environment, you might assign dedicated people to monitor the SharePoint environment. For very large enterprise farms, you might require that one or two people are dedicated to each farm.
  
When planning for monitoring personnel, consider the following:
  
- Small farm (Small user base, or line of business (LOB) applications)
    
- Medium farm (Enterprise, Service Applications, etc.)
    
- Large enterprise farm (Large Enterprise, Many Service Applications, Self-Provisioning, etc.)
    
- High availability requirements (Service level agreements, SLAs)
    
- High performance requirements (Page render times)
    
- User base size (how many unique users)
    
- Concurrent users (how many users actively hitting the portal at once)
    
- Requests per second (also during peak hours)
    
- Operational maturity
    
- Management tools
    
The following table shows approximately how many people of different skill levels are required to monitor the SharePoint environment depending on the number of servers. Note that this table only provides a very rough estimate. 
  
**Monitoring personnel required**

|**Number of servers**|**Personnel required**|**Skill level required**|
|:-----|:-----|:-----|
|1~4  <br/> |1  <br/> |Basic  <br/> |
|4~10  <br/> |1~2  <br/> |Advanced  <br/> |
|10~40  <br/> |3~4  <br/> |Basic and Advanced  <br/> |
|40~100  <br/> |5+  <br/> |Basic and Advanced  <br/> |
|100+  <br/> |10+  <br/> |Basic and Advanced  <br/> |
   
## Create a response plan
<a name="section5"> </a>

We recommend that you create a response plan to help prepare for potential problems and to specify what actions to take when a problem does occur.
  
The response plan should exclude SharePoint Health Analyzer rules that provide workable solutions already. For a problem that has no immediate solutions, you must investigate the logs by using monitoring tools such as the Event Viewer to find a solution.
  
The following table shows some factors that you should consider when you develop a response plan.
  
**Suggested items in a response plan**

|**Item**|**Description**|
|:-----|:-----|
|Alert/Event/Problem  <br/> |The verbatim message, the verbatim event, or description of the problem.  <br/> |
|Affected services/applications  <br/> |Services or applications that will be affected by the problem.  <br/> |
|Symptom  <br/> |Symptom of the problem.  <br/> |
|Severity  <br/> |Severity of the problem. Problems with high severity must have high priority.  <br/> |
|Problem must be resolved in (minutes or hours)  <br/> |Acceptable lapse time of service.  <br/> |
|Possible causes  <br/> |Possible causes of the problem.  <br/> |
|Resolutions  <br/> |Resolutions of the problem.  <br/> |
|Contacts  <br/> |People who should be contacted when this problem occurs.  <br/> |
|Escalation  <br/> |People or teams that should be contacted if the resolutions did not successfully resolve the problem.  <br/> |
|Related resources  <br/> |Any resources that may help resolve the problem, such as articles on docs.microsoft.com for SharePoint Server.  <br/> |
|Note  <br/> |Any issues that you want to highlight.  <br/> |
   
## See also
<a name="section5"> </a>

#### Concepts

[Overview of monitoring in SharePoint Server](monitoring-overview.md)
  
[Monitor apps for SharePoint for SharePoint Server](monitor-apps-for-sharepoint.md)
  
[Storage and SQL Server capacity planning and configuration (SharePoint Server)](storage-and-sql-server-capacity-planning-and-configuration.md)
  
[Monitor cache performance in SharePoint Server 2016](monitor-cache-performance.md)
#### Other Resources

[Microsoft Network Monitor](https://www.microsoft.com/download/details.aspx?id=4865)
