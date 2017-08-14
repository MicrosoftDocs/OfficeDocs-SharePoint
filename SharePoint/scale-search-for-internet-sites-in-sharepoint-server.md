---
title: Scale search for Internet sites in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: 651dba4d-8751-4bd8-9492-f2842b2e1177
---


# Scale search for Internet sites in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-25* **Summary:** Determine hardware requirements and review considerations to scale out SharePoint Server search topologies for Internet sites for performance and availability.This article lists the minimum hardware requirements for virtual machines and physical servers for search topologies for Internet sites.This article also provides basic guidance on the scaling of search topologies to improve performance and availability.In this article:
-  [Hardware requirements for search topologies for Internet sites](#HW_FIS)
    
  
-  [Performance considerations for a medium Internet sites topology](#Scale_FIS)
    
  

## Introduction

This article lists the minimum requirements and gives guidance about how and when to scale out search topologies for Internet sites.For examples of topologies, see the technical diagram  [Internet sites search architectures for SharePoint Server 2016](https://docs.com/officeitpro/2341/internet-sites-search-architectures-for-sharepoint).For an overview and a description of search components and the overall search architecture, see  [Overview of search architecture in SharePoint Server](html/overview-of-search-architecture-in-sharepoint-server.md) and the technical diagram [Search architectures for SharePoint Server 2016](http://download.microsoft.com/download/2/0/8/2081E053-4E56-4B87-87A4-9380D042B95D/SP_2016_Search_Architecture_Model.pdf).
## Hardware requirements for search topologies for Internet sites
<a name="HW_FIS"> </a>

The following tables show the hardware requirements for servers that host a medium search topology for Internet sites. The hardware requirements apply to:
- Application servers and Web servers that contain search components.
    
  
- Database servers that contain search databases.
    
  
The minimum listed RAM requirements for a server that hosts a search component is the total required amount of RAM for that server. For example, if you are hosting a content processing component, a search administration component and a crawl component on one server, the total amount of minimum required RAM for that server is 24 GB.Each server must have sufficient disk space for the base installation of the Windows Server operating system and sufficient disk space for diagnostics such as logging, debugging, creating memory dumps, and so on. For production use, the server also needs additional free disk space for day-to-day operations and for the page file. Follow the guidance on free disk space and page file size corresponding to your Windows Server installation.
> [!NOTE:]

  
    
    


### Application servers and Web servers hosting search components

Search component on the physical server RAM Hard disk Processor Index component  <br/> 48 GB for each server in the farm that hosts an index component, a query processing component and the Web front end.  <br/> 500 GB additional disk space, preferably a separate disk volume/partition.  <br/> **All components:** <br/> 64-bit, 4 cores minimum, 8 cores recommended.  <br/> Analytics processing component  <br/> 24 GB for each server in the farm that hosts an analytics processing component, a crawl component, a content processing component and/or a search administration component.  <br/> 300 GB additional disk space, preferably a separate disk volume/partition.  <br/> Crawl component  <br/> Content processing component  <br/> See the requirements listed for the analytics processing component.  <br/> 80 GB for system drive.  <br/> Query processing component  <br/> See the requirements listed for the index component.  <br/> Search administration component  <br/> See the requirements listed for the analytics processing component.  <br/> 
### Database servers hosting search databases

Component Minimum requirements Processor  <br/> 64-bit, 4 cores for small topologies.  <br/> 64-bit, 8 cores for medium topologies.  <br/> RAM  <br/> 8 GB for small topologies.  <br/> 16 GB for medium topologies.  <br/> Hard disk  <br/> 80 GB for system drive.  <br/> Hard disk space depends on the amount of content.  <br/> 
## Performance considerations for a medium Internet sites topology
<a name="Scale_FIS"> </a>

A medium Internet sites (FIS) topology is optimized for a corpus size of 3,400,000 items, processing approximately 100-200 documents per second, depending on language, and a usage pattern of 85 page views per second, which corresponds to 100 queries per second.
### Performance considerations

What to consider Why this is important Cache  <br/> The query and its results are cached with Windows Server AppFabric, in key-value pairs: the query being the key and the results being the value. For each query, there is an approximate 50% cache ratio. This means that if you have a usage pattern of 200 queries per second, about 100 queries are sent to the search index and the other 100 queries are cached. The results from the cache have lower query latency than those that you retrieve from the search index. For example, results for front-page queries that are often run are likely to be cached.  <br/> Continuous crawl  <br/> We recommend that you enable continuous crawl with an interval of one minute, instead of the default interval of 15 minutes. You can only enable continuous crawl on SharePoint content sources.  <br/> Anonymous access  <br/> With anonymous access, users do not have to use credentials to log on to a SharePoint Internet site. Anonymous queries are cached, so they are cheaper because of lower query latency. You must enable anonymous access in two locations: on the web front-end and on the site.  <br/> Query latency  <br/> Query latency is influenced by caching, anonymous access and by other factors such as the number and complexity of query rules that are applied and triggered. Also, consider the disks on which the search index is stored; a disk that has multiple spindles can improve the access speed of the disk and reduce query latency.  <br/> 
# See also

#### 

 [Manage the search topology in SharePoint Server](html/manage-the-search-topology-in-sharepoint-server.md)
  
    
    
 [Change the default search topology in SharePoint Server](html/change-the-default-search-topology-in-sharepoint-server.md)
  
    
    
 [Manage search components in SharePoint Server](html/manage-search-components-in-sharepoint-server.md)
  
    
    
 [Manage the index component in SharePoint Server](html/manage-the-index-component-in-sharepoint-server.md)
  
    
    

  
    
    

