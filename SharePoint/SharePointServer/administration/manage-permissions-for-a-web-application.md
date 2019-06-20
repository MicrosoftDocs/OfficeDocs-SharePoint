---
title: "Manage permissions for a web application in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/6/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 28a53440-2adc-4957-84bd-99ed97f0c430
description: "Learn how to globally enable or disable permissions for SharePoint Server web applications."
---

# Manage permissions for a web application in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
Sites and site collections have a variety of permissions that you can set, such as adding or editing list items or documents. These permissions are normally given to a user by assigning them to a particular permission level, such as Full Control, Contribute, or View Only.
  
Each individual permission can be enabled or disabled for an entire web application. (All permissions are enabled by default.) For example, if you know that you'll never be using the Client Object Model or SharePoint Designer to access your sites, you can disable the Use Remote Interfaces permission. Doing so will prevent that permission from being granted to any users regardless of which permission level they're assigned.
  
If you want to set permissions for specific users or groups in a web application, you can [create a permission policy for the web application](manage-permission-policies-for-a-web-application.md).
  
Use the following procedure to update the user permissions for a web application. Be sure you're a member of the Farm Administrator's group before following this procedure.
  
 **To manage permissions for a web application**
  
1. Start SharePoint 2016 Central Administration.
    
2. On the SharePoint Central Administration website, in the **Application Management** section, click **Manage web applications**.
    
3. In the web applications list, click the web application for which you want to manage permissions.
    
4. In the **Security** group of the ribbon, click **User Permissions**.
    
5. In the **User Permissions for Web Application** dialog box, select the check boxes next to the permissions that you want to enable, and clear the check boxes next to those permissions that you want to disable. 
    
    You can select all permissions by selecting the **Select All** check box. You can clear all permissions by clearing the **Select All** check box. 
    
6. Click **Save**.
    
## See also

#### Concepts

[Administration of SharePoint Server](administration.md)
  
[Manage permission policies for a web application in SharePoint Server](manage-permission-policies-for-a-web-application.md)

