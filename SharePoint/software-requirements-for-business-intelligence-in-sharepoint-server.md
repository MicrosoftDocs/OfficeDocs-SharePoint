---
title: Software requirements for business intelligence in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: 6824b3bf-9046-4d43-b266-de463d0007e5
---


# Software requirements for business intelligence in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-17* **Summary:** Learn about the minimum software requirements to run business intelligence features in SharePoint Server 2016 and SharePoint Server 2013.The business intelligence tools for SharePoint Server 2016 include the following:
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
    
  
- Microsoft Power Pivot for SharePoint Server 2013
    
  
- Microsoft SQL Server 2012 SP1 Analysis Services (SSAS)
    
  
- Excel Services
    
  
- PerformancePoint Services
    
  
- Visio Services
    
  

## Software requirements for Power Pivot for SharePoint Server 2016
<a name="section1"> </a>

The requirements for Power Pivot for SharePoint Server 2016 are as follows: 
-  [Install Analysis Services in Power Pivot Mode](http://go.microsoft.com/fwlink/?LinkID=808752&amp;clcid=0x409) - in order to use the Excel Online features such as advanced data models on SharePoint Server 2016, an instance of SQL Server 2016 Analysis Services must be installed in Power Pivot mode.
    
  
- Office Online Server with Excel Online must be configured on the farm and at least one Analysis Services server in SharePoint mode must be registered in the Office Online Server configuration. Excel Online can use multiple Analysis Services servers, but they must all use the release version of SQL Server Management Studio (SSMS). For more information, see  [Download SQL Server Management Studio (SSMS)](https://msdn.microsoft.com/en-us/library/mt238290.aspx).
    
  
- Secure Store must be configured on the farm if you want to configure scheduled data refresh of Power Pivot workbooks.
    
  

> [!IMPORTANT:]

  
    
    


## Software requirements for Power Pivot for SharePoint 2013
<a name="section1a"> </a>

The requirements for Power Pivot for SharePoint 2013 are as follows: 
-  [SQL Server 2012 SP1](https://go.microsoft.com/fwlink/p/?LinkID=255906): To be able to use the new Excel 2016 features such as advanced data models on SharePoint Server 2016, an instance of SQL Server 2012 SP1 Analysis Services must be installed in SharePoint deployment mode. 
    
  
- Excel Services must be configured on the farm and at least one Analysis Services server in SharePoint mode must be registered in the Excel Services configuration. Excel Services in SharePoint Server 2013 can use multiple Analysis Services servers, but they must all be SQL 2012 SP1.
    
  
- Secure Store must be configured on the farm if you want to configure scheduled data refresh of PowerPivot workbooks.
    
  

> [!IMPORTANT:]

  
    
    


## Software requirements for Reporting Services on SharePoint Server 2016
<a name="section1a"> </a>

The requirements to run Power View, start Report Builder from SharePoint and view Reporting Services reports on SharePoint Server 2016 are as follows:
-  [Microsoft SQL Server 2016 Reporting Services Add-in for Microsoft SharePoint](https://www.microsoft.com/en-us/download/details.aspx?id=52682): To be able to start Report Builder from SharePoint Server 2016 and for viewing Reporting Services reports from SharePoint Server 2016, an instance of SQL Server 2016 Reporting Services must be installed in SharePoint mode on an application server assigned the MinRole Custom role. Reporting Services doesn't support MinRole and cannot run on application servers that are assigned any other role.
    
  
- To view Power View sheets in Excel Online workbooks on SharePoint Server 2016, SQL Server 2016 Reporting Services and Office Online Server must be configured on the farm and at least one Analysis Services server in SharePoint mode must be registered in the Excel Online configuration. Excel Online can use multiple Analysis Services servers, but they must all be SQL Server 2016.
    
  

## Software requirements for Reporting Services on SharePoint Server 2013
<a name="section1a"> </a>

The requirements to run Power View, start Report Builder from SharePoint and view Reporting Services reports on SharePoint 2013 are as follows: 
-  [SQL Server 2012 SP1](https://go.microsoft.com/fwlink/p/?LinkID=255906): To be able to start Report Builder from SharePoint 2013 and for viewing Reporting Services reports from SharePoint 2013, an instance of SQL Server 2012 SP1 Reporting Services must be installed in SharePoint deployment mode. 
    
  
- To view Power View sheets in Excel 2016 workbooks on SharePoint 2013, Excel Services must be configured on the farm and at least one Analysis Services server in SharePoint mode must be registered in the Excel Services configuration. Excel Services can use multiple Analysis Services servers, but they must all be SQL 2012 SP1. 3.
    
  

> [!NOTE:]

  
    
    


## Software requirements for Excel Online
<a name="section1a"> </a>

The requirements for Excel Online in Office Online Serverfor SharePoint Server 2016 are as follows:
- If you plan to use Excel Online with advanced data models, at least one SQL Server Analysis Services in SharePoint mode must be registered in the Office Online Server configuration. Excel Online can use multiple Analysis Services servers, but they must all use SQL Server Management Studio. For more information, see  [Download SQL Server Management Studio (SSMS)](https://msdn.microsoft.com/library/mt238290.aspx). Note that if you use multiple Analysis Services servers with Excel Online they don't need to be SQL Server 2016.
    
    Configure each computer in your Office Online Server farm as an  [Analysis Services administrator](https://go.microsoft.com/fwlink/p/?LinkId=717498). For more information, see "Configure an Analysis Services (data model) server for Excel Online" in  [Configure Excel Online administrative settings](configure-excel-online-administrative-settings.md#SSAS).
    
  
- The Secure Store Service must be configured in the farm if you want to use a Secure Store target application for data refresh scenarios, or if you want to use an Office Data Connection (ODC) file that specifies a Secure Store target application. For more information, see **Configure Excel Online data refresh by using embedded data connections in Office Online Server** and [Plan the Secure Store Service in SharePoint Server](html/plan-the-secure-store-service-in-sharepoint-server.md). 
    
  
- You can use Kerberos constrained delegation, Secure Store Service, or the EffectiveUserName option for authentication with Excel Online. For more information, see "Windows authentication" in **Data authentication for Excel Online in Office Online Server** and [Configure Analysis Services EffectiveUserName in Excel Online](configure-excel-online-administrative-settings.md#EffectiveUserName).
    
  

> [!NOTE:]

  
    
    

For information about planning for Excel Online, see **Plan Office Online Server**. For information about configuring Excel Online, see **Configure Excel Online administrative settings**.
## Software requirements for Excel Services in SharePoint Server 2013
<a name="section1a"> </a>

The requirements for Excel Services for SharePoint Server 2016 are as follows:
- If you plan to use Excel Services with advanced data models, at least one Analysis Server in SharePoint mode must be registered in the Excel Services configuration. Excel Services can use multiple Analysis Services servers, but they must all be SQL 2012 SP1. 
    
  
- The Secure Store Service must be configured in the farm if you want to store encrypted credentials for data refresh scenarios, or if you want to use the Excel Services unattended service account. For more information, see  [Plan the Secure Store Service in SharePoint Server](html/plan-the-secure-store-service-in-sharepoint-server.md).
    
  
- Kerberos constrained delegation must be configured if you want to delegate user credentials to an external data source for data refresh scenarios.
    
  

> [!NOTE:]

  
    
    

For information about planning for Excel Services, see  [Overview of Excel Services in SharePoint Server 2013](html/overview-of-excel-services-in-sharepoint-server-2013.md). For information about configuring Excel Services, see **Configure Excel Online administrative settings**.
## Software requirements for PerformancePoint Services in SharePoint Server 2016
<a name="section1a"> </a>

The requirements for PerformancePoint Services in SharePoint Server 2016 are as follows:
- ADOMD.net V11
    
  
- Configure a SharePoint Server 2016 managed account for the PerformancePoint Services application pool account. For more information, see  [Configure PerformancePoint Services](html/configure-performancepoint-services.md).
    
  

> [!NOTE:]

  
    
    


> [!NOTE:]

  
    
    

For information about how to plan for and configure PerformancePoint Services, see  [PerformancePoint Services in SharePoint Server 2016 overview](html/performancepoint-services-in-sharepoint-server-2016-overview.md) and [Configure PerformancePoint Services](html/configure-performancepoint-services.md).
## Software requirements for PerformancePoint Services in SharePoint Server 2013
<a name="section1a"> </a>

The requirements for PerformancePoint Services are as follows:
- ADOMD.net V11
    
  
- SQLSERVER2008_ASAMO10
    
  
- Secure Store must be configured in the farm if you want to store encrypted credentials for data refresh scenarios, or if you want to use the PerformancePoint Services unattended service account. For more information, see  [Plan the Secure Store Service in SharePoint Server](html/plan-the-secure-store-service-in-sharepoint-server.md).
    
  
- Kerberos constrained delegation must be configured if you want to delegate user credentials to an external data source for data refresh scenarios.
    
  

> [!NOTE:]

  
    
    


> [!NOTE:]

  
    
    

For information about how to plan for PerformancePoint Services, see  [PerformancePoint Services in SharePoint Server 2016 overview](html/performancepoint-services-in-sharepoint-server-2016-overview.md). For information about how to configure PerformancePoint Services, see  [Configure PerformancePoint Services](html/configure-performancepoint-services.md).
## Software requirements for Visio Services in SharePoint
<a name="section1a"> </a>

The requirements for Visio Services in SharePoint are as follows:
- Secure Store must be configured in the farm if you want to store encrypted credentials for data refresh scenarios. For more information, see  [Plan the Secure Store Service in SharePoint Server](html/plan-the-secure-store-service-in-sharepoint-server.md).
    
  
- Kerberos constrained delegation must be configured if you want to delegate user credentials to an external data source for data refresh scenarios.
    
  
For information about how to plan for Visio Services, see  [Overview of Visio Services in SharePoint Server](html/overview-of-visio-services-in-sharepoint-server.md). For information about how to configure Visio Services, see  [Configure Visio Services](html/configure-visio-services.md).
# See also

#### 

 [SQL Server 2016 with SP1](https://www.microsoft.com/en-us/evalcenter/evaluate-sql-server-2016)
  
    
    
 [SQL 2012 SP1 Installation](https://go.microsoft.com/fwlink/p/?LinkID=255906)
  
    
    
 [Deploying SQL Server 2016 PowerPivot and Power View in SharePoint 2016](http://go.microsoft.com/fwlink/p/?LinkID=717977&amp;clcid=0x409)
  
    
    
 [Deploying SQL Server 2016 PowerPivot and Power View in a Multi-Tier SharePoint 2016 Farm](http://go.microsoft.com/fwlink/p/?LinkID=723106&amp;clcid=0x409)
  
    
    

  
    
    

