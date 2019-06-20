---
title: "Configure Visio Services"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/6/2017
audience: ITPro
ms.topic: get-started-article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 2db321b3-1d59-4b3a-a242-8daabfde367c
description: "Configure Visio Services by using SharePoint Central Administration."
---

# Configure Visio Services

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
The following steps show how to create a Visio Graphics Service service application.
  
To create a service application, you must be a member of the farm administrators group.
  
## Create a Visio Services service application

 **To create a Visio Graphics Service service application by using Central Administration**
  
1. On the SharePoint Central Administration website Home page, in the **Application Management** section, click **Manage service applications**.
    
    > [!IMPORTANT]
    > Visio Services requires the SharePoint Server Enterprise Site Collection Features feature to be active on each site collection where you plan to use the Visio Web Access Web Part. 
  
2. On the ribbon, click **New**, and then click **Visio Graphics Service**.
    
3. Type a name for the new service application.
    
4. Choose an existing application pool or create a new one.
    
5. Choose whether to create a Visio Graphics Service Application Proxy (recommended).
    
6. Click **OK**.
    
If you are using SharePoint Server 2013, you must turn on the Visio Graphics Service on at least one server in your farm. (In Central Administration, click **Manage services on server**.) If you are using SharePoint Server 2016, the Visio Graphics Service is managed automatically by MinRole.
  
## Configure Visio Services Global Settings

 **To configure Visio Services Global Settings**
  
1. On the SharePoint Central Administration website Home page, in the **Application Management** section, click **Manage service applications**.
    
2. Click the Visio Graphics Service service application that you want to configure.
    
3. On the Visio Graphics Service Settings page, configure the following settings:
    
|**Parameter**|**Description**|
|:-----|:-----|
|**Maximum Diagram Size** <br/> |The maximum size in MB of a diagram that can be rendered. A larger size limit may lead to slower performance if the server is under heavy load, whereas a smaller limit may prevent more complex diagrams from being rendered.  <br/> Valid values range from 1 to 50. The default value is 25 MB.  <br/> |
|**Minimum Cache Age** <br/> |The minimum number of minutes that a diagram is cached in memory. Smaller values allow for more frequent data refresh operations for users, but increase CPU and memory usage on the server.  <br/> This value is per user per diagram. The interval begins when a user views a diagram. That user cannot refresh that diagram until the interval expires. The interval begins for other users when they first view the diagram.  <br/> This parameter applies to diagrams with data connections and diagrams with recalculations based on shape sheet functions. The automatic refresh setting in Visio Web Parts is also constrained by this setting.  <br/> Valid values range from 0 to 34560 minutes. The default value is 5 minutes.  <br/> |
|**Maximum Cache Age** <br/> |The number of minutes after which cached diagrams are purged. Larger values decrease file I/O and CPU load but increase memory usage on the server.  <br/> Valid values range from 0 to 34560 minutes. The default value is 60 minutes.  <br/> |
|**Maximum Recalc Duration** <br/> |The number of seconds before data refresh operations time out. Longer timeouts will allow for more complex data connected diagrams to be recalculated, but will use more processing power. This applies only to data connected diagrams.  <br/> This parameter applies to diagrams with data connections and diagrams with recalculations based on shape sheet functions.  <br/> Valid values range from 10 to 120. The default value is 60 seconds.  <br/> |
|**Maximum Cache Size** <br/> |The maximum cache size in MB (between 100 and 1024000) that can be used. A larger size limit may lead to more disk resource usage by the service, while a smaller limit may impact performance.  <br/> Valid values range from 100 to 1024000. The default value is 5120 MB.  <br/> |
|**External Data** <br/> |The target application ID in the registered Secure Store Service that is used to reference Unattended Service Account credentials. The Unattended Service Account is a single account that all documents can use to refresh data. It is required when you connect to data sources external to SharePoint Server, such as SQL Server.  <br/> |
   
4. Click **OK**.
    

