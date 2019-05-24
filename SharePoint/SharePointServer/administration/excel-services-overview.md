---
title: "Overview of Excel Services in SharePoint Server 2013"
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 6/23/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: fe776cf2-17a4-4bb6-95ea-66288f243a93
description: "Excel Services is a business intelligence tool in SharePoint Server that allows you to share data-connected workbooks across an organization."
---

# Overview of Excel Services in SharePoint Server 2013

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)]
  
Excel Services is a shared service that you can use to publish Excel workbooks on SharePoint Server 2013. The published workbooks can be managed and secured according to your organizational needs and shared among SharePoint Server 2013 users, who can render the workbooks in a browser. Excel Services is available only in the Enterprise edition of SharePoint Server 2013.
  
Excel Services is used primarily for business intelligence scenarios. Excel workbooks can be connected to external data sources, reports created, and then the workbook can be published to a SharePoint document library. When a user opens the workbook from the the document library, it is rendered in the browser by using Excel Services. The external data connection is maintained and the data is refreshed if necessary. This allows broad sharing of reports throughout an organization.
  
Excel Services consists of Excel Calculation Services, the Excel Web Access Web Part, and Excel Web Services for programmatic access. It supports sharing, securing, managing, and using Excel workbooks in a browser by providing the following: 
  
- Global settings for managing workbooks, which include settings for security, load balancing, session management, memory utilization, workbook caches, and external data connections.
    
- Trusted file locations (which allow you to define which document libraries are trusted by Excel Services) together with session management, workbook size, calculation behavior, and external data settings of workbooks stored in those locations.
    
- An extensive list of trusted data providers for connecting to your data, plus the ability to add your own trusted data provider.
    
- Trusted data connection libraries, which allow you to define which data connection libraries in your farm are trusted by Excel Services.
    
- The ability to add your own user-defined function assemblies.
    
While users can interact with Excel workbooks in a browser through Excel Services, the workbooks cannot be edited in the browser by using Excel Services. Programmatic options are available.
  
Looking at several specific scenarios can help you understand how best to take advantage of Excel Services:
  
- **Sharing workbooks** Users can save Excel workbooks to a SharePoint Server document library to give other users browser-based access to the server-calculated version of the workbook. When the workbook is accessed, Excel Services loads the workbook, refreshes the external data if it is necessary, calculates it if it is necessary, and sends the resulting output view back through the browser. A user can interact with Excel-based data by sorting, filtering, expanding, or collapsing PivotTables, and by passing in parameters. This provides the ability to perform analysis on published workbooks. A user does not have to have Excel installed to view the workbook. Users will always view the latest version of a workbook, and they can interact with it in a browser. Security permissions can be set to limit what access is provided to which user. 
    
- **Building business intelligence (BI) dashboards** Browser-based dashboards can be created by using Excel and Excel Services together with the Excel Web Access Web Part. PerformancePoint Services can also use Excel Services workbooks as a data source. 
    
- **Reuse of logic encapsulated in Excel workbooks in custom applications** Besides a browser-based interface with the server, Excel Services provides a Web-service-based interface so that a published workbook can be accessed programmatically by any application that uses Web services. The Web service applications can change values, calculate the workbook, and retrieve some or all of the updated workbook by using that interface according to what security permissions are set for the published workbook. 
    
- **Report Building** One of the most useful features of Excel Services is report building. By publishing data-connected workbooks to a SharePoint document library and making them available through Excel Services, you can make reports that you have created in Excel available to others in your organization. Instead of multiple users having separate copies of the workbooks on their computers, the workbooks can be created and changed by a trusted author in a central location that is trusted by Excel Services. The correct version of the worksheet is easier to find, share, and use from Excel, SharePoint Server, and other applications. 
    
## Farms using Office Web Apps Server

If your SharePoint Server farm has been integrated with Office Web Apps Server and Excel Web App, the features available in Excel Services will depend on how Excel Web App has been configured.
  
Excel Web App runs in one of two modes:
  
- **SharePoint view mode** In this mode, Excel Services is used to view workbooks in the browser. 
    
- **Office Web Apps Server view mode** In this mode, Excel Web App is used to view workbooks in the browser. 
    
The following table lists the business intelligence features available in Excel Services in each mode.
  
**BI features in Excel Services, by mode**

||**SharePoint Server only**|**SharePoint Server with Excel Web App (SharePoint view mode)**|**SharePoint Server with Excel Web App (Office Web Apps Server view mode)**|
|:-----|:-----|:-----|:-----|
|Excel Web Access Web Part  <br/> |×  <br/> |×  <br/> ||
|Refresh OData connections  <br/> |×  <br/> |×  <br/> ||
|View and interact with Power View reports  <br/> |×  <br/> |×  <br/> ||
|View and interact with Power Pivot data models  <br/> |×  <br/> |×  <br/> ||
|Refresh Power Pivot data models  <br/> |×  <br/> |×  <br/> ||
|Refresh data by using the Excel Services unattended service account  <br/> |×  <br/> |×  <br/> ||
|Refresh data by using Secure Store and Windows credentials  <br/> |×  <br/> |×  <br/> |×  <br/> |
|Refresh data by using Effective User Name connections  <br/> |×  <br/> |×  <br/> ||
|Kerberos delegation  <br/> |×  <br/> |×  <br/> ||
   
## See also

#### Concepts

  
[Business intelligence capabilities in Excel Service (SharePoint Server 2013)](bi-capabilities-in-excel-and-excel-services.md)

