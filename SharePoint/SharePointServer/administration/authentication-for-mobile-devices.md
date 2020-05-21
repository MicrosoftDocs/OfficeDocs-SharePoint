---
title: "Authentication for mobile devices in SharePoint 2013"
ms.reviewer: 
ms.author: toresing
author: tomresing
manager: pamgreen
ms.date: 7/20/2017
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: ad6a501d-5d8c-4b87-af69-7f655b8c3d1e
description: "This article contains information about the supported authentication types for select devices in SharePoint Server 2013."
---

# Authentication for mobile devices in SharePoint 2013

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)]

This article contains information about the supported authentication types for select devices in SharePoint Server 2013.
  
    
## Plan for mobile device security
<a name="PlanMobileDeviceSecurity"> </a>

Authentication is one aspect of security that you must consider to make sure that SharePoint Server 2013 is not compromised. We recommend that you consult the following articles to make sure that your corporate data is safe:
  
- [Mobile security and authentication in SharePoint 2013](mobile-security-and-authentication.md) (/SharePoint/administration/mobile-security-and-authentication) 
    
- [The Importance of Smartphone Security](https://www.microsoft.com/security/blog/2013/06/19/the-importance-of-smartphone-security/) 
  
SharePoint Server 2013 supports multiple authentication methods and authentication modes. Not all mobile browsers and devices work with all the available authentication methods. When you plan for mobile device access, you must do the following:
  
- Determine the mobile devices that you must support. Then, learn the authentication methods that are supported by the mobile devices. This information varies by manufacturer.
    
- Determine the sites that you want to make available to your mobile device users.
    
- Determine whether you want to make SharePoint sites available for mobile devices when the devices are used outside the corporate firewall. If you do, the method that you use to enable external access can also affect mobile device authentication.
    
## Authentication for mobile devices
<a name="AuthenticationMobileDevices"> </a>

The following tables detail the authentication types for browsers and Office Hub Windows Phone experience in SharePoint Server 2013.
  
**Table: Mobile authentication support for SharePoint browsers**

|**SharePoint Infrastructure**|**Authentication mode**|**Authentication provider**|**Windows Phone 7.5 or later versions (Internet Explorer Mobile)**|**iOS 5.0 or later versions (iPad, iPhone using Safari)**|
|:-----|:-----|:-----|:-----|:-----|
|SharePoint on-premises  <br/> |NTLM  <br/> |Active Directory  <br/> |Supported  <br/> |Supported  <br/> |
|SharePoint on-premises  <br/> |Basic authentication  <br/> |Active Directory  <br/> |Supported  <br/> |Supported  <br/> |
|SharePoint on-premises  <br/> |SAML  <br/> |WS-Federation 1.1 compatible Identity Provider  <br/> |Supported  <br/> |Supported  <br/> |
|SharePoint  <br/> |Forms-based authentication  <br/> |Org-ID  <br/> |Supported  <br/> |Supported  <br/> |
   
**Table: Mobile authentication support for Office Hub**

|**SharePoint infrastructure**|**Authentication mode**|**Authentication provider**|**Windows Phone 7.5 or later versions**|
|:-----|:-----|:-----|:-----|
|SharePoint on-premises  <br/> |NTLM  <br/> |Active Directory  <br/> |Supported  <br/> |
|SharePoint on-premises  <br/> |Basic authentication  <br/> |Active Directory  <br/> |Not supported  <br/> |
|SharePoint on-premises  <br/> |SAML  <br/> |WS-Federation 1.1 compatible Identity Provider  <br/> |Not supported  <br/> |
|SharePoint  <br/> |Forms-based authentication  <br/> |Org-ID  <br/> |Supported  <br/> |
   
> [!IMPORTANT]
> In order for mobile devices to communicate with SharePoint servers, Internet Protocol security (IPsec) must be disabled on the servers. This must be done because mobile devices are not domain-joined. 
  
## See also
<a name="AuthenticationMobileDevices"> </a>

#### Concepts

[Overview of mobile devices and SharePoint Server 2013](mobile-devices-overview.md)

