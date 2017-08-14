---
title: Description of MinRole and associated services in SharePoint Server 2016
ms.prod: SHAREPOINT
ms.assetid: 00c33e26-dacb-47d4-97b8-84659095b108
---


# Description of MinRole and associated services in SharePoint Server 2016
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2016-11-29* **Summary:** Learn about the MinRole feature in SharePoint Server 2016 and the services that are associated with each server role.The MinRole feature in SharePoint Server 2016 lets SharePoint farm administrators assign each server's role in a farm topology. The role of a server is specified when you create a new farm or join a server to an existing farm.This article describes the services associated with each server role. These services are listed in Central Administration -> System settings -> Manage services in this farm, or by running the Get-SPService cmdlet. The service instances for some services are hidden because they are internal to the operation of SharePoint and not meant to be directly controlled. To retrieve a list of services instances on a server, including hidden services, use this syntax, (Get-SPServer <server_name>).ServiceInstances.
> [!NOTE:]

  
    
    

For additional information about the MinRole feature in SharePoint Server 2016, see  [Overview of MinRole Server Roles in SharePoint Server 2016](html/overview-of-minrole-server-roles-in-sharepoint-server-2016.md).
## MinRole and associated services for each server role

The following table shows the services for each server role.
### 

Server role Services Front-end  <br/>  Access Services <br/>  Access Services 2010 <br/>  App Management Service <br/>  Business Data Connectivity Service <br/>  Claims to Windows Token Service <br/>  Machine Translation Service <br/>  Managed Metadata Web Service <br/>  Microsoft SharePoint Foundation Administration <br/>  Microsoft SharePoint Foundation Sandboxed Code Service <br/>  Microsoft SharePoint Foundation Subscription Settings Service <br/>  Microsoft SharePoint Foundation Timer <br/>  Microsoft SharePoint Foundation Web Application <br/>  Microsoft SharePoint Insights <br/>  PerformancePoint Service <br/>  Project Server Application Service <br/>  Request Management <br/>  Secure Store Service <br/>  User Profile Service <br/>  Visio Graphics Service <br/> 
> [!NOTE:]
>  Information Management Policy Configuration Service>  Microsoft Project Server Calculation Service>  Microsoft Project Server Events Service>  Microsoft Project Server Queuing Service>  Microsoft SharePoint Foundation Tracing>  Microsoft SharePoint Foundation Usage>  Portal Service>  Security Token Service>  SSP Job Control Service
  
    
    

Application  <br/>  App Management Service <br/>  Application Discovery and Load Balancer Service <br/>  Business Data Connectivity Service <br/>  Claims to Windows Token Service <br/>  Machine Translation Service <br/>  Managed Metadata Web Service <br/>  Microsoft SharePoint Foundation Administration <br/>  Microsoft SharePoint Foundation Incoming E-Mail <br/>  Microsoft SharePoint Foundation Subscription Settings Service <br/>  Microsoft SharePoint Foundation Timer <br/>  Microsoft SharePoint Foundation Web Application <br/>  Microsoft SharePoint Foundation Workflow Timer Service <br/>  Microsoft SharePoint Insights <br/>  PowerPoint Conversion Service <br/>  Project Server Application Service <br/>  Request Management <br/>  Secure Store Service <br/>  User Profile Service <br/>  Word Automation Services <br/> 
> [!NOTE:]
>  Information Management Policy Configuration Service>  Microsoft Project Server Calculation Service>  Microsoft Project Server Events Service>  Microsoft Project Server Queuing Service>  Microsoft SharePoint Foundation Tracing>  Microsoft SharePoint Foundation Usage>  Portal Service>  Security Token Service>  SSP Job Control Service
  
    
    

Distributed cache  <br/>  Distributed Cache <br/>  Microsoft SharePoint Foundation Administration <br/>  Microsoft SharePoint Foundation Timer <br/>  Microsoft SharePoint Insights <br/> 
> [!NOTE:]
>  Microsoft SharePoint Foundation Tracing>  Microsoft SharePoint Foundation Usage>  Portal Service>  Security Token Service>  SSP Job Control Service
  
    
    


> [!NOTE:]
>  Claims to Windows Token Service>  Microsoft SharePoint Foundation Web Application>  Request Management
  
    
    

Search  <br/>  Application Discovery and Load Balancer Service <br/>  Microsoft SharePoint Foundation Timer <br/>  Microsoft SharePoint Insights <br/>  Search Administration Web Service <br/>  Search Host Controller Service <br/>  Search Query and Site Settings Service <br/>  SharePoint Server Search <br/> 
> [!NOTE:]
>  Microsoft SharePoint Foundation Tracing>  Microsoft SharePoint Foundation Usage>  Portal Service>  Security Token Service>  SSP Job Control Service
  
    
    


> [!NOTE:]
>  Claims to Windows Token Service
  
    
    

Custom  <br/>  Distributed Cache <br/>  Microsoft SharePoint Foundation Administration <br/>  Microsoft SharePoint Foundation Timer <br/>  Microsoft SharePoint Foundation Web Application <br/> Single-server farm  <br/>  Access Services <br/>  Access Services 2010 <br/>  App Management Service <br/>  Application Discovery and Load Balancer Service <br/>  Business Data Connectivity Service <br/>  Claims to Windows Token Service <br/>  Distributed Cache <br/>  Lotus Notes Connector <br/>  Machine Translation Service <br/>  Managed Metadata Web Service <br/>  Microsoft SharePoint Foundation Administration <br/>  Microsoft SharePoint Foundation Incoming E-Mail <br/>  Microsoft SharePoint Foundation Sandboxed Code Service <br/>  Microsoft SharePoint Foundation Subscription Settings Service <br/>  Microsoft SharePoint Foundation Timer <br/>  Microsoft SharePoint Foundation Web Application <br/>  Microsoft SharePoint Foundation Workflow Timer Service <br/>  Microsoft SharePoint Insights <br/>  PerformancePoint Service <br/>  PowerPoint Conversion Service <br/>  Project Server Application Service <br/>  Request Management <br/>  Search Administration Web Service <br/>  Search Host Controller Service <br/>  Search Query and Site Settings Service <br/>  Secure Store Service <br/>  SharePoint Server Search <br/>  User Profile Service <br/>  Visio Graphics Service <br/>  Word Automation Services <br/> 
> [!NOTE:]
>  Information Management Policy Configuration Service>  Microsoft Project Server Calculation Service>  Microsoft Project Server Events Service>  Microsoft Project Server Queuing Service>  Microsoft SharePoint Foundation Tracing>  Microsoft SharePoint Foundation Usage>  Portal Service>  Security Token Service>  SSP Job Control Service
  
    
    

Front-end with Distributed Cache  <br/>  Access Services <br/>  Access Services 2010 <br/>  App Management Service <br/>  Business Data Connectivity Service <br/>  Claims to Windows Token Service <br/>  Distributed Cache <br/>  Machine Translation Service <br/>  Managed Metadata Web Service <br/>  Microsoft SharePoint Foundation Administration <br/>  Microsoft SharePoint Foundation Sandboxed Code Service <br/>  Microsoft SharePoint Foundation Subscription Settings Service <br/>  Microsoft SharePoint Foundation Timer <br/>  Microsoft SharePoint Foundation Web Application <br/>  Microsoft SharePoint Insights <br/>  PerformancePoint Service <br/>  Project Server Application Service <br/>  Request Management <br/>  Secure Store Service <br/>  User Profile Service <br/>  Visio Graphics Service <br/> 
> [!NOTE:]
>  Information Management Policy Configuration Service>  Microsoft Project Server Calculation Service>  Microsoft Project Server Events Service>  Microsoft Project Server Queuing Service>  Microsoft SharePoint Foundation Tracing>  Microsoft SharePoint Foundation Usage>  Portal Service>  Security Token Service>  SSP Job Control Service
  
    
    

Application with Search  <br/>  App Management Service <br/>  Application Discovery and Load Balancer Service <br/>  Business Data Connectivity Service <br/>  Claims to Windows Token Service <br/>  Machine Translation Service <br/>  Managed Metadata Web Service <br/>  Microsoft SharePoint Foundation Administration <br/>  Microsoft SharePoint Foundation Incoming E-Mail <br/>  Microsoft SharePoint Foundation Subscription Settings Service <br/>  Microsoft SharePoint Foundation Timer <br/>  Microsoft SharePoint Foundation Web Application <br/>  Microsoft SharePoint Foundation Workflow Timer Service <br/>  Microsoft SharePoint Insights <br/>  PowerPoint Conversion Service <br/>  Project Server Application Service <br/>  Request Management <br/>  Search Administration Web Service <br/>  ﻿Search Host Controller Service <br/>  ﻿Search Query and Site Settings Service <br/>  Secure Store Service <br/>  SharePoint Server Search <br/>  User Profile Service <br/>  Word Automation Services <br/> 
> [!NOTE:]
>  Information Management Policy Configuration Service>  Microsoft Project Server Calculation Service>  Microsoft Project Server Events Service>  Microsoft Project Server Queuing Service>  Microsoft SharePoint Foundation Tracing>  Microsoft SharePoint Foundation Usage>  Portal Service>  Security Token Service>  SSP Job Control Service
  
    
    


# See also

#### 

 [Overview of MinRole Server Roles in SharePoint Server 2016](html/overview-of-minrole-server-roles-in-sharepoint-server-2016.md)
  
    
    

#### 

 [Planning for a MinRole server deployment in SharePoint Server 2016](html/planning-for-a-minrole-server-deployment-in-sharepoint-server-2016.md)
  
    
    
 [Managing a MinRole Server Farm in SharePoint Server 2016](html/managing-a-minrole-server-farm-in-sharepoint-server-2016.md)
  
    
    

  
    
    

