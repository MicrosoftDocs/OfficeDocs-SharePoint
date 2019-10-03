---
title: "Plan alternate access mappings for SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 5/30/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 0d2efc06-afb4-40fe-9ac9-f973ac3d985f
description: "Learn how to plan for alternate access mappings in SharePoint Server."
---

# Plan alternate access mappings for SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
Alternate access mappings direct users to the correct URLs during their interaction with SharePoint Server 2016 (while browsing to the home page of a SharePoint Server 2016 website, for example). Alternate access mappings enable SharePoint Server to map web requests to the correct web applications and sites, and they enable SharePoint Server  to serve the correct content back to the user.
  
Because the features of alternate access mapping are deprecated, we recommend that you use host-named site collections over alternate access mappings.
  
For additional information about how to plan for host-named site collections, see [Host-named site collection architecture and deployment (SharePoint 2013)](host-named-site-collection-architecture-and-deployment.md).
    
Alternate access mappings were implemented because there are common Internet deployment scenarios in which the URL of a web request received by Internet Information Services (IIS) differs from the URL that was typed by a user. This is most likely to occur in deployment scenarios that include reverse proxy publishing and load balancing.
  
> [!NOTE]
> Alternate access mappings must be configured for load balancing, even though it generally does not apply to host header site collections. The default zone public URL should be set to a domain URL that is appropriate for all users to see. Unless you do this, the names of web servers or their IP addresses might be displayed in parameters that were passed between pages within SharePoint Server 2016. 
  
## About alternate access mappings
<a name="section1"> </a>

Alternate access mappings enable a web application that receives a request for an internal URL in one of the five zones to return pages that contain links to the public URL for the zone. You can associate a web application by using a collection of mappings between internal and public URLs. Internal refers to the URL of a web request as it is received by SharePoint Server. Public refers to the URL by which SharePoint will format links that correspond to requests that match one of the internal URLs on that zone when it returns a response. The public URL is the base URL that SharePoint Server uses in the pages that it returns. If the internal URL was changed by a reverse proxy device, it can differ from the public URL. 
  
> [!NOTE]
> Host-named site collections can't use alternate access mappings. Host-named site collections are automatically considered in the Default zone, and the URL of the request must not be changed between the user and the server. 
  
Multiple internal URLs can be associated with a single public URL. Mapping collections can contain up to five authentication zones. But each zone can have only a single public URL. Mapping collections correspond to the following authentication zones:
  
- Default
    
- Intranet
    
- Internet
    
- Custom
    
- Extranet
    
## Reverse proxy publishing
<a name="section2"> </a>

A reverse proxy is a device that sits between users and your web server. All requests to your web server are first received by the reverse proxy device and, if those requests pass the proxy's security filtering, the proxy forwards the requests to your web server.
  
## Alternate access mapping integration with authentication providers
<a name="section3"> </a>

Alternate access mappings allow you to expose a web application in as many as five different zones, with a different IIS website backing each zone. 
  
> [!NOTE]
> Some people mistakenly refer to this as having up to five different web applications sharing the same content databases. In reality, there is just one web application. 
  
Not only do these zones allow you to use multiple URLs to access the same web application, they also allow you to use multiple authentication providers to access the same web application.
  
When extending a web application into a zone, you have to use Windows authentication provided by IIS. After the web application has extended into the zone, you can change the zone to use a different type of authentication. 
  
Use the following procedure to change the authentication configuration for a zone.
  
 **To change the authentication type for a zone**
  
1. From **Administrative Tools**, open Central Administration.
    
2. On the Central Administration home page, click **Application Management**.
    
3. On the **Application Management** page, in the **Application Security** section, click **Authentication providers**.
    
4. On the **Authentication Providers** page, select your web application, which is listed in the **Web Application** box. 
    
5. Click the name of the zone whose authentication configuration you want to change.
    
    > [!NOTE]
    > You'll be able to select only from among zones that have a backing IIS website. These zones were assigned an IIS website during the "Extend an existing web application" procedure. 
  
6. On the **Edit Authentication** page, in the **Claims Authentication Types** section, select the authentication type that you want to use for this zone: 
    
  - **Windows authentication (default value)**
    
  - **Basic authentication**
    
  - **Forms based authentication (FBA)**
    
  - **Trusted Identity provider**
    
7. Change any other authentication configuration settings that you want to change, and click **Save**.
    
At this point, you can change authentication configuration settings for any other zone. You can configure completely independent authentication settings for different zones accessing the same content. For example, you might configure some content to be anonymously available while other content requires credentials. You could configure one zone to have anonymous access enabled and all other forms of authentication disabled, guaranteeing that only the anonymous content will be available. At the same time, another zone can have anonymous access disabled while NTLM authentication is enabled, guaranteeing that only authenticated access will be enabled. In addition, you can have different types of accounts to access the same content: one zone can be configured to use Active Directory accounts in Windows while another zone can be configured to use non-Active Directory accounts that use ASP.NET forms-based authentication.
  
## Alternate access mapping integration with web application policies
<a name="section4"> </a>

Web application policies allow administrators to grant or deny access to accounts and security groups for all sites exposed through a zone. This can be useful for many scenarios.
  
For example, the SharePoint Server search crawler must undergo the same authorization infrastructure as any other user: it can only crawl content that it has access to. But users would still like search to crawl restricted content so that authorized users can find that content in search results. The search service uses a Full Read policy on the web applications to give its crawler permission to read all content on that web application. That way, it can crawl and index all existing and future content, even content to which the site administrator had not explicitly given it access.
  
Another example would be helpdesk personnel who need administrative access to SharePoint Server sites so that they can help users. To do this, you can create a web application policy that grants the helpdesk staff accounts Full Control permission so that they have full administrative access to all current and future sites on the web application.
  
Because policies are tied to both web applications and their zones, you can guarantee that the policy that you have applied to one zone does not affect other zones. This can be useful if you have content exposed both on the corporate network and to the Internet. For example, suppose that you have given a helpdesk staff account Full Control permission over a web application's zone that is assigned to the corporate network. If someone were to try to use that account to access the site over the Internet, that Full Control policy wouldn't apply because it would recognize that the URL is in a different zone. Therefore, the account wouldn't automatically be given administrative access to the site.
  
## Alternate access mapping and external resource mapping
<a name="section5"> </a>

SharePoint Server allows you to extend the alternate access mapping functionality to content that is not hosted within the SharePoint Server farm. To configure this functionality, browse to the **Alternate Access Mappings** page, and then click **Map to External Resource**. You'll then be asked to create an entry for an external resource, which you can think of as another web application. After you have an external resource, you can assign different URLs and zones to it in the same manner that you do for web applications. This feature is not used in SharePoint Server, but third-party products that build onto SharePoint Server  can use it.
  
For example, the search technology in SharePoint Server  can crawl content external to the farm, such as file shares and websites. If that content is available at different URLs on different networks, you would want search to return results by using the appropriate URLs for the user's current network. By using alternate access mapping's external resource mapping technology, search can remap the external URLs in its results to match the user's zone.
  
## See also
<a name="section5"> </a>

#### Concepts

[Configure alternate access mappings for SharePoint 2013](configure-alternate-access-mappings.md)

