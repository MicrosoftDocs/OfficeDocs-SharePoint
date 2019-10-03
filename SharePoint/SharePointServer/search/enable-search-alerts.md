---
title: "Enable search alerts in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 3/7/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 73cfd7b3-be90-480a-b415-039fa97d9b89
description: "Learn how to enable or disable search alerts."
---

# Enable search alerts in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
Search alerts allow end-users to receive e-mail notification when specified search query results are changed or updated. Search alerts should be enabled when you want allow end-users to create alerts for search queries. Search alerts may be configured on the search query page when a search query is completed and results are displayed. Search alerts are created and configured per-user and are only configurable and viewable by the user who creates them. Search alerts are enabled by default. Use this procedure to enable or disable search alerts.
  
    
## Before you begin
<a name="begin"> </a>

Before you begin this operation, have this in place:
  
- A Search service application 
    
- A User Profile service application
    
### To enable or disable search alerts

1. Verify that the user account that is performing this procedure is an administrator for the Search service application.
    
2. In Central Administration, in the **Application Management** section, click **Manage service applications**.
    
3. On the Manage Service Applications page, click the Search service application for which you want to configure search alerts. 
    
4. On the Search Administration page, in the **System Status** section, locate **Search alerts status**.
    
5. The search alerts status displays as **Off** **Enable** or **On** **Disable**. 
    
6. By default, search alerts are turned **On**. Click **Disable** to turn off search alerts or click **Enable** to turn on search alerts. 
    
The option is now set. Search alerts are sent only if outgoing e-mail is configured. For more information, see [Configure outgoing email for a SharePoint Server farm](../administration/outgoing-email-configuration.md). If you enabled search alerts, users can create search alerts for search queries that they run. To configure search alerts for search queries, users can click the **Alert Me** link that is located on the bottom of the Search Results page. The **Alert Me** link will appear a few minutes after search alerts are turned on. If search alerts are turned off, this icon does not appear. 
  

