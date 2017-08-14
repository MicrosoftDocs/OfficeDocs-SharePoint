---
title: Hardware and software requirements for SharePoint hybrid
ms.prod: SHAREPOINT
ms.assetid: 43e52f2f-2586-451d-814d-edf43f3459ab
---


# Hardware and software requirements for SharePoint hybrid
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** Office 365 Enterprise, SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-06-20* **Summary:** Learn what prerequisites you’ll need to configure hybrid for SharePoint Server.This article describes the prerequisites that are required to deploy a SharePoint hybrid solution between SharePoint Server and SharePoint Online in Office 365 for enterprises.
## Hardware and software requirements


- An operational, on-premises Active Directory Directory Services (AD DS) domain.
    
  
- An operational SharePoint Server farm. For more information, see  [Hardware and software requirements for SharePoint Server 2016](html/hardware-and-software-requirements-for-sharepoint-server-2016.md).
    
  
- A  [properly configured Office 365 tenant ](html/configure-office-365-for-sharepoint-hybrid.md) that is provisioned with SharePoint Online with one of the following subscription plans: E1 supports [Display hybrid federated search results in SharePoint Server](html/display-hybrid-federated-search-results-in-sharepoint-server.md) only, E3, or E4.
    
  

## Certificate requirements
<a name="CertReq"> </a>

For all SharePoint Server except hybrid OneDrive for Business you need to update your SharePoint Server Security Token Service (STS) certificate.The default STS certificate in the SharePoint farm doesn’t work in a SharePoint hybrid topology. You have to replace it on each server in the SharePoint Server farm with either a self-signed certification or a certificate that’s issued by a public certification authority.For more information, see  [Plan to replace the STS certificate](plan-server-to-server-authentication.md#ReplaceSTS). 
## Inbound connectivity requirements
<a name="CertReq"> </a>

The following hybrid solutions require inbound connectivity from Office 365 to SharePoint Server:
- Inbound hybrid search (displaying search results from SharePoint Server in Office 365)
    
  
- Hybrid Business Connectivity Services
    
  
- Hybrid Duet Enterprise Online for Microsoft SharePoint and SAP
    
  
For each of these hybrid solutions, the requirements in the following sections apply.
## Additional hardware requirements

Inbound connectivity requires the following:
- A reverse proxy device. For more information, see  [Reverse proxy device requirements](f6b221a8-97bd-48f3-8db1-b5c5357728fb.md#RPDreqs) later in this article.
    
  
- An Internet domain (such as https://adventureworks.com) and the permission to create or edit DNS records for that domain.
    
    
    
    > [!NOTE:]
      

## Certificate requirements

This section describes the certificates you’ll need to configure a inbound connectivity from Office 365 to SharePoint Server.
#### About the Secure Channel SSL certificate

This certificate provides authentication and encryption between the reverse proxy device and Office 365. It must be either a wildcard or a SAN certificate and be issued by a public root certification authority. For more information, see  [About Secure Channel SSL certificates](plan-connectivity-from-office-365-to-sharepoint-server.md#AboutSecureChannel) and [Get a Secure Channel SSL certificate](plan-connectivity-from-office-365-to-sharepoint-server.md#GetSecureChannel).
#### About the SSL certificate for the Security Token Service

The default certificate that is used for the Security Token Service (STS) in the SharePoint farm doesn’t work in a SharePoint hybrid topology. You have to replace it on each server in the on-premises SharePoint farm with either a self-signed certificate or a certificate that’s issued by a public certification authority. For more information, see  [About STS certificates](plan-connectivity-from-office-365-to-sharepoint-server.md#AboutSTS) and [Obtain an STS certificate](plan-connectivity-from-office-365-to-sharepoint-server.md#ObtainSTS).
#### About the on-premises SharePoint SSL certificate

If you’ll configure your primary web application to use SSL (which is the web application on the on-premises SharePoint farm that’s configured for hybrid), you’ll have to bind an SSL certificate to the primary web application.If this web application already exists and is configured for SSL, you’re ready to go. Otherwise you have to either obtain or create one for this purpose. For production environments, this certificate should be issued by a public certification authority (CA). For test and development environments, it can be a self-signed certificate.For more information, see  [Plan SSL certificates](plan-connectivity-from-office-365-to-sharepoint-server.md#certificates) and the [SharePoint 2013 Hybrid Topology: Certificate, Authentication, and Authorization](https://go.microsoft.com/fwlink/?LinkId=392320) poster.
#### Reverse proxy device requirements
<a name="RPDreqs"> </a>

The reverse proxy device provides a secure endpoint for inbound traffic using SSL encryption and client certificate authentication.
##### Supported reverse proxy devices
The following table lists the currently supported reverse proxy devices for SharePoint Server hybrid deployments. This list will be updated as new devices are tested for supportability.
### 

Supported reverse proxy devicesConfiguration articleMore informationWindows Server 2012 R2 with Web Application Proxy (WA-P)  <br/>  [Configure Web Application Proxy for a hybrid environment](html/configure-web-application-proxy-for-a-hybrid-environment.md) <br/> Web Application Proxy (WA-P) is a Remote Access service in Windows Server 2012 R2 that publishes web applications that users can interact with from many devices.  <br/> 
> [!IMPORTANT:]

  
    
    

Forefront Threat Management Gateway (TMG) 2010  <br/>  [Configure Forefront TMG for a hybrid environment](html/configure-forefront-tmg-for-a-hybrid-environment.md) <br/> Forefront TMG 2010 is a comprehensive, secure, web gateway solution that provides secure reverse proxy functionality.  <br/> 
> [!NOTE:]

  
    
    

F5 BIG-IP  <br/>  [Enabling SharePoint 2013 Hybrid Search with the BIG-IP](http://go.microsoft.com/fwlink/?LinkId=402977) <br/> This is external content that’s managed by F5 Networks.  <br/> 
##### General reverse proxy requirements
In a hybrid SharePoint Server scenario, the reverse proxy must be able to:
- Support client certificate authentication with a wildcard or SAN SSL certificate.
    
  
- Support pass-through authentication for OAuth 2.0, including unlimited OAuth bearer token transactions.
    
  
- Accept unsolicited inbound traffic on **TCP port 443** (HTTPS).
    
    
    
    > [!TIP:]
      
- Bind a wildcard or SAN SSL certificate to a published endpoint.
    
  
- Relay traffic to an on-premises SharePoint Server farm or load balancer without rewriting any packet headers.
    
  
For an overview of reverse proxy devices in a SharePoint hybrid topology, see  [Configure a reverse proxy device for SharePoint Server hybrid](html/configure-a-reverse-proxy-device-for-sharepoint-server-hybrid.md).
