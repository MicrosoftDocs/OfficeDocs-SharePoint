---
title: "Create and configure a Search service application in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 3/8/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 3fa7973f-2c1a-4be0-b903-3f1e6bdcf1d8
description: "Learn how to create and configure a SharePoint Search service application so that you can crawl content and provide search results to users."
---

# Create and configure a Search service application in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
## Before you begin
<a name="begin"> </a>

If you used the Farm Configuration Wizard after you installed SharePoint Server 2016 or SharePoint Server 2019, a Search service application might have been created at that time. To verify whether a Search service application exists, you can click **Manage service applications** in the **Application Management** section on the Central Administration home page. For the remainder of this article, it is assumed that a Search service application does not exist yet, and that therefore you must create one. 
  
    
## How to create and configure a SharePoint Search service application
<a name="begin"> </a>

When you deploy and configure a Search service application, you perform the following main tasks:
  
1. **Create accounts** — Certain domain user accounts are required specifically for a Search service application. 
    
2. **Create a Search service application** — A Search service application provides enterprise search features and functionality. 
    
3. **Configure the Search service application** — Basic configuration of a Search service application includes configuring a default content access account, an email contact, and content sources. 
    
4. **Configure the Search service application topology** — You can deploy search components on different servers in the farm. You can also specify which instance of SQL Server is used to host the search-related databases. 
    
## Step 1: Create accounts that are required for a SharePoint Search service application
<a name="begin"> </a>

The following table lists the accounts that are required when a Search service application is created.
  
|                                               **Account**                                                |                                          **Description**                                           |                                                                                                           **Notes**                                                                                                            |
| :------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Search service                                                                                           | Windows user credentials for the SharePoint Server Search service, which is a Windows service      | This setting applies to all Search service applications in the farm. You can change this account at any time by clicking **Configure service accounts** in the **Security** section on the Central Administration home page.   |
| Search Admin Web Service application pool  <br/><br/>  Search Query and Site Settings Web Service application pool | Windows user credentials                                                                           | For each of these accounts, you can use the same credentials that you specified for the Search service. Or, you can assign different credentials to each account according to the principle of least-privilege administration. |
| Default content access                                                                                   | Windows user credentials for the Search service application to use to access content when crawling | We recommend that you specify a separate account for the default content access account according to the principle of least-privilege administration.                                                                          |
   
The accounts that you use for the Search service, the Search Admin Web Service application pool, and the Search Query and Site Settings Web Service application pool must be registered as managed accounts in SharePoint Server so that they are available when you create the Search service application. Use the following procedure to register each of these accounts as a managed account.
  
 **To register a managed account**
  
1. On the Central Administration home page, in the Quick Launch, click **Security**.
    
2. On the Security page, in the **General Security** section, click **Configure managed accounts**.
    
3. On the Managed Accounts page, click **Register Managed Account**.
    
4. On the Register Managed Account page, in the **Account Registration** section, type the user name and password that you want to use as credentials for the service account. 
    
5. If you want SharePoint Server to manage password changes for this account, select the **Enable automatic password change** check box and configure the parameters for automatic password change. 
    
6. Click **OK**.
    
## Step 2: Create a SharePoint Search service application
<a name="begin"> </a>

Each Search service application has a separate content index. You can create multiple Search service applications if you want to have different content indexes for different sets of content. For example, if you want to segregate sensitive content (such as employee benefits information) into a separate content index, you can create a separate Search service application to correspond to that set of content.
  
If your SharePoint environment is hybrid, you can index content that resides in SharePoint Server into the Office 365 content index. In this case you need to create a Search service application of type **cloud**. You can only create one cloud Search service application per farm, but you can create multiple SSAs in combination with the single cloud SSA. 
  
> [!NOTE]
> Each Search service application has its own search topology. If you create more than one Search service application in a farm, we recommend that you allocate dedicated servers for the search topology of each Search service application. Deploying several Search service applications to the same servers will significantly increase the resource requirements (CPU and memory) on those servers. 
  
Use the following procedure to create a Search service application or a cloud Search service application.
  
 **To create a Search service application**
  
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group for the farm for which you want to create the service application.
    
2. On the Central Administration home page, in the **Application Management** section, click **Manage service applications**.
    
3. On the Manage Service Applications page, on the ribbon, click **New**, and then click **Search Service Application**.
    
4. On the Create New Search Service Application page, do the following: 
    
  - Accept the default value for **Service Application name**, or type a new name for the Search service application.
    
  - To make this a cloud Search service application, in the **Search Service Application type** section, checkmark the **Cloud Search Service Application** box. Otherwise, leave the box unchecked. 
    
  - In the **Search Service Account** list, select the managed account that you registered in the previous procedure to run the Search service. 
    
  - In the **Application Pool for Search Admin Web Service** section, do the following: 
    
    - Select the **Create new application pool** option, and then specify a name for the application pool in the **Application pool name** text box. 
    
    - In the **Select a security account for this application pool** section, select the **Configurable** option, and then from the list select the account that you registered to run the application pool for the Search Admin Web Service. 
    
  - In the **Application Pool for Search Query and Site Settings Web Service** section, do the following: 
    
    - Choose the **Create new application pool** option, and then specify a name for the application pool in the **Application pool name** text box. 
    
    - In the **Select a security account for this application pool** section, select the **Configurable** option, and then from the list select the account that you registered to run the application pool for the Search Query and Site Settings Web Service. 
    
5. Click **OK**.
    
## Step 3: Configure the SharePoint Search service application
<a name="begin"> </a>

You configure a Search service application on the Search Administration page for that service application. Use the following procedure to go to the Search Administration page for a particular Search service application.
  
 **To go to the Search Administration page**
  
1. Verify that the user account that is performing this procedure is an administrator for the Search service application that you want to configure.
    
2. On the home page of the Central Administration website, in the **Application Management** section, click **Manage service applications**.
    
3. On the Manage Service Applications page, click the Search service application that you want to configure.
    
On the Search Administration page, configure the settings as described in the following sections:
  
- Specify the default content access account
    
- Specify the contact email address
    
- Create content sources
    
### Specify the default content access account

When you create a Search service application, the account that you specify for the Search service is automatically configured as the default content access account. The crawler uses this account to crawl content that does not have an associated crawl rule that specifies a different account. For the default content access account, we recommend that you specify a domain user account that has read access to as much of the content that you want to crawl as possible. You can change the default content access account at any time. For more information, see [Use the default content access account to crawl most content](best-practices-for-crawling.md#BKMK_UseDefault) in [Best practices for crawling in SharePoint Server](best-practices-for-crawling.md).
  
If you have to crawl certain content by using a different account, you can create a crawl rule and specify a different account for crawling. For information about how to create a crawl rule, see [Manage crawl rules in SharePoint Server](manage-crawl-rules.md).
  
Use the following procedure to specify the default content access account.
  
 **To specify the default content access account**
  
1. On the Search Administration page, in the **System Status** section, click the link in the **Default content access account** row. 
    
2. In the **Default Content Access Account** dialog box, in the **Account** box, type the account that you created for content access in the form  _domain\user name_.
    
3. Type the password for this account in the **Password** and **Confirm Password** boxes. 
    
4. Click **OK**.
    
### Specify the contact email address

The Search service writes the contact email address to the logs of crawled servers. The default contact email address, someone@example.com, is a placeholder. We recommend that you change this to an account that an external administrator can contact when a crawl might be contributing to a problem such as a decrease in performance on a server that the search system is crawling.
  
Use the following procedure to specify the contact email address.
  
 **To specify the contact email address**
  
1. On the Search Administration page, in the **System Status** section, click the link for the **Contact e-mail address**.
    
2. In the **Search E-mail Setting** dialog box, in the **E-mail Address** box, type the email address that you want to appear in the logs of servers that are crawled by the search system. 
    
3. Click **OK**.
    
### Create content sources in a SharePoint Search service application

In order for users to be able to get search results, the search system must first crawl the corresponding content. Crawling requires at least one content source. A content source is a set of options that you use to specify the type of content to crawl, the starting URLs to crawl, and when and how deep to crawl. When a Search service application is created, a content source named "Local SharePoint sites" is automatically created and configured for crawling all SharePoint sites in the local server farm, and for crawling user profiles. You can create content sources to specify other content to crawl and how the system will crawl that content. For more information, see [Add, edit, or delete a content source in SharePoint Server](add-edit-or-delete-a-content-source.md). However, you do not have to create other content sources if you do not want to crawl content other than the SharePoint sites in the local farm.
  
If you choose the **Standalone** installation option when you install SharePoint Server 2016 or SharePoint Server 2019, a full crawl of all SharePoint sites in the farm is automatically performed after installation and an incremental crawl is scheduled to occur every 20 minutes after that. If you choose the **Server Farm** installation option when you install SharePoint Server 2016 or SharePoint Server 2019, no crawls are automatically scheduled or performed. In the latter case, you must either start crawls manually or schedule times for crawls to be performed. For more information, see the following articles; 
  
- [Start, pause, resume, or stop a crawl in SharePoint Server](start-pause-resume-or-stop-a-crawl.md)
    
- [Best practices for crawling in SharePoint Server](best-practices-for-crawling.md)
    
## Step 4: Configure the SharePoint Search service application topology
<a name="begin"> </a>

When you create a Search service application, the SharePoint Server Search service is started on the application server that is hosting the Central Administration website, and search components are deployed to that server. If you have more than one application server in your farm, you can deploy additional search components on other application servers, depending on your requirements. You can deploy multiple instances of certain components. For more information, see the following articles:
  
- [Manage the search topology in SharePoint Server](manage-the-search-topology.md)
    
- [Plan enterprise search architecture in SharePoint Server 2016](plan-enterprise-search-architecture.md)
    
- [Plan your search architecture in SharePoint Server for cloud hybrid search](/SharePoint/hybrid/plan-cloud-hybrid-search-for-sharepoint)
    
## See also
<a name="begin"> </a>

[Create a Search Center site in SharePoint Server](create-a-search-center-site.md)

