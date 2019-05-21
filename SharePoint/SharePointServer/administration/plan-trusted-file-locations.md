---
title: "Plan Trusted File Locations in SharePoint Server 2013"
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 6/23/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: 3a080c72-df1f-43a2-8aee-a3ffd0c43ad2
description: "Plan Excel Services trusted file location parameters, including session, workbook, calculation, memory, and external data settings."
---

# Plan Trusted File Locations in SharePoint Server 2013

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)]. 
  
This article describes trusted file locations for Excel Services.
  
    
## Introduction to Trusted File Locations for Excel Services
<a name="introduction"> </a>

 Excel Services automatically creates a default trusted file location (http://) which trusts the whole SharePoint Server 2013 farm. This default trusted location enables any file to be loaded from the SharePoint Server 2013 farm or stand-alone deployment by using Excel Services. Trusting the whole SharePoint farm by default enables easier setup for administrators. Administrators can define new trusted file locations to expand workbook capabilities and tighten security. 
  
Excel Services administrators can add new trusted file locations as needed. Trusted file locations are either SharePoint sites, UNC paths, or HTTP Web sites from which a server that is running Excel Services is permitted to access workbooks. 
  
To make sure that only trusted users have access to workbooks stored in trusted locations, it is important to enforce ACLs on all trusted file locations.
  
There are three core scenarios to deploy Excel Services: enterprise, small department, and custom.
  
In an enterprise deployment, consider the following guidelines:
  
- Do not configure support for user-defined functions.
    
- Do not enable workbooks to use embedded data connections to directly access external data sources.
    
- Limit the use of data connection libraries for external data source access from workbooks.
    
- Restrict the size of workbooks that can be opened in Excel Services.
    
- Selectively trust specific file locations and do not enable **Trust Children** for trusted sites and directories. 
    
In a small department deployment, consider the following guidelines:
  
- Enable trust for all file locations that are used by department members to store workbooks.
    
- Enable **Trust Children** for all trusted sites and directories. 
    
- Selectively restrict access to specific file locations if problems occur.
    
In a custom deployment, consider the following guidelines:
  
- Enable Excel Services to open large workbooks.
    
- Configure long session time-out settings.
    
- Configure large data caches.
    
- Create a single trusted location for this deployment.
    
- Do not enable **Trust Children** for this trusted location. 
    
## Workbook location settings for Excel Services
<a name="location"> </a>

In the **Location** section of the Excel Services Add Trusted File Location page, you can configure the address, the location type, and whether child libraries of trusted file locations are also trusted. By selecting **Trust children** you can simplify manageability. However, you can also create a potential security issue by enabling subsites and subdirectories of trusted locations to be automatically trusted as soon as they are created. Only choose **Children trusted** if you are certain that any child directories or libraries will contain workbooks that you want Excel Services to trust. 
  
## Session management settings for Excel Services
<a name="sessionmanagement"> </a>

In the **Session Management** section, you can configure settings to help conserve resource availability and improve Excel Services performance and security. Performance can decrease when many users have multiple Excel Services sessions open at the same time. You can control resource consumption and limit the duration of open Excel Services sessions by configuring two time-out settings for open sessions. 
  
The **Session Timeout** setting determines the time that an Excel Services session can remain open and inactive after each user interaction. The **Short Session Timeout** setting determines how long an Excel Services session can remain open and inactive after the initial session request. The **New Workbook Session Timeout** setting determines how long an Excel Services session for a new workbook can remain open and inactive before it is shut down. You can also control the number of seconds allowed for any single session request by configuring a **Maximum Request Duration** value. Similarly, you can configure the **Maximum Chart Render Duration**. By limiting how long sessions remain open, you can help reduce the risk of denial-of-service attacks.
  
We recommend that you start with the default values and adjust them as needed if you encounter performance issues.
  
## Workbook and image size settings for Excel Services
<a name="imagesize"> </a>

In the **Workbook Properties** section, you can configure a maximum size of any workbook, chart or image that is permitted to be opened in an Excel Services session. Performance and resource availability can be compromised when users open extremely large workbooks. Unless you control the allowable size of workbooks running in open Excel Services sessions, you risk users exceeding your resource capacity and causing the server to fail. 
  
## Calculation behavior settings for Excel Services
<a name="calculation"> </a>

In the **Calculation Behavior** section, you determine calculation modes in Excel Calculation Services for workbooks from this location. The **Volatile Function Cache Lifetime** setting specifies how long a computed value for a volatile function is cached for automatic recalculations. The **Workbook Calculation Mode** setting specifies options for how and when workbook calculations are performed. 
  
## External Data settings for Excel Services
<a name="externaldata"> </a>

In the **External Data** section, you can determine whether workbooks stored in trusted file locations and opened in Excel Services sessions can access an external data source. You can designate whether **Allow External Data** is set to **None**, **Trusted data connection libraries only**, or **Trusted data connection libraries and embedded**. If you select either **Trusted data connection libraries only** or **Trusted data connection libraries and embedded**, the workbooks stored in the trusted file locations can access external data sources.
  
External data connections can be accessed only when they are embedded in or linked from a workbook. Excel Services checks the list of trusted file locations before it opens a workbook. If you select **None**, Excel Services will block any attempt to access an external data source. If you manage data connections for many workbook authors, consider specifying **Trusted data connection libraries only**. This ensures that all data connections in all of the workbooks generated by authenticated workbook authors have to use a trusted data connection library to access any external data sources.
  
If you manage data connections for only a few workbook authors, consider specifying **Trusted data connection libraries and embedded**. This enables workbook authors to embed direct connections to external data sources in their workbooks, but still have access to trusted data connection libraries.
  
In the **Warn on Refresh** area of the **External Data** section, you can specify whether a warning is displayed before a workbook updates from an external data source. By selecting **Refresh warning enabled**, you ensure that external data is not automatically refreshed without user interaction.
  
In the **Display Granular External Data Errors** option, if you enable the Granular External Data Errors setting it provides descriptive error messages to display that provide helpful information for troubleshooting and fixing connection problems. 
  
In the **Stop When Refresh on Open Fails** area, you can specify if Excel Services stops opening a workbook if the workbook contains a Refresh on Open data connection that fails. By selecting **Stopping open enabled**, you ensure that cached values are not displayed if an update operation fails when the workbook is opened by any user having View Only permissions to the workbook. This is useful when a report may contain per-user data and you don't want a user to see another user's cached data. When Refresh on Open is successful, cached values are purged. By clearing the **Stopping open enabled** check box, you risk displaying cached values if Refresh on Open fails. 
  
In the **External Data Cache Lifetime** area of the **External Data** section, you can specify the maximum time that cached values can be used before they expire, and the maximum number of external data queries that can execute at the same time in a single session. 
  
You can also specify the maximum number of queries that you want to allow for a given session, as well as whether to enable allow external data using REST.
  
## User-defined functions settings for Excel Services
<a name="userdefinedfunctions"> </a>

If your deployment scenarios include workbooks that contain user-defined functions to extend the capabilities of Excel Calculation Services, you must configure Excel Services to support user-defined functions.
  
To configure this support, you must enable user-defined functions on trusted file locations that contain workbooks that require access to user-defined functions. In addition, you must register user-defined function assemblies on the Excel Services user-defined function assembly list. See [Manage Excel Services user defined function assemblies (SharePoint Server 2013)](manage-excel-services-user-defined-function-assemblies.md) for more information about how to enable user-defined functions. 
  
## See also
<a name="userdefinedfunctions"> </a>

#### Concepts

[Plan Trusted Data Connection Libraries in SharePoint Server 2013](plan-trusted-data-connection-libraries.md)

