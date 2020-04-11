---
title: "Data sources supported in Excel Services (SharePoint Server 2013)"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 6/23/2017
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: db4bea29-65fb-4c48-828a-f96502fed697
description: "Learn about different kinds of data sources that you can use in Excel and Excel Services."
---

# Data sources supported in Excel Services (SharePoint Server 2013)

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)]
  
You can bring data into Excel using lots of data sources and connections. Many, but not all, of the data connections that you can use in Excel are supported in Excel Services. In addition, if your organization is using Office Web Apps Server, some data sources that you can use in Excel are not supported in Excel Web App.
  
At a high level, the following table summarizes the Excel data sources that are supported in Excel Services (as part of SharePoint Server 2013) and Excel Web App (as part of Office Web Apps Server).
  
**Table: Summary of Excel data sources that are supported in Excel Services and Excel Web App**

|**Excel data source**|**Supported in Excel Services?**|**Supported in Excel Web App?**|
|:-----|:-----|:-----|
|SQL Server tables  <br/> |Yes  <br/> |Yes, if the environment is configured to use Secure Store Service or an unattended service account.  <br/> |
|SQL Server Analysis Services cubes  <br/> |Yes  <br/> |Yes, if the environment is configured to use Secure Store Service or an unattended service account.  <br/> |
|OLE DB or ODBC data source  <br/> |Yes, as long as the connection string contains a user name and password for the connection.  <br/> |Yes, as long as the connection string contains a user name and password for the connection.  <br/> |
|Data model that was created by using Excel  <br/> |Yes, provided Excel Services is configured to use an instance of SQL Server Analysis Services for data models.  <br/> |No  <br/> |
|Azure Marketplace data  <br/> |No  <br/> |No  <br/> |
|OData data  <br/> |No  <br/> |No  <br/> |
|XML data  <br/> |No  <br/> |No  <br/> |
|Access data  <br/> |No  <br/> |No  <br/> |
|Data from a text file  <br/> |No  <br/> |No  <br/> |
   
The following sections contain more detailed information about how to work with data in Excel and Excel Services.
  
 **In this article**
  
- [Working with external data in Excel ](#part1)
    
- [External data connections that are supported in Excel Services in SharePoint Server ](#part2)
    
- [External data connections that are supported in a SharePoint environment that includes Office Web Apps Server ](#part3)
    
- [Working with data models in Excel Services](#part4)
    
- [Working with native data in Excel Services](#part5)
    
## Working with external data in Excel
<a name="part1"> </a>

In Excel 2016, you can connect to lots of data sources. These include the following:
  
- SQL Server tables
    
- SQL Server Analysis Services cubes
    
- Azure Marketplace data
    
- OData data
    
- XML data
    
- Access data
    
- Text file data
    
To bring data into Excel, you can use existing connections, or you can create your own connections. Existing connections can be stored on your computer or in a central location, such as a SharePoint site.
  
Ideally, you'll have access to a set of existing data connections in a site, such as a Business Intelligence Center site, that you can use to work with data in Excel. This is especially helpful if you plan to publish a workbook to a documents library in a Business Intelligence Center site. Typically, a SharePoint administrator configures such locations as trusted locations in Excel Services. This makes it possible for you and others to refresh data in your workbooks to view the most current information. 
  
 **To use an existing data connection in Excel**
  
1. In Excel, on the **Data** tab, choose **Existing Connections**.
    
2. Choose **Browse for More** to open the **Select a Data Source** dialog box. 
    
3. Specify the location of the data source that you want to use, select the data source, and then choose **Open**.
    
4. On the **Import Data** page, choose how you want to view the data, and then choose **OK**. 
    
    The options that are available depend on the particular data source that you are using. For example, you might choose to create a data table, a PivotChart report, a PivotTable report, or a Power View sheet.
    
If you do not have an existing connection or you want to create a new connection, you can easily do this in Excel. You'll typically have to know the name of the location (such as a server or a website) where the data is stored and what authentication method that you should use to connect to the data. For example, to create a connection to a table that is stored in SQL Server, you must know the name of the server, the database, and table that you want to use, and what credentials are used to connect to the data.
  
 **To create and use a new data connection in Excel**
  
1. In Excel, on the **Data** tab, in the **Get External Data** group, choose one of the following options: 
    
  - Choose **From Access** to use data that is stored in an Access database. 
    
  - Choose **From Web** to use data from an internal or external website. 
    
  - Choose **From Text** to use data that is stored in a text file. 
    
  - Choose **From Other Sources** to use data that is available in SQL Server, SQL Server Analysis Services, Azure Marketplace, OData, an XML file, or data that is available through a custom provider. 
    
    The Data Connection Wizard opens.
    
2. Specify the information that is required for each step of the Data Connection Wizard, and then click **Finish**. 
    
3. On the **Import Data** page, choose how you want to view the data, and then choose **OK**. 
    
    The options that are available depend on the particular data source that you are using. For example, you might choose to create a data table, a PivotChart report, a PivotTable report, a Power View sheet, or just the data connection.
    
For more detailed information about how to create data connections, see [Share data connections by using Excel and Excel Services (SharePoint Server 2013)](share-data-connections-by-using-excel-and-excel-services-sharepoint-server-2013.md).
  
After you have created an Excel workbook that uses external data and views, such as PivotChart reports, PivotTable reports, or Power View views, you can share that workbook with others by using a site such as a SharePoint site. Depending on your environment, the external data connections that are used in your workbook might not be supported. Whether an external data connection is supported determines whether data refresh is available for the workbook and whether the workbook is viewable in a browser window. 
  
## External data connections that are supported in Excel Services in SharePoint Server
<a name="part2"> </a>

Most, but not all, of the data connections that you can use in Excel are supported in Excel Services. These include connections to the following data sources:
  
- SQL Server tables
    
- SQL Server Analysis Services cubes
    
- OLE DB and ODBC data sources
    
When a data connection is supported, it means that people can refresh data in Excel Services that use that data connection, as long as Excel Services is configured correctly.
  
Data sources that you can connect to in Excel that are not supported in Excel Services include the Access databases, website content, XML files, Azure Marketplace data, and text files. If you plan to use these kinds of data sources in workbooks that you'll publish to SharePoint Server 2013, consider importing data into Excel and using the data as native data. For more information, see [Working with native data in Excel Services](data-sources-supported-in-excel-services-sharepoint-server-2013.md#part5).
  
## External data connections that are supported in a SharePoint environment that includes Office Web Apps Server
<a name="part3"> </a>

Office Web Apps Server is the online companion to Office Word, Excel, PowerPoint, and OneNote applications. If your organization is using SharePoint Server 2013 together with Office Web Apps Server, then your organization is using either Excel Services or Excel Web App (part of Office Web Apps Server) to display workbooks in a browser window. This decision affects which data sources are supported for workbooks rendered in a browser window.
  
Excel Web App supports some, but not all, kinds of secure external data connections. Data connections to Microsoft Access databases, website content, XML files, Azure Marketplace data, and text files are not supported in Excel Web App. If you plan to use these kinds of data sources in workbooks that you'll share using Excel Web App, consider importing data into Excel and using the data as native data.
  
## Working with data models in Excel Services
<a name="part4"> </a>

A data model is a dataset that consists of multiple tables. Data models are useful for bringing together data from different databases to create a single database that can serve as a data source for views, such as PivotChart reports, PivotTable reports, and Power View views. Data models can be created by using external data or native data. For more information about data models, see [PowerPivot: Powerful data analysis and data modeling in Excel](https://go.microsoft.com/fwlink/p/?LinkId=263500).
  
To view or use a workbook that contains a data model in Excel Services, Excel Services must be configured to support data models. For more information, [Manage Excel Services data model settings (SharePoint Server 2013)](manage-excel-services-data-model-settings.md). Currently, Office Web Apps Server does not support data models.
  
## Working with native data in Excel Services
<a name="part5"> </a>

Native data is data that is imported into Excel and does not keep connections to external databases. Native data is also known as worksheet data or sheet data, and it is either static data or data that is updated manually. Working with native data in Excel workbooks offers certain advantages:
  
- You can publish workbooks that use data from sources that are not supported in Excel Services or Excel Web App.
    
- You and others can view and interact with workbooks that use native data in a browser window, whether the workbook is rendered by either Office Web Apps Server or SharePoint Server 2013. Note that data models are not supported in Office Web Apps Server, but PivotChart reports and PivotTable reports that use native data are supported.
    
- If a workbook does not consume more than 10 MB of disk space, you can share or view the workbook on Microsoft 365. This makes it possible to share information "in the cloud."
    
## See also
<a name="part5"> </a>

#### Concepts

[Share data connections by using Excel and Excel Services (SharePoint Server 2013)](share-data-connections-by-using-excel-and-excel-services-sharepoint-server-2013.md)
  
[Business intelligence capabilities in Excel Service (SharePoint Server 2013)](bi-capabilities-in-excel-and-excel-services.md)
#### Other Resources

[Data authentication for Excel Services in SharePoint Server ](/SharePoint/administration/excel-services-overview)

