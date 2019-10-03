---
title: "Verify that OAuth is configured correctly for the Machine Translation Service application proxy (SharePoint Server)"
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
ms.assetid: d7b9c8dd-274a-46ec-a8f6-28b7f5f0fa9e
description: "Learn how to resolve the SharePoint Health Analyzer rule: Verify that OAuth is configured correctly for the Machine Translation Service application proxy, for SharePoint Server."
---

# Verify that OAuth is configured correctly for the Machine Translation Service application proxy (SharePoint Server)

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
 **Rule Name:** Verify that OAuth is configured correctly for the Machine Translation Service application proxy. 
  
 **Summary:** The Machine Translation Service application proxy that is provisioned on the farm can function correctly only when OAuth is correctly configured. 
  
 **Cause:** OAuth is not configured correctly for the Machine Translation Service application proxy. 
  
 **Resolution: Ensure that every Web application with a Machine Translation Service application proxy has a connection to a User Profile service application and an App Management service application, and is in claims-based authentication mode.**
  
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
2. On the SharePoint Central Administration website, click **Application Management**.
    
3. On the Application Management page, in the **Service Applications** section, click **Configure service application associations**.
    
4. In the **Application Proxy Group** column, click the proxy group for the Web application or service application that you want to configure. Usually it is the **default** Application Proxy Group. 
    
5. Select the **User Profile Service Application Proxy** check box and the **App Management Service Application Proxy** check box. 
    
6. Go back to Central Administration and in the **Application Management** section, click **Manage web applications**.
    
7. Click the Web application you want to configure, and then click the **Authentication Providers** button on the ribbon. 
    
8. Ensure that the Membership Provider Name for the **Default** zone is **Claims Based Authentication**. If not, you have to migrate the Web applications from classic mode to claims-based authentication. For more information, see [Migrate from classic-mode to claims-based authentication in SharePoint Server](/previous-versions/office/sharepoint-server-2010/gg251985(v=office.14)).
    

