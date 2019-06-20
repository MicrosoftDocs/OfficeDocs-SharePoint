---
title: "Set up OneDrive for Business in a SharePoint Server on-premises environment"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 3/1/2018
audience: ITPro
ms.topic: get-started-article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_OneDriveAdmin
- IT_OneDriveAdmin_Top
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 42e7a722-1e13-4f48-b866-2548cff05225
description: "Learn the steps needed to set up OneDrive for Business in a SharePoint Server on-premises environment."
---

# Set up OneDrive for Business in a SharePoint Server on-premises environment

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
> [!NOTE]
> This article describes how to set up OneDrive for Business in a SharePoint Server on-premises environment, and does not describe OneDrive for Business in an Office 365 environment. For more information about administering OneDrive for Business in Office 365, see [OneDrive for Business admin help](https://go.microsoft.com/fwlink/p/?LinkId=824831). 
  
When setting up OneDrive for Business in your SharePoint Server on-premises environment, an IT-administrator will need to go through the following steps: 
  
- [Set up the required services ](set-up-onedrive-for-business.md#setup)
    
- [Enable the Recently Shared Items (RSI) cache to quickly populate the Shared with Me view](set-up-onedrive-for-business.md#EnableRSIcache)
    
- [Verify that OneDrive for Business is available to your users](set-up-onedrive-for-business.md#verify)
    
Before proceeding with setup, please review planning considerations you might need to address that are described in [Plan for OneDrive for Business in SharePoint Server](onedrive-for-business-planning.md).
  
## Set up the required services
<a name="setup"> </a>

Setting up OneDrive for Business in a SharePoint Server on-premises environment requires the following services to be running on your farm:
  
- Managed Metadata service application
    
- My Sites 
    
- User Profile service application
    
Let's look at how to set up each.
  
> [!NOTE]
> The following provides basic steps to configure the Managed Metadata and Users Profile service applications to provide OneDrive for Business functionality in SharePoint Server. Careful planning is required for both services if you intend to use them for additional functionality in SharePoint Server. For more information, about managed metadata, see [Plan for managed metadata in SharePoint Server](../governance/managed-metadata-planning.md). 
  
### Managed Metadata service

First, let's create a Managed Metadata service application.
  
 **To create a Managed Metadata service application**
  
1. In Central Administration, under **Application Management**, click **Manage service applications**.
    
2. Click **New**, and then click **Managed Metadata Service**.
    
3. Type a name for the service application in the **Name** box. 
    
4. In the **Database Name** box, type a name for the database. 
    
5. Under **Application Pool**, choose **SharePoint Web Services Default** from the **Use existing application pool list**.
    
6. Click **OK**.
    
### My Sites

The first thing we need to do is to create a web application for the My Sites site. We recommend that My Sites be in a separate web application, although the web application can be in an application pool that is shared with other collaboration sites, or it can be in a separate application pool but in a shared IIS website.
  
 **To create a web application**
  
1. In Central Administration, in the **Application Management** section, click **Manage web applications**.
    
2. On the ribbon, click **New**.
    
3. On the **Create New Web Application** page, in the **Authentication** section, select the authentication mode that will be used for this web application. 
    
4. In the **IIS Web Site** section, you can configure the settings for your new web application by selecting one of the following two options: 
    
  - Click **Use an existing web site**, and then select the website on which to install your new web application.
    
  - Click **Create a new IIS web site**, and then type the name of the website in the **Name** box. 
    
    You can also provide the port number, host header, or path for the new IIS website.
    
5. In the **Security Configuration** section, select an authentication provider, whether to allow anonymous access, and whether to use Secure Sockets Layer (SSL). 
    
6. In the **Application Pool** section, do one of the following: 
    
  - If you want to use an existing application pool, click **Use existing application pool**, and then select the application pool from the drop-down menu.
    
  - If you want to create a new application pool, click **Create a new application pool**, type the name of the application pool, and either select the account that the application pool will run under or create a new managed account for the application pool to run under.
    
7. In the **Database Name and Authentication** section, select the database server, database name, and authentication method for your new web application. 
    
8. If you use database mirroring, in the **Failover Server** section, in the **Failover Database Server** box, type the name of a specific failover database server that you want to associate with a content database. 
    
9. In the **Service Application Connections** section, select the service application connections that will be available to the web application. 
    
10. In the **Customer Experience Improvement Program** section, click **Yes** or **No**.
    
11. Click **OK** to create the new web application. 
    
12. When the **Application Created** page appears, click **OK**.
    
Next, we need to create the site collection that will host users' My Sites.
  
 **To create a My Site Host site collection**
  
1. On Central Administration, in the **Application Management** section, click **Create site collections**. 
    
2. On the **Create Site Collection** page, in the **Web Application** section, select the web application that you just created for My Sites. 
    
3. In the **Title and Description** section, type the title and description for the site collection. 
    
4. In the **Web Site Address** section, select the path of the URL for the My Site host. In most cases, you can use the root directory (/). 
    
5. In the **Template Selection** section, click the **Enterprise** tab, and then select **My Site Host**.
    
6. In the **Primary Site Collection Administrator** section, type the user name (in the form  _\<DOMAIN\>_\ _\<user name\>_) for the user who will be the site collection administrator.
    
7. In the **Secondary Site Collection Administrator** section, type the user name for the secondary administrator of the site collection. 
    
8. If you are using quotas to manage storage for site collections, in the **Quota Template** section, click a template in the **Select a quota template** list. 
    
9. Click **OK**.
    
The **Top-Level Site Successfully Created** page will appear when the My Site Host site collection is created. Although you can click the link to browse to the root of the site collection, doing this results in an error because the user profile cannot be loaded. This behavior is to be expected; user profiles are not imported at this point. 
  
### User Profile service

Next, let's create a User Profile service application.
  
 **To create a User Profile service application**
  
1. In Central Administration, under **Application Management**, click **Manage service applications**.
    
2. Click **New**, and then click **User Profile Service Application**.
    
3. Type a name for the service application in the **Name** box. 
    
4. Under **Application Pool**, choose **SharePoint Web Services Default** from the **Use existing application pool list**.
    
5. In the **My Site Host URL** box, type the URL of the My Site Host that you created. 
    
6. Optionally change other settings to meet the needs of your organization. The default settings work fine for hybrid environments.
    
7. Click **OK**.
    
## Enable the Recently Shared Items (RSI) cache to quickly populate the Shared with Me view
<a name="EnableRSIcache"> </a>

This step allows your users to immediately view files that are shared explicitly with them in their OneDrive for Business Shared with Me View.
  
The Shared with Me view in OneDrive for Business lets users to see which documents and folders that users have shared directly with them. By default, the Shared with Me view is populated once a shared item is crawled and re-indexed through search. This means that your crawling/indexing schedule may cause some latency between the when the item was shared and when the it appears in the user's Shared with Me View.
  
Your users will still be able to open the shared items or folder if they are sent a link (for example, through an email notification), they just won't be able to see the items listed in the Shared with me View until the items have been crawled and indexed. For more information about how files are shared in OneDrive for Business, see [Share OneDrive files and folders](https://support.office.com/article/9fcc2f7d-de0c-4cec-93b0-a82024800c07).
  
To eliminate this latency in your SharePoint Server environment, your IT administrator can enable the Recently Shared Items (RSI) cache. The RSI cache is provisioned on the My Site host and it is used to populate the Shared with Me view until the file permission changes resulting from the sharing action are crawled. The RSI cache is disabled by default in SharePoint Server.
  
RSI doesn't support a multi-farm scenario where the My Site Host is not on the content farm. This site collection typically has a URL such as http://\<hostname\>/my. If the My Site Host is not on the content farm, sharing will be broken.
  
> [!IMPORTANT]
> The RSI list contains information identifying the sharing action, including the name of the shared file and who it was shared with. If you choose to enable RSI, this information will be viewable by the My Site Host admin and those to whom My Site Host access has been delegated. 
  
To enable the RSI list in the My Site Host, run the following PowerShell command:
  
```
$msh = Get-SPSite | where {$_.RootWeb.WebTemplateId -eq 54}
Enable-SPFeature "RecentlySharedItems" -Url $msh.Url
```

If you need to disable the RSI list in the My Site Host, run the following PowerShell command:
  
```
$msh = Get-SPSite | where {$_.RootWeb.WebTemplateId -eq 54}
Disable-SPFeature "RecentlySharedItems" -Url $msh.Url

```

## Verify that OneDrive for Business is available to your users
<a name="verify"> </a>

Use the following procedure to check if OneDrive for Business is available to your users.
  
1. Have a user open a SharePoint Server site (for example, their own My Site: http://\<hostname\>/my).
    
2. In the top left corner of the page, click on the app launcher, which will display the OneDrive tile.
    
3. Click on the OneDrive tile, which should display your OneDrive for Business documents page.
    
![OneDrive for Business tile in SharePoint Server 2016](../media/d38459ac-be0d-4823-b504-fddc8aadc0f3.jpg)
  
## See Also
<a name="also"> </a>

[Create a User Profile service applications in SharePoint Server](../install/create-a-user-profile-service-application.md)
