---
title: "Description of MinRole and associated services in SharePoint Servers 2016 and 2019"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/24/2018
audience: ITPro
ms.topic: overview
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 00c33e26-dacb-47d4-97b8-84659095b108
description: "Learn about the MinRole feature in SharePoint Server and the services that are associated with each server role."
---

# Description of MinRole and associated services in SharePoint Servers 2016 and 2019

[!INCLUDE[appliesto-xxx-2016-2019-xxx-md](../includes/appliesto-xxx-2016-2019-xxx-md.md)] 
  
The MinRole feature in SharePoint Servers 2016 and 2019 lets SharePoint farm administrators assign each server's role in a farm topology. The role of a server is specified when you create a new farm or join a server to an existing farm.
  
This article describes the services associated with each server role. These services are listed in Central Administration -> System settings -> Manage services in this farm, or by running the Get-SPService cmdlet. The service instances for some services are hidden because they are internal to the operation of SharePoint and not meant to be directly controlled. To retrieve a list of services instances on a server, including hidden services, use this syntax,  `(Get-SPServer <server_name>).ServiceInstances`.
  
> [!NOTE]
> The services listed is the list of what will be running on each server role if all of the services are enabled. Services associated with service applications will only be enabled if the farm administrator provisions that service application. Services that aren't associated with service applications will only be running if Auto Provision is enabled on that service. 
  
For additional information about the MinRole feature in SharePoint Server 2016, see [Overview of MinRole Server Roles in SharePoint Servers 2016 and 2019](../install/overview-of-minrole-server-roles-in-sharepoint-server.md).
  
## MinRole and associated services for each server role

The following table shows the services for each server role.
  
|**Server role**|**Services**|
|:-----|:-----|
|Front-end  <br/> | Access Services  <br/>  Access Services 2010  <br/>  App Management Service  <br/>  Business Data Connectivity Service  <br/>  Claims to Windows Token Service  <br/>  Machine Translation Service  <br/>  Managed Metadata Web Service  <br/>  Microsoft SharePoint Foundation Administration  <br/>  Microsoft SharePoint Foundation Sandboxed Code Service  <br/>  Microsoft SharePoint Foundation Subscription Settings Service  <br/>  Microsoft SharePoint Foundation Timer  <br/>  Microsoft SharePoint Foundation Web Application  <br/>  Microsoft SharePoint Insights  <br/>  PerformancePoint Service  <br/>  Project Server Application Service  <br/>  Request Management  <br/>  Secure Store Service  <br/>  User Profile Service  <br/>  Visio Graphics Service  <br/> **Note**: The list of **hidden services** are:  <br/>  Information Management Policy Configuration Service  <br/>  Microsoft Project Server Calculation Service  <br/>  Microsoft Project Server Events Service  <br/>  Microsoft Project Server Queuing Service  <br/>  Microsoft SharePoint Foundation Tracing  <br/>  Microsoft SharePoint Foundation Usage  <br/>  Portal Service  <br/>  Security Token Service  <br/>  SSP Job Control Service  <br/> |
|Application  <br/> | App Management Service  <br/>  Application Discovery and Load Balancer Service  <br/>  Business Data Connectivity Service  <br/>  Claims to Windows Token Service  <br/>  Machine Translation Service  <br/>  Managed Metadata Web Service  <br/>  Microsoft SharePoint Foundation Administration  <br/>  Microsoft SharePoint Foundation Incoming E-Mail  <br/>  Microsoft SharePoint Foundation Subscription Settings Service  <br/>  Microsoft SharePoint Foundation Timer  <br/>  Microsoft SharePoint Foundation Web Application  <br/>  Microsoft SharePoint Foundation Workflow Timer Service  <br/>  Microsoft SharePoint Insights  <br/>  PowerPoint Conversion Service  <br/>  Project Server Application Service  <br/>  Request Management  <br/>  Secure Store Service  <br/>  User Profile Service  <br/>  Word Automation Services  <br/> **Note**: The list of **hidden services** are:  <br/>  Information Management Policy Configuration Service  <br/>  Microsoft Project Server Calculation Service  <br/>  Microsoft Project Server Events Service  <br/>  Microsoft Project Server Queuing Service  <br/>  Microsoft SharePoint Foundation Tracing  <br/>  Microsoft SharePoint Foundation Usage  <br/>  Portal Service  <br/>  Security Token Service  <br/>  SSP Job Control Service  <br/> |
|Distributed cache  <br/> | Distributed Cache  <br/>  Microsoft SharePoint Foundation Administration  <br/>  Microsoft SharePoint Foundation Timer  <br/>  Microsoft SharePoint Insights  <br/> **Note**: The list of **hidden services** are:  <br/>  Microsoft SharePoint Foundation Tracing  <br/>  Microsoft SharePoint Foundation Usage  <br/>  Portal Service  <br/>  Security Token Service  <br/>  SSP Job Control Service  <br/> **Note**: If the November 2016 Public Update for SharePoint Server 2016 (Feature Pack 1) or higher is not installed, the following services will also be assigned to this role:  <br/>  Claims to Windows Token Service  <br/>  Microsoft SharePoint Foundation Web Application  <br/>  Request Management  <br/> |
|Search  <br/> | Application Discovery and Load Balancer Service  <br/>  Microsoft SharePoint Foundation Timer  <br/>  Microsoft SharePoint Insights  <br/>  Search Administration Web Service  <br/>  Search Host Controller Service  <br/>  Search Query and Site Settings Service  <br/>  SharePoint Server Search  <br/> **Note**: The list of **hidden services** are:  <br/>  Microsoft SharePoint Foundation Tracing  <br/>  Microsoft SharePoint Foundation Usage  <br/>  Portal Service  <br/>  Security Token Service  <br/>  SSP Job Control Service  <br/> **Note**: If the November 2016 Public Update for SharePoint Server 2016 (Feature Pack 1) or higher is not installed, the following service will also be assigned to this role:  <br/>  Claims to Windows Token Service  <br/> |
|Custom  <br/> | Distributed Cache  <br/>  Microsoft SharePoint Foundation Administration  <br/>  Microsoft SharePoint Foundation Timer  <br/>  Microsoft SharePoint Foundation Web Application  <br/> |
|Single-server farm  <br/> | Access Services  <br/>  Access Services 2010  <br/>  App Management Service  <br/>  Application Discovery and Load Balancer Service  <br/>  Business Data Connectivity Service  <br/>  Claims to Windows Token Service  <br/>  Distributed Cache  <br/>  Lotus Notes Connector  <br/>  Machine Translation Service  <br/>  Managed Metadata Web Service  <br/>  Microsoft SharePoint Foundation Administration  <br/>  Microsoft SharePoint Foundation Incoming E-Mail  <br/>  Microsoft SharePoint Foundation Sandboxed Code Service  <br/>  Microsoft SharePoint Foundation Subscription Settings Service  <br/>  Microsoft SharePoint Foundation Timer  <br/>  Microsoft SharePoint Foundation Web Application  <br/>  Microsoft SharePoint Foundation Workflow Timer Service  <br/>  Microsoft SharePoint Insights  <br/>  PerformancePoint Service  <br/>  PowerPoint Conversion Service  <br/>  Project Server Application Service  <br/>  Request Management  <br/>  Search Administration Web Service  <br/>  Search Host Controller Service  <br/>  Search Query and Site Settings Service  <br/>  Secure Store Service  <br/>  SharePoint Server Search  <br/>  User Profile Service  <br/>  Visio Graphics Service  <br/>  Word Automation Services  <br/> **Note**: The list of **hidden services** are:  <br/>  Information Management Policy Configuration Service  <br/>  Microsoft Project Server Calculation Service  <br/>  Microsoft Project Server Events Service  <br/>  Microsoft Project Server Queuing Service  <br/>  Microsoft SharePoint Foundation Tracing  <br/>  Microsoft SharePoint Foundation Usage  <br/>  Portal Service  <br/>  Security Token Service  <br/>  SSP Job Control Service  <br/> |
|Front-end with Distributed Cache  <br/> | Access Services  <br/>  Access Services 2010  <br/>  App Management Service  <br/>  Business Data Connectivity Service  <br/>  Claims to Windows Token Service  <br/>  Distributed Cache  <br/>  Machine Translation Service  <br/>  Managed Metadata Web Service  <br/>  Microsoft SharePoint Foundation Administration  <br/>  Microsoft SharePoint Foundation Sandboxed Code Service  <br/>  Microsoft SharePoint Foundation Subscription Settings Service  <br/>  Microsoft SharePoint Foundation Timer  <br/>  Microsoft SharePoint Foundation Web Application  <br/>  Microsoft SharePoint Insights  <br/>  PerformancePoint Service  <br/>  Project Server Application Service  <br/>  Request Management  <br/>  Secure Store Service  <br/>  User Profile Service  <br/>  Visio Graphics Service  <br/> **Note**: The list of **hidden services** are:  <br/>  Information Management Policy Configuration Service  <br/>  Microsoft Project Server Calculation Service  <br/>  Microsoft Project Server Events Service  <br/>  Microsoft Project Server Queuing Service  <br/>  Microsoft SharePoint Foundation Tracing  <br/>  Microsoft SharePoint Foundation Usage  <br/>  Portal Service  <br/>  Security Token Service  <br/>  SSP Job Control Service  <br/> |
|Application with Search  <br/> | App Management Service  <br/>  Application Discovery and Load Balancer Service  <br/>  Business Data Connectivity Service  <br/>  Claims to Windows Token Service  <br/>  Machine Translation Service  <br/>  Managed Metadata Web Service  <br/>  Microsoft SharePoint Foundation Administration  <br/>  Microsoft SharePoint Foundation Incoming E-Mail  <br/>  Microsoft SharePoint Foundation Subscription Settings Service  <br/>  Microsoft SharePoint Foundation Timer  <br/>  Microsoft SharePoint Foundation Web Application  <br/>  Microsoft SharePoint Foundation Workflow Timer Service  <br/>  Microsoft SharePoint Insights  <br/>  PowerPoint Conversion Service  <br/>  Project Server Application Service  <br/>  Request Management  <br/>  Search Administration Web Service  <br/>  ﻿Search Host Controller Service  <br/>  ﻿Search Query and Site Settings Service  <br/>  Secure Store Service  <br/>  SharePoint Server Search  <br/>  User Profile Service  <br/>  Word Automation Services  <br/> **Note**: The list of **hidden services** are:  <br/>  Information Management Policy Configuration Service  <br/>  Microsoft Project Server Calculation Service  <br/>  Microsoft Project Server Events Service  <br/>  Microsoft Project Server Queuing Service  <br/>  Microsoft SharePoint Foundation Tracing  <br/>  Microsoft SharePoint Foundation Usage  <br/>  Portal Service  <br/>  Security Token Service  <br/>  SSP Job Control Service  <br/> |
   
## See also

#### Concepts

[Overview of MinRole Server Roles in SharePoint Servers 2016 and 2019](../install/overview-of-minrole-server-roles-in-sharepoint-server.md)
#### Other Resources

[Planning for a MinRole server deployment in SharePoint Servers 2016 and 2019](../install/planning-for-a-minrole-server-deployment-in-sharepoint-server.md)
  
[Managing a MinRole Server Farm in SharePoint Servers 2016 and 2019](managing-a-minrole-server-farm-in-sharepoint-server-2016.md)

