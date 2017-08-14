---
title: Configure a reverse proxy device for SharePoint Server hybrid
ms.prod: SHAREPOINT
ms.assetid: 1780ec27-19f8-4d77-b787-8abc23921258
---


# Configure a reverse proxy device for SharePoint Server hybrid
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Online, SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-06-22* **Summary:** Learn about supported reverse proxy devices for SharePoint Server hybrid deployments. **This article is part of a roadmap of procedures for configuring SharePoint hybrid solutions. Be sure you're  [following a roadmap](html/sharepoint-server-2016-hybrid-configuration-roadmaps.md) when you do the procedures in this article.**This topic provides an overview of the role of reverse proxy devices in a SharePoint Server hybrid deployment and links to device-specific configuration guidance.In this article:
-  [The role of a reverse proxy in a SharePoint Server 2013 hybrid deployment](#role)
    
  
-  [General reverse proxy requirements](#requirements)
    
  
-  [Supported reverse proxy devices](#devices)
    
  

## The role of a reverse proxy in a SharePoint Server hybrid deployment
<a name="role"> </a>

SharePoint Server and SharePoint Online can be configured in a hybrid configuration to securely combine search results and external data from Microsoft Business Connectivity Services. Reverse proxy devices play a role in the secure configuration of a hybrid SharePoint Server deployment when inbound traffic from SharePoint Online needs to be relayed to your on-premises SharePoint Server farm. For example, if a federated user uses a SharePoint Online search portal that is configured to return hybrid search results, a reverse proxy device intercepts and pre-authenticates the request for on-premises SharePoint Server content and then relays it to SharePoint Server. The reverse proxy device in a hybrid topology provides a secure endpoint for inbound traffic using SSL encryption and client certificate authentication.
## How inbound connectivity works

The following diagrams show how a reverse proxy device is used for inbound connectivity.With an inbound search solution, only the SharePoint Online site has search results from both locations. **Inbound connectivity**
  
    
    
![A graphic of an inbound proxy.](images/)
  
    
    
In the example below, a federated user on the Internet uses the SharePoint Online search portal to search for content in both SharePoint Online and her company’s on-premises SharePoint Server server. **A federated user on the Internet searches for content that’s located on her company’s on-premises server.**
  
    
    
![This graphic explains how extranet users access files through TMG.](images/)
  
    
    
The following list describes the steps shown in the preceding picture.
  
    
    

1. From the Internet, a federated user browses to her SharePoint Online site.
    
  
2. SharePoint Online queries the search index in SharePoint Online and also sends the search query to the external URL of the on-premises SharePoint farm which resolves to the external endpoint of the reverse proxy device.
    
  
3. The reverse proxy device pre-authenticates the request using the Secure Channel SSL certificate and relays the request to the URL of the primary web application.
    
  
4. The SharePoint farm service account queries the on-premises search index and security trims the search results in the context of the user who sent the search request.
    
  
5. Security trimmed search results are returned to SharePoint Online and displayed on the search results page. This result set includes search results from the SharePoint Online search index and search results from the search index of the SharePoint Server farm.
    
  

    
> [!NOTE:]

  
    
    

For a more detailed description of this process, that shows how certificates are used and authentication and authorization work in this topology, see  [Poster: SharePoint 2013 Hybrid Topology: Certificate, Authentication, and Authorization flow](https://go.microsoft.com/fwlink/?LinkId=392320).
## General reverse proxy requirements
<a name="requirements"> </a>

In a hybrid SharePoint Server scenario, the reverse proxy must be able to:
- Support client certificate authentication with a wildcard or SAN SSL certificate.
    
  
- Support pass-through authentication for OAuth 2.0, including unlimited OAuth bearer token transactions.
    
  
- Accept unsolicited inbound traffic on **TCP port 443** (HTTPS).
    
    > [!TIP:]
      
- Bind a wildcard or SAN SSL certificate to a published endpoint.
    
  
- Relay traffic to an on-premises SharePoint Server farm or load balancer without rewriting any packet headers.
    
  

## Supported reverse proxy devices
<a name="devices"> </a>

The table below lists the currently supported reverse proxy devices for SharePoint Server hybrid deployments. This list will be updated as new devices are tested for supportability. Follow the steps in the configuration article for the reverse proxy device that you want to use. When you've completed configuring the reverse proxy device, return to your  [roadmap](html/sharepoint-server-2016-hybrid-configuration-roadmaps.md).
### 

Supported reverse proxy devices Configuration article Additional information Windows Server 2012 R2 with Web Application Proxy (WA-P)  <br/>  [Configure Web Application Proxy for a hybrid environment](html/configure-web-application-proxy-for-a-hybrid-environment.md) <br/> Web Application Proxy (WA-P) is a Remote Access service in Windows Server 2012 R2 that publishes web applications that users can interact with from many devices.  <br/> 
> [!IMPORTANT:]

  
    
    

Forefront Threat Management Gateway (TMG) 2010  <br/>  [Configure Forefront TMG for a hybrid environment](html/configure-forefront-tmg-for-a-hybrid-environment.md) <br/> Forefront TMG 2010 is a comprehensive, secure, web gateway solution that provides secure reverse proxy functionality.  <br/> 
> [!NOTE:]

  
    
    

F5 BIG-IP  <br/>  [Enabling SharePoint 2013 Hybrid Search with the BIG-IP](https://devcentral.f5.com/articles/enabling-sharepoint-2013-hybrid-search-with-the-big-ip) <br/> External content managed by F5 Networks.  <br/> Citrix NetScaler  <br/>  [Citrix NetScaler and Microsoft SharePoint 2013 Hybrid Deployment Guide](https://www.citrix.com/content/dam/citrix/en_us/documents/products-solutions/deployment-guide-netscaler-office-365-en.pdf) <br/> External content managed by Citrix.  <br/> 
# See also

#### 

 [Hybrid for SharePoint Server](html/hybrid-for-sharepoint-server.md)
  
    
    

  
    
    

