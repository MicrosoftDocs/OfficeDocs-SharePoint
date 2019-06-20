---
title: "Monitor apps for your SharePoint Online environment"
ms.reviewer: 
ms.author: kaarins
author: kaarins
manager: pamgreen
audience: Admin
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
search.appverid:
- SPO160
- MET150
ms.assetid: 81daca87-ef0c-4602-af89-9a749dbef377
description: "Learn how to monitor app usage and error information for the apps being used in your SharePoint Online environment."
---

# Monitor apps for your SharePoint Online environment

As a SharePoint or global admin in Office 365, you can monitor information such as app usage and error information for the apps that are in use in your SharePoint Online environment. Before you can monitor information about an app, you need to add it to the list of apps you want to monitor.
  
## Select apps to monitor
<a name="__top"> </a>

1. Sign in to https://admin.microsoft.com as a global or SharePoint admin. (If you see a message that you don't have permission to access the page, you don't have Office 365 administrator permissions in your organization.)
    
    > [!NOTE]
    > If you have Office 365 Germany, sign in at https://portal.office.de. If you have Office 365 operated by 21Vianet (China), sign in at https://login.partner.microsoftonline.cn/. Then select the Admin tile to open the admin center.  
    
2. In the left pane, under **Admin centers**, select **SharePoint**. (You might need to select **Show all** to see the list of admin centers.) If this opens the new SharePoint admin center, select **Classic SharePoint admin center** in the left pane.
      
3. In the left pane, select **apps**. 
    
4. Select **Monitor Apps**.
    
5. To add apps to the list, select **Add App**. 
    
6. Search for the app(s) you want to add, or select from the list of available apps, and then select **Add**.
    
## View app details or errors
<a name="__top"> </a>

1. Sign in to https://admin.microsoft.com as a global or SharePoint admin. (If you see a message that you don't have permission to access the page, you don't have Office 365 administrator permissions in your organization.)
    
    > [!NOTE]
    > If you have Office 365 Germany, sign in at https://portal.office.de. If you have Office 365 operated by 21Vianet (China), sign in at https://login.partner.microsoftonline.cn/. Then select the Admin tile to open the admin center.  
    
2. In the left pane, under **Admin centers**, select **SharePoint**. (You might need to select **Show all** to see the list of admin centers.) If this opens the new SharePoint admin center, select **Classic SharePoint admin center** in the left pane.
      
3. In the left pane, select **apps**. 
    
4. Select **Monitor Apps**.
    
5. Point to the app for which you want to view information, select the check box that appears, and then do one of the following
    
|****To do this:****|****Do this:****|
|:-----|:-----|
| View the details about the app such as:  <br/>  number of licenses purchased or used  <br/>  counts of errors and installs  <br/>  usage information  <br/> | Select **View Details** on the ribbon. In the **Usage** section, select **Days**, **Months**, or **Years** to change the timeframe for the usage information that displays in the chart. |
|View error information for an app  <br/> | Select **View Errors** on the ribbon. You can use the Correlation ID to find the errors in the error log. Select the URL in the **Location** column to view more error details for this app. |
   
> [!NOTE]
> If you no longer want to monitor an app, you can select it on the Monitor Apps page, and select **Remove App** on the ribbon. <br>
    
App usage and error detail information is processed by different timer jobs that are pre-configured to run at set times for SharePoint Online. These timer jobs pick up events for the previous day. For this reason, the data visible on the Monitor Apps page may be delayed for up to 29 hours.
    

