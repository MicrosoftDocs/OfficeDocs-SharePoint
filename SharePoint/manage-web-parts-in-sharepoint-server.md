---
title: Manage web parts in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: 39928a90-e197-4755-af49-130e1ba6f5e5
---


# Manage web parts in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Foundation 2013, SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-08-04* **Summary: ** Helps you prepare to manage security for web parts pages and controls that are used with SharePoint Server 2016 and SharePoint 2013.In SharePoint Server, a web parts page is a collection of web parts that combines list data, timely information, or useful graphics into a dynamic web page. The layout and content of a web parts page can be set for all users and then, optionally, personalized for individual users. A site owner or a site member with the appropriate permissions can create and customize web parts pages by using a browser to add, reconfigure, or remove web parts.You can use web parts on web parts pages, wiki pages, content pages, and publishing pages.The web parts infrastructure in SharePoint Server exists on a layer above the ASP.NET web parts infrastructure. To effectively protect SharePoint sites, server administrators must be familiar with security guidelines and best practices for ASP.NET. For more information, see  [Security Guidelines: ASP.NET](https://go.microsoft.com/fwlink/p/?LinkId=103423).
> [!NOTE:]

  
    
    


## Security for web parts pages and controls

Protecting web parts pages and controls is a collaborative effort. Developers, site administrators, and server administrators must work together to improve security for web parts and web parts pages. Developers should validate Web Part input to prevent server attacks. Server administrators must configure Internet Information Services (IIS) to use an appropriate authentication method. Server administrators also configure and deploy web parts solutions to a web server or web farm. After the solution is deployed, site administrators or server administrators define the permission levels and permissions that allow access to web parts pages.Thank you to Waqas Sarwar, Microsoft MVP, for providing the following article about web part security in SharePoint Server 2016,  [SharePoint 2016 Central Admin - Security - Manage Web Part security](https://krossfarm.com/?p=1483).The following articles about managing web parts in SharePoint Server are available in this section:
### 

ContentDescription [Configure and deploy web parts in SharePoint Server](html/configure-and-deploy-web-parts-in-sharepoint-server.md) <br/> How to secure and deploy web parts in SharePoint Server.  <br/>  [Edit existing web parts in SharePoint Server](html/edit-existing-web-parts-in-sharepoint-server.md) <br/> How to edit web parts and web part properties in SharePoint Server,  <br/> 
# See also

#### 

 [Administer sites and site collections in SharePoint Server](html/administer-sites-and-site-collections-in-sharepoint-server.md)
  
    
    
 [Configure and deploy web parts in SharePoint Server](html/configure-and-deploy-web-parts-in-sharepoint-server.md)
  
    
    
 [Edit existing web parts in SharePoint Server](html/edit-existing-web-parts-in-sharepoint-server.md)
  
    
    
 [Security for SharePoint Server](html/security-for-sharepoint-server.md)
  
    
    
 [Plan for user authentication methods in SharePoint Server](html/plan-for-user-authentication-methods-in-sharepoint-server.md)
  
    
    

#### 

 [Add, edit, minimize, or delete a Web Part from a page](https://support.office.com/en-us/article/Add-edit-minimize-or-delete-a-Web-Part-from-a-page-362b1684-ad95-4a53-b826-443d8d9bdee0)
  
    
    
 [Using web parts on pages](https://support.office.com/en-us/article/Using-web-parts-on-pages-336e8e92-3e2d-4298-ae01-d404bbe751e0?ui=en-US&amp;rs=en-US&amp;ad=US)
  
    
    

  
    
    

