---
title: "Business intelligence capabilities in Excel Service (SharePoint Server 2013)"
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 6/23/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: cdd1d3d6-034e-458f-9324-c51d90fa9273

description: "Excel 2013 offers a wide range of business intelligence capabilities. Learn which capabilities are supported in Excel Services (on premises)."
---

# Business intelligence capabilities in Excel Service (SharePoint Server 2013)

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)]
  
Excel offers certain business intelligence capabilities that make it easier than ever to explore and analyze data. Many of these features are supported by Excel Services. Read this article to learn about which capabilities in Excel are supported in SharePoint Server 2013 and Office Web Apps Server. 
  
> [!IMPORTANT]
> The information in this article applies to on-premises deployments of SharePoint Server 2013. 
  
    
## Business intelligence capabilities in Excel 2013
<a name="part1"> </a>

Using Excel 2016, you can create powerful reports, scorecards, and dashboards. You can bring data into Excel, sort, and organize data, and use it to create reports and scorecards. You can also use powerful analytic capabilities in Excel to visualize and explore data. The following table describes business intelligence features in Excel.
  
**Table: Overview of business intelligence capabilities in Excel 2013**

|**Task area**|**Capability**|**Description**|
|:-----|:-----|:-----|
|Get data  <br/> |Native data  <br/> |Native data is data that was imported into Excel and lives in Excel without maintaining an external data connection. This is useful for working with static data, working with data that is updated manually, and creating workbooks that are published in locations where external data connections are not supported.  <br/> |
|Get data  <br/> |External data  <br/> |External data is data that resides on another computer and is accessed in Excel through one or more external data connections. Excel can connect to many kinds of data sources.  <br/> |
|Work with data  <br/> |Data Models  <br/> |A Data Model is a dataset that consists of multiple tables. You can use Data Models to bring together data from different databases and create relationships between tables of data. You can use a Data Model as a source for reports, scorecards, and dashboards. For more information, see [PowerPivot: Powerful data analysis and data modeling in Excel](https://go.microsoft.com/fwlink/p/?LinkId=263500).  <br/> |
|Work with data  <br/> |Flash Fill  <br/> |Flash Fill is functionality that enables you to quickly and easily format data that is displayed in a table in Excel. For example, suppose that you have imported data into Excel and you have a column that lists dates and times, and you only want to use dates. You can insert a new column, type the date that corresponds to the first item in the format that you want to use, and then use Flash Fill to automatically do this for all the rows in your table.  <br/> |
|Create reports  <br/> |Quick Analysis  <br/> |Quick Analysis is functionality that enables you to select a range of data and see recommended ways to visualize that information. When you use Quick Analysis, you can see what your chart or table will resemble before actually selecting which chart type to use.  <br/> |
|Create reports  <br/> |Reports  <br/> |Reports can include tables, line charts, bar charts, scatter plots, radar charts, and many other kinds of charts. You can use Excel to create powerful, interactive PivotChart reports and PivotTable reports to display relevant information by using lots of data sources.  <br/> |
|Create reports  <br/> |Scorecards  <br/> |Scorecards are a special kind of report designed to show whether performance is on- or off-target for one or more metrics at a glance. Scorecards typically contain one or more key performance indicators (KPIs) that compare actual values to target values and use a graphical indicator, such as colors or symbols, to show performance at a glance.  <br/> In Excel, you can use KPIs that were defined in an external database or use Power Pivot to create your own KPIs.  <br/> |
|Create reports  <br/> |Power View  <br/> |Power View is an add-in for Excel that you can use to create highly interactive views. Power View enables you to quickly and easily create reports, scorecards, and dashboards. You can configure connections between items in a view so that values in one report can be used as parameters for other reports in the view. For more information about Power View, see [Power View: Explore, visualize, and present your data](https://go.microsoft.com/fwlink/p/?LinkId=263501).  <br/> |
|Create or edit reports  <br/> |Field List and Field Well  <br/> | When you create a PivotChart or PivotTable report, you use the **Fields** section to specify what information to display in the reports. The Fields section contains the **Field List** and **Field Well**.  <br/>  The **Field List** lists items such as dimensions and members from the data source that you are using for the PivotChart or PivotTable report. You can also use the Field List to determine whether you are using native data or external data.  <br/>  The **Field Well** shows which items from the **Field List** are displayed in the report. You can change what information is displayed in a PivotChart or PivotTable report by selecting (or clearing) different items and measures.  <br/> |
|Apply filters  <br/> |Timeline control  <br/> |The Timeline control is a special kind of time filter that you can use in Excel. To add a timeline control to a worksheet, at least one report on the worksheet must use data that contains a calendar date/time hierarchy. You can use the timeline control to select a single time period or a range of time, and any reports that are connected to the timeline are automatically updated to show information for that time period.  <br/> |
|Apply filters  <br/> |Slicers  <br/> |Slicers are a kind of filter that you can use to select one or more items to use as a filter for reports and scorecards in a worksheet. For example, suppose that you want to see sales information for different colors of items, such as shirts that your company carries. You can create a slicer that lists shirt colors, connect it to a sales report, and then use the slicer to view sales information for the colors that are selected in the slicer.  <br/> |
|Explore and analyze data  <br/> |Quick Explore  <br/> |Quick Explore is functionality that enables you to click a value in a PivotChart or PivotTable report that uses SQL Server Analysis Services data or Power Pivot data, and then see additional information about that value displayed as a chart type. You can also use Quick Explore to drill up (or down) to view higher (or lower) levels of detail in a PivotChart or PivotTable report.  <br/> |
|Use advanced analytic capabilities  <br/> |Calculated Members and Calculated Measures  <br/> |Calculated Members and Calculated Measures are items that you can define by using Multidimensional Expressions (MDX) queries in Excel. You can create calculated members and calculated measures for PivotChart or PivotTable reports that use multidimensional data that is stored in Analysis Services.  <br/> > [!IMPORTANT]> Calculated Members and Calculated Measures are not the same things as Calculated Fields. You can only create Calculated Members and Calculated Measures when you have created a PivotTable report or a PivotChart report that uses data that is stored in Analysis Services. To create calculated members or calculated measures, you should be familiar with the database that you are using and be proficient in writing MDX queries.           |
|Use advanced analytic capabilities  <br/> |Calculated Fields  <br/> |Calculated Fields enable you to change a Data Model that was created by using Power Pivot. When you create Calculated Fields, custom columns are added to the Data Model. You can then use those columns in reports that you create using that Data Model.  <br/> > [!NOTE]> To create calculated fields, you should be familiar with the database that you are using and be proficient in writing Data Analysis Expressions (DAX).           |
   
## Business intelligence capabilities supported in Excel Services in SharePoint Server
<a name="part2"> </a>

After you have created reports, scorecards, and dashboards using Excel, you can publish those items to SharePoint Server 2013 to make them available to people in your organization. The following table summarizes which business intelligence features are supported by Excel Services (on premises).
  
**Table: Overview of business intelligence capabilities in Excel Services**

|**Item**|**Supported in Excel Services in the on-premises version of SharePoint Server 2013?**|
|:-----|:-----|
|External data connections  <br/> |Most external data connections are supported in Excel Services. Excel Services supports SQL Server Analysis Services (SSAS), SQL Server databases, and OLE DB and ODBC data sources. For more information, see [Data authentication for Excel Services (SharePoint Server 2013)](/SharePoint/administration/excel-services-overview).  <br/> |
|Data Models  <br/> |Data Models are supported in Excel Services as long as an instance of SQL Server Analysis Services is specified for Excel Services. For more information, see [Plan Excel Services Data Model settings in SharePoint Server 2013](plan-excel-services-data-model-settings.md).  <br/> |
|Flash Fill  <br/> |Flash Fill is not supported when you view a workbook in a browser window. You can edit a workbook in Excel to use Flash Fill.  <br/> |
|Quick Analysis  <br/> |Quick Analysis is not supported when you view a workbook in a browser window. You can edit a workbook in Excel to use Quick Analysis.  <br/> |
|Reports and scorecards  <br/> |Reports, scorecards, and dashboards that were created by using Excel are supported in Excel Services. You can view, sort, filter, and interact with PivotTable reports and PivotChart reports in a browser window much such as you would by using the Excel client. This includes views that were created by using Power View.  <br/> |
|**Field List** and **Field Well** (for PivotChart and PivotTable reports)  <br/> |The ability to open and use the **Field List** and **Field Well** in a browser window is supported in Excel Services.  <br/> |
|Timeline control  <br/> |The ability to use an existing timeline control is supported in Excel Services. However, to add a timeline control to a workbook, you must use the Excel client.  <br/> |
|Slicers  <br/> |The ability to use existing slicers is supported in Excel Services. However, to add slicers to a workbook, you must use the Excel client.  <br/> |
|Quick Explore  <br/> |The ability to use Quick Explore is supported in Excel Services. You can use Quick Explore to drill up and down to view higher or lower levels of information. However, you can't create new views using Quick Explore in a browser window.  <br/> |
|Calculated Members and Calculated Measures  <br/> |The ability to use existing calculated members and calculated measures is supported in Excel Services. However, to create calculated members and calculated measures, you must use the Excel client.  <br/> |
|Calculated Fields  <br/> |The ability to use existing calculated fields is supported in Excel Services. However, to create calculated fields, you must use Power Pivot for Excel.  <br/> |
|Business Intelligence Center  <br/> |A Business Intelligence Center site template is available in SharePoint Server 2013. This enables you to create a site that serves as a central location to store business intelligence content, such as reports, scorecards, and dashboards. For more information, see [Configure a Business Intelligence Center in SharePoint Server 2013](/SharePoint/sharepoint-server).  <br/> |
|Excel Web Access Web Part  <br/> |An Excel Web Access Web Part is available in SharePoint Server 2013. This enables you to display all or part of an Excel workbook that was published to SharePoint Server 2013. For more information about how to use the Excel Web Access Web Part, see [Display Excel content in an Excel Web Access Web Part](https://go.microsoft.com/fwlink/p/?LinkId=296506).  <br/> |
   
## Business intelligence capabilities supported in Office Web Apps Server 2013 and SharePoint Server 2013
<a name="part3"> </a>

Office Web Apps Server is the online companion to Office Word, Excel, PowerPoint, and OneNote applications. Office Web Apps Server gives users a browser-based viewing and editing experience by providing a representation of an Office document in the browser. Organizations that have SharePoint Server 2013 might also be using Office Web Apps Server, and that has certain implications for which business intelligence capabilities are supported in a browser window.
  
> [!IMPORTANT]
> If your organization is using Office Web Apps Server together with SharePoint Server 2013, then your organization can use either Office Web Apps Server or SharePoint Server 2013 to display workbooks. This decision affects which business intelligence capabilities are supported in a browser window. > To enable people to interact with workbooks that contain a Data Model or Power View views in a browser window, configure Excel Services in SharePoint Server 2013 to display workbooks. This requires a SharePoint administrator to run the **New-SPWOPISupressionSetting** cmdlet on the server where SharePoint Server 2013 in installed. For more information, see [New-SPWOPISuppressionSetting](/powershell/module/sharepoint-server/New-SPWOPISuppressionSetting?view=sharepoint-ps). 
  
The following table summarizes the business intelligence features that are supported by Office Web Apps Server and by SharePoint Server 2013.
  
**Table: Overview of business intelligence capabilities in Office Web Apps Server and SharePoint Server**

|**Excel Capability**|**What's supported when Office Web Apps Server is used to display workbooks**|**What's supported when SharePoint Server 2013 is used to display workbooks**|
|:-----|:-----|:-----|
|External data connections and authentication methods  <br/> |Office Web Apps Server supports some, but not all, kinds of secure external data connections. Data connections that use Secure Store Service or an unattended service account are supported as long as SharePoint Server 2013 is configured to use these methods.  <br/> |SharePoint Server 2013 supports most kinds of external data connections. These include SQL Server Analysis Services (SSAS), SQL Server databases, and OLE DB and ODBC data sources.  <br/> For more information about authentication methods, see [Data authentication for Excel Services in SharePoint Server 2013 ](/SharePoint/administration/excel-services-overview).  <br/> |
|Data Models  <br/> |Office Web Apps Server enables you to view workbooks that contain Data Models that use native data. However, you can't explore data in items such as PivotTable reports, PivotChart reports, and timeline controls that use a Data Model as the data source.  <br/> |SharePoint Server 2013 enables you to view, interact with, and refresh workbooks that contain Data Models using native or external data. This includes the ability to explore data in PivotChart reports and PivotTable reports and to use timeline controls in a browser window.  <br/> |
|Flash Fill  <br/> |Office Web Apps Server does not support using Flash Fill when you edit a workbook in a browser window. However, you can open the workbook in Excel to use Flash Fill.  <br/> |SharePoint Server 2013 does not support Flash Fill when you view a workbook in a browser window. However, you can open the workbook in Excel to use Flash Fill.  <br/> |
|Quick Analysis  <br/> |Office Web Apps Server does not support using Quick Analysis when you edit a workbook in a browser window. However, you can use open the workbook in Excel to use Quick Analysis.  <br/> |SharePoint Server 2013 does not support Quick Analysis when you view a workbook in a browser window.  <br/> |
|Reports and scorecards  <br/> |Office Web Apps Server enables you to view, sort, and filter reports, scorecards, and dashboards that were created by using Excel. However, Office Web Apps Server does not support views that were created by using Power View.  <br/> |SharePoint Server 2013 enables you to view, sort, and filter reports, scorecards, and dashboards that were created by using Excel. This includes views that were created by using Power View.  <br/> |
|**Field List** and **Field Well** (for PivotChart and PivotTable reports)  <br/> |Office Web Apps Server enables you to open and use the **Field List** and **Field Well** in a browser window.  <br/> |SharePoint Server 2013 enables you to open and use the **Field List** and **Field Well** in a browser window.  <br/> |
|Timeline control  <br/> |Office Web Apps Server enables you to use an existing timeline control. To add a timeline control to a workbook you must use the Excel client.  <br/> |SharePoint Server 2013 enables you to use an existing timeline control. To add a timeline control to a workbook you must use the Excel client.  <br/> |
|Slicers  <br/> |Office Web Apps Server enables you to use slicers.  <br/> |SharePoint Server 2013 enables you to use slicers.  <br/> |
|Quick Explore  <br/> |Office Web Apps Server enables you to use Quick Explore.  <br/> |SharePoint Server 2013 enables you to use Quick Explore.  <br/> |
|Calculated Members and Calculated Measures  <br/> |Office Web Apps Server supports workbooks that contain calculated members and calculated measures. However, to create calculated members and calculated measures, you must use the Excel client.  <br/> |SharePoint Server 2013 enables you to use existing calculated members and calculated measures. However, to create calculated members and calculated measures, you must use the Excel client.  <br/> |
|Calculated Fields  <br/> |Office Web Apps Server does not support calculated fields.  <br/> |SharePoint Server 2013 enables you to use existing calculated fields. However, to create calculated fields, you must use Power Pivot for Excel.  <br/> |
|Business Intelligence Center  <br/> |You can use the Business Intelligence Center site template to create a central location to store business intelligence content, such as reports, scorecards, and dashboards. For more information, see [Configure a Business Intelligence Center in SharePoint Server 2013](/SharePoint/sharepoint-server).  <br/> |You can use the Business Intelligence Center site template to create a central location to store business intelligence content, such as reports, scorecards, and dashboards. For more information, see [Configure a Business Intelligence Center in SharePoint Server 2013](/SharePoint/sharepoint-server).  <br/> |
|Excel Web Access Web Part  <br/> |The Excel Web Access Web Part that is available in SharePoint Server 2013 enables you to display all or part of an Excel workbook that was published to a SharePoint library in a Web Part on a SharePoint page. Even if Office Web Apps Server is used to display workbooks in a browser window, the Excel Web Access Web Part uses Excel Services in SharePoint Server 2013 to display content in that Web Part.  <br/> For more information about how to use the Excel Web Access Web Part, see [Display Excel content in an Excel Web Access Web Part](https://go.microsoft.com/fwlink/p/?LinkId=296506).  <br/> |The Excel Web Access Web Part that is available in SharePoint Server 2013 enables you to display all or part of an Excel workbook that was published to a SharePoint library in a Web Part on a SharePoint page.  <br/> For more information about how to use the Excel Web Access Web Part, see [Display Excel content in an Excel Web Access Web Part](https://go.microsoft.com/fwlink/p/?LinkId=296506).  <br/> |
   
To learn more about Office Web Apps Server, see [Overview of Office Web Apps Server ](/webappsserver/office-web-apps-server-overview).
  
## See also
<a name="part3"> </a>

#### Concepts

[Overview of Excel Services in SharePoint Server 2013](excel-services-overview.md)
#### Other Resources

[What's new in business intelligence in SharePoint Server 2013](/SharePoint/what-s-new/new-and-improved-features-in-sharepoint-server-2016)
  
[Office Web Apps ](/webappsserver/office-web-apps-server)
