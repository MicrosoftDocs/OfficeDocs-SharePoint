---
title: "Monitor apps for your SharePoint environment"
ms.reviewer: 
ms.author: kaarins
author: kaarins
manager: pamgreen
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
search.appverid:
- SPO160
- MET150
ms.assetid: 81daca87-ef0c-4602-af89-9a749dbef377
description: "Learn how to monitor app usage and error information for the apps being used in your SharePoint environment."
---

# Monitor apps for your SharePoint environment

As a SharePoint or global admin in Office 365, you can monitor information such as app usage and error information for the apps that are in use in your SharePoint environment. Before you can monitor information about an app, you need to add it to the list of apps you want to monitor.
  
## Select apps to monitor
<a name="__top"> </a>

1. Go to the [More features page of the new SharePoint admin center](https://admin.microsoft.com/sharepoint?page=classicfeatures&modern=true) and sign in with an account that has [admin permissions](/sharepoint/sharepoint-admin-role) for your organization.

>[!NOTE]
>If you have Office 365 Germany, [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=848041), then browse to the SharePoint admin center and open the More features page. <br>If you have Office 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the More features page.
 
2. Under **Apps**, click **Open**.
    
3. Select **Monitor Apps**.
    
4. To add apps to the list, select **Add App**. 
    
5. Search for the app(s) you want to add, or select from the list of available apps, and then select **Add**.
    
## View app details or errors
<a name="__top"> </a>

1. Go to the [More features page of the new SharePoint admin center](https://admin.microsoft.com/sharepoint?page=classicfeatures&modern=true) and sign in with an account that has [admin permissions](/sharepoint/sharepoint-admin-role) for your organization.

>[!NOTE]
>If you have Office 365 Germany, [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=848041), then browse to the SharePoint admin center and open the More features page. <br>If you have Office 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the More features page.
 
2. Under **Apps**, click **Open**. 
  
3. Select **Monitor Apps**.
    
4. Point to the app for which you want to view information, select the check box that appears, and then do one of the following
    
|****To do this:****|****Do this:****|
|:-----|:-----|
| View the details about the app such as:  <br/>  number of licenses purchased or used  <br/>  counts of errors and installs  <br/>  usage information  <br/> | Select **View Details** on the ribbon. In the **Usage** section, select **Days**, **Months**, or **Years** to change the timeframe for the usage information that displays in the chart. |
|View error information for an app  <br/> | Select **View Errors** on the ribbon. You can use the Correlation ID to find the errors in the error log. Select the URL in the **Location** column to view more error details for this app. |
   
> [!NOTE]
> If you no longer want to monitor an app, you can select it on the Monitor Apps page, and select **Remove App** on the ribbon. <br>
    
App usage and error detail information is processed by different timer jobs that are pre-configured to run at set times for SharePoint. These timer jobs pick up events for the previous day. For this reason, the data visible on the Monitor Apps page may be delayed for up to 29 hours.
