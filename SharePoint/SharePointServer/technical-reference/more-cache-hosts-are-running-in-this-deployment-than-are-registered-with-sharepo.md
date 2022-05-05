---
title: "More cache hosts are running in this deployment than are registered with SharePoint (SharePoint Server)"
ms.reviewer: 
ms.author: serdars
author: SerdarSoysal
manager: serdars
ms.date: 12/5/2017
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: troubleshooting
ms.prod: sharepoint-server-itpro
ms.localizationpriority: medium
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 5e7be5ff-5216-406b-9bfe-f9ff1f9651aa
description: "Learn how to resolve the SharePoint Health Analyzer rule: More Cache hosts are running in this deployment than are registered with SharePoint, for SharePoint Server."
---

# More cache hosts are running in this deployment than are registered with SharePoint (SharePoint Server)

[!INCLUDE[appliesto-2013-2016-2019-SUB-xxx-md](../includes/appliesto-2013-2016-2019-SUB-xxx-md.md)]
  
 **Rule Name:** More Cache hosts are running in this deployment than are registered with SharePoint. 
  
 **Summary:** Some cache hosts are running but not registered with SharePoint Server. 
  
 **Cause:**SharePoint Server fails to identify some cache hosts.
  
 **Resolution: Log on to the cache host that is not registered with SharePoint Server, and then manually stop the AppFabric Caching Service.**
  
1. Identify the cache hosts that are not registered with SharePoint Server. To do this, in the SharePoint Central Administration website, in the **Monitoring** section, click **Review problems and solutions**, and then find the name of the server in the **Failing Servers** list. If there are multiple failing servers in a server farm, you must repeat the following steps on each failing server. 
    
2. Verify that the user account that is performing this procedure is a member of the Administrators group on the local computer.
    
3. On **Server Manager**, click **Tools**, and then select **Services**.
    
4. In the **Services** list, double-click **AppFabric Caching Service**.
    
5. In the **AppFabric Caching Service Properties (Local Computer)** dialog, click **Stop**.
    
## See also
<a name="server"> </a>

#### Concepts

[Manage the Distributed Cache service in SharePoint Server](../administration/manage-the-distributed-cache-service.md)
  
[Plan for feeds and the Distributed Cache service in SharePoint Server](../administration/plan-for-feeds-and-the-distributed-cache-service.md)
#### Other Resources

[Planning and using the Distributed Cache service](https://go.microsoft.com/fwlink/p/?LinkID=271302)

