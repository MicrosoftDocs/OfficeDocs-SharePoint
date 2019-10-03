---
title: "Web.config file has incorrect settings for the requestFiltering element (SharePoint Server)"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 8/31/2017
audience: ITPro
ms.topic: troubleshooting
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: f3625c2f-a588-422c-9fbe-0b83205fbc88
description: "Learn how to resolve the SharePoint Health Analyzer rule: Web.config file has incorrect settings for the requestFiltering element, for SharePoint Server."
---

# Web.config file has incorrect settings for the requestFiltering element (SharePoint Server)

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
 **Rule Name:** Web.config file has incorrect settings for the requestFiltering element. 
  
 **Summary:** To support file names that contain the + character, the requestFiltering element in the Web.config file must have the allowDoubleEscaping attribute set to **True** and it must have a requestLimits element that has a maxAllowedContentLength value set to 2147483647 to avoid interfering with file upload. 
  
 **Cause:** The settings of the requestFiltering element in the Web.config file are incorrect. 
  
 **Resolution: Change the requestFiltering settings in the Web.config file in Internet Information Services (IIS).**
  
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
2. Identify the server on which this event occurs. On the SharePoint Central Administration website, in the **Monitoring** section, click **Review problems and solutions**, and then find the name of the server in the **Failing Servers** column. If there are multiple failing servers in a server farm, you must repeat the following steps on each failing server. 
    
3. Verify that the user account that is performing the following steps is a member of the Administrators group on the local computer that you identified in the previous step.
    
4. Log on to the server on which this event occurs.
    
5. On **Server Manager**, click **Tools**, and then select **Internet Information Services (IIS) Manager**.
    
6. In the Internet Information Services management console, in the **Connections** pane, expand the tree view of the server name, expand **Sites**, and then click the site for which you want to change the requestFiltering settings.
    
7. On the site Home page, switch to **Features View**, and then in the **Management** section, double-click **Configuration Editor**.
    
8. In the **Section** list, expand **system.webServer**, expand **security**, and then click **requestFiltering**.
    
9. On the Configuration Editor page, ensure the following attributes or elements exist and are configured correctly:
    
  - The allowDoubleEscaping attribute is set to **True**.
    
  - The requestLimits element exists.
    
  - The requestLimits element has a maxAllowedContentLength attribute and its value is set to **2147483647**.
    
    For more information, see [How to: Add and Remove Web.config Settings Programmatically](http://go.microsoft.com/fwlink/p/?LinkID=227014).
    
10. After you have made changes to these settings, in the **Actions** pane, click **Apply**.
    

