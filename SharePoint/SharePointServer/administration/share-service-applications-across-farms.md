---
title: "Share service applications across farms in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 9f0df411-ba75-4d04-9195-836129fe2282
description: "Describes the process and cautions that are involved in sharing service applications across farms in SharePoint Server."
---

# Share service applications across farms in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
In SharePoint Server, some service applications can be shared across server farms.
  
By publishing a service application, you can optimize resources, avoid redundancy, and provide enterprise-wide services without installing a dedicated enterprise services farm. You can publish the following service applications in a SharePoint Server farm:
  
- Business Data Connectivity
    
- Machine Translation
    
- Managed Metadata
    
- User Profile
    
- Search
    
- Secure Store
    
Additionally, a SharePoint (N-1) farm can consume services from a SharePoint Server (N) farm but a SharePoint Server (N) farm cannot consume services from a SharePoint (N-1) farm. This allows for upgrade of multi-farm environments in which a farm hosting service applications is upgraded first. In this scenario, the service applications and features that the SharePoint (N-1) farm experiences are limited to those that are available in SharePoint (N-1).

Cross farm service publishing supported scenarios:

- A SharePoint 2013 farm can consume services from a SharePoint 2016 farm

- A SharePoint 2016 farm can consume services from a SharePoint 2019 farm

> [!NOTE]
> It is not supported to consume services from a server version which is more than one version behind. This means it is not supported for a SharePoint (N-2+) farm to consume services from a SharePoint (N) farm. For example, SharePoint 2013 cannot consume services from SharePoint 2019 as well as SharePoint 2010 cannot consume services from SharePoint 2016.

 **Important:** There are significant restrictions on when services and content can be shared between a SharePoint 2010 farm and a SharePoint 2013 farm. Content type syndication uses the backup and restore mechanism in SharePoint Server to publish the content types across site collections. Backup and restore does not work across versions in the following scenarios:
  
- Between a SharePoint 2010 farm and a SharePoint 2013 farm
    
- Between sites in 2010 mode on a 2013 farm and those in 2013 mode on a 2013 farm
    
To learn how to work with these restrictions and successfully share services and content between SharePoint 2010 and SharePoint 2013 farms, see [How to upgrade an environment that uses content type syndication (SharePoint Server 2013)](/SharePoint/upgrade-and-update/how-to-upgrade-an-environment-that-uses-content-type-syndication-sharepoint-serv)
  
> [!NOTE]
> If the server farms are located in different domains, the User Profile service application requires both domains to trust one another. For the Business Data Connectivity service and Secure Store service application administration features to work from the consuming farm, the domain of the publishing farm must trust the domain of the consuming farm. Other cross-farm service applications work without a trust requirement between domains. 
  
The User Profile service must reside in the same datacenter as the content it supports — The performance of social features require the User Profile service application to be located in the same datacenter as My Sites, team sites, and community sites.
  
The farm that contains the service application and publishes the service application so that other farms can consume the service application is known as the publishing farm. The farm that connects to a remote location to use a service application that the remote location is hosting is known as the consuming farm. 
  
This article describes the steps that are required to publish and consume service applications across farms. These steps must be performed in the order listed.
  
1. Exchange trust certificates between the farms.
    
    To start, an administrator of the consuming farm must provide two trust certificates to the administrator of the publishing farm: a root certificate and a security token service (STS) certificate. Additionally, an administrator of the publishing farm must provide a root certificate to the administrator of the consuming farm. By exchanging certificates, each farm acknowledges that the other farm can be trusted. 
    
    For more information, see [Exchange trust certificates between farms in SharePoint Server](exchange-trust-certificates-between-farms.md).
    
2. On the publishing farm, publish the service application.
    
    On the farm on which the service application is located, an administrator must explicitly publish the service application. Service applications that are not explicitly published are available to the local farm only.
    
    For more information, see [Publish service applications in SharePoint Server](publish-a-service-application.md).
    
3. On the publishing farm, set the permission to the appropriate service applications for the consuming farm
    
    You must give the consuming farm permission to the Application Discovery and Load Balancing Service Application on the publishing farm. After doing this, give the consuming farm permission to the published service applications that it will be consuming.
    
    For more information, see [Set permissions to published service applications in SharePoint Server](set-permission-to-a-published-service-application.md).
    
4. On the consuming farm, connect to the remote service application.
    
    After the publishing farm has published the service application, an administrator of the consuming farm can connect to that service application from the consuming farm if the address of the specific service application is known. 
    
    For more information, see [Connect to service applications on remote farms in SharePoint Server](connect-to-a-service-application-on-a-remote-farm.md).
    
    > [!IMPORTANT]
    > You cannot share a User Profile service application across farms that reside in separate domains unless you first establish a domain-level trust between the two domains. 
  
5. Add the shared service application to a Web application proxy group on the consuming farm.
    
    An administrator must associate the new service application connection with a local Web application on the consuming farm. Only Web applications that are configured to use this association can use the remote service application. 
    
    For information about how to configure a Web application proxy group connection, see [Add or remove service application connections from a web application in SharePoint Server](add-or-remove-a-service-application-connection-to-a-web-application.md).
    
    > [!NOTE]
    > It's important that you plan the proxy group layout before you add service applications to proxy groups. 
  
6. Configure server-to-server authentication between the publishing and consuming farms.
    
    To allow a web application or an application service to request a resource from a web application on another farm on behalf of a user, you have to configure server-to-server authentication between the farms. For more information, see [Configure server-to-server authentication between publishing and consuming farms](configure-server-to-server-authentication-in-sharepoint.md).
    
    > [!NOTE]
    > Web applications or application services that request resources from an application service on another farm do not require server-to-server authentication. 
  
## See also

#### Other Resources

[How to upgrade an environment that uses content type syndication (SharePoint Server 2013)](../upgrade-and-update/how-to-upgrade-an-environment-that-uses-content-type-syndication-sharepoint-serv.md)

