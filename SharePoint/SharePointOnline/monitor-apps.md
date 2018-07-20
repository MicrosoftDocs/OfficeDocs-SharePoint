---
title: "Monitor apps for your SharePoint Online environment"
ms.author: kaarins
author: kaarins
manager: pamgreen
ms.date: 5/22/2018
ms.audience: Admin
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
search.appverid:
- SPO160
- MET150
ms.assetid: 81daca87-ef0c-4602-af89-9a749dbef377
description: "This article explains how the SharePoint Online admin can monitor thigns like app usage and error information for the apps that are in use in a SharePoint Online environment."
---

# Monitor apps for your SharePoint Online environment

As a SharePoint Online admin, you can monitor information such as app usage and error information for the apps that are in use in your SharePoint Online environment. Before you can monitor information about an app, you need to add it to the list of apps you want to monitor.
  
## Select apps to monitor
<a name="__top"> </a>

1. Sign in to Office 365 as a global admin or SharePoint admin.
    
2. Select the app launcher icon ![The app launcher icon in Office 365](media/e5aee650-c566-4100-aaad-4cc2355d909f.png) in the upper-left and choose **Admin** to open the Office 365 admin center. (If you don't see the Admin tile, you don't have Office 365 administrator permissions in your organization.) 
    
3. Select **Apps** on the left, and then select **Monitor Apps**.
    
4. To add apps to the list, select **Add App**. 
    
5. Search for the app(s) you want to add, or select from the list of available apps, and then select **Add**.
    
## View app details or errors
<a name="__top"> </a>

1. Sign in to Office 365 as a global admin or SharePoint admin.
    
2. Select the app launcher icon ![The app launcher icon in Office 365](media/e5aee650-c566-4100-aaad-4cc2355d909f.png) in the upper-left and choose **Admin** to open the Office 365 admin center. (If you don't see the Admin tile, you don't have Office 365 administrator permissions in your organization.) 
    
3. Select **Apps** on the left, and then select **Monitor Apps**.
    
4. Point to the app for which you want to view information, select the check box that appears, and then do one of the following
    
|****To do this:****|****Do this:****|
|:-----|:-----|
| View the details about the app such as:  <br/>  number of licenses purchased or used  <br/>  counts of errors and installs  <br/>  usage information  <br/> |
Select View Details on the ribbon. In the Usage section, select Days, Months, or Years to change the timeframe for the usage information that displays in the chart. |
|View error information for an app  <br/> |
Select View Errors on the ribbon. You can use the Correlation ID to find the errors in the error log. Select the URL in the Location column to view more error details for this app. |
   
 **Good to know:**
  
- If you no longer want to monitor an app, you can select it on the Monitor Apps page, and select **Remove App** on the ribbon. 
    
- App usage and error detail information is processed by different timer jobs that are pre-configured to run at set times for SharePoint Online. These timer jobs pick up events for the previous day. For this reason, the data visible on the Monitor Apps page may be delayed for up to 29 hours.
    

