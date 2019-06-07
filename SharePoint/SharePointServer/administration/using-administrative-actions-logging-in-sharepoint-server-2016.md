---
title: "Using Administrative Actions logging in SharePoint Server 2016"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.date: 11/7/2016
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 3a832d60-f14f-4663-93bd-f006e6148c02

description: "The Administrative Actions logging feature is included in the November 2016 Public Update for SharePoint Server 2016 (Feature Pack 1). This feature enables logging of SharePoint Server 2016 administrative actions."
---

# Using Administrative Actions logging in SharePoint Server 2016

[!INCLUDE[appliesto-xxx-2016-xxx-xxx-md](../includes/appliesto-xxx-2016-xxx-xxx-md.md)]

The Administrative Actions logging feature is included in the November 2016 Public Update for SharePoint Server 2016 (Feature Pack 1). This feature enables logging of SharePoint Server 2016 administrative actions.
  
## Overview

Administrative changes to SharePoint Server settings can sometimes cause errors or have unintended effects. To aid in troubleshooting administrative changes, logging around key SharePoint administrative actions is available in Feature Pack 1. Logging is available for both Central Administration and Windows PowerShell actions.
  
## Turning on Administrative Actions logging

Administrative Actions logging is turned on by default when you install SharePoint Server 2016 November 2016 Public Update for SharePoint Server 2016 (Feature Pack 1). 
  
After you install Feature Pack 1, Administrative Actions will show up as a checked option under "Events to log" in the **Configure usage and health data collection** page of SharePoint 2016 Central Administration. 
  
![Administrative Action Logging in Central Administration of SharePoint 2016](../media/596f8663-863a-4393-8017-6e961ea08152.png)
  
## How to find the Administrative actions local log file location

Administrative actions log files are stored on your server. To view the local location of these logs:
  
1. On the SharePoint 2016 Central Administration home page, click **Monitoring**. 
    
2. In the Reporting section, click **Configure usage and health data collection**. 
    
3. You will see the log file location listed under **Usage Data Collection Settings**. 
    
## How to find the Administrative actions Usage Database log files

Administrative actions logs are written to the SharePoint Usage Database. To find your logging database server:
  
1. On the SharePoint 2016 Central Administration home page, click ** Monitoring **. 
    
2. In the Reporting section, click **Configure usage and health data collection**. 
    
3. You will find the logging database server and database name under: **Logging Database Server settings**. 
    
## Retrieving logs from the SharePoint Usage Database

Administrative actions logs are kept in the SharePoint Usage Database for a maximum of 31 days.
  
1. Open Microsoft SQL Server Management Studio. ** Note: ** You must be logged in as Administrator. 
    
2. Connect to the Server name indicated as the "Database Server," in the Logging **Database Server settings** above. 
    
3. Connect to your applicable logging database. This is the database you have specified as the "Database Name" in the **Logging Database Server settings**, typically WSS_Logging. 
    
4. Query the "AdministrativeActions" partitions.
    
    > [!NOTE]
    > Select the number of applicable "AdministrativeActions" partitions. There should be 32 partitions created, partitions 0 through 31. WSS_logging is the default logging **Database Name**. Modify the query if your logging **Database Name** is different. 
  
 **Sample Query**
  
```
SELECT TOP 1000 [PartitionId]
      ,[RowId]
      ,[LogTime]
      ,[MachineName]
      ,[FarmId]
      ,[SiteSubscriptionId]
      ,[UserLogin]
      ,[CorrelationId]
      ,[Action]
      ,[Target]
      ,[Details]
      ,[RowCreatedTime]
  FROM (
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition0]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition1]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition2]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition3]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition4]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition5]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition6]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition7]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition8]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition9]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition10]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition11]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition12]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition13]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition14]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition15]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition16]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition17]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition18]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition19]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition20]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition21]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition22]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition23]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition24]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition25]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition26]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition27]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition28]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition29]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition30]
union
select * from [WSS_Logging].[dbo].[AdministrativeActions_Partition31]
) as A

```

## Using Windows PowerShell to retrieve logs

You can also retrieve Administrative Actions logs using the Windows PowerShell cmdlet, ** Merge-SPUsageLog **. 
  
> [!IMPORTANT]
> Remote cmdlet execution must be enabled to use **Merge-SPUsageLog**. To configure the computer to receive remote commands, see [Enable-PSRemoting](/powershell/module/Microsoft.PowerShell.Core/Enable-PSRemoting?view=powershell-5.1). 
  
The **Merge-SPUsageLog** cmdlet gathers, filters, and aggregates logs based on the your specified criteria. We recommend that you filter by using the StartTime and EndTime parameters to optimize performance of this cmdlet. 
  
 **Merge-SPUsageLog** generates objects into PowerShell pipeline from logs that meet the criteria. You should at least specify a usage type, for example "Administrative Actions". 
  
```
Merge-SPUsageLog -Identity <SPUsageDefinitionPipeBind> [-AssignmentCollection <SPAssignmentCollection>] [-DiagnosticLogPath <String>] [-EndTime <DateTime>] [-OverWrite <SwitchParameter>] [-Servers <String[]>] [-StartTime <DateTime>] 
 
```

|**Parameter**|**Required**|**Type**|**Description**|
|:-----|:-----|:-----|:-----|
|Identity  <br/> |Required  <br/> |Microsoft.SharePoint.PowerShell.SPUsageDefinitionPipeBind  <br/> |Specifies the name of usage log file.  <br/> |
|AssignmentCollection  <br/> |Optional  <br/> |Microsoft.SharePoint.PowerShell.SPAssignmentCollection  <br/> |Manages objects for the purpose of proper disposal. Use of objects, such as SPWeb or SPSite, can use large amounts of memory and use of these objects in Windows PowerShell scripts requires proper memory management. Using the SPAssignment object, you can assign objects to a variable and dispose of the objects after they are needed to free up memory. When SPWeb, SPSite, or SPSiteAdministration objects are used, the objects are automatically disposed of if an assignment collection or the Global parameter is not used.  <br/> > [!NOTE]> When the Global parameter is used, all objects are contained in the global store. If objects are not immediately used, or disposed of by using the Stop-SPAssignment command, an out-of-memory scenario can occur.           |
|DiagnosticLogPath  <br/> |Optional  <br/> |System.String  <br/> |Specifies the file to write diagnostic information to. A relative path is supported.  <br/> |
|EndTime  <br/> |Optional  <br/> |System.DateTime  <br/> |Specifies the end time of the log entries returned. The type must be a valid DateTime format that is culture-specific to the administrative language, that is, 2/16/2007 12:15:12 for English-US. The default value is the current time.  <br/> If you want to specify UTC time, you must add a "Z" to the end of the parameter. For example, "2016-06-15 03:29:18.199 Z". If the "Z" is not specify, local computer time will be displayed instead of UTC.  <br/> |
|OverWrite  <br/> |Optional  <br/> |System.Management.Automation.SwitchParameter  <br/> |Overwrites the diagnostic log file if it already exists at the specified path.  <br/> |
|Servers  <br/> |Optional  <br/> |System.String[]  <br/> |The server address or addresses to filter on. To obtain a list of valid addresses in the farm use Get-SPServer | Select Address.  <br/> |
|StartTime  <br/> |Optional  <br/> |System.DateTime  <br/> |Specifies the start time of the log entries returned. The type must be a valid DateTime format that is culture-specific to the administrative language, such as "2/16/2007 12:15:12" for English-US. The default value is one hour prior to the current time on the local computer.  <br/> If you want to specify UTC time, you must add a "Z" to the end of the parameter. For example, "2016-06-15 03:29:18.199 Z". If the "Z" is not specify, local computer time will be displayed instead of UTC.  <br/> |
   
 **Example 1:** This example merges the last hour of log data for "Administrative Actions" usage provider from all farm computers. 
  
```
Merge-SPUsageLog -Identity "Administrative Actions" 
```

 **Example 2:** This example merges the log entries for the "Administrative Actions" usage provider from "06/09/2016 16:00" until now from servers named "A-0606" and "A-0505". 
  
```
Merge-SPUsageLog -Identity "Administrative Actions" -Servers "A-0606","A-0505" -StartTime "06/09/2008 16:00" 

```

 **Example 3:** This example retrieves Administrative Actions logs starting from Aug 11th, and then selects the following fields to display: User, ActionName, and TimeStamp. The results are sorted by TimeStamp. This example uses the Windows PowerShell pipeline. For more information about how to use the pipeline, see about_Pipelines 
  
```
Get-SPUsageDefinition -Identity "Administrative Actions" | Merge-SPUsagelog  -StartTime "08/11/2016 3:50 AM" | Select User, ActionName, Timestamp | Sort Timestamp  
 
```

## Types of administrative actions logged

The following tables details the types of Administrative Actions that are captured in the logs.
  
|**Action category**|**Action sub-category**|**Log actions(s)**|**Description**|
|:-----|:-----|:-----|:-----|
|Configure Accounts  <br/> |Add, Remove, Update  <br/> |Administration.Security.User.Add          Administration.Security.User.Remove          Administration.Security.User.Update          Administration.Security.User.Role.Update  <br/> |Logs administrative account configuration and information changes including the addition, removal, and updates of farm and site collections administrators. Also, logs role updates.  <br/> |
|Configure managed accounts  <br/> |New, Remove, Update  <br/> |Administration.Security.ManagedAccount.New Administration.Security.ManagedAccount.Remove Administration.Security.ManagedAccount.Update  <br/> |Logs changes in the configuration of managed accounts, creation and removal of managed accounts, and updates to existing managed accounts.  <br/> |
|Configure Service Account  <br/> |Update  <br/> |Administration.Security.ServiceAccount.Update  <br/> |Logs updates to the designated service accounts in the farm.  <br/> |
|Configure Password change settings  <br/> |Update  <br/> |Administration.Security.AccountPasswordSetting.Update  <br/> |Logs updates to password management settings.  <br/> |
|Specify Authentication Providers  <br/> |Update  <br/> |Administration.Security.AuthenticationProviderSetting.Update  <br/> |Logs updates to authentication provider settings.  <br/> |
|Manage Trust  <br/> |Edit, Remove, Update  <br/> |Administration.Security.ManageTrust.SPTrustedRootAuthority.Edit Administration.Security.ManageTrust.SPTrustedRootAuthority.New Administration.Security.ManageTrust.SPTrustedRootAuthority.Remove Administration.Security.ManageTrust.SPTrustedSecurityTokenIssuer.Edit Administration.Security.ManageTrust.SPTrustedSecurityTokenIssuer.New Administration.Security.ManageTrust.SPTrustedSecurityTokenIssuer.Remove  <br/> |Administration.Security.ManageTrust.SPTrustedRootAuthority logs edits to, and removals of the trust relationship settings in the farm, and the creation of new trust relationships. Administration.Security.ManageTrust.SPTrustedSecurityTokenIssuer logs edits to, and removals of the token issuer settings, and the creation of new token issuer trust relationships.  <br/> |
|Manage Web Part Security  <br/> |Update  <br/> |Administration.Security.WebPart.Update  <br/> |Logs updates to Web Part pages and Web parts on your selected web application.  <br/> |
|Farm backup and restore operations  <br/> |Backup, Restore, Update  <br/> |Administration.Farm.BackupRestore.Backup Administration.Farm.BackupRestore.Restore Administration.Farm.BackupRestore.Settings.Update  <br/> |Logs farm restore and backup operations, including updates to your default backup and restore settings.  <br/> |
|Server Administration  <br/> |Add, Remove, Update  <br/> |Administration.Farm.Server.Add Administration.Farm.Server.Remove Administration.Farm.Server.Role.Update  <br/> |Logs removals and additions of servers to the farm, including role updates of farm servers.  <br/> |
|Configuration database changes  <br/> |New, Remove  <br/> |Administration.Farm.ConfigurationDatabase.New Administration.Farm.ConfigurationDatabase.Remove  <br/> |Logs the addition of the new configuration database or the removal of an existing one.  <br/> |
|Site Collection Administration  <br/> |Add, Backup, Export, Import, Remove, Restore, Update  <br/> |Administration.SiteCollection.Add Administration.SiteCollection.Remove Administration.SiteCollection.BackupRestore.Backup Administration.SiteCollection.BackupRestore.Restore Administration.SiteCollection.Owner.Update Administration.SiteCollection.SecondContact.Update Administration.SiteCollection.Quota.Update Administration.SiteCollection.ImportExport.Export Administration.SiteCollection.ImportExport.Import  <br/> |Logs the most common operations around site collection administration, including the addition and removal of a site collection, backup and restore operations of a site collection, changes to ownership, secondary contact, and quota, and import and export operations of the site collection.  <br/> |
|Site Collection Content Database  <br/> |Add, New, Remove, Set  <br/> |Administration.ContentDatabase.Add Administration.ContentDatabase.New Administration.ContentDatabase.Remove Administration.ContentDatabase.Set  <br/> |Logs common SharePoint content database operations such as: adding a content database to the farm, creating a new content database, removing a content database, and setting the global properties of a content database.  <br/> |
|Quota Changes  <br/> |New, Remove, Update  <br/> |Administration.Quota.New Administration.Quota.Remove Administration.Quota.Update  <br/> |Logs setting a site new collection quota, making updates to an existing site collection quota, and removing a site collection quota.  <br/> |
|Feature Administration  <br/> |Install, Disable, Uninstall, Enable  <br/> |Administration.Feature.Disable Administration.Feature.Enable Administration.Feature.Install Administration.Feature.Uninstall  <br/> |Logs site collection feature administration actions to disable, enable, install, and uninstall features.  <br/> |
|Web Application Administration  <br/> |Edit, New, Remove  <br/> |Administration.WebApplication.Edit Administration.WebApplication.New Administration.WebApplication.Remove  <br/> |Logs common web application administrations actions including edits to an existing web application, the creation of a new web application, and the removal of an existing web application.  <br/> |
|Web Application Administration User Policy  <br/> |Add, New, Remove, Update  <br/> |Administration.WebApplication.UserPolicy.Add Administration.WebApplication.UserPolicy.New Administration.WebApplication.UserPolicy.Remove Administration.WebApplication.UserPolicy.Update  <br/> |Logs operations related to the management of user permission policies of web applications including: adding users to an existing web application user policy, creating a new user policy, removing users from an existing user policy, and making updates to a user permission policy.  <br/> |
|Service Application  <br/> |Edit, New, Remove  <br/> |Administration.ServiceApplication.Edit Administration.ServiceApplication.New Administration.ServiceApplication.Remove  <br/> |Logs edits to Service Applications, the creation of a new Service Application, and the removal of an existing Service Application.  <br/> |
|Form &amp; Feature Template Administration  <br/> |Convert, Disable, Enable, Install, New, Set, Start, Stop, Test, Update, Upgrade, Uninstall  <br/> |Administration.FormTemplate.Convert Administration.FormTemplate.Disable Administration.FormTemplate.Enable Administration.FormTemplate.Install Administration.FormTemplate.New Administration.FormTemplate.Set Administration.FormTemplate.Start Administration.FormTemplate.Stop Administration.FormTemplate.Update Administration.FormTemplate.Test Administration.FormTemplate.Upgrade Administration.FormTemplate.Uninstall Administration.Feature.FormTemplate.Install Administration.Feature.FormTemplate.Uninstall  <br/> |Logs operations related to the management of InfoPath templates in site collections, including: template conversion, disablement (deactivation), enablement, installation, creation of a new template, setting a template, starting and stopping of templates, updates, testing, upgrade, and uninstalling of a template.  <br/> |
|Content Database  <br/> |Add, New, Remove, Set  <br/> |Administration.ContentDatabase.Add Administration.ContentDatabase.New Administration.ContentDatabase.Remove Administration.ContentDatabase.Set  <br/> ||
|Configure Groups  <br/> |Add, Remove, Update  <br/> |Administration.Security.Group.Add Administration.Security.Group.Remove Administration.Security.Group.Update  <br/> |Logs actions related to group creation, deletion, and management, such as: adding, removing, and updating groups.  <br/> |
|User &amp; Group Migration  <br/> |Move  <br/> |Administration.Security.User.Move Administration.Security.Group.Move  <br/> |Logs activities relating the migration of group and user logins.  <br/> |
   

