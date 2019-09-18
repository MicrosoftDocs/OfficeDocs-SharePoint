---
title: "Services upgrade overview for SharePoint Server 2016"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 9/29/2016
audience: ITPro
ms.topic: get-started-article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 5aeff319-0a8f-4d6b-86d5-6086611c48ed
description: "Create a plan to upgrade data for service applications when you upgrade from SharePoint Server 2013 to SharePoint Server 2016."
---

# Services upgrade overview for SharePoint Server 2016   
  
The upgrade process for SharePoint Server 2016 uses the database attach upgrade method. When you move your databases to a new farm and upgrade the content, you must create your services infrastructure in the new farm, and configure the services appropriately for your new farm and new version. The following service applications have databases that can be upgraded when you upgrade from SharePoint Server 2013 to SharePoint Server 2016:
  
- Business Data Connectivity service application
    
- Managed Metadata service application
    
- PerformancePoint Services service application
    
- Search service application
    
- Secure Store Service application
    
- User Profile service application
    
> [!NOTE]
> Word Automation Services and Machine Translation Services can't be upgraded. A new service instance needs to be created. 
  
Attaching and upgrading these databases configures these service applications. Settings for other services will have to be reconfigured when you upgrade.
  
## Database attach upgrade with services
<a name="dbattach"> </a>

You must create the service applications on your new farm before you upgrade your content databases. The steps included in the installation guide above describe how to use the Farm Configuration Wizard to enable all service applications. Some service applications can be upgraded by using a service application database upgrade. If you want to upgrade these service applications by upgrading the service application databases, you should not use the Farm Configuration Wizard to configure these service applications when you set up your new farm.
  
The following service applications can be upgraded by performing a services database upgrade:
  
- **Business Data Connectivity service**
    
    The Business Data Connectivity service uses a database to store information about external data. This database must be upgraded as part of a services database attach upgrade. This service application is also available in SharePoint Foundation 2013.
    
- **Managed Metadata service**
    
    The Managed Metadata service uses a database to store metadata information. This database must be upgraded as part of a services database attach upgrade. You must attach and upgrade the database for this service and for the User Profile service before you can upgrade any My Sites.
    
- **PerformancePoint services**
    
    PerformancePoint Services use a database to store information. This database must be upgraded as part of a services database attach upgrade.
    
- **Secure Store service**
    
    The Secure Store Service uses a database to store information. This database must be upgraded as part of a services database attach upgrade. You have to upgrade the data for this service application so that any connections from Excel Services Application and Business Connectivity Services can work with existing passwords.
    
- **User Profile service**
    
    The User Profile service uses databases to store profile, social, and sync information. These databases must be upgraded as part of a services database attach upgrade. You have to attach and upgrade the databases for this service and for the Managed Metadata service before you can upgrade any My Sites.
    
- **Search**
    
    The Search service uses several databases. The search administration database stores search configuration data, such as the topology, crawl rules, query rules, and the mappings between crawled and managed properties. The analytics reporting database stores the results of usage analytics and statistics information from the analyses.
  
The search administration database must be upgraded as part of a services database attach upgrade, and you can optionally upgrade the analytics database as part of the services database attach upgrade. You have to attach and upgrade the database for the User Profile service and Managed Metadata service before you upgrade the search databases. You cannot use the database attach approach for the rest of the search databases, these databases are re-created when you upgrade the Search service application.
    
Specifically, the following service application databases can be upgraded:
  
|**Service application**|**Default database name**|
|:-----|:-----|
|Business Data Connectivity  <br/> |BDC_Service_DB_\<GUID\>  <br/> |
|Managed Metadata  <br/> |Managed Metadata Service_\<GUID\>  <br/> |
|PerformancePoint  <br/> |PerformancePoint Service Application_\<GUID\>  <br/> |
|Search  <br/> |Search_Service_Application_DB_\<GUID\>  <br/> Search_Service_Application_AnalyticsReportingStoreDB_\<GUID\>  <br/> |
|Secure Store  <br/> |Secure_Store_Service_DB_\<GUID\>  <br/> |
|User Profile: Profile and Social databases  <br/> |User Profile Service Application_ProfileDB_\<GUID\>  <br/> User Profile Service Application_SocialDB_\<GUID\>  <br/> User Profile Service Application_SyncDB_\<GUID\>  <br/> |
   
The steps to upgrade these service application databases are included in [Upgrade service applications to SharePoint Server 2016](/SharePoint/upgrade-and-update/upgrade-service-applications-to-sharepoint-server-2016).
  
## Considerations for specific services
<a name="Considerations"> </a>

The following services in SharePoint Server 2016 also require additional steps to enable and configure when you upgrade:
  
- **InfoPath Forms Service**
    
    This service is not part of the Farm Configuration Wizard. If you want to use this service, you can use the **Configure InfoPath Forms Services** link on the **General Application Settings** page in SharePoint Central Administration to configure it. If you want to continue using form templates from your previous environment, you can export any administrator-deployed form templates (.xsn files) and data connection files (.udcx files) from your SharePoint Server 2013 environment, and then import them to your new SharePoint Server 2016 environment by using the **Export-SPInfoPathAdministrationFiles** PowerShell cmdlet. If the URL of the new server differs from the URL of the previous server, you can run the **Update-SPInfoPathAdminFileUrl** PowerShell cmdlet to update links that are used in the upgraded form templates. 
    
- **Office Online Server**
    
    You must deploy Office Online Server and then connect SharePoint Server 2016 it to after the content databases are upgraded. You do not have to wait until the site collections are upgraded because Office Online Server supports both the 2013 and 2016 site collection modes in SharePoint Server 2016. For more information, see [Office Web Apps](/webappsserver/office-web-apps-server).
    
## See also
<a name="Considerations"> </a>

#### Concepts

[Overview of the upgrade process to SharePoint Server 2016](overview-of-the-upgrade-process.md)
  
[Upgrade content databases to SharePoint Server 2016](upgrade-content-databases.md)

