---
title: PerformancePoint Services application settings
ms.prod: SHAREPOINT
ms.assetid: bf9068c7-9187-49bb-9946-c298389bf4b0
---


# PerformancePoint Services application settings
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-06* **Summary:**   Learn how to customize PerformancePoint Services application settings to meet your business needs.PerformancePoint Services has settings such as cache durations, filter behavior, and query time-out that affect performance, security, and connections to external data. These settings affect anyone who uses the same service application. The settings can be managed by using the SharePoint Central Administration website.
## PerformancePoint Services application settings


### 

SettingDescriptionSecure Store and Unattended Service Account  <br/> A single shared user account is used to access all data sources. This is a low-privileged domain account stored in the Secure Store Service. An application ID is automatically mapped in the Secure Store Service that specifies the default secure store target application, PerformancePoint Services, and it looks up credential mapping when it connects to external data sources.  <br/> 
> [!IMPORTANT:]

  
    
    

Comments  <br/> Users who have appropriate permissions can annotate scorecard cells in Dashboard Designer and on a deployed SharePoint site.  <br/> 
> [!NOTE:]

  
    
    

You can also remove comments by clicking **Delete Comments by Date**. This command opens a dialog box. Select the date by which you want comments removed from the PerformancePoint Services database, and then click **Delete**. <br/> Analysis Services EffectiveUserName  <br/> The Analysis Services EffectiveUserName capability is an alternative to Windows delegation for allowing individual users to securely access Analysis Services data. When this setting is enable, all connections to Analysis Services data for individual users will be made using the EffectiveUserName connection string property instead of Windows delegation.  <br/> Cache  <br/> Temporarily storing (or "caching") frequently-accessed items decreases load times for future requests. Specify the duration for items to remain in the cache.  <br/> Data Sources  <br/> Set the duration of no response before a data source query is canceled.  <br/> Filters  <br/> Specify how long to remember user-selected filter values and how often to clear expired values. Set the maximum number of members to retrieve and insert into a filter of type "tree".  <br/> Select Measure Control  <br/> Set the maximum number of measures to retrieve and insert into a dashboard Select Measure control.  <br/> Show Details  <br/> Set the limit for the number of rows returned when a user clicks "Show Details."  <br/> Decomposition Tree  <br/> Set the maximum number of individual items (per level) returned to the decomposition tree visualization. The minimum value is 0. The maximum is 1,000,000.  <br/> 
