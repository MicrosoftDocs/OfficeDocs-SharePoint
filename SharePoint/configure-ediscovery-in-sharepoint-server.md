---
title: Configure eDiscovery in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: 5cdce2aa-fa6e-4888-a34f-de61713f5096
---


# Configure eDiscovery in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-18* **Summary:** Learn the steps to set up and configure eDiscovery in SharePoint Server 2013, SharePoint Server 2016, Exchange Server 2016, and Exchange Server 2013.This article identifies the steps that are required to configure eDiscovery in SharePoint Server. When you complete the steps that are listed in this article, users will be able to create and work with eDiscovery cases.Before you configure eDiscovery, you should understand the concepts that are presented in the article  [Overview of eDiscovery and in-place holds in SharePoint Server](html/overview-of-ediscovery-and-in-place-holds-in-sharepoint-server.md).You must perform the following tasks to configure eDiscovery:
- Configure communication between SharePoint Server and Exchange Server 2016.
    
  
- Configure Search to crawl all discoverable content.
    
  
- Grant permissions.
    
  
- Create an eDiscovery Center.
    
  

## Configure communication between SharePoint Server and Exchange Server 2016
<a name="configure_SP_Ex"> </a>

If you will use a SharePoint eDiscovery Center to discover content in Exchange Server, you must configure SharePoint Server and Exchange Server to interact.
> [!IMPORTANT:]

  
    
    

Perform the following steps:
1. Ensure that the Exchange Web Service managed API is installed on every front-end server that is running SharePoint Server. 
    
  
2. Configure a trust relationship between SharePoint Server and Exchange Server. For information about the trust relationship, see  [Plan for server-to-server authentication in SharePoint Server](html/plan-for-server-to-server-authentication-in-sharepoint-server.md).
    
  
3. If you want content from Skype for Business Server to be discoverable, configure the server to archive to Exchange Server 2016. For information about how to configure Skype for Business Server 2015 archiving, see  [Configure Skype for Business Server 2015 to use Exchange Server archiving](https://technet.microsoft.com/en-us/library/jj679896.aspx).
    
  
4. Perform the eDiscovery configuration steps for Exchange. For information about how to configure Exchange Server 2013 for eDiscovery, see  [Integration with SharePoint](https://technet.microsoft.com/en-us/library/dd298021%28v=exchg.160%29.aspx#SP).
    
  

## Configure Search to crawl all discoverable content
<a name="configure-search"> </a>

Content is only discoverable if it is crawled and indexed by the Search service application that is associated with the web application that the eDiscovery Center is in. You should have identified this Search service application when you planned for eDiscovery. To configure the Search service application to crawl the appropriate content, follow these steps:
1. If content in Exchange Server 2013 must be discoverable, add Exchange Server 2013 as a result source. For information about how to configure a result source, see  [Configure result sources for search in SharePoint Server](html/configure-result-sources-for-search-in-sharepoint-server.md).
    
  
2. Ensure that all websites that contain discoverable content are being crawled. For information about how to configure a location to be crawled, see  [Add, edit, or delete a content source in SharePoint Server](html/add-edit-or-delete-a-content-source-in-sharepoint-server.md).
    
  
3. Ensure that all file shares that contain discoverable content are being crawled.
    
  

## Grant permissions
<a name="permissions"> </a>

We recommend that you create a security group to contain all users of the eDiscovery Center. After you create the security group, grant the security group permissions to access all discoverable content.
1. If you will grant permissions at the web application level, create a user policy that gives the security group full read permissions for each web application that contains discoverable content. For information about how to create a policy for a web application, see  [Manage permission policies for a web application in SharePoint Server](html/manage-permission-policies-for-a-web-application-in-sharepoint-server.md).
    
    > [!NOTE:]
      
2. If you will grant permissions at the site collection level, make the security group a site collection administrator for each site collection that contains discoverable content. For information about how to add a site collection administrator, see  [Add, change, or remove a site collection administrator](https://support.office.com/en-US/article/Create-and-manage-SharePoint-groups-B1E3CD23-1A78-4264-9284-87FED7282048).
    
    > [!IMPORTANT:]
      
3. Ensure that the security group has permissions to access all file shares and other websites that contain discoverable content.
    
  
4. If you will use a SharePoint eDiscovery Center to discover content in Exchange Server, grant the security group permissions to access Exchange Server mailboxes. For information about how to grant permissions in Exchange, see  [Integration with SharePoint](https://technet.microsoft.com/en-us/library/dd298021%28v=exchg.160%29.aspx#SP).
    
  
5. Grant the security group permissions to view the crawl log. For information about how to grant permissions to access the crawl log, see **Set-SPEnterpriseSearchCrawlLogReadPermission**.
    
  

## Create an eDiscovery center
<a name="create-eDC"> </a>

An eDiscovery Center is a site collection from which users can create and manage eDiscovery cases. To create an eDiscovery Center, follow the procedure in the article  [Create a site collection in SharePoint Server](html/create-a-site-collection-in-sharepoint-server.md), and choose the **eDiscovery Center** site collection type from the **Enterprise** tab. Be aware that an eDiscovery Center must be in a web application that supports claims authentication.
