---
title: "Plan service deployment in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 8/18/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 4e6a620f-224d-4c72-a4fd-b69ed4db8bc9
description: "Learn about the services on the Services on Server page in the SharePoint Central Administration website and deployment guidance for these services. Many of these services are associated with service applications."
---

# Plan service deployment in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
    
## About Services on Server
<a name="Section3"> </a>

The **Services on Server** page in Central Administration lists services that are started or stopped on specific servers in the farm. Some of these services are associated with service applications. After deploying service applications to the farm, go to the Services on Server page and make sure that the associated services are started on the appropriate servers. Some of these services are not associated with service applications. 
  
> [!NOTE]
> Note: Search components are deployed by using PowerShell instead of the **Services on Server** page. 
  
After planning the farm topology, use this article to make sure that the appropriate services on server are started for each server in the farm. This may not be necessary for small farms in which all of the service applications and services are run on one server or two redundant servers. 
  
This article lists recommended configuration of services and service applications for two different architecture approaches:
  
- **Streamlined topologies** — The distribution of services and other components in a farm is intended to maximize system resources of server hardware. Streamlined architectures include Front-end servers, Application servers, Search servers, Distributedand database servers. 
    
- **Traditional topologies** — Topologies are based on traditional approaches to building architectures with Web servers, application servers, and database servers. 
    
For more information about these SharePoint 2013 topology approaches, see the following models:
  
- [Streamlined Topologies for SharePoint Server 2013](https://go.microsoft.com/fwlink/p/?LinkId=286786)
    
- [Traditional Topologies for SharePoint Server 2013](https://go.microsoft.com/fwlink/p/?LinkId=257303)
    
For information about SharePoint Server 2016 topology, see the following model:
  
- [Planning for a MinRole server deployment in SharePoint Server](/sharepoint/install/planning-for-a-minrole-server-deployment-in-sharepoint-server)
    
## Services on server for streamlined topologies in SharePoint 2013
<a name="Section1"> </a>

> [!NOTE]
> The following table only apply to SharePoint 2013. 
  
**Table: Service applications and Services on Server for streamlined topologies**

|**Service application**|**Services on server**|**MinRole server role**|**Additional information**|
|:-----|:-----|:-----|:-----|
|Access Services  <br/> |Access Services  <br/> |Front-end or Application server  <br/> |Enables users of the Access 2013 client to create new Access service applications. View, edit, and interact with Access Services databases in a browser.  <br/> |
|Access Services 2010  <br/> |Access Services 2010  <br/> |Front-end server  <br/> |Allows continued maintenance of SharePoint 2010 Access service applications by using Access 2010 clients and Access 2013 clients. Does not allow users to create new applications.  <br/> |
|App Management Service  <br/> |App Management Service  <br/> |Front-end or Application server  <br/> ||
|Business Data Connectivity  <br/> |Business Data Connectivity service  <br/> |Front-end or Application server  <br/> ||
|Excel Services  <br/> |Excel Calculation Services  <br/> |Front-end server or specialized server  <br/> ||
|Machine Translation Service  <br/> |Machine Translation Service  <br/> |Front-end or Application server  <br/> |The Machine Translation Service uses SharePoint OAuth for file management. The Machine Translation Service Application's app pool account needs permissions to the User Profile Application to function correctly. The Machine Translation Service connects to the Microsoft Translator online service. Microsoft Translator may collect some data to improve the quality of translations.  <br/> |
|Managed Metadata Service  <br/> |Managed Metadata Web Service  <br/> |Front-end or Application server  <br/> ||
|Microsoft SharePoint Foundation Subscription Settings Service  <br/> |Microsoft SharePoint Foundation Subscription Settings Service  <br/> |Front-end server  <br/> |You must use Microsoft PowerShell to deploy this service. Start this service if you have deployed service applications in multi-tenant mode or if the farm includes sites that use site subscriptions. This service stores settings and configuration data for tenants in a multi-tenant environment. After you start this service, web applications consume the service automatically.  <br/> |
|PerformancePoint  <br/> |PerformancePoint Service  <br/> |Front-end server  <br/> ||
|PowerPoint Conversion  <br/> |PowerPoint Conversion Service  <br/> |Application server  <br/> |This service converts PowerPoint presentations to other formats. It typically runs on one or more application servers. It starts one or more worker processes to perform conversions. When actively converting, a worker process may use up a complete processor core. Memory usage depends on the size and content of files being converted. You can use Microsoft PowerShell cmdlets to control the number of worker processes that are used. Several other configuration options are also available through Microsoft PowerShell cmdlets.  <br/> |
|Search  <br/> |Lotus Notes Connector  <br/> |Search server  <br/> |Refer to documentation to learn how to configure Lotus Notes Connector which crawls data on a Lotus Domino server.  <br/> |
|Search  <br/> |Search Host Controller Service  <br/> |Search servers  <br/> |This service manages the search topology components. The service is automatically started on all servers that run search topology components.  <br/> |
|Search  <br/> |Search Query and Site Settings Service  <br/> |Search servers  <br/> |This service load balances queries within the search topology. It also detects farm-level changes to the search service and puts these in the Search Admin database. The service is automatically started on all servers that run the query processing component.  <br/> |
|Search  <br/> |SharePoint Server Search  <br/> |Search servers  <br/> |This service crawls content for the search index. This service is automatically started on all servers that run search topology components. The service cannot be stopped or started from the Services on Server page.  <br/> |
|Secure Store Service  <br/> |Secure Store Service  <br/> |Front-end or Application server  <br/> ||
|Usage and Health Data Collection  <br/> |||This service application has no associated service on server.  <br/> |
|User Profile  <br/> |User Profile Service  <br/> |Front-end or Application server  <br/> ||
|User Profile  <br/> |User Profile Synchronization Service  <br/> |Front-end server  <br/> ||
|Visio Graphics Service  <br/> |Visio Graphics Service  <br/> |Front-end server  <br/> ||
|Word Automation Service  <br/> |Word Automation Services  <br/> |Application server  <br/> |Performs automated bulk document conversions. When actively converting, this service will fully use one CPU for each worker process (configured in Central Administration). If the service is started on multiple servers, a job will be shared across all the servers.  <br/> |
|Work Management  <br/> |Work Management Service  <br/> |Batch-processing server  <br/> ||
||Central Administration  <br/> |Front-end or Application server  <br/> |This service runs the Central Administration site. It can be put on a batch-processing server if security policies of an organization mandate this.  <br/> |
||Claims to Windows Token Service  <br/> |Application server  <br/> ||
||Distributed Cache  <br/> |Distributed Cache OR Custom servers  <br/> |By default this service is started on all web servers and application servers in a farm.  <br/> |
||Document Conversions Launcher Service  <br/> |Batch-processing servers  <br/> |Schedules and starts the document conversions on a server.  <br/> |
||Document Conversions Load Balancer Service  <br/> |Batch-processing servers  <br/> |Balances document conversion requests from across the server farm. Each web application can have only one load balancer registered with it at a time.  <br/> |
||Microsoft SharePoint Foundation Incoming E-Mail  <br/> |Application servers  <br/> |Typically, this service runs on a web server. If you have to isolate this service, you can start it on an application server.  <br/> |
||Microsoft SharePoint Foundation Sandboxed Code Service  <br/> |Front-end servers  <br/> |Start this service on computers that run sandboxed code in the farm. This can include front-end servers and batch-processing servers. This service runs code that is deployed as part of a sandboxed solution in a remote, rights-restricted process and measures the server resources that are used during execution against a site collection-scoped, daily quota.  <br/> |
||Microsoft SharePoint Foundation Web Application  <br/> |Front-end servers, batch-processing servers, plus the Distributed Cache and Request Management servers if these servers are implemented  <br/> |This service provides web server functionality. It is started by default on web servers. Custom features scoped to web applications may not display in Central Administration as intended if this service is not started on the server running Central Administration and if the feature cannot be deployed globally.  <br/> |
||Microsoft SharePoint Foundation Workflow Timer Service  <br/> |Application server  <br/> |This service is automatically configured to run on all web servers in a farm.  <br/> |
||Request Management  <br/> |Distributed Cache and Request Management tier  <br/> |In integrated mode, Request Management runs on all web servers in a farm. In dedicated mode servers in a separate Request Management farm are between the hardware load balancer and one or more SharePoint farms.  <br/> |
   
## Services on Server for traditional topologies in SharePoint 2013
<a name="Section2"> </a>

> [!NOTE]
> The following table only apply to SharePoint 2013. 
  
**Table: Service applications and Services on Server for traditional topologies**

|**Service Application**|**Services on Server**|**Server Recommendation**|**More information**|
|:-----|:-----|:-----|:-----|
|Access Services 2010  <br/> |Access Services 2010  <br/> |Front-end Server  <br/> |Allows continued maintenance of SharePoint 2010 Access service applications by using Access 2010 clients and Access 2013 clients. Does not allow users to create new applications.  <br/> |
|Access Services  <br/> |Access Services  <br/> |Front-end Server  <br/> |Allows creation of new Access service applications by using the Access 2013 client. View, edit, and interact with Access Services databases in a browser.  <br/> |
|App Management Service  <br/> |App Management Service  <br/> |Front-end or Application Server  <br/> ||
|||||
|Business Data Connectivity  <br/> |Business Data Connectivity service  <br/> |Front-end or Application Server  <br/> ||
|Excel Calculation Services  <br/> |Excel Calculation Services  <br/> |Application Server  <br/> ||
|Machine Translation Service  <br/> |Machine Translation Service  <br/> |Front-end or Application Server  <br/> |The Machine Translation Service uses SharePoint OAuth for file management. The Machine Translation Service Application's app pool account needs permissions to the User Profile Application to function correctly. The Machine Translation Service connects to the Microsoft Translator online service. Microsoft Translator may collect some data to improve the quality of translations.  <br/> |
|Managed Metadata Service  <br/> |Managed Metadata Web Service  <br/> |Application Server  <br/> ||
|Microsoft SharePoint Foundation Subscription Settings Service  <br/> |Microsoft SharePoint Foundation Subscription Settings Service  <br/> |Front-end server  <br/> |This service application is deployed only by using PowerShell. In hosting environments, this service is typically started on one or more application servers. Start this service if you have deployed service applications in multi-tenant mode or if the farm includes sites that use site subscriptions. This service stores settings and configuration data for tenants in a multi-tenant environment. After it is started, web applications consume this service automatically.  <br/> |
|PerformancePoint  <br/> |PerformancePoint Service  <br/> |Front-end server  <br/> ||
|PowerPoint Conversion  <br/> |PowerPoint Conversion Service  <br/> |Application Server  <br/> |This service converts PowerPoint presentations to other formats. It typically runs on one or more application servers. It starts one or more worker processes to perform conversions. When actively converting, a worker process may use up a whole processor core. Memory usage depends on the size and content of files being converted. The number of worker processes that are used can be controlled through PowerShell cmdlets. Several other configuration options are also available through PowerShell cmdlets.  <br/> |
|Search  <br/> |Lotus Notes Connector  <br/> |Search Server  <br/> |Refer to documentation to learn how to configure Lotus Notes Connector which crawls data on a Lotus Domino server.  <br/> |
|Search  <br/> |Search Host Controller Service  <br/> |Search servers  <br/> |This service manages the search topology components. The service is automatically started on all servers that run search topology components.  <br/> |
|Search  <br/> |Search Query and Site Settings Service  <br/> |Search servers  <br/> |This service load balances queries within the search topology. It also detects farm-level changes to the search service and puts these in the Search Admin database. The service is automatically started on all servers that run the query processing component.  <br/> |
|Search  <br/> |SharePoint Server Search  <br/> |Search servers  <br/> |This service crawls content for the search index. This service is automatically started on all servers that run search topology components. The service cannot be stopped or started from the Services on Server page.  <br/> |
|Secure Store Service  <br/> |Secure Store Service  <br/> |Search or Application server  <br/> ||
|Usage and Health Data Collection  <br/> |NA  <br/> |NA  <br/> |This service application has no associated service on server.  <br/> |
|User Profile  <br/> |User Profile Service  <br/> |Front-end or Application server  <br/> ||
|User Profile  <br/> |User Profile Synchronization Service  <br/> |Front-end or Application Server  <br/> ||
|Visio Graphics Service  <br/> |Visio Graphics Service  <br/> |Front-end or server  <br/> ||
|Word Automation Service  <br/> |Word Automation Services  <br/> |Application server  <br/> |Performs automated bulk document conversions. When actively converting, this service will fully use one CPU for each worker process (configured in Central Administration). If the service is started on multiple servers, a job will be shared across all the servers.  <br/> |
|Work Management  <br/> |Work Management Service  <br/> |Application Server  <br/> ||
||Central Administration  <br/> |Front-end or Application Server  <br/> |This service runs the SharePoint Central Administration website.  <br/> |
||Claims to Windows Token Service  <br/> |Web and application servers  <br/> |This service is automatically configured to run on applicable servers.  <br/> |
||Distributed Cache  <br/> |Web and application servers  <br/> |By default this service is started on all web servers and application servers in a farm.  <br/> |
||Document Conversions Launcher Service  <br/> |Application Server  <br/> |Schedules and starts the document conversions on a server.  <br/> |
||Document Conversions Load Balancer Service  <br/> |Application Server  <br/> |Balances document conversion requests from across the server farm. Each web application can have only one load balancer registered with it at a time.  <br/> |
||Microsoft SharePoint Foundation Incoming E-Mail  <br/> |Web server or application server  <br/> |Typically, this service runs on a web server. If you need to isolate this service, you can start it on an application server.  <br/> |
||Microsoft SharePoint Foundation Sandboxed Code Service  <br/> |Web server or application server  <br/> |Start this service on computers in the farm that run sandboxed code. This can include web servers and application servers. This service runs code that is deployed as part of a sandboxed solution in a remote, rights-restricted process and measures the server resources that are used during execution against a site collection-scoped, daily quota.  <br/> |
||Microsoft SharePoint Foundation Web Application  <br/> |Web server  <br/> |Ensure that this service is started on all web servers in a farm. Stop this service on application servers. This service provides web server functionality. It is started by default on web servers. Custom features scoped to web applications may not display in Central Administration as intended if this service is not started on the server that runs Central Administration and if the feature cannot be deployed globally.  <br/> |
||Microsoft SharePoint Foundation Workflow Timer Service  <br/> |Web server  <br/> |This service is automatically configured to run on all web servers in a farm.  <br/> |
||Request Management  <br/> |Web server or dedicated servers  <br/> |In integrated mode, Request Management runs on all web servers in a farm. In dedicated mode servers in a separate Request Management farm are between the hardware load balancer and one or more SharePoint farms.  <br/> |
   
For a list of **Services on Server** in SharePoint Server 2016, see [Description of MinRole and associated services in SharePoint Server 2016](/SharePoint/administration/description-of-minrole-and-associated-services-in-sharepoint-server-2016).
  
## See also
<a name="Section2"> </a>

#### Other Resources

[Plan for SharePoint Server](/SharePoint/getting-started)

