---
title: "Monitor apps for SharePoint for SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/27/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 3adafdd2-f276-4a9d-8a74-e06b8916bbc2
description: "Learn how administrators and site owners can monitor the health and usage details for apps for SharePoint in SharePoint Server."
---

# Monitor apps for SharePoint for SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
You can use the SharePoint Central Administration website to monitor apps for SharePoint and check details and errors. Be sure you've [configured your environment for apps for SharePoint](configure-an-environment-for-apps-for-sharepoint.md) and [created an app catalog](manage-the-app-catalog.md) before you get started. 
  
You must be a member of the Farm Administrators group or the site Owners group to perform the steps in this article.
  
> [!IMPORTANT]
>  The **Monitor Apps** page requires the following search analytics and usage file import timer jobs to be active: >  ECM analytics timer job name: Usage Analytics timer job for Search Service >  Usage DB timer job name: Microsoft SharePoint Foundation Usage Data Import >  These are automatically activated when you configure Search in your environment. 
  
    
## Selecting apps to monitor in Central Administration
<a name="proc1"> </a>

The Monitored Apps page displays the apps for SharePoint that have been configured for monitoring. Each app for SharePoint that is listed on this page includes details to help an administrator monitor performance. Each app for SharePoint provides the following properties: Name, Status, Source, Licenses in Use, Licenses Purchased, Install Locations, and Runtime Errors.
  
 **To add an app to the monitor apps list**
  
1. In Central Administration, click **General Application Settings**.
    
2. On the General Application Settings page, in the **Apps** section, click **Monitor Apps**.
    
3. On the Monitored Apps page, in the **Action** group of the ribbon, click **Add App**.
    
4. Select the checkbox for the app that you want to monitor, or type a name in the **Search for app name** box, and then click the Search icon. 
    
5. On the search results page, select the app that you want to monitor.
    
6. Click **Add App**.
    
    The app now appears in the list of monitored apps.
    
 **To remove an app from the monitor apps list**
  
1. On the Monitored Apps page, select the checkbox next to the app that you want to remove.
    
2. In the **Manage** group of the ribbon, click **Remove App**.
    
## Monitoring app details in Central Administration
<a name="proc2"> </a>

This section explains how you can monitor and understand the apps for SharePoint details. There are multiple ways that you can view the error and usage details for apps for SharePoint. By selecting an app in the Monitored Apps page, you can use the ribbon to access the error or usage details for that app. You can also click an app in the list on the Monitored Apps page to open the app details page and access the same error or usage details.
  
The app usage and app error details data that is on the app monitoring pages can be delayed for up to 29 hours. The app details depend on when the ECM analytics timer job is scheduled to run. When the timer job runs, it collects events for the previous day. For example, if the timer job is scheduled to run at 5 A.M., then the most recent events that are collected are from 11:59 P.M. the previous day. An event that occurs at 12:01 A.M. will not appear in the app details pages until up to 29 hours later.
  
Note that if you view the app error details page for a specific instance of an app, the number of errors for the app is synchronized with the error messages in the list. This occurs because the number of errors appears in the app error details page instead of the events that are processed by the ECM analytics timer job.
  
> [!NOTE]
> Be aware that in the Monitored Apps page, the error dialog box can show more errors than are counted. The errors are counted every 24 hours, but the error messages are processed more often. As a result, the error dialog box can show error messages that are generated in the current day before the count is updated at the end of the day. 
  
 **To view the app usage details in Monitored Apps**
  
1. On the Monitored Apps page, click the app that you want to view.
    
    A new page opens and displays detailed information about the app, such as the following: licensing, errors, installations, and usage.
    
    > [!NOTE]
    > You can also select an app in the monitored apps list and in the **App Details** group of the ribbon, click **View Details**. 
  
2. In the **Usage** section, click **Days**, **Months**, or **Years** to change the chart to those time frames. 
    
 **To view the app error details in Monitored Apps**
  
1. On the Monitored Apps page, click the number in the Runtime Errors column for the app you want to view.
    
    > [!NOTE]
    > You can also select an app in the monitored apps list and in the App Details group of the ribbon, click **View Errors**. 
  
2. The App Monitoring Details dialog appears with information about each error for that app. You can use the Correlation ID to find the errors in the error log.
    
3. Click the URL in the Location column to view more error details for this app.
    
4. On the App Monitoring Details page, click the number next to **Runtime Errors**.
    
5. The App Monitoring Details dialog appears and includes a list of all Runtime Errors for this app, the time each error occurred, and the Correlation ID.
    
## Monitoring app details in a SharePoint site
<a name="proc3"> </a>

This section explains how site owners can monitor and understand the usage of apps for SharePoint. A site owner can view the error and usage details for apps for SharePoint by selecting an app in the Site Contents page and then clicking Monitor in the app dialog box.
  
> [!NOTE]
> Be aware that in the app details page, the error dialog box can show more errors than are counted. The errors are counted every 24 hours, but the error messages are processed more often. As a result, the error dialog box can show error messages that are generated in the current day before the count is updated at the end of the day. 
  
 **To view the app usage details in a SharePoint site**
  
1. On the Site Contents page, click the icon next to the app you want to monitor and then click **Details** in the callout. 
    
    The App Details page appears for the selected app and the site owner can see the details for licenses, errors Installs and usage.
    
2. In the **Errors** section, click the number next to Install Errors, Runtime Errors, or Upgrade Errors to see the error details. 
    
    This app error list can help you determine if you want to remove the app because there are too many errors or if the app is working as it should.
    
    > [!NOTE]
    > The app errors that appear in this list have occurred within the previous four days. 
  
3. In the **Usage** section, click **Days**, **Months**, or **Years** to change the chart to those time frames. 
    
    The chart displays two bars for each time period that represents the number of times the app has been launched and the number of specific users that use this app each day.
    
    > [!NOTE]
    > If the app uses connections to external data sources through Business Connectivity Services, a graph that shows the number of calls made to the external data sources is also shown. Dates that appear in the Usage and BCS Calls graphs are in Coordinated Universal Time (UTC). 
  
## See also
<a name="proc3"> </a>

#### Concepts

[Plan for apps for SharePoint Server](plan-for-apps-for-sharepoint.md)

