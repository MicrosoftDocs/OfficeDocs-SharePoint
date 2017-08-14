---
title: Overview of PerformancePoint analytic charts and grids
ms.prod: SHAREPOINT
ms.assetid: 6529a690-639d-47fc-9399-62813ae331ef
---


# Overview of PerformancePoint analytic charts and grids
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2016-09-16* **Summary:** Learn about analytic charts and grids in PerformancePoint Dashboard Designer.You can create analytic reports for your dashboards by using PerformancePoint Dashboard Designer. Analytic reports are dynamic, visual representations of data that can be displayed as interactive line charts, bar charts, pie charts, and tables (which are called grids). PerformancePoint analytic reports remain connected to the data, which means that their content is always up to date. 
## Interactive functionality in PerformancePoint Services analytic charts and grids

You would typically include one or more analytic reports in your dashboard. Depending on how you set up your analytic charts or grids, dashboard users can use those reports to:
- Open a **Decomposition Tree** to see how a specific value can be broken down into its contributing members and discover trends across individual members.
    
    > [!IMPORTANT:]
      
- Apply value filters to display the top (or bottom) members in a group, or values that are in a given range.
    
  
- Use **Additional Actions**, which are defined in the Analysis Services cube.
    
  
- Sort values or chart legend items in ascending or descending order. 
    
  
- Drill down or up to see lower or higher levels of detail. 
    
  
- Filter out empty items, isolate an item, or remove an item from the report view. 
    
  
- Pivot the report, or configure the view type and format. 
    
  
- Show or hide information, such as measures or background information. 
    
  
- Work with multiple pages of data. (This is useful when a query returns a large set of results.) 
    
  
- Export information to PowerPoint or Excel.
    
  

> [!TIP:]

  
    
    


## Data sources for analytic charts and grids

Analytic reports pull information from data that is arranged into cubes in Analysis Services. These cubes consist of dimensions, members, and named sets, as described here:
### 

ItemDescriptionDimension  <br/> A structured, hierarchical way to organize data. For example, a **Products** dimension might have a hierarchy such as **Products** > **Product Categories** > **Product Names**, and a **Date** dimension might have **Year** > **Week** > **Day**. <br/> Measure  <br/> A cube member that associates a numeric value with one or more dimension members. For example, some measures might include **Sales Amounts**, **Gross Profit**, and **Gross Profit Margin**. <br/> Named set  <br/> A collection of one or more dimension members that is defined in the database. For example, **Core Products** is a common named set that contains a subset of the members that are included in the **Products** dimension. <br/> 
