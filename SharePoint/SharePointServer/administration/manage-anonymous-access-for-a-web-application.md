---
title: "Manage anonymous access for a web application in SharePoint Server"
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
ms.assetid: 8b35493f-45d2-428f-b17b-55d69ee11138
description: "Learn how to grant or deny anonymous access to a web application in SharePoint Server."
---

# Manage anonymous access for a web application in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
You can enable or disable anonymous access for a web application. If you enable anonymous access for a web application, site administrators can then grant or deny anonymous access at the site collection, site, or item level. If anonymous access is disabled for a web application, no sites within that web application can be accessed by anonymous users. 

    > [!NOTE]
    > Both classic and modern experience sites support anonymous access.

The following permission policies can be specified for anonymous users:
  
- **None:** No policy is specified. This setting gives anonymous users the same default permissions available to NT AUTHORITY\Authenticated Users and All Authenticated Users. 
    
- **Deny Write:** This setting enables anonymous users to read all content within the site collections in a web application. You can then restrict the Read access by site collection, site, or item. 
    
- **Deny All:** Anonymous users have no access to any part of the web application. 
    
Use the following procedure to configure anonymous access for a web application.
  
 **To configure anonymous access for a web application**
  
1. Start SharePoint 2016 Central Administration.
    
2. On the SharePoint Central Administration website, in the **Application Management** section, click **Manage web applications**.
    
3. Click to highlight the web application whose permission policy that you want to manage.
    
4. In the **Security** group of the ribbon, click **Authentication Providers**.
    
5. Click the zone where you want to enable anonymous access.
    
6. Ensure that the **Enable anonymous access** check box is selected, and click **OK**.
    
7. In the **Policy** group of the ribbon, click **Anonymous Policy**.
    
8. In the Anonymous Access Restrictions dialog box, in the ** Zone ** list, click the zone for which you want the policy to apply. 
    
9. In the **Permissions** section, select the permission policy that you want anonymous users to have, and then click **Save**.
    

