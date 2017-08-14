---
title: Overview of PerformancePoint scorecards
ms.prod: SHAREPOINT
ms.assetid: 49150632-b723-44ae-9918-3099f7dd0151
---


# Overview of PerformancePoint scorecards
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2016-09-16* **Summary:** Learn about PerformancePoint scorecards.A scorecard is a special kind of report that provides a high-level snapshot of performance for a group or an organization. Scorecards display a collection of key performance indicators (KPIs) and the performance targets for those KPIs to show progress toward achieving specific goals. The KPIs in a scorecard represent specific, measurable elements of performance, such "Sales” for a particular group, or "Number of customer complaints per day." A scorecard provides a visual representation of performance that can give you a summary of progress at a glance. 
## Characteristics of PerformancePoint scorecards
<a name="section1"> </a>

A scorecard that was created by using PerformancePoint Dashboard Designer is known as a PerformancePoint scorecard. Some features that you might see in a PerformancePoint scorecard are described in the following list:
- Trend indicators, such as arrows, that show whether performance has improved, remained the same, or decreased from a previous time period. 
    
  
- Complex KPIs that measure performance by comparing multiple values or by using calculated metrics. For example, suppose that sales performance is determined not only by comparing gross sales amounts to quota, but also by factoring in gross profit margin and weighted sales metrics. You can have KPIs that show all the measures of sales performance and then calculate an overall performance measurement.
    
  
- Time Intelligence to show performance for dynamic time periods or as of a particular date. For example, you might have a column labeled **Last Six Months** in your scorecard that is automatically updated.
    
  
- Expandable and collapsible rows or columns that you can use to see lower or higher levels of detail in the scorecard. For example, suppose that you have an item named All Products on rows in your scorecard. Depending on how the scorecard is configured, you can click Products and see the next level of detail. The scorecard updates and displays additional rows, one for each item in the Products group.
    
  
- KPIs that are used as filters for other reports, such as analytic charts or grids in a dashboard. For example, suppose that you have a scorecard that is connected to an analytic chart. When you click a KPI, the analytic chart automatically updates to display information that is relevant to that KPI. When you click another KPI, the report updates again to display information for that KPI, and so on.
    
  
- The ability to open a Decomposition Tree to analyze how individual members contribute to a value. Depending on how the scorecard is configured and if it uses SQL Server Analysis Services data, you can right-click a value, and then click **Decomposition Tree**.
    
  

## Interactive functionality in PerformancePoint scorecards
<a name="section2"> </a>

You would typically include one or more scorecards in your dashboard to enable dashboard users to easily view whether performance is on or off target at a glance. Depending on how you set up your scorecards, dashboard users can use those scorecards to perform the following tasks:
- Expand or collapse rows in the scorecard.
    
    Drill up (or down) to view higher (or lower levels) of detail.
    
  
- Apply value filters to display the top (or bottom) members in a group, or values that are in a given range.
    
  
- Export information to PowerPoint or Excel.
    
  
- Click a value in a scorecard that is linked to a KPI Details report to view additional information about KPI values and properties. 
    
    > [!NOTE:]
      
- Click a KPI that is linked to another report, such as an analytic chart or grid, to display additional information about that KPI value.
    
  

## Data sources for PerformancePoint scorecards
<a name="section3"> </a>

PerformancePoint scorecards can use data that is stored in any of the following data sources:
- SQL Server Analysis Services
    
  
- A SharePoint list
    
  
- A table in a SQL Server database
    
  
- A list of values that is created by the scorecard author
    
  

