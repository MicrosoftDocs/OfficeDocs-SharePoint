---
title: "Overview of SQL Server in a SharePoint Server 2013 environment"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 3/9/2018
audience: ITPro
ms.topic: concetpual
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 4dd5daa5-a22c-40c8-b250-6b4779714bb3
description: "Learn about the SharePoint Server relationship with SQL Server 2008 R2 with Service Pack 1 (SP1), SQL Server 2012, and SQL Server 2014 and how you can interact with the databases."
---

# Overview of SQL Server in a SharePoint Server 2013 environment

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)]
  
SharePoint Server 2013 supports several versions of SQL Server. Depending on the installed version, you can use specific features of SQL Server, such as reporting and business intelligence (BI).
  
> [!NOTE]
> SharePoint Foundation 2013 does not support BI features, which require SharePoint Server 2013. 
  
The minimum requirements for a database server in SharePoint Server 2013 are SQL Server 2008 R2 with Service Pack 1 (SP1) or SQL Server 2012, or SQL Server 2014 64-bit versions. Note that to use the business intelligence (BI) tools in SharePoint Server 2013 you must install SQL Server 2012 with Service Pack 1 (SP1) or SQL Server 2014, 64-bit version. For more information, see [Hardware and software requirements for SharePoint Server 2016](../install/hardware-and-software-requirements.md).
  
    
## SharePoint Server 2013 and the SQL Server database engine
<a name="sec1"> </a>

The SharePoint Server 2013 application is built on the SQL Server database engine. Most content and settings in SQL Server 2008 R2 with Service Pack 1 (SP1), SQL Server 2012, and SQL Server 2014 are stored in relational databases. The following table shows the databases that SharePoint Server 2013 uses.
  
|**Database type**|**Description**|
|:-----|:-----|
|Configuration  <br/> |The Configuration database and Central Administration content database are called configuration databases. They contain data about farm settings such as the databases that are used, Internet Information Services (IIS) web sites or web applications, solutions, Web Part packages, site templates, default quota, and blocked file types. A farm can only have one set of configuration databases.  <br/> |
|Content  <br/> | Content databases store all site content:  <br/>  Site documents, such as files in document libraries  <br/>  List data  <br/>  Web Part properties  <br/>  Data for apps for SharePoint  <br/>  User names and permissions  <br/>  Each web application can contain many content databases. Each site collection can be associated with only one content database, although a content database can be associated with many site collections.  <br/> |
|Service application  <br/> |Databases for service applications store the data that service applications use.  <br/> |
   
For a full list of all of the databases that support SharePoint Server, see [Database types and descriptions in SharePoint Server](../technical-reference/database-types-and-descriptions.md). For a graphical representation of the databases that support SharePoint Server 2013, see [Databases that support SharePoint 20113](https://go.microsoft.com/fwlink/p/?LinkId=259177).
  
## Working with the SQL Server databases that support SharePoint Server 2013
<a name="sec2"> </a>

The databases that support SharePoint Server 2013 are either created automatically with the SharePoint Products Configuration Wizard or by database administrators when they manually configure SharePoint Server 2013.
  
Microsoft does not support directly querying or modifying the databases that support SharePoint Server. In SharePoint Server the Usage and Health Data Collection database does support schema modifications.
  
The SQL Server databases that support SharePoint Server 2013 are subject to sizing limitations and to configuration recommendations that are not standard for SQL Server. For more information, see [Storage and SQL Server capacity planning and configuration (SharePoint Server)](storage-and-sql-server-capacity-planning-and-configuration.md).
  
## SQL Server 2008 R2 with Service Pack 1 (SP1)
<a name="sqlserverr2"> </a>

SQL Server 2008 R2 introduced Power Pivot for SharePoint and Power Pivot for Excel 2010 for SharePoint business intelligence capability through integration with SharePoint Server 2010. Both SQL Server Analysis Services and SQL Server Reporting Services can run in the same SharePoint Server farm. SQL Server 2008 R2 with Service Pack 1 (SP1) introduced various new features and fixed many SQL Server 2008 R2 issues. For more information, see "1.0 What's New in Service Pack 1" in [Microsoft SQL Server 2008 R2 SP1 Release Notes](https://social.technet.microsoft.com/wiki/contents/articles/2973.microsoft-sql-server-2008-r2-sp1-release-notes.aspx#whats_new?wa=wsignin1.0).
  
### SQL Server Reporting Services in SharePoint Integrated Mode
<a name="RSint"> </a>

SQL Server 2008 R2 Reporting Services supports two types of SharePoint integration. Full integration relies on the SharePoint integrated mode. Partial integration relies on two Web Parts, Report Explorer and Report Viewer, which you must install on a SharePoint site and point to a remote report server instance. For more information, see [Overview of Reporting Services and SharePoint Technology Integration](https://go.microsoft.com/fwlink/p/?LinkID=190605) and [Planning for SharePoint Integration](https://go.microsoft.com/fwlink/p/?LinkId=285618).
  
> [!NOTE]
> Reporting Services supports SharePoint integrated mode using SharePoint Server 2013 only. 
  
When you setup Reporting Services with SharePoint Server 2013 you create a report server. The report server is the central component of Reporting Services. This component contains two processing engines and a set of unique extensions that handle authentication, data processing, rendering, and delivery operations. 
  
> [!NOTE]
> When you configure a report server to run with SharePoint Server 2013 in integrated mode you must install the SQL Server 2012 Reporting Services add-in or later on a SharePoint front-end web server. > SQL Server 2008 R2 is the minimum version and is not supported when you use SQL Server 2012 Reporting Services or SQL Server 2014 Reporting Services. 
  
For more information, see [Supported Combinations of SharePoint and Reporting Services Components](http://go.microsoft.com/fwlink/?LinkID=524852&amp;clcid=0x409). The following levels of integration are provided when you run a report server in integrated mode with SharePoint Server 2013.
  
- Shared storage
    
- Shared security
    
- Same site access for all business documents such as reports, report models, and shared data sources
    
When Reporting Services runs in SharePoint integrated mode, both the SharePoint content and report server databases store content and metadata. The following table shows the report server data that each database stores.
  
|**Name of database**|**Report server data**|
|:-----|:-----|
|SharePoint content  <br/> | Primary storage for the following data:  <br/>  Published reports  <br/>  Report models  <br/>  Shared data sources  <br/>  Resources  <br/>  Properties  <br/>  Permissions  <br/> |
|SharePoint configuration  <br/> | All report server configuration settings that you make in Central Administration including:  <br/>  Report server URL  <br/>  Report server Reporting Services account information  <br/>  Information about the authentication provider that is used on the server  <br/>  Site-level settings that limit or enable report history and logging  <br/> |
|Report server  <br/> | Internal copies of report content and metadata, which are also stored in the SharePoint content database, and the following report data:  <br/>  Schedules  <br/>  Subscriptions  <br/>  Snapshots for report history or report execution  <br/> |
|Report server Temp  <br/> | Temporary data, including the following:  <br/>  Session data  <br/>  Temporary snapshots created for subscription processing, interactive reporting, or report caching as a performance improvement  <br/> |
   
Reporting Services data alerts are available to inform recipients of changes in report data.
  
For more information, see [Storing and Synchronizing Report Server Content With SharePoint Databases](https://go.microsoft.com/fwlink/p/?LinkID=190612)
  
## SQL Server 2012 and SQL Server 2014
<a name="sec4"> </a>

SQL Server 2012 with SP1 and SQL Server 2014 provide business intelligence solutions for SharePoint Server 2013. The SharePoint mode of SQL Server 2012 provides features for SQL Server Analysis Services and SQL Server Reporting Services. In addition, the SharePoint mode provides SQL Server BI features in SharePoint Server 2013. For more information, see [Features Supported by the Editions of SQL Server 2012](http://go.microsoft.com/fwlink/?LinkID=524889&amp;clcid=0x409) and [Features Supported by the Editions of SQL Server 2014](http://go.microsoft.com/fwlink/?LinkID=524888&amp;clcid=0x409).
  
> [!NOTE]
> SharePoint Foundation 2013 does not support SQL Server BI features. 
  
### High Availability Solutions
<a name="HA"> </a>

We recommend AlwaysOn Availability Groups for high availability in SQL Server 2012 Reporting Services and SQL Server 2014 Reporting Services. Other high availability solutions are AlwaysOn Failover Cluster Instances, database mirroring, and log shipping. Both AlwaysOn Availability Groups and Failover Cluster Instances solutions require and use Windows Server Failover Clustering (WSFC).
  
> [!NOTE]
> We recommend that you use AlwaysOn Availability Groups instead of database mirroring for your high availability solution with SQL Server 2012 or SQL Server 2014 and SharePoint Server 2013. For more information, see [Overview of SQL Server High-Availability Solutions](https://go.microsoft.com/fwlink/p/?LinkID=188016). 
  
For more information, see [AlwaysOn Availability Groups (SQL Server)](https://go.microsoft.com/fwlink/p/?LinkID=272808), and [Prerequisites, Restrictions, and Recommendations for AlwaysOn Availability Groups (SQL Server)](/sql/database-engine/availability-groups/windows/prereqs-restrictions-recommendations-always-on-availability?view=sql-server-2017).
  
### Reporting Services SharePoint mode
<a name="RSsp"> </a>

SharePoint mode in SQL Server 2012 Reporting Services and SQL Server 2014 Reporting Services is a SharePoint Server 2013 shared service that you configure in either the SharePoint Central Administration website or by using Reporting Services SharePoint mode Microsoft PowerShell cmdlets. For more information, see [PowerShell cmdlets (Reporting Services SharePoint Mode)](/sql/reporting-services/report-server-sharepoint/powershell-cmdlets-for-reporting-services-sharepoint-mode?view=sql-server-2016). SharePoint mode supports SharePoint Server 2013 backup and restore for SQL Server Reporting Services service application and Unified Logging Service (ULS) trace logs. SharePoint mode also supports claims-based authentication. For more information, see the "SharePoint Mode" section of [What's New (Reporting Services)](/previous-versions/sql/sql-server-2012/ms170438(v=sql.110)). For more information about the SharePoint Microsoft PowerShell cmdlets for ULS, see [Logging and events cmdlets in SharePoint 2013](/powershell/module/sharepoint-server/?view=sharepoint-ps).
  
SharePoint mode requires that a report server component of Reporting Services must run within a SharePoint Server farm. This means that a SharePoint application server must exist with the Reporting Services shared service installed and at least one Reporting Services service application.
  
For more information, see [Reporting Services Report Server (SSRS)](https://msdn.microsoft.com/en-us/library/ms157231%28robot,v=sql.115%29.aspx) and [Reporting Services Report Server (SharePoint Mode)](/sql/reporting-services/report-server-sharepoint/reporting-services-report-server-sharepoint-mode?view=sql-server-2016).
  
### Business intelligence features
<a name="BI"> </a>

> [!NOTE]
> SharePoint Foundation 2013 does not support BI features, which require SharePoint Server 2013. 
  
When you install SQL Server 2012 Analysis Services (SSAS) and SQL Server 2012 Reporting Services (SSRS) in a SharePoint Server 2013 farm the following business intelligence features are enabled:
  
- SQL Server 2012 Power Pivot for SharePoint 2013
    
- Power View for SharePoint 2013
    
- Reporting Services interactive report designer that runs on Power Pivot or Analysis Services tabular data models
    
The xVelocity in-memory analytics engine in SQL Server 2012 supports both self-service BI and corporate BI. For more information, see [xVelocity in SQL Server 2012](/previous-versions/sql/sql-server-2012/hh922900(v=sql.110)).
  
For more information, see [Guidance for Using SQL Server BI Features in a SharePoint Farm](https://technet.microsoft.com/en-us/library/hh231680.aspx), [Install SQL Server BI Features with SharePoint 2013 (SQL Server 2012 SP1)](/sql/sql-server/install/guidance-for-using-sql-server-bi-features-in-a-sharepoint-2010-farm?view=sql-server-2014), and [Install SQL Server BI Features with SharePoint (PowerPivot and Reporting Services)](/previous-versions/sql/sql-server-2016/hh231671(v=sql.130)).
  
### Power Pivot for SharePoint 2013
<a name="PP"> </a>

SQL Server 2012 with SP1 is required to deploy Power Pivot for SharePoint 2013. Power Pivot for SharePoint 2013 is a SharePoint Server service application that becomes available when Analysis Services runs in SharePoint mode. This provides a server that hosts Power Pivot data in a SharePoint farm. SQL Server 2012 Analysis Services provides three modes for analysis, Multidimensional, Tabular, and Power Pivot for SharePoint. Note that each server mode is independent of the others, and each supports a type of analytical database that only runs in that modality. For more information about SQL Server 2012 Analysis Services (SSAS), see [Analysis Services](https://go.microsoft.com/fwlink/p/?LinkId=285657). For more information about SQL Server 2014 Analysis Services, see [Analysis Services](/sql/analysis-services/analysis-services?view=sql-server-2014). The server that hosts Power Pivot for SharePoint 2013 can be outside a SharePoint Server 2013 farm.
  
To configure Power Pivot for SharePoint you can use the SharePoint Central Administration website, the Power Pivot for SharePoint 2013 Configuration tool, or Microsoft PowerShell cmdlets. The following table lists each method and describes the process: 
  
|**Power Pivot for SharePoint Configuration method**|**Description**|
|:-----|:-----|
|SharePoint Server 2013 Central Administration  <br/> |Provides all available options to configure the Power Pivot for SharePoint service application.  <br/> |
|Power Pivot for SharePoint 2013 Configuration Tool  <br/> |Evaluates an existing installation and determines what needs to be configured in the SharePoint farm and Power Pivot for SharePoint and then configures everything required.  <br/> |
|Microsoft PowerShell cmdlets  <br/> |Provides cmdlets that you can use to build PowerShell script files (.ps1) and automate the configuration process for Power Pivot for SharePoint.  <br/> |
   
The Power Pivot for SharePoint 2013 add-in enables PowerPivot Gallery, Schedule Data Refresh, and the PowerPivot Management Dashboard in Central Administration. For more information, see [PowerPivot for SharePoint (SSAS)](/sql/analysis-services/power-pivot-sharepoint/power-pivot-for-sharepoint-ssas?view=sql-server-2017).
  
## See also
<a name="sec4"> </a>

#### Other Resources

[Supported Combinations of SharePoint and Reporting Services Components](http://go.microsoft.com/fwlink/?LinkID=524852&amp;clcid=0x409)
  
[What's New (Analysis Services)](/sql/analysis-services/what-s-new-in-analysis-services?view=sql-server-2017)
  
[Features Supported by the Editions of SQL Server 2014](https://go.microsoft.com/fwlink/p/?LinkId=151940)
  
[Deprecated Database Engine Features in SQL Server 2014](https://go.microsoft.com/fwlink/p/?LinkId=157729)

