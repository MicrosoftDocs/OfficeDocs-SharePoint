---
title: "Hardware and software requirements for SharePoint hybrid"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 2/5/2018
audience: ITPro
ms.topic: get-started-article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- Ent_O365_Hybrid
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
- M365-collaboration
ms.assetid: 43e52f2f-2586-451d-814d-edf43f3459ab

description: "Learn what prerequisites you'll need to configure hybrid for SharePoint Server."
---

# Hardware and software requirements for SharePoint hybrid

[!INCLUDE[appliesto-2013-2016-2019-SPO-md](../includes/appliesto-2013-2016-2019-SPO-md.md)]
  
This article describes the prerequisites that are required to deploy a SharePoint hybrid solution between SharePoint Server and SharePoint Online in Office 365 for enterprises.
  
## Hardware and software requirements

- An operational, on-premises Active Directory Directory Services (AD DS) domain.
    
- An operational SharePoint Server farm. Services must be running on the local farm - farms with federated services are not supported. For more information about setting up a farm, see [Install SharePoint Server](../install/install.md).
    
- A [properly configured Office 365 tenant](configure-office-365-for-sharepoint-hybrid.md) that is provisioned with SharePoint Online with one of the following subscription plans: E1 supports [Display hybrid federated search results in SharePoint Server](display-hybrid-federated-search-results-in-sharepoint-server.md) only, E3, or E4. 
    
## Certificate requirements
<a name="CertReq"> </a>

The default STS certificate in the SharePoint farm is used by the hybrid picker to establish the token signing trust when configuring hybrid workloads. Using the inbuilt STS certificate is the recommended approach when configuring hybrid workloads. If however, you intend to use a publicly signed certificate instead of the inbuilt STS one then you must replace the inbuilt certificate with your own following the provided guidance.
  
For more information, see [Replace the STS certificate](plan-server-to-server-authentication-0.md).
  
## Inbound connectivity requirements
<a name="CertReq"> </a>

The following hybrid solutions require inbound connectivity from Office 365 to SharePoint Server:
  
- Inbound hybrid search (displaying search results from SharePoint Server in Office 365)
    
- Hybrid Business Connectivity Services
    
- Hybrid Duet Enterprise Online for Microsoft SharePoint and SAP
    
For each of these hybrid solutions, the requirements in the following sections apply.
  
### Additional hardware requirements

Inbound connectivity requires the following:
  
- [A reverse proxy device](configure-a-reverse-proxy-device-for-sharepoint-server-hybrid.md). The reverse proxy device provides a secure endpoint for inbound traffic using SSL encryption and client certificate authentication.
    
- An Internet domain (such as https://adventureworks.com) and the permission to create or edit DNS records for that domain.
    
    > [!NOTE]
    > This public domain must be registered by using a domain registrar, such as GoDaddy.com, and must be the same domain that the URL of the external endpoint of the reverse proxy device is associated with. 
  
### Certificate requirements

This section describes the certificates you'll need to configure a inbound connectivity from Office 365 to SharePoint Server.
  
#### About the Secure Channel SSL certificate

This certificate provides authentication and encryption between the reverse proxy device and Office 365. It must be either a wildcard or a SAN certificate and be issued by a public root certification authority. For more information, see [About Secure Channel SSL certificates](plan-connectivity-from-office-365-to-sharepoint-server.md#AboutSecureChannel) and [Get a Secure Channel SSL certificate](plan-connectivity-from-office-365-to-sharepoint-server.md#GetSecureChannel).
  
#### About the on-premises SharePoint SSL certificate

If you'll configure your primary web application to use SSL (which is the web application on the on-premises SharePoint farm that's configured for hybrid), you'll have to bind an SSL certificate to the primary web application.
  
If this web application already exists and is configured for SSL, you're ready to go. Otherwise you have to either obtain or create one for this purpose. For production environments, this certificate should be issued by a public certification authority (CA). For test and development environments, it can be a self-signed certificate.
  
For more information, see [Plan SSL certificates](plan-connectivity-from-office-365-to-sharepoint-server.md#certificates). 
  
#### Supported reverse proxy devices

The following table lists the currently supported reverse proxy devices for SharePoint Server hybrid deployments. This list will be updated as new devices are tested for supportability.
  
|**Supported reverse proxy devices**|**Configuration article**|**More information**|
|:-----|:-----|:-----|
|Windows Server 2012 R2 with Web Application Proxy (WA-P)  <br/> |[Configure Web Application Proxy for a hybrid environment](configure-web-application-proxy-for-a-hybrid-environment.md) <br/> |Web Application Proxy (WA-P) is a Remote Access service in Windows Server 2012 R2 that publishes web applications that users can interact with from many devices.  <br/> > [!IMPORTANT]> To use Web Application Proxy as a reverse proxy device in a hybrid SharePoint Server environment, you must also deploy AD FS in Windows Server 2012 R2. Earlier versions of Windows don't support Web Application Proxy           |
|Forefront Threat Management Gateway (TMG) 2010  <br/> |[Configure Forefront TMG for a hybrid environment](configure-forefront-tmg-for-a-hybrid-environment.md) <br/> |Forefront TMG 2010 is a comprehensive, secure, web gateway solution that provides secure reverse proxy functionality.  <br/> Note that Forefront TMG 2010 is no longer sold by Microsoft but will be supported through 4/14/2020. For more information, see [Microsoft Support Lifecycle information for Forefront TMG 2010](http://go.microsoft.com/fwlink/p/?LinkID=784960&amp;clcid=0x409).           |
|F5 BIG-IP  <br/> |[Enabling SharePoint 2013 Hybrid Search with the BIG-IP](https://devcentral.f5.com/articles/enabling-sharepoint-2013-hybrid-search-with-the-big-ip) <br/> |This is external content that's managed by F5 Networks.  <br/> |
   
#### General reverse proxy requirements

In a hybrid SharePoint Server scenario, the reverse proxy must be able to:
  
- Support client certificate authentication with a wildcard or SAN SSL certificate.
    
- Support pass-through authentication for OAuth 2.0, including unlimited OAuth bearer token transactions.
    
- Accept unsolicited inbound traffic on **TCP port 443** (HTTPS). 
    
    > [!TIP]
    > No ports other than TCP 443 have to be opened on the external reverse proxy endpoint to support hybrid connectivity. 
  
- Bind a wildcard or SAN SSL certificate to a published endpoint.
    
- Relay traffic to an on-premises SharePoint Server farm or load balancer without rewriting any packet headers.
    
For an overview of reverse proxy devices in a SharePoint hybrid topology, see [Configure a reverse proxy device for SharePoint Server hybrid](configure-a-reverse-proxy-device-for-sharepoint-server-hybrid.md).
  

