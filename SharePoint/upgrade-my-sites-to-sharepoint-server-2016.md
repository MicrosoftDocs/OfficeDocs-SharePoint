---
title: Upgrade My Sites to SharePoint Server 2016
ms.prod: SHAREPOINT
ms.assetid: d47575fa-bb85-4017-8db7-5e25f98ba171
---


# Upgrade My Sites to SharePoint Server 2016
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2016-09-16* **Summary:** Learn how to upgrade My Sites site collections in SharePoint Server 2016.
## 

My Sites are personal site collections that end users can use to store their documents, connect with other users, and follow and discover content. Upgrading My Sites differs from upgrading other site collections because My Sites consist of both the shared My Site Host site collection (also known as the My Site Host) and the My Site personal site collection (also known as the personal site collection). 
- **My Site Host.** The My Site Host is a special site collection shared among all My Site users. The My Site Host is used to show the profile (person.aspx) and newsfeed pages (default.aspx) on the My Site. The My Site Host is also used for storing the user profile photos.
    
  
- **Personal site collection.** In SharePoint Server 2013, the personal site collection was used to store a user’s documents. In SharePoint Server 2016, the personal site collection contains OneDrive for Business, followed content, and so on.
    
  

## Plan to upgrade My Sites

Before you start to upgrade from SharePoint Server 2013 to SharePoint Server 2016, you should carefully plan your upgrade process. The following list discusses some considerations when planning a My Site upgrade. 
- Before upgrading the My Site Host and the personal site collections, you must upgrade the Managed Metadata service application, and then the User Profile Service application. For more information, see  [Services upgrade overview for SharePoint Server 2016](html/services-upgrade-overview-for-sharepoint-server-2016.md)
    
  
- Some enterprises have multiple farms, that may include a services farm. In these environments, typically, one server farm, known as the enterprise services farm, publishes cross-farm shared services, and the other farms consume those shared services. In some cases, the User Profile Service application will be shared from the services farm, while a separate farm that consumes the shared User Profile Service application contains the My Sites. When you upgrade this type of configuration, you must upgrade the User Profile Service application on the services farm first, before you upgrade the My Sites farm.
    
  
- Consider whether you have to upgrade from classic-mode to claims-based authentication in SharePoint Server 2013. For more information, see **Migrate from classic-mode to claims-based authentication in SharePoint Server**
    
  

> [!IMPORTANT:]

  
    
    


## Upgrade My Sites
<a name="procUMS"> </a>

The following list summarizes some of the upgrade activities for a My Site upgrade only. For more information about upgrades, see  [Upgrade to SharePoint Server 2016](html/upgrade-to-sharepoint-server-2016.md)
> [!IMPORTANT:]
>  Once you upgrade your My Site Host and personal site collections, you cannot undo the upgrade.>  Some of the items in the following list require additional steps to be performed. These additional steps are discussed in the sections that follow this procedure. It is recommended when upgrading the entire server farm, that you also upgrade My Sites.
  
    
    


1. Install and configure a new SharePoint Server 2016 farm. For more information, see  [Create the SharePoint Server 2016 farm for a database attach upgrade](html/create-the-sharepoint-server-2016-farm-for-a-database-attach-upgrade.md).
    
  
2. Copy the SharePoint Server 2013 My Site content database, Social database, Sync database (optional), Profile database, and Managed Metadata service database to the SQL Server that supports your SharePoint Server 2016 farm. You will need db_owner permissions to perform this step. For more information, see  [Copy databases to the new farm for upgrade to SharePoint Server 2016](html/copy-databases-to-the-new-farm-for-upgrade-to-sharepoint-server-2016.md) and [Create the SharePoint Server 2016 farm for a database attach upgrade](html/create-the-sharepoint-server-2016-farm-for-a-database-attach-upgrade.md).
    
  
3. Create the new service applications that you need for the SharePoint Server 2016 farm. Do not create the **User Profile Service application** and the **Managed Metadata service application**. You must upgrade these service applications, which is described in the next step. You must however start the User Profile Service and Managed Metadata service from **Manage Services on Server.**
    
  
4. Upgrade the **Managed Metadata service** and **User Profile service applications** using the database attach method. For more information, see [Upgrade service applications to SharePoint Server 2016](html/upgrade-service-applications-to-sharepoint-server-2016.md). Ensure the **My Site Host URL** field on the User Profile Service application is left blank because this field will be updated during the upgrade process. For more information, see [Configure My Site settings for the User Profile service application](configure-my-sites-in-sharepoint-server.md#configsettings)
    
  
5. Create the web application for the My Sites using the default content database. To ensure the storage requirements of your users are met, you should review the site quota on the My Sites web application.
    
  
6. Set the compatibility range settings for site creation on the My Sites web application. Use **MinCompatibilityLevel = 15** and **MaxCompatibilityLevel= 15** for your compatibility range settings.
    
  
7. Install customizations.
    
  
8. Run the **Test-SPContentDatabase** cmdlet to make sure that all customizations and language packs are installed on the server before upgrading the My Site content databases. This cmdlet must be run against all My Sites content databases. After running this cmdlet, you'll get a report on your environment. Ensure you review all items in this report as some reported items may prevent you from moving onto the next step.
    
  
9. Run the **Mount-SPContentDatabase** cmdlet. Note: this does not upgrade any of the personal site collections at this point. After this step is complete, the My Sites will still be displayed as SharePoint Server 2013 My Sites.
    
  
10. Check the configuration of the self-service site creation and managed paths settings on the My Sites web application to ensure the correct configuration settings are applied to the web application. For more information, see  [Configure My Sites in SharePoint Server](html/configure-my-sites-in-sharepoint-server.md).
    
  
11. Verify that the **My Site Host URL** field on the User Profile Service application has the correct URL users should use to access the My Sites web application. For more information, see [Configure My Site settings for the User Profile service application](configure-my-sites-in-sharepoint-server.md#configsettings).
    
  
12. Upgrade the My Site Host from a SharePoint Server 2013 My Site host to a SharePoint Server 2016 My Site Host (discussed in the section titled  [Upgrading the My Site Host](#UMSH)). 
    
  
13. Upgrade the personal site collections (discussed in the section titled  [Upgrading the personal site collection](#UPSC)).
    
  

> [!WARNING:]

  
    
    


## Upgrade the My Site Host site collection
<a name="UMSH"> </a>

To upgrade a SharePoint Server 2013 My Site host to a SharePoint Server 2016 My Site host, run the following command at the SharePoint 2016 Management Shell command prompt:
```

Upgrade-SPSite http://MySiteHostURL -versionupgrade
```

Where:
-  *http://MySiteHostURL*  is the URL of the My Site Host.
    
  

## Upgrade the personal site collection
<a name="UPSC"> </a>

The personal site collections are upgraded automatically when a user visits their My Site. The SharePoint Server 2016 My Site Host has a hidden, automatic upgrade web part on it. When a user visits the My Site Host, and if the compatibility range settings allow 2013 user interface mode, an automatic upgrade of the user’s My Site starts. This upgrade process is performed per user and may take some time to finish.
## Alternative procedure for upgrading My Sites
<a name="UPSC"> </a>

You may have constraints that restrict you from upgrading your My Sites to SharePoint Server 2016 My Sites. For example, you are upgrading your entire server farm but you have customizations on your My Sites that you have not tested on SharePoint Server 2016. In this scenario, you may not want to upgrade your My Sites until you complete your testing. If you want to upgrade your server farm but keep your My Sites as SharePoint Server 2013 My Sites, change the previous procedure for upgrading My Sites as follows:
- Step 6: Use MinCompatibilityLevel = 14 and MaxCompatibilityLevel= 14 for your compatibility range settings on the My Sites web application.
    
  
- Step 12: do not perform this step.
    
  
- Step 13: do not perform this step.
    
  
When you are ready to perform the upgrade of your My Sites:
- Set MinCompatibilityLevel = 15 and MaxCompatibilityLevel= 15 for your compatibility range settings on the My Sites web application.
    
  
- Upgrade the My Site Host as described in Step 12
    
  
- Upgrade the personal site collections as described in Step 13
    
  

> [!IMPORTANT:]

  
    
    


## Alternative procedure for upgrading the personal site collection
<a name="UPSC"> </a>

Administrators may choose these alternate methods of upgrading the personal site collections if they do not want their users experiencing the automatic upgrade of their My Site on their first visit to the My Site Host:
- **Forced upgrade.** If you use the forced upgrade path, users will not experience an automatic upgrade the first time they visit their My Site. Instead, their My Site will already be upgraded for them. A farm administrator can perform a forced upgrade of all My Sites in the farm by running the following command at the **SharePoint 2016 Management Shell** command prompt:
    
  ```
  
Get-SPSite -limit all |where {$_.CompatibilityLevel -eq '14'} | where {$_.RootWeb.WebTemplateId -eq  21} | upgrade-spsite -versionupgrade
  ```


    > [!IMPORTANT:]
      

    > [!WARNING:]
      
- **Deferred site collection upgrade.** The deferred site collection upgrade process uses the compatibility range settings to allow administrators to upgrade their databases and keep their site collections in SharePoint Server 2010 mode. When the compatibility range settings allow both 2010 user interface mode and 2013 user interface mode (MinCompatibilityLevel = 14 and MaxCompatibilityLevel= 15), the owner of the My Site will see a red banner at the top of their My Site. From the banner, they can request an evaluation site collection of their My Site to preview before upgrading to the SharePoint Server 2013 user interface. The evaluation site cannot be converted to a regular My Site because it is a temporary site which will eventually be deleted. The deferred site collection upgrade path is performed per user.
    
    > [!WARNING:]
      

## Troubleshoot a My Site upgrade
<a name="UPSC"> </a>

If users are experiencing issues, such as mixed user interface modes or they cannot upgrade their My Site to the SharePoint Server 2013 user interface mode, verify that the following steps were completed:
- The My Site Host was upgraded to a SharePoint Server 2016 My Site Host.
    
  
- The compatibility range settings allow site creation in 2013 user interface mode.
    
  
- The SPSite.CanUpgrade property on the personal site collection of the user requesting the upgrade is set to **true**. An administrator may allow or restrict certain site collections from being upgraded by setting this property at the site collection level.
    
  

> [!NOTE:]

  
    
    


# See also

#### 

 **Update-SPProfilePhotoStore**
  
    
    
 [Upgrade a site collection](http://office.microsoft.com/en-us/office365-sharepoint-online-enterprise-help/upgrade-a-site-collection-HA102865473.aspx?CTT=5&amp;origin=HA104034491)
  
    
    

  
    
    

