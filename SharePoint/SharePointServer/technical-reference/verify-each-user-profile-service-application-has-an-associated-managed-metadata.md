---
title: "Verify each User Profile Service Application has an associated Managed Metadata Service Connection (SharePoint Server)"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 8/30/2017
audience: ITPro
ms.topic: troubleshooting
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 63f233ef-8a72-449e-8211-c66fea977b6e
description: "Learn how to resolve the SharePoint Health Analyzer rule: Verify each User Profile Service Application has an associated Managed Metadata Service Connection, for SharePoint Server."
---

# Verify each User Profile Service Application has an associated Managed Metadata Service Connection (SharePoint Server)

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
 **Rule Name:** Verify each User Profile Service Application has an associated Managed Metadata Service Connection. 
  
 **Summary:** If the Managed Metadata service is not associated with the User Profile service application, features such as social tagging and properties backed by managed terms do not work. 
  
 **Cause:** The Managed Metadata service connection is not included in the group of connections that is associated with the User Profile service application. 
  
 **Resolution: Edit the connections for the User Profile service application.**
  
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
2. On the Central Administration home page, click **Application Management**.
    
3. On the Application Management page, in the **Service Applications** section, click **Configure service application associations**.
    
4. On the Service Application Associations page, in the **View** list, click **Service Applications**.
    
5. In the **Web Application/Service Application** column, click the User Profile service application for which you want to edit the connection. 
    
6. In the **Configure Service Application Associations** dialog box, select the **Managed Metadata Service** check box, or select **Default** in the **Edit the following group of connections** list, and then click **OK**. By default, all connections are included.
    

