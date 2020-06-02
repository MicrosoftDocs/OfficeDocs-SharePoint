---
title: "Configure diagnostic logging in SharePoint Server"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.date: 7/31/2017
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: faab1eb4-5848-4970-b13f-ba6df14272fe
description: "Learn to configure diagnostic logging in SharePoint Server from the SharePoint Central Administration website or by using Microsoft PowerShell."
---

# Configure diagnostic logging in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
    
## Prerequisites

The user account that is performing procedures from Central Administrationmust be a member of the Farm Administrators SharePoint group.
  
## Diagnostic logging setting best practices
<a name="section1"> </a>

The SharePoint Server environment might require configuration of the diagnostic logging settings after initial deployment, after upgrade, and if a change is made to the environment, such as adding or removing a server. The guidelines in the following list can help you form best practices for the specific environment.
  
- **Change the drive to which the server writes logs.**
    
    By default, SharePoint Server writes diagnostic logs to the same drive and partition on which it was installed. Because diagnostic logging can use a large amount of drive space and compromise drive performance, you should configure SharePoint Server to write to another drive on which SharePoint Server is not installed. You should also consider the connection speed to the drive on which SharePoint Server writes the logs. If verbose-level logging is configured, the server records a large amount of data. Therefore, a slow connection might result in poor log performance.
    
- **Restrict log disk space usage.**
    
    By default, the amount of disk space that diagnostic logging can use is unlimited. Therefore, restrict the disk space that logging uses, especially if you configure logging to write verbose-level events. When the disk reaches the restriction, SharePoint Server removes the oldest logs before it records new logging data.
    
- **Use the Verbose setting sparingly.**
    
    You can configure diagnostic logging to record verbose-level events. This means that SharePoint Server records every action that it takes. Verbose-level logging can quickly use drive space and affect drive and server performance. You can use verbose-level logging to record more detail when you are making critical changes and then reconfigure logging to record only higher-level events after you make the change.
    
- **Regularly back up logs.**
    
    Diagnostic logs contain important data. Therefore, back up the logs regularly to ensure that this data is preserved. When you restrict log drive space usage, or if you keep logs for only a few days, SharePoint Server automatically deletes log files, starting with the oldest files first, when the threshold is met.
    
- **Enable event log flooding protection.**
    
    When you enable this setting, SharePoint Server detects repeating events in the Windows event log, and suppresses them until conditions return to a typical state.
    
You can set the level of diagnostic logging for the event log and for the trace log. This limits the types and amount of information that are written to each log. The following tables define the levels of logging that are available for the event log and trace log.
  
**Event log levels**

|**Level**|**Definition**|
|:-----|:-----|
|None  <br/> |No logging occurs.  <br/> |
|Critical  <br/> |This message type indicates a serious error that has caused a major failure in the solution.  <br/> |
|Error  <br/> |This message type indicates an urgent condition. You should investigate all error events.  <br/> |
|Warning  <br/> |This message type indicates a potential problem or issue that might require attention. You should review and track warning messages for patterns over time.  <br/> |
|Information  <br/> |Information messages do not require any action. However, they can provide valuable data for monitoring the state of your solution.  <br/> |
|Verbose  <br/> |This event log level corresponds to lengthy events or messages.  <br/> |
   
**Trace log levels**

|**Level**|**Definition**|
|:-----|:-----|
|None  <br/> |No trace logs are written.  <br/> |
|Unexpected  <br/> |This level records messages about events that cause solutions to stop processing. When set to this level, the log will include events at the Unexpected, Exception, Assert, and Critical levels.  <br/> |
|Monitorable  <br/> |This level records messages about all unrecoverable events that limit the functionality of the solution but do not stop the application. When set to this level, the log also includes events that the Unexpected setting records.  <br/> |
|High  <br/> |This level records all events that are unexpected but which do not stop the processing of a solution. When set to log at this level, the log also includes all events that the Monitorable setting records.  <br/> |
|Medium  <br/> |When set to this level, the trace log includes all messages except Verbose and VerboseEx messages. This level records all high-level information about operations that were performed. This level provides enough detail to construct the data flow and sequence of operations. Administrators or support professionals could use this level of logging to troubleshoot issues. When set to this level, the log will also include all events that the High setting records.  <br/> |
|Verbose  <br/> |When set to this level, the log includes most actions. Verbose tracing produces many log messages. This level is typically used only for debugging in a development environment. When set to log at this level, the log will also include all events that the Medium setting records.  <br/> |
|VerboseEx  <br/> |This level is only supported by the **Set-SPLogLevel** PowerShell cmdlet, and includes very low-level diagnostic data. This level should only be used in a development environment. When set to this level, the log includes all events that the Verbose setting records.  <br/> |
   
## Configure diagnostic logging by using Central Administration
<a name="section2"> </a>

You can use the SharePoint Central Administration website to configure diagnostic logging.
  
 **To configure diagnostic logging by using Central Administration**
  
1. In Central Administration, on the home page, click **Monitoring**.
    
2. On the Monitoring page, in the **Reporting** section, click **Configure diagnostic logging**.
    
3. On the Diagnostic Logging page, in the **Event Throttling** section, configure event throttling as follows: 
    
    To configure event throttling for all categories:
    
1. Select the **All Categories** check box. 
    
2. Select the event log level from the **Least critical event to report to the event log** list. 
    
3. Select the trace log level from the **Least critical event to report to the trace log** list. 
    
    To configure event throttling for one or more categories:
    
1. Select the check boxes of the categories that you want.
    
2. Select the event log level from the **Least critical event to report to the event log** list. 
    
3. Select the trace log level from the **Least critical event to report to the trace log** list. 
    
    To configure event throttling for one or more subcategories (you can expand one or more categories and select any subcategory):
    
1. Click the plus **(+)** next to the category to expand the category. 
    
2. Select the check box of the subcategory.
    
3. Select the event log level from the **Least critical event to report to the event log** list. 
    
4. Select the trace log level from the **Least critical event to report to the trace log** list. 
    
    To return event throttling for all categories to default settings:
    
1. Select the **All Categories** check box. 
    
2. Select **Reset to default** from the **Least critical event to report to the event log** list. 
    
3. Select **Reset to default** from the **Least critical event to report to the trace log** list. 
    
4. In the **Event Log Flood Protection** section, select the **Enable Event Log Flood Protection** check box. 
    
5. In the **Trace Log** section, in the **Path** box, type the path of the folder to which you want logs to be written. 
    
6. In the **Number of days to store log files** box, type the number of days (1-366) that you want logs to be kept. After this time, logs will automatically be deleted. 
    
7. To restrict the disk space that logs can use, select the **Restrict Trace Log disk space usage** check box, and then type the number gigabytes (GB) you want to restrict log files to. When logs reach this value, older logs will automatically be deleted. 
    
8. After you have made the changes that you want on the Diagnostic Logging page, click **OK**.
    
## Configure diagnostic logging by using PowerShell
<a name="section3"> </a>

You can use PowerShell to configure diagnostic logging.
  
 **To configure diagnostic logging by using PowerShell**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use PowerShell cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. From the SharePoint Management Shell, change the drive to which the server writes logs.
    
3. At the PowerShell command prompt, type the following command:
    
  ```
  Set-SPDiagnosticConfig -LogLocation D:\DiagnosticLogs
  ```

4. To restrict log disk space usage, at the PowerShell command prompt, type the following command:
    
  ```
  Set-SPDiagnosticConfig -LogMaxDiskSpaceUsageEnabled
  ```

    Or assign the maximum disk space for logs:
    
  ```
  Set-SPDiagnosticConfig -LogDiskSpaceUsageGB 500
  ```

5. To view the current logging level, at the PowerShell command prompt, type the following command:
    
  ```
  Get-SPLogLevel
  ```

6. To change the logging level, at the PowerShell command prompt, type the following command:
    
  ```
  Set-SPLogLevel -TraceSeverity Monitorable
  ```

    To set all categories back to default levels, at the PowerShell command prompt, type the following command, and then press ENTER: 
    
  ```
  Clear-SPLogLevel
  ```

7. To enable event log flooding protection, at the PowerShell command prompt, type the following command:
    
  ```
  Set-SPDiagnosticConfig -EventLogFloodProtectionEnabled
  ```

For more information, see [Set-SPDiagnosticConfig](/powershell/module/sharepoint-server/Set-SPDiagnosticConfig?view=sharepoint-ps), [Set-SPLogLevel](/powershell/module/sharepoint-server/Set-SPLogLevel?view=sharepoint-ps) and [Get-SPLogLevel](/powershell/module/sharepoint-server/Get-SPLogLevel?view=sharepoint-ps). 
  
## See also
<a name="section3"> </a>

#### Concepts

[Overview of monitoring in SharePoint Server](monitoring-overview.md)

