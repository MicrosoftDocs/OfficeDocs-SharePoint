---
title: "Plan for server-to-server authentication in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 3/2/2018
audience: ITPro
ms.topic: concetpual
ms.prod: sharepoint-server-itpro
localization_priority: Priority
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
- Strat_SP_server
ms.custom: 
ms.assetid: 2ce4b90f-5eb0-4d5d-8ddb-3cf00952de4e
description: "Learn how to plan for server-to-server authentication in SharePoint Server."
---

# Plan for server-to-server authentication in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
Server-to-server authentication enables servers that are capable of server-to-server authentication to access and request resources from one another on behalf of users. Servers that are capable of server-to-server authentication run SharePoint Server, Exchange Server 2016, Skype for Business Server 2015, Azure Workflow Service, or other software that supports the Microsoft server-to-server protocol. Server-to-server authentication enables a new set of functionality and scenarios that can be achieved through cross-server resource sharing and access.
  
To provide the requested resources from another server that can perform server-to-server authentication, the server that runs SharePoint Server must do the following:
  
- Verify that the requesting server is trusted. To authenticate the requesting server, you must configure the server that runs SharePoint Server to trust the server that is sending it requests. This is a one-way trust relationship.
    
- Verify that the type of access that the server is requesting is authorized. To authorize the access, you must configure the server that runs SharePoint Server for the appropriate set of permissions for the requested resources.
    
Note that the server-to-server authentication protocol in SharePoint Server is separate from user authentication and is not used as a sign-in authentication protocol by SharePoint users. The server-to-server authentication protocol, which uses the [Open Authorization (OAuth) 2.0 protocol](https://go.microsoft.com/fwlink/p/?LinkID=214783), does not add to the set of user sign-on protocols, such as WS-Federation. There are no new user authentication protocols in SharePoint Server. The server-to-server authentication protocol does not appear in the list of identity providers. 
  
    
For information about how to plan for the User Profile application service for server-to-server authentication, see [Server-to-server authentication and user profiles in SharePoint Server](server-to-server-authentication-and-user-profiles.md).
  
## Introduction
<a name="intro"> </a>

Planning for server-to-server authentication consists of the following tasks:
  
- Identify the set of trust relationships that you have to configure on a server that runs SharePoint Server.
    
- Address User Profile application service considerations. For more information, see [Server-to-server authentication and user profiles in SharePoint Server](server-to-server-authentication-and-user-profiles.md).
    
> [!IMPORTANT]
> The web applications that include server-to-server authentication endpoints (for incoming server-to-server requests) or that make outgoing server-to-server requests to other servers must be configured to use Secure Sockets Layer (SSL). 
  
> [!NOTE]
> You only have to plan for server-to-server authentication on a server that runs SharePoint Server if you are configuring one or more server-to-server scenarios that require its use. 
  
## Identify the set of trust relationships
<a name="trust"> </a>

From the perspective of a server that runs SharePoint Server, a trust relationship with another server that can perform server-to-server authentication consists of the following:
  
- The server that runs SharePoint Server trusts requests from a server that can perform server-to-server authentication (incoming to the server that runs SharePoint Server).
    
    This requires configuration on the server that runs SharePoint Server so that it trusts the requesting server.
    
- The server that can perform server-to-server authentication trusts requests from a server that runs SharePoint Server (outgoing from the server that runs SharePoint Server).
    
    This requires configuration on the server that can perform server-to-server authentication so that it trusts the requesting server that runs SharePoint Server.
    
For each farm that runs SharePoint Server, make a list of servers that are capable server-to-server authentication and that will be receiving incoming requests based on the server-to-server scenarios that involve the farm. There are two cases of server-to-server authentication relationships to examine.
  
 **Case 1: Farms are on-premises**
  
If the farm that can perform server-to-server authentication is on-premises, you must configure the farm that runs SharePoint Server. Use the [New-SPTrustedSecurityTokenIssuer](/powershell/module/sharepoint-server/New-SPTrustedSecurityTokenIssuer?view=sharepoint-ps) PowerShell cmdlet to add a JavaScript Object Notation (JSON) metadata endpoint of the server that can perform server-to-server authentication to the server that runs SharePoint Server. If the server that can perform server-to-server authentication is another server that runs SharePoint Server, the JSON metadata endpoint is in the format: https://<HostName>/_layouts/15/metadata/json/1. 
  
 **Case 2: Farms are part of an Office 365 tenancy**
  
If the farm that runs SharePoint Server and the other server that can perform server-to-server authentication are both part of an Office 365 tenancy, no additional configuration for server-to-server authentication is needed.
  
After you determine the set of servers that require server-to-server authentication, see [Configure server-to-server authentication in SharePoint Server](/sharepoint/security-for-sharepoint-server/security-for-sharepoint-server) to configure the server-to-server trust relationships. 
  
## See also
<a name="trust"> </a>

#### Concepts

[Authentication overview for SharePoint Server](authentication-overview.md)
  
[Server-to-server authentication and user profiles in SharePoint Server](server-to-server-authentication-and-user-profiles.md)

