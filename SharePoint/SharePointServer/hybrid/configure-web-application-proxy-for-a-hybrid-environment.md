---
title: "Configure Web Application Proxy for a hybrid environment"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 6/22/2017
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
ms.collection:
- Ent_O365_Hybrid
- IT_Sharepoint_Server
- IT_SharePoint_Hybrid_Top
- SPO_Content
localization_priority: Normal
ms.assetid: b95b4ecc-f31b-4bbc-9b3d-a9f111dac8a1
description: "Learn how to configure Windows Server 2012 R2 with Web Application Proxy (WA-P) as a reverse proxy device in a SharePoint hybrid environment."
---

# Configure Web Application Proxy for a hybrid environment

[!INCLUDE[appliesto-2013-2016-2019-SPO-md](../includes/appliesto-2013-2016-2019-SPO-md.md)]
  
This article describes Web Application Proxy and helps you set it up to use as a reverse proxy for a hybrid SharePoint Server environment.
  
## Before you begin

 **Accessibility note:** SharePoint Server supports the accessibility features of common browsers to help you administer deployments and access sites. For more information, see [Accessibility for SharePoint 2013](/SharePoint/accessibility-guidelines).
  
## About Web Application Proxy in a hybrid environment

Web Application Proxy is a Remote Access service in Windows Server 2012 R2 that publishes web applications that users can interact with from many devices. It also includes proxy functionality for Active Directory Federation Services (AD FS). This helps system administrators provide secure access to an AD FS server. By using Web Application Proxy, system administrators choose how users authenticate themselves to a web application and can determine who is authorized to use one.
  
In hybrid SharePoint Server environments in which SharePoint in Microsoft 365 requests data from SharePoint Server, you can use Windows Server 2012 R2 with Web Application Proxy as a reverse proxy device to securely relay requests from the Internet to your on-premises SharePoint Server farm. 
  
> [!IMPORTANT]
> To use Web Application Proxy as a reverse proxy device in a hybrid SharePoint Server environment, you must also deploy AD FS in Windows Server 2012 R2. 
  
> [!NOTE]
> To install and configure the Web Application Proxy feature, you must be a local administrator on the computer where Windows Server 2012 R2 is installed. The Windows Server 2012 R2 server running the Web Application Proxy feature can be a member of a domain or a workgroup. 
  
## Step 1: Install AD FS and the Web Application Proxy feature

For information about installing AD FS in Windows Server 2012 R2, see [Active Directory Federation Services Overview](/windows-server/identity/active-directory-federation-services).
  
For information about installing the Web Application Proxy feature in Windows Server 2012 R2, see [Install Server Roles and Features on a Server Core Server](/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/jj574158(v=ws.11)).
  
## Step 2: Configure the Web Application Proxy

This section describes how to configure the Web Application Proxy feature after it is installed:
  
1. Web Application Proxy matches the thumbprint against the secure channel certificate, which must be imported and installed in the local computer's Personal certificate store on the Web Application Proxy server.
    
2. Configure Web Application Proxy with a published application that can accept inbound requests from your SharePoint tenant.
    
### Import the Secure Channel SSL certificate

You must import the Secure Channel SSL certificate into the Personal store of the local computer account and then set permissions on the certificate's private key to allow the service account of the Web Application Proxy Service (appproxysvc) Full Control.
  
> [!NOTE]
> The default service account of the Web Application Proxy Service is the local computer **Network Service**. 
  
|||
|:-----|:-----|
|![Edit icon](../media/mod_icon_edit_m.png)|The location of the **Secure Channel SSL certificate** is recorded in **Row 1** (Secure Channel SSL Certificate location and Filename) of **Table 4b: Secure Channel SSL Certificate**.  <br/> If the certificate contains a private key, you will need to provide the certificate password, which is recorded in **Row 4** (Secure Channel SSL Certificate password) of **Table 4b: Secure Channel SSL Certificate**.  <br/> |
   
For information about how to import an SSL certificate, see [Import a Certificate](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc754489(v=ws.11)).
  
### Configure the published application

> [!NOTE]
> The steps in this section can be performed only by using Windows PowerShell. 
  
To configure a published application to accept and relay requests from your SharePoint tenant, type the following Microsoft PowerShell command.
  
```
Add-WebApplicationProxyApplication -ExternalPreauthentication ClientCertificate -ExternalUrl <external URL> -BackendServerUrl <bridging URL> -name <friendly name of the published application> -ExternalCertificateThumbprint <certificate thumbprint> -ClientCertificatePreauthenticationThumbprint <certificate thumbprint> -DisableTranslateUrlInRequestHeaders:$False -DisableTranslateUrlInResponseHeaders:$False
```

Where:
  
-  _\<externalUrl\>_ is the external URL for the web application. This is the public URL to which SharePoint in Microsoft 365 will send inbound requests for SharePoint Server content and resources. 
    
|||
|:-----|:-----|
|![Edit icon](../media/mod_icon_edit_m.png)|The external URL is recorded in **Row 3** (External URL) of **Table 3: Public Domain Info** in the SharePoint Hybrid worksheet. |
   
-  _\<bridging URL\>_ is the internal URL you configured for the primary web application in your on-premises SharePoint Server farm. This is the URL to which Web Application Proxy will relay inbound requests from SharePoint in Microsoft 365. 
    
|||
|:-----|:-----|
|![Edit icon](../media/mod_icon_edit_m.png)| The bridging URL is recorded in one the following locations in the SharePoint Hybrid worksheet:  <br/>  If your primary web application is configured with a *host-named site collection*, use the value in **Row 1** (Primary web application URL) of **Table 5a: Primary web application (host-named site collection)**.  <br/>  If your primary web application is configured with a  *path-based site collection*  , use the value in **Row 1** (Primary web application URL) of **Table 5b: Primary web application (path-based site collection without AAM)**.  <br/>  If your primary web application is configured with a  *path-based site collection with AAM*  , use the value in **Row 5** (Primary web application URL) of **Table 5c: Primary web application (path-based site collection with AAM)**.  <br/> |
   
-  _\<friendly name of the published application\>_ is a name you choose to identify the published application in Web Application Proxy. 
    
-  _\<certificate thumbprint\>_ is the certificate thumbprint, as a string with no spaces, of the certificate to use for the address specified by the  _ExternalUrl_ parameter. This value should be entered twice, once for the _ExternalCertificateThumbprint_ parameter and again for the _ClientCertificatePreauthenticationThumbprint_ parameter. 
    
|||
|:-----|:-----|
|![Edit icon](../media/mod_icon_edit_m.png)|This is the thumbprint of the **Secure Channel SSL certificate**. The location of this certificate file is recorded in **Row 1** (Secure Channel SSL Certificate location and Filename) of **Table 4b: Secure Channel SSL Certificate**. |
   
For additional information about the **Add-WebApplicationProxyApplication** cmdlet, see [Add-WebApplicationProxyApplication](/previous-versions/windows/powershell-scripting/dn283409(v=wps.630)).
  
## Validate the published application

To validate the published application, use the **Get-WebApplicationProxyApplication** cmdlet. Type the following Microsoft PowerShell command. 
  
```
Get-WebApplicationProxyApplication |fl
```

The output should resemble the content in the following table.
  
|||
|:-----|:-----|
|ADFSRelyingPartyID  <br/> |:\<populated at run time\>  <br/> |
|ADFSRelyingPartyName  <br/> |:\<relying party name\>  <br/> |
|BackendServerAuthenticationMode  <br/> |:ADFS  <br/> |
|BackendServerAuthenticationSPN  <br/> |: None  <br/> |
|BackendServerCertificateValidation  <br/> |: None  <br/> |
|BackendServerUrl  <br/> |: https://\<bridging URL\>/  <br/> |
|ClientCertificateAuthenticationBindingMode  <br/> |: None  <br/> |
|ClientCertificatePreauthenticationThumbprint :  <br/> |: \<certificate thumbprint\>  <br/> |
|DisableTranslateUrlInRequestHeaders  <br/> |: False  <br/> |
|DisableTranslateUrlInResponseHeaders  <br/> |: False  <br/> |
|ExternalCertificateThumbprint  <br/> |: \<certificate thumbprint\>  <br/> |
|ExternalPreauthentication  <br/> |: PassThrough  <br/> |
|ExternalUrl  <br/> |: https://\<external URL\>/  <br/> |
|ID  <br/> |: 91CFE805-44FB-A8A6-41E9-6197448BEA72  <br/> |
|InactiveTransactionsTimeoutSec  <br/> |: 300  <br/> |
|Name  <br/> |: \<friendly name of the published application\>  <br/> |
|UseOAuthAuthentication  <br/> |: False  <br/> |
|PSComputerName  <br/> |:  <br/> |
   
## Troubleshooting
<a name="troubleshooting"> </a>

Web Application Proxy logs events and errors to the Application and Remote Access Windows Server event logs. Logging plays an important role in troubleshooting issues with connectivity and authentication between SharePoint Server and SharePoint in Microsoft 365. Identifying the component that is causing a connection failure can be challenging, and reverse proxy logs are the first place you should look for clues. Troubleshooting can involve comparing log events from Web Application Proxy event logs, SharePoint Server ULS logs, Windows Server event logs, and Internet Information Services (IIS) logs on multiple servers.
  
For more info about troubleshooting techniques and tools for SharePoint Server hybrid environments, see [Troubleshooting hybrid environments](/SharePoint/hybrid/hybrid).
  
## See also
<a name="troubleshooting"> </a>

#### Concepts

[Hybrid for SharePoint Server](hybrid.md)
  
[Configure a reverse proxy device for SharePoint Server hybrid](configure-a-reverse-proxy-device-for-sharepoint-server-hybrid.md)

