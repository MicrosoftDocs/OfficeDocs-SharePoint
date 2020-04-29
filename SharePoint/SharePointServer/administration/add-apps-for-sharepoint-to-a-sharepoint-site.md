---
title: "Add apps for SharePoint to a SharePoint site"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 5/30/2017
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 57d52c9e-5069-4bcf-87e3-24482198a462
description: "Site owners can add apps for SharePoint to SharePoint sites so that they and other users of the site can use the app."
---

# Add apps for SharePoint to a SharePoint site

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
Site owners can add apps for SharePoint from the SharePoint Store or an App Catalog to their sites. Adding an app installs an instance of that app to the site. This article covers how to add apps to your sites.
  
Be sure you've [configured your environment for SharePoint apps](configure-an-environment-for-apps-for-sharepoint.md) before you get started. 
  
## Add apps for SharePoint to SharePoint sites

Site owners can add apps for SharePoint from the following sources to their sites:
  
- from the list of apps already available for a site (default apps, such as standard lists and libraries, and apps that have been purchased already).
    
- from the App Catalog.
    
- from the SharePoint Store.
    
Note that a user logged in as the system account cannot install an app.
  
When you add an app for SharePoint, the app requests permissions that it needs to function (for example, access to Search, or to create a list). If you don't have those permissions, the app won't install. Contact your administrator to get the needed permissions or have someone with those permissions add the app.
  
The following procedures provide steps for adding apps from these sources.
  
 **To add an app from the list of available apps in a site**
  
1. Verify that the user account that is performing this procedure is a member of the site Owners group.
    
2. On the home page, under **Get started with your site**, click **Add lists, libraries, and other apps.**
    
    If the Get started with your site control does not appear on the home page, click the **Settings** icon, and click **View Site Contents**, and then on the **Site Contents** page, click **Add an App**.
    
3. In the Your Apps list, click the app you want to add.
    
4. Follow the instructions to Trust the app (if it is a custom component) or Name the app (if it is a SharePoint component).
    
    The app for SharePoint is added and appears in the **Apps** section of your Site Contents list. 
    
 **To add an app from an App Catalog**
  
1. Verify that the user account that is performing this procedure is a member of the site Owners group.
    
2. On the home page, under **Get started with your site**, click **Add lists, libraries, and other apps.**
    
    If the Get started with your site control does not appear on the home page, click the Settings icon, and click **View Site Contents**, and then on the Site Contents page, click **Add an App**.
    
3. Click **From** _Name_.
    
    Where _Name_ is the name of your organization's App Catalog. For example, "From Contoso". 
    
    > [!TIP]
    > Apps marked as Featured in the App Catalog will also appear in the main list of Apps. 
  
4. Click the app you want to add.
    
5. In the Grant Permission to an App dialog, if you trust the app, click **Allow Access**.
    
    The app for SharePoint is added and appears in Apps section of your Site Contents list.
    
 **To add an app from the SharePoint Store**
  
1. Verify that the user account that is performing this procedure is a member of the site Owners group.
    
2. On the home page, under **Get started with your site**, click **Add lists, libraries, and other apps.**
    
    If the Get started with your site control does not appear on the home page, click the Settings icon, and click **View Site Contents**, and then on the Site Contents page, click **Add an App**.
    
3. Click **SharePoint Store**.
    
4. Browse the SharePoint Store to find an app that you want.
    
5. Click the app you want to add.
    
6. Click Details, and then click **Buy It**.
    
7. Follow the steps to log in and purchase the app, if required.
    
8. In the **Grant Permission to an App** dialog, if you trust the app, click **Allow Access**.
    
    The app for SharePoint is added and appears in the Apps section of your Site Contents list.
    
## See also

#### Concepts

[Install and manage apps for SharePoint Server](install-and-manage-apps-for-sharepoint-server.md)
#### Other Resources

[Import-SPAppPackage](/powershell/module/sharepoint-server/Import-SPAppPackage?view=sharepoint-ps)
  
[Install-SPApp](/powershell/module/sharepoint-server/Install-SPApp?view=sharepoint-ps)

