---
title: "Upgrade My Sites to SharePoint Server 2019"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
audience: ITPro
ms.topic: get-started-article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
- SP2019
ms.assetid: d47575fa-bb85-4017-8db7-5e25f98ba171
description: "Learn how to upgrade My Sites site collections in SharePoint Server 2019."
---

# Upgrade My Sites to SharePoint Server 2019

[!INCLUDE[appliesto-xxx-2016-2019-xxx-md](../includes/appliesto-xxx-2016-2019-xxx-md.md)] 
  
## 

My Sites are personal site collections that end users can use to store their documents, connect with other users, and follow and discover content. Upgrading My Sites differs from upgrading other site collections because My Sites consist of both the shared My Site Host site collection (also known as the My Site Host) and the My Site personal site collection (also known as the personal site collection). 
  
- **My Site Host.** The My Site Host is a special site collection shared among all My Site users. The My Site Host is used to show the profile (person.aspx) and newsfeed pages (default.aspx) on the My Site. The My Site Host is also used for storing the user profile photos. 
    
- **Personal site collection.** In SharePoint Server 2019, the personal site collection is used to store a user's documents. In SharePoint Server 2019, the personal site collection contains OneDrive for Business, followed content, and so on. 
    
## Plan to upgrade My Sites

Before you start to upgrade from SharePoint Server 2016 to SharePoint Server 2019, you should carefully plan your upgrade process. The following list discusses some considerations when planning a My Site upgrade. 
  
- Before upgrading the My Site Host and the personal site collections, you must upgrade the Managed Metadata service application, and then the User Profile Service application. For more information, see [Services upgrade overview for SharePoint Server 2019](overview-of-the-services-upgrade-process-2019.md)
    
- Some enterprises have multiple farms, that may include a services farm. In these environments, typically, one server farm, known as the enterprise services farm, publishes cross-farm shared services, and the other farms consume those shared services. In some cases, the User Profile Service application will be shared from the services farm, while a separate farm that consumes the shared User Profile Service application contains the My Sites. When you upgrade this type of configuration, you must upgrade the User Profile Service application on the services farm first, before you upgrade the My Sites farm.
    
   
> [!IMPORTANT]
> This list highlights some important things to consider when you perform an upgrade of My Sites. For a detailed discussion on upgrades, see [Get started with upgrades to SharePoint Server 2019](get-started-with-upgrade-2019.md)
  
## Upgrade My Sites
<a name="procUMS"> </a>

The following list summarizes some of the upgrade activities for a My Site upgrade only. For more information about upgrades, see [Upgrade to SharePoint Server 2019](upgrade-to-sharepoint-server-2019.md)
  
> [!IMPORTANT]
>  Once you upgrade your My Site Host and personal site collections, you cannot undo the upgrade. >  Some of the items in the following list require additional steps to be performed. These additional steps are discussed in the sections that follow this procedure. It is recommended when upgrading the entire server farm, that you also upgrade My Sites. 
  
1. Install and configure a new SharePoint Server 2019 farm. For more information, see [Create the SharePoint Server 2016 farm for a database attach upgrade](create-the-sharepoint-server-2019-farm-for-a-database-attach-upgrade.md).
    
2. Copy the SharePoint Server 2016 My Site content database, Social database, Sync database (optional), Profile database, and Managed Metadata service database to the SQL Server that supports your SharePoint Server 2019 farm. You will need db_owner permissions to perform this step. For more information, see [Copy databases to the new farm for upgrade to SharePoint Server 2016](copy-databases-to-the-new-farm-for-upgrade-to-sharepoint-server-2019.md) and [Create the SharePoint Server 2016 farm for a database attach upgrade](create-the-sharepoint-server-2019-farm-for-a-database-attach-upgrade.md).
    
3. Create the new service applications that you need for the SharePoint Server 2019 farm. Do not create the **User Profile Service application** and the **Managed Metadata service application**. You must upgrade these service applications, which is described in the next step. You must however start the User Profile Service and Managed Metadata service from **Manage Services on Server.**
    
4. Upgrade the **Managed Metadata service** and **User Profile service applications** using the database attach method. For more information, see [Upgrade service applications to SharePoint Server 2019](upgrade-service-applications-to-sharepoint-server-2019.md). Ensure the **My Site Host URL** field on the User Profile Service application is left blank because this field will be updated during the upgrade process. For more information, see [Configure My Site settings for the User Profile service application](../install/configure-my-sites.md#configsettings)
    
5. Create the web application for the My Sites using the default content database. To ensure the storage requirements of your users are met, you should review the site quota on the My Sites web application.
    
  
6. Install customizations.
    
7. Run the **Test-SPContentDatabase** cmdlet to make sure that all customizations and language packs are installed on the server before upgrading the My Site content databases. This cmdlet must be run against all My Sites content databases. After running this cmdlet, you'll get a report on your environment. Ensure you review all items in this report as some reported items may prevent you from moving onto the next step. 
    
8. Run the **Mount-SPContentDatabase** cmdlet. Note: this does not upgrade any of the personal site collections at this point. After this step is complete, the My Sites will still be displayed as SharePoint Server 2013 My Sites. 
    
9. Check the configuration of the self-service site creation and managed paths settings on the My Sites web application to ensure the correct configuration settings are applied to the web application. 
    
10. Verify that the **My Site Host URL** field on the User Profile Service application has the correct URL users should use to access the My Sites web application. For more information, see [Configure My Site settings for the User Profile service application](../install/configure-my-sites.md#configsettings).
    
11. Upgrade the My Site Host from a SharePoint Server 2016 My Site host to a SharePoint Server 2019 My Site Host (discussed in the section titled [Upgrade the My Site Host site collection](upgrade-my-sites-2019.md#UMSH)). 
    
12. Upgrade the personal site collections (discussed in the section titled [Upgrade the personal site collection](upgrade-my-sites-2019.md#UPSC)).
    
> [!CAUTION]
> During the upgrade process, users will see some visual changes occurring on their My Sites until the upgrade process is complete. You should inform your users and helpdesk administrators that this experience is expected. 
  
## Upgrade the My Site Host site collection
<a name="UMSH"> </a>

To upgrade a SharePoint Server 2016 My Site host to a SharePoint Server 2019 My Site host, run the following command at the SharePoint 2019 Management Shell command prompt:
  
```
Upgrade-SPSite http://MySiteHostURL -versionupgrade
```

Where:
  
-  _http://MySiteHostURL_ is the URL of the My Site Host. 
    
## Upgrade the personal site collection
<a name="UPSC"> </a>

The personal site collections are upgraded automatically when a user visits their My Site. The SharePoint Server 2019 My Site Host has a hidden, automatic upgrade web part on it. This upgrade process is performed per user and may take some time to finish.
  
 
> [!IMPORTANT]
> Once you upgrade your My Sites to SharePoint Server 2019 My Sites, you cannot revert to SharePoint Server 2016 My Sites. 
  
  
> [!NOTE]
> The upgrade of the personal site collection is not an instant process. The My Site is added to an upgrade queue. When the upgrade starts, the My Site remains available to use during the upgrade process. Users can work on their documents throughout the upgrade process. The My Site Host and personal site collection will display mixed user interface modes until the upgrade is complete. 
  
#### Other Resources

[Upgrade a site collection](https://support.office.com/en-us/article/upgrade-your-2010-version-sharepoint-online-sites-to-latest-classic-ui-experience-7f66dfdc-9a3d-4769-8a05-c654e4a27ec2?ocmsassetID=HA102865473&CTT=5&amp%3Borigin=HA104034491&CorrelationId=db6f9747-dd10-4526-85b6-79e94c1599e4&ui=en-US&rs=en-US&ad=US)
  
[Update-SPProfilePhotoStore](/powershell/module/sharepoint-server/Update-SPProfilePhotoStore?view=sharepoint-ps)

