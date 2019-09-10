---
title: "Configure eDiscovery in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 5cdce2aa-fa6e-4888-a34f-de61713f5096
description: "Learn the steps to set up and configure eDiscovery in SharePoint Server and Exchange Server."
---

# Configure eDiscovery in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
This article identifies the steps that are required to configure eDiscovery in SharePoint Server. When you complete the steps that are listed in this article, users will be able to create and work with eDiscovery cases.
  
Before you configure eDiscovery, you should understand the concepts that are presented in the article [eDiscovery and in-place holds in SharePoint Server](ediscovery-and-in-place-holds-in-sharepoint-server.md).
  
You must perform the following tasks to configure eDiscovery:
  
- Configure communication between SharePoint Server and Exchange Server 2016.
    
- Configure Search to crawl all discoverable content.
    
- Grant permissions.
    
- Create an eDiscovery Center.
    
## Configure communication between SharePoint Server and Exchange Servers 2019 and 2016
<a name="configure_SP_Ex"> </a>

If you will use a SharePoint eDiscovery Center to discover content in Exchange Server, you must configure SharePoint Server and Exchange Server to interact.
  
> [!IMPORTANT]
> To discover content in Exchange Server from a SharePoint eDiscovery Center, you must be running Exchange Server versions 2019, 2016, or 2013. 
  
  
Perform the following steps:
  
1. Ensure that the Exchange Web Service managed API is installed on every front-end server that is running SharePoint Server. 
    
2. Configure a trust relationship between SharePoint Server and Exchange Server. For information about the trust relationship, see [Plan for server-to-server authentication in SharePoint Server](../security-for-sharepoint-server/plan-server-to-server-authentication.md).
    
3. If you want content from Skype for Business Server to be discoverable, configure the server to archive to Exchange Server 2016. For information about how to configure Skype for Business Server 2015 archiving, see [Configure Skype for Business Server 2015 to use Exchange Server archiving](/skypeforbusiness/deploy/integrate-with-exchange-server/use-exchange-archiving).

4. If you want SharePoint Server 2019 users to link to and share documents that are stored in OneDrive for Business instead of attaching file to Outlook messages, see the [Document collaboration](/Exchange/new-features/new-features?view=exchserver-2019#document-collaboration) section in **What's new in Exchange Server**.
    
5. Perform the eDiscovery configuration steps for Exchange. For information about how to configure Exchange Server 2013 for eDiscovery, see [Integration with SharePoint](https://go.microsoft.com/fwlink/?linkid=857898).
    
## Configure Search to crawl all discoverable content
<a name="configure-search"> </a>

Content is only discoverable if it is crawled and indexed by the Search service application that is associated with the web application that the eDiscovery Center is in. You should have identified this Search service application when you planned for eDiscovery. To configure the Search service application to crawl the appropriate content, follow these steps:
  
1. If content in Exchange Server 2013 must be discoverable, add Exchange Server 2013 as a result source. For information about how to configure a result source, see [Configure result sources for search in SharePoint Server](../search/configure-result-sources-for-search.md).
    
2. Ensure that all websites that contain discoverable content are being crawled. For information about how to configure a location to be crawled, see [Add, edit, or delete a content source in SharePoint Server](../search/add-edit-or-delete-a-content-source.md).
    
3. Ensure that all file shares that contain discoverable content are being crawled.
    
## Grant permissions
<a name="permissions"> </a>

We recommend that you create a security group to contain all users of the eDiscovery Center. After you create the security group, grant the security group permissions to access all discoverable content.
  
1. If you will grant permissions at the web application level, create a user policy that gives the security group full read permissions for each web application that contains discoverable content. For information about how to create a policy for a web application, see [Manage permission policies for a web application in SharePoint Server](../administration/manage-permission-policies-for-a-web-application.md).
    
    > [!NOTE]
    > When you change permissions at the web application level, Search re-crawls all of the content in the web application. 
  
2. If you will grant permissions at the site collection level, make the security group a site collection administrator for each site collection that contains discoverable content. For information about how to add a site collection administrator, see [Add, change, or remove a site collection administrator](/sharepoint/customize-sharepoint-site-permissions).
    
    > [!IMPORTANT]
    > A site collection administrator must add the security group as an additional site collection administrator by using the **Site Settings** menu. You cannot use Central Administration to make a security group a site collection administrator 
  
3. Ensure that the security group has permissions to access all file shares and other websites that contain discoverable content.
    
4. If you will use a SharePoint eDiscovery Center to discover content in Exchange Server, grant the security group permissions to access Exchange Server mailboxes. For information about how to grant permissions in Exchange, see [Integration with SharePoint](https://go.microsoft.com/fwlink/?linkid=857898).
    
5. Grant the security group permissions to view the crawl log. For information about how to grant permissions to access the crawl log, see [Set-SPEnterpriseSearchCrawlLogReadPermission](/powershell/module/sharepoint-server/Set-SPEnterpriseSearchCrawlLogReadPermission?view=sharepoint-ps).
    
## Create an eDiscovery center
<a name="create-eDC"> </a>

An eDiscovery Center is a site collection from which users can create and manage eDiscovery cases. To create an eDiscovery Center, follow the procedure in the article [Create a site collection in SharePoint Server](../sites/create-a-site-collection.md), and choose the **eDiscovery Center** site collection type from the **Enterprise** tab. Be aware that an eDiscovery Center must be in a web application that supports claims authentication. 
  
## See also
<a name="configure"> </a>

#### Concepts

[eDiscovery and in-place holds in SharePoint Server](ediscovery-and-in-place-holds-in-sharepoint-server.md)
  
[Configure eDiscovery in SharePoint Server](configure-ediscovery-0.md)

[Search and place a hold on public folders using In-Place eDicovery](/Exchange/policy-and-compliance/ediscovery/search-public-folders?view=exchserver-2019)

[Assign eDiscovery permissions in Exchange Server](/Exchange/policy-and-compliance/ediscovery/assign-permissions?view=exchserver-2019)
