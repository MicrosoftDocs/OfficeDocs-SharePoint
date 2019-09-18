---
title: "What's new in SharePoint 2013 upgrade"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/24/2017
audience: ITPro
ms.topic: get-started-article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 2a78e133-5228-4ab6-9d9b-cf318c0e3883
description: "SharePoint 2013 includes new upgrade features, such as upgrade for service applications, a site health checker, and upgrade for site collections."
---

# What's new in SharePoint 2013 upgrade

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)]
  
SharePoint 2013 does not support in-place upgrade for an existing environment. You must use the database-attach upgrade method to upgrade your databases to a new environment that is based on SharePoint 2013. Also, to provide more flexibility to farm administrators and site administrators, the upgrade process has changed to separate upgrade of the software and databases from upgrade of the sites. 
  
## In-place upgrade of the farm is not supported
<a name="NoInplace"> </a>

An upgrade to SharePoint Server 2010 or SharePoint Foundation 2010 provided an option to install the new version over the earlier version on the same hardware. This was called an in-place upgrade. During this process, the complete installation (both databases and sites) was upgraded in a fixed order. Although this was a simple method, in-place upgrade presented problems in performance and control for a farm administrator. There was no way to control the order in which content is upgraded, and a failure in a particular site collection could stop the whole process.
  
The database-attach upgrade method offers more flexibility, more control, and a better success rate. Therefore, in-place upgrade is not supported for SharePoint 2013 and database-attach upgrade is the only supported upgrade method.
  
To use a database attach upgrade, you complete the following tasks:
  
1. Create and configure a new farm that is separate from the old farm
    
2. Copy the content and services databases to the new farm
    
3. Upgrade the data and sites
    
You can upgrade the content databases in any order and upgrade several databases at the same time to speed up the overall process.
  
For more information, see [Overview of the upgrade process from SharePoint 2010 to SharePoint 2013](overview-of-the-upgrade-process-from-sharepoint-2010-to-sharepoint-2013.md).
  
## Database-attach upgrade is available for some service application databases
<a name="DBattachforservices"> </a>

For the SharePoint 2013, you can use the database attach upgrade method to upgrade the following service application databases:
  
- Business Data Connectivity
    
    This service application is available for both SharePoint 2013 and SharePoint Foundation 2013.
    
- Managed Metadata
    
    This service application is available only for SharePoint 2013.
    
- PerformancePoint
    
    This service application is available only for SharePoint 2013.
    
- Secure Store
    
    This service application is available only for SharePoint 2013.
    
- User Profile (Profile, Social, and Sync databases)
    
    This service application is available only for SharePoint 2013.
    
- Search administration
    
    This service application is available only for SharePoint 2013.
    
For more information, see [Services upgrade overview from SharePoint 2010 to SharePoint Server 2013](services-upgrade-overview-from-sharepoint-2010-to-sharepoint-server-2013.md).
  
## Deferred site collection upgrade
<a name="SiteCollUpgrade"> </a>

In SharePoint 2010 Products, farm administrators use either the in-place upgrade process to upgrade sites immediately, or the command line to upgrade all sites at the same time or individually. In SharePoint 2013, farm administrators can now allow site collection owners to upgrade their sites to the new user interface on their own timeline. The commands for upgrading a site collection are on the Site Settings page in the Site Collection Administration section. There are also Microsoft PowerShell cmdlets to upgrade site collections to the new user interface. For more information, see [Plan for site collection upgrades in SharePoint 2013](/previous-versions/office/sharepoint-server-2010/ff191199(v=office.14)), [Upgrade a site collection to SharePoint 2013](upgrade-a-site-collection-to-sharepoint-2013.md) and [Manage site collection upgrades (SharePoint 2013 Products)](/SharePoint/upgrade-and-update/manage-site-collection-upgrades-to-sharepoint-2013).
  
## Site collection health checker
<a name="HealthChecker"> </a>

Site collection owners or administrators can use a site collection health checker to detect any potential issues with their site collections and address them before they upgrade sites to the new version. The checker is available after upgrade also to detect any health issues on an ongoing basis. Note that some issues can be repaired automatically, but others require manual steps to repair. During a site collection upgrade, if the checker finds issues that can be repaired automatically, they are repaired at that time. For more information, see [Run site collection health checks in SharePoint 2013](/SharePoint/sharepoint-server).
  
## Upgrade evaluation site collections
<a name="EvalSites"> </a>

In SharePoint 2013, the upgrade of the software and data was separated from the upgrade of the site. This means that the sites can truly remain running in SharePoint 2010 mode until a site owner or administrator explicitly upgrades the site to the new user interface. Site collection owners can request an evaluation site, which is a separate copy of the site, to review the new interface and functionality. After they have reviewed the site and made necessary changes in their original site, they can then upgrade their sites to the new version. Evaluation sites are set to automatically expire and be deleted. For more information, see [Plan for site collection upgrades in SharePoint 2013](/previous-versions/office/sharepoint-server-2010/ff191199(v=office.14)#EvalSites), [Upgrade a site collection](upgrade-a-site-collection.md), and [Manage site collection upgrades (SharePoint 2013 Products)](/SharePoint/upgrade-and-update/manage-site-collection-upgrades-to-sharepoint-2013).
  
## Notifications for life-cycle events
<a name="Notifications"> </a>

An email message and a status bar notification in a site collection notifies site collection owners when an upgrade is available. Site collection owners can create an evaluation site from email and control the expiration and deletion of that site by using email also. A status bar notification in the site collection also informs all users if a site is in read-only mode. For more information, see [Plan for site collection upgrades in SharePoint 2013](/previous-versions/office/sharepoint-server-2010/ff191199(v=office.14)#Notifications) and [Manage site collection upgrades (SharePoint 2013 Products)](/SharePoint/upgrade-and-update/manage-site-collection-upgrades-to-sharepoint-2013).
  
## Throttles for site collection upgrade
<a name="Notifications"> </a>

To make sure that site collection upgrades do not cause an outage on your farm, there are throttles built in at the web application, database, and content level. This means that even if 100 site collection owners decide to upgrade their site collections at the same time, only some are run at the same time, and the rest are put into a queue to run later. For more information, see [Plan for site collection upgrades in SharePoint 2013](/previous-versions/office/sharepoint-server-2010/ff191199(v=office.14)#Throttling) and [Manage site collection upgrades (SharePoint 2013 Products)](/SharePoint/upgrade-and-update/manage-site-collection-upgrades-to-sharepoint-2013).
  
## True "SharePoint 2010" instead of visual upgrade
<a name="SiteMode"> </a>

Visual upgrade in SharePoint 2010 Products lets site owners and administrators see what their site would be like in the new user interface. However, it is not a true preview because the site itself has already been upgraded to the new functionality. Consequently, some Web Parts or other elements do not display correctly.
  
SharePoint 2013 can host sites in both SharePoint 2010 and SharePoint 2013 modes. The installation contains both SharePoint 2010 and SharePoint 2013 versions of the following types of elements:
  
- Features, site templates, site definitions, and Web Parts
    
    The directories on the file system are duplicated in both the 14 and 15 paths, for example:
    
  - Web Server Extensions/14/TEMPLATE/Features 
    
  - Web Server Extensions/15/TEMPLATE/Features
    
- IIS support directories:
    
  - _Layouts, _Layouts/15
    
  - _ControlTemplates, _ControlTemplates/15
    
- Solution deployment, which lets legacy solutions work in 2010 mode
    
    Note that existing SharePoint 2010 Products solutions can be deployed to SharePoint 2013 and continue to function for 2010 sites, usually without requiring any changes. 
    
Because of these directories, you can continue hosting unupgraded sites in an upgraded environment until all site collections are ready to upgrade. For more information, see [Plan for site collection upgrades in SharePoint 2013](/previous-versions/office/sharepoint-server-2010/ff191199(v=office.14)#SiteModes).
  
## Log files now in ULS format
<a name="SiteMode"> </a>

The format of the upgrade, upgrade error, and site upgrade log files now comply with the Unified Logging System (ULS) conventions for easier review. For more information, see [Verify database upgrades in SharePoint 2013](verify-upgrade.md).
  

