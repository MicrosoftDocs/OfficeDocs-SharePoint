---
title: "Upgrade My Sites to SharePoint Server 2013"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 2/21/2018
audience: ITPro
ms.topic: get-started-article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 33012208-8ff7-4816-993a-bd38b6e82fec
description: "Learn how to upgrade My Sites in SharePoint Server 2013."
---

# Upgrade My Sites to SharePoint Server 2013

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)]
  
## 

My Sites are site collections owned by the user for the user to store their documents, connect with other users, follow and discover content, and so on. Upgrading My Sites differs from upgrading other site collections because My Sites consist of both the shared My Site Host site collection (also known as the My Site Host) and the My Site personal site collection (also known as the personal site collection). 
  
- **My Site Host.** The My Site Host is a special site collection shared among all My Site users. The My Site Host is used to show the profile (person.aspx) and newsfeed pages (default.aspx) on the My Site. The My Site Host is also used for storing the user profile photos. 
    
- **Personal site collection.** In SharePoint Server 2010, the personal site collection was used to store a user's documents. In SharePoint Server 2013, the personal site collection contains OneDrive for Business, followed content, and so on. 
    
## Upgrading My Sites terms and concepts

- **Compatibility range settings.** The compatibility range settings control which user interface mode sites are created or displayed in (2010 user interface mode or 2013 user interface mode). The compatibility range settings allow administrators to separate the upgrade of site collections from the upgrade of content databases. To control the user interface mode, an administrator can set the MinCompatibilityLevel and the MaxCompatibilityLevel properties on a web application. For more information, see [Manage site collection upgrades to SharePoint 2013](manage-site-collection-upgrades-to-sharepoint-2013.md)
    
- **Mixed user interface modes.** During an upgrade, a user's My Site may display both the SharePoint Server 2010 and SharePoint Server 2013 master pages. When this happens, the My Site is displaying mixed user interface modes which may cause confusion for users. The mixed user interface modes are affected by the combination of the version of the My Site Host, and the compatibility range settings. When experiencing the mixed user interface modes on My Sites, users will not lose any data. 
    
> [!IMPORTANT]
> If you follow the section titled [Upgrade My Sites](upgrade-my-sites.md#procUMS), you will not encounter mixed user interface modes. 
  
## Planning considerations for upgrading My Sites

Before you start to upgrade from SharePoint Server 2010 to SharePoint Server 2013, you should carefully plan your upgrade process. The following list discusses some considerations when planning a My Site upgrade. 
  
- Before upgrading the My Site Host and the personal site collections, you must upgrade the Managed Metadata service application, and then the User Profile Service application. For more information, see [Services upgrade overview from SharePoint 2010 to SharePoint Server 2013](services-upgrade-overview-from-sharepoint-2010-to-sharepoint-server-2013.md)
    
- Some enterprises have multiple farms, that may include a services farm. In these environments, typically, one server farm, known as the enterprise services farm, publishes cross-farm shared services, and the other farms consume those shared services. In some cases, the User Profile Service application will be shared from the services farm, while a separate farm that consumes the shared User Profile Service application contains the My Sites. When you upgrade this type of configuration, you must upgrade the User Profile Service application on the services farm first, before you upgrade the My Sites farm.
    
- Consider whether you have to upgrade from classic-mode to claims-based authentication in SharePoint Server 2013. For more information, see [Migrate from classic-mode to claims-based authentication in SharePoint 2013](migrate-from-classic-mode-to-claims-based-authentication-in-sharepoint-2013.md)
    
> [!IMPORTANT]
> This list highlights some important things to consider when you perform an upgrade of My Sites. For a detailed discussion on upgrades, see [Get started with upgrades to SharePoint 2013](get-started-with-upgrade-0.md)
  
## Procedure to upgrade My Sites
<a name="procUMS"> </a>

The following list summarizes some of the upgrade activities for a My Site upgrade only. For more information about upgrades, see [Overview of the upgrade process from SharePoint 2010 to SharePoint 2013](overview-of-the-upgrade-process-from-sharepoint-2010-to-sharepoint-2013.md)
  
> [!IMPORTANT]
> Once you upgrade your My Site Host and personal site collections, you cannot undo the upgrade. 
  
> [!IMPORTANT]
> Some of the items in the following list require additional steps to be performed. These additional steps are discussed in the sections that follow this procedure. It is recommended when upgrading the entire server farm, that you also upgrade My Sites. 
  
1. Install and configure a new SharePoint Server 2013 farm. For more information, see [Create the SharePoint 2013 farm for a database attach upgrade](create-the-sharepoint-2013-farm-for-a-database-attach-upgrade.md).
    
2. Copy the SharePoint Server 2010 My Site content database, Social database, Sync database (optional), Profile database, and Managed Metadata service database to the SQL Server that supports your SharePoint Server 2013 farm. You will need db_owner permissions to perform this step. For more information, see [Copy databases to the new farm for upgrade to SharePoint 2013](copy-databases-to-the-new-farm-for-upgrade-to-sharepoint-2013.md) and [Create the SharePoint 2013 farm for a database attach upgrade](create-the-sharepoint-2013-farm-for-a-database-attach-upgrade.md).
    
3. Create the new service applications that you need for the SharePoint Server 2013 farm. Do not create the **User Profile Service application** and the **Managed Metadata service application**. You must upgrade these service applications, which is described in the next step. You must however start the User Profile Service and Managed Metadata service from **Manage Services on Server.**
    
4. Upgrade the **Managed Metadata service** and **User Profile service applications** using the database attach method. For more information, see [Upgrade service applications to SharePoint 2013](upgrade-service-applications-to-sharepoint-2013.md). Ensure the **My Site Host URL** field on the User Profile Service application is left blank because this field will be updated during the upgrade process. For more information, see [Configure My Site settings for the User Profile service application](../install/configure-my-sites.md#configsettings)
    
5. Create the web application for the My Sites using the default content database. To ensure the storage requirements of your users are met, you should review the site quota on the My Sites web application.
    
6. Set the compatibility range settings for site creation on the My Sites web application. Use **MinCompatibilityLevel = 15** and **MaxCompatibilityLevel= 15** for your compatibility range settings. 
    
7. Install customizations.
    
8. Run the **Test-SPContentDatabase** cmdlet to make sure that all customizations and language packs are installed on the server before upgrading the My Site content databases. This cmdlet must be run against all My Sites content databases. After running this cmdlet, you'll get a report on your environment. Ensure you review all items in this report as some reported items may prevent you from moving onto the next step. 
    
9. Run the **Mount-SPContentDatabase** cmdlet. Note: this does not upgrade any of the personal site collections at this point. After this step is complete, the My Sites will still be displayed as SharePoint Server 2010 My Sites. 
    
10. Check the configuration of the self-service site creation and managed paths settings on the My Sites web application to ensure the correct configuration settings are applied to the web application. For more information, see [Configure My Sites in SharePoint Server](../install/configure-my-sites.md).
    
11. Verify that the **My Site Host URL** field on the User Profile Service application has the correct URL users should use to access the My Sites web application. For more information, see [Configure My Site settings for the User Profile service application](../install/configure-my-sites.md#configsettings).
    
12. Upgrade the My Site Host from a SharePoint Server 2010 My Site host to a SharePoint Server 2013 My Site Host (discussed in the section titled [Upgrade the My Site Host site collection](upgrade-my-sites.md#UMSH)). 
    
13. Upgrade the personal site collections (discussed in the section titled [Upgrade the personal site collection](upgrade-my-sites.md#UPSC)).
    
> [!CAUTION]
> During the upgrade process, users will see some visual changes occurring on their My Sites until the upgrade process is complete. You should inform your users and helpdesk administrators that this experience is expected. 
  
## Upgrading the My Site Host
<a name="UMSH"> </a>

To upgrade a SharePoint Server 2010 My Site host to a SharePoint Server 2013 My Site host, run the following command at the **SharePoint 2013 Management Shell** command prompt: 
  
```
Upgrade-SPSite http://MySiteHostURL -versionupgrade
```

Where:
  
-  _http://MySiteHostURL_ is the URL of the My Site Host. 
    
## Upgrading the personal site collection
<a name="UPSC"> </a>

The personal site collections are upgraded automatically when a user visits their My Site. The SharePoint Server 2013 My Site Host has a hidden, automatic upgrade web part on it. When a user visits the My Site Host, and if the compatibility range settings allow 2013 user interface mode, an automatic upgrade of the user's My Site starts. This upgrade process is performed per user and may take some time to finish.
  
## Alternative procedure for upgrading My Sites
<a name="UPSC"> </a>

You may have constraints that restrict you from upgrading your My Sites to SharePoint Server 2013 My Sites. For example, you are upgrading your entire server farm but you have customizations on your My Sites that you have not tested on SharePoint Server 2013. In this scenario, you may not want to upgrade your My Sites until you complete your testing. 
  
If you want to upgrade your server farm but keep your My Sites as SharePoint Server 2010 My Sites, change the previous procedure for upgrading My Sites as follows:
  
- Step 6: Use MinCompatibilityLevel = 14 and MaxCompatibilityLevel= 14 for your compatibility range settings on the My Sites web application.
    
- Step 12: do not perform this step.
    
- Step 13: do not perform this step.
    
When you are ready to perform the upgrade of your My Sites:
  
- Set MinCompatibilityLevel = 15 and MaxCompatibilityLevel= 15 for your compatibility range settings on the My Sites web application.
    
- Upgrade the My Site Host as described in Step 12
    
- Upgrade the personal site collections as described in Step 13
    
> [!IMPORTANT]
> Once you upgrade your My Sites to SharePoint Server 2013 My Sites, you cannot revert to SharePoint Server 2010 My Sites. 
  
## Alternative procedure for upgrading the personal site collection
<a name="UPSC"> </a>

Administrators may choose these alternate methods of upgrading the personal site collections if they do not want their users experiencing the automatic upgrade of their My Site on their first visit to the My Site Host:
  
- **Forced upgrade.** If you use the forced upgrade path, users will not experience an automatic upgrade the first time they visit their My Site. Instead, their My Site will already be upgraded for them. A farm administrator can perform a forced upgrade of all My Sites in the farm by running the following command at the **SharePoint 2013 Management Shell** command prompt: 
    
  ```
  Get-SPSite -limit all |where {$_.CompatibilityLevel -eq '14'} | where {$_.RootWeb.WebTemplateId -eq  21} | upgrade-spsite -versionupgrade
  ```

    > [!IMPORTANT]
    > Before performing a forced upgrade, you should confirm that the My Site Host was upgraded successfully. You can verify this by either making sure that the My Site Host has the SharePoint Server 2013 user interface, or by inspecting the ULS logs to make sure that no errors were encountered during the upgrade process. 
  
    > [!CAUTION]
    > Using the forced upgrade approach may take lots of time to complete depending on the number of My Sites you are upgrading. This will affect your server farm's performance and the farm will be in read-only mode during the complete upgrade process. 
  
- **Deferred site collection upgrade.** The deferred site collection upgrade process uses the compatibility range settings to allow administrators to upgrade their databases and keep their site collections in SharePoint Server 2010 mode. When the compatibility range settings allow both 2010 user interface mode and 2013 user interface mode (MinCompatibilityLevel = 14 and MaxCompatibilityLevel= 15), the owner of the My Site will see a red banner at the top of their My Site. From the banner, they can request an evaluation site collection of their My Site to preview before upgrading to the SharePoint Server 2013 user interface. The evaluation site cannot be converted to a regular My Site because it is a temporary site which will eventually be deleted. The deferred site collection upgrade path is performed per user. 
    
    > [!CAUTION]
    > Using the deferred site collection upgrade may result in the mixed user interface mode issue. Be sure to stage and test your upgrade carefully before you do this in production. When you encounter the mixed user interface mode on your My Sites, new users who do not have a My Site cannot create new My Sites. 
  
## Troubleshooting a My Site upgrade
<a name="UPSC"> </a>

If users are experiencing issues, such as mixed user interface modes or they cannot upgrade their My Site to the SharePoint Server 2013 user interface mode, verify that the following steps were completed:
  
- The My Site Host was upgraded to a SharePoint Server 2013 My Site Host.
    
- The compatibility range settings allow site creation in 2013 user interface mode.
    
- The SPSite.CanUpgrade property on the personal site collection of the user requesting the upgrade is set to **true**. An administrator may allow or restrict certain site collections from being upgraded by setting this property at the site collection level. 
    
> [!NOTE]
> The upgrade of the personal site collection is not an instant process. The My Site is added to an upgrade queue. When the upgrade starts, the My Site remains available to use during the upgrade process. Users can work on their documents throughout the upgrade process. The My Site Host and personal site collection will display mixed user interface modes until the upgrade is complete. 
  
## See also
<a name="UPSC"> </a>

#### Other Resources

[Upgrade a site collection to SharePoint 2013](upgrade-a-site-collection-to-sharepoint-2013.md)
  
[Update-SPProfilePhotoStore](/powershell/module/sharepoint-server/Update-SPProfilePhotoStore?view=sharepoint-ps)

