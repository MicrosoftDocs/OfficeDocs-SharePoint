---
title: Plan for feeds and the Distributed Cache service in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: 4045020c-6ed2-4139-84f4-4bf7d099918d
---


# Plan for feeds and the Distributed Cache service in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-08-03* **Summary: ** Learn how to plan to implement microblog features, the Newsfeed, and the Distributed Cache service in SharePoint Server 2013 and SharePoint Server 2016.In SharePoint Server, microblog functionality enables users to have short, public conversations about topics they are interested in. The Newsfeed and the Distributed Cache service support this microblog functionality in SharePoint Server. .In this article:
-  [Planning for the Feeds](#planfeeds)
    
  
-  [Planning for the Distributed Cache service](#plandc)
    
  

## Plan for the feeds
<a name="planfeeds"> </a>


## Site feeds

Site feeds provide newsfeed functionality to a specific group of users. Site feeds are available on team sites. When planning to use site feeds on your team sites in SharePoint Server, the team sites must consume the same User Profile Service application as My Sites. Team Sites and My Sites can be located on the same or different farms, but must use the same User Profile service application. If you have team sites on a different farm from the My Site Host, server-to-server authentication between the two farms is required. In SharePoint Server, we recommend that the same service account be used for both the My Site host web application and the web application hosting the team sites. Additionally, the My Site host site collection must be a SharePoint Server My Site host, and the user must have a SharePoint Server My Site to use the site feed feature. Consider enabling Self Service Site Creation on the web application that contains the team sites so that users can easily create team sites from their My Site. In a SharePoint Server deployment where users only use **About Me** pages (the administrator has configured the rest of the My Site features to be unavailable), site feeds are still available to users.When an administrator upgrades team sites from SharePoint Server 2013 with Service Pack 1 (SP1), they must activate site feeds on the upgraded team site by first enabling the **Following Content** feature on the team site, and then enabling the **Site Feeds** feature on the team site. Following entities and seeing posts from Site Feeds are then available to the user.
> [!NOTE:]

  
    
    


## My Sites planning

A user can include an image in microblog posts. When posts include an image, SharePoint Server uploads that image to a private folder on the user’s My Site. This image is automatically reduced in file size and dimensions to optimize how much space is consumed by the image on the user's My Site. When assigning quotas for My Sites, an administrator should plan for this additional image storage requirement. If the user does not have available storage on their My Site and the user is attempting to post a message that has an image, an error is displayed to the user. 
## Notifications

Notifications are system-generated email messages that notify the user of an activity that occurs in a thread they contributed to, or that someone has started following them. Notifications require the configuration of outgoing email settings in SharePoint Server as a prerequisite. 
## Upgrade

When upgrading from SharePoint Server 2013 with Service Pack 1 (SP1) to SharePoint Server 2016, the newsfeeds from SharePoint Server 2013 with Service Pack 1 (SP1) are upgraded as a legacy feature in SharePoint Server 2016. This means that the SharePoint Server 2013 with Service Pack 1 (SP1) newsfeed is being deprecated, but is still available from within SharePoint Server. An administrator must perform special configuration steps to allow users access to the upgraded SharePoint Server 2013 with Service Pack 1 (SP1) newsfeed. Any data that is stored in the SharePoint Server 2013 with Service Pack 1 (SP1) newsfeed is available in SharePoint Server. However, an administrator cannot migrate data from the SharePoint Server 2013 with Service Pack 1 (SP1) newsfeed to the SharePoint Server newsfeed because the feeds differ significantly.
## Outlook Social Connector

The Outlook Social Connector displays feed information in Microsoft Outlook alongside Outlook messages, meetings, and so on. The Outlook Social Connector increases system load on a SharePoint Server server farm. This is because the Outlook Social Connector frequently accesses My Sites features and pushes the information into Outlook. This affects the performance of the SharePoint Server farm and should be considered when designing the server farm.
## Search and security trimming

The **Everyone** view and **Following** view contain public conversations (posts and replies), which all users can access. When public conversations are added to the search index in SharePoint Server, users can search for and view search results that include these public conversations. Security trimming does not apply to public conversations because there are no permissions assigned to the conversation. If users require security trimming to be applied to specific conversations, use site feeds on team sites. On the team site, assign permissions to the group of users who can participate in the conversation. The search results are then security trimmed based on the assigned permissions.Consider how you configure the incremental crawl schedule of the indexer because this affects how quickly conversations appear in the search results of users. If users actively use the microblog features to make posts and replies, they might expect to see conversations appear in the search results quicker. In this case, consider shorter intervals between updates.
## Plan for the Distributed Cache service
<a name="plandc"> </a>

When you plan to implement the Distributed Cache service, consider that the Distributed Cache service can be deployed in two modes: dedicated mode or collocated mode. In dedicated mode, all services other than the Distributed Cache service are stopped on the application server that runs the Distributed Cache service. In collocated mode, the Distributed Cache service runs together with other services on the application server. Dedicated mode is the recommended mode in which to deploy the Distributed Cache service.
> [!IMPORTANT:]

  
    
    


> [!IMPORTANT:]

  
    
    


## Install the Windows Server AppFabric prerequisite

When the SharePoint Server prerequisite installer runs, it installs Windows Server AppFabric. This is the recommended approach for installing Windows Server AppFabric on a server that is running SharePoint Server. If you already have Windows Server AppFabric installed on the server before you run the prerequisite installer, you must uninstall Windows Server AppFabric before you run the prerequisite installer. If an administrator decides to install Windows Server AppFabric manually, the administrator must install the CacheAdmin, CachingService, and CacheClient features, and use the **/gac** switch. For more information see [Automated Installation (AppFabric 1.1 Caching)](https://msdn.microsoft.com/en-us/library/hh351353.aspx) in the MSDN Library.
## Capacity planning for the Distributed Cache service

This section of the document helps administrators plan the architecture and memory requirements for servers hosting the Distributed Cache service. The Distributed Cache service stores data in-memory only and does not have a dependency on databases in SharePoint Server. Additionally, some services in SharePoint Server require significant memory resources which may affect the performance of the Distributed Cache service. The performance of the Distributed Cache service is significantly affected by both the choice of architecture and memory allocation for the Distributed Cache service. The following table lists different memory and architecture recommendations for the Distributed Cache service, depending on the total number of users.
### 

Deployment sizeSmall farmMedium farmLarge farmTotal number of users  <br/> < 10,000  <br/> < 100,000  <br/> < 500,000  <br/> Recommended cache size for the Distributed Cache service  <br/> 1 GB  <br/> 2.5 GB  <br/> 12 GB  <br/> Total memory allocation for the Distributed Cache service (double the recommended cache size above, plus reserve 2 GB for the OS)  <br/> 2 GB  <br/> 5 GB  <br/> 34 GB  <br/> 
> [!NOTE:]

  
    
    

Recommended architectural configuration  <br/> Dedicated server or co-located on a front-end server  <br/> Dedicated server  <br/> Dedicated server  <br/> Minimum cache hosts per farm  <br/> 1  <br/> 1  <br/> 2  <br/> 
> [!NOTE:]

  
    
    


## Memory allocation

The Distributed Cache service’s memory allocation for the cache size is set to a default value of 10 percent of total physical memory when SharePoint Server installs. An administrator can change the memory allocation for the Distributed Cache service by using the **Update-SPDistributedCacheSize** cmdlet. The Distributed Cache service can be assigned a maximum of 16GB of memory per cache host in the cache cluster. We recommend that you reserve 2 GB of memory for other services that are running on the server, and assign the remaining memory to the Distributed Cache service. For more information, see [Manage the Distributed Cache service in SharePoint Server](html/manage-the-distributed-cache-service-in-sharepoint-server.md).
> [!IMPORTANT:]

  
    
    


> [!IMPORTANT:]

  
    
    

If you require more memory, you can configure the Distributed Cache service to run on several application servers. In this case, the cache spans all the servers that are running the Distributed Cache service, and acts as one cache that supports the entire farm. To add another application server, join the new application server to the server farm by using the SharePoint Configuration Wizard. You should decide whether the new application server should run in dedicated or collocated mode. You must ensure that the memory allocation assigned to the Distributed Cache service is the same on all servers that are running the Distributed Cache service. Cached data is stored on one server, not both servers. For more information, see  [Manage the Distributed Cache service in SharePoint Server](html/manage-the-distributed-cache-service-in-sharepoint-server.md).When the Distributed Cache service runs in collocated mode, the physical memory of the server should be increased and all non-essential services stopped. We do not recommend that any of the following services or applications run on the same server as the Distributed Cache service:
- SQL Server 2008 or SQL Server 2012
    
  
- Search service
    
  
- Excel Services in SharePoint (only available in SharePoint Server 2013)
    
  
- Project Server services
    
  
When planning for developer workstations, the developer’s workstation should have a minimum of 32 GB of total physical memory. On developer workstations, SharePoint Server is installed as a single server deployment. This means that the Distributed Cache service is deployed in collocated mode. In collocated mode, there will be competition for memory resources. To manage memory resource allocation, a developer can shut down any services that are not used, or they can periodically restart SQL Server. 
> [!IMPORTANT:]

  
    
    


## Distributed Cache service configuration sequence

Starting and stopping the Distributed Cache service in an unplanned manner results in the Distributed Cache service becoming unstable. When performing the initial configuration of a SharePoint Server 2013 farm, perform the following steps in the following order:
- Run the Configuration Wizard to join all servers to the server farm. The Distributed Cache service is started on all web servers and application servers in the server farm. 
    
  
- Perform other farm configuration steps as necessary.
    
  
- When ready to configure the Distributed Cache service, confirm that the Distributed Cache service is running on all servers in the server farm. Then proceed to stop the Distributed Cache service on any server that is not intended to be part of the cache cluster. Avoid stopping and restarting the Distributed Cache service on a server. If the Distributed Cache service was accidentally stopped on a server and a restart of the Distributed Cache service is now required, refer to the guidance in  [Manage the Distributed Cache service in SharePoint Server](html/manage-the-distributed-cache-service-in-sharepoint-server.md). 
    
  

> [!IMPORTANT:]

  
    
    

As an alternative to the previous method, an administrator can install SharePoint Server without registering the Distributed Cache service on servers not intended to be part of the cache cluster. This can be achieved by using the **skipRegisterAsDistributedCachehost** parameter with the **New-SPConfigurationDatabase** or the **Connect-SPConfigurationDatabase** PowerShell cmdlets, or when running **psconfig.exe** at the command line. This parameter is optional.
## Firewall configuration considerations
<a name="firewall"> </a>

The Distributed Cache service uses the following communication ports:
- 22233
    
  
- 22234
    
  
- 22235
    
  
- 22236
    
  

> [!NOTE:]

  
    
    


