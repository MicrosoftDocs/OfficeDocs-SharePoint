---
title: "Monitor and manage app licenses in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/27/2017
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: a8c86550-d709-4333-9b38-181590d5ead9
description: "Learn how SharePoint Server farm administrators assign, monitor, and manage the app for SharePoint Server licenses in SharePoint Server."
---

# Monitor and manage app licenses in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
You can use the SharePoint Central Administration website to monitor and manage licenses for apps for SharePoint. Licenses for apps for SharePoint are digital sets of verifiable information that state the user rights for a app for SharePoint. Apps that are distributed through the SharePoint Store are the only apps that have built-in licenses that SharePoint Server recognizes.
  
Members of the Farm Administrators group manage licenses for apps and can also assign license managers for others to manage app for SharePoint licenses.
  
Here are the basics of what SharePoint Server does and does not provide for apps for SharePoint licensing:
  
- SharePoint Server provides:
    
  - Storefront to obtain apps
    
  - Storage and renewal of app for SharePoint licenses
    
  - User Interface (UI) to assign users to specific app for SharePoint licenses
    
  - APIs for developers to query for license information
    
- SharePoint Server does not enforce app for SharePoint licenses.
    
- Developers must add code in their apps for SharePoint to retrieve license information and react accordingly.
    
- All app for SharePoint licenses are bound to a specific SharePoint Server deployment but can be transferred to a different SharePoint Server deployment three times.
    
## Monitoring and managing app licenses
<a name="proc1"> </a>

A farm administrator or a license manager can check the licenses for all apps for SharePoint on the App Licenses page. It is important to track the number of licenses that are available for each app for SharePoint so that users do not exceed this number. An administrator can assign additional users to a app for SharePoint license, purchase additional licenses for an app, and also add managers to a license.
  
 **To view app license details**
  
1. In Central Administration, click **Apps**.
    
2. On the **Apps** page, in the **SharePoint and Office Store** section, click **Manage App Licenses**.
    
3. On the **Manage App Licenses** page, click an app for SharePoint in the list to view the license details. 
    
    The **Manage App License** page shows detailed licensing information. This includes the name of the app, the developer, and current license details. 
    
4. In the top section, click the drop-down arrow in the dialog box to see purchase details for the selected app for SharePoint.
    
    The app details include the following information:
    
  - Number of licenses available for users
    
  - License type
    
  - App purchaser name
    
 **To add users to the app license**
  
1. On the **Manage App Licenses** page, click an app for SharePoint for which you want to add users. 
    
2. In the **People with a License** section, click **assign people**.
    
3. In the dialog box that appears below, enter the user name that you want to add and then, click **Add User**.
    
    The user name is added to the list at the bottom of this section and the number of available licenses for this app is refreshed for the selected app for SharePoint.
    
 **To purchase more app licenses**
  
1. On the **Manage App Licenses** page, click an app for SharePoint for which you want to purchase more licenses. 
    
2. In the **People with a License** section, click **buy more licenses**.
    
3. The SharePoint Store opens with the specific app showing the details with links to purchase additional licenses. Choose the number of Apps you want to purchase and then click **OK**.
    
 **To remove app licenses**
  
1. On the **Manage App Licenses** page, click an app for SharePoint for which you want to remove licenses. 
    
2. On the **Actions** drop down list, click **Remove this License**.
    
3. **Verification:** Optionally, include steps that users should perform to verify that the operation was successful. 
    
 **To recover app licenses**
  
1. On the **Manage App Licenses** page, click an app for SharePoint for which you want to recover licenses. 
    
2. On the **Actions** drop down list, click **Recover License**.
    
    The app for SharePoint details show any changes the administrator has made.
    
 **To add a license manager**
  
1. On the **Manage App License** page, in the **License Managers** section, click **add manager**.
    
    Below the License Managers section, the new App manager appears in the list.
    
## See also
<a name="proc1"> </a>

#### Concepts

[Configure an environment for apps for SharePoint Server](configure-an-environment-for-apps-for-sharepoint.md)

