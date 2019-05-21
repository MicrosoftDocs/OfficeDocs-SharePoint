---
title: "Overview of monitoring in SharePoint Server"
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.date: 3/12/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 6483e4c3-dc7e-49fd-92a7-15e1bb63d432
description: "Learn about configuring monitoring, viewing SharePoint reports and logs, and using SharePoint Health Analyzer rules."
---

# Overview of monitoring in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
The primary goal of monitoring is to ensure a healthy SharePoint Server 2016 environment so that you can achieve service performance objectives such as short response time. You can use the monitoring features from the SharePoint Central Administration website, System Center Management Pack for SharePoint Server 2013, and Microsoft PowerShell scripts to monitor the SharePoint Server 2016 environment and services.
  
Logs and reports track SharePoint Server 2016 environment and service status. You can read the logs from the logging database. The advantage of using logging database is that you can configure your view and export the logs to Excel. The logs and reports from Central Administration help you understand how the SharePoint Server 2016 system is running, analyze and repair problems, and view metrics for the sites. In addition, System Center Management Pack for SharePoint Server 2013 provides an end-to-end monitoring and reporting system that you can use to monitor SharePoint Server 2016. 
  
Monitoring the SharePoint Server 2016 environment includes the following tasks:
  
- Configuring the various aspects of monitoring to suit business needs.
    
- Viewing reports and logs to monitor the SharePoint Server 2016 environment.
    
- Monitoring and resolving problems by using SharePoint Health Analyzer
    
## Configuring monitoring in a SharePoint environment
<a name="section1"> </a>

SharePoint Server 2016 comes installed with default settings for its monitoring features. However, you might want to change some of these settings to better suit business needs. These settings include diagnostic logging and usage and health data collection. **Diagnostic logging** collects data about the SharePoint Server 2016 farm environment. **Usage and health data** is collected for SharePoint Server 2016 services. 
  
### Diagnostic logging

SharePoint Server 2016 collects data in the diagnostic log that you can use to troubleshoot the SharePoint Server 2016 farm environment. The default settings are sufficient for most situations, but depending upon the business needs and lifecycle of the farm, you might want to change these settings. For example, if you are deploying a new feature or making large-scale changes to the environment, you might want to change the logging level to either a more verbose level, to capture as much data about the state of the system during the changes, or to a lower level to reduce the size of the log and the resources that are required to log the data. For more information and best practices, see [Configure diagnostic logging in SharePoint Server](configure-diagnostic-logging.md).
  
### Usage and health data collection and timer job

Usage and health data is collected to show how SharePoint Server 2016 is used. The system writes usage and health data to the logging folder and the logging database. The usage and health data might consist of performance counter data, event log data, timer service data, metrics for site collections and sites, search usage data, or various performance aspects of the Web servers. The system uses this data to create health reports, and administrative reports.
  
Many features in SharePoint Server 2016 rely on timer jobs to run services according to a schedule. SharePoint Server 2016 uses specific timer jobs to regularly monitor tasks and collect monitoring data. A timer job specifies the service to run and how frequently the service should be started. The SharePoint Timer Service (SPTimerV4) runs timer jobs. 
  
You might want timer jobs to run more frequently or less frequently. You might even want to disable jobs that collect data that you are not interested in. You can perform the following tasks on timer jobs:
  
- Modify the schedule that the timer job runs on.
    
- Run timer jobs immediately.
    
- Enable or disable timer jobs.
    
- View timer job status. You can view currently scheduled jobs, failed jobs, currently running jobs, and a complete timer job history.
    
For more information, see [Configure SharePoint Health Analyzer timer jobs in SharePoint Server 2016](configure-sharepoint-health-analyzer-timer-jobs.md).
  
## Viewing SharePoint reports and logs
<a name="section2"> </a>

SharePoint Server 2016 can be configured to collect data and create reports about server status, site use and search. See the following resources: 
  
- [View health reports in SharePoint Server](view-health-reports.md) . Health reports include slowest pages and top active pages. 
    
- [Usage reports](../search/view-search-diagnostics.md#Proc4). 
    
You can view logs by using Microsoft PowerShell or read the logs directly from the logging database. You can monitor cache performance and search. And you can also view the timer job status.
  
The following resources give more information about reports and logs:
  
- To learn how to get detailed information about any problems that arise, see [View diagnostic logs in SharePoint Server](view-diagnostic-logs.md). 
    
- To ensure that the farm cache settings are correct and that the caching is running at maximum performance, see [Monitor cache performance in SharePoint Server 2016](monitor-cache-performance.md).
    
- To review and update the timer jobs, see [View timer job status in SharePoint Server 2016](view-timer-job-status.md).
    
## Monitoring and resolving problems by using SharePoint Health Analyzer
<a name="section3"> </a>

SharePoint Server 2016 includes an integrated health analysis tool that is named SharePoint Health Analyzer that you can use to check for potential configuration, performance, and usage problems. SharePoint Health Analyzer runs predefined health rules against servers in the farm. A health rule runs a test and returns a status that tells you the outcome of the test. When any rule fails, SharePoint Health Analyzer creates an alert on the Review problems and solutions page and writes status to the Windows Event log. You can click an alert to view more information about the problem and see steps to resolve the problem. You can also open the rule that raised the alert and change its settings.
  
You can also edit Health Analyzer Reports list items, create custom views, export the list items into Excel, subscribe to the RSS feed for the list, and perform many other tasks. Each health rule falls in one of the following categories: Security, Performance, Configuration, or Availability.
  
All health rules are available through Central Administration, on the Monitoring page. Farm administrators can configure specific health rules to do the following:
  
- Enable or disable rules.
    
- Configure rules to run on a predefined schedule.
    
- Define the scope where the rules run.
    
- Receive e-mail alerts when problems are found.
    
- Run rules on a defined schedule or on an impromptu basis.
    
For more information about configuring these settings, see [Configure SharePoint Health Analyzer rules in SharePoint Server](configure-sharepoint-health-analyzer-rules.md).
  
For more information about the health rules and how to troubleshoot problems in SharePoint Server 2016, see [SharePoint Health Analyzer rules reference for SharePoint Server 2016](../technical-reference/sharepoint-health-analyzer-rules-reference.md).
  

