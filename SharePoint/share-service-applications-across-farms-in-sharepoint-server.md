---
title: Share service applications across farms in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: 9f0df411-ba75-4d04-9195-836129fe2282
---


# Share service applications across farms in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** Search Server 2013, SharePoint Foundation 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-25* **Summary:** Describes the process and cautions that are involved in sharing service applications across farms in SharePoint Server 2016.In SharePoint Server, some service applications can be shared across server farms.By publishing a service application, you can optimize resources, avoid redundancy, and provide enterprise-wide services without installing a dedicated enterprise services farm. You can publish the following service applications in a SharePoint Server farm:
- Business Data Connectivity
    
  
- Machine Translation
    
  
- Managed Metadata
    
  
- User Profile
    
  
- Search
    
  
- Secure Store
    
  
Additionally, a SharePoint 2013 farm can consume services from a SharePoint Server 2016 farm but a SharePoint Server 2016 farm cannot consume services from a SharePoint 2013 farm. For example, a SharePoint 2013 content farm can access a SharePoint Server 2016 farm, but a SharePoint Server 2016 content farm cannot access a SharePoint 2013 farm. This allows for upgrade of multi-farm environments in which a farm hosting service applications is upgraded first. In this scenario, the service applications and features that the SharePoint 2013 farm experiences are limited to those that are available in SharePoint 2013. For example, a SharePoint 2013 farm cannot consume the Machine Translation service application from a SharePoint Server 2016 farm and does not benefit from new features of any service application.
> [!IMPORTANT:]

  
    
    


> [!NOTE:]

  
    
    

The User Profile service must reside in the same datacenter as the content it supports — The performance of social features require the User Profile service application to be located in the same datacenter as My Sites, team sites, and community sites.The farm that contains the service application and publishes the service application so that other farms can consume the service application is known as the  *publishing farm*  . The farm that connects to a remote location to use a service application that the remote location is hosting is known as the *consuming farm*  .This article describes the steps that are required to publish and consume service applications across farms. These steps must be performed in the order listed.
1. Exchange trust certificates between the farms.
    
    To start, an administrator of the consuming farm must provide two trust certificates to the administrator of the publishing farm: a root certificate and a security token service (STS) certificate. Additionally, an administrator of the publishing farm must provide a root certificate to the administrator of the consuming farm. By exchanging certificates, each farm acknowledges that the other farm can be trusted. 
    
    For more information, see  [Exchange trust certificates between farms in SharePoint Server](html/exchange-trust-certificates-between-farms-in-sharepoint-server.md).
    
  
2. On the publishing farm, publish the service application.
    
    On the farm on which the service application is located, an administrator must explicitly publish the service application. Service applications that are not explicitly published are available to the local farm only.
    
    For more information, see  [Publish service applications in SharePoint Server](html/publish-service-applications-in-sharepoint-server.md).
    
  
3. On the consuming farm, set the permission to the appropriate service applications
    
    You must give the consuming farm permission to the Application Discovery and Load Balancing Service Application on the publishing farm. After doing this, give the consuming farm permission to the published service applications that it will be consuming.
    
    For more information, see  [Set permissions to published service applications in SharePoint Server](html/set-permissions-to-published-service-applications-in-sharepoint-server.md).
    
  
4. On the consuming farm, connect to the remote service application.
    
    After the publishing farm has published the service application, an administrator of the consuming farm can connect to that service application from the consuming farm if the address of the specific service application is known. 
    
    For more information, see  [Connect to service applications on remote farms in SharePoint Server](html/connect-to-service-applications-on-remote-farms-in-sharepoint-server.md).
    
    
    
    > [!IMPORTANT:]
      
5. Add the shared service application to a Web application proxy group on the consuming farm.
    
    An administrator must associate the new service application connection with a local Web application on the consuming farm. Only Web applications that are configured to use this association can use the remote service application. 
    
    For information about how to configure a Web application proxy group connection, see  [Add or remove service application connections from a web application in SharePoint Server](html/add-or-remove-service-application-connections-from-a-web-application-in-sharepoi.md).
    
    
    
    > [!NOTE:]
      
6. Configure server-to-server authentication between the publishing and consuming farms.
    
    To allow a web application or an application service to request a resource from a web application on another farm on behalf of a user, you have to configure server-to-server authentication between the farms. For more information, see **Configure server-to-server authentication between publishing and consuming farms**.
    
    
    
    > [!NOTE:]
      

# See also

#### 

 **How to upgrade an environment that uses content type syndication (SharePoint Server 2013)**
  
    
    

  
    
    

