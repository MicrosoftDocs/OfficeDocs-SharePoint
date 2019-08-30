---
title: "Plan for app authentication in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 3/5/2018
audience: ITPro
ms.topic: concetpual
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: a29d4cc4-7944-4c3e-94ea-d681f432f07b

description: "Learn how to plan for app authentication in SharePoint Server."
---

# Plan for app authentication in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]  
  
App authentication is the validation of an external app for SharePoint's identity and the authorization of both the app and an associated user when the app requests access to a secured SharePoint resource. App authentication occurs when an external component of a SharePoint Store app or an App Catalog app, such as a web server that is located on the intranet or the Internet, attempts to access a secured SharePoint resource. For example, an app for SharePoint that includes a component that runs in Microsoft Azure is an external app. App authentication enables a new set of functionality and scenarios that can be achieved by allowing apps to include data from SharePoint resources in the results that the app processes and displays for users.
  
To provide the requested resources from an app for SharePoint, the server that runs SharePoint Server must do the following:
  
- Verify that the requesting app is trusted.
    
    To authenticate the requesting app, you must configure the server that runs SharePoint Server to trust the app that is sending it requests. This is a one-way trust relationship.
    
- Verify that the type of access that the app is requesting is authorized.
    
    To authorize the access, SharePoint Server relies on the set of app permissions, which was specified in the app manifest file when it was installed, and the permissions that are associated with the user on whose behalf the app is acting. SharePoint Server also relies on the permissions that were granted to the SPAppPrincipal when the trust was established by using the [Set-SPAppPrincipalPermission](/powershell/module/sharepoint-server/Set-SPAppPrincipalPermission?view=sharepoint-ps) PowerShell cmdlet. 
    
Note that app authentication in SharePoint Server is separate from user authentication and is not used as a sign-in authentication protocol by SharePoint users. App authentication uses the [Open Authorization (OAuth) 2.0 protocol](https://go.microsoft.com/fwlink/p/?LinkID=214783) and does not add to the set of user authentication or sign-on protocols, such as WS-Federation. There are no new user authentication protocols in SharePoint Server. App authentication and OAuth do not appear in the list of identity providers. 
  
    
## Introduction
<a name="intro"> </a>

Planning for app authentication consists of the following tasks:
  
- Identify the set of trust relationships that you have to configure on a farm that runs SharePoint Server that correspond to the external apps that will be making requests for SharePoint resources.
    
- Provide incoming access from external applications that the Internet hosts.
    
> [!IMPORTANT]
> The web applications that include app authentication endpoints (for incoming requests by apps for SharePoint) must be configured to use Secure Sockets Layer (SSL). You can configure OAuth in SharePoint Server so that it does not require SSL. However, we recommend this only for evaluation, for ease of configuration or to create an app development environment. 
  
> [!NOTE]
> You only have to plan for app authentication on a SharePoint farm if you are using one or more external apps for SharePoint that require its resources. 
  
## Identify the set of trust relationships
<a name="trust"> </a>

You must configure the SharePoint farm to trust the access tokens that correspond to resource requests that the following types of external apps send:
  
- Provider-hosted apps run on their own servers on the Internet or your intranet, are registered with Microsoft Azure, and use ACS to obtain the access token.
    
    For provider-hosted apps, you must configure the SharePoint farm to trust the ACS instance of the provider-hosted app.
    
- High-trust apps run on stand-alone servers on your intranet and use a signing certificate to digitally sign the access tokens that the app generates.
    
    High-trust apps use the server-to-server protocol to request resources on behalf of a user. For high-trust apps, configure the SharePoint farm with the JavaScript Object Notation (JSON) metadata endpoint of the server that hosts the app. Or, you can manually configure the trust. For more information, see [Configure app authentication in SharePoint Server](/sharepoint/administration/install-and-manage-apps-for-sharepoint-server)
    
    For more information about high-trust apps, see [How to: Create high-trust apps for SharePoint 2013 using the server-to-server protocol](https://go.microsoft.com/fwlink/p/?LinkId=267561).
    
## Choose user authentication methods for on-premises apps
<a name="onprem"> </a>

An on-premises app is either a provider-hosted app that is hosted on an on-premises server or a SharePoint hosted app. Table 1 lists the different authentication user methods of SharePoint Server and whether that method can be used for SharePoint Server on-premises apps.
  
**Table 1. User authentication methods and support by on-premises apps**

|**Authentication method**|**Supported by SharePoint hosted apps**|**Supported by Provider hosted apps**|
|:-----|:-----|:-----|
|NTLM  <br/> |Yes  <br/> |Yes  <br/> |
|Kerberos  <br/> |Yes, but only when it is configured to use NTLM as a fallback authentication method. Kerberos-only is not supported.  <br/> |Yes  <br/> |
|Basic  <br/> |Yes  <br/> |Yes  <br/> |
|Anonymous  <br/> |Yes  <br/> |Yes  <br/> |
|Forms-based authentication using the default ASP.NET provider  <br/> |Yes  <br/> |Yes  <br/> |
|Forms-based authentication using Lightweight Directory Access Protocol (LDAP)  <br/> |Yes  <br/> |Yes  <br/> |
|Security Assertion Markup Language (SAML) authentication  <br/> |Yes, if the identity provider supports wildcard return uniform resource locator (URL) registration and honors the **wreply** parameter. .  <br/> To configure SharePoint Server to use the **wreply** parameter, use the following commands at a Microsoft PowerShell command prompt:  <br/> ```$p = Get-SPTrustedIdentityTokenIssuer$p.UseWReplyParameter = $true$p.Update()```> [!NOTE]> Active Directory Federation Services (AD FS) 2.0 version does not support wildcard for return URL registration.           |Yes  <br/> |
   
For more information about user authentication methods in SharePoint Server, see [Plan for user authentication methods in SharePoint Server](plan-user-authentication.md).
  
## Provide incoming access from external applications hosted on the Internet
<a name="inbound"> </a>

If external provider-hosted apps are located on the Internet, you have to configure a reverse web proxy to perform app authentication and request resources from intranet SharePoint farms. A configured reverse web proxy at the edge of your network has to allow incoming HTTP over SSL (HTTPS) connections from the apps to your SharePoint farms. You typically identify the HTTPS-based URLs that the external applications will access and configure the reverse proxy to publish those URLs and provide the appropriate security.
  
## Address User Profile application service considerations
<a name="UP"> </a>

High-trust apps generate their own access tokens, which include an assertion of the identity of the user on whose behalf they are acting. The server that runs SharePoint Server and services the incoming resource request must be able to resolve the request to a specific SharePoint user, a process known as rehydrating the user's identity. Note that this differs from app authentication for provider-hosted apps, in which the user is identified, but not asserted.
  
To rehydrate a user's identity, a server that runs SharePoint Server takes the claims from the incoming access token and resolves it to a specific SharePoint user. By default, SharePoint Server uses the built-in User Profile service application as the identity resolver.
  
The key user attributes for user identity rehydration are as follows:
  
- The Windows Security Identifier (SID)
    
- The Active Directory Domain Services (AD DS) user principal name (UPN)
    
- The Simple Mail Transfer Protocol (SMTP) address
    
- The Session Initiation Protocol (SIP) address
    
Therefore, the app must include at least one of these user attributes and that attribute must be current in user profiles. We recommend a periodic synchronization from identity stores to the User Profile service application.
  
Furthermore, SharePoint Server expects only one entry in the User Profile service application for a given lookup query that is based on one or more of these four attributes. Otherwise, it returns an error condition that multiple user profiles were found. Therefore, you should delete obsolete user profiles in the User Profile service application periodically to avoid multiple user profiles.
  
If a user profile exists for a user and the relevant group memberships are not synchronized, access may be denied when the user is supposed to be granted access for a given resource. Therefore, make sure that group memberships are synchronized with the User Profile service application.
  
## See also
<a name="UP"> </a>

#### Concepts

[Authentication overview for SharePoint Server](authentication-overview.md)

