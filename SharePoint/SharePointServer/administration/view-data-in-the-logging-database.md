---
title: "View data in the logging database in SharePoint Server"
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.date: 5/30/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: c5c6fd31-d747-49c0-9784-b4f29bd82809
description: "Learn about the SharePoint logging database, how to view monitoring information, use custom SQL views, and export into Excel."
---

# View data in the logging database in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
- [Introduction to the SharePoint logging database](#section1)
    
- [Pre-defined SQL views in the SharePoint logging database](#section2)
    
- [Custom SQL views in the SharePoint logging database](#section3)
    
> [!NOTE]
>  Because SharePoint Server 2016 runs as websites in Internet Information Services (IIS), administrators and users depend on the accessibility features that browsers provide. SharePoint Server 2016 supports the accessibility features of supported browsers. For more information, see the following resources: > [Plan browser support](https://go.microsoft.com/fwlink/p/?LinkId=246502)> [Accessibility features in SharePoint Products](https://go.microsoft.com/fwlink/p/?LinkId=246501)> [Keyboard shortcuts](https://go.microsoft.com/fwlink/p/?LinkID=246504)> [Touch](https://go.microsoft.com/fwlink/p/?LinkId=246506)
  
## Introduction to the SharePoint logging database
<a name="section1"> </a>

To monitor servers that are running SharePoint Server 2016 and the services that run on the servers, you can directly access various logs such as the Windows Server event logs, SharePoint Unified Logging Service (ULS) logs (also known as trace logs), or usage data logs. You can also go to SharePoint Server 2016the SharePoint Central Administration website to review various reports. SharePoint Health Analyzer reports contain rules for servers or services. Administration (diagnostics) reports contain search-related information. Web Analytics reports contain web analytics metrics. For more information about reports, see [View reports and logs in SharePoint Server 2016](view-reports-and-logs.md).
  
All the monitoring methods mentioned previously have limits. For example, Windows Server event logs, SharePoint ULS logs, and usage data logs are not stored in one single place. You have to go to different places to find related logs. Similarly, although reports from Central Administration contain the most frequently used metrics and monitoring information, if you want to add more monitoring information to those reports, you cannot do it because these reports are pre-defined and cannot be changed. 
  
You can increase monitoring efficiency by using the logging database in SharePoint Server 2016. The logging database is a farm-wide repository of SharePoint Server 2016 monitoring information from every server in the farm. The logging database provides the option to view and customize various monitoring information in one place. Moreover, the logging database is the only SharePoint Server 2016 database for which you can customize reports by directly changing the database. 
  
> [!NOTE]
> For more information about SharePoint Server 2016 databases, see [Database types and descriptions in SharePoint Server](../technical-reference/database-types-and-descriptions.md). 
  
> [!NOTE]
> The default name of the database is **SharePoint_Logging**. You can change the default name and the SharePoint database server location by using Microsoft PowerShell. For more information about the logging database name and database server location, see [Configure usage and health data collection in SharePoint Server](configure-usage-and-health-data-collection.md). 
  
A single place that stores various monitoring information helps you efficiently monitor SharePoint Server 2016 servers and services. More importantly, you can create your own reports for unique monitoring, reporting and troubleshooting requirement based on tables inside the logging database. This article describes how to create reports by using existing tables and views. You might want to write your own providers to create new tables. 
  
> [!NOTE]
> A SQL view is a virtual table. One difference between a table and a SQL view is that you can modify the data inside a table but you cannot modify the data inside a SQL view. 
  
You use SharePoint Server 2016 Central Administration to configure logs imported into the logging database. For more information about how to configure log categories, log levels, and trace (ULS) log path, see [Configure diagnostic logging in SharePoint Server](configure-diagnostic-logging.md). For more information about how to enable what is written into the logging database, see [Configure usage and health data collection in SharePoint Server](configure-usage-and-health-data-collection.md). For more information about how to specify the logging database server, name and database authentication information, the events to be written to the logging database, and the frequency that logs are written to the logging database (that is, timer jobs related to usage database importing), see [Configure SharePoint Health Analyzer timer jobs in SharePoint Server 2016](configure-sharepoint-health-analyzer-timer-jobs.md). 
  
The procedures in this article use SQL Server Management Studio to access the logging database. Management Studio is a component of SQL Server 2008.
  
> [!NOTE]
> To access the logging database, you have to have either Windows authentication (recommended) or SQL authentication. The database authentication information is configured in SharePoint Server 2016Central Administration. For more information about authentication methods, see [Configure usage and health data collection in SharePoint Server](configure-usage-and-health-data-collection.md). 
  
## Pre-defined SQL views in the SharePoint logging database
<a name="section2"> </a>

This section describes partition tables and SQL views inside the SharePoint Server 2016 logging database, and includes the following three procedures:
  
- To access the logging database by using SQL Server Management Studio
    
- To view the logging information from default views
    
- To export to and view the logging data by using Excel
    
The logging database uses a separate partition table for the daily data for each category. For example, the timer job usage data for the first day is written to the **dbo.TimerJobUsage_Partition0** table and the data for 32 days later is written to the **dbo.TimerJobUsageUsage_Partition31** table. Logs within one day are written to one partition table. That means, for each log category, each partition table stores one particular day's logs. 
  
> [!NOTE]
> The mapping between one partition table and the exact date depends on the logging database retention period and the starting date to write logs into the logging database. You can get the mapping by observing time information inside each table. For example, if the retention period is 14 days and today's logs are written to partition table 2, tomorrow's logs will be written into partition table 3 and so on. After 14 days, all logs are deleted and new logs are written to these partition tables starting from partition table 0. 
  
You can use the pre-defined SQL views in Management Studio to view all monitoring information in one place. Each pre-defined view collects the data from all 32 partition tables for the specific log category. For example, you can view the monitoring information in 32 tables from **dbo.TimerJobUsage_Partition0** to **dbo.TimerJobUsageUsage_Partition31**. 
  
To access the pre-defined views, you must access the SharePoint Server 2016 logging database. Then from the logging database, you view the monitoring information.
  
 **To access the logging database by using Management Studio**
  
1. Verify that the user account that is performing this procedure has the **db_owner** fixed database role. 
    
2. On the taskbar, click **Start**, point to **All Programs**, click **Microsoft SQL Server 2008** or the latest Microsoft SQL Server version that is installed, and then click **SQL Server Management Studio**.
    
    > [!NOTE]
    > If you do not have Management Studio on the server, reinstall SQL Server 2008 and add the Management Studio component. For more information, see [SQL Server Install](https://go.microsoft.com/fwlink/p/?LinkId=237482). 
  
3. In the **Connect to Server** dialog box, choose **Database Engine**. Then specify the server name, for example, ServerName\SharePoint. Select the authentication type ( **Windows Authentication** or **SQL Server Authentication**) that you configured through SharePoint Server 2016Central Administration. If it is **SQL Server Authentication**, specify the credentials for the database administrator. After the information is set, click **Connect**. 
    
4. Switch to the **Object Explorer** view by clicking **View**, and then clicking **Object Explorer**. Expand **Databases** to see the logging database that has default name **SharePoint_Logging** or a name that you configured in Central Administration. 
    
5. Optionally, expand the logging database to see tables and views.
    
 **To view the logging information from default views**
  
1. Verify that the user account that is performing this procedure has the **db_owner** fixed database role. 
    
2. In Management Studio, go to the logging database node by using the previous procedure.
    
3. Expand the **Views** node of the database to see the default views. Right-click the view — for example **dbo.RequestUsage**, and choose **Select Top 1000 Rows**.
    
    The operation **Select Top 1000 Rows** is the following T-SQL query script: 
    
  ```
  /****** Script for SelectTopNRows command from SSMS ******/
  SELECT TOP 1000 [PartitionId]
        ,[RowId]
        ,[LogTime]
        ,[MachineName]
        ,[FarmId]
        ,[SiteSubscriptionId]
        ,[UserLogin]
        ,[CorrelationId]
        ,[WebApplicationId]
        ,[ServerUrl]
        ,[SiteId]
        ,[SiteUrl]
        ,[WebId]
        ,[WebUrl]
        ,[DocumentPath]
        ,[ContentTypeId]
        ,[QueryString]
        ,[BytesConsumed]
        ,[HttpStatus]
        ,[SessionId]
        ,[ReferrerUrl]
        ,[ReferrerQueryString]
        ,[Browser]
        ,[UserAgent]
        ,[UserAddress]
        ,[RequestCount]
        ,[QueryCount]
        ,[QueryDurationSum]
        ,[ServiceCallCount]
        ,[ServiceCallDurationSum]
        ,[OperationCount]
        ,[Duration]
        ,[RequestType]
        ,[Title]
        ,[RowCreatedTime]
    FROM [SharePoint_Logging].[dbo].[RequestUsage]
  ```

    The top 1000 rows of the table category **Request Usage** appear in the result window. 
    
4. You can modify the T-SQL query in the SQL editor window. For example, if there are more than 1000 rows in the tables, you might want to view the top 5000 rows. To do that, change the script by replacing "SELECT TOP 1000" with "SELECT TOP 5000", and then click **Execute**.
    
If you want to view logs by using tools other than Management Studio, you can extract the monitoring information from the views and save as a text file or a CSV file. In the following procedure, Excel is used as an example. 
  
 **To export and view the logging data by using Excel**
  
1. Verify that the user account that is performing this procedure has the **db_owner** fixed database role. 
    
2. In Management Studio, go to the logging database node.
    
3. Expand the **Views** node, right-click the view from which you want to extract data, and then click **Select Top 1000 Rows**.
    
4. In the result window, right-click, and then click **Select All**. Then right-click and then click **Save Results As…**.
    
5. In the **Save Grid Results** window, specify the folder in which you want to save the file, specify the **Save as type** as CSV(Comma delimited), and then specify an appropriate file name. 
    
6. Open the CSV file by double-clicking it in Excel.
    
## Custom SQL views in the SharePoint logging database
<a name="section3"> </a>

The logging database in SharePoint Server 2016 enables you to create custom reports in two ways. You can generate new views by combining related information from existing tables, or you can write providers to generate new partition tables inside the logging database. The examples in this section only show the first way. 
  
In usage tables and the ULSTraceLog tables, the **CorrelationId** is an important parameter for troubleshooting. This is because every error message contains a unique **CorrelationId**. **CorrelationId** is a GUID that links all the related information with respect to a request. The following procedure shows how to make a custom view that links multiple log categories by using the **CorrelationId**.
  
 **To create a custom SQL view that uses existing tables**
  
1. Verify that the user account that is performing this procedure has the **db_owner** fixed database role. 
    
2. In Management Studio, go to the logging database node.
    
3. In the logging database, expand the **Views** node. Choose one of the views for which you want to collect information. Right-click the view, and then click **New View**.
    
4. In the **Add Table** window, choose the tables to add. For example, if you want to obtain information about feature usage site requests for a single day, you can add **dbo.FeatureUsage_Partion1** and **dbo.RequestUsage_Partion1**.
    
    The T-SQL query automatically inner joins the unique key **PartionId** in these two tables. 
    
  ```
  SELECT     
  FROM   dbo.FeatureUsage_Partition1 INNER JOIN
      dbo.RequestUsage_Partition1 ON dbo.FeatureUsage_Partition1.PartitionId = dbo.RequestUsage_Partition1.PartitionId
  
  ```

5. Disjoin the two tables by right-clicking the link between these tables and selecting **removing**.
    
6. To inner join the two tables using **CorrelationId**, click the **CorrelationId** column in one table and move the pointer to the **CorrelationId** column in another table. Or you can modify the SQL query directly from the Query Editor. 
    
  ```
  SELECT  
  FROM   dbo.FeatureUsage_Partition1 INNER JOIN
      dbo.RequestUsage_Partition1 ON dbo.FeatureUsage_Partition1.CorrelationId = dbo.RequestUsage_Partition1.CorrelationId 
  
  ```

7. Choose the columns in each table that you want to show in the new view.
    
8. Right-click and choose **Execute SQL**. The results appear in the result window.
    
## See also
<a name="section3"> </a>

#### Concepts

[View reports and logs in SharePoint Server 2016](view-reports-and-logs.md)
  
[Overview of monitoring in SharePoint Server](monitoring-overview.md)

