---
title: Extend claims-based web applications in SharePoint
ms.prod: SHAREPOINT
ms.assetid: 265ace67-3115-4987-ab2d-80c55e452d4b
---


# Extend claims-based web applications in SharePoint
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-06* **Summary:** Learn how to extend an existing claims-based SharePoint Server 2013 and SharePoint Server 2016 web application into a new zone to surface content to different types of users.You can extend a web application that uses claims-based authentication by using Central Administration. When you extend a web application, you expose the same content to different sets of users by using an additional IIS web site to host the same content.
## Extend a claims-based web application by using Central Administration

Use the procedure described in this section to extend a claims-based SharePoint Server web application using the Central Administration. **To extend a claims-based web application**
1. Start SharePoint 2016 Central Administration.
    
  
2. On the Central Administration Home page, in the **Application Management** section, click **Manage web applications**.
    
  
3. Select the web application you want to extend and, in the **Contribute** group of the ribbon, click **Extend**.
    
  
4. On the **Extend Web Application to Another IIS Web Site** page, in the **IIS Web Site** section, configure the settings for your extended web application by selecting one of the following two options:
    
  - Click **Use an existing IIS web site**, and then select the web site on which to extend your existing web application.
    
  
  - Click **Create a new IIS web site**, and then type the name of the web site in the **Name** box.
    
  
5. In the **IIS Web Site** section, in the **Port** box, type the port number you want to use to access the web application. If you are creating a new web site, this box contains a suggested port number. If you are using an existing web site, this box contains the current port number.
    
    > [!NOTE:]
      
6. Optional: In the **IIS Web Site** section, in the **Host Header** box, type the host name (for example, www.contoso.com) that you want to use to access the web application.
    
    > [!NOTE:]
      
7. In the **IIS Web Site** section, in the **Path** box, type the path to the site directory on the server. If you are creating a new web site, this box contains a suggested path. If you are using an existing web site, this box contains the current path of that web site.
    
  
8. In the **Security Configuration** section, select the authentication method that you want to use for the web application and choose whether or not to use **Use Secure Sockets Layer (SSL)**.
    
    > [!IMPORTANT:]
      

  - Under **Authentication provider**, select **NTLM** or **Negotiate (Kerberos)**.
    
    Kerberos is the recommended security configuration to use with Integrated Windows authentication. Kerberos requires special configuration by the domain administrator. NTLM authentication will work with any application pool account.
    
  
  - In the **Security Configuration** section, click **Yes** or **No** for the **Use Secure Sockets Layer (SSL)** options. If you choose **Yes**, you must request and install an SSL certificate to configure SSL. For more information about how to set up SSL, see [How to Setup SSL on IIS 7.0](https://go.microsoft.com/fwlink/p/?LinkId=187887).
    
  
9. In the **Public URL** section, type the URL for the domain name for all sites that users will access in this web application. This URL will be the base URL for links on pages within the web application. The default URL is the current server name and port.
    
  
10. In the **Public URL** section, select the zone to use for the web application in the drop-down menu.
    
  
11. Click **OK** to extend the existing web application.
    
  

## Extended web applications and cross-site publishing

If you're using  [cross-site publishing](html/overview-of-cross-site-publishing-in-sharepoint-server.md), be careful about extending the web application. Depending on which site collection you extend the web application for, it can break the friendly URLs to your catalog items. Here’s what you should do:
  
    
    

- On your authoring site, don’t extend the web application. It’ll break the friendly URLs to your catalog items. For example, the URL to your catalog item will not point to the friendly URL http://www.contoso.com/Computers/model101 but to the catalog item in your authoring site, for examplehttp://www.contoso.com/sites/catalog/Lists/Products/DispForm.aspx?ID=1&amp;Source=http%3A%2F%. 
    
  
- On your publishing site, if you want to extend the web application, for example to support different authentication providers, you have to extend the web application  *before*  you connect your publishing site to a catalog as described in **Connect a publishing site to a catalog in SharePoint Server**. If you've already connected your publishing site to a catalog, do the following:
    
1. Disconnect the publishing site from the catalog.
    
  
2. Extend the web application for your publishing site.
    
  
3. Repeat the procedure of connecting your publishing site to the catalog.
    
  

# See also

#### 

 **New-SPWebApplicationExtension**
  
    
    
 **Create claims-based web applications in SharePoint Server**
  
    
    

  
    
    

