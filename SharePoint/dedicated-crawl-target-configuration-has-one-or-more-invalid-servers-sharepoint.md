---
title: Dedicated crawl target configuration has one or more invalid servers (SharePoint Server 2016)
ms.prod: SHAREPOINT
ms.assetid: 80521ae8-be93-4d1c-9956-5f4bed1ac4a7
---


# Dedicated crawl target configuration has one or more invalid servers (SharePoint Server 2016)
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-05-30* **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "Dedicated crawl target configuration has one or more invalid servers", in SharePoint Server 2016. **Rule Name:**  Dedicated crawl target configuration has one or more invalid servers. **Summary:** Dedicated crawl target configuration has one or more invalid servers. This may degrade search crawl performance. **Cause:**  The URI is incorrect, or the server is not joined with a valid role to the SharePoint farm. **Resolution: Make sure the uniform resource identifier (URI) is correct, and the server is joined with a valid role to the SharePoint farm.**
1. Make sure that the URI is correct. A valid URI meets the following criteria:
    
  - The host portion of the URI should be the name of a server that has joined the SharePoint farm.
    
  
  - The URI Scheme should be HTTP.
    
  
  - The URI must not contain an absolute path.
    
  

    For more information, see  [URI class](https://go.microsoft.com/fwlink/p/?LinkID=193513).
    
  
2. Make sure that the server is joined with a valid role to the SharePoint farm. The server can be any of the following:
    
  - Front-end
    
  
  - Application server
    
  
  - Distributed cache
    
  
  - Search
    
  
  - Custom
    
  
  - Single-server farm
    
  
For more information, see  [Overview of MinRole Server Roles in SharePoint Server 2016](html/overview-of-minrole-server-roles-in-sharepoint-server-2016.md) and [Description of MinRole and associated services in SharePoint Server 2016](html/description-of-minrole-and-associated-services-in-sharepoint-server-2016.md).
## 


# See also

#### 

 [Add SharePoint server to a farm in SharePoint Server 2016](html/add-sharepoint-server-to-a-farm-in-sharepoint-server-2016.md)
  
    
    

  
    
    

