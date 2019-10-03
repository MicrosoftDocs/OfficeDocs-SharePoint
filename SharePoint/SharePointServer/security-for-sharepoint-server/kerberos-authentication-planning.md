---
title: "Plan for Kerberos authentication in SharePoint Server"
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
ms.assetid: 3e66d9df-442e-445f-bddc-99b446c2a4cb
description: "Learn how to plan for Kerberos authentication in SharePoint Server and claims-based authentication."
---

# Plan for Kerberos authentication in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]  
  
The Kerberos protocol supports an authentication method that uses tickets that a trusted source provides. Kerberos tickets indicate that the network credentials of a user who is associated with a client computer were authenticated. The Kerberos protocol defines how users interact with a network service to gain access to network resources. The Kerberos Key Distribution Center (KDC) issues a ticket-granting-ticket (TGT) to a client computer on behalf of a user. In Windows, the client computer is a member of an Active Directory Domain Services (AD DS) domain and the TGT is proof that the domain controller authenticated the user credentials. 
  
Before establishing a network connection to a network service, the client computer presents its TGT to the KDC and requests a service ticket. Based on the previously issued TGT, which confirms that the client computer was authenticated, the KDC issues a service ticket to the client computer. The client computer then submits the service ticket to the network service. The service ticket must also contain an acceptable Service Principal Name (SPN) that identifies the service. To enable Kerberos authentication, the client and server computers must already have a trusted connection to the KDC. The client and server computers must also be able to access AD DS.
  
    
## Kerberos authentication and SharePoint Server
<a name="section1"> </a>

The reasons why you should consider Kerberos authentication are as follows:
  
- The Kerberos protocol is the strongest Integrated Windows authentication protocol, and supports advanced security features including Advanced Encryption Standard (AES) encryption and mutual authentication of clients and servers.
    
- The Kerberos protocol allows for delegation of client credentials.
    
- Of the available secure authentication methods, Kerberos requires the least amount of network traffic to AD DS domain controllers. Kerberos can reduce page latency in certain scenarios, or increase the number of pages that a front-end web server can serve in certain scenarios. Kerberos can also reduce the load on domain controllers.
    
- The Kerberos protocol is an open protocol that is supported by many platforms and vendors.
    
The reasons why Kerberos authentication might not be appropriate are as follows:
  
- In contrast to other authentication methods, Kerberos authentication requires additional infrastructure and environment configuration to function correctly. In many cases, domain administrator permission is required to configure Kerberos authentication which can be difficult to set up and manage. Misconfiguring Kerberos can prevent successful authentication to your sites.
    
- Kerberos authentication requires client computer connectivity to a KDC and to an AD DS domain controller. In a Windows and SharePoint deployment, the KDC is an AD DS domain controller. While this is a common network configuration on an organization intranet, Internet-facing deployments are typically not configured in this manner.
    
 **Kerberos delegation**
  
Kerberos authentication supports the delegation of client identity. This means that a service can impersonate an authenticated client's identity. Impersonation enables a service to pass the authenticated identity to other network services on behalf of the client. Claims-based authentication can also be used to delegate client credentials, but requires the back-end application to be claims-aware.
  
Used with SharePoint Server, Kerberos delegation enables a front-end service to authenticate a client and then use the client's identity to authenticate to a back-end system. The back-end system then performs its own authentication. When a client uses Kerberos authentication to authenticate with a front-end service, Kerberos delegation can be used to pass a client's identity to a back-end system. The Kerberos protocol supports two types of delegation:
  
- Basic Kerberos delegation (unconstrained)
    
- Kerberos constrained delegation
    
 **Basic Kerberos delegation and Kerberos constrained delegation**
  
Basic Kerberos delegation can cross domain boundaries within the same forest but cannot cross a forest boundary. Kerberos constrained delegation cannot cross domain or forest boundaries, except when you are using domain controllers that run Windows Server 2012. 
  
Depending on the service applications that are part of a SharePoint Server deployment, implementing Kerberos authentications with SharePoint Server can require Kerberos constrained delegation.
  
> [!IMPORTANT]
>  To deploy Kerberos authentication with any of the following service applications, SharePoint Server and all external data sources must reside in the same Windows domain: >  Excel Services >  PerformancePoint Services >  InfoPath Forms Services >  Visio Services >  These service applications are not available in SharePoint Foundation 2013. Excel Services is not available in SharePoint Server 2016. 
  
To deploy Kerberos authentication with any of the following service applications or products, SharePoint Server can use either basic Kerberos delegation or Kerberos constrained delegation:
  
- Business Data Connectivity service (this service application is not available in SharePoint Foundation 2013)
    
- Access Services (this service application is not available in SharePoint Foundation 2013)
    
- SQL Server Reporting Services (SSRS) (a separate product)
    
- Project Server 2016 (a separate product)
    
Services that are enabled for Kerberos authentication can delegate identity multiple times. As an identity travels from service to service, the delegation method can change from basic Kerberos to Kerberos constrained. However, the reverse is not possible. The delegation method cannot change from Kerberos constrained to basic Kerberos. Therefore, it is important to anticipate and plan for whether a back-end service will require basic Kerberos delegation. This can affect the planning and design of domain boundaries.
  
 A Kerberos-enabled service can use protocol transition to convert a non-Kerberos identity to a Kerberos identity that can be delegated to other Kerberos enabled services. This capability can be used, for example, to delegate a non-Kerberos identity from a front-end service to a Kerberos identity on a back-end service. 
  
> [!IMPORTANT]
> Protocol transition requires Kerberos constrained delegation. Therefore, protocol transitioned identities cannot cross domain boundaries. 
  
Claims-based authentication can be used as an alternative to Kerberos delegation. Claims-based authentication enables a client's authentication claim to be passed between different services if the services meet all of the following criteria: 
  
- There must be a trust relationship between the services.
    
- The services must be claims-aware.
    
For more information about Kerberos authentication, see the following resources:
   
- [Microsoft Kerberos](https://docs.microsoft.com/en-us/windows/desktop/secauthn/microsoft-kerberos)
    
- [Kerberos Explained](/previous-versions/windows/it-pro/windows-2000-server/bb742516(v=technet.10))

- [How the Kerberos Version 5 Authentication Protocol Works](/previous-versions/windows/it-pro/windows-server-2003/cc772815(v=ws.10))

- [Kerberos Authentication Tools and Settings](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc738673(v%3dws.10)) 
    
## Kerberos authentication and claims-based authentication
<a name="section2"> </a>

 SharePoint 2013 and SharePoint Server 2016 supports claims-based authentication. Claims-based authentication is built on the Windows Identity Foundation (WIF), which is a set of the .NET Framework classes that are used to implement claims-based identity. Claims-based authentication relies on standards such as WS-Federation and WS-Trust. For more information about claims-based authentication, see the following resources: 
  
- [Claims-based Identity for Windows (white paper)](https://go.microsoft.com/fwlink/p/?LinkId=198942) 
    
- [Windows Identity Foundation home page](https://go.microsoft.com/fwlink/p/?LinkId=198943)
    
    
When you create a SharePoint Server web application by using Central Administration, you must select one or more claims-based authentication types. When you create a SharePoint Server web application by using the **New-SPWebApplication** Microsoft PowerShell cmdlet, you can specify either claims authentication and claims authentication types or classic mode authentication. Claims authentication is recommended for all SharePoint Server web applications. By using claims authentication, all supported authentication types are available for your web applications and you can take advantage of server-to-server authentication and app authentication. For more information, see [What's new in authentication for SharePoint Server 2013](/SharePoint/what-s-new/new-and-improved-features-in-sharepoint-server-2016).
  
> [!IMPORTANT]
> The following service applications in SharePoint Server require the translation of claims-based credentials to Windows credentials. This process of translation uses the Claims to Windows Token Service (C2WTS): > **Excel Services**> **PerformancePoint Services**> **InfoPath Forms Services**> **Visio Services**> > These service applications are not available in SharePoint Foundation 2013. Excel Services is not available in SharePoint Server 2016. 
  
The service applications that require the C2WTS must use Kerberos constrained delegation because C2WTS requires protocol transition, which is only supported by Kerberos constrained delegation. For the service applications in the previous list, the C2WTS translates claims within the farm to Windows credentials for outgoing authentication. It is important to understand that these service applications can use the C2WTS only if the incoming authentication method is either Windows claims or Windows classic mode. Service applications that are accessed through web applications and that use Security Assertion Markup Language (SAML) claims or forms-based authentication claims do not use the C2WTS. Therefore, they cannot translate claims to Windows credentials.
  
## Kerberos authentication and the new SharePoint app model
<a name="section2"> </a>

If you are using Windows claims mode for user authentication and the web application is configured to use only Kerberos authentication without falling back to NTLM as the authentication protocol, then app authentication does not work. For more information, see [Plan for app authentication in SharePoint Server](plan-for-app-authentication-in-sharepoint-server.md).
  
## See also
<a name="section2"> </a>

#### Concepts

[Plan for user authentication methods in SharePoint Server](plan-user-authentication.md)

