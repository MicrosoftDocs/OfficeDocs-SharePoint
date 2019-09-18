---
title: "Update a web application URL and IIS bindings for SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 8/10/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 41d83364-afc7-4b3c-81f2-faef0f140f89
description: "Learn how to update a web application and IIS bindings for SharePoint Server."
---

# Update a web application URL and IIS bindings for SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
After you have extended a web application into a zone with a set of Internet Information Services (IIS) bindings and alternate access mapping URLs, you might decide that you want to use a different URL to reach the web application. For example, you might have originally created a web application to use HTTP and later decide to use SSL instead. Or, you might create a web application to use the www.contoso1.com host header and then decide to use the www.contoso2.com host header instead. This article provides detailed guidance for changing the URL and IIS bindings of a web application.
  
> [!NOTE]
> This article focuses on changing the existing URL and IIS bindings of a web application. If you want to add additional URLs and IIS bindings to a web application, you can do so by extending the web application into an unused zone. 
    
## About updating a web application URL and IIS bindings
<a name="section1"> </a>

Unlike typical IIS applications, you cannot simply use IIS Manager or other IIS metabase tools to modify the bindings of IIS web applications that have been extended with SharePoint Server. 
  
If you modify the IIS bindings of a web application by adding a host header binding or SSL port or by changing a port number, SharePoint Server will not be aware of these changes and will not update the web application's alternate access mapping URLs. If you update the web application's alternate access mappings to change a host header, switch to an SSL URL, or change a port number, SharePoint Server will not automatically update your IIS bindings to match.
  
To update the URL or IIS bindings of a web application, unextend and reextend the web application and reconfigure the alternate access mapping URLs or IIS website bindings.
  
We do not recommend reusing the same IIS website for your HTTP and SSL hosting. Instead, extend a dedicated HTTP and a dedicated SSL website, with each assigned to its own alternate access mapping zone and URLs.
  
For more information about alternate access mappings, see [Plan alternate access mappings for SharePoint 2013](plan-alternate-access-mappings.md).
  
Alternate access mapping collections correspond to the following authentication zones:
  
- Default
    
- Intranet
    
- Internet
    
- Custom
    
- Extranet
    
## Unextending and reextending a web application
<a name="section2"> </a>

If you need to change your IIS bindings, unextend the web application from the zone that the web application has been extended into (without deleting the web application), and then reextend the web application into the same zone. Consider trying these migration procedures in a test environment before deploying them in a production environment.
  
Unextend the web application from the zone by using the **Remove SharePoint from IIS Web site** link on the **Central Administration Application Management** page, as described in the following procedure. 
  
 **To unextend a web application**
  
1. On the SharePoint Central Administration website, on the **Application Management** page, in the **Web Applications** section, click **Manage web applications**.
    
2. On the **Web Applications** menu, click the web application you want to unextend, click **Delete**, and then click **Remove SharePoint from IIS Web Site**.
    
3. On the **Remove SharePoint From Web Site** page, click the web application you want to unextend. 
    
4. In the **Select IIS Web site and zone to remove** list, click the IIS website and zone you want to remove. Because a web application can be extended in up to five zones, make sure you select the correct IIS website and zone. 
    
5. In the **Delete IIS Web sites** section, click **Yes** if the IIS website is hosting only SharePoint Products and Technologies content. If the IIS web site is hosting other content, you might not want to delete the web site. In that case, click **No**.
    
6. Click **OK**. This action does not delete the web application, nor does it delete the content databases of the web application.
    
After you have unextended the web application, you can reextend the web application to the same zone by using your updated bindings.
  
 **To reextend a web application**
  
1. On the SharePoint Central Administration website, on the **Application Management** page, in the **Web Applications** section, click **Manage web applications**.
    
2. Click the web application you want to extend. On the ribbon, click **Extend**. 
    
3. In the **IIS Web Site** section, if you have already created an IIS website with the appropriate bindings for SharePoint Server to use, click the **Use an existing IIS Web site** option and select the IIS website from the list. Otherwise, click the **Create a new IIS Web site** option. 
    
4. In the **Port**, **Host Header**, and **Use Secure Sockets Layer (SSL)** fields, type the IIS bindings you want to use. 
    
5. In the **Load Balanced URL** section, in the **URL** field, type the URL that users will use to locate this web application. If you are using a load balancer or reverse proxy, this is the URL of the load balancer or reverse proxy. 
    
6. In the **Load Balanced URL** section, in the **Zone** list, click the zone that you previously selected. 
    
7. Click **OK**.
    
## Additional steps for updating a web application URL and IIS bindings
<a name="section3"> </a>

To complete the process of updating a web application URL or IIS bindings, perform the additional steps listed in this section after you have reextended the web application into the same zone.
  
### Update the alternate access mapping URLs for the zone

If you are using a load balancer or a reverse proxy, make sure that your internal URLs are updated in the alternate access mappings to reflect the new IIS bindings. In addition, update your load balancer rules or your reverse proxy rules to align with the new IIS bindings.
  
### Apply an SSL certificate

If the new IIS bindings use SSL, apply an SSL certificate to the new IIS website assigned to your zone. See [How to Set Up SSL on IIS 7)](https://docs.microsoft.com/iis/manage/configuring-security/how-to-set-up-ssl-on-iis) for more on configuring SSL.
  
### Apply an authentication method

When you reextend your web application, the default SharePoint Server authentication method for the zone is Integrated Windows authentication. If you want to use an authentication method other than Integrated Windows, explicitly apply the authentication method you want to use. For more information about authentication methods, see [Plan for user authentication methods in SharePoint Server](/SharePoint/security-for-sharepoint-server/plan-user-authentication).
  
For more information about how to configure authentication for SharePoint Server 2016, see [Configure authentication infrastructure in SharePoint Server](/sharepoint/security-for-sharepoint-server/security-for-sharepoint-server).
  
### Verify the Search start addresses and My Site settings

Verify that the SharePoint Server Search start addresses are correct for your content sources. If the SharePoint Server Search start addresses are incorrect, update them. Also, verify that your My Site settings, including Personal Search Center, Personal Site Provider, and default RSS feed, are correct. If your My Site settings are incorrect, update them. For more information about how to configure My Site settings, see [Configure My Sites in SharePoint Server](/SharePoint/install/configure-my-sites).
  
For more information about Search start addresses, see [Plan crawling and federation in SharePoint Server](/SharePoint/search/plan-crawling-and-federation).
  
### Verify the trusted file locations

If Excel Services in SharePoint Server 2013 is part of your deployment, verify that your trusted file locations are configured correctly. If your trusted file locations are configured incorrectly, update them. For more information about trusted file locations, see [Configure Excel Services in SharePoint Server 2013](/SharePoint/administration/configure-excel-services).
  
> [!NOTE]
> Excel Services in SharePoint Server 2013 is only available in SharePoint Server 2013. 
  
### Redeploy solutions

When you remove SharePoint Server from an IIS website, if you are removing the last (or only) website that is associated with the web application, any web application solutions you have deployed will also be removed. If you need these solutions, redeploy them. For additional information about how to manage solutions, see [Install and manage solutions for SharePoint Server](/SharePoint/administration/configure-excel-services)
  

