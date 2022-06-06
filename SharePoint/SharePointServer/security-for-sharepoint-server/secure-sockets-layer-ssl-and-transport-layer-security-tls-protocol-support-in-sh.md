---
title: "Secure Sockets Layer (SSL) and Transport Layer Security (TLS) protocol support in SharePoint Server"
ms.reviewer: 
ms.author: serdars
author: SerdarSoysal
manager: serdars
ms.date: 4/20/2022
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: reference
ms.prod: sharepoint-server-itpro
ms.localizationpriority: medium
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: f7fcf9d3-c895-4f91-b9c2-4036519a2fd5
description: "This article describes the versions of the Secure Sockets Layer (SSL) and Transport Layer Security (TLS) protocol that SharePoint Server supports."
---

# Secure Sockets Layer (SSL) and Transport Layer Security (TLS) protocol support in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-SUB-xxx-md](../includes/appliesto-2013-2016-2019-SUB-xxx-md.md)] 
  
SharePoint Server supports the following versions of the TLS protocol:
  
- TLS 1.0
    
- TLS 1.1
    
- TLS 1.2
    
- SSL 3.0
  > [!NOTE]
  > SharePoint Server 2016 does not fully support SSL 3.0. This is because SharePoint Server 2016 disables SSL 3.0 connection encryption by default for some, but not all features.
  
> [!IMPORTANT]
> We recommend completely disabling the SSL 3.0 protocol due to its security vulnerability. For additional information on how to completely disable SSL 3.0, see the "Disabled SSL 3.0 in Windows For Server Software" and "Disabled SSL 3.0 in Windows For Client Software" sections in [Microsoft Security Advisory 3009008](/security-updates/SecurityAdvisories/2015/3009008).
  
For information about how to enable TLS support, see:

- [Strong Transport Layer Security (TLS) Encryption in SharePoint Server Subscription Edition](strong-tls-encryption.md)

- [Enable TLS 1.1 and TLS 1.2 support in SharePoint Server 2019](enable-tls-1-1-and-tls-1-2-support-in-sharepoint-server-2019.md)

- [Enable TLS 1.1 and TLS 1.2 support in SharePoint Server 2016](enable-tls-1-1-and-tls-1-2-support-in-sharepoint-server-2016.md)
  
- [Enable TLS and SSL support in SharePoint 2013](enable-tls-and-ssl-support-in-sharepoint-2013.md)
    
    
## SSL and TLS Protocols that can be disabled

SharePoint Server supports disabling the following versions of the SSL/TLS protocol:
  
- TLS 1.0
    
- TLS 1.1
    
- TLS 1.2
    
- SSL 3.0
    
> [!NOTE]
> At least one of the following TLS protocols must remain enabled: TLS 1.0, TLS 1.1, or TLS 1.2. 
  
## See also

[Transport Layer Security (TLS) in SharePoint Server Subscription Edition](strong-tls-encryption.md)