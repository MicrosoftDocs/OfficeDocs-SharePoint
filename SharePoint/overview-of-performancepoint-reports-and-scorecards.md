---
title: Overview of PerformancePoint reports and scorecards
ms.prod: SHAREPOINT
ms.assetid: 90d8dee0-5c31-4c9b-93d5-cf09cb2320aa
---


# Overview of PerformancePoint reports and scorecards
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2016-12-30* **Summary:** Learn about reports and scorecards within PerformancePoint Dashboard Designer.You can use PerformancePoint Dashboard Designer to create reports and scorecards for your dashboards. As you create each report or scorecard, you begin by selecting the appropriate template within Dashboard Designer.In this article:
-  [Report templates](#section1)
    
  
-  [Scorecard templates](#section2)
    
  

## PerformancePoint Services report templates
<a name="section1"> </a>

PerformancePoint reports can vary greatly in appearance and functionality. Some reports are created by using Dashboard Designer, but others are often external, existing reports that you can display in a PerformancePoint dashboard by creating a PerformancePoint Web Part. Finally, for some reports, you must have at least one scorecard created to successfully create and display information in those reports. 
### 

TemplateDescription **Analytic Chart** <br/> An analytic chart is an interactive line, bar, or pie chart that you create and configure by using Dashboard Designer. Analytic charts use data that is stored in SQL Server Analysis Services.  <br/> **Analytic Grid** <br/> An analytic grid is an interactive table that you create and configure by using Dashboard Designer. Analytic grids use data that is stored in SQL Server Analysis.  <br/> **KPI Details** <br/> A KPI Details report is a report that serves as a companion to a scorecard to provide additional information about scorecard key performance indicator (KPI) values and properties.  <br/> A KPI Details report does not contain or display information by itself. The KPI Details report derives all its information directly from the scorecard to which it is connected. Dashboard users click a value in a scorecard, and the KPI Details report updates to display additional information about that particular scorecard value without cluttering up the scorecard.  <br/> **Reporting Services** <br/> A Reporting Services report is a view that was published to SQL Server Reporting Services Report Server.  <br/> In Dashboard Designer, you do not actually create a Reporting Services report. Instead, you create a PerformancePoint Web Part to display an existing Reporting Services report.  <br/> **Strategy Map** <br/> A strategy map is a report that serves as a companion to a scorecard to show relationships between objectives, goals, and KPIs at a glance. Strategy maps are based on the Balanced Scorecard framework.  <br/> A strategy map uses a scorecard as its data source and a Visio diagram as its display structure.  <br/> **Web Page** <br/> A Web Page report is a fully functional internal or external Web site that you can display alongside other reports in your dashboard.  <br/> In Dashboard Designer, you do not actually create a Web Page. Instead, you create a PerformancePoint Web Part to display an existing website.  <br/> **Decomposition Tree** <br/> A Decomposition Tree is an interactive view that dashboard users open from a scorecard or a report that uses SQL Server Analysis Services data. However, as a dashboard author, you do not create the Decomposition Tree by using PerformancePoint Dashboard Designer. In addition, you cannot display a Decomposition Tree as a top-level report view that is always displayed in a dashboard alongside other reports.  <br/> 
## PerformancePoint Services scorecard templates
<a name="section2"> </a>

A scorecard is a special kind of report that provides a high-level snapshot of performance for a group or an organization. A scorecard provides a visual representation of performance that can give you a summary of progress at a glance. When you create a PerformancePoint scorecard, you can use a wizard to guide you through the process. When you use a wizard, you begin by selecting a template. The template that you select corresponds to the kind of data source that you plan to use for at least one key performance indicator (KPI) in your scorecard.
> [!IMPORTANT:]

  
    
    


### 

TemplateDescription **Analysis Services** <br/>  The Analysis Services scorecard template enables you to create a scorecard that uses an Analysis Services data source for at least one KPI in the scorecard. <br/>  Depending on how an Analysis Services scorecard is configured, dashboard users can perform certain tasks that are not necessarily available with other scorecard templates: <br/>  Use **Show Details** to view transaction-level details for a particular scorecard value. <br/>  Open a Decomposition Tree to decompose, or analyze, a group to see its individual members and how they can be ranked according to a selected measure. For more information, see [Learn about the Decomposition Tree](https://go.microsoft.com/fwlink/p/?LinkId=204883) (https://go.microsoft.com/fwlink/p/?LinkId=204883). <br/>  View higher or lower levels of data in the scorecard. <br/>  View dynamic dimension hierarchies in the scorecard. <br/>  When you use the Analysis Services scorecard template, you can create KPIs that are based on measures in the data cube, or you can select existing KPIs that you or other dashboard authors have created. However, you can also copy KPIs that are defined in the data cube into the scorecard. This ability to copy KPIs is unique to the Analysis Services scorecard template. <br/> **Blank Scorecard** <br/> The Blank Scorecard template enables you to create an empty scorecard that has no KPIs or other information. You would typically create a blank scorecard when you and other dashboard authors have already created KPIs.  <br/> **Fixed Values Scorecard** <br/> The Fixed Values Scorecard template enables you to create a scorecard that does not use a separate data source. When you use this template, you specify the values for the scorecard while you use the wizard.  <br/>  Tabular templates. They include the following: <br/> **Excel Workbook** <br/> **SharePoint List** <br/> **SQL Server Table** <br/> The three tabular templates (Excel Workbook, SharePoint List, and SQL Server Table) enable you to create a scorecard that uses a tabular data source for at least one KPI in the scorecard. Similar to the Analysis Services scorecard template, when you use a tabular data scorecard template, you can create KPIs that are based on measures in the data source, or you can select existing KPIs that you or other dashboard authors have created.  <br/> 
