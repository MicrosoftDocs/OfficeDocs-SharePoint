---
title: "Create a User Profile service applications in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 8/1/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: 25d888b2-035a-40b4-a2b9-a496657a36e3
description: "Learn how to configure a User Profile service application in SharePoint Server."
---

# Create a User Profile service applications in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
The User Profile service is a shared service in SharePoint Server that provides a central location for configuring and managing [user profiles](user-profile-service-overview.md).
  
This article contains required information and procedures for configuring a User Profile service application.
  
## Before you begin
<a name="begin"> </a>

Before you begin this operation, review the following information about prerequisites:
  
- You have [configure the managed metadata service](../governance/configure-the-managed-metadata-service.md).
    
- A managed path exists. 
    
- An application pool for My Sites exists.
    
- A site collection that uses the My Site Host template exists.
    
## Create a User Profile service application
<a name="createapp"> </a>

You can create a User Profile service application by using either the SharePoint Central Administration website or Microsoft PowerShell. Be sure you're a member of the Farm Administrators group when you perform these procedures.
  
 **To create a User Profile Service application by using Central Administration**
  
1. In Central Administration, in the **Application Management** section, click **Manage service applications**.
    
2. In the **Create** group of the ribbon, click **New**, and then click **User Profile Service Application** in the list of service applications to create. 
    
3. In the **Create New User Profile Service Application** dialog box, in the **Name** section, type a unique name for the User Profile service application. 
    
4. In the **Application Pool** section, select **Use existing application pool** to choose an existing application pool from the list or select **Create a new application pool** to create a new application pool. 
    
5. In the **Application Pool** section, for the **Select a security account for this application pool** option, select **Predefined** to choose an existing predefined security account from the list or select **Configurable** to choose an existing managed account. 
    
6. In the **Profile Database** section, in the **Database Server** box, type the name of the database server where you want to create the profile database. In the **Database Name** box, type the name that you want to use for the profile database. 
    
7. In the **Profile Database** section, for the **Database authentication** option, select **Windows Authentication (recommended)** to use Integrated Windows authentication to connect to the profile database or select **SQL authentication** to enter the credentials that will be used to connect to the profile database. 
    
8. In the **Failover Server** section, in the **Failover Database Server** box, type the name of the database server to be used together with SQL Server database mirroring. 
    
9. In the **Synchronization Database** section, in the **Database Server** box, type the name of the database server where you want to create the synchronization database. In the **Database Name** box, type the name of the synchronization database. 
    
    > [!NOTE]
    > Only ASCII characters are allowed for the synchronization database name. 
  
10. In the **Failover Server** section under **Synchronization Database**, in the **Failover Database Server** box, type the name of the database server to be used together with SQL Server database mirroring. 
    
11. In the **Social Tagging Database** section, in the **Database Server** box, type the name of the database server where the social tagging database will be located. In the **Database Name** box, type the name of the database where social tags will be stored. 
    
12. In the **Social Tagging Database** section, for the **Database authentication** option, select **Windows Authentication (recommended)** to use Integrated Windows authentication to connect to the social tagging database or select **SQL authentication** to type the credentials that will be used to connect to the social tagging database. 
    
13. In the **Failover Server** section, in the **Failover Database Server** box, type the name of the database server that you want to use with SQL Server database mirroring. 
    
14. In the **My Site Host URL** section, type the URL of the site collection where the My Site Host is provisioned. 
    
15. In the **My Site Managed Path** section, type the managed path where you want to create individual My Sites. 
    
    > [!NOTE]
    > Self-service site creation can be enabled for the web application that hosts My Sites. Users must have **Create Personal Site** permissions to create their own My Site. By default, this permission is enabled in SharePoint Server for all authenticated users. Ensure that you want the default setting to apply to the organization. Or, you can use one or more security groups to grant the **Create Personal Site** permission to a subset of users in an organization. 
  
16. In the **Site Naming Format**section, select one of the following formats for naming new personal sites:
    
  - **User name (do not resolve conflicts)**
    
  - **User name (resolve conflicts by using domain_user name)**
    
  - **Domain and user name (will not have conflicts)**
    
17. In the **Default Proxy Group** section, select whether you want the proxy of this User Profile service application to be a part of the default proxy group on this farm. 
    
18. In the **Yammer Integration** section, select whether you want to use Yammer for social collaboration. 
    
19. Click **Create**.
    
## See also
<a name="createapp"> </a>

#### Concepts

[Administer the User Profile service in SharePoint Server](../administration/user-profile-service-administration.md)
  
[User Profile service overview](user-profile-service-overview.md)

