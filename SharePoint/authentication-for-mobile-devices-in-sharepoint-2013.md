---
title: Authentication for mobile devices in SharePoint 2013
ms.prod: SHAREPOINT
ms.assetid: ad6a501d-5d8c-4b87-af69-7f655b8c3d1e
---


# Authentication for mobile devices in SharePoint 2013
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** Internet Explorer, OneDrive, SharePoint Server 2013*  * **Topic Last Modified:** 2017-07-20* This article contains information about the supported authentication types for select devices in SharePoint Server 2013.In this article:
-  [Plan for mobile device security](#PlanMobileDeviceSecurity)
    
  
-  [Authentication for mobile devices](#AuthenticationMobileDevices)
    
  

## Plan for mobile device security
<a name="PlanMobileDeviceSecurity"> </a>

Authentication is one aspect of security that you must consider to make sure that SharePoint Server 2013 is not compromised. We recommend that you consult the following articles to make sure that your corporate data is safe:
-  [Mobile security and authentication in SharePoint 2013](html/mobile-security-and-authentication-in-sharepoint-2013.md) (http://technet.microsoft.com/en-us/library/fp161350(v=office.15).aspx)
    
  
-  [Microsoft Safety &amp; Security Center – Mobile and wireless](http://go.microsoft.com/fwlink/?LinkID=533039&amp;clcid=0x409 ) (http://go.microsoft.com/fwlink/?LinkID=533039&amp;clcid=0x409)
    
  
-  [Microsoft Safety &amp; Security Center – Get smart about mobile phone safety](https://www.microsoft.com/security/online-privacy/mobile-phone-safety.aspx) (https://www.microsoft.com/security/online-privacy/mobile-phone-safety.aspx)
    
  
SharePoint Server 2013 supports multiple authentication methods and authentication modes. Not all mobile browsers and devices work with all the available authentication methods. When you plan for mobile device access, you must do the following:
- Determine the mobile devices that you must support. Then, learn the authentication methods that are supported by the mobile devices. This information varies by manufacturer.
    
  
- Determine the sites that you want to make available to your mobile device users.
    
  
- Determine whether you want to make SharePoint sites available for mobile devices when the devices are used outside the corporate firewall. If you do, the method that you use to enable external access can also affect mobile device authentication.
    
  

## Authentication for mobile devices
<a name="AuthenticationMobileDevices"> </a>

The following tables detail the authentication types for browsers and Office Hub Windows Phone experience in SharePoint Server 2013.
### Table: Mobile authentication support for SharePoint browsers

SharePoint InfrastructureAuthentication modeAuthentication providerWindows Phone 7.5 or later versions (Internet Explorer Mobile)iOS 5.0 or later versions (iPad, iPhone using Safari)SharePoint on-premises  <br/> NTLM  <br/> Active Directory  <br/> Supported  <br/> Supported  <br/> SharePoint on-premises  <br/> Basic authentication  <br/> Active Directory  <br/> Supported  <br/> Supported  <br/> SharePoint on-premises  <br/> SAML  <br/> WS-Federation 1.1 compatible Identity Provider  <br/> Supported  <br/> Supported  <br/> SharePoint Online  <br/> Forms-based authentication  <br/> Org-ID  <br/> Supported  <br/> Supported  <br/> 
### Table: Mobile authentication support for Office Hub

SharePoint infrastructureAuthentication modeAuthentication providerWindows Phone 7.5 or later versionsSharePoint on-premises  <br/> NTLM  <br/> Active Directory  <br/> Supported  <br/> SharePoint on-premises  <br/> Basic authentication  <br/> Active Directory  <br/> Not supported  <br/> SharePoint on-premises  <br/> SAML  <br/> WS-Federation 1.1 compatible Identity Provider  <br/> Not supported  <br/> SharePoint Online  <br/> Forms-based authentication  <br/> Org-ID  <br/> Supported  <br/> 
> [!IMPORTANT:]

  
    
    


# See also

#### 

 [Overview of mobile devices and SharePoint Server 2013](html/overview-of-mobile-devices-and-sharepoint-server-2013.md)
  
    
    

  
    
    

