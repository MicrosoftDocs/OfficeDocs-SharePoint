---
title: "PerformancePoint Services application settings"
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/6/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: bf9068c7-9187-49bb-9946-c298389bf4b0

description: "Learn how to customize PerformancePoint Services application settings to meet your business needs."
---

# PerformancePoint Services application settings

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
PerformancePoint Services has settings such as cache durations, filter behavior, and query time-out that affect performance, security, and connections to external data. These settings affect anyone who uses the same service application. The settings can be managed by using the SharePoint Central Administration website.
  
## PerformancePoint Services application settings

****

|**Setting**|**Description**|
|:-----|:-----|
|Secure Store and Unattended Service Account  <br/> |A single shared user account is used to access all data sources. This is a low-privileged domain account stored in the Secure Store Service. An application ID is automatically mapped in the Secure Store Service that specifies the default secure store target application, PerformancePoint Services, and it looks up credential mapping when it connects to external data sources.  <br/> > [!IMPORTANT]> When you establish an unattended service account, first determine whether this account should have access to the data sources that will be retrieved in Dashboard Designer.           |
|Comments  <br/> |Users who have appropriate permissions can annotate scorecard cells in Dashboard Designer and on a deployed SharePoint site.  <br/> > [!NOTE]> If a Dashboard Designer author attempts to add cell comments that are disabled, the author will receive a message that states, "An unexpected system error has occurred. Additional details have been logged for your administrator." If you want the author to be able to insert comments in a cell, select the check box, **Enable comments**.           You can also remove comments by clicking **Delete Comments by Date**. This command opens a dialog box. Select the date by which you want comments removed from the PerformancePoint Services database, and then click **Delete**.  <br/> |
|Analysis Services EffectiveUserName  <br/> |The Analysis Services EffectiveUserName capability is an alternative to Windows delegation for allowing individual users to securely access Analysis Services data. When this setting is enable, all connections to Analysis Services data for individual users will be made using the EffectiveUserName connection string property instead of Windows delegation.  <br/> |
|Cache  <br/> |Temporarily storing (or "caching") frequently-accessed items decreases load times for future requests. Specify the duration for items to remain in the cache.  <br/> |
|Data Sources  <br/> |Set the duration of no response before a data source query is canceled.  <br/> |
|Filters  <br/> |Specify how long to remember user-selected filter values and how often to clear expired values. Set the maximum number of members to retrieve and insert into a filter of type "tree".  <br/> |
|Select Measure Control  <br/> |Set the maximum number of measures to retrieve and insert into a dashboard Select Measure control.  <br/> |
|Show Details  <br/> |Set the limit for the number of rows returned when a user clicks "Show Details."  <br/> |
|Decomposition Tree  <br/> |Set the maximum number of individual items (per level) returned to the decomposition tree visualization. The minimum value is 0. The maximum is 1,000,000.  <br/> |
   

