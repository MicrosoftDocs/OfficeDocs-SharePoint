---
title: Overview of the PerformancePoint Decomposition Tree
ms.prod: SHAREPOINT
ms.assetid: 6f72c13c-d745-484a-b07f-3426e3c49d3f
---


# Overview of the PerformancePoint Decomposition Tree
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-05-30* **Summary:** Learn about PerformancePoint decomposition trees.The PerformancePoint Decomposition Tree, is an analytics tool that dashboard users can use to perform root-cause analysis. Dashboard users can view how individual members in a group contribute to the whole. In a Decomposition Tree, members are ranked from greatest to least, or from least to greatest. The Decomposition Tree enables users to decompose, or analyze, a group to see its individual members and how they can be ranked according to a selected measure, such as by sales amounts. 
> [!NOTE:]

  
    
    

In this article:
-  [How do I create or open a Decomposition Tree?](#section1)
    
  
-  [How do I use a Decomposition Tree?](#section2)
    
  

## How do I create or open a PerformancePoint Decomposition Tree?
<a name="section1"> </a>

As a dashboard author, you do not create the Decomposition Tree by using PerformancePoint Dashboard Designer. In addition, you cannot display a Decomposition Tree as a top-level report view that is always displayed in a dashboard alongside other reports. Instead, dashboard users open the Decomposition Tree from a report in a dashboard that is deployed to SharePoint Server 2016. 
> [!NOTE:]

  
    
    

 **To open the Decomposition Tree**
1. In a PerformancePoint dashboard that is published to SharePoint Server 2016, select a report view that uses SQL Server Analysis Services data. Examples include analytic charts and grids, and some kinds of scorecards.
    
  
2. In the report view, right-click a value, and then select **Decomposition Tree**. The value can be a cell in a scorecard or a grid, or it can be an amount in a chart.
    
    The Decomposition Tree opens in a browser window.
    
  

## How do I use a PerformancePoint Decomposition Tree?
<a name="section2"> </a>

Dashboard users would typically use a Decomposition Tree to see how a single value in a report or a scorecard can be broken down into its contributing members. The Decomposition Tree automatically sorts results and applies an inline Pareto chart to the data. Therefore, dashboard users can quickly see the highest contributors to a particular report value. Dashboard users can also see trends across individual members that contribute to an overall value. When dashboard users begin to use the Decomposition Tree, they typically start with one bar, which is a decomposition node, located on the left side of the screen. Use the following procedure to conduct root-cause analysis. **To conduct root-cause analysis by using a Decomposition Tree**
1. In a PerformancePoint dashboard that is published to SharePoint Server 2016, select a report view that uses SQL Server Analysis Services data. Examples include analytic charts and grids, and some kinds of scorecards.
    
  
2. In the report view, right-click a value, and then select **Decomposition Tree**. The value can be a cell in a scorecard or a grid, or it can be an amount in a chart.
    
    The Decomposition Tree opens in a browser window.
    
  
3. Click a decomposition node. A list of dimensions and hierarchies is displayed.
    
  
4. Select the dimension and hierarchy that you want to use. The view automatically updates to display the next level of detail for the item that you selected. 
    
  
5. Repeat Steps 3 and 4 to show additional levels of detail in the view.
    
  
6. To view member properties for a dimension member, browse to a single dimension member. Click its node to open a dialog box that contains additional options, and then click **Show Properties**.
    
  

# See also

#### 

 [Overview of PerformancePoint reports and scorecards](html/overview-of-performancepoint-reports-and-scorecards.md)
  
    
    

  
    
    

