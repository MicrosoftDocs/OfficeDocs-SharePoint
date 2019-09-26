---
title: "Profile schema reference in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 3/5/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 05bdd5cb-2c97-40ca-bbac-bb91d300ad5c
description: "Understand the XML schema for profiles for use in scripted monitoring configuration for SharePoint Server."
---

# Profile schema reference in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
When you run the BackupMonitoringSettings.ps1 Microsoft PowerShell script on a SharePoint farm, you create a file that's called a Profile. The Profile follows an XML schema. You can modify settings of elements of the schema to create a custom Profile. You can then use the custom Profile to automate configuration of the monitoring settings in a SharePoint environment. For an introduction to scripted monitoring configuration, see [Overview of scripted monitoring configuration in SharePoint Server](overview-of-scripted-monitoring-configuration.md).
  
Administrators can run the scripts before, during, and after changes to the farm, such as farm topology, major security changes, applying software updates, or running a performance test. The scripts alter the monitoring settings so that all of the necessary monitoring data are collected during the event without flooding the Logging database during normal operation.
  
> [!NOTE]
> You must download the PowerShell scripts to back up, restore, or modify the farm monitoring settings. The scripts are available on the TechNet Gallery at [Scripted Monitoring Configuration - BackupMonitoringSettings](https://go.microsoft.com/fwlink/p/?LinkID=299269) and [Scripted Monitoring Configuration - AlterMonitoringSettings](https://go.microsoft.com/fwlink/p/?LinkID=299270). The **BackupMonitoringSettings.ps1** PowerShell script creates the backup Profile from which you can create other Profiles. 
  
You can create one or more Profiles to adjust the level of monitoring during different phases of the SharePoint lifecycle. You can also use a custom Profile to configure monitoring on several farms at once.
  
You would typically create Profiles for the following purposes:
  
- To complete the configuration of the monitoring settings on a farm after you install SharePoint Server
    
- To change the monitoring settings on a farm just before an administrative change, such as changing the settings of a Search service application on the farm
    
    As a result, you can capture more monitoring data related to that change and suppress unwanted monitoring data. Then you can return the monitoring settings to the original values after the change has been completed.
    
- To restore the monitoring settings on a farm after some administrative change
    
- To restore a previous set of monitoring settings on a farm
    
    You might do this if you are making manual adjustments to the settings and decide that you want to restore the previous settings.
    
- To restore the default settings
    
- To create a profile that you can apply to multiple farms
    
## Backing up the original settings

You should always back up the default monitoring settings before altering them. That way, you can restore those settings should you need to. The backup Profile also can serve as the beginning point for the other Profiles you will create. For more information about how to back up the settings, see [Run scripted monitoring configuration in SharePoint Server](run-scripted-monitoring-configuration.md).
  
## Understanding the Profile schema

When you run the **BackupMonitoringSettings.ps1** PowerShell script, you create a Profile that conforms to the following XML schema. The elements of the file contain the associated monitoring settings from the farm. 
  
```
<?xml version="1.0" standalone="yes"?>
<Configuration>
  <FarmDiagnosticConfig />
  <UsageServices>
    <UsageService />  
  </UsageServices>
  <UsageDefinitions>
    <UsageDefinition />
  </UsageDefinitions>
  <LogLevels>
    <LogLevel />
  </LogLevels>
  <TimerJobs>
    <TimerJob />
  </TimerJobs>
  <HealthAnalyzerRules>
    <HealthAnalyzerRule />
  </HealthAnalyzerRules>
</Configuration>
```

> [!IMPORTANT]
> In the following tables, you cannot change values in fields that are marked as Read-Only. If you change values in Read-Only fields in your Profiles, unpredictable results may occur. 
  
**Settings for the FarmDiagnosticConfig element**

|**Name**|**Value Type**|**Notes**|
|:-----|:-----|:-----|
|AllowLegacyTraceProviders  <br/> |Boolean  <br/> |Specifies that trace providers built for previous versions of SharePoint Products and Technologies can write to the trace session for SharePoint Server.  <br/> |
|AppAnalyticsAutomaticUploadEnabled  <br/> |Boolean  <br/> |Specifies whether aggregated app usage data is automatically uploaded to Microsoft.  <br/> |
|CustomerExperienceImprovementProgramEnabled  <br/> |Boolean  <br/> |Determines whether a Management Group has enabled the Customer Experience Improvement Program feature.  <br/> |
|ErrorReportingEnabled  <br/> |Boolean  <br/> |Gets or sets a value to indicate whether crash data collection and error reporting is enabled.  <br/> |
|ErrorReportingAutomaticUploadEnabled  <br/> |Boolean  <br/> |Specifies whether participation in the Customer Experience Improvement Program (CEIP) is enabled. The CEIP is designed to improve the quality, reliability, and performance of Microsoft products and technologies. With your permission, anonymous information about your server is sent to Microsoft to help improve SharePoint Server.  <br/> |
|DownloadErrorReportingUpdatesEnabled  <br/> |Boolean  <br/> |Specifies whether error reports are uploaded to Microsoft automatically. Error reports include the following: Information about the condition of the server when a problem occurs, The operating system version and computer hardware in use, and The digital product ID, which can be used to identify your license.  <br/> **Note:** <br/> The IP address of your computer is also sent because you are connecting to an online service to send error reports; however, the IP address is used only to generate aggregate statistics.  <br/> |
|DaysToKeepLogs  <br/> |Integer  <br/> |Specifies the number of days to keep trace log files. The type must be a valid number between 1 and 366. The default value is 14 days.  <br/> |
|LogMaxDiskSpaceUsageEnabled  <br/> |Boolean  <br/> |Specifies whether to restrict the maximum space to use for trace log files.  <br/> |
|LogDiskSpaceUsageGB  <br/> |Integer  <br/> |Specifies the maximum amount of storage to use for trace log files, in gigabytes (GB). The default value is 1000 and only takes effect when the LogMaxDiskSpaceusageEnabled parameter is set to True. The type must be a valid number between 1 and 1000.  <br/> |
|LogLocation  <br/> |String:Path  <br/> |This is the full path to the location where you want log files to be stored. It can be a remote location. Example: "%CommonProgramFiles%\Microsoft Shared\Web Server Extensions\16\LOGS\" and "%CommonProgramFiles%\Microsoft Shared\Web Server Extensions\15\LOGS\"  <br/> |
|LogCutInterval  <br/> |Integer  <br/> |Specifies a time period to roll over to the next log file. The type must be a valid number between 0 and 1440.  <br/> |
|EventLogFloodProtectionEnabled  <br/> |Boolean  <br/> |Specifies whether the Event log flood protection feature is enabled. If multiple similar events are written to the event log, some duplicate messages are suppressed. After a period of time, a summary message shows how many events were suppressed.  <br/> |
|EventLogFloodProtectionThreshold  <br/> |Integer  <br/> |Specifies the number of events allowed in a given timeframe before an event is considered to be flooding the event log. The integer range is between 1 and 100. The default value is 5.  <br/> |
|EventLogFloodProtectionTriggerPeriod  <br/> |Integer  <br/> |Specifies in minutes the timeframe to watch for events that may be flooding. The integer range is between 1 and 1440. The default value is 2.  <br/> |
|EventLogFloodProtectionQuietPeriod  <br/> |Integer  <br/> |Specifies in minutes how much time must pass without an event firing to exit flood protection. The integer range is between 1 and 1440. The default value is 2.  <br/> |
|EventLogFloodProtectionNotifyInterval  <br/> |Integer  <br/> |Specifies in minutes how often to write a summary event that indicates how many events were suppressed due to flood protection. The integer range is between 1 and 1440. The default value is 5.  <br/> |
|ScriptErrorReportingEnabled  <br/> |Boolean  <br/> |Enables or disabled the reporting of script errors in the Log file.  <br/> |
|ScriptErrorReportingRequireAuth  <br/> |Boolean  <br/> |Specifies whether script error reporting requires authentication.  <br/> |
|ScriptErrorReportingDelay  <br/> |Integer  <br/> |Specifies the time in minutes between script error reports. The value must be a valid integer between 0 and 1440. The value is specified in minutes. The default value is 30.  <br/> |
   
Use the following table for the UsageServices settings.

**The elements of the UsageServices settings**

|**Name**|**Value Type**|**Notes**|
|:-----|:-----|:-----|
|ID  <br/> |GUID: **Read-Only** <br/> |A GUID, in the form 12345678-90ab-cdef-1234-567890bcdefgh.  <br/> |
|UsageLogLocation  <br/> |Path  <br/> |Specifies the path on every computer in the farm where usage log files are created. The same path must exist on all computers in the farm.  <br/> |
|LoggingEnabled  <br/> |Boolean  <br/> |Specifies that usage data is logged to usage files.  <br/> |
|UsageLogMaxFileSizeKB  <br/> |Integer  <br/> |Specifies the maximum size of a single usage file that is applied to all the usage providers. The minimum value is 512 kilobytes (KB) and the maximum value is 65536 KB.  <br/> |
|UsageLogCutTime  <br/> |Integer  <br/> |Specifies the time in minutes of usage data that is collected per usage log file. The default time is 5 minutes. The value must be an integer in the range of 1 to 1440.  <br/> |
   
Use the following table for the UsageDefinition settings.

**The elements of the UsageDefinition settings**

|**Name**|**Value Type**|**Notes**|
|:-----|:-----|:-----|
|ID  <br/> |GUID: **Read-Only** <br/> |A GUID, in the form 12345678-90ab-cdef-1234-567890bcdefgh.  <br/> |
|Name  <br/> |String: **Read-Only** <br/> |The string name of the UsageDefinition.  <br/> |
|DaysRetained  <br/> |Integer  <br/> |Specifies the number of days to retain usage data for the usage provider in the usage service database. The default value is 14. The type must be an integer between 0 and 31.  <br/> |
|DaysToKeepUsageFiles  <br/> |Integer  <br/> |Specifies the number of days to retain usage files. The value must be less than or equal to value of the **DaysRetained** parameter.  <br/> |
|Enabled  <br/> |Boolean  <br/> |Enables or disables the specified usage provider.  <br/> |
   
Use the following table for the LogLevel settings.

**The elements of the LogLevel settings**

|**Name**|**Value Type**|**Notes**|
|:-----|:-----|:-----|
|Area  <br/> |String: **Read-Only** <br/> |The component or service that the LogLevel applies to.  <br/> |
|Identity  <br/> |String: **Read-Only** <br/> |Specifies the names of the category or set of categories to set the throttle for; for example, "Unified Logging Service".  <br/> **Note:** <br/> If the Identity parameter is not specified, the event-throttling setting is applied to all categories in the farm.  <br/> |
|EventSeverity  <br/> |String:[None | ErrorCritical |Error | Warning |Information | Verbose]  <br/> |Specifies the category level to be set. The category level is any one of the following values:[None | ErrorCritical |Error | Warning |Information | Verbose]  <br/> |
|TraceSeverity  <br/> |String:[None | Unexpected |Monitorable | High |Medium | Verbose | VerboseX]  <br/> |Specifies trace throttle to set the specified categories to. The trace log files are text files that are written to the trace log path that is defined on the Diagnostic Logging Settings page on the the SharePoint Central Administration website. The type must be any one of the following values::[None | Unexpected |Monitorable | High |Medium | Verbose | VerboseX]  <br/> |
   
Use the following table for the TimerJob settings.

**The elements of the TimerJob settings**

|**Name**|**Value Type**|**Notes**|
|:-----|:-----|:-----|
|Identity  <br/> |GUID: **Read-Only** <br/> |Specifies the timer job to update. The type must be a valid GUID, in the form 12345678-90ab-cdef-1234-567890bcdefgh.  <br/> |
|Schedule  <br/> |String  <br/> |Specifies the schedule for running the timer job. The type must be a valid SharePoint Timer service (SPTimer) schedule in the form of any one of the following schedules: Every 5 minutes between 0 and 59, Hourly between 0 and 59, Daily at 15:00:00, Weekly between Fri 22:00:00 and Sun 06:00:00, Monthly at 15 15:00:00, and Yearly at Jan 1 15:00:00  <br/> |
|Enabled  <br/> |Boolean  <br/> |Enables or disables the timer job.  <br/> |
   
Use the following table for the HealthAnalyzerRule settings.

**The elements of the HealthAnalyzerRule settings**

|**Name**|**Value Type**|**Notes**|
|:-----|:-----|:-----|
|Identity  <br/> |GUID: **Read-Only** <br/> |Specifies the name or GUID of the health analyzer rule to set.  <br/> |
|Enabled  <br/> |Boolean  <br/> |Enables or disables the health analyzer rule.  <br/> |
   
## Create Profiles

You can create an unlimited number of Profiles as. Each Profile might be used for a different purpose, such as to increase the levels of monitoring before a specific change to the environment, or to lower the levels after a change. 
  
You only need to create profile entries for the specific changes that you want to make. The other settings will remain unchanged. For example, if you want to change a few LogLevel settings, then you only need to specify those settings in the Profile. Settings that are not specified in the Profile will not be changed.
  
You might want to use a naming convention for your Profiles so that you can organize them and more easily use them.
  
> [!IMPORTANT]
> Always back up the monitoring settings before making any changes to them. Always work from a copy of the backup Profile and never from the original backup file itself. 
  
## See also

#### Concepts

[Overview of scripted monitoring configuration in SharePoint Server](overview-of-scripted-monitoring-configuration.md)
  
[Run scripted monitoring configuration in SharePoint Server](run-scripted-monitoring-configuration.md)

