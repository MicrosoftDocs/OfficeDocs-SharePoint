---
title: "Authentication overview for SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 6/21/2017
audience: ITPro
ms.topic: overview
ms.prod: sharepoint-server-itpro
localization_priority: Priority
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
- Strat_SP_server
ms.custom: 
ms.assetid: 403e75f3-9e53-4d5b-a476-365e6e4bc92e
description: "Learn about how user authentication, app authentication, and server-to-server authentication work in SharePoint Server."
---

# Authentication overview for SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
SharePoint Server requires authentication for the following types of interactions:
  
- Users who access on-premises SharePoint resources
    
- Apps that access on-premises SharePoint resources
    
- On-premises servers that access on-premises SharePoint resources, or vice versa
    
    
## User authentication in SharePoint Server
<a name="userauth"> </a>

User authentication is the validation of a user's identity against an authentication provider, which is a directory or database that contains the user's credentials and can verify that the user submitted them correctly. User authentication occurs when a user attempts to access a SharePoint resource.
  
SharePoint Server supports claims-based authentication.
  
The result of a claims-based authentication is a claims-based security token, which the SharePoint Security Token Service (STS) generates. 
  
SharePoint Server supports Windows, forms-based, and Security Assertion Markup Language (SAML)-based claims authentication. For information about how these three authentication methods work, see the following videos.
  
> [!NOTE]
> The information in the videos applies to SharePoint Server 2013 and SharePoint Server 2016. 
  
**Windows claims authentication in SharePoint Server 2013 and 2016 video**

> [!VIDEO https://www.microsoft.com/videoplayer/embed/9627c892-e5c8-410c-8f26-4964a5292801?autoplay=false]
**Forms-based claims authentication in SharePoint Server 2013 and 2016 video**

> [!VIDEO https://www.microsoft.com/videoplayer/embed/8bafab78-092f-4ece-8b0b-6fb1aa7e315e?autoplay=false]
**SAML-based claims authentication in SharePoint Server 2013 and 2016 video**

> [!VIDEO https://www.microsoft.com/videoplayer/embed/a4ab580d-ac9f-4c4d-8c23-9ddfea7603cf?autoplay=false]

For more information, see [Plan for user authentication methods in SharePoint Server](plan-user-authentication.md).
  
## App authentication in SharePoint Server
<a name="appauth"> </a>

App authentication is the validation of a remote SharePoint app's identity and the authorization of the app and an associated user of a secured SharePoint resource request. App authentication occurs when an external component of a SharePoint Store app or an App Catalog app, such as a web server that is located on the intranet or the Internet, attempts to access a secured SharePoint resource. 
  
For example, suppose that a user opens a SharePoint page that contains an IFRAME of a SharePoint app, and that IFRAME needs an external component, such as a server on the intranet or the Internet, to access a secured SharePoint resource in order to render the page. The external component of the SharePoint app must be authenticated and authorized so that SharePoint provides the requested information and the app can render the page for the user.
  
Note that if the SharePoint app does not require a SharePoint secured resource to render the page for the user, app authentication is not needed. For example, a SharePoint app that provides weather forecast information and only has to access a weather information server on the Internet does not have to use app authentication. 
  
App authentication is a combination of two processes:
  
- Authentication
    
    Verifying that the application has registered correctly with a commonly trusted identity broker
    
- Authorization
    
    Verifying that the application and the associated user for the request has the appropriate permissions to perform its operation, such as accessing a folder or list or executing a query
    
To perform app authentication, the application obtains an access token either from the Microsoft Azure Access Control Service (ACS) or by self-signing an access token using a certificate that SharePoint Server trusts. The access token asserts a request for access to a specific SharePoint resource and contains information that identifies the app and the associated user, instead of the validation of the user's credentials. The access token is not a logon token. 
  
For SharePoint Store apps, an example of the authentication process is as follows:
  
1. A user opens a SharePoint web page that contains an IFRAME that has to be rendered by a SharePoint Store app, which is hosted on the Internet and uses ACS as its trust broker. To render the IFRAME for the user, the SharePoint Store app must access a SharePoint resource. 
    
2. The SharePoint STS requests and receives a context token from ACS.
    
3. SharePoint sends the requested web page together with the context token to the user's web browser.
    
4. The user's web browser sends a request for the IFRAME's content and the context token to the SharePoint Store app server on the Internet.
    
5. The SharePoint Store app server requests and receives an access token from ACS.
    
6. The SharePoint Store app server sends the SharePoint resource request and the access token to the SharePoint server.
    
7. The SharePoint server authorizes the access, checking both the app's permissions, which were specified when the app was installed, and the associated user's permissions.
    
8. If permitted, SharePoint sends the requested data to the SharePoint Store app server on the Internet.
    
9. The SharePoint Store app server on the Internet sends the IFRAME results to the web browser, which renders the IFRAME portion of the page for the user.
    
Notice how the SharePoint Store app has accessed SharePoint server resources without having to obtain the user's credentials. The access was authenticated through ACS, which is trusted by the server running SharePoint Server, and authorized through the set of app and user permissions.
  
For SharePoint App Catalog apps, an example of the authentication process is as follows:
  
1. A user opens a SharePoint web page that contains an IFRAME that has to be rendered by an App Catalog app that is hosted on the intranet and uses a self-signed certificate for its access tokens. To render the IFRAME for the user, the App Catalog app must access a SharePoint resource.
    
2. SharePoint sends the requested page along with the IFRAME to the user's web browser.
    
3. The user's web browser sends a request for the IFRAME's content to the App Catalog app server on the intranet.
    
4. The App Catalog app server authenticates the user and generates an access token, signed with its self-signed certificate.
    
5. The App Catalog app server sends the SharePoint resource request and the access token to the SharePoint server.
    
6. The SharePoint server authorizes the access, checking both the app's permissions, which were specified when the app was installed, and the associated user's permissions.
    
7. If permitted, the SharePoint server sends the requested data to the App Catalog app server on the intranet.
    
8. The App Catalog app server sends the IFRAME results to the web browser, which renders the IFRAME portion of the page for the user.
    
> [!NOTE]
> App Catalog apps can use either ACS or a self-signed certificate for their access tokens. 
  
For more information, see [Plan for app authentication in SharePoint 2013 Preview](/SharePoint/security-for-sharepoint-server/plan-for-app-authentication-in-sharepoint-server).
  
## Server-to-server authentication in SharePoint Server
<a name="s2sauth"> </a>

Server-to-server authentication is the validation of a server's request for resources that is based on a trust relationship established between the STS of the server that runs SharePoint Server and the STS of another server that supports the OAuth server-to-server protocol, such as on-premises running SharePoint Server, Exchange Server 2016, Skype for Business 2016, or Azure Workflow Service, and SharePoint Server running in Office 365. Based on this trust relationship, a requesting server can access secured resources on the SharePoint server on behalf of a specified user account, subject to server and user permissions.
  
For example, a server running Exchange Server 2016 can request resources of a server running SharePoint Server for a specific user account. This contrasts with app authentication, in which the app does not have access to user account credential information. The user can be currently signed in to the server making the resource request or not, depending on the service and the request.
  
When a server running SharePoint Server attempts to access a resource on a server or a server attempts to access a resource on a server running SharePoint Server, the incoming access request must be authenticated so that the server accepts the incoming access request and subsequent data. Server-to-server authentication verifies that the server running SharePoint Server and the user whom it is representing are trusted.
  
The token that is used for a server-to-server authentication is a server-to-server token, not a logon token. The server-to-server token contains information about the server that requests access and the user account on whose behalf the server is acting.
  
For on-premises servers, an example basic process is as follows:
  
1. A user opens a SharePoint web page that requires information from another server (for example, display the list of tasks from both SharePoint Server and Exchange Server 2016).
    
2. SharePoint Server generates a server-to-server token.
    
3. SharePoint Server sends the server-to-server token to the other server.
    
4. The other server validates the SharePoint server-to-server token.
    
5. The other server sends a message to SharePoint Server to indicate that the sent server-to-server token was valid.
    
6. The service on the server running SharePoint Server accesses the data on the server.
    
7. The service on the server running SharePoint Server renders the page for the user.
    
When both servers are running in Office 365, an example process is as follows:
  
1. A user opens a SharePoint web page that requires information from another server (for example, display the list of tasks from both SharePoint Online and Exchange Online).
    
2. SharePoint Online requests and receives a server-to-server token from ACS.
    
3. SharePoint Online sends the server-to-server token to the Office 365 server.
    
4. The Office 365 server verifies the user identity in the server-to-server token with ACS.
    
5. The Office 365 server sends a message to SharePoint Online to indicate that the sent server-to-server token was valid.
    
6. The service on SharePoint Online accesses the data on the Office 365 server.
    
7. The service on SharePoint Online renders the page for the user.
    
For more information, see [Plan for server-to-server authentication in SharePoint Server](plan-server-to-server-authentication.md).
  

