---
title: "Configure Request Manager in SharePoint Server"
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 6/24/2019
ms.audience: ITPro
ms.topic: concetpual
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 
description: "Learn how Request Manager in SharePoint Server can route and throttle incoming requests to help improve performance and availability. "
---

# Configure Request Manager in SharePoint Server
[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]  


## Overview ##

Request Manager is functionality in SharePoint Server  that enables administrators to manage incoming requests and determine how SharePoint Server  routes these requests. 

Request Manager uses configured rules to perform the following tasks when it encounters requests:

- Deny potentially harmful requests from entering a SharePoint farm.
- Route good requests to an available server.
- Manually optimize performance.

Information that administrators or an automated process provide to Request Manager determine the effectiveness of routed requests.

The following table describes possible scenarios and resolutions that Request Manager can address.

|**Area**|**Scenario**|**Resolution**|
|:-----|:-----|:-----|:-----|:-----|
|**Reliability and performance** <br/> |Routing new requests to web front end with low performance can increase latency and cause timeouts.  <br/> |Request Manager can route to front-end web servers that have better performance, keeping low performance front-end web servers available.  <br/> |
|Requests from users and bots have equal priority.<br/> |Prioritize requests by throttling requests from bots to instead serve requests from end-users).<br/> | 
|**Manageability, accountability, and capacity planning** <br/> |SharePoint Server fails or generally responds slowly, but it’s difficult to identify the cause of a failure or slowdown.  <br/> |Request Manager can send all requests of a specific type, for example, Search, User Profiles, or Office Online, to specific computers. When a computer is failing or slow, Request Manager can locate the problem. <br/> |
|All front-end web servers must be able to handle the requests because they could be sent to any front-end web server. <br/> |Request Manager can send multiple or single requests to front-end web servers that are designated to handle them.  <br/> |
|**Scaling limits** <br/> |Hardware scaling limited by load balancer <br/> |Request Manager can perform application routing and scale out as needed so that a load balancer can quickly balance loads at the network level. <br/> |

## Setup and Deployment ##

Request Manager's task is to decide two things: a SharePoint farm will accept a request, and if the answer is "yes", to which front-end web server SharePoint Server will send it. The three major functional components of Request Manager are Request Routing, Request Throttling and Prioritizing, and Request Load Balancing. These components determine how to handle requests. Request Manager manages all requests on a per-web-application basis. Because Request Manager is part of the SharePoint Server  Internet Information Services (IIS) module, it only affects requests that IIS hosts.

When a new request is received, Request Manager is the first code that runs in a SharePoint farm. Although Request Manager is installed during setup of SharePoint Server on a front-end web server, the Request Management service is not enabled. You can use the [Start-SPServiceInstance](https://docs.microsoft.com/en-us/powershell/module/sharepoint-server/start-spserviceinstance?view=sharepoint-ps) and [Stop-SPServiceInstance](https://docs.microsoft.com/en-us/powershell/module/sharepoint-server/stop-spserviceinstance?view=sharepoint-ps) cmdlets to start and stop the Request Management service instance respectively or the Manage services on server page on the the SharePoint Central Administration website. You can use the **RoutingEnabled** or **ThrottlingEnabled** parameters of the [Set-SPRequestManagementSettings](https://docs.microsoft.com/en-us/powershell/module/sharepoint-server/set-sprequestmanagementsettings?view=sharepoint-ps) Microsoft PowerShell cmdlet to change properties of Request Manager.

**NOTE**: There is no user interface to configure properties of Request Manager. The Windows PowerShell cmdlet is the only way to perform this task.

Request Manager has two supported deployment modes: Dedicated and Integrated. 

### Dedicated mode ###

A set of front-end web servers is dedicated to managing requests exclusively. The front-end web servers that are dedicated to Request Manager are in their own farm that is located between the hardware load balancers (HLBs) and the SharePoint farm. The HLBs send all requests to the Request Manager front-end web servers. Request Manager that runs on these front-end web servers decides to which SharePoint front-end web servers it will send the requests and then routes the requests. Depending on the routing and throttling rules, Request Manager might ignore some requests without sending them to another server. The SharePoint front-end web servers do their normal tasks in processing requests and then send responses back through the front-end web servers that run Request Manager and to the clients.

Note that all farms are set up as SharePoint farms. All front-end web servers are SharePoint front-end web servers, each of which can do the same work as any other. The difference between the farms is that the Request Manager front-end web servers have Request Manager enabled.

Dedicated mode is good for larger-scale deployments when physical computers are readily available. The ability to create a separate farm for Request manager provides two benefits: Request Manager and SharePoint processes do not compete for resources and you can scale out one without having to also scale out the other. This allows you to have more control over the performance of each role.
- Request Manager and SharePoint processes do not compete for resources.
- You can scale out each farm separately, which provides more control over the performance of each farm.

### Integrated mode ###

In an integrated mode deployment, all SharePoint front-end web servers run Request Manager. Hardware load balancers send requests to all front-end web servers. When a front-end web server receives a request, Request Manager decides how to handle it: .
- Allow it to be processed locally.
- Route it to a different front-end web server.
- Deny the request.
Integrated mode is good for small-scale deployments when many physical computers are not readily available. This mode lets Request Manager and the rest of SharePoint Server to run on all computers. This mode is common for on-premises deployments.

## Configuration ##

Request Manager has two configurable parts: **General settings** and **Decision information**. General settings are parameters that make Request Manager ready to use, such as enabling or disabling Request Routing and Request Throttling and Prioritizing. Decision information is all of the information that is used during the routing and throttling processes, such as routing and throttling rules.

**NOTE**: You configure Request Manager on a farm and functionality occurs at a web application level in SharePoint Server 2013 and the web application role in SharePoint Servers 2016 and 2019.

### General settings ##

By default, request routing and request throttling and prioritizing are enabled. You use the [Set-SPRequestManagementSettings](https://docs.microsoft.com/en-us/powershell/module/sharepoint-server/set-sprequestmanagementsettings?view=sharepoint-ps) cmdlet to change the properties of request routing, request throttling and prioritizing, and select a routing weight scheme.

The table describes the configuration situation and Windows PowerShell syntax to use.

|**Situation**|**Microsoft PowerShell example**||
|:-----|:-----|:-----|:-----|:-----|
|Enable routing and throttling for all web applications <br/>| ```|Get-SPWebApplication | Set-SPRequestManagementSettings –RoutingEnabled $true –ThrottlingEnabled $true ```<br/> ||
|Enable routing with static weighting for all web applications <br/>| ```Get-SPWebApplication | Get-SPRequestManagementSettings | Set-SPRequestManagementSettings –RoutingEnabled $true –ThrottlingEnabled $false –RoutingWeightScheme Static```<br/> ||

In some situations, multiple front-end web servers will be suitable destinations for a particular request. In this case, by default, SharePoint Server selects one server randomly and uniformly. 
One routing weight scheme is static-weighted routing. In this scheme, static weights are associated with front-end web servers so that Request Manager always favors a higher static weight during the selection process. This scheme is useful to give added weight to more powerful front-end web servers and produce less strain on less powerful ones. Each front-end web server will have a static weight associated with it. The values of the weights are any integer value, where 1 is the default. A value less than 1 represents lower weight, and greater than 1 represents higher weight.

Another weighting scheme is health-weighted. In health-weighted routing, front-end web servers that have health scores closer to zero will be favored, and fewer requests will be sent to front-end web servers that have a higher health score values. The health weights run from 0 to 10, where 0 is the healthiest and therefore will get the most requests. By default, all front-end web servers are set to healthy, and therefore, will have equal weights. SharePoint's health score based monitoring system assigns weight to server and send a health score value as a header in the response to a request. Request Manager uses same health score and stores it in local memory.

### Decision information ###
Decision information applies to routing targets, routing rules, and throttling rules.

### Routing targets ###
Request routing determines the routing targets that are available when a routing pool is selected for a request. The scope of routing targets is currently for front-end web servers only, but Request Manager’s design does not exclude routing to application servers, too. A list of front-end web servers in a farm is automatically maintained by using the configuration database. An administrator who wants to change that list, typically in dedicated mode, has to use the appropriate routing cmdlets to get, add, set, and remove routing targets.

The following table describes the various routing target tasks and the associated Windows PowerShell syntax to use.

|**Task**|**Microsoft PowerShell example**||
|:-----|:-----|:-----|:-----|:-----|
|Return a list of routing targets for all available web applications <br/>| ```Get-SPWebApplication | Get-SPRequestManagementSettings | Get-SPRoutingMachineInfo –Availability Available ```<br/> ||
|Add a new routing target for a specified web application. <br/>| ```$web=Get-SPWebApplication -Identity <URL of web application> ``` <br/> ||
| <br/>| ```$rm=Get-SPRequestManagementSettings -Identity $web ``` <br/> ||
| <br/>| ```Add-SPRoutingMachineInfo –RequestManagementSettings $rm -Name <MachineName> -Availability Available ``` <br/> ||
|Edit an existing routing target’s availability and static weight for a specified web application. <br/>| ```$web=Get-SPWebApplication -Identity <URL of web application> ``` <br/> ||
| <br/>| ```$rm=Get-SPRequestManagementSettings -Identity $web ``` <br/> ||
| <br/>| ```$m=Get-SPRoutingMachineInfo -RequestManagementSettings $rm -Name <MachineName> ``` <br/> ||
| <br/>| ```Set-SPRoutingMachineInfo -Identity $m -Availability Unavailable ``` <br/> ||
|Remove a routing target from a specified web application. <br/>| ```$web=Get-SPWebApplication -Identity <URL of web application> ``` <br/> ||
| <br/>| ```$rm=Get-SPRequestManagementSettings -Identity $web ``` <br/> ||
| <br/>| ```$m=Get-SPRoutingMachineInfo -RequestManagementSettings $rm -Name <MachineName> ``` <br/> ||
| <br/>| ```Remove-SPRoutingMachineInfo -Identity $M ``` <br/> ||

**NOTE**: You cannot remove front-end web servers that are in the farm. Instead, you can use the **Availability** parameter of the **Set-SPRoutingMachineInfo** cmdlet to make them unavailable.

### Routing and throttling rules ##
Request routing and request throttling and prioritizing are decision algorithms that use rules to prescribe many actions. The rules determine how Request Manager handles requests.

Rules are separated into two categories, routing rules and throttling rules, which are used in request routing and request throttling and prioritizing, respectively. Routing rules match criteria and route to a machine pool. Throttling rules match criteria and throttle based on known health score of a computer.

## Request Routing ##
Request processing is all operations that occur sequentially from the time that Request Manager receives a new request to the time that Request Manager sends a response to the client.

Request processing is divided into the components: 
- request routing
- incoming request handler
- request throttling and prioritizing
- request load balancing

### Incoming request handler ###
The role of the incoming request handler is to determine whether Request Manager should process a request. If request throttling and prioritizing is disabled and the Request Manager queue is empty, Request Manager directs the request to SharePoint Server that is running on the current front-end web server. If request throttling and prioritizing is enabled, request throttling and prioritizing determines whether the request should be allowed or denied on the current front-end web server
.
The processes steps of the incoming request handler are as follows:
1.	Request is determined if it should be throttled or routed
2.	For routed requests, load balance algorithm is run
3.	Request routed to load balancer endpoint

Request routing and Request throttling and prioritizing only run if it is enabled and is routed once per farm. Request load balancer only runs if a request has been determined as routable. The outgoing request handler only runs if the request has to be sent to a different front-end web server. The role of the outgoing request handler is to send the request to the selected front-end web server, wait for a response, and send the response back to the source. 

### Request routing ###
The role of request routing is to select a front-end web server to route a request. By using no routing rules that are defined, the routing scheme is as easy as randomly selecting an available front-end web server. 

The algorithm of request routing is defined by two parts: request-rule matching and front-end web server selection.


### Request rule matching ###

Every rule has one or more match criteria, which consist of three things: match property, match type, and match value.

The following table describes the different types of match properties and match types:

|**Match property**|**Match type**||
|:-----|:-----|:-----|:-----|:-----|
|Hostname <br/>| ReqEx| <br/> ||
|URL <br/>| Equals<br/> ||
|Port number <br/>| Starts with<br/> ||
|MIME type <br/>| Ends with<br/> ||

For example, an administrator would use the following match criteria to match http://contoso requests: Match Property=URL; Match value= http://contoso; Match type=RegEx.

### Front-end web server selection ###

The front-end web server selection uses all routing rules, whether they match or do not match a given request. Rules that match have machine pools, a request sends load balanced to any machine in any matching rule’s machine pool. If a request does not match any request, it sends load balanced to any available routing target.

**NOTE**: For SharePoint Servers 2016 and 2019, the front-end role type is used.

### Request routing and prioritizing ###

For routing requests that use the health-based monitoring system, the role of request routing and prioritizing is to reduce the routing pool to computers that have a good health score to process requests. If request routing is enabled, the routing pool is whichever front-end web server is selected. If request routing is disabled, the routing pool only contains the current front-end web server.

Request routing and prioritizing can be divided into two parts: request-rule matching and front-end web server filtering. Request-rule matching happens exactly like in request routing. Front-end web server filtering uses the health threshold parameter from the throttling rules in combination with front-end web server health data to determine whether the front-end web servers in the selected routing pool can process the given request.

The front-end web server filtering process follows these steps:

1.	The routing pool is either the current front-end web server or one or more front-end web servers that request routing selects.
2.	All matching rules are checked to find the smallest health threshold value.
3.	Remove front-end web servers in the routing pool that have health scores greater than or equal to the smallest health threshold value.

For example, request routing is disabled and the current front-end web server has a health score of 7 and a rule “Block OneNote” without a health threshold (that is, health threshold = 0) is created.

The routing pool is the current front-end web server that has a health threshold equal to zero (0). So, the smallest threshold that the front-end web server can serve is zero. Because the current front-end web server has health score of 7, Request Manager denies and removes the request.

### Request load balancing ###

The role of request load balancing is to select a single target to which to send the request. Request load balancing uses the routing weight schemes to select the target. All routing targets begin with a weight of 1. If static weighting is enabled, request load balancing uses the static weights set of each routing target to adjust the weights and the value can be valid integer number. If health weighting is enabled,request load balancing uses health information to add weight to healthier targets and remove weight from less healthy targets.

## Monitoring and maintenance ##

Monitoring and logging are keys to managing requests from Request Manager. 
- The rules that matched.
- The rules that did not match.
- The final decision of the request.

Decisions might include useful information such as the following.
- Was the request denied?
- Which front-end web server was selected and from which routing pool.
- Did the request succeed or fail and why?
- How long did each part, routing, throttling, and waiting for front-end web server to respond, take?


An administrator can use this information to adjust the routing and throttling rule sets to optimize the system and correct problems. To help you monitor and evaluate your farm's performance, you can create a performance monitor log file and add the following SharePoint Foundation Request Manager Performance counters:

|**Counter name**|**Description**||
|:-----|:-----|:-----|:-----|:-----|
|Connections Current <br/>| The total number of connections that are currently open by Request Manager.| <br/> ||
|Connections Reused / Sec <br/>| The number of connections per second that are reused when the same client connection makes another request without closing the connection.<br/> ||
|Routed Requests / Sec <br/>| The number of routed requests per second.  The instance determines the application pool and server for which this counter tracks.<br/> ||
|Throttled Requests / Sec <br/>| The number of throttled requests per second.<br/> ||
Failed Requests / Sec <br/>| Ends with<br/> ||
|MIME type <br/>| The number of failed requests per second.<br/> ||
|Average Processing Time<br/>| Ends with<br/> ||
|MIME type <br/>| The time to process the request that is, the time to evaluate all the rules and determine a routing target.<br/> ||
|Last Ping Latency<br/>| The last ping latency (that is, Request Manager's PING feature) and the instance determine which application pool and machine target.<br/> ||
|Connection Endpoints Current <br/>| The total number of endpoints that are connected for all active connections.<br/> ||
|Routed Requests Current <br/>| The number of unfinished routed requests. The instance determines which application pool and machine target.<br/> ||

Along with creating a performance monitor log file, the verbose logging level can be enabled by using the following Microsoft PowerShell syntax:

```
Set-SPLogLevel “Request Management” –TraceSeverity Verbose
```
