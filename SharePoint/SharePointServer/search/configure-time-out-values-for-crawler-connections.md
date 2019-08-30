---
title: "Configure time-out values for crawler connections in SharePoint Server"
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
ms.assetid: 5978d831-4070-4b03-a81c-dfce3b7d594e
description: "Change how long the SharePoint Server search crawler will wait for a connection to a content repository or for a response to a connection attempt."
---

# Configure time-out values for crawler connections in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
By default, when the crawler attempts to connect to a content repository, it waits 60 seconds for a connection or for a response to a connection attempt. Use the procedure in this article to change these crawler time-out values. 
  
If the crawler does not connect or get a response within the time specified, it tries to connect again. If the crawler does not connect on the second attempt within the time specified, it does not crawl the repository during that crawl.
  
**To configure time-out settings for crawler connections**
  
1. Verify that the user account that is performing this procedure is a farm administrator.
    
2. In Central Administration, in the Quick Launch, click **General Application Settings**.
    
3. On the General Application Settings page, in the **Search** section, click **Farm Search Administration**.
    
4. On the Farm Search Administration page, in the **Farm-Level Search Settings** section, click either of the **Time-out (seconds)** setting values. 
    
     ![Screenshot of crawler time-out settings on Farm Search Administration page](../media/CrawlerTimeoutSettings.gif)
  
5. In the **Search Time-out Setting** dialog box, do the following: 
    
  - In the **Connection time (in seconds)** text box, type the number of seconds that you want the crawler to wait when it attempts to connect to a content repository. The default value is 60 seconds. 
    
  - In the **Request acknowledgement time (in seconds)** text box, type the number of seconds that you want the crawler to wait for a content repository to respond to a connection attempt. The default value is 60 seconds. 
    
  - Click **OK**.
    
## See also

[Manage crawling in SharePoint Server](manage-crawling.md)

