---
title: Configure Web Application Proxy for a hybrid environment
ms.prod: SHAREPOINT
ms.assetid: b95b4ecc-f31b-4bbc-9b3d-a9f111dac8a1
---


# Configure Web Application Proxy for a hybrid environment
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-06-22* **Summary:** Learn how to configure Windows Server 2012 R2 with Web Application Proxy (WA-P) as a reverse proxy device in a SharePoint hybrid environment.This article describes Web Application Proxy and helps you set it up to use as a reverse proxy for a hybrid SharePoint Server environment.
## Before you begin

 **Accessibility note:** SharePoint Server supports the accessibility features of common browsers to help you administer deployments and access sites. For more information, see **Accessibility for SharePoint 2013**.
## About Web Application Proxy in a hybrid environment

Web Application Proxy is a Remote Access service in Windows Server 2012 R2 that publishes web applications that users can interact with from many devices. It also includes proxy functionality for Active Directory Federation Services (AD FS). This helps system administrators provide secure access to an AD FS server. By using Web Application Proxy, system administrators choose how users authenticate themselves to a web application and can determine who is authorized to use one.In hybrid SharePoint Server environments in which SharePoint Online requests data from SharePoint Server, you can use Windows Server 2012 R2 with Web Application Proxy as a reverse proxy device to securely relay requests from the Internet to your on-premises SharePoint Server farm. 
> [!IMPORTANT:]

  
    
    


> [!NOTE:]

  
    
    


## Step 1: Install AD FS and the Web Application Proxy feature

For information about installing AD FS in Windows Server 2012 R2, see  [Active Directory Federation Services Overview](https://technet.microsoft.com/en-us/library/hh831502.aspx).For information about installing the Web Application Proxy feature in Windows Server 2012 R2, see  [Install Server Roles and Features on a Server Core Server](https://technet.microsoft.com/en-us/library/jj574158.aspx).
## Step 2: Configure the Web Application Proxy

This section describes how to configure the Web Application Proxy feature after it is installed:
1. Web Application Proxy matches the thumbprint against the secure channel certificate, which must be imported and installed in the local computer’s Personal certificate store on the Web Application Proxy server.
    
  
2. Configure Web Application Proxy with a published application that can accept inbound requests from your SharePoint Online tenant.
    
  

## Import the Secure Channel SSL certificate

You must import the Secure Channel SSL certificate into the Personal store of the local computer account and then set permissions on the certificate’s private key to allow the service account of the Web Application Proxy Service (appproxysvc) Full Control.
> [!NOTE:]

  
    
    


### 

![Edit icon](images/)The location of the **Secure Channel SSL certificate** is recorded in **Row 1** (Secure Channel SSL Certificate location and Filename) of **Table 4b: Secure Channel SSL Certificate**. <br/> If the certificate contains a private key, you will need to provide the certificate password, which is recorded in **Row 4** (Secure Channel SSL Certificate password) of **Table 4b: Secure Channel SSL Certificate**. <br/> For information about how to import an SSL certificate, see  [Import a Certificate](https://technet.microsoft.com/en-us/library/cc754489.aspx).
## Configure the published application


> [!NOTE:]

  
    
    

To configure a published application to accept and relay requests from your SharePoint Online tenant, type the following Microsoft PowerShell command.
```

Add-WebApplicationProxyApplication -ExternalPreauthentication ClientCertificate -ExternalUrl <external URL> -BackendServerUrl <bridging URL> -name <friendly name of the published application> -ExternalCertificateThumbprint <certificate thumbprint> -ClientCertificatePreauthenticationThumbprint <certificate thumbprint> -DisableTranslateUrlInRequestHeaders:$False -DisableTranslateUrlInResponseHeaders:$False
```

Where:
-  *<externalUrl>*  is the external URL for the web application. This is the public URL to which SharePoint Online will send inbound requests for SharePoint Server content and resources.
    
### 

![Edit icon](images/)The external URL is recorded in **Row 3** (External URL) of **Table 3: Public Domain Info** in the SharePoint Hybrid worksheet.-  *<bridging URL>*  is the internal URL you configured for the primary web application in your on-premises SharePoint Server farm. This is the URL to which Web Application Proxy will relay inbound requests from SharePoint Online.
    
### 

![Edit icon](images/) The bridging URL is recorded in one the following locations in the SharePoint Hybrid worksheet: <br/>  If your primary web application is configured with a *host-named site collection*  , use the value in **Row 1** (Primary web application URL) of **Table 5a: Primary web application (host-named site collection)**. <br/>  If your primary web application is configured with a *path-based site collection*  , use the value in **Row 1** (Primary web application URL) of **Table 5b: Primary web application (path-based site collection without AAM)**. <br/>  If your primary web application is configured with a *path-based site collection with AAM*  , use the value in **Row 5** (Primary web application URL) of **Table 5c: Primary web application (path-based site collection with AAM)**. <br/> -  *<friendly name of the published application>*  is a name you choose to identify the published application in Web Application Proxy.
    
  
-  *<certificate thumbprint>*  is the certificate thumbprint, as a string with no spaces, of the certificate to use for the address specified by the *ExternalUrl*  parameter. This value should be entered twice, once for the *ExternalCertificateThumbprint*  parameter and again for the *ClientCertificatePreauthenticationThumbprint*  parameter.
    
### 

![Edit icon](images/)This is the thumbprint of the **Secure Channel SSL certificate**. The location of this certificate file is recorded in **Row 1** (Secure Channel SSL Certificate location and Filename) of **Table 4b: Secure Channel SSL Certificate**.For additional information about the **Add-WebApplicationProxyApplication** cmdlet, see [Add-WebApplicationProxyApplication](https://technet.microsoft.com/en-us/library/dn283409%28v=wps.630%29.aspx).
## Validate the published application

To validate the published application, use the **Get-WebApplicationProxyApplication** cmdlet. Type the following Microsoft PowerShell command.
```
Get-WebApplicationProxyApplication |fl
```

The output should resemble the content in the following table.
### 

ADFSRelyingPartyID  <br/> :<populated at run time>  <br/> ADFSRelyingPartyName  <br/> :<relying party name>  <br/> BackendServerAuthenticationMode  <br/> :ADFS  <br/> BackendServerAuthenticationSPN  <br/> : None  <br/> BackendServerCertificateValidation  <br/> : None  <br/> BackendServerUrl  <br/> : https://<bridging URL>/  <br/> ClientCertificateAuthenticationBindingMode   <br/> : None  <br/> ClientCertificatePreauthenticationThumbprint :  <br/> : <certificate thumbprint>  <br/> DisableTranslateUrlInRequestHeaders  <br/> : False  <br/> DisableTranslateUrlInResponseHeaders  <br/> : False  <br/> ExternalCertificateThumbprint  <br/> : <certificate thumbprint>  <br/> ExternalPreauthentication  <br/> : PassThrough  <br/> ExternalUrl  <br/> : https://<external URL>/  <br/> ID  <br/> : 91CFE805-44FB-A8A6-41E9-6197448BEA72  <br/> InactiveTransactionsTimeoutSec  <br/> : 300  <br/> Name  <br/> : <friendly name of the published application>  <br/> UseOAuthAuthentication  <br/> : False  <br/> PSComputerName  <br/> :  <br/> 
## Troubleshooting
<a name="troubleshooting"> </a>

Web Application Proxy logs events and errors to the Application and Remote Access Windows Server event logs. Logging plays an important role in troubleshooting issues with connectivity and authentication between SharePoint Server and SharePoint Online. Identifying the component that is causing a connection failure can be challenging, and reverse proxy logs are the first place you should look for clues. Troubleshooting can involve comparing log events from Web Application Proxy event logs, SharePoint Server ULS logs, Windows Server event logs, and Internet Information Services (IIS) logs on multiple servers.For more information on troubleshooting techniques and tools for SharePoint Server hybrid environments, see **Troubleshooting hybrid environments**.
# See also

#### 

 [Hybrid for SharePoint Server](html/hybrid-for-sharepoint-server.md)
  
    
    
 [Configure a reverse proxy device for SharePoint Server hybrid](html/configure-a-reverse-proxy-device-for-sharepoint-server-hybrid.md)
  
    
    

  
    
    

