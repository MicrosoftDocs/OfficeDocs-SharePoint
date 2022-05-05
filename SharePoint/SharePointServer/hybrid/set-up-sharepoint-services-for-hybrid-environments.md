---
title: "Set up SharePoint services for hybrid environments"
ms.reviewer: 
ms.author: serdars
author: SerdarSoysal
manager: serdars
ms.date: 6/21/2017
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: how-to
ms.prod: sharepoint-server-itpro
ms.localizationpriority: medium
ms.collection:
- Ent_O365_Hybrid
- IT_SharePoint_Hybrid_Top
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
- Strat_SP_gtc
- M365-collaboration
- SPO_Content
ms.custom: 
ms.assetid: 70e043ef-8908-436e-92bf-abbcd89874f7
description: "Learn how to set up the SharePoint Server services you'll need for a hybrid environment."
---

# Set up SharePoint Server services for hybrid environments

[!INCLUDE[appliesto-2013-2016-2019-SUB-SPO-md](../includes/appliesto-2013-2016-2019-SUB-SPO-md.md)] 
  
 **This article is part of a roadmap of procedures for configuring SharePoint hybrid solutions. Be sure you're [following a roadmap](configuration-roadmaps.md) when you do the procedures in this article.**
  
## Set up SharePoint Server services for hybrid

SharePoint Server services such as My Sites, User Profiles, and Managed Metadata can be challenging to deploy and can require a lot of planning. If you plan to make use of these services in depth, we highly recommend that you follow the detailed planning information for [My Sites](../install/my-sites-planning.md), [User Profiles](../administration/user-profiles-and-identities.md), and [Managed Metadata](../governance/managed-metadata-planning.md).
  
However, SharePoint Server hybrid scenarios, such as hybrid Search require several services to be running in SharePoint Server, but they do not require them to be extensively configured. In this article, we're going to look at the easy path to getting these services running on your farm for use in a hybrid configuration. You can do more extensive configuration of these services later if you want to use more of the available features.
  
Note that if you're using SharePoint Server 2013, you need to turn on some services manually. (We call this out in the appropriate procedures later in the article.) If you're using SharePoint Server 2016, these services are handled automatically by MinRole. 
  
## Services for hybrid deployments in SharePoint Server

SharePoint Server hybrid configurations all require the following services to be running on your farm:
  
- Managed Metadata service application
    
- User Profile Service application
    
- My Sites 
    
If you're setting up OneDrive, these are the only services you need. If you're setting up a hybrid Search or hybrid sites features, there are some additional requirements that we'll cover in the next section.
  
If you've already configured these services, there's no need to add additional instances of them for hybrid, but be sure to see [Configure hybrid specific settings](set-up-sharepoint-services-for-hybrid-environments.md#HybridSettings) for important configuration information for the User Profile Service for SharePoint and BCS hybrid deployments. 
  
Let's look at how to set up each.
  
 **Managed Metadata service**
  
 **To turn on the Managed Metadata Web Service (SharePoint Server 2013 only)**
  
1. In Central Administration, under **System Settings**, select **Manage services on server**.
    
2. On the server dropdown, select **Change Server**.
    
3. Select the server where you want to run the Managed Metadata Web Service.
    
4. In the **Service** list, select **Start** for the **Managed Metadata Web Service**.
    
You need to create a Managed Metadata service application.
  
 **To create a Managed Metadata service application**
  
1. In Central Administration, under **Application Management**, select **Manage service applications**.
    
2. Select **New**, and then select **Managed Metadata Service**.
    
3. In the **Name** box, enter a name for the service application. 
    
4. In the **Database Name** box, enter a name for the database. 
    
5. Under **Application Pool**, from the **Use existing application pool list**, select **SharePoint Web Services Default**.
    
6. Select **OK**.
    
That's all the configuration that you need to do for the Managed Metadata service if you're configuring a hybrid scenario. If you want to make further use of the Managed Metadata service, see [Plan for managed metadata in SharePoint Server](../governance/managed-metadata-planning.md).
  
 **My Sites**
  
The first thing we need to do is to create a web application for the My Sites site. We recommend that My Sites be in a separate web application, although the web application can be in an application pool that is shared with other collaboration sites, or it can be in a separate application pool but in a shared IIS website.
  
The default settings for this web application will work fine for a hybrid environment, or you can customize any that you need to for your organization.
  
 **To create a web application**
  
1. In Central Administration, in the **Application Management** section, select **Manage web applications**.
    
2. On the ribbon, select **New**.
    
3. On the **Create New Web Application** page, in the **Authentication** section, select the authentication mode that will be used for this web application. 
    
4. In the **IIS Web Site** section, you can configure the settings for your new web application by selecting one of the following two options: 
    
  - Select **Use an existing web site**, and then select the website on which to install your new web application.
    
  - Select **Create a new IIS web site**, and then enter the name of the website in the **Name** box. 
    
    You can also provide the port number, host header, or path for the new IIS website.
    
5. In the **Security Configuration** section, select an authentication provider, whether to allow anonymous access, and whether to use Secure Sockets Layer (SSL). 
    
6. In the **Application Pool** section, do one of the following: 
    
  - If you want to use an existing application pool, select **Use existing application pool**, and then select the application pool from the dropdown.
    
  - If you want to create a new application pool, select **Create a new application pool**, enter the name of the application pool, and either select the account that the application pool will run under or create a new managed account for the application pool to run under.
    
7. In the **Database Name and Authentication** section, select the database server, database name, and authentication method for your new web application. 
    
8. If you use database mirroring, in the **Failover Server** section, in the **Failover Database Server** box, enter the name of a specific failover database server that you want to associate with a content database. 
    
9. In the **Service Application Connections** section, select the service application connections that will be available to the web application. 
    
10. In the **Customer Experience Improvement Program** section, select **Yes** or **No**.
    
11. Select **OK** to create the new web application. 
    
12. When the **Application Created** page appears, select **OK**.
    
Next, we need to create the site collection that will host users' My Sites.
  
 **To create a My Site Host site collection**
  
1. On Central Administration, in the **Application Management** section, select **Create site collections**. 
    
2. On the **Create Site Collection** page, in the **Web Application** section, select the web application that you just created for My Sites. 
    
3. In the **Title and Description** section, enter the title and description for the site collection. 
    
4. In the **Web Site Address** section, select the path of the URL for the My Site host. In most cases, you can use the root directory (/). 
    
5. In the **Template Selection** section, select the **Enterprise** tab, and then select **My Site Host**.
    
6. In the **Primary Site Collection Administrator** section, enter the user name (in the form  _\<DOMAIN\>_\ _\<user name\>_) for the user who will be the site collection administrator.
    
7. In the **Secondary Site Collection Administrator** section, enter the user name for the secondary administrator of the site collection. 
    
8. If you are using quotas to manage storage for site collections, in the **Quota Template** section, select a template in the **Select a quota template** list. 
    
9. Select **OK**.
    
The **Top-Level Site Successfully Created** page will appear when the My Site Host site collection is created. Although you can select the link to browse to the root of the site collection, doing this results in an error because the user profile cannot be loaded. This behavior is to be expected; user profiles are not imported at this point. 
  
 **User Profile Service**
  
If you're running SharePoint Server 2013, then you need to turn on the User Profile Service on at least one server in your farm.
  
 **To turn on the User Profile Service (SharePoint Server 2013 only)**
  
1. In Central Administration, under **System Settings**, select **Manage services on server**.
    
2. On the Server dropdown, select **Change Server**.
    
3. Select the server where you want to run the User Profile Service.
    
4. In the **Service** list, select **Start** for the **User Profile Service**.
    
    > [!NOTE]
    > Do not turn on the User Profile Synchronization Service. We'll do that later after we've configured the User Profile service application. 
  
Next, let's create a User Profile service application.
  
 **To create a User Profile service application**
  
1. In Central Administration, under **Application Management**, select **Manage service applications**.
    
2. Select **New**, and then select **User Profile Service Application**.
    
3. Enter a name for the service application in the **Name** box. 
    
4. Under **Application Pool**, select **SharePoint Web Services Default** from the **Use existing application pool list**.
    
5. In the **My Site Host URL** box, enter the URL of the My Site Host that you created. 
    
6. Optionally change other settings to meet the needs of your organization. The default settings work fine for hybrid environments.
    
7. Select **OK**.
    
If you're using SharePoint Server 2013, the next step is to turn on the User Profile Synchronization Service. Be sure that you turn it on on the server that you specified as the Profile Synchronization Instance when you created the service application.
  
 **To turn on the User Profile Synchronization Service (SharePoint Server 2013 only)**
  
1. In Central Administration, under **System Settings**, select **Manage services on server**.
    
2. On the Server dropdown, select **Change Server**.
    
3. Select the server that you specified as the Profile Synchronization Instance.
    
4. In the **Service** list, select **Start** for the **User Profile Synchronization Service**.
    
5. Enter the credentials for the account shown, and select **OK**.
    
    > [!NOTE]
    > This service can take several minutes or longer to start. Refresh the page occasionally until you see a status of **Started**. 
  
Next, we'll configure the App Management Service.
  
 **App Management Service**
  
If you're using SharePoint Server 2013, you need to turn on the App Management Service on at least one server in your farm.
  
 **To turn on the App Management Service (SharePoint Server 2013 only)**
  
1. In Central Administration, under **System Settings**, select **Manage services on server**.
    
2. On the Server dropdown, select **Change Server**.
    
3. Select the server where you want to run the Managed Metadata Web Service.
    
4. In the **Service** list, select **Start** for the **App Management Service**.
    
You need to create an App Management service application.
  
 **To create a App Management service application**
  
1. In Central Administration, under **Application Management**, select **Manage service applications**.
    
2. Select **New**, and then select **App Management Service**.
    
3. In the **Service Application Name** box, enter a name for the service application. 
    
4. Under **Application Pool**, from the **Use existing application pool list**, select **SharePoint Web Services Default**.
    
5. Select **OK**.
    
### Configure hybrid specific settings
<a name="HybridSettings"> </a>

Hybrid uses the Microsoft SharePoint in Microsoft 365 Foundation Subscription Settings Service which is turned off by default in SharePoint Server. Use the following procedure to turn it on.
  
 **To turn on the Microsoft SharePoint Foundation Subscription Settings Service (SharePoint Server 2013)**
  
1. In Central Administration, under **System Settings**, select **Manage services on server**.
    
2. For the **Microsoft SharePoint Foundation Subscription Settings Service**, select **Start**.

 **To turn on the Microsoft SharePoint Foundation Subscription Settings Service** (SharePoint Server 2016 and SharePoint 2019)
  
1. In Central Administration, under **System Settings**, select **Manage services in this farm**.
    
2. For the **Microsoft SharePoint Foundation Subscription Settings Service**, select **Enable Auto Provision**

You must also have a Subscription Settings service application and proxy. These must be created by using Microsoft PowerShell. Use the example script provided at [New-SPSubscriptionSettingsServiceApplication](/powershell/module/sharepoint-server/New-SPSubscriptionSettingsServiceApplication).
  
 **Active Directory Domain Services synchronization connection**
  
 For hybrid, we need a synchronization connection with Active Directory Domain Services for the User Profile service. If you haven't already configured one, use the following procedure to do so. 
  
 **To configure a synchronization connection**
  
1. In Central Administration, under **Application Management**, select **Manage service applications**.
    
2. Select the User Profile service application.
    
3. Select **Configure Synchronization Connections**.
    
4. Select **Create New Connection**.
    
5. In the **Connection Name** box, enter a name for the connection. 
    
6. In the **Forest name** box, enter the name of your domain, for example, contoso.com. 
    
7. Enter the user name and password of your domain administrator.
    
8. Select **Populate Containers**.
    
9. Expand the domain node, and select the check box for the object where your users are located.
    
10. Select **OK**.
    
Next, we'll verify some user properties in the User Profile Service.
  
The **Work email** user property needs to contain the email address that you configured for each user in Active Directory Directory Services. Also, the **User Principal Name** property must be mapped to the **userPrincipalName** attribute. Use the following procedure to verify both of these mappings. 
  
 **To verify user profile properties**
  
1. In Central Administration, under **Application Management**, select **Manage service applications**.
    
2. Select the User Profile service application.
    
3. Select **Manage User Properties**.
    
4. In the **Property Name** column, confirm that **User Principal Name** is mapped to **userPrincipalName** in the **Mapped Attribute** column. 
    
5. In the **Property Name** column, confirm that **Work email** is mapped to **mail** in the **Mapped Attribute** column. 
    
If either of these properties is not mapped as described, you need to [update the mapping](../administration/add-edit-or-delete-custom-properties-for-a-user-profile.md).
  
 **Synchronize user profiles**
  
After you verify the user property mappings, we need to synchronize the UPN domain suffix and email address that we configured in Active Directory Domain Services. To do this, you have to start a profile synchronization. 
  
 **To start profile synchronization manually**
  
1. On the SharePoint in Microsoft 365 Central Administration website, in the **Application Management** section, select **Manage service applications**.
    
2. Select the User Profile service application.
    
3. On the **Manage Profile Service** page, in the **Synchronization** section, select **Start Profile Synchronization**.
    
4. On the **Start Profile Synchronization** page, select **Start Incremental Synchronization** to synchronize the profiles that you have updated. 
    
5. Select **OK**.
    
    > [!NOTE]
    > Refresh the **Manage Profile Service** page to view the profile synchronization status. 
  
That's all the configuration that you need to do for the App Management Service. Next, move on to the next step in your [roadmap](configuration-roadmaps.md).
  

