---
title: Plan server-to-server authentication
ms.prod: SHAREPOINT
ms.assetid: 6951d670-e2a8-4a7e-b3ea-ccc9c00a0ffc
---


# Plan server-to-server authentication
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Online, SharePoint Server 2016*  * **Topic Last Modified:** 2017-06-20* **Summary:**  Plan and prepare to configure server-to-server authentication from SharePoint Server to Office 365 for SharePoint hybrid.Server-to-server authentication enables your SharePoint Server farm to consume content and resources from your Office 365 tenant. For example, search can be configured to allow federated users to see both SharePoint Server and SharePoint Online search results in a SharePoint Server search portal.The major thing that you need to plan for when configuring server-to-server authentication between SharePoint Server and Office 365 is your web application configuration.
## Plan your web application configuration for hybrid server-to-server authentication

This section helps you plan how to configure your SharePoint Server web application to support hybrid functionality.Outbound requests to SharePoint Online can be made from any web application in the on-premises SharePoint farm that uses **Integrated Windows authentication using NTLM**, as shown in the following image.
  
    
    
![Claim authentication types for SharePoint hybrid](images/)
  
    
    
If your existing web application is not configured to use Integrated Windows authentication using NTLM, you must either create a web application or extend your existing web application and configure it to use Integrated Windows authentication using NTLM.If you have to create a new web application to configure for hybrid functionality, you have two choices:
- **Extend an existing web application to connect to an existing content database.** This creates a new website in Internet Information Services (IIS) with a unique URL and authentication configuration. The extended web application can be used to access the same site collections and content as the original web application by using the new URL.
    
    This is the best choice if you want users to go to an enterprise search portal in an existing site collection to use hybrid search.
    
  
- **Create a new web application and a new content database.** This creates a new web application that has a new, empty content database in which you can create a new site collection with an enterprise search portal.
    
    This is the best choice if you want users to go to an enterprise search portal in a new site collection to use hybrid search.
    
  
Integrated Windows authentication using NTLM is required to allow the SharePoint Authentication service to pass user claims to SharePoint Online using OAuth.
