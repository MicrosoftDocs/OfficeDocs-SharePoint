---
title: "Overview of MinRole Server Roles in SharePoint Servers 2016 and 2019"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 01/26/2017
audience: ITPro
ms.topic: concetpual
ms.prod: sharepoint-server-itpro
localization_priority: Priority
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
- Strat_SP_server
- SP2019
ms.custom: 
ms.assetid: a590d614-7488-4b03-8c8f-d45dd48ca726
description: "Learn about the new MinRole farm topology and its benefits in SharePoint Server."
---

# Overview of MinRole Server Roles in SharePoint Servers 2016 and 2019

[!INCLUDE[appliesto-xxx-2016-2019-xxx-md](../includes/appliesto-xxx-2016-2019-xxx-md.md)]

Learn about the new MinRole farm topology and its benefits in SharePoint Servers 2016 and 2019.
  
## What is MinRole?

 **MinRole** is a new farm topology based on a set of predefined server roles introduced in SharePoint Server 2016. When configuring your SharePoint farm, you now select the role of a server when you create a new farm or join a server to an existing farm. SharePoint will automatically configure the services on each server based on the server's role. SharePoint Server 2016 and 2019 has been optimized for the MinRole farm topology. 
  
The following video gives a general overview what MinRole is and can do for your organization.
  
> [!VIDEO https://www.microsoft.com/videoplayer/embed/05c5d811-fbce-4bac-b95e-820acf941b01?autoplay=false]
## Benefits of using the MinRole farm topology

Some of the primary benefits to using MinRole are:
  
- **Simplified deployment**: Now you no longer need to worry about which services should be started on which servers. By deploying your farm in a recommended MinRole topology, you can focus on what functionality to enable in your farm and let SharePoint take care of the rest. 
    
- **Improved performance and reliability**: Microsoft has been operating SharePoint Online for years and has analyzed the performance characteristics of SharePoint under a variety of conditions, including CPU, memory, disk I/O, and network latency. SharePoint Servers 2016 and 2019 have been optimized for the MinRole farm topology based on that analysis. By deploying your farm in a recommended MinRole topology, you'll be able to reduce network latency and increase reliability. 
    
- **Simplified capacity planning and farm scalability**: Microsoft bases capacity planning on the MinRole topology. By deploying your farm in a recommended MinRole topology, you'll be able to leverage more predictable and prescriptive capacity-planning guidance. Plus, it's now easier to add servers into your farm as your needs grow because SharePoint automatically configures the additional servers for you. 
    
## How does MinRole simplify deployment?

MinRole automatically starts and stops service instances on each MinRole-managed server in your farm based on the server role. When you create a new farm or join a machine to an existing farm, SharePoint starts the base set of service instances that are required for the server's role. It also detects which additional services have been enabled in the farm and starts the matching service instances as appropriate for the server's role. Finally, it detects which service applications have been created in the farm and which services are necessary to support those service applications. Those service instances will be started as appropriate for the server's role, as well.
  
MinRole management of service instances doesn't happen only when you join a server to a farm. As you enable or disable services in the farm, or as you create and delete service applications in the farm, MinRole starts and stops service instances on the existing servers in the farm. This ensures that each server in your SharePoint farm is running exactly the services it needs.
  
The result is that SharePoint farm administrators can now focus on **what** services you want to run in your farm and not worry about **where** they're running. As long as you've deployed a supported MinRole farm topology, SharePoint will handle those details. 
  
## ﻿How does MinRole improve performance and reliability?

SharePoint often needs to communicate with service instances when serving requests. In previous releases, many service instances were typically hosted on separate servers, requiring cross-server connections from the front-end servers, which added latency. In addition, if one of the servers hosting those service instances was unhealthy, it could affect requests from multiple front-end servers, making it difficult to troubleshoot the issue and limit the impact on the rest of the farm.
  
MinRole improves this experience by hosting service instances appropriate for each server role on the local server. For example, service instances that are appropriate for user requests are hosted on the Front-end server role, while service instances appropriate for background tasks are hosted on the Application server role. When SharePoint needs to communicate with a service instance to serve a request, it detects ﻿if the service instance is hosted on the local server. If it is, it will always use that local service instance instead of a service instance hosted on a remote server.
  
﻿This ﻿design reduces latency by keeping ﻿traffic on the local ﻿server whenever possible. It also improves reliability by limiting the impact of unhealthy servers on the overall farm. Once an administrator determines that a server is unhealthy and removes it from the load balancer rotation, the remaining healthy servers can continue to ﻿serve requests and not be affected by the unhealthy server.
  
MinRole is also self-healing. ﻿MinRole scans each server in your farm once a day to confirm that it's running the service instances that it's supposed to be running. If it detects a server that's not compliant with its server role, it will automatically start or stop the necessary service instances to return it to compliance. The SharePoint farm administrator has full control over this health scan and can change ﻿how often the scan is performed, whether MinRole automatically fixes non-compliant servers or simply reports them to the farm administrator, and can disable the scan entirely.
  
## ﻿How does MinRole simplify capacity planning and farm scalability?

﻿Microsoft provides a variety of recommended MinRole farm topologies for our customers, including small, medium, and large-sized farms. To review the recommended MinRole farm topologies, see [Planning for a MinRole server deployment in SharePoint Servers 2016 and 2019](planning-for-a-minrole-server-deployment-in-sharepoint-server.md).
  
MinRole is also adaptable with ﻿built-in ﻿server role conversion. You can easily convert a server from one server role to another without having to disconnect a server from a farm and then rejoining it to the farm. Server role conversion can be performed through the Central Administration web site or Windows PowerShell.
  
## ﻿MinRole enhancements

﻿Starting with the November 2016 Public Update for SharePoint Server 2016, ﻿Microsoft has introduced the following enhancements to MinRole:
  
- Better support for small and medium-sized farm topologies via new shared roles. Now you can ﻿deploy a MinRole farm with just 2 servers, or a high availability (HA) MinRole ﻿farm with just 4 servers. For more ﻿information about these new roles and recommended MinRole farm topologies, see [Planning for a MinRole server deployment in SharePoint Servers 2016 and 2019](planning-for-a-minrole-server-deployment-in-sharepoint-server.md)﻿.
    
- ﻿An improved server role conversion experience via role conversion pre-validation. Now MinRole will check to ﻿ensure your ﻿server is ready for role conversion before starting the conversion. If it detects that the server isn't ready, it will block ﻿the conversion and ﻿present a message explaining why the role conversion was blocked, as well as instructions to resolve the issue. For more information about role conversion pre-validation, see [Role conversion using MinRole in SharePoint Servers 2016 and 2019](../administration/role-conversion-using-minrole-in-sharepoint-server-2016.md).
    
- ﻿Updated service instance assignments for each server role to ensure your farm is operating at optimal performance. For more information about the new service instance assignments, see [Description of MinRole and associated services in SharePoint Servers 2016 and 2019](../administration/description-of-minrole-and-associated-services-in-sharepoint-server-2016.md).
    
Microsoft recommends installing the November 2016 Public Update (or newer) for SharePoint Server 2016 to take full advantage of these MinRole enhancements.
  
## See also

#### Concepts

[Technical diagrams for SharePoint Server](../technical-reference/technical-diagrams.md)
  
[Description of MinRole and associated services in SharePoint Servers 2016 and 2019](../administration/description-of-minrole-and-associated-services-in-sharepoint-server-2016.md)
#### Other Resources

[Planning for a MinRole server deployment in SharePoint Servers 2016 and 2019](planning-for-a-minrole-server-deployment-in-sharepoint-server.md)
  
[Managing a MinRole Server Farm in SharePoint Servers 2016 and 2019](../administration/managing-a-minrole-server-farm-in-sharepoint-server-2016.md)

