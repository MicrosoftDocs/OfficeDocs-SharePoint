---
title: "Software requirements for business intelligence in SharePoint Server"
ms.author: stevhord
author: bentoncity
manager: pamgreen
ms.date: 2/15/2018
ms.audience: ITPro
ms.topic: article
ms.prod: office-online-server
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.custom: Strat_SP_server
ms.assetid: 6824b3bf-9046-4d43-b266-de463d0007e5
description: "Summary: Learn about the minimum software requirements to run business intelligence features in SharePoint Server 2016 and SharePoint Server 2013."
---

# Software requirements for business intelligence in SharePoint Server

 **Summary:** Learn about the minimum software requirements to run business intelligence features in SharePoint Server 2016 and SharePoint Server 2013. 
  
The business intelligence tools for SharePoint Server 2016 include the following:
  
- Microsoft Power View for SharePoint Server 2016
    
- Microsoft SQL Server 2016 Reporting Services (SSRS)
    
- Microsoft Power Pivot for SharePoint Server 2016
    
- Microsoft SQL Server 2016 Analysis Services (SSAS)
    
- Office Online Server for Excel Online
    
- PerformancePoint Services
    
- Visio Services
    
The business intelligence tools for SharePoint Server 2013 include the following:
  
- Microsoft Power View for SharePoint 2013
    
- Microsoft SQL Server 2012 Reporting Services for SharePoint
    
- Microsoft Power Pivot for SharePoint 2013
    
- Microsoft SQL Server 2012 SP1 Analysis Services (SSAS)
    
- Excel Services
    
- PerformancePoint Services
    
- Visio Services
    
## Software requirements for Power Pivot for SharePoint Server 2016
<a name="section1"> </a>

The requirements for Power Pivot for SharePoint Server 2016 are as follows: 
  
- [Install Analysis Services in Power Pivot Mode](http://go.microsoft.com/fwlink/?LinkID=808752&amp;clcid=0x409) - in order to use the Excel Online features such as advanced data models on SharePoint Server 2016, an instance of SQL Server 2016 Analysis Services must be installed in Power Pivot mode. 
    
- Office Online Server with Excel Online must be configured on the farm and at least one Analysis Services server in SharePoint mode must be registered in the Office Online Server configuration. Excel Online can use multiple Analysis Services servers, but they must all use the release version of SQL Server Management Studio (SSMS). For more information, see [Download SQL Server Management Studio (SSMS)](https://go.microsoft.com/fwlink/?linkid=857511).
    
- Secure Store must be configured on the farm if you want to configure scheduled data refresh of Power Pivot workbooks.
    
> [!IMPORTANT]
> For SharePoint Server 2016, Power Pivot for SharePoint 2013 must be installed from SQL Server 2016. 
  
## Software requirements for Power Pivot for SharePoint 2013
<a name="section1a"> </a>

The requirements for Power Pivot for SharePoint 2013 are as follows: 
  
- [SQL Server 2012 SP1](https://go.microsoft.com/fwlink/p/?LinkID=255906): To be able to use the new Excel 2016 features such as advanced data models on SharePoint Server 2016, an instance of SQL Server 2012 SP1 Analysis Services must be installed in SharePoint deployment mode. 
    
- Excel Services must be configured on the farm and at least one Analysis Services server in SharePoint mode must be registered in the Excel Services configuration. Excel Services in SharePoint Server 2013 can use multiple Analysis Services servers, but they must all be SQL 2012 SP1.
    
- Secure Store must be configured on the farm if you want to configure scheduled data refresh of PowerPivot workbooks.
    
> [!IMPORTANT]
> For SharePoint Server 2016, Power Pivot for SharePoint 2013 must be installed from either SQL Server 2012 SP1 setup or the SQL Server 2012 SP1 Feature Pack web page. 
  
## Software requirements for Reporting Services on SharePoint Server 2016
<a name="section1a"> </a>

The requirements to run Power View, start Report Builder from SharePoint and view Reporting Services reports on SharePoint Server 2016 are as follows:
  
- [Microsoft SQL Server 2016 Reporting Services Add-in for Microsoft SharePoint](https://go.microsoft.com/fwlink/?linkid=857537): To be able to start Report Builder from SharePoint Server 2016 and for viewing Reporting Services reports from SharePoint Server 2016, an instance of SQL Server 2016 Reporting Services must be installed in SharePoint mode on an application server assigned the MinRole Custom role. Reporting Services doesn't support MinRole and cannot run on application servers that are assigned any other role.
    
- To view Power View sheets in Excel Online workbooks on SharePoint Server 2016, SQL Server 2016 Reporting Services and Office Online Server must be configured on the farm and at least one Analysis Services server in SharePoint mode must be registered in the Excel Online configuration. Excel Online can use multiple Analysis Services servers, but they must all be SQL Server 2016.
    
## Software requirements for Reporting Services on SharePoint Server 2013
<a name="section1a"> </a>

The requirements to run Power View, start Report Builder from SharePoint and view Reporting Services reports on SharePoint 2013 are as follows: 
  
- [SQL Server 2012 SP1](https://go.microsoft.com/fwlink/p/?LinkID=255906): To be able to start Report Builder from SharePoint 2013 and for viewing Reporting Services reports from SharePoint 2013, an instance of SQL Server 2012 SP1 Reporting Services must be installed in SharePoint deployment mode. 
    
- To view Power View sheets in Excel 2016 workbooks on SharePoint 2013, Excel Services must be configured on the farm and at least one Analysis Services server in SharePoint mode must be registered in the Excel Services configuration. Excel Services can use multiple Analysis Services servers, but they must all be SQL 2012 SP1. 3.
    
> [!NOTE]
> The Report Viewer component is no longer needed. The SQL Server 2012 SP1. Reporting Services in SharePoint deployment mode includes all of the web-front-end components required. 
  
## Software requirements for Excel Online
<a name="section1a"> </a>

The requirements for Excel Online in Office Online Server for SharePoint Server 2016 are as follows:
  
- If you plan to use Excel Online with advanced data models, at least one SQL Server Analysis Services in SharePoint mode must be registered in the Office Online Server configuration. Excel Online can use multiple Analysis Services servers, but they must all use SQL Server Management Studio. For more information, see [Download SQL Server Management Studio (SSMS)](https://go.microsoft.com/fwlink/?linkid=857511). Note that if you use multiple Analysis Services servers with Excel Online they don't need to be SQL Server 2016.
    
    Configure each computer in your Office Online Server farm as an [Analysis Services administrator](https://go.microsoft.com/fwlink/p/?LinkId=717498). For more information, see "Configure an Analysis Services (data model) server for Excel Online" in [Configure Excel Online administrative settings](http://technet.microsoft.com/library/9cb81758-9d0b-4970-9ca0-a75eedf6093b.aspx#SSAS).
    
- The Secure Store Service must be configured in the farm if you want to use a Secure Store target application for data refresh scenarios, or if you want to use an Office Data Connection (ODC) file that specifies a Secure Store target application. For more information, see [Configure Excel Online data refresh by using embedded data connections in Office Online Server](http://technet.microsoft.com/library/9a78496b-50c0-471c-b112-6dbc7231635d.aspx) and [Plan the Secure Store Service in SharePoint Server](http://technet.microsoft.com/library/e1196de0-1eb9-4c50-aeca-93e0eba7be0d%28Office.14%29.aspx). 
    
- You can use Kerberos constrained delegation, Secure Store Service, or the EffectiveUserName option for authentication with Excel Online. For more information, see "Windows authentication" in [Data authentication for Excel Online in Office Online Server](http://technet.microsoft.com/library/7ced238b-2866-4961-af1c-6b597a55ce7a.aspx) and [Configure Analysis Services EffectiveUserName in Excel Online](http://technet.microsoft.com/library/9cb81758-9d0b-4970-9ca0-a75eedf6093b.aspx#EffectiveUserName).
    
> [!NOTE]
> For Analysis Services data, the EffectiveUserName option is an alternative method of accessing data. When it is enabled, all connections to Analysis Services data for individual users will be made by using the EffectiveUserName connection string property instead of Windows delegation. For more information, see "Configure Analysis Services EffectiveUserName in Excel Online in [Configure Excel Online administrative settings](http://technet.microsoft.com/library/9cb81758-9d0b-4970-9ca0-a75eedf6093b.aspx#EffectiveUserName). 
  
For information about planning for Excel Online, see [Plan Office Online Server](http://technet.microsoft.com/library/2e147f11-6f47-46bc-90bf-b2f179958d11.aspx). For information about configuring Excel Online, see [Configure Excel Online administrative settings](http://technet.microsoft.com/library/9cb81758-9d0b-4970-9ca0-a75eedf6093b.aspx).
  
## Software requirements for Excel Services in SharePoint Server 2013
<a name="section1a"> </a>

The requirements for Excel Services for SharePoint Server 2016 are as follows:
  
- If you plan to use Excel Services with advanced data models, at least one Analysis Server in SharePoint mode must be registered in the Excel Services configuration. Excel Services can use multiple Analysis Services servers, but they must all be SQL Server 2012 SP1 Analysis Services (SSAS). 
    
- The Secure Store Service must be configured in the farm if you want to store encrypted credentials for data refresh scenarios, or if you want to use the Excel Services unattended service account. For more information, see [Plan the Secure Store Service in SharePoint Server](http://technet.microsoft.com/library/e1196de0-1eb9-4c50-aeca-93e0eba7be0d%28Office.14%29.aspx).
    
- Kerberos constrained delegation must be configured if you want to delegate user credentials to an external data source for data refresh scenarios.
    
> [!NOTE]
> For Analysis Services data, the EffectiveUserName option is an alternative method of accessing data. When it is enabled, all connections to Analysis Services data for individual users will be made by using the EffectiveUserName connection string property instead of Windows delegation. For more information, see [Use Analysis Services EffectiveUserName in SharePoint Server](use-analysis-services-effectiveusername-in-sharepoint-server.md). 
  
For information about planning for Excel Services, see [Overview of Excel Services in SharePoint Server 2013](excel-services-overview.md). For information about configuring Excel Services, see [Configure Excel Services in SharePoint Server 2013](http://technet.microsoft.com/library/9cb81758-9d0b-4970-9ca0-a75eedf6093b.aspx).
  
## Software requirements for PerformancePoint Services in SharePoint Server 2016
<a name="section1a"> </a>

The requirements for PerformancePoint Services in SharePoint Server 2016 are as follows:
  
- ADOMD.net V11
    
- Configure a SharePoint Server 2016 managed account for the PerformancePoint Services application pool account. For more information, see [Configure PerformancePoint Services](configure-performancepoint-services.md).
    
> [!NOTE]
> For Analysis Services data, the EffectiveUserName option is an alternative method of accessing data. When enabled, all connections to Analysis Services data for individual users will be made using the EffectiveUserName connection string property instead of Windows delegation. 
  
> [!NOTE]
> ADOMD.net V11 is not installed as part of the SharePoint Server 2016 prerequisite installer tool. Install ADOMD.NET from the [SQL Server 2012 Feature Pack](https://go.microsoft.com/fwlink/p/?LinkId=275448). However, if you are installing the SQL Server 2016 Reporting Services in SharePoint mode on your application server, this file is included. 
  
For information about how to plan for and configure PerformancePoint Services, see [PerformancePoint Services in SharePoint Server 2016 overview](http://technet.microsoft.com/library/0bcc4cd8-68cf-45b5-a880-d56fdaabe284%28Office.14%29.aspx) and [Configure PerformancePoint Services](configure-performancepoint-services.md).
  
## Software requirements for PerformancePoint Services in SharePoint Server 2013
<a name="section1a"> </a>

The requirements for PerformancePoint Services are as follows:
  
- ADOMD.net V11
    
- SQLSERVER2008_ASAMO10
    
- Secure Store must be configured in the farm if you want to store encrypted credentials for data refresh scenarios, or if you want to use the PerformancePoint Services unattended service account. For more information, see [Plan the Secure Store Service in SharePoint Server](http://technet.microsoft.com/library/e1196de0-1eb9-4c50-aeca-93e0eba7be0d%28Office.14%29.aspx).
    
- Kerberos constrained delegation must be configured if you want to delegate user credentials to an external data source for data refresh scenarios.
    
> [!NOTE]
> For Analysis Services data, the EffectiveUserName option is an alternative method of accessing data. When enabled, all connections to Analysis Services data for individual users will be made using the EffectiveUserName connection string property instead of Windows delegation. 
  
> [!NOTE]
> ADOMD.net V11 is not installed as part of the SharePoint 2013 prerequisite installer tool. However, if you are installing the SQL Server 2012 Reporting Services SQL Server 2012 Reporting Services in SharePoint 2013 mode on your application server, this file is included. 
  
For information about how to plan for PerformancePoint Services, see [PerformancePoint Services in SharePoint Server 2016 overview](http://technet.microsoft.com/library/0bcc4cd8-68cf-45b5-a880-d56fdaabe284%28Office.14%29.aspx). For information about how to configure PerformancePoint Services, see [Configure PerformancePoint Services](configure-performancepoint-services.md).
  
## Software requirements for Visio Services in SharePoint
<a name="section1a"> </a>

The requirements for Visio Services in SharePoint are as follows:
  
- Secure Store must be configured in the farm if you want to store encrypted credentials for data refresh scenarios. For more information, see [Plan the Secure Store Service in SharePoint Server](http://technet.microsoft.com/library/e1196de0-1eb9-4c50-aeca-93e0eba7be0d%28Office.14%29.aspx).
    
- Kerberos constrained delegation must be configured if you want to delegate user credentials to an external data source for data refresh scenarios.
    
For information about how to plan for Visio Services, see [Overview of Visio Services in SharePoint Server](http://technet.microsoft.com/library/9e952b26-fb0e-48a5-89b1-054f54f9b986%28Office.14%29.aspx). For information about how to configure Visio Services, see [Configure Visio Services](configure-visio-services.md).
  
## See also
<a name="section1a"> </a>

#### Other Resources

[SQL Server 2016 with SP1](https://go.microsoft.com/fwlink/?linkid=857522)
  
[SQL 2012 SP1 Installation](https://go.microsoft.com/fwlink/p/?LinkID=255906)
  
[Deploying SQL Server 2016 PowerPivot and Power View in SharePoint 2016](http://go.microsoft.com/fwlink/p/?LinkID=717977&amp;clcid=0x409)
  
[Deploying SQL Server 2016 PowerPivot and Power View in a Multi-Tier SharePoint 2016 Farm](http://go.microsoft.com/fwlink/p/?LinkID=723106&amp;clcid=0x409)

