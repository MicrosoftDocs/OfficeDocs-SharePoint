---
title: "Enable query logging in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 9/11/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 6259e195-2b83-454f-b635-8f228c1fd1ac
description: "Learn how to enable or disable query logging."
---

# Enable query logging in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
SharePoint Server search collects information about user search queries and search results that users select on their computers. SharePoint Server uses this information to improve the relevance of search results and to improve query suggestions. Site collection administrators, tenant administrators and administrators of the Search service application can also create reports based on this information. Query logging is enabled by default. Use this procedure to enable or disable query logging.
  
 **To enable or disable query logging**
  
1. Verify that the user account performing this procedure is an administrator for the Search service application.
    
2. In Central Administration, in the **Application Management** section, click **Manage service applications**.
    
3. On the Manage Service Applications page, click the Search service application for which you want to configure query logging.
    
4. On the Search Administration page, in the **System Status** section, locate **Query logging**.
    
5. The **Query logging** status displays as **Off** **Enable** or **On** **Disable**. 
    
6. By default, query logging is turned **On**. Click **Disable** to turn off query logging or click **Enable** to turn on query logging. 
    
The option is set and no other actions are necessary. User search queries and user selected results will no longer be logged if you clicked **Disable**, or will now be logged if you clicked **Enable**. 
  

