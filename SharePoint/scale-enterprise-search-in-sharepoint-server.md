---
title: Scale enterprise search in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: 3e2db0df-d07c-4adc-98a1-81e3fd42a272
---


# Scale enterprise search in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2016-11-23* **Summary:** Learn which approach to use to scale your enterprise search architecture for performance and availability.Sometimes it’s necessary to scale your search topology, for example:
- Because your search environment has grown in amount of content or number of users, or both.
    
  
- Because you’ve identified a bottleneck while monitoring your search solution and this bottleneck might affect the search performance.
    
  
- Because your search environment has specific performance requirements that weren’t addressed when you implemented one of the recommended search architectures described in Plan enterprise search architecture.
    
  

## How to scale your search topology


1. Redesign your search topology:
    
  - If you’re scaling because your search environment has grown, follow the guidance in  [Redesign enterprise search topology for more content and users in SharePoint 2016](html/redesign-enterprise-search-topology-for-more-content-and-users-in-sharepoint-201.md).
    
  
  - If you’re scaling because you have specific performance requirements or to remove a bottleneck, follow the guidance in  [Redesign enterprise search topology for specific performance requirements in SharePoint 2016](html/redesign-enterprise-search-topology-for-specific-performance-requirements-in-sha.md).
    
  
2. Implement the redesigned topology either on new servers, servers in your existing farm, or a combination. Follow the guidance in  [Manage the search topology in SharePoint Server](html/manage-the-search-topology-in-sharepoint-server.md).
    
  

