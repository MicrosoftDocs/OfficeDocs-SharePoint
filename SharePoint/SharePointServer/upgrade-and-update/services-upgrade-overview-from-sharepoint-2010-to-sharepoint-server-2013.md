---
title: "Services upgrade overview from SharePoint 2010 to SharePoint Server 2013"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/26/2017
audience: ITPro
ms.topic: concetpual
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 1f2997aa-6bfe-441e-a100-2466c527468f
description: "Create a plan to upgrade data for service applications when you upgrade from SharePoint Server 2010 to SharePoint Server 2013."
---

# Services upgrade overview from SharePoint 2010 to SharePoint Server 2013

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)]
  
The upgrade process for SharePoint Server 2013 uses the database attach upgrade method. When you move your databases to a new farm and upgrade the content, you must create your services infrastructure in the new farm, and configure the services appropriately for your new farm and new version. The following service applications have databases that can be upgraded when you upgrade from SharePoint Server 2010 to SharePoint Server 2013:
  
- Business Data Connectivity service application
    
- Managed Metadata service application
    
- PerformancePoint Services service application
    
- Search service application
    
- Secure Store Service application
    
- User Profile service application
    
Attaching and upgrading these databases configures these service applications. Settings for other services will have to be reconfigured when you upgrade.
  
> [!IMPORTANT]
> The content in this article about the Business Data Connectivity service application applies to both SharePoint Foundation 2013 and SharePoint Server 2013. Other services are available only in SharePoint Server 2013. 
  
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
    
- **Search**
    
    In SharePoint Server 2010, the Search service application Administration database contains settings for the Search service application such as content sources, crawl rules, start addresses, server name mapping, and federated locations. You can upgrade a Search service application Administration database from SharePoint Server 2010 to SharePoint Server 2013 by using a database attach approach.
    
    You cannot use the database attach approach to upgrade any other search databases, such as crawl databases or property databases. (These databases are re-created when you perform a full crawl in the new farm.) Also, the upgrade process does not preserve or upgrade logical components of the SharePoint Server 2010 farm topology. After you perform the upgrade, you must manually re-create a topology as appropriate for the requirements of the organization.
    
- **Secure Store service**
    
    The Secure Store Service uses a database to store information. This database must be upgraded as part of a services database attach upgrade. You have to upgrade the data for this service application so that any connections from Excel Services Application and Business Connectivity Services can work with existing passwords.
    
- **User Profile service**
    
    The User Profile service uses databases to store profile, social, and sync information. These databases must be upgraded as part of a services database attach upgrade. You have to attach and upgrade the databases for this service and for the Managed Metadata service before you can upgrade any My Sites. 
    
    > [!NOTE]
    > My Sites are not available in SharePoint Foundation 2010 or SharePoint Foundation 2013. 
  
Specifically, the following service application databases can be upgraded:
  
|**Service application**|**Default database name**|
|:-----|:-----|
|Business Data Connectivity  <br/> |BDC_Service_DB_ _ID_ <br/> |
|Managed Metadata  <br/> |Managed Metadata Service_ _ID_ <br/> |
|PerformancePoint  <br/> |PerformancePoint Service Application_ _ID_ <br/> |
|Search Administration  <br/> |Search_Service_Application_DB_ _ID_ <br/> |
|Secure Store  <br/> |Secure_Store_Service_DB_ _ID_ <br/> |
|User Profile: Profile and Social databases  <br/> |User Profile Service Application_ProfileDB_ _ID_ <br/> User Profile Service Application_SocialDB_ _ID_ <br/> User Profile Service Application_SyncDB_ _ID_ <br/> |
   
The steps to upgrade these service application databases are included in [Upgrade content databases to SharePoint Server 2016](upgrade-content-databases.md).
  
## Considerations for specific services
<a name="Considerations"> </a>

The following services in SharePoint Server 2013 also require additional steps to enable and configure when you upgrade:
  
- **Excel Services**
    
    You can enable this service by using the Farm Configuration Wizard, but you must make sure that you re-create all trusted data connections. For more information, see [Manage Excel Services trusted data providers (SharePoint Server 2013)](../administration/manage-excel-services-trusted-data-providers.md).
    
- **InfoPath Forms Service**
    
    This service is not part of the Farm Configuration Wizard. If you want to use this service, you can use the **Configure InfoPath Forms Services** link on the **General Application Settings** page in SharePoint Central Administration to configure it. If you want to continue using form templates from your previous environment, you can export any administrator-deployed form templates (.xsn files) and data connection files (.udcx files) from your SharePoint Server 2010 environment, and then import them to your new SharePoint Server 2013 environment by using the **Export-SPInfoPathAdministrationFiles** PowerShell cmdlet. If the URL of the new server differs from the URL of the previous server, you can run the **Update-SPInfoPathAdminFileUrl** PowerShell cmdlet to update links that are used in the upgraded form templates. For more information, see [Configure InfoPath Forms Services (SharePoint Server 2010)](https://go.microsoft.com/fwlink/?LinkId=403876). 
    
- **Office Web Apps**
    
    If you installed Office Online with SharePoint 2010 Products, Office Online will not be available after you upgrade to SharePoint 2013 Products. You must deploy Office Online Server and then connect SharePoint 2013 Products it to after the content databases are upgraded. You do not have to wait until the site collections are upgraded because Office Online Server supports both the 2010 and 2013 site collection modes in SharePoint 2013 Products. For more information, see [Office Web Apps](/webappsserver/office-web-apps-server).
    
## See also
<a name="Considerations"> </a>

#### Other Resources

[Overview of the upgrade process from SharePoint 2010 to SharePoint 2013](overview-of-the-upgrade-process-from-sharepoint-2010-to-sharepoint-2013.md)
  
[Upgrade content databases from SharePoint 2010 to SharePoint 2013](upgrade-content-databases-from-sharepoint-2010-to-sharepoint-2013.md)

